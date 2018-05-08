# -*- coding:utf8 -*-
import os
import json


def read_config():
    path = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(path, 'config.json')
    with open(config_path, encoding='utf-8') as f:
        mysql_info = f.read()
        mysql_info = json.loads(mysql_info)
    mysql_dict = mysql_info['mysql']

    mysql_url = 'mysql://%s:%s@%s:%s/%s' % (
        mysql_dict['user'],
        mysql_dict['password'],
        mysql_dict['host'],
        mysql_dict['port'],
        mysql_dict['database']
    )
    return mysql_url


class Config:
    DEBUG = True
    # SECRET_KEY = os.urandom(24)
    SECRET_KEY = 'fm'

    SQLALCHEMY_DATABASE_URI = read_config()
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    BOOTSTRAP_SERVE_LOCAL = True
    FLASKY_PER_PAGE = 20

    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'

    ASSETS_DEBUG = False

    @staticmethod
    def init_app(app):
        pass
