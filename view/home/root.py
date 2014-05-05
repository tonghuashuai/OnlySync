#!/usr/bin/env python
#coding:utf-8

import tornado.web
from view._base import BaseHandler as _BaseHanlder
from model.access import Access


class BaseHandler(_BaseHanlder):
    pass


class NewHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render()


class SettingHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        where = "u_id = {0}".format(self.current_user.id)
        querys = Access.select(where)
        self.render()
