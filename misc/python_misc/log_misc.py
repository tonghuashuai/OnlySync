#!/usr/bin/env python
#coding:utf-8

import logging
from config import *


class LogHanlderDict(object):
    c = 0
    f = 1
    fc = 2

class Log(object):
    def __init__(self):
        # 创建一个logger
        self.logger = logging.getLogger('')
        self.logger.setLevel(logging.DEBUG)

        handler_list = self.get_handler()
        for handler in handler_list:
            handler.setLevel(logging.DEBUG)
            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

            # 给logger添加handler
            self.logger.addHandler(handler)

    def info(self, msg):
        self.logger.info(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def get_handler(self):
        handler_list = []
        if LOG_HANDLER == LogHanlderDict.c:
            handler = self.get_console_handler()
            handler_list.append(handler)
        elif LOG_HANDLER == LogHanlderDict.f:
            handler = self.get_file_handler()
            handler_list.append(handler)
        elif LOG_HANDLER == LogHanlderDict.fc:
            handler = self.get_console_handler()
            handler_list.append(handler)
            
            handler = self.get_file_handler()
            handler_list.append(handler)

        return handler_list

    def get_console_handler(self):
        # 创建一个handler，用于输出到控制台
        return logging.StreamHandler()

    def get_file_handler(self):
        # 创建一个handler，用于写入日志文件
        return logging.FileHandler(LOG_FILE)

class ConsoleLog(Log):
    def get_handler(self):
        # 创建一个handler，用于输出到控制台
        ch = self.get_console_handler()

        return [ch]

class FileLog(Log):
    def get_handler(self):
        # 创建一个handler，用于写入日志文件
        fh = self.get_file_handler()

        return [fh]
