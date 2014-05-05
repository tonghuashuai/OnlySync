#!/usr/bin/env python
#coding:utf-8

import json
from misc.config import SEX_EN 
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
    def update_access_token(cls, uid, sns, access_token, expires_in):
        uid = int(uid)


