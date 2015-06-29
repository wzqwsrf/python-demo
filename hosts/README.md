## 关于hosts
------
1. 持续关注<http://www.awolau.com/hosts/google-hosts.html> 并且更新hosts文件。
2. 每次都需要大量的复制粘贴，我又懒得做。
3. 所以我将内容爬下来了。
4. 该博客反爬虫，所以使用了浏览器模拟登陆，即增加了headers。


## 运行
------
1. 安装第三方依赖包`requests`,`BeautifulSoup`即可。
2. `python hosts.py`会在当前目录下产生hosts文件。
3. 追加到**/etc/hosts**文件中即可。