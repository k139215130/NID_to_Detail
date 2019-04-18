from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class SingleForm(FlaskForm):
    username = StringField('學號', validators=[DataRequired()])
    password = PasswordField('密碼', validators=[DataRequired()])
    nid = StringField('欲查詢學號', validators=[DataRequired()])
    submit = SubmitField("Submit")

class MultiForm(FlaskForm):
    username = StringField('學號', validators=[DataRequired()])
    password = PasswordField('密碼', validators=[DataRequired()])
    file = FileField(validators=[FileRequired(), FileAllowed(['xlsx'], 'xlsx Only!')])
    store = BooleanField('是否將資料存置資料庫')
    name = StringField('名稱')
    submit = SubmitField("Submit")