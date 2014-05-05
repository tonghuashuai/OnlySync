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

        return user.get_json() 
