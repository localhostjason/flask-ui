# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..base import BaseForm

from ..app import upload_files


class FileForm(FlaskForm, BaseForm):
    file = FileField('file', validators=[FileRequired('不允许为空'), FileAllowed(upload_files, '只允许文本文档')])
    submit = SubmitField('submit')
