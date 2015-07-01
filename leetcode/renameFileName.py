# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-07-01 17:26:57

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 获取目录下的所有文件
def get_directory_files(path, newpath, prob_dict):
    current_files = os.listdir(path)
    print len(current_files)
    files = []
    for file_name in current_files:
        file_name = os.path.join(path, file_name)
        file_object = open(file_name)
        new_file_name = ''
        code = ''
        k = 0
        for line in file_object.readlines():
            if k == 1:
                key = line.replace('//', '').strip()
                new_file_name = prob_dict[key]
            code += line + '\n'
            k += 1
        if new_file_name not in files:
            files.append(new_file_name)
        else:
            print file_name
        new_file_name = os.path.join(newpath, new_file_name)
        write_file(new_file_name, code)


# 写文件
def write_file(file_name, code):
    file_object = open(file_name, 'w')
    file_object.write(code)
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
            probname_dict[prob_name] = full_name
    finally:
        file_object.close()
    return probname_dict


if __name__ == '__main__':
    prob_dict = get_filename_by_probname()
    path = '/Users/wangzhenqing/git_work/python-demo/leetcode/test1'
    newpath = '/Users/wangzhenqing/git_work/python-demo/leetcode/test2'
    get_directory_files(path, newpath, prob_dict)
    print 'over'
