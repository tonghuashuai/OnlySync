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

cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

def query(sql):
    count = cursor.execute(sql)

    return cursor.fetchall()
    
