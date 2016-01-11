#!/usr/bin/env python
# coding:utf-8

import os

settings = {
    "debug": True,
    "template_path": os.path.join(os.path.dirname(__file__), 'html'),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
}

port = 8088

NAME = "OnlySync"
