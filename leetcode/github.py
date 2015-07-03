# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015年07月02日15:53:50

import requests
from bs4 import BeautifulSoup as soup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 获取leetcode列表
def get_github_url():
    urls = []
    # 获取网页内容
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36'
    }
    cur_url = 'https://github.com/wzqwsrf/Leetcode/tree/master/Java'
    s = requests.session()
    r = s.get(cur_url, headers=headers)
    # 这里主要转义一些特殊符号，如<会有问题
    r.encoding = 'utf-8'
    html = soup(r.text)
    problem_list = html.findAll('table', {"class": "files"})
    tbody = problem_list[0].find('tbody')
    common_url = 'https://github.com'
    spans = tbody.findAll('span', {"class": "css-truncate css-truncate-target"})
    k = 0
    slen = len(spans)
    for x in xrange(0, slen, 3):
        span = spans[x]
        print span
        a = span.find('a')
        title = a['title']
        url = a['href']
        urls.append(title)
    return urls


# 写文件
def write_file(urls):
    file_object = open('github.txt', 'w')
    for url in urls:
        file_object.write(url + '\n')
    file_object.close()


if __name__ == '__main__':
    urls = get_github_url()
    write_file(urls)
    print 'over'
