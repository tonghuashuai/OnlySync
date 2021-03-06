#!/usr/bin/env python
# coding:utf-8

from base import Base


class Access(Base):
    def __init__(self, u_id=0, sns_code="", access_token="",
                 expires_time="", expires_in="", open_id=""):
        self.u_id = u_id
        self.sns_code = sns_code
        self.access_token = access_token
        self.expires_time = expires_time
        self.expires_in = expires_in
        self.open_id = open_id
