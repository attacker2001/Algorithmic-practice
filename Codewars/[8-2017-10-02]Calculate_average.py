#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/2 17:04
# @Author  : attacker2001
# @Site    : 
# @File    : [8-2017-10-02]Calculate_average
# @Software: PyCharm

# coding=utf-8

"""
Description:

Write function avg which calculates average of numbers in given list.

"""


def find_average(array):
    if array:
        return sum(array) / len(array)
    else:
        return 0


if __name__ == '__main__':
    print find_average([1, 2, 3])

"""
Other solution:
def find_average(array):
    return sum(array) / len(array) if array else 0

上述是Python的三元表达式写法


def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0
直接用异常处理进行判断

"""
