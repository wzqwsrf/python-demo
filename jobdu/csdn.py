# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-06-30 13:47:19


import requests
from bs4 import BeautifulSoup as soup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 获取csdn列表
def get_cdsn_url():
    urls = []
    # 获取网页内容
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36'
    }
    for x in xrange(1, 20):
        print x
        s = requests.session()
        cur_url = 'http://blog.csdn.net/u013027996/article/list/' + str(x)
        r = s.get(cur_url, headers=headers)
        # 这里主要转义一些特殊符号，如<会有问题
        r.encoding = 'utf-8'
        # , 'id': 'article_list'
        # print r.text
        html = soup(r.text)
        link_titles = html.findAll('span', {"class": "link_title"})
        common_url = 'http://blog.csdn.net'
        for link_title in link_titles:
            a = link_title.find('a')
            title = ''
            for s in a.stripped_strings:
                if s != '':
                   title = s
            url = common_url + a['href']
            print url
            url = title + '||' + url
            print url
            if url in urls:
                continue
            urls.append(url)
    return urls


# 写文件
def write_file(urls):
    file_object = open('url.txt', 'w')
    for url in urls:
        file_object.write(url + '\n')
    file_object.close()


if __name__ == '__main__':
    urls = get_cdsn_url()
    write_file(urls)
    print 'over'
