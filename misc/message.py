#!/usr/bin/env python
#coding:utf-8

import tempfile
from misc.config import SNSCode 
from misc.weibo import APIClient as SinaClient
from misc.renren import APIClient as RenrenClient
from misc.douban_client import DoubanClient
from misc.tweibo import API, JSONParser
from misc.tweibo import OAuth2_0_Handler as AuthHandler
from misc.config import *

class Message(object):
    @classmethod
    def send(cls, access_info_list, msg, img_):
        client = None
        if access_info_list:
            tmp_file = None
            file_name = ''
            img = None
            for obj in access_info_list:
                access_token = obj.get("access_token")
                if len(img_) > 0:
                    tmp_file = tempfile.NamedTemporaryFile(delete=True)
                    tmp_file.write(img_["img"][0]["body"])
                    tmp_file.seek(0)
                    img = tmp_file
                    file_name = img_["img"][0]["filename"]

                if obj.get("code") == SNSCode.SWEIBO:
                    expires_in = obj.get("expires_in")
                    client = SinaClient()
                    client.set_access_token(access_token, expires_in)
                    if img:
                        client.statuses.upload.post(status=msg, pic=img)
                    else:
                        client.statuses.update.post(status=msg)

                elif obj.get("code") == SNSCode.RENREN:
                    client = RenrenClient() 
                    client.set_access_token(access_token)
                    if img:
                        file_name = file_name.encode('utf-8')
                        r = client.photo.upload(file=img, filename=file_name, description=msg)
                    else:
                        client.status.put(content=msg) #Requires read_user_status,status_update scopes

                elif obj.get("code") == SNSCode.DOUBAN:
                    client = DoubanClient() 
                    client.auth_with_token(access_token)
                    client.miniblog.new(msg, image=img)

                elif obj.get("code") == SNSCode.TWEIBO:
                    open_id = obj.get("open_id")
                    auth = AuthHandler()
                    auth.set_token(access_token, open_id)
                    api = API(auth, parser=JSONParser())
                    a = api.tweet.add(msg, clientip='113.11.199.40')

                if img:
                    img.close()

        # print client.statuses.user_timeline.get()
        # print client.statuses.update.post(status=u'测试OAuth 2.0发微博')
        # print client.statuses.upload.post(status=u'测试OAuth 2.0带图片发微博', pic=open('/home/tonghs/42py/css/_img/logo/google.png'))

        # print client.user.get(userId="234999822")
        # print client.status.put(content="test") #Requires read_user_status,status_update scopes
        # f = open("/home/tonghs/42py/css/_img/logo/google.png", "rb")
        # r = client.photo.upload(file=f, filename="test.png")
        # f.close()  # you need to do this manually
