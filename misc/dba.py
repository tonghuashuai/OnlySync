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
    try:
        count = cursor.execute(sql)
        querys = cursor.fetchall()
    except Exception as d:
        cursor.close()
        conn.close()
        raise d 

    return querys

    
def execute(sql):
    cursor, conn = get_cursor()
    try:
        cursor.execute(sql)
    except Exception as d:
        cursor.close()
        conn.close()
        raise d 
