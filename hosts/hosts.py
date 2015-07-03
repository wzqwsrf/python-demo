# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-06-29 14:32:07


import sys
import requests
from bs4 import BeautifulSoup as soup

reload(sys)
sys.setdefaultencoding("utf-8")


def get_hosts_contents():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36'
    }
    url = 'http://www.awolau.com/hosts/google-hosts.html'
    # 因为awolau反爬虫，所以加上头文件，模拟浏览器访问。
    # 判断是否反爬虫，打印status_code，一般可以看到text有内容但是状态码为403
    r = requests.get(url=url, headers=headers)
    r.encoding = 'utf-8'
    print r.status_code
    data = r.text
    pres = soup(data).findAll('pre')
    content_list = []
    for span in pres[1].findAll('span', {"class": "line"}):
        contents = span.contents
        clen = len(contents)
        print clen
        # print contents
        if '2015' in span.text:
            content_list.append(span.text)
            continue
        if clen != 4 and clen != 6 and clen != 8:
            content_list.append(span.text)
            continue
        text = ''
        for x in xrange(0, 3):
            text += contents[x].string
        for x in xrange(0, 17-len(text)):
            text += ' '
        for x in xrange(3, clen):
            text += contents[x].string.strip()
        content_list.append(text)
    return content_list


# 写文件
def write_file(content_list):
    file_object = open('hosts.txt', 'w')
    for content in content_list:
        file_object.write(content + '\n')
    file_object.close()


if __name__ == '__main__':
    txt = get_hosts_contents()
    write_file(txt)
