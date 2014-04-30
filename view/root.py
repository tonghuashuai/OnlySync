#!/usr/bin/env python
#coding:utf-8


from _base import BaseHandler
from model.user import User


class IndexHandler(BaseHandler):
    def get(self):
        self.render()


class AboutHandler(BaseHandler):
    def get(self):
        self.render(body="about")


class LoginHandler(BaseHandler):
    def get(self):
        next_url = self.get_argument("next", "")

        self.render(next_url=next_url)

    def post(self):
        email = self.get_argument("email")
        pwd = self.get_argument("pwd")
        next_url = self.get_argument("next_url", "")

        user = User.login(email, pwd)
        print user
        if user:
            self.set_secure_cookie("user", user.get_json()) 
            if not next_url:
                next_url = "/"
        else:
            next_url = "/login"

        self.finish(next_url)
