# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-07-01 17:26:57

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 写文件
def write_file(list3):
    file_object = open('not_in_github.txt', 'w')
    for name in list3:
        file_object.write(name + '\n')
    file_object.close()


# 读取txt文件
def get_leetcode_names():
    list1 = []
    file_object = open('leetcode.txt')
    try:
        lines = file_object.readlines()
        for line in lines:
            line_array = line.split('||')
            prob_name = line_array[1]
            prob_id = line_array[0]
            if len(prob_id) == 1:
                prob_id = '00' + prob_id
            elif len(prob_id) == 2:
                prob_id = '0' + prob_id
            full_name = prob_id + ' ' + prob_name
            list1.append(full_name)
    finally:
        file_object.close()
    return list1


# 读取txt文件
def get_github_names():
    list2 = []
    file_object = open('github.txt')
    try:
        lines = file_object.readlines()
        for line in lines:
            list2.append(line.replace('\n', '').strip().replace('.java', ''))
    finally:
        file_object.close()
    return list2


# 获取没有提交的题目列表
def get_not_github():
    list3 = []
    list1 = get_leetcode_names()
    list2 = get_github_names()
    for name in list1:
        if name not in list2:
            list3.append(name)
    write_file(list3)


# 创建文件
def create_files(prob_dict):
    file_object = open('not_in_github.txt')
    for line in file_object.readlines():
        file_write = open(line + '.java', 'w')
        file_write.write('\n')
        file_write.write('//' + line[3:] + '\n')
        file_write.write('/**' + '\n')
        file_write.write(' * @author:wangzq' + '\n')
        file_write.write(' * @email:wangzhenqing1008@163.com' + '\n')
        file_write.write(' * @date:2015-07-02 16:57:36' + '\n')
        file_write.write(' * @url:' + prob_dict[line.replace('\n', '')])
        file_write.write(' */' + '\n')
    file_object.close()


# 读取txt文件
def get_filename_by_probname():
    probname_dict = {}
    file_object = open('leetcode.txt')
    try:
        lines = file_object.readlines()
        for line in lines:
            line_array = line.split('||')
            prob_name = line_array[1]
            prob_id = line_array[0]
            if len(prob_id) == 1:
                prob_id = '00' + prob_id
            elif len(prob_id) == 2:
                prob_id = '0' + prob_id
            full_name = prob_id + ' ' + prob_name
            # if 'Best Time to Buy and Sell Stock IV' in full_name:
            #     print line_array
            #     print line_array[2]
            probname_dict[full_name] = line_array[2]
    finally:
        file_object.close()
    return probname_dict


if __name__ == '__main__':
    # prob_dict = get_filename_by_probname()
    get_not_github()
    print 'over'
