#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [6]persistent-bugger.py 
@time: 2018/12/05
@project: Algorithm-Exercise 
@software: PyCharm
"""

"""
https://www.codewars.com/kata/persistent-bugger/train/python


Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number

"""


def x(n):
    temp = 1
    for i in str(n):
        temp *= int(i)
    return str(temp)


def persistence(n):
    # your code
    count = 0
    if len(str(n)) > 1:
        result = x(n)
        count += 1
        while len(result) > 1:
            result = x(result)
            count += 1

    return count


if __name__ == '__main__':
    print persistence(39), 3
    print persistence(4), 0
    print persistence(25), 2
    print persistence(999), 4


"""
Other solutions:

# (1)
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
    
# (2)
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist

# (3)
from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1

"""