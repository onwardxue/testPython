# -*- coding:utf-8 -*-
# @Time : 2022/5/18 20:15
# @Author : BinBin Xue
# @File : 058_爬虫_urllib_get请求的urlencode方法
# @Project : testPython

# urlencode应用场景：url中带有多个参数的时候
# 如url = 'https://www.baidu.com/s?wd=周杰伦&sex=男'

import urllib.parse

data = {
    'wd' : '周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}
# urlencode连接多个参数并转成Unicode
a = urllib.parse.urlencode(data)
print(a)

# 需求：获取url = 'https://www.baidu.com/s?wd='的网页源代码
import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location':'中国台湾省'
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url=base_url+new_data

headers={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.67 Mobile Safari/537.36 '
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码的数据
content = response.read().decode('utf-8')

# 打印数据
print(content)