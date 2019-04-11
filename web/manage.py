#!/usr/bin/env python3
from flask import Flask, render_template, flash, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_bootstrap import Bootstrap

# get nid
import requests
from bs4 import BeautifulSoup
import re

# excel
from openpyxl import load_workbook, Workbook
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
from tempfile import NamedTemporaryFile
from io import BytesIO
import os

# chart
from pyecharts import Bar

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
app.config['UPLOAD_FOLDER'] = "hard to guess string"
bootstrap = Bootstrap(app)

class SingleForm(FlaskForm):
    username = StringField('學號', validators=[DataRequired()])
    password = PasswordField('密碼', validators=[DataRequired()])
    nid = StringField('欲查詢學號', validators=[DataRequired()])
    submit = SubmitField("Submit")

class MultiForm(FlaskForm):
    username = StringField('學號', validators=[DataRequired()])
    password = PasswordField('密碼', validators=[DataRequired()])
    file = FileField(validators=[FileRequired(), FileAllowed(['xlsx'], 'xlsx Only!')])
    submit = SubmitField("Submit")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/single", methods=['GET','POST'])
def single():
    form = SingleForm()
    if form.validate_on_submit():
        s = requests.Session()
        # 檢查網路狀態
        try:
          login = s.get("http://infocenter.fcu.edu.tw/assoc/assoc_login.jsp", timeout=3)
        except:
            flash('未使用校內網路', 'error')
        loginData = {
          'asn_code': 'A66',  # 社團代號
          'auserid': form.username.data,  # 帳號
          'apwd': form.password.data # 密碼
        }
        login = s.post('http://infocenter.fcu.edu.tw/assoc/authenticate.jsp', data=loginData)
        bs_loginPage = BeautifulSoup(login.text, "html.parser").get_text(strip=True)  # 分析登入頁面
        if re.search('對不起!!您的帳號/密碼有誤!!', bs_loginPage):
            flash('密碼輸入錯誤!', 'error')
        elif re.search('對不起!!您無權進入系統!', bs_loginPage):
            flash('帳號密碼輸入錯誤!', 'error')
        searchData = {
          'stuid': form.nid.data,  # 學號
          'idButton': '送出'
        }
        searchPage = s.post('http://infocenter.fcu.edu.tw/assoc/assoc30.jsp', data=searchData)
        bs_searchPage = BeautifulSoup(searchPage.text, "html.parser")  # 分析查詢頁面
        if re.search('抱歉, 資料不存在!', bs_searchPage.get_text(strip=True)):
            result = {'學號': form.nid.data, '系級': '查無資料', '姓名': '查無資料', '性別': '查無資料', '出生年月日': '查無資料'}
        else:
            result = bs_searchPage.select("table.tableStyle td.tableContentLeft")
            newResult = []
            for i in result:
                newResult.append(re.search(r'>(.*)<', re.sub(r'\s', '', str(i))).group(1))
            result = {'學號': newResult[0], '系級': newResult[1], '姓名': newResult[2], '性別': newResult[3], '出生年月日': newResult[4]}
        return render_template('single.html', form=form, result=result)
    return render_template('single.html', form=form)

@app.route("/chart")
def chart():
    bar = Bar("主標題", "副標題")
    bar.add("A", ["B", "C", "D", "E", "F", "G"], [5, 20, 36, 10, 75, 90])
    return render_template('chart.html', chart=bar.render_embed())

@app.route("/multi", methods=['GET','POST'])
def multi():
    form = MultiForm()
    if form.validate_on_submit():
        f = form.file.data
        f.save(f.filename)
        # 讀檔後放入 nidList
        nidList = []
        wb = load_workbook(f.filename, read_only=True)
        sheet = wb.active
        for row in sheet.rows:
            for cell in row:
                nidList.append(cell.value)
        # 獲取登入網頁
        s = requests.Session()
        try:
            login = s.get("http://infocenter.fcu.edu.tw/assoc/assoc_login.jsp", timeout=3)
        except:
            flash('未使用校內網路', 'error')
        # 登入
        loginData = {
            'asn_code': 'A66',  # 社團代號
            'auserid': form.username.data,  # 帳號
            'apwd': form.password.data  # 密碼
        }
        login = s.post('http://infocenter.fcu.edu.tw/assoc/authenticate.jsp', data=loginData)
        bs_loginPage = BeautifulSoup(login.text, "html.parser").get_text(strip=True)  # 分析登入頁面
        if re.search('對不起!!您的帳號/密碼有誤!!', bs_loginPage):
            flash('密碼輸入錯誤!', 'error')
        elif re.search('對不起!!您無權進入系統!', bs_loginPage):
            flash('帳號密碼輸入錯誤!', 'error')
        wb = Workbook()
        ws = wb.create_sheet('詳細資料', 0)
        for nid in nidList:
            searchData = {
                'stuid': nid, # 學號
                'idButton': '送出'
            }
            searchPage = s.post('http://infocenter.fcu.edu.tw/assoc/assoc30.jsp', data=searchData)
            bs_searchPage = BeautifulSoup(searchPage.text, "html.parser")  # 分析查詢頁面
            if re.search('抱歉, 資料不存在!', bs_searchPage.get_text(strip=True)):
                d = {'學號': nid, '系級': '查無資料', '姓名': '查無資料','性別': '查無資料', '出生年月日': '查無資料'}
            else:
                result = bs_searchPage.select("table.tableStyle td.tableContentLeft")
                newResult = []
                for i in result:
                    newResult.append(re.search(r'>(.*)<', re.sub(r'\s', '', str(i))).group(1))
                d = {'學號': newResult[0], '系級': newResult[1], '姓名': newResult[2], '性別': newResult[3], '出生年月日': newResult[4]}
            ws.append([d['學號'], d['系級'], d['姓名'], d['性別'], d['出生年月日']])
        with NamedTemporaryFile() as tmp:
            wb.save(tmp.name)
            tmp.seek(0)
            stream = tmp.read()
            return send_file(BytesIO(stream), attachment_filename='output.xlsx', as_attachment=True, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return render_template('multi.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
