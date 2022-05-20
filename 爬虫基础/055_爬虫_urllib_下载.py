# -*- coding:utf-8 -*-
# @Time : 2022/5/18 18:54
# @Author : BinBin Xue
# @File : 055_爬虫_urllib_下载
# @Project : testPython

# 下载网页
import urllib.request

# url_page = 'http://www.baidu.com'
# # url代表的是下载的路径 filename文件的名字
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片 url_img = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fblog%2F202008
# %2F12%2F20200812063353_pqdcs.thumb.1000_0.jpg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,
# 10000&q=a80&n=0&g=0n&fmt=auto?sec=1655463691&t=1a3f889321b2be8a6c7b595af1748b40' urllib.request.urlretrieve(
# url=url_img,filename='lisa.jpg')

# 下载视频
url_video = 'https://mediago-static.cdn.bcebos.com/haokan/bundle-2.2.2.js'
urllib.request.urlretrieve(url_video,'lisavideo.mp4')