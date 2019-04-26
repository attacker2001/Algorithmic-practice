#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 7. Reverse Integer.py 
@time: 2019/04/23
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−2^31,  2^31 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.

"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        Runtime: 40 ms, faster than 99.92% of Python3 online submissions for Reverse Integer.
        Memory Usage: 13 MB, less than 5.71% of Python3 online submissions for Reverse Integer.
        :param x:
        :return:
        """
        if x > 0:
            return int(str(x)[::-1]) if int(str(x)[::-1]) <= 2**31-1 else 0
        elif x == 0:
            return 0
        else:
            return -1 * self.reverse(-x)


if __name__ == '__main__':
    test = Solution()
    print(test.reverse(1534236469))
    print(test.reverse(1563847412))
