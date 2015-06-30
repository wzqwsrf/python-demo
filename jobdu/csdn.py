# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-06-30 13:47:19


import requests
from BeautifulSoup import BeautifulSoup as soup
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
        r = s.get('http://blog.csdn.net/u013027996/article/list/' + str(x), headers=headers)
        # 这里主要转义一些特殊符号，如<会有问题
        r.encoding = 'utf-8'
        # , 'id': 'article_list'
        # print r.text
        html = soup(r.text, convertEntities=soup.HTML_ENTITIES)
        link_titles = html.findAll('span', {"class": "link_title"})
        # print articles
        for link_title in link_titles:
            common_url = 'http://blog.csdn.net'
            title = link_title.text
            url = common_url + link_title.find('a')['href']
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
