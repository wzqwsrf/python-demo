# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-08-17 14:07:29

import requests
from bs4 import BeautifulSoup as soup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 获取leetcode列表
def get_ziru_url(urls, rental):
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
        print url
        print desc
        print name
        print price
        urls.append(name + ' | ' + desc + ' | ' + price + ' | ' + url)
    return urls


def get_community_list():
    return ['世纪龙翔嘉园', '翠堤春晓', '林奥嘉园', '新街坊', '平安嘉苑', '清友园',
            '茉藜园', '绣菊园', '蕴实园', '来春园', '北京青年城', '来北家园',
            '望春园', '旭辉奥都', '拂林园', '天居园', '天畅园', '上元君庭']


def get_all_data():
    all_data = []
    rentals = get_community_list()
    for rental in rentals:
        all_data = get_ziru_url(all_data, rental)
    return all_data


# 写文件
def write_file(urls):
    file_object = open('ddzufang.txt', 'w')
    for url in urls:
        file_object.write(url + '\n')
    file_object.close()


if __name__ == '__main__':
    urls = get_all_data()
    write_file(urls)
    print 'over'
