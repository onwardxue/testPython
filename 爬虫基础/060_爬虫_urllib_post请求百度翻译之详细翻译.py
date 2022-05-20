# -*- coding:utf-8 -*-
# @Time : 2022/5/18 20:59
# @Author : BinBin Xue
# @File : 060_爬虫_urllib_post请求百度翻译之详细翻译
# @Project : testPython

import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

# 反扒手段2：cookie
headers = {
    # 'Accept': '*/*',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '135',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=6F5ABF6CBDD2DC9DA4F540D6B5035073; PSTM=1635833249; '
              'BAIDUID=6F5ABF6CBDD2DC9DF0DD9913145EEAC4:FG=1; '
              '__yjs_duid=1_14e601f8b2d4e7f4870ede7bb9ea307e1635857374454; '
              'BDUSS_BFESS=RTV3VhaEg1bklza01tWEJuRnpFMmNibU9iRWNNZjdrWDVHTn5BaTBkcHE5R05pSUFBQUFBJCQAAAAAAAAAAAEAAADFM-Gw1u648LuwzOzPwgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGpnPGJqZzxiNn; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=107312_110085_127969_174441_179347_184716_190621_194085_194519_196426_196527_197242_197471_197711_199022_199579_201193_203309_203880_203882_203885_204713_204715_204717_204720_204859_204908_205218_205420_205424_205751_206927_207237_207264_207540_207716_207997_208721_209063_209345_209394_209568_209579_209748_209847_210308_210359_210670_210696_210733_210757_210793_211022_211116_211158_211350_211456_211580_211694_211740_211758_212515_212618_212646_212699_212740_212776_212798_212949_212970_212994_213003_213010_213045_213094_213125_213134_213139_213345_213416_213566_213594_213596_213644_213730_213870_213920_214001_214005; BAIDULOC=12621477.586917942_2630165.703848785_12143.746113070882_257_1652873215329; BAIDULOC_BFESS=12621477.586917942_2630165.703848785_12143.746113070882_257_1652873215329; BA_HECTOR=0k800180ka09a4akqh1h89mkr0r; BAIDUID_BFESS=6F5ABF6CBDD2DC9DF0DD9913145EEAC4:FG=1; delPer=0; PSINO=1; rsv_i=2fc7D%2FR2j0sahG8ne6H0dMb%2BuDryJJ2sX52n5mftPfVOhmAf%2F5hZwq2dlNF54NNCE7iuXq%2Bz46Jb%2BM51ANCoPGJ7tY%2BGkm4; SE_LAUNCH=5%3A27547904_0%3A27547904; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=36429_31254_34813_36423_36165_34584_35979_36055_36236_26350_36447; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1651909495,1652877242; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1652877262; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1652878448; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1652878623; ab_sr=1.0.1_N2M0NmQ1MGZlODU2OWJlOWYyYzhmMjU5ODExYjE4ZGI0MzMwNDE4Mzg4MzYyY2QxMjIxYjAxMTJjM2JlZjhlYzJjNjZmN2FkMzliZGVkYjYzYzUxZTEwOTg2YzY5MjA4YzA3NTM2ZjliNTExZWViMGIyM2QzOTQ2ZWRlNGI2MjU2MTIwYWQzMmNmYmYwOGFjMGFmZjBmOGFiNDNlOWU3Y2JhMzQyZDY2ZGU1N2I4MDE2YzRlZjMxOTRlYTRlNjE0',
    # 'Host': 'fanyi.baidu.com', 'Origin': 'https://fanyi.baidu.com', 'Pragma': 'no-cache', 'Referer':
    # 'https://fanyi.baidu.com/?aldtype=16047', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101",
    # "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'Sec-Fetch-Dest':
    # 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': 'Mozilla/5.0 (Linux; Android
    # 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Mobile Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': 'b7f7a79c5f7103744f68cd5a3c144fc6',
    'domain': 'common',
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

import json

obj = json.loads(content)

print(obj)
