#!/usr/bin/env python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web
from view._base import BaseHandler as _BaseHanlder
from model.access import Access
from misc import dba
from misc.config import SELECT_ACCESS_INFO 


class BaseHandler(_BaseHanlder):
    pass


class NewHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render()


class SettingHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        uid = self.current_user.id
        sql = SELECT_ACCESS_INFO .format(self.current_user.id)
        querys = dba.query(sql)

        self.render(querys=querys)
