#!/usr/bin/env python
#coding:utf-8

import urllib
import json
from view._base import BaseHandler
from misc.util import get_img_url, get_price, get_title, get_desc

class ParserHandler(BaseHandler): 
    def post(self):
        url = self.get_argument('url')
        c = urllib.urlopen(url)
        html = c.read()
        # 转码，淘宝页面为 gbk 编码
        html = unicode(html,'GBK').encode('UTF-8')

        img_list = get_img_url(html)
        price = get_price(html)
        title = get_title(html)
        desc = get_desc(html)

        self.write({
            'title': title,
            'price': price,
            'img_list': img_list,
            'desc': desc
        })
