# -*- coding:utf-8 -*-
# @Time : 2022/5/18 18:00
# @Author : BinBin Xue
# @File : 054_爬虫_urllib_1个类型和6个方法
# @Project : testPython

import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
# print(type(response))

# 1.返回多少个字节
# content = response.read(5)
# print(content)

# 2.读取一行
# content = response.readline()
# print(content)

# 3.读取多行
# content = response.readlines()
# print(content)

# 4.返回状态码 200表示我们的逻辑没有错
print(response.getcode())

# 5.返回的是url地址
print(response.geturl())

# 6.获取的是状态信息
print(response.getheaders())