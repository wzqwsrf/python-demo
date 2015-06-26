__author__ = 'wzqwsrf'
# encoding:utf-8

import re
import requests
from BeautifulSoup import BeautifulSoup as soup
# 获取网页内容
r = requests.get('http://ac.jobdu.com/status.php?pid=1001&user_id=wzqwsrf')
# 修改编码格式，否则输出为乱码
r.encoding = 'utf-8'
data = r.text
# 获取所有table内容，主要获取我的提交历史。这里的table应该只有一个。
table = soup(data).findAll('table')
# 理论上来讲，获取第一个table就可以。好像实际也是这样
table = table[0]
# 开始获取每一行了，应该是每个tbody。有多少行就有多少个tbody
tbody = table.findAll('tbody')
tbodyLen = len(tbody)
for i in range(tbodyLen):
    body = tbody[i]
#   针对每个body取出td。
    tds = body.findAll(name="td")
    # print tds
    # print tds[3].find('font').string
    yuyan = tds[7].string
    # print len(yuyan)
    if 'Java' in yuyan:
        yuyan = 'Java'
    elif 'C++' in yuyan:
        yuyan = 'C++'
    print yuyan
    url = 'http://ac.jobdu.com/showsource.php?sid='+tds[0].string
    print url
    urlr = requests.get(url)
    urlr.encoding = 'utf-8'
    code = urlr.text
    print code
    code = soup(code).findAll('table')
    print code
#   列值是有规律的，不再遍历，10列
#     probId = tds[0]
#     probAc = tds[3]
#     print probId.string
#     print probAc

