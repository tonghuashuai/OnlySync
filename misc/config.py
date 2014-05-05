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

APP_KEY = "3250001650" # app key
APP_SECRET = "21f7e89d289626838e4cc2d3c60140c7" # app secret
CALLBACK_URL = "http://job.tonghs.com:8089/auth/sina_callback" # callback url

MYSQL_HOST = "127.0.0.1"
MYSQL_DB = "onlysync"
MYSQL_USR = "root"
MYSQL_PWD = "admin"

SELECT_ALL = "select * from {tbl_name};"
SELECT_BY_ID = "select * from {tbl_name} where id = {o_id};"
