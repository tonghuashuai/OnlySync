#!/usr/bin/env python
#coding:utf-8

import json
from _base import BaseHandler
from model.user import User
from misc import dba
from misc.weibo import APIClient as SinaClient
from misc.renren import APIClient as RenrenClient
from misc.douban_client import DoubanClient
from misc.config import *
from misc.message import Message

from misc.python_misc.datetime_misc import *


class IndexHandler(BaseHandler):
    def get(self):
        sql = "select SNS.name, SNS.icon, SNS.code, Access.access_token, Access.expires_time, Access.expires_in, Access.u_id from SNS left join Access on SNS.code = Access.sns_code where u_id = 1 or u_id is null;"
        querys = dba.query(sql)
        self.render(querys=querys)

    def post(self):
        data = self.get_argument("data")
        msg = self.get_argument("msg")
        objs = json.loads(data)
        Message.send(objs, msg)

        self.finish({})

class AboutHandler(BaseHandler):
    def get(self):
        self.render(body="about")


class LoginHandler(BaseHandler):
    def get(self):
        next_url = self.get_argument("next", "")
        msg = self.get_argument("msg", "")

        self.render(next_url=next_url, msg=msg)

    def post(self):
        email = self.get_argument("email")
        pwd = self.get_argument("pwd")
        next_url = self.get_argument("next_url", "")
        next_url = next_url or "/"

        user = User.login(email, pwd)
        if user:
            self.set_secure_cookie("user", user.get_json())
        else:
            msg = "登录失败，请重试！"
            next_url = "/login?next={0}&msg={1}".format(next_url, msg)

        self.finish(next_url)

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")

class SinaHandler(BaseHandler):
    def get(self):
        client = SinaClient()
        url = client.get_authorize_url()
        
        self.redirect(url)

class SinacallbackHandler(BaseHandler):
    def get(self):
        # 获取URL参数code:
        code = self.get_argument('code')
        client = SinaClient()
        r = client.request_access_token(code)
        access_token = r.access_token # 新浪返回的token，类似abc123xyz456
        expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
        User.update_access_token(self.current_user.id, 
                                 SNSCode.SINA_WEIBO,
                                 access_token,
                                 timestamp_datetime(expires_in),
                                 expires_in)

        js_ = """
            <script>
                parent.$.fancybox.close()
            </script>
        """
        self.write(js_)

class RenrenHandler(BaseHandler):
    def get(self):
        client = RenrenClient() 
        url = client.get_authorize_url()

        self.redirect(url)

class RenrencallbackHandler(BaseHandler):
    def get(self):
        code = self.get_argument('code')
        client = RenrenClient()
        r = client.request_access_token(code)
        access_token = r["access_token"]  # access token
        expires_in = r["expires_in"] # access token expires in time
        refresh_token = r["refresh_token"] # token used for refresh
        
        User.update_access_token(self.current_user.id, 
                                 SNSCode.RENREN,
                                 access_token,
                                 timestamp_datetime(expires_in),
                                 expires_in)

        js_ = """
            <script>
                parent.$.fancybox.close()
            </script>
        """
        self.write(js_)


class DoubanHandler(BaseHandler):
    def get(self):
        client = DoubanClient()
        url = client.authorize_url

        self.redirect(url)


class DoubancallbackHandler(BaseHandler):
    def get(self):
        code = self.get_argument("code")
        client = DoubanClient()
        client.auth_with_code(code)
        token_code = client.token_code

        User.update_access_token(self.current_user.id, 
                                 SNSCode.DOUBAN,
                                 token_code,
                                 None, None)
        js_ = """
            <script>
                parent.$.fancybox.close()
            </script>
        """
        self.write(js_)
