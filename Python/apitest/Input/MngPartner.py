import datetime
from dateutil.relativedelta import relativedelta
import requests
import clipboard
import time

import json
from requests_toolbelt import MultipartEncoder
from bs4 import BeautifulSoup as bs
import re, os, sys

from configparser import ConfigParser

from collections.abc import Iterator
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

import pymssql
import xmltodict

now = datetime.datetime.now() # 현재시간

''' 
    Used External Library
        - requests
        - clipboard
        - requests-toolbelt
        - bs4 (Beautiful Soup4)
        - pymssql
'''

# _lock = Lock() # Thread Lock을 방지하기 위한 Global Lock 생성

###################################################### assign
config_path=os.path.join(os.path.dirname(__file__),"PythonConfigFile.txt")

List_threads = []

elv_no_list = []


###################################################### 작업대상 파일 분류
# PROD
elv_udt_path = sys.argv[1] # ex) elvUdtList_Sch_ConPass.txt, elvUdtList_Sch_Fail.txt ...
# elv_udt_path = r"C:\RPA_Working\HDEL\ServiceMgmt\P60003_PartnerManagement\Input\elevatorNoList.txt"
# elv_udt_path = r'C:\Users\Administrator\Desktop\협력사관리\Input\elvUdtList_Sch_Fail.txt'
# elv_udt_path = r'C:\Users\Administrator\Desktop\새 폴더\협력사관리\Input\test.txt'
# elv_udt_path = r'C:\Study\Python\apitest\Input\elevatorNoList.txt'

authToken = ""
folderPath = ""
######################################################
config = ConfigParser(interpolation=None)
_ = config
_.read(config_path)

folder_path_fir = _.get('Var','folder_path_fir') # Working
# folder_path_sec = _.get('Var','folder_path_sec') # Working2
# folder_path_thi = _.get('Var','folder_path_thi') # Working3


# sheet_name = _.get('Var','sheet_name')

output_folder_path = _.get('Var','output_folder_path')

serviceKey = _.get('Var','serviceKey')

dateList=[]
for i in range(0,3):
    temp = now - relativedelta(months= i)
    dateList.append(temp.strftime('%Y%m'))

#PROD
log_file_name = _.get('Var','log_file_name') + '.txt'

input_folder_path = _.get('Var','input_folder_path')

# DB Session Open
conn = pymssql.connect(host="10.31.1.192:1433", user='server_talk', password='Guseo!23', database= 'MIData')
cursor = conn.cursor(as_dict=True)
cursor.execute("SELECT elevatorNo, elvtrMgtNo1 + ',' + elvtrMgtNo2 as elvtrMgtNo, mntCpnyNm, subcntrCpny FROM ElvList")
elvtrMgtNoList = cursor.fetchall()

# excel_row_cnt = 1
######################################################

def getElvNoList(elv_udt_path): # Thread Pool을 생성하기 위해 List 변수 생성
    with open(elv_udt_path,'r') as f:
        lines = f.readlines()
        del lines[0]
        lines.sort()

    for line in lines:
        elv_no = line.strip()
        if elv_no == '':
            continue
        elv_no_list.append(elv_no)
    return elv_no_list

elv_no_list = getElvNoList(elv_udt_path)

total_cnt = len(elv_no_list)


# floor_total_cnt = total_cnt/3 # 3으로 나눠서 폴더에 저장
# floor_total_cnt = math.floor(floor_total_cnt)

class RateLimiter(Iterator): # 동시에 여러개의 Thread를 통해 데이터를 요청하면 서버에서 거부당하기 때문에, GLobal Delay를 설정
    """Iterator that yields a value at most once every 'interval' seconds."""
    def __init__(self, interval):
        self.lock = Lock()
        self.interval = interval
        self.next_yield = 0

    def __next__(self):
        with self.lock:
            t = time.monotonic()
            if t < self.next_yield:
                time.sleep(self.next_yield - t)
                t = time.monotonic()
            self.next_yield = t + self.interval

api_rate_limiter = RateLimiter(0.2) # API Request 전에, 이미 요청중인 Thread가 있다면 0.2초 대기
delay_limiter = RateLimiter(1) # API Request 오류 발생시, 5초 대기

def append_txt(result, folder_path, file_name):
    try:
        f = open(folder_path + "\\" + file_name,'a', encoding='UTF-8')
        f.write(result + '\n')
        f.close()
    except Exception as e:
        print(e)


def PostForm(url, headers, field_data): # Post Parameter의 형식이 MultipartForm 일 때, Wrapping해주는 Function
    try:
        m = MultipartEncoder(fields=field_data)
        headers = {'Content-Type' : m.content_type}
        res = requests.post(url, headers=headers, data=m,timeout=5)
        res.raise_for_status()
        return res
    except Exception as e:
        return 'X'

