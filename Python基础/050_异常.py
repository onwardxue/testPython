# -*- coding:utf-8 -*-
# @Time : 2022/5/18 17:03
# @Author : BinBin Xue
# @File : 050_异常
# @Project : testPython

try:
    fp = open('text.txt','r')
    fp.read()
except FileNotFoundError:
    print("系统正在升级，请稍后再试。。")
