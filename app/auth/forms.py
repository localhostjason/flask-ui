# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from ..models import User
from ..base import BaseForm


class LoginForm(FlaskForm, BaseForm):
    username = StringField(validators=[DataRequired(message='用户名不能为空！')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空！')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

    def __init__(self):
        super(LoginForm, self).__init__()
        render_kw_dict = {
            'username': {'placeholder': '帐号名'},
            'password': {'placeholder': '登录密码'},
        }
        self.required_form(**render_kw_dict)
