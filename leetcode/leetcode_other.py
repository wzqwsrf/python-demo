# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-07-17 14:37:25

import requests
from bs4 import BeautifulSoup as soup
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')


# 根据登陆url，用户名，密码获取登陆后的requests
def get_login_requests(login_url, user_id, password):
    # 获取网页内容
    s = requests.session()
    data = dict(login=user_id, password=password, csrfmiddlewaretoken='kJlv5K5pKS2AJ2oN6PXcAEY2aOWo2Tl6')
    cookies = {
        '__atuvc': '63%7C26%2C36%7C27%2C55%7C28',
        '_gat': '1',
        'csrftoken': 'kJlv5K5pKS2AJ2oN6PXcAEY2aOWo2Tl6',
        '_ga': 'GA1.2.764974747.1435544317'
    }
    headers = {
        'Referer': "https://leetcode.com/accounts/login/",
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36',
        'Host': 'leetcode.com'
    }
    s.post(login_url, data=data, headers=headers,
           cookies=cookies)
    return s


# 获取leetcode列表
def get_leetcode_url(s):
    urls = []
    cur_url = 'https    ://leetcode.com/problemset/algorithms/'
    r = s.get(cur_url)
    r.encoding = 'utf-8'
    html = soup(r.text)
    problem_list = html.findAll('table', {"id": "problemList"})
    tbody = problem_list[0].find('tbody')
    common_url = 'https://leetcode.com'
    trs = tbody.findAll('tr')
    for tr in trs:
        tds = tr.findAll('td')
        prob_id = tds[1].text.replace('\n', '')
        prob_name = tds[2].text.replace('\n', '')
        url = tds[2].find('a')['href']
        # print prob_id + ' ' + prob_name
        # print common_url + url
        urls.append(prob_id + '||' + prob_name + '||' + common_url + url)
    return urls


# 获取每道题目的Java内容
def get_every_java_solution(s, url):
    # 获取网页内容
    print url + 'submissions/'
    r = s.get(url + 'submissions/')
    # 修改编码格式，否则输出为乱码
    r.encoding = 'utf-8'
    data = r.text
    # 获取所有table内容，主要获取我的提交历史。这里的table应该只有一个。
    table = soup(data).findAll('table')
    if len(table) == 0:
        return ''
    # 理论上来讲，获取第一个table就可以。好像实际也是这样
    table = table[0]
    # 开始获取每一行了，应该是每个tr
    tbody = table.findAll('tbody')
    trs = tbody[0].findAll('tr')
    for i in range(len(trs)):
        tr = trs[i]
        tds = tr.findAll('td')
        td = tds[2]
        a = td.find('a')
        ac = a.find('strong').text
        href = a['href']
        if ac != 'Accepted':
            continue
        url = 'https://leetcode.com/' + href
        urlr = s.get(url)
        urlr.encoding = 'utf-8'
        code = urlr.text
        pres = soup(code).findAll('script')
        pre = pres[len(pres) - 5]
        pre = str(pre.text)
        listp = pre.split('\n')
        for p in listp:
            if 'scope.code.java' in p:
                print p


# 写文件
def write_file(filename, code):
    print type(filename)
    filename = filename.encode('utf-8', 'ignore')
    file_object = open('c++/' + filename + '.cpp', 'w')
    file_object.write(code)
    file_object.close()


# 主函数
def print_all_problems():
    username = 'wzqwsrf@126.com'
    password = 'password'
    login_url = 'https://leetcode.com/accounts/login/'
    s = get_login_requests(login_url, username, password)
    get_every_java_solution(s, 'https://leetcode.com/problems/product-of-array-except-self/')
    # urls = get_leetcode_url(s)
    # k = 0
    # for url in urls:
    #     print url
    #     get_every_java_solution(s, url.split('||')[2])
    #     k += 1
    #     if k >= 1:
    #         break


if __name__ == '__main__':
    print_all_problems()
    print 'over'
