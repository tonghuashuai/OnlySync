#!/usr/bin/env python
#coding:utf-8

import json
from _base import BaseHandler
from model.user import User
from misc import dba
from misc.weibo import APIClient as SinaClient
from misc.renren import APIClient as RenrenClient
from misc.douban_client import DoubanClient
from misc.tweibo import API, JSONParser
from misc.tweibo import OAuth2_0_Handler as AuthHandler
from misc.config import *
from misc.python_misc.string_misc import md5
from misc.message import Message
from misc.config import SELECT_ACCESS_INFO 
import _mysql_exceptions
from misc.python_misc.datetime_misc import *


class IndexHandler(BaseHandler):
    def get(self):
        querys = None
        if self.current_user:
            sql = SELECT_ACCESS_INFO .format(self.current_user.id)
            querys = dba.query(sql)
        msg = self.get_argument("msg", "");
        self.render(querys=querys, msg=msg)

    def post(self):
        msg = self.get_argument("txt")
        loc = self.get_argument("txt_loc")
        if loc:
            msg = "我会告诉你我在 {0} 吗？  {1}".format(loc, msg)
        access_info = self.get_argument("access_info")

        objs = json.loads(access_info)
        Message.send(objs, msg, self.request.files)

        self.redirect("/?msg=发送成功")

class AboutHandler(BaseHandler):
    def get(self):
        self.render()


class RegisterHandler(BaseHandler):
    def get(self):
        self.render()

    def post(self):
        msg = "ok"
        email = self.get_argument("email")
        name = self.get_argument("name")
        pwd = self.get_argument("pwd")
        sex = self.get_argument("sex")

        user = User(name,md5(pwd), sex, email)
        try:
            user.insert()
        except _mysql_exceptions.IntegrityError as e:
            msg = "邮箱已注册"
        
        self.finish({'msg': msg})

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

class ShareHandler(BaseHandler):
    def get(self):
        txt = self.get_argument("txt", "")
        txt = txt.replace("<", "&lt;").replace(">", "&gt;")
        self.render(txt=txt)

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
                                 SNSCode.SWEIBO,
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

class TweiboHandler(BaseHandler):
    def get(self):
        auth = AuthHandler()
        ## use get_authorization_url if you haven't got a token
        url = auth.get_authorization_url()

        self.redirect(url)


class TweibocallbackHandler(BaseHandler):
    def get(self):
        code = self.get_argument("code")
        auth = AuthHandler()
        r = auth.get_access_token(code)
        access_token = r["access_token"]
        open_id = r["openid"]
        expires_in = int(r["expires_in"])

        User.update_access_token(self.current_user.id, 
                                 SNSCode.TWEIBO,
                                 access_token,
                                 timestamp_datetime(expires_in),
                                 expires_in, open_id)

        js_ = """
            <script>
                window.location.href="/setting"
            </script>
        """
        self.write(js_)
