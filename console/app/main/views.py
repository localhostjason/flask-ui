# coding: utf-8
from flask import render_template, redirect, url_for, jsonify, abort, request, flash
from flask_login import login_required

from . import main


@main.route('/main')
@main.route('/')
@login_required
def dashboard():
    return render_template('main/main.html')


@main.route('/test')
@login_required
def test():
    return render_template('main/test.html')
