# -*- coding:utf-8 -*-
# @Time : 2022/5/18 19:09
# @Author : BinBin Xue
# @File : 056_爬虫_请求对象的定制
# @Project : testPython

import urllib.request

url = 'https://www.baidu.com'

# url的组成
# https://www.baidu.com/s?wd=周杰伦

# http/https        www.baidu.com       80/443          s            wd=周杰伦             #
#     协议                          主机                     端口号        路径              参数                   锚点
# http      80
# https     443
# mysql   3306
# oracle   1521
# redis     6379
# mongodb   27017
# UA - USER AGENT
# 从网页->检查->网络中取得的信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.67 Mobile Safari/537.36 '
}

# 因为urlopen方法中不能存储字典，所以headers不能传递进去
# 反扒手段1：请求对象的定制（将url和header组合定制成请求体，作为请求网络的参数）
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
