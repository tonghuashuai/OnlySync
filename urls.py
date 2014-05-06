#!/usr/bin/env python
#coding:utf-8


from view.root import * 
from view.test.root import *
from view.home.root import *
from view.j.root import *


urls = [
    (r"/", IndexHandler),
    (r"/about", AboutHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/new", NewHandler),
    (r"/setting", SettingHandler),
    (r"/auth/sina", SinaHandler),
    (r"/auth/sina_callback", SinacallbackHandler),

    (r"/j/parser", ParserHandler),

    (r"/t", TestHandler),
]
