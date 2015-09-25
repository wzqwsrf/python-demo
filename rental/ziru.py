# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-08-17 10:15:33

import requests
from bs4 import BeautifulSoup as soup
from common import get_community_list, write_file
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_ziru_url(urls, rental):
    # 获取网页内容
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36'
    }
    cur_url = 'http://www.ziroom.com/z/nl/'
    common_url = 'http://www.ziroom.com'
    data = {"qwd": rental}
    s = requests.session()
    r = s.get(cur_url, headers=headers, params=data)
    r.encoding = 'utf-8'
    html = soup(r.text)
    house_list = html.findAll('ul', {"id": "houseList"})
    lis = house_list[0].findAll('li')
    for li in lis:
        div = li.find('div', {"class": "txt"})
        h3 = div.find('h3')
        box = div.find('div', {"class": "box"})
        a = h3.findAll('a')[-1]
        url = a['href']
        name = a.text
        data_addr = h3.find('b')['data-addr'].replace('\n', '')
        data_addr = str(data_addr)
        data_addr = data_addr.split(" ")[0]
        price = box.find('p', {"class": "p1"})
        price = price.find('span', {"class": "en"}).text
        if rental not in data_addr:
            continue
        print url
        print data_addr
        print name
        print price
        urls.append(name + ' | ' + price + ' | ' + data_addr + ' | ' + common_url + url)
    return urls


def get_house_list():
    house_list = []
    rentals = get_community_list()
    for rental in rentals:
        house_list = get_ziru_url(house_list, rental)
    return house_list


if __name__ == '__main__':
    urls = get_house_list()
    write_file(urls, 'ziru.txt')
    print 'over'
