#!/usr/bin/env python
#coding:utf-8


from _base import BaseHandler
from model.user import User
from misc.weibo import APIClient
from misc.config import *

from misc.python_misc.datetime_misc import *


class IndexHandler(BaseHandler):
    def get(self):
        self.render()


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
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
        url = client.get_authorize_url()
        
        self.redirect(url)

class SinacallbackHandler(BaseHandler):
    def get(self):
        # 获取URL参数code:
        code = self.get_argument('code')
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
        r = client.request_access_token(code)
        access_token = r.access_token # 新浪返回的token，类似abc123xyz456
        expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
        User.update_access_token(self.current_user.id, 
                                 SNSCode.SINA_WEIBO,
                                 access_token,
                                 timestamp_datetime(expires_in))
        client.set_access_token(access_token, expires_in)

        # print client.statuses.user_timeline.get()
        # print client.statuses.update.post(status=u'测试OAuth 2.0发微博')
        # print client.statuses.upload.post(status=u'测试OAuth 2.0带图片发微博', pic=open('/home/tonghs/42py/css/_img/logo/google.png'))

        js_ = """
            <script>
                parent.$.fancybox.close()
            </script>
        """
        self.render(js_=js_)
