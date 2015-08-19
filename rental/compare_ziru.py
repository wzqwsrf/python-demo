# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-08-19 09:56:12

import requests
from bs4 import BeautifulSoup as soup
from common import get_community_list
from send_mail import send_to_special
import datetime
import time
import os
import os.path
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def read_file(filename):
    house_list = []
    lines = open(filename).readlines()
    for line in lines:
        line = line.replace('\n', '')
        line = line.split('|')[-1]
        house_list.append(line.strip())
    return house_list


def get_ziru_url(house_list_old, urls, new_urls, rental):
    # 获取网页内容
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36'
    }
    cur_url = 'http://www.ziroom.com/z/nl/'
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
        if url not in house_list_old:
            print url
            urls.append(name + ' | ' + data_addr + ' | ' + price + ' | ' + url)
        new_urls.append(name + ' | ' + data_addr + ' | ' + price + ' | ' + url)
    return [urls, new_urls]


def get_house_list(old_house_list):
    house_list = [[],[]]
    rentals = get_community_list()
    for rental in rentals:
        house_list = get_ziru_url(old_house_list, house_list[0], house_list[1], rental)
    return house_list


def get_filename():
    curtime = datetime.datetime.today()
    year_time = curtime.strftime('%Y-%m-%d')
    hour_time = curtime.strftime('%H:%M:%S')
    time_array = hour_time.split(':')
    first = int(time_array[0]) * 12
    last = int(time_array[1]) / 5
    index = first + last
    old_index = index - 1
    filename = 'ziru_' + year_time + '_' + str(index) + '.txt'
    old_filename = 'ziru_' + year_time + '_' + str(old_index) + '.txt'
    return [old_filename, filename]


def write_file(house_list, filename):
    file_object = open(filename, 'w')
    for house in house_list:
        file_object.write(house + '\n')
    file_object.close()


def main():
    file_names = get_filename()
    file_lines = read_file(file_names[0])
    house_list = get_house_list(file_lines)
    write_file(house_list[1], file_names[1])
    if len(house_list[0]):
        msg = ''
        for house in house_list[0]:
            msg = msg + house + '\n'
        send_to_special('自如友家', msg)
        print msg
        print 'send_over'
    if os.path.isfile(file_names[0]):
        os.remove(file_names[0])
    print 'over'


if __name__ == '__main__':
    while True:
        main()
        time.sleep(300)
