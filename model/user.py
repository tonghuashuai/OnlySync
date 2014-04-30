#!/usr/bin/env python
#coding:utf-8

import json
from misc.config import SEX_EN 

class User(object):
    def __init__(self, name, pwd, sex=None, email=""):
        self.uid = 0
        self.name = name
        self.pwd = pwd
        self.sex = sex or SEX_EN.get("NOT_SURE")
        self.email = email
    
    @classmethod
    def get(cls, uid):
        pass

    @classmethod
    def login(cls, email, pwd):
        user = User(email, pwd) 
        # todo 验证用户
        return user 

    def get_dict(self):
        return self.__dict__

    def get_json(self):
        return json.dumps(self.get_dict())

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

