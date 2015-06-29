# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-06-29 16:50:06


import requests
from BeautifulSoup import BeautifulSoup as soup


# 测试爬虫时需要登陆的访问情况
def login():
    # 获取网页内容
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/43.0.2357.130 Safari/537.36'
    }
    s = requests.session()
    data = dict(user_id="wzqwsrf", password='password')
    s.post('http://ac.jobdu.com/login.php', data=data, headers=headers)
    r = s.get('http://ac.jobdu.com/showsource.php?sid=1298941')
    r.encoding = 'utf-8'
    data = r.text
    # 这里主要转义一些特殊符号，如<会有问题
    table = soup(data, convertEntities=soup.HTML_ENTITIES).findAll('pre')
    print table[0].string
    # 修改编码格式，否则输出为乱码
