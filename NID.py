# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import os


def get_NID_detail(username, password, nid):
     s = requests.Session()
     try:
          login = s.get("http://infocenter.fcu.edu.tw/assoc/assoc_login.jsp", timeout=3)
     except:
          print('未使用校內網路')
          os._exit(0)

     loginData = {
          'asn_code': 'A66',  # 社團代號
          'auserid': username,  # 帳號
          'apwd': password # 密碼
     }

     login = s.post('http://infocenter.fcu.edu.tw/assoc/authenticate.jsp', data=loginData)

     searchData = {
          'stuid': nid,  # 學號
          'idButton': '送出'
     }

     searchPage = s.post('http://infocenter.fcu.edu.tw/assoc/assoc30.jsp', data=searchData)

     bs_searchPage = BeautifulSoup(searchPage.text, "html.parser")  # 分析查詢頁面

     if re.search('抱歉, 資料不存在!', bs_searchPage.get_text(strip=True)):
          d = {'學號': nid, '系級': '查無資料', '姓名': '查無資料', '性別': '查無資料', '出生年月日': '查無資料'}
          return d
     else:
          result = bs_searchPage.select("table.tableStyle td.tableContentLeft")

          # re.sub('\s','',str(i)) 去掉空白
          newResult = []

          for i in result:
               newResult.append(re.search('>(.*)<', re.sub('\s', '', str(i))).group(1))

          d = {'學號': newResult[0], '系級': newResult[1], '姓名': newResult[2], '性別': newResult[3], '出生年月日': newResult[4]}
          return d

if __name__ == '__main__':
     import getpass
     username = input('請輸入學號:')
     password = getpass.getpass('請輸入密碼:')
     nid = input('請輸入欲查詢學號:')
     result = get_NID_detail(username, password, nid)
     print('學號: ' + result['學號'])
     print('系級: ' + result['系級'])
     print('姓名: ' + result['姓名'])
     print('性別: ' + result['性別'])
     print('出生年月日:' + result['出生年月日'])