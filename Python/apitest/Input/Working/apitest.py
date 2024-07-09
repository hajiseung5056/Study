import requests

# 요청 URL
url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"

# 페이로드
payload = {
    'bld': 'dbms/MDC/STAT/srt/MDCSTAT30001',
    'tboxisuCd_finder_srtisu0_0' : '019210%2F%EC%99%80%EC%9D%B4%EC%A7%80-%EC%9B%90',
    'isuCd': 'KR7019210004',
    'isuCd2': 'KR7019210004',
    'codeNmisuCd_finder_srtisu0_0': '%EC%99%80%EC%9D%B4%EC%A7%80-%EC%9B%90',
    'param1isuCd_finder_srtisu0_0': "",
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

# POST 요청 보내기
response = requests.post(url, data=payload, headers=headers)

# 응답 JSON 파싱
data = response.json()

# 확인을 위해 응답 데이터 출력
print(data)