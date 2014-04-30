#!/usr/bin/env python
#coding:utf-8

import tornado.web
from view._base import BaseHandler as _BaseHanlder


class BaseHandler(_BaseHanlder):
    pass


class NewHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render()


class SettingHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render()
