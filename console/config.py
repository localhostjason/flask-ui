# -*- coding:utf8 -*-
import os
import json


class ReadConfigJson(object):

    def __init__(self):
        path = os.path.abspath(os.path.dirname(__file__))
        config_path = os.path.join(path, 'config.json')
        self.config_path = config_path

    def __read_json(self):
        with open(self.config_path, encoding='utf-8') as f:
            data = f.read()
            data = json.loads(data)
        return data

    def get_mysql_config(self):
        mysql_dict = self.__read_json()['mysql']
        mysql_url = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(user=mysql_dict['user'],
                                                                                        password=mysql_dict['password'],
                                                                                        host=mysql_dict['host'],
                                                                                        port=mysql_dict['port'],
                                                                                        database=mysql_dict['database'])

        return mysql_url


base_path = os.path.abspath(os.path.dirname(__file__))
upload_path = os.path.join(base_path, 'upload', 'files')
print(upload_path)


class Config:
    DEBUG = True
    # SECRET_KEY = os.urandom(24)
    SECRET_KEY = 'tc'

    SQLALCHEMY_DATABASE_URI = ReadConfigJson().get_mysql_config()
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    BOOTSTRAP_SERVE_LOCAL = True
    FLASKY_PER_PAGE = 20

    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'

    ASSETS_DEBUG = False

    UPLOADS_DEFAULT_DEST = upload_path

    @staticmethod
    def init_app(app):
        pass
