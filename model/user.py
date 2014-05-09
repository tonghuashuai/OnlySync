#!/usr/bin/env python
#coding:utf-8

import json
from misc.config import SEX_EN 
from misc.python_misc.log_misc import Log
from access import Access
from base import Base

log = Log()

class User(Base):
    def __init__(self, name="", pwd="", sex=None, email=""):
        self.id = 0
        self.u = name
        self.p = pwd
        self.sex = sex or SEX_EN.get("NOT_SURE")
        self.email = email

    @classmethod
    def login(cls, email, pwd):
        user = None
        where = "email = '{email}' and p = '{p}'".format(email=email, p=pwd)
        users = User.select(where)
        if users:
            user = users[0]

        return user 

    @classmethod
    def update_access_token(cls, uid, sns_code, access_token,
                            expires_time, expires_in, open_id=''):
        uid = int(uid)
        where = "u_id = {uid} and sns_code = '{sns_code}'"
        where = where.format(uid=uid, sns_code=sns_code)
        querys = Access.select(where)

        if len(querys) == 0:
            a = Access(uid, sns_code, access_token, expires_time, expires_in, open_id)
            a.insert()
        else:
            access = querys[0]
            access.access_token = access_token
            access.expires_time = expires_time
            access.expires_in = expires_in
            access.open_id = open_id

            access.update()
        return querys
