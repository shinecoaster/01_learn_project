#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 16:08
# @Author  : Alaska
# @File    : main
# @Software: PyCharm

'''
从 60 倒数。
倒数至 0 时播放声音文件（alarm.wav）。 这意味着代码将需要做到以下几点： 
在显示倒计时的每个数字之间，调用 time.sleep()暂停一秒。 
调用 subprocess.Popen()，用默认的应用程序播放声音文件。 
打开一个新的文件编辑器窗口，并保存为 countdown.py
'''

import subprocess
import time

for i in range(10,0,-1):
    print(i)
    time.sleep(1)

p = subprocess.Popen([r'C:\Program Files\Notepad++\notepad++.exe', r'C:\02_python\01_learn_project\ch15\15_9\main.py'])
