#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [6]plus-1-array.py 
@time: 2018/11/20
@project: Algorithm-Exercise 
@software: PyCharm
"""

"""
https://www.codewars.com/kata/plus-1-array/train/python

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

For example an array [2, 3, 9] equals 239, add one would return an array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (language equivalent) for invalid inputs

"""


def up_array(arr):
    if arr:
        for i in arr:
            if i < 0 or i >= 10:
                return
        return [int(x) for x in str(int("".join([str(i) for i in arr])) + 1)]
    else:
        return


if __name__ == '__main__':
    print up_array([2, 3, 9])
    print up_array([4, 3, 2, 5])

"""
Other solutions:
(1)
def up_array(arr):
  if not arr or min(arr) < 0 or max(arr) > 9:
    return None
  else:
    return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
      
(2)
def up_array(arr):
    return None if arr==[] or any([x not in range(10) for x in arr]) else [int(c) for c in str(int("".join([str(x) for x in arr]))+1)]
    

(3)
def up_array(arr):
    if arr and all(0 <= x <= 9 for x in arr):
        return map(int, str(int(''.join(map(str, arr))) + 1))

"""
