# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wzqwsrf'

import re
import requests
from BeautifulSoup import BeautifulSoup as soup

# 获取网页内容
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}
s = requests.session()
data = dict(user_id="wzqwsrf", password='password')
s.post('http://ac.jobdu.com/login.php', data=data, headers=headers)
r = s.get('http://ac.jobdu.com/problem.php?pid=1516')
r.encoding = 'utf-8'
data = r.text
# 获取所有table内容，主要获取我的提交历史。这里的table应该只有一个。
table = soup(data, convertEntities=soup.HTML_ENTITIES)
# print table
head = table.findAll('dt', {"class": "title-hd"})
print type(head[0])
print head[0].text
divs = table.find('div', {"class": "topic-desc-bd"})
lines = divs.getText('\r\n')
# print len(lines)
# print lines.strip().replace(' ', '')
bs = divs.findAll('b')
# print bs
ps = divs.findAll('p')
# print ps
pres = divs.findAll('pre')[0].getText('\n')
# print pres

reg1 = re.compile("<[^>]*>")
content = reg1.sub(' ',divs.prettify())
# content = content.replace('\n','')
# print content
print type(content)

file_object = open('1.md', 'w')
file_object.write(content)
file_object.close()

# file_object = open('1.md','w')

# print type(title.string)
# print title.stripped_strings
# 修改编码格式，否则输出为乱码

