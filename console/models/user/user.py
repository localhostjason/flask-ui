from ..base import *
from datetime import datetime
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declared_attr


class UserBaseMixin:
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    display_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    login_ip = db.Column(db.String(32))
    login_time = db.Column(db.DateTime())
    register_time = db.Column(db.DateTime(), default=datetime.now)
    theme = db.Column(db.String(32), default='default')

    role = db.Column(db.String(16))
