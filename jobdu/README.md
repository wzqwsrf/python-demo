## 关于Jobdu
------
1. 刷题网站，类似于leetcode。<http://ac.jobdu.com/index.php>
2. 初衷，基本刷完，想将代码提交至github，但是每次复制粘贴好麻烦。
3. 用python写个爬虫，将所有的题目代码爬下来，按照题目分成多个文件。


## python第三方依赖
------
1. **`requests`**
2. **`beautifulsoup4`**
3. 可以使用如下命令安装第三方依赖包。
   - `pip install requests`
   - `pip install beautifulsoup4`
4. 或者安装**`virtualenv`**
   - `virtualenv .venv`
   - `source .venv/bin/active`
   - `pip install requests`
   - `pip install beautifulsoup4`
   

## 运行
------
1. Python部分。
   - 直接运行jobdu.py会产生所有AC题目的Java或者C++代码。根据需要可以修改路径和用户名密码。
   - 运行方式可以为`python jobdu.py`或者使用**Pycharm**导入项目以后运行。
2. Java部分。
   - 抓取的代码格式会乱，没有格式化。
   - 调用eclipse快捷键的内部代码，对产生的Java代码进行格式化。
   - 请根据实际情况调整代码路径。
   - maven依赖  
   
     ```
        <dependency>
            <groupId>org.eclipse.jdt</groupId>
            <artifactId>core</artifactId>
            <version>3.1.1</version>
        </dependency>
        <dependency>
            <groupId>org.eclipse.jface</groupId>
            <artifactId>text</artifactId>
            <version>3.3.0-v20070606-0010</version>
        </dependency>
        <dependency>
            <groupId>org.eclipse.text</groupId>
            <artifactId>org.eclipse.text</artifactId>
            <version>3.5.101</version>
        </dependency>
     ```
    