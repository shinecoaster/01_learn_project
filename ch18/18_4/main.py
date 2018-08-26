#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 16:16
# @Author  : Alaska
# @File    : main
# @Software: PyCharm

import pyautogui
print('press Ctrl + C to quit \n')
p = pyautogui.position()
try:
    while True:
        pstr = str(p)
        le = len(pstr)
        #print(pstr)
        print(pstr, end='')
        a = 1
        print('\b'*(le+1), end='', flush=True)
        p = pyautogui.position()
except KeyboardInterrupt:
    print('\nover\n')