# -*- coding: utf-8 -*-
import xlrd, xlwt, getpass
from NID import get_NID_detail

rdxls = xlrd.open_workbook("example.xlsx").sheets()[0] #放讀取路徑
nrows = rdxls.nrows
wb =  xlwt.Workbook()
sh = wb.add_sheet('name',cell_overwrite_ok=True)

username = input('請輸入學號:')
password = getpass.getpass('請輸入密碼:')

for i in range(nrows):
	nid_input = rdxls.cell(i,0).value
	result = get_NID_detail(username, password, nid_input)
	sh.write(i, 0, result['學號'])
	sh.write(i, 1, result['系級'])
	sh.write(i, 2, result['姓名'])
	sh.write(i, 3, result['性別'])
	sh.write(i, 4, result['出生年月日'])
	wb.save('ouput.xls')#放輸出路徑

print('查詢完畢!!!')