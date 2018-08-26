#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/24 16:23
# @Author  : Alaska
# @File    : main
# @Software: PyCharm

import os
from PIL import Image


#os.chdir(r'')
logo = Image.open('logo.png')
w1, h1 = logo.size
print(w1, h1)
for fname in os.listdir('.\win'):
    print(fname)
    g1 = Image.open(r'.\win\%s'%fname)
    w, h = g1.size
    if w < h:
        if h > 3000:
            w = w*3000/h
            h = 3000
    else:
        if w > 3000:
            h = h*3000/w
            w = 3000
    print(w, h)
    g2 = g1.resize((w, h))
    g2.paste(logo, (w-w1, h-h1))
    g2.save(r'.\win_new\%s'%fname)