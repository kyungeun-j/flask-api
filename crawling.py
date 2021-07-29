import requests
import pprint

from bs4 import BeautifulSoup 

# HTTP GET Request
req = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=').text
soup = BeautifulSoup(req, 'html.parser')

selector = soup.select('#content > div > div.caseTable > div')

arr = []
for i in selector:
    obj = {}
    obj['ct'] = i.select_one('.ca_top').string

    for j in i.select('ul > li:nth-child(1)'):
        obj2 = {}
        if j.select_one('.ca_subtit') != None and j.select_one('.ca_value') != None:
            obj2['cs'] = j.select_one('.ca_subtit').string
            obj2['cv'] = j.select_one('.ca_value').string
            obj['cc'] = obj2
    
    arr3 = []
    for j in i.select('ul > li:nth-child(2) > dl'):
        # print(j)
        obj3 = {}
        if j.select_one('.ca_subtit') != None:
            obj3['cs'] = j.select_one('.ca_subtit').string
        if j.select_one('.sum') != None:
            arr4 = []
            for k in j.select('dd > ul > li'):
                obj4 = {}
                obj4['it'] = k.select_one('.inner_tit').string
                obj4['iv'] = k.select_one('.inner_value').string
                arr4.append(obj4)
                obj3['ii'] = arr4
        if j.select_one('.txt_ntc') != None:
            obj3['tn'] = j.select_one('.txt_ntc').string
        arr3.append(obj3)
        obj['ci'] = arr3
        
        # print(obj3)
    arr.append(obj)
pprint.pprint(arr)