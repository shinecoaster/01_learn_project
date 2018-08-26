#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 17:01
# @Author  : Alaska
# @File    : main
# @Software: PyCharm

import time, pyautogui

time.sleep(10)
pyautogui.click()

distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance -= 5
    pyautogui.dragRel(0,distance,duration=0.2)
    pyautogui.dragRel(-distance,0,duration=0.2)
    distance -= 5
    pyautogui.dragRel(0,-distance,duration=0.2)
