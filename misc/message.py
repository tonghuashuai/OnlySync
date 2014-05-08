#!/usr/bin/env python
#coding:utf-8

from misc.config import SNSCode 
from misc.weibo import APIClient as SinaClient
from misc.renren import APIClient as RenrenClient
from misc.douban_client import DoubanClient
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
                    client = SinaClient()
                    client.set_access_token(access_token, expires_in)
                    client.statuses.update.post(status=msg)
                elif obj.get("code") == SNSCode.RENREN:
                    client = RenrenClient() 
                    client.set_access_token(access_token)
                    client.status.put(content=msg) #Requires read_user_status,status_update scopes
                elif obj.get("code") == SNSCode.DOUBAN:
                    client = DoubanClient() 
                    client.auth_with_token(access_token)
                    client.miniblog.new(msg)

        # print client.statuses.user_timeline.get()
        # print client.statuses.update.post(status=u'测试OAuth 2.0发微博')
        # print client.statuses.upload.post(status=u'测试OAuth 2.0带图片发微博', pic=open('/home/tonghs/42py/css/_img/logo/google.png'))

        # print client.user.get(userId="234999822")
        # print client.status.put(content="test") #Requires read_user_status,status_update scopes
        # f = open("/home/tonghs/42py/css/_img/logo/google.png", "rb")
        # r = client.photo.upload(file=f, filename="test.png")
        # f.close()  # you need to do this manually
