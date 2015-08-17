# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-07-17 14:37:25

import sys
import requests

reload(sys)
sys.setdefaultencoding('utf-8')


# 根据登陆url，用户名，密码获取登陆后的requests
def get_login_requests(login_url, user_id, password):
    # 获取网页内容
    s = requests.session()
    data = dict(login=user_id, password=password,
                csrfmiddlewaretoken='kJlv5K5pKS2AJ2oN6PXcAEY2aOWo2Tl6')
    cookies = {
        '__atuvc': '63%7C26%2C36%7C27%2C55%7C28',
        '_gat': '1',
        'csrftoken': 'kJlv5K5pKS2AJ2oN6PXcAEY2aOWo2Tl6',
        '_ga': 'GA1.2.764974747.1435544317'
    }
    headers = {
        'Referer': "https://leetcode.com/accounts/login/",
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36',
        'Host': 'leetcode.com'
    }
    r = s.post(login_url, data=data, headers=headers,
               cookies=cookies)
    print r.headers
    print r.text


if __name__ == '__main__':
    login_url = 'https://leetcode.com/accounts/login/'
    r = requests.get(login_url)
    cookies = r.cookies['csrftoken']
    print r.cookies['csrftoken']
    get_login_requests(login_url, 'username', 'password')
    print 'over'
