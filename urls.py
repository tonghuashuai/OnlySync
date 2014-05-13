#!/usr/bin/env python
#coding:utf-8


from view.root import * 
from view.test.root import *
from view.home.root import *
from view.home.j.root import *
from view.j.root import *


urls = [
    (r"/", IndexHandler),
    (r"/about", AboutHandler),
    (r"/login", LoginHandler),
    (r"/register", RegisterHandler),
    (r"/logout", LogoutHandler),
    (r"/new", NewHandler),
    (r"/setting", SettingHandler),
    (r"/share", ShareHandler),

    (r"/auth/sina", SinaHandler),
    (r"/auth/renren", RenrenHandler),
    (r"/auth/douban", DoubanHandler),
    (r"/auth/tweibo", TweiboHandler),
    (r"/auth/sina_callback", SinacallbackHandler),
    (r"/auth/renren_callback", RenrencallbackHandler),
    (r"/auth/douban_callback", DoubancallbackHandler),
    (r"/auth/tweibo_callback", TweibocallbackHandler),

    (r"/j/parser", ParserHandler),
    (r"/j/unband", UnbandHandler),

    (r"/t", TestHandler),
]
