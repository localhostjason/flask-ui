# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import request, current_app
from flask_login import current_user
from datetime import datetime
from . import db, login_manager

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from models.user.user import UserBaseMixin


class BaseModelFunc:
    @staticmethod
    def enum_to_value(data):
        if not data:
            new_data = None
            return new_data

        try:
            new_data = data.value
        except Exception as e:
            new_data = data
        return new_data

    @staticmethod
    def enum_to_name(data):
        if not data:
            new_data = None
            return new_data

        try:
            new_data = data.name.lower()
        except Exception as e:
            new_data = data
        return new_data

    def to_dict(self, extra_kw=None, extra_dict=None, remove_key=list()):
        model_field = [v for v in self.__dict__.keys() if not v.startswith('_') and v not in remove_key]
        result = dict()
        for info in model_field:
            result[info] = self.enum_to_value(getattr(self, info))

        if extra_kw and isinstance(extra_kw, list):
            for info in extra_kw:
                result[info] = self.enum_to_value(getattr(self, info))

        if extra_dict and isinstance(extra_dict, dict):
            for k, v in extra_dict.items():
                result[k] = v

        return result

    def to_dict_lo(self, extra_kw=None, extra_dict=None, remove_key=list()):
        model_field = [v for v in self.__dict__.keys() if not v.startswith('_') and v not in remove_key]
        result = dict()
        for info in model_field:
            result[info] = self.enum_to_name(getattr(self, info))

        if extra_kw and isinstance(extra_kw, list):
            for info in extra_kw:
                result[info] = self.enum_to_name(getattr(self, info))

        if extra_dict and isinstance(extra_dict, dict):
            for k, v in extra_dict.items():
                result[k] = v

        return result


class User(UserBaseMixin, UserMixin, BaseModelFunc, db.Model):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def bool_password(self):
        return bool(self.password_hash)

    def is_admin(self):
        return bool(self.username == 'admin')

    @classmethod
    def update_time_ip(cls):
        user = cls.query.filter(cls.username == current_user.username).first_or_404()
        user.login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user.login_ip = request.remote_addr
        db.session.add(user)

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)

        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])

        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    @staticmethod
    def insert_admin():
        u = {
            'username': 'admin',
            'password': '123',
            'role': 'admin',
        }
        old = User.query.filter_by(username=u['username']).first()
        if not old:
            db.session.add(User(**u))
            db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
