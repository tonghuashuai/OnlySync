#!/usr/bin/env python
# coding:utf-8

import re
import hashlib


def extract(s, start, end, pre_suf_fix=False):
    p = '{start}.*?{end}'.format(start=start, end=end)
    target = re.findall(p, s)

    s_ = None
    if target:
        s_ = target[0]
        if not pre_suf_fix:
            s_ = s_.replace(start, '').replace(end, '')

    return s_


def md5(s):
    m = hashlib.md5()
    m.update(s)

    return m.hexdigest()
