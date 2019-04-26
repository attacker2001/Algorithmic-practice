#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 709. To Lower Case.py 
@time: 2019/04/26

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
Accepted
96,655
Submissions
126,129
"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        """
        Runtime: 36 ms, faster than 76.82% of Python3 online submissions for To Lower Case.
        Memory Usage: 13 MB, less than 5.45% of Python3 online submissions for To Lower Case.
        """
        return str.lower()


if __name__ == '__main__':
    a = Solution()
    print(a.toLowerCase('Hello'))

"""
Other solutions:

class Solution:
    def toLowerCase(self, str): 
        '''
        Runtime: 36 ms, faster than 76.82% of Python3 online submissions for To Lower Case.
        Memory Usage: 13.1 MB, less than 5.45% of Python3 online submissions for To Lower Case.
        '''
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)


class Solution:
    def toLowerCase(self, str): 
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)
"""
