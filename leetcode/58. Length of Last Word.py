#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 58. Length of Last Word.py 
@time: 2020/02/17

URL:
https://leetcode.com/problems/length-of-last-word/

Description:
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in s.split(' ')[::-1]:
            if i:
                return len(i)
        else:
            return 0


if __name__ == '__main__':
    a = Solution()
    print(a.lengthOfLastWord("Hello World"))
    print(a.lengthOfLastWord("Hello !"))
    print(a.lengthOfLastWord("Hello "))
    print(a.lengthOfLastWord("a") == 1)
    print(a.lengthOfLastWord(" 2  World  2         "))
    print(a.lengthOfLastWord("    2         "))

"""
My other solutions:


Other solutions:
def lengthOfLastWord(self, s):
    return len(s.rstrip(' ').split(' ')[-1])


def lengthOfLastWord(self, s):
    return len(s.strip().split(' ')[-1])


def lengthOfLastWord(self, s):
    return 0 if len(s.split()) == 0 else len(s.split()[-1])
"""
