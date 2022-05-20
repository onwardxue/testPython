# -*- coding:utf-8 -*-
# @Time : 2022/5/18 19:54
# @Author : BinBin Xue
# @File : 057_爬虫_urllib_get请求的quote方法
# @Project : testPython

# Unicode编码
# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# =https://www.baidu.com/s?wd=周杰伦

# 需求 获取https://www.baidu.com/s?wd=周杰伦的网页源码，从而获取信息

import urllib.request

url = 'https://www.baidu.com/s?wd='

# 请求对象的定制UA是为了解决反爬的一种手段
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.67 Mobile Safari/537.36 '
}

# *将周杰伦三个字变成Unicode编码的格式
# *需要使用urllib.parse.quote（能将汉字变成Unicode编码）
name = urllib.parse.quote('周杰伦')
url = url + name
print(url)

# 请求对象的定制
request = urllib.request.Request(url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')

# 打印数据
print(content)