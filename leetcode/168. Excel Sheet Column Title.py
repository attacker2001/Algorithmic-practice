#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 168. Excel Sheet Column Title.py 
@time: 2019/05/07

Description:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"


Input: 703
Output: "AAA"
"""


class Solution:
    def convertToTitle(self, num):
        return "" if num == 0 else self.convertToTitle((num - 1) // 26) + chr((num - 1) % 26 + ord('A'))


if __name__ == '__main__':
    a = Solution()
    # print(a.convertToTitle(1))
    # print(a.convertToTitle(28))
    # print(a.convertToTitle(701))
    print(a.convertToTitle(6203))

"""
My other solutions:


Other solutions:

def convertToTitle(self, n):
    return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))
"""
