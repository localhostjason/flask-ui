# coding: utf-8
from flask import render_template, redirect, url_for, jsonify, abort, request, flash
from flask_login import login_required

from . import main


@main.route('/main')
@main.route('/')
@login_required
def index():
    return render_template('main/index.html')


@main.route('/menu')
@login_required
def menu_list():
    return render_template('main/menu.html')
