#!/uar/bin/env python
#coding:utf-8

from view._base import BaseHandler
from model.user import User

class TestHandler(BaseHandler):
    def get(self):
        args = self.request.arguments
        msg = str(getattr(TestUnit, args.get('fun')[0])(args))
        if not msg:
            msg = TestUnit.MSG
        self.finish(msg)


class TestUnit(object):
    MSG = 'ok'

    @classmethod
    def user_get(cls, args):
        uid = args.get('uid')[0]
        user = User.get(int(uid))
        user.p = 't'
        user.update()

        return user.get_json() 

    @classmethod
    def select(cls, args):
        querys = User.update_access_token(1, "sweibo", "atttt", "2014-01-04")
        return querys[0].get_json()
