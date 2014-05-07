#!/usr/bin/env python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web
from view._base import BaseHandler as _BaseHanlder
from model.access import Access
from misc import dba


class BaseHandler(_BaseHanlder):
    pass


class NewHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render()


class SettingHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        sql = "select SNS.name, SNS.icon, SNS.code, Access.access_token, Access.expires_time, Access.u_id from SNS left join Access on SNS.code = Access.sns_code where u_id = 1 or u_id is null;"
        querys = dba.query(sql)

        self.render(querys=querys)
