# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-06-29 14:32:07


import requests
from BeautifulSoup import BeautifulSoup as soup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 根据登陆url，用户名，密码获取登陆后的requests
def get_login_requests(loginUrl, userId, password):
    # 获取网页内容
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.130 Safari/537.36'
    }
    s = requests.session()
    data = dict(user_id=userId, password=password)
    s.post(loginUrl, data=data, headers=headers)
    return s


# 获取每道题目的Java内容
def get_every_java_solution(s, probId, userId):
    # 获取网页内容
    r = s.get('http://ac.jobdu.com/status.php?pid=' +
              str(probId) + '&user_id=' + userId)
    # 修改编码格式，否则输出为乱码
    r.encoding = 'utf-8'
    data = r.text
    # 获取所有table内容，主要获取我的提交历史。这里的table应该只有一个。
    table = soup(data).findAll('table')
    if len(table) == 0:
        return ''
    # 理论上来讲，获取第一个table就可以。好像实际也是这样
    table = table[0]
    # 开始获取每一行了，应该是每个tbody。有多少行就有多少个tbody
    tbody = table.findAll('tbody')
    tbodyLen = len(tbody)
    for i in range(tbodyLen):
        body = tbody[i]
        # 针对每个body取出td。
        tds = body.findAll(name="td")
        yuyan = tds[8].text
        # 列值是有规律的，不再遍历，10列
        ac = tds[3].find('font').string
        if ac != 'Accepted' or 'Java' not in yuyan:
            continue
        url = 'http://ac.jobdu.com/showsource.php?sid=' + tds[0].string
        urlr = s.get(url)
        urlr.encoding = 'utf-8'
        code = urlr.text
        pre = soup(code, convertEntities=soup.HTML_ENTITIES).findAll('pre')
        if len(pre) == 0:
            print probId
            print url
            print pre
        print pre
        return pre[0].string


# 获取文件名
def get_prob_names(s, probId):
    r = s.get('http://ac.jobdu.com/problem.php?pid=' + str(probId))
    r.encoding = 'utf-8'
    data = r.text
    # 获取所有table内容，主要获取我的提交历史。这里的table应该只有一个。
    table = soup(data, convertEntities=soup.HTML_ENTITIES)
    # print table
    head = table.findAll('dt', {"class": "title-hd"})
    # print type(head[0])
    return head[0].text


# 写文件
def writeStr(filename, code):
    print type(filename)
    filename = filename.encode('utf-8', 'ignore')
    file_object = open('Java/' + filename + '.java', 'w')
    file_object.write(code)
    file_object.close()


# 主函数
def print_all_problems():
    num = 1557
    start = 1001
    login_url = 'http://ac.jobdu.com/login.php'
    username = 'wzqwsrf'
    password = 'password'
    while start <= num:
        s = get_login_requests(login_url, username, password)
        code = get_every_java_solution(s, start, username)
        if code is None or code == '':
            start += 1
            continue
        print type(code)
        filename = get_prob_names(s, start)
        print filename
        writeStr(filename, code)
        start += 1


if __name__ == '__main__':
    print_all_problems()
    print 'over'
