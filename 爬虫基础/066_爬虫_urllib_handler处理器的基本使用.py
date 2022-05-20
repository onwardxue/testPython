# -*- coding:utf-8 -*-
# @Time : 2022/5/19 21:36
# @Author : BinBin Xue
# @File : 066_爬虫_urllib_handler处理器的基本使用
# @Project : testPython

# 需求 使用handler访问百度 获取网页源码 （handler具有代理功能，更强大）
import urllib.request
url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.67 Mobile Safari/537.36 '
}

request = urllib.request.Request(url=url, headers=headers)

# handler  build_opener open 三步

# (1)获取handler对象
handler = urllib.request.HTTPHandler()

# (2)获取opener对象
opener = urllib.request.build_opener(handler)

# (3)调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)