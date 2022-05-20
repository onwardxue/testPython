# -*- coding:utf-8 -*-
# @Time : 2022/5/18 11:51
# @Author : BinBin Xue
# @File : 023_输出
# @Project : testPython

# 普通输出 - print
print("中国万事安康！")

# 格式化输出
# scrapy框架的时候 excel文件/mysql/redis
age = 18
name = '浪费时间'
print('我的名字是%s,我的年龄是%d' % (name, age))

# 输入 - input
password = input("请输入您的银行卡密码：")
print('我的密码是：%s' % password)