class PartnerManagement():
    def __init__(self, id, elvNo, working) -> None:
        self.id = id # Thread 구분을 위한 ID
        self.flag = False
        self.timeOut=10 # API Timeout
        self.tar = {}
        self.working = working # 결과 파일을 저장할 폴더경로
        self.elvNo = str(elvNo) # ElevatorNo
        self.cnt = ""
        self.main()

    def getAuthTok(self): # 승강기 정보센터에서 사용할 인증키 추출
        global authToken # Thread 중 하나라도 인증키 값 추출에 성공했다면 공유하며 사용
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.headers['Referer'] = 'https://www.elevator.go.kr/'
        tokPath = rf"{input_folder_path}\authToken.txt"
        self.tokPath = tokPath
        if 'authToken' in globals() and len(authToken) >= 3:
            pass
        elif os.path.exists(tokPath):
            _.read(tokPath)
            authToken = _.get('Var','authToken')
        else:
            self.rqstAuthTok() # 아직 아무도 인증키를 추출하지 못했다면, 인증키 생성
            
    def rqstAuthTok(self): # 실제 인증키를 생성하는 Module
        try:
            tokPath = self.tokPath
            # url = "https://www.elevator.go.kr/js/fsp.js"
            url = "https://www.elevator.go.kr/js/elev/fsp.js"
            res = requests.get(url,timeout=self.timeOut)
            s = res.text
            s = s[s.find("AuthToken")+len("AuthToken"):s.find("url")].strip()
            authToken = s[s.find(':"')+len(':"'):s.find('",')+1].strip().replace('"','')
            with open(tokPath,'w') as f:
                f.write("[Var]\n")
                f.write(f"authToken={authToken}")
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log = f"{exc_type}, {fname}, {exc_tb.tb_lineno}, {str(e)}"
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)
            append_txt(result=log,folder_path=output_folder_path,file_name=log_file_name)
            self.sucFlag = 'X'

    

    def getDBData(self): # 국가 승강기 정보센터의 대상 데이터를 조회할 때 사용할 키 값 mng1, mng2 추출
        try:
            # 승강기정보센터 api 변경으로 기존 로직 사용 불가하여 현대엘리베이터 DB에서 mng1, mng2 값 받아오도록 변경

            # headers = self.headers
            # payload = {'searchElvtrNo': self.elvNo}
            # headers['Content-Type'] = 'application/x-www-form-urlencoded'
            # url = 'https://www.elevator.go.kr/com/ElvtrNumAddrL01.do'
            # s = PostForm(url, headers, payload).text
            # if s == 'X':
            #     raise "authToken 생성 실패"
            # soup = bs(s, "html.parser")

            # elements = soup.select("td.txt_center > a[style='color:blue;']")[0]['onclick']
            # s = elements[elements.find("fnElvtrDetail")+len("fnElvtrDetail"):elements.find(";")]
            # mng1 = s.split(",")[0].replace("(","")[1:-1]
            # mng2 = s.split(",")[1][1:-1]

            # self.mng1 = mng1
            # self.mng2 = mng2
            row = next(item for item in elvtrMgtNoList if item['elevatorNo'] == self.elvNo)
            self.mng1, self.mng2, self.mntCpnyNm, self.subcntrCpny = row["elvtrMgtNo"].split(",")[0], row["elvtrMgtNo"].split(",")[1], row['mntCpnyNm'], row['subcntrCpny']
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log = f"{exc_type}, {fname}, {exc_tb.tb_lineno}, {str(e)}"
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)
            append_txt(result=log,folder_path=output_folder_path,file_name=log_file_name)
            self.sucFlag = 'X'

    # def getMntCpnyNm(self):
    #     try:
    #         headers = self.headers
    #         headers['Content-Type'] = 'application/x-www-form-urlencoded'
    #         payload = {'elevatorNo' : self.elvNo,
    #                    'elvtrMgtNo1' : self.mng1,
    #                    'elvtrMgtNo2' : self.mng2}
    #         url = 'https://www.elevator.go.kr/com/ElvtrDetail.do'
    #         s = re.sub(r',\s*]}', ']}', re.sub(r'[\n\r\t]','', PostForm(url, headers, payload).text))
    #         if s == 'X':
    #             raise "유지관리업체 조회실패"
    #         d = json.loads(s)['data']
    #         self.mntCpnyNm = d['mntCpnyNm']
    #         self.subcntrCpny = d['subcntrCpny']
    #     except Exception as e:
    #         exc_type, exc_obj, exc_tb = sys.exc_info()
    #         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #         log = f"{exc_type}, {fname}, {exc_tb.tb_lineno}, {str(e)}"
    #         print(exc_type, fname, exc_tb.tb_lineno)
    #         print(e)
    #         append_txt(result=log,folder_path=output_folder_path,file_name=log_file_name)
    #         self.sucFlag = 'X'

    def getInscptHist(self):
        try:
            headers = self.headers
            headers['Content-Type'] = 'application/json; charset=UTF-8'
            payload = {"Cmd":"E","AuthToken":authToken,"SvcID":"inspctHist","ds_cond":{"elvtrMgtNo1":self.mng1,"elvtrMgtNo2":self.mng2, "elevatorNo" : self.elvNo},"person_no":""}
            url = 'https://data.koelsa.or.kr/opensql/opensql'
            res = requests.post(url,headers=headers,data=json.dumps(payload))
            s = res.json()['ds_list']
            if len(s) > 0:
                self.inscptKind = s[0]['INSPCT_KIND']
                self.inscptDt = s[0]['INSPCT_DT']
                self.applcBeDt = s[0]['APPLC_BE_DT']
                self.applcEnDt = s[0]['APPLC_EN_DT']
            else:
                self.inscptKind = "NULL"
                self.inscptDt = "NULL"
                self.applcBeDt = "NULL"
                self.applcEnDt = "NULL"
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log = f"{exc_type}, {fname}, {exc_tb.tb_lineno}, {str(e)}"
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)
            append_txt(result=log,folder_path=output_folder_path,file_name=log_file_name)
            self.sucFlag = 'X'

    def getSelChk(self):
        try:
            self.selChkList = []
            headers = self.headers
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            # payload = {'elevatorNo' : self.elvNo,
            #            'elvtrMgtNo1' : self.mng1,
            #            'elvtrMgtNo2' : self.mng2}
            # url = 'https://www.elevator.go.kr/com/selectSelchkList.do'
            # res = PostForm(url, headers, payload)
            for ym in dateList:
                url = rf"http://openapi.elevator.go.kr/openapi/service/ElevatorSelfCheckService/getSelfCheckList?serviceKey={serviceKey}&pageNo=1&numOfRows=1&yyyymm={ym}&elevator_no={self.elvNo}"
                res = requests.get(url)
                json_data = xmltodict.parse(res.text)
                if json_data['response']['body']['totalCount'] != '0':
                    self.selChkList.append(json_data['response']['body']['items']['item'])
            # if res == 'X':
            #     raise "자체점검이력 조회실패"
            # s = res.text
            # fixed_json_string = re.sub(r',\s*]}', ']}', re.sub(r'[\n\r\t]','', s))
            # l = json.loads(fixed_json_string)['data']
            # if len(l) > 3:
            #     selChkList = l[:3]
            # else:
            #     selChkList = l
            # self.selChkList = selChkList
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log = f"{exc_type}, {fname}, {exc_tb.tb_lineno}, {str(e)}"
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)
            append_txt(result=log,folder_path=output_folder_path,file_name=log_file_name)
            self.sucFlag = 'X'

    def WriteToFile(self):
        ELEVATORNO = "NULL"
        MNTCPNYNM = "NULL"
        SUBCNTRCPNY = "NULL"
        SELFINSCPTM3DE = "NULL"
        SELFINSCPTM3CPNYNM = "NULL"
        SELFINSCPTM2DE = "NULL"
        SELFINSCPTM2CPNYNM = "NULL"
        SELFINSCPTM1DE = "NULL"
        SELFINSCPTM1CPNYNM = "NULL"

        inscptKIND = self.inscptKind
        inscptDT = self.inscptDt
        APPLCBEDT = self.applcBeDt
        APPLCENDT = self.applcEnDt
        
        ELEVATORNO = self.elvNo
        MNTCPNYNM = str(self.mntCpnyNm).encode('ISO-8859-1').decode('cp949')
        SUBCNTRCPNY = str(self.subcntrCpny).encode('ISO-8859-1').decode('cp949')

        selChkList = self.selChkList
        for i, item in enumerate(selChkList):
            if i == 0:
                SELFINSCPTM1CPNYNM = item['companyNm']
                SELFINSCPTM1DE = item['selchkBeginDate'][:6]
            elif i == 1:
                SELFINSCPTM2CPNYNM = item['companyNm']
                SELFINSCPTM2DE = item['selchkBeginDate'][:6]
            elif i == 2:
                SELFINSCPTM3CPNYNM = item['companyNm']
                SELFINSCPTM3DE = item['selchkBeginDate'][:6]
            else:
                break
        
        filePath = rf"{self.working}\{self.elvNo}.txt"
        with open(filePath,'w',encoding='utf8') as f:
            f.write(f"elevatorNo={ELEVATORNO}\n")
            f.write(f"mntCpnyNm={MNTCPNYNM}\n")
            f.write(f"subcntrCpny={SUBCNTRCPNY}\n")
            f.write(f"inscptKind={inscptKIND}\n")
            f.write(f"inscptDt={inscptDT}\n")
            f.write(f"applcBeDt={APPLCBEDT}\n")
            f.write(f"applcEnDt={APPLCENDT}\n")
            f.write(f"selfInscptM3De={SELFINSCPTM3DE}\n")
            f.write(f"selfInscptM3CpnyNm={SELFINSCPTM3CPNYNM}\n")
            f.write(f"selfInscptM2De={SELFINSCPTM2DE}\n")
            f.write(f"selfInscptM2CpnyNm={SELFINSCPTM2CPNYNM}\n")
            f.write(f"selfInscptM1De={SELFINSCPTM1DE}\n")
            f.write(f"selfInscptM1CpnyNm={SELFINSCPTM1CPNYNM}\n")

    def WriteNoData(self):
        ELEVATORNO = "NULL"
        ELEVATORNO = self.elvNo

        filePath = rf"{self.working}\{self.elvNo}.txt"
        with open(filePath,'w',encoding='utf8') as f:
            f.write(f"elevatorNo={ELEVATORNO}\n")
            f.write(f"mntCpnyNm=수정필요\n")
            f.write(f"subcntrCpny=수정필요\n")
            f.write(f"inscptKind=수정필요\n")
            f.write(f"inscptDt=수정필요\n")
            f.write(f"applcBeDt=수정필요\n")
            f.write(f"applcEnDt=수정필요\n")
            f.write(f"selfInscptM3De=수정필요\n")
            f.write(f"selfInscptM3CpnyNm=수정필요\n")
            f.write(f"selfInscptM2De=수정필요\n")
            f.write(f"selfInscptM2CpnyNm=수정필요\n")
            f.write(f"selfInscptM1De=수정필요\n")
            f.write(f"selfInscptM1CpnyNm=수정필요\n")

    def main(self):
        # global excel_row_cnt
        start = time.time()
        for i in range(3):
            try:
                self.sucFlag = ""
                self.getAuthTok()
                if self.sucFlag == 'X':
                    raise Exception('Token 생성 실패')

                self.getDBData()
                if self.sucFlag == 'X':
                    if i == 4:
                        self.WriteNoData()
                        break
                    raise Exception('MngNo, mntCpnyNm, subcntrCpny 추출 실패')
                if self.sucFlag == 'X':
                    raise Exception('점검업체 코드 추출 API 조회 실패')
                
                self.getInscptHist()
                if self.sucFlag == 'X':
                    raise Exception('검사이력 API 조회 실패')
                
                self.getSelChk()
                if self.sucFlag == 'X':
                    raise Exception('자체점검 API 조회 실패')

                self.WriteToFile()

            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                log = f"elvNo: {self.elvNo}, {exc_type}, {fname}, {exc_tb.tb_lineno}, {str(e)}"
                append_txt(result=log,folder_path=output_folder_path,file_name=log_file_name)
                print(log)
                self.sucFlag = 'X'
                next(delay_limiter)
            finally:
                if self.sucFlag != "X":
                    self.cnt = i+1
                    break
        self.taken_time = time.time() - start  # api 호출 끝난 시간

if not os.path.isdir(folder_path_fir):
    os.makedirs(folder_path_fir)
# if not os.path.isdir(folder_path_sec):
#     os.makedirs(folder_path_sec)
# if not os.path.isdir(folder_path_thi):
#     os.makedirs(folder_path_thi)





def work_function(id, elvNo,folderPath):
    # next(api_rate_limiter)
    PartnerManagement(id, elvNo,folderPath)

# folderPath = folder_path_fir
# for i, elv_no in enumerate(elv_no_list):
#     work_function(i,elv_no,folderPath)

# exit()

with ThreadPoolExecutor() as executor:
    for i, elv_no in enumerate(elv_no_list):
        folderPath = folder_path_fir
        # if i <= floor_total_cnt:
        #     folderPath = folder_path_fir
        # elif i <= floor_total_cnt*2:
        #     folderPath = folder_path_sec
        # else:
            # folderPath = folder_path_thi
        executor.submit(work_function, i, elv_no, folderPath)

# Finish log
with open(rf"{input_folder_path}\finish.txt",'w') as f:
    f.write(str(datetime.datetime.now() - now)[:11])
msg = "finish"
print(msg)
clipboard.copy(msg)