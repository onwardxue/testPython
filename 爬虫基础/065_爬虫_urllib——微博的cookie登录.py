# -*- coding:utf-8 -*-
# @Time : 2022/5/19 20:49
# @Author : BinBin Xue
# @File : 065_爬虫_urllib——微博的cookie登录
# @Project : testPython

# 适用的场景：数据采集的时候，需要绕过登录，然后进入到某个页面
# 个人信息页面是utf-8，但还是报错了编码错误，因为没有进入到个人信息页面
# 什么情况下，访问不成功？
# 因为请求体的信息不够，所以访问不成功 -> 要加入request header中的cookie才能实现登录

import urllib.request

url = 'https://weibo.cn/6451491586/info'

headers = {
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/101.0.4951.67 Mobile Safari/537.36 '
    }

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('gb2312')

with open(' weibo.html','w',encoding='gb2312')as fp:
    fp.write(content)
