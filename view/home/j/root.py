#!/usr/bin/env python
#coding: utf-8


import tornado.web
from view.home.root import BaseHandler
from model.user import User

class UnbandHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        uid = self.current_user.id
        code = self.get_argument("code")

        User.update_access_token(self.current_user.id, 
                                 code, None, None, None, None)

