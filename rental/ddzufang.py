# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-08-17 14:07:29

import requests
from bs4 import BeautifulSoup as soup
from common import get_community_list, write_file
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_ddzufang_url(urls, rental):
    # 获取网页内容
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36'
    }
    cur_url = 'http://www.zufangzi.com/house/houseControllor/houseListPage.do'
    data = {"keyword": rental}
    s = requests.session()
    r = s.get(cur_url, headers=headers, params=data)
    r.encoding = 'utf-8'
    html = soup(r.text)
    house_list = html.findAll('div', {"id": "houseList"})
    divs = house_list[0].findAll('div', {"class": "listCon wid1000"})
    for div in divs:
        div_left = div.find('div', {"class": "listCon_c_l"})
        div_right = div.find('div', {"class": "listCon_c_r"})
        ps = div_left.findAll('p')
        a = ps[0].find('a')
        name = a.text
        url = a['href']
        desc = ps[1].text
        price = div_right.find('dt')
        price = price.find('span').text
        if rental not in name:
            continue
        print url
        print desc
        print name
        print price
        urls.append(name + ' | ' + desc + ' | ' + price + ' | ' + url)
    return urls


def get_house_list():
    house_list = []
    rentals = get_community_list()
    for rental in rentals:
        house_list = get_ddzufang_url(house_list, rental)
    return house_list


if __name__ == '__main__':
    urls = get_house_list()
    write_file(urls, 'ddzufang.txt')
    print 'over'
