#!/usr/bin/env python
#coding:utf-8

from misc.config import *
from misc import dba
from misc.python_misc.log_misc import Log
import json

log = Log()

class Base(object):
    
    @classmethod
    def get(cls, o_id):
        model = None
        try:
            where = "and id = {0}"
            querys = cls.select(where.format(str(o_id)))

            if querys:
                model = querys[0]

        except Exception as e:
            log.error(e)

        return model 

    def get_dict(self):
        return self.__dict__

    def get_json(self):
        return json.dumps(self.get_dict())

    @classmethod
    def get_from_dict(cls, dic):
        model = cls()
        for k, v in dic.iteritems():
            setattr(model, k, v)

        return model 

    @classmethod
    def select(cls, where=""):
        model_list = []
        try:
            where = "and {0}".format(where)
            tbl_name = cls.__name__
            sql = SELECT_ALL.format(tbl_name=tbl_name, where=where)
            models = dba.query(sql)
            
            for dic in models:
                model = cls.get_from_dict(dic)
                model_list.append(model)

        except Exception as e:
            log.error(e)

        return model_list

    @classmethod
    def get_from_json(cls, json_str):
        model = None
        try:
            if json_str:
                dic = json.loads(json_str)
                model = cls.get_from_dict(dic)

        except Exception as e:
            log.error(e)

        return model

    def insert(self):
        try:
            tbl_name = self.__class__.__name__
            sql = "insert into {tbl_name} ({cols}) values ({vals});"
            cols = ""
            vals = ""

            o_dict = self.get_dict()
            for k, v in o_dict.iteritems():
                if k != "id":
                    cols += k + ","
                    f_type = type(v).__name__
                    # 数字型不需要加引号
                    if f_type == "int" or f_type == "long":
                        vals += str(v) + ","
                    else:
                        vals += "'" +  v + "',"

            cols = cols[:-1]
            vals = vals[:-1]
            sql = sql.format(tbl_name=tbl_name, cols=cols, vals=vals)
            
            dba.execute(sql)
        except Exception as e:
            log.error(e)

    def update(self):
        try:
            tbl_name = self.__class__.__name__
            sql = "update {tbl_name} set {sets} where id={o_id};"

            o_dict = self.get_dict()
            sets = ""
            for k, v in o_dict.iteritems():
                if k != "id":
                    col = k + "="
                    f_type = type(v).__name__
                    # 数字型不需要加引号
                    if f_type == "int" or f_type == "long":
                        val = str(v) + ","
                    elif f_type == "NoneType":
                        val = "NULL,"
                    else:
                        val = "'" +  v + "',"

                    sets += col + val
            sets = sets[:-1]
            sql = sql.format(tbl_name=tbl_name, sets=sets, o_id=self.id)

            dba.execute(sql)
        except Exception as e:
            log.error(e)
