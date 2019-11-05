#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 43. Multiply Strings.py 
@time: 2019/11/05


Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


if __name__ == '__main__':
    a = Solution()
    print(a.multiply('456', '5416456'))
    print(int(a.multiply('45456555555556', '5416456')) == 45456555555556*5416456)

"""
def multiply(self, num1, num2):
    res = 0
    carry1 = 1
    for n1 in num1[::-1]:
        carry2 = 1
        for n2 in num2[::-1]:
            res += int(n1)*int(n2)*carry1*carry2
            carry2 *= 10
        carry1 *= 10
    return str(res)

i think it's not work at "res += int(n1)*int(n2)carry1carry2" when res is vary large.
you should turn res to a string then do the ''+''.

"""
