#!/usr/bin/env python
#coding:utf-8

import re
import urllib

def get_img_url(html):
    p = '<img class="small-img"  src=".*?" />'
    img_list = map(get_img_src, re.findall(p, html))

    return img_list


def get_img_src(html):
    return html.replace('<img class="small-img"  src="', '').replace('_80x60.jpg" />', '')
    

def get_price(html):
    price = '0'
    p = '<span class="price big"><b>&yen;</b><em>\d+\.\d+</em></span>'
    price_html = re.findall(p, html)
    if price_html:
        price = price_html[0].replace('<span class="price big"><b>&yen;</b><em>', '').replace('</em></span>', '')
    
    return price


def get_title(html):
    title = ''
    p = '<h2 class="title">.*?</h2>'
    title_html = re.findall(p, html)
    if title_html:
        title = title_html[0].replace('<h2 class="title">', '').replace('</h2>', '')

    return title


def get_desc(html):
    desc = ''
    p = '<div data-url=".*?" class="describe" id="J_DescContent">'
    desc_html = re.findall(p, html)
    if desc_html:
        desc_url = desc_html[0].replace('<div data-url="', '').replace('" class="describe" id="J_DescContent">', '')
        c = urllib.urlopen(desc_url)
        txt = c.read()
        # 转码，淘宝页面为 gbk 编码
        txt = unicode(txt,'GBK').encode('UTF-8')
        if txt:
            desc = txt.replace("var desc='", '').replace("';", '').replace('\\', '<br>')
    
    return desc
