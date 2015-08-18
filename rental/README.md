## 关于rental
1. 获取自如和丁丁租房的所有关注的小区的房源信息。
2. 小区，价格，以及链接地址。
3. 帝都租房好难。。。
4. 自如和丁丁租房的前端开发好像是同一拨人。
5. 居然不限制爬虫。

## 结果
1. 生成相关的txt文件。
2. 根据第一次生成的租房信息，后面每次都比对信息，一旦有新出的房子，立马发邮件给我。
3. 邮件内容是这样的：
   
   ![在这里](https://github.com/wzqwsrf/python-demo/blob/master/rental/compare_ddzufang.png)

## 类
1. **[ddzufang.py](https://github.com/wzqwsrf/python-demo/blob/master/rental/ddzufang.py)** 用来抓取丁丁租房所有附近小区的信息。
2. **[ziru.py](https://github.com/wzqwsrf/python-demo/blob/master/rental/ziru.py)**用来抓取自如所有附近小区的信息。
3. **[compare_ddzufang.py](https://github.com/wzqwsrf/python-demo/blob/master/rental/compare_ddzufang.py)**用来比较丁丁租房信息更新。