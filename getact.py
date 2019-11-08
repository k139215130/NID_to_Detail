# -*- coding: utf-8 -*-
import getpass
import requests
from bs4 import BeautifulSoup
import re
import os
from openpyxl import Workbook

# 獲取登入網頁
s = requests.Session()
try:
	login = s.get("http://infocenter.fcu.edu.tw/assoc/assoc_login.jsp", timeout=3)
except:
	print('未使用校內網路')
	os._exit(0)

# 登入
code = input('請輸入社團代號:')
username = input('請輸入學號:')
password = getpass.getpass('請輸入密碼:')
year = input('請輸入學年度:')

loginData = {
	'asn_code': code,  # 社團代號
	'auserid': username,  # 帳號
	'apwd': password  # 密碼
}

login = s.post('http://infocenter.fcu.edu.tw/assoc/authenticate.jsp', data=loginData)

bs_loginPage = BeautifulSoup(login.text, "html.parser").get_text(strip=True)  # 分析登入頁面

if re.search('對不起!!您的帳號/密碼有誤!!', bs_loginPage):
	print('密碼輸入錯誤!')
	os._exit(0)
elif re.search('對不起!!您無權進入系統!', bs_loginPage):
	print('帳號密碼輸入錯誤!')
	os._exit(0)

print('登入成功!')
print('查詢中，請稍後')

actPage = s.get('http://infocenter.fcu.edu.tw/assoc/assoc23.jsp')
bs_actPage = BeautifulSoup(actPage.text, "html.parser")  # 分析活動頁面

searchData = {
    'selectYy': year, # 學年度
    'sent': bs_actPage.find("input", {"name": "sent"})['value']
}

actPage = s.post('http://infocenter.fcu.edu.tw/assoc/assoc23.jsp', data=searchData)
bs_actPage = BeautifulSoup(actPage.text, "html.parser")  # 分析活動頁面
sentValue = bs_actPage.find("input", {"name": "sent"})['value']

actList = bs_actPage.select("table.tableStyle")[0].select("tr")
actList.pop(0) #移除第一個元素

allData = []

for i in range(0, len(actList), 2):
    lst = actList[i].select("td.tableContent")
    title = lst[0].get_text(strip=True) #標題
    location = lst[1].get_text(strip=True) #地點
    tmpTime = lst[2].get_text(strip=True).split()
    cadreLink = lst[7].find("button")['name']
    memberLink = lst[8].find("button")['name']
    startDate = tmpTime[0] #開始日期
    startTime = tmpTime[1] #開始時間
    endDate = tmpTime[2][1:] #結束日期
    endTime = tmpTime[3] #結束時間

    data = {
        'selectYy': year, # 學年度
        cadreLink : '',
        'sent': sentValue
    }
    page = s.post('http://infocenter.fcu.edu.tw/assoc/assoc23.jsp', data=data)
    bs_page = BeautifulSoup(page.text, "html.parser")  # 分析活動頁面
    sentValue = bs_page.find("input", {"name": "sent"})['value']

    cadrePage = s.get('http://infocenter.fcu.edu.tw/assoc/assoc24.jsp')
    bs_cadrePage = BeautifulSoup(cadrePage.text, "html.parser")  # 分析工作人員頁面
    cadreItem = bs_cadrePage.select("table.tableStyle")[1].select("tr")
    cadreItem.pop(0) #移除第一個元素
    cadreList = []
    for i in cadreItem:
        cadreList.append(i.select('td.tableContent')[0].get_text(strip=True))


    data = {
        'selectYy': year, # 學年度
        memberLink : '',
        'sent': sentValue
    }
    page = s.post('http://infocenter.fcu.edu.tw/assoc/assoc23.jsp', data=data)
    bs_page = BeautifulSoup(page.text, "html.parser")  # 分析活動頁面
    sentValue = bs_page.find("input", {"name": "sent"})['value']

    memberPage = s.get('http://infocenter.fcu.edu.tw/assoc/assoc25.jsp')
    bs_memberPage = BeautifulSoup(memberPage.text, "html.parser")  # 分析參與者頁面
    memberItem = bs_memberPage.select("table.tableStyle")[1].select("tr")
    memberItem.pop(0) #移除第一個元素
    memberList = []
    for i in memberItem:
        memberList.append(i.select('td.tableContent')[0].get_text(strip=True))

    allData.append([title, location, startDate, startTime, endDate, endTime, cadreList, memberList])

print('資訊搜尋完畢')
print('建立資料夾中')
os.mkdir(year)
print('建立資料夾完畢')
os.chdir(year)
print('寫檔中')

for i in allData:
    wb = Workbook(write_only=True)

    ws1 = wb.create_sheet('詳細資料')
    ws1.append(['活動標題', i[0]])
    ws1.append(['活動地點', i[1]])
    ws1.append(['開始日期', i[2]])
    ws1.append(['開始時間', i[3]])
    ws1.append(['結束日期', i[4]])
    ws1.append(['結束時間', i[5]])

    ws2 = wb.create_sheet('工作人員名單')
    for j in i[6]:
        ws2.append([j])

    ws3 = wb.create_sheet('參與者名單')
    for j in i[7]:
        ws3.append([j])

    wb.save(i[0] + '.xlsx')

print(year + ' 學年度已匯出完成')
