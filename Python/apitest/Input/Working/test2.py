import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import datetime as dt2

#공매도
#a : 공매도테이블을 json으로 변환한것
# enddate : 오늘날짜, startdate : 20일 전 날짜
#date : 날짜, count : 잔여수량, money : 잔여 금액
def gong():
    enddate = dt.today()
    Senddate = enddate.strftime("%Y%m%d")
    startdate = enddate - dt2.timedelta(days=20)
    Sstartdate = startdate.strftime("%Y%m%d")
    url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd?bld=dbms/MDC/STAT/srt/MDCSTAT30001&tboxisuCd_finder_srtisu0_0=019210%2F%EC%99%80%EC%9D%B4%EC%A7%80-%EC%9B%90&isuCd=KR7019210004&isuCd2=KR7019210004&codeNmisuCd_finder_srtisu0_0=%EC%99%80%EC%9D%B4%EC%A7%80-%EC%9B%90&param1isuCd_finder_srtisu0_0=&strtDd="+Sstartdate+ "&endDd="+Senddate+"&share=1&money=1&csvxls_isNo=false"
    req = requests.get(url)
    a = req.json()["OutBlock_1"]
    for i in a:
        if i["STR_CONST_VAL1"] != "-":
            date = i["TRD_DD"]
            count = i["STR_CONST_VAL1"]
            money = i["STR_CONST_VAL2"]
            break
    result = date+"~~~"+count+"~~~"+money
    
  
    print(result)
    return result