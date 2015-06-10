__author__ = 'wzqwsrf'
# encoding:utf-8

import re
import requests
# 获取网页内容
r = requests.get('https://leetcode.com/problemset/algorithms/')
data = r.text
# 利用正则查找所有连接
linkList = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
allList1 = []
for url in linkList:
    if url[1:9] == 'problems':
        urlInfo = url.split('/')
        allList1.append(urlInfo[2])


r = requests.get('https://github.com/wzqwsrf/Leetcode/tree/master/Java')
data = r.text
# 利用正则查找所有连接
linkList = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
# linkList = re.findall(r"('/wzqwsrf/Leetcode/blob/master/Java/')", data)
allList2 = []
for url in linkList:
    prefix = '/wzqwsrf/Leetcode/blob/master/Java/'
    if prefix in url:
        url = url.replace(prefix, '')
        url = url.replace('.java', '')
        url = url.replace('_', '-')
        url = url.lower()
        allList2.append(url)

print 'sort-colors' not in allList1
print 'sort-colors' not in allList2

file_object = open('3.txt', 'w')
for url in allList1:
    print url
    if url not in allList2:
        file_object.write(url)
        file_object.write('\n')
file_object.close()

# file_object = open('1.txt', 'w')
# for url in allList1:
#     file_object.write(url)
#     file_object.write('\n')
# file_object.close()
#
# file_object = open('2.txt', 'w')
# for url in allList2:
#     file_object.write(url)
#     file_object.write('\n')
#
# file_object.close()