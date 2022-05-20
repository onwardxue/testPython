# -*- coding:utf-8 -*-
# @Time : 2022/5/19 21:43
# @Author : BinBin Xue
# @File : 067_爬虫_urllib_代理
# @Project : testPython

# 代理的常用功能：
# 1.访问国外网站；
# 2.访问一些单位或团体内部资源；
# 3.提高访问速度；
# 4.隐藏真实IP

# 代理要从快代理网站上买一个，使用代理ip，别人就找不到了

import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.67 Mobile Safari/537.36 '
}

# 请求对象的定制
request = urllib.request.Request(url, headers=headers)

# 模拟浏览器访问服务器
# 配置代理ip
proxies = {
    'http':'。。。'
}
# 生成代理handler
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应的信息
content = response.read().decode('utf-8')

# 保存
with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)