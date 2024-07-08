import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import datetime as dt2

#공매도
#a : 공매도테이블을 json으로 변환한것
# enddate : 오늘날짜, startdate : 20일 전 날짜
#date : 날짜, count : 잔여수량, money : 잔여 금액
def gong():
    print("hello")
    enddate = dt.today()
    Senddate = enddate.strftime("%Y%m%d")
    startdate = enddate - dt2.timedelta(days=20)
    Sstartdate = startdate.strftime("%Y%m%d")
    url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"

    # 페이로드
    payload = {
        'bld': 'dbms/MDC/STAT/srt/MDCSTAT30201',
        'locale': 'ko_KR',
        'indTpCd': '1',
        'mktTpCd': '1',
        'indAggClssCd': '001',
        'idxIndCd': '001',
        'strtDd': '20240607',
        'endDd': '20240708',
        'share': '1',
        'money': '1',
        'csvxls_isNo': 'false'
    }

    # 헤더
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '__smVisitorID=sl56KUy-r51; JSESSIONID=PvLENz4RkJFeyw9bbkF2TBmoan0uM9LMRUZj4zySz8ZVOmqtzHbYl5MahjRGMXF9.bWRjX2RvbWFpbi9tZGNvd2FwMS1tZGNhcHAwMQ==',
        'Host': 'data.krx.co.kr',
        'Origin': 'http://data.krx.co.kr',
        'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0203',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    req = requests.post(url, data=payload, headers=headers)
    
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

gong()
