# -*- coding:utf-8 -*-
# @Time : 2022/5/18 20:38
# @Author : BinBin Xue
# @File : 059_爬虫_urllib_post请求百度翻译
# @Project : testPython

import urllib.request

# 从网页找端口
url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.67 Mobile Safari/537.36 '
}

data = {
    'kw': 'spider'
}

# *post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf=8')

# *post的请求参数 是不会拼接在url后面的 而是需要放在请求对象定制的参数中 （get请求的参数放在url后面）
# *post请求参数，必须要进行编码
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

# 字符串变成json对象
import json

obj = json.loads(content)
print(obj)

# post请求方式的参数 必须编码 data=urllib.parse.urlencode(data)
# 编码之后必须调用encode方法 data = urllib.parse.urlencode(data).encode('utf=8')
# 参数是放在请求对象的定制方法中 request = urllib.request.Request(url=url,data=data,headers=headers)
