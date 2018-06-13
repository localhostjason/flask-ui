# coding: utf-8
from flask import render_template, redirect, url_for, abort, request, flash, jsonify
from flask_login import login_user, current_user, login_required, logout_user
from . import auth
from .forms import *
from ..base import Check


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    Check(form).check_validate_on_submit()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            current_user.update_time_ip()
            return redirect(request.args.get('next') or url_for('main.index'))
        flash({'errors': '用户名或者密码错误！'})

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
