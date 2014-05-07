#!/usr/bin/env python
#coding:utf-8

import MySQLdb
from config import *
from misc.python_misc.log_misc import Log

log = Log()

def get_conn():
    conn = MySQLdb.connect(
        host=MYSQL_HOST,
        user=MYSQL_USR,
        passwd=MYSQL_PWD,
        db=MYSQL_DB,
        charset="utf8")

    return conn


def get_cursor():
    conn = get_conn()
    cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    return cursor, conn


def query(sql):
    cursor, conn = get_cursor()
    count = cursor.execute(sql)
    querys = cursor.fetchall()
    cursor.close()
    conn.close()

    return querys

    
def execute(sql):
    cursor, conn = get_cursor()
    cursor.execute(sql)
    cursor.close()
    conn.close()
