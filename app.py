#! /usr/bin/env python
# coding:utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.web

import options
from urls import urls


settings = options.settings
application = tornado.web.Application(urls, **settings)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
