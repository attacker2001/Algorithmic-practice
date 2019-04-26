#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [4]Twice linear.py 
@time: 2018/11/20
@project: Algorithm-Exercise 
@software: PyCharm
"""

"""
https://www.codewars.com/kata/twice-linear/train/python

Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

#Task: Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u.

#Example: dbl_linear(10) should return 22

#Note: Focus attention on efficiency


难点是对重复数字的处理

"""


def dbl_linear(n):
    total_list = [1]
    i = 0
    j = 0
    while len(total_list) <= n:
        x = 2 * total_list[i] + 1
        y = 3 * total_list[j] + 1
        if x <= y:
            i += 1
        if x >= y:
            j += 1
        total_list.append(min(x, y))

    return total_list[n]


if __name__ == '__main__':
    print dbl_linear(10), " Answer is:", 22
    print dbl_linear(20), " Answer is:", 57
    print dbl_linear(30), " Answer is:", 91
    print dbl_linear(50), " Answer is:", 175

"""

(1)
from collections import deque

def dbl_linear(n):
    h = 1; cnt = 0; q2, q3 = deque([]), deque([])
    while True:
        if (cnt >= n):
            return h
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0], q3[0])
        if h == q2[0]: h = q2.popleft()
        if h == q3[0]: h = q3.popleft()
        cnt += 1

(2)
def dbl_linear(n):
  num_list = [1]
  for i in num_list:
    num_list.append((i * 2) + 1)
    num_list.append((i * 3) + 1)
    if len(num_list) > n *10:
      break
  return sorted(list(set(num_list)))[n]

"""
