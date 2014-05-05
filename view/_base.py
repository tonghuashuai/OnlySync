#!/usr/bin/env python
#coding:utf-8


import tornado.web
import mako.lookup
import mako.template
import json
import logging

from model.user import User


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        template_path = self.get_template_path()
        self.lookup = mako.lookup.TemplateLookup(directories=template_path,
                                                 input_encoding='utf-8',
                                                 output_encoding='utf-8')

    def render_string(self, filename, **kwargs):
        kwargs["current_user"] = self.current_user
        template = self.lookup.get_template(filename)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return template.render(**namespace)

    def render(self, **kwargs):
        filename = "{0}.html".format(self.__class__.__name__.replace("Handler", ""))
        filename = "{0}{1}".format(filename[0].lower(), filename[1:])
        self.finish(self.render_string(filename, **kwargs))

    def get_current_user(self):
        json = self.get_secure_cookie("user")
        user = User.get_from_json(json)

        return user
