# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-08-20 15:00:01

import requests
from bs4 import BeautifulSoup as soup
from common import get_community_list, write_file
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_woaiwojia_url(urls, rental):
    # 获取网页内容
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36'
    }
    cur_url = 'http://bj.5i5j.com/rent/_' + rental
    common_url = 'http://bj.5i5j.com'
    # data = {"qwd": rental}
    s = requests.session()
    # r = s.get(cur_url, headers=headers, params=data)
    r = s.get(cur_url, headers=headers)
    r.encoding = 'utf-8'
    html = soup(r.text)
    house_list = html.findAll('div', {"id": "exchangeList"})
    ul = house_list[0].find('ul', {"class": "list-body"})
    lis = ul.findAll('li')
    for li in lis:
        h2 = li.find('h2')
        if not h2:
            continue
        a = h2.find('a')
        url = a['href']
        desc = li.find('li', {"class": "font-balck"}).text
        # time = li.find('li', {"class": "publish"}).text
        h3 = li.findAll('h3')
        name = h3[0].text.strip()
        price = h3[1].text
        url = common_url + url
        if rental not in name:
            continue
        print url
        print name
        print desc
        print price
        urls.append(name + ' | ' + desc + ' | ' + price + ' | ' + url)
    return urls


def get_house_list():
    house_list = []
    rentals = get_community_list()
    for rental in rentals:
        house_list = get_woaiwojia_url(house_list, rental)
    return house_list


if __name__ == '__main__':
    urls = get_house_list()
    write_file(urls, 'woaiwojia.txt')
    get_woaiwojia_url([], '')
    print 'over'
