#!/usr/bin/env python
#coding:utf-8

from misc.config import SNSCode 
from misc.weibo import APIClient as SinaClient
from misc.renren import APIClient as RenrenClient
from misc.config import *

class Message(object):
    @classmethod
    def send(cls, access_info_list, msg):
        client = None
        if access_info_list:
            for obj in access_info_list:
                access_token = obj.get("access_token")
                expires_in = obj.get("expires_in")
                if obj.get("code") == SNSCode.SINA_WEIBO:
                    client = SinaClient(app_key=SINA_APP_KEY, app_secret=SINA_APP_SECRET, redirect_uri=SINA_CALLBACK_URL)
                    client.set_access_token(access_token, expires_in)
                    client.statuses.update.post(status=msg)
                elif obj.get("code") == SNSCode.RENREN:
                    client = RenrenClient(app_key=REN_APP_KEY, app_secret=REN_APP_SECRET,
                                          redirect_uri=REN_REDIRECT_URI) 
                    client.set_access_token(access_token)
                    client.status.put(content=msg) #Requires read_user_status,status_update scopes
