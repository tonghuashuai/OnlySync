#!/usr/bin/env python
#coding:utf-8

import MySQLdb
from config import *

conn = MySQLdb.connect(
    host=MYSQL_HOST,
    user=MYSQL_USR,
    passwd=MYSQL_PWD,
    db=MYSQL_DB,
    charset="utf8")

def get_cursor():
    cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    return cursor

def query(sql):
    cursor = get_cursor()
    count = cursor.execute(sql)

    return cursor.fetchall()
    
def execute(sql):
    cursor = get_cursor()
    cursor.execute(sql)
