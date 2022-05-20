# -*- coding:utf-8 -*-
# @Time : 2022/5/18 17:47
# @Author : BinBin Xue
# @File : 053_爬虫_urllib_基本使用
# @Project : testPython

# 使用urllib模拟浏览器获取百度首页的源码
import urllib.request

# (1)定义一个url 就是你要访问的地址
url = 'http://www.baidu.com'

# (2) 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# (3)获取响应中的页面的源码
# read方法返回的是字节形式的二进制数据
# 要将二进制的数据转换为字符串（解码）decode('编码的格式')
content = response.read().decode('utf-8')

# (4)打印数据
print(content)
