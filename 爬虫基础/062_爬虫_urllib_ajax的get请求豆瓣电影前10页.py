# -*- coding:utf-8 -*-
# @Time : 2022/5/19 14:56
# @Author : BinBin Xue
# @File : 062_爬虫_urllib_ajax的get请求豆瓣电影前10页
# @Project : testPython

#  https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20
#  start=0;limit=20

#  https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=20&limit=20
#  start=20;limit=20

#  https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=40&limit=20
#  start=40;limit=20

#  https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=60&limit=20
#  start=60;limit=20

#  https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=80&limit=20
#  start=80;limit=20

# ajax：实现页面下滑，逐渐增加内容（即不用点击下一页，进入下一页，能增加项目条数，每页有20条数据）

# 下载豆瓣电影前10页的数据
# （1）请求对象的定制
# （2）获取响应的数据
# （3）下载数据
import urllib.parse

import urllib.request


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&'

    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.67 Mobile Safari/537.36 '
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page,content):
    with open('douban' + str(page) + 'json', 'w',  encoding='utf-8') as fp:
        fp.write(content)

# 程序的入口
if __name__ == '__main__':
    start_page = int(input('请输入起始的页面：'))
    end_page = int(input('请输入结束的页面：'))

    for page in range(start_page, end_page + 1):
        # 每一页都有自己的请求对象的定制
        request = create_request(page)
        # 获取响应的数据
        content = get_content(request)
        # 下载
        down_load(page,content)