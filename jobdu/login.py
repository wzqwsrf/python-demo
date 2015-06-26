__author__ = 'wzqwsrf'
# encoding:utf-8

import re
import requests
from BeautifulSoup import BeautifulSoup as soup

# 获取网页内容
headers = {
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}
s = requests.session()
data = dict(user_id="wzqwsrf", password='wzq881021')
s.post('http://ac.jobdu.com/login.php', data=data, headers=headers)
r = s.get('http://ac.jobdu.com/showsource.php?sid=1298941')
r.encoding = 'utf-8'
data = r.text
# 获取所有table内容，主要获取我的提交历史。这里的table应该只有一个。
table = soup(data, convertEntities=soup.HTML_ENTITIES).findAll('pre')
print table[0].string
# 修改编码格式，否则输出为乱码