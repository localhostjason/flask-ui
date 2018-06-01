# coding: utf-8
from flask import render_template, redirect, url_for, jsonify, abort, request, flash, current_app
from flask_login import login_required

from . import main
from .forms import *
from ..base import Check
from ..app import upload_files
from config import Config
import os
from datetime import datetime


@main.route('/main')
@main.route('/')
@login_required
def index():
    return render_template('main/index.html')


@main.route('/menu', methods=['GET', 'POST'])
@login_required
def menu_list():
    form = FileForm()

    Check(form).check_validate_on_submit()
    if form.validate_on_submit():
        upload_files_path = os.path.join(Config.UPLOADS_DEFAULT_DEST, datetime.now().strftime('%Y%m%d'))

        filename = upload_files.save(form.file.data, folder=upload_files_path, name=form.file.data.filename)
        file_url = upload_files.url(filename)
        print('filename', filename)
        print('file_url', file_url)

        # file_path = upload_files.path(filename)
        # os.remove(file_path)
        # print(file_path)
        return render_template('main/menu.html', form=form, filename=filename)

    return render_template('main/menu.html', form=form)
