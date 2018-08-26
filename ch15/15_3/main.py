#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 15:13
# @Author  : Alaska
# @File    : main
# @Software: PyCharm

import time

print('press enter to start\npress ctrl+C to end\n')
entercnt = 0
starttime = 0
endtime = 0



try:
    while True:
        input()
        if 0 == entercnt:
            starttime = time.time()
            entercnt += 1
            print('start ')
        else:
            endtime = time.time()
            print('time is %ss and cycle is %s' % (endtime - starttime, entercnt))
            starttime = endtime
            entercnt += 1
except KeyboardInterrupt:
    print('stop')