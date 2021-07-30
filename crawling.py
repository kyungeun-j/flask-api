import requests
from bs4 import BeautifulSoup 
import json
from collections import OrderedDict

# HTTP GET Request
req = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=').text
soup = BeautifulSoup(req, 'html.parser')

selector = soup.select('#content > div > div.caseTable > div')

title = ["covid_positive", "quarantine_release", "quarantine", "death"]
sub_title = ["small_total", "from_korea", "from_hello"]

TodayCount = OrderedDict()
for i, t in zip(selector, title):
    mainObj = OrderedDict()
    for j in i.select('ul > li:nth-child(1)'):
        if j.select_one('.ca_subtit') != None and j.select_one('.ca_value') != None:
            mainObj['total'] = j.select_one('.ca_value').string
    
    for j in i.select('ul > li:nth-child(2) > dl'):
        if j.select_one('.sum') != None:
            subObj = OrderedDict()
            for k, st in zip(j.select('dd > ul > li'), sub_title):
                subObj[st] = k.select_one('.inner_value').string
            mainObj['diff_yesterday'] = subObj
        if j.select_one('.txt_ntc') != None:
            mainObj['diff_yesterday'] = j.select_one('.txt_ntc').string
    TodayCount[t] = mainObj
print('TodayCount', json.dumps(TodayCount, ensure_ascii=False, indent="\t") )


selector2 = soup.select('#content > div > div:nth-child(17) > table > tbody > tr')
DailyCount = OrderedDict()
for i,j in enumerate(selector2):
    dayObj = OrderedDict()
    dayObj['date'] = j.select_one('td:nth-child(1)').string
    dayObj['total'] = j.select_one('td:nth-child(3)').string
    DailyCount[i] = dayObj
print('DailyCount', json.dumps(DailyCount, ensure_ascii=False, indent="\t") )