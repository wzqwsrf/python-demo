# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-09-25 18:37:15
# 内置函数getattr hasattr setattr delattr


"""getattr()函数是Python自省的核心函数，具体使用大体如下：
   获取对象引用getattr
   getattr用于返回一个对象属性，或者方法
"""


class A:
    def __init__(self):
        self.name = "zhenqing.wang"

    def get_name(self):
        print "My name is %s" % self.name


def test_getattr():
    li = ['zhenqing.wang', 'wzqwsrf']
    print getattr(li, "pop")
    print li.pop
    print li
    li.pop()
    print li
    getattr(li, "pop")()
    print li
    getattr(li, "append")("more")
    print li


def main():
    a = A()
    print getattr(a, 'name', 'not find name')
    print getattr(a, 'age', 'not find age')
    print getattr(a, 'get_name', 'default')
    getattr(a, 'get_name', 'default')() # 调用A中的get_name() 等同于a.get_name()
    print hasattr(a, "name")  # 有name属性
    setattr(a, 'age', 25)
    print a.age
    delattr(a, 'age')
    print getattr(a, 'age', 'not find age')


if __name__ == "__main__":
    main()
    print '\n=====test []=====\n'
    test_getattr()



"""注：使用getattr可以轻松实现工厂模式。
例：一个模块支持html、text、xml等格式的打印，
根据传入的format参数的不同，调用不同的函数实现几种格式的输出

import statsout

def output(data, format="text"):
    output_function = getattr(statsout, "output_%s" % format)
    return output_function(data)

"""
