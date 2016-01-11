#!/usr/bin/env python
# coding:utf-8

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

HOST = "http://sync.tonghs.com"

# 新浪微博
SINA_APP_KEY = "3250001650"  # app key
SINA_APP_SECRET = "21f7e89d289626838e4cc2d3c60140c7"  # app secret
SINA_CALLBACK_URL = "{0}/auth/sina_callback".format(HOST)  # callback url

# renren
REN_APP_KEY = "267824"
REN_APP_SECRET = "9ccb1b104de449ebb7ab5b5df398ec6d"
REN_REDIRECT_URI = "{0}/auth/renren_callback".format(HOST)
REN_SCOPE = ["status_update", "photo_upload", "read_user_status"]

# douban
DOUBAN_APP_KEY = "05d6fd652e63364b1184f82f8b29a2e1"
DOUBAN_APP_SECRET = "b9dfa5c1a62eb874"
DOUBAN_REDIRECT_URI = "{0}/auth/douban_callback".format(HOST)
DOUBAN_SCOPE = 'douban_basic_common,shuo_basic_r,shuo_basic_w'

# tencent weibo
TWEIBO_APP_KEY = "801504862"
TWEIBO_APP_SECRET = "a24f8a49a949680882ab60c3c30b75c3"
TWEIBO_CALLBACK_URL = "{0}/auth/tweibo_callback".format(HOST)


MYSQL_HOST = "127.0.0.1"
MYSQL_DB = "onlysync"
MYSQL_USR = "root"
MYSQL_PWD = "OhMyGod20!@"

SELECT_ALL = "select * from {tbl_name} where 1 = 1 {where};"
UPDATE = "update {tbl_name} set {k_v} where {where}"
SELECT_ACCESS_INFO = "select s.name, a.access_token, s.icon, s.code,\
    u.id as u_id, a.expires_in, a.expires_time from User as u left join\
    SNS as s on 1 = 1 left join Access\
    as a on a.u_id = u.id and \
    a.sns_code = s.code where\
    u.id = {0};"


class SNSCode(object):
    SWEIBO = "sweibo"
    WEIXIN = "weixin"
    RENREN = "renren"
    DOUBAN = "douban"
    TWEIBO = "tweibo"
