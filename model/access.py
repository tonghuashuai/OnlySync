#!/usr/bin/env python
#coding:utf-8

from base import Base


class Access(Base):
    def __init__(self, u_id=0, sns_code="", access_token="",
                 expires_time=""):
        self.u_id = u_id
        self.sns_code = sns_code
        self.access_token = access_token
        self.expires_time = expires_time
