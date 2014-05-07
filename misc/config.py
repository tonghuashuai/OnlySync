#!/usr/bin/env python
#coding:utf-8

SEX_EN = {
    "MALE": 1,
    "FAMALE": 2,
    "NOT_SURE": 0 
}

SEX_CN = {
    1: "男",
    2: "女",
    0: "保密"
}

# 新浪微博
SINA_APP_KEY = "3250001650" # app key
SINA_APP_SECRET = "21f7e89d289626838e4cc2d3c60140c7" # app secret
SINA_CALLBACK_URL = "http://job.tonghs.com:8089/auth/sina_callback" # callback url

# renren
REN_APP_KEY = "267824"
REN_APP_SECRET = "9ccb1b104de449ebb7ab5b5df398ec6d"
REN_REDIRECT_URI = "http://job.tonghs.com:8089/auth/renren_callback"

MYSQL_HOST = "127.0.0.1"
MYSQL_DB = "onlysync"
MYSQL_USR = "root"
MYSQL_PWD = "admin"

SELECT_ALL = "select * from {tbl_name} where 1 = 1 {where};"
UPDATE = "update {tbl_name} set {k_v} where {where}"

class SNSCode(object):
    SINA_WEIBO = "sweibo"
    WEIXIN = "weixin"
    RENREN = "renren"
    DOUBAN = "douban"
