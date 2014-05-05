#!/usr/bin/env python
#coding:utf-8

import json
from misc.config import SEX_EN 
from access import Access
from base import Base

class User(Base):
    def __init__(self, name="", pwd="", sex=None, email=""):
        self.id = 0
        self.u = name
        self.p = pwd
        self.sex = sex or SEX_EN.get("NOT_SURE")
        self.email = email

    @classmethod
    def login(cls, email, pwd):
        user = User(email, pwd) 
        # todo 验证用户
        return user 

    @classmethod
    def update_access_token(cls, uid, sns_code, access_token, expires_time):
        uid = int(uid)
        where = "u_id = {uid} and sns_code = '{sns_code}'"
        where = where.format(uid=uid, sns_code=sns_code)
        querys = Access.select(where)

        if len(querys) == 0:
            a = Access(uid, sns_code, access_token, expires_time)
            a.insert()
        else:
            access = querys[0]
            access.access_token = access_token
            access.expires_time = expires_time
        return querys
