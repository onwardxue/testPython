# -*- coding:utf-8 -*-
# @Time : 2022/5/19 20:41
# @Author : BinBin Xue
# @File : 064_爬虫_urllib_异常
# @Project : testPython
import urllib.request

url = 'http://www.douban111.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.67 Mobile Safari/537.36 '
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)

except urllib.error.URLError:
    print('系统正在升级。。。')

