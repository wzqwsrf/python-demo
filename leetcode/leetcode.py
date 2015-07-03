# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-07-01 17:08:11

import requests
from bs4 import BeautifulSoup as soup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 获取leetcode列表
def get_leetcode_url():
    urls = []
    # 获取网页内容
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36'
    }
    cur_url = 'https://leetcode.com/problemset/algorithms/'
    s = requests.session()
    r = s.get(cur_url, headers=headers)
    r.encoding = 'utf-8'
    html = soup(r.contents)
    problem_list = html.findAll('table', {"id": "problemList"})
    tbody = problem_list[0].find('tbody')
    common_url = 'https://leetcode.com'
    trs = tbody.findAll('tr')
    for tr in trs:
        tds = tr.findAll('td')
        prob_id = tds[1].text
        prob_name = tds[2].text
        url = tds[2].find('a')['href']
        # print prob_id + ' ' + prob_name
        # print common_url + url
        urls.append(prob_id + '||' + prob_name + '||' + common_url + url)
    return urls


# 写文件
def write_file(urls):
    file_object = open('leetcode.txt', 'w')
    for url in urls:
        file_object.write(url + '\n')
    file_object.close()


if __name__ == '__main__':
    urls = get_leetcode_url()
    write_file(urls)
    print 'over'
