#!/usr/bin/env python
#coding:utf-8

import json
from misc.config import SEX_EN 
from base import Base

class User(Base):
    def __init__(self, name="", pwd="", sex=None, email=""):
        self.uid = 0
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
    def get_from_json(cls, user_json):
        user = None
        try:
            if user_json:
                user_dic = json.loads(user_json)
                uid = user_dic.get("uid", 0)
                name = user_dic.get("name", "")
                pwd = user_dic.get("pwd", "")
                email = user_dic.get("email", "")
                sex = user_dic.get("sex", SEX_EN.get("NOT_SURE"))

                user = User(name, pwd, sex, email)
        except Exception as e:
            print e

        return user

    @classmethod
    def update_access_token(cls, uid, sns, access_token, expires_in):
        uid = int(uid)


