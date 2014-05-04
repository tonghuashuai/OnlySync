#!/usr/bin/env python
#coding:utf-8

from misc.config import *
from misc import dba
import json

class Base(object):
    def get_dict(self):
        return self.__dict__

    def get_json(self):
        return json.dumps(self.get_dict())

    @classmethod
    def get(cls):
        model_list = []
        tbl_name = cls.__name__
        objs = dba.query(SELECT_ALL.format(tbl_name=tbl_name))
        
        for dic in objs:
            obj = cls()
            for k, v in dic.iteritems():
                setattr(obj, k, v)

            model_list.append(obj)

        return model_list

    def save(self):
        tbl_name = self.__class__.__name__
        sql = "insert into {tbl_name} ({cols}) values ({vals})"
        cols = ""
        vals = ""

        o_dict = self.get_dict()
        for k, v in o_dict.iteritems():
            # todo 数据类型 加单引号的问题
            # todo 确定主键，insert 忽略主键的问题
            cols += k + ","
            vals += str(v) + ","

        cols = cols[:-1]
        vals = vals[:-1]
        sql = sql.format(tbl_name=tbl_name, cols=cols, vals=vals)
        print sql
