# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-08-18 17:54:02

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_community_list():
    return ['世纪龙祥嘉园', '翠堤春晓', '林奥嘉园', '新街坊', '平安嘉苑',
            '清友园', '茉藜园', '绣菊园', '蕴实园', '来春园', '北京青年城',
            '来北家园', '望春园', '旭辉奥都', '拂林园', '天居园', '天畅园',
            '上元君庭', '天月园', '天翠园', '万科星园', '筑华年',
            '佳兴园', '美立方']


# 写文件
def write_file(house_list, filename):
    file_object = open(filename, 'w')
    for house in house_list:
        file_object.write(house + '\n')
    file_object.close()
