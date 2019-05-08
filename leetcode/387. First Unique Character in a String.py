#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 387. First Unique Character in a String.py 
@time: 2019/05/08

Description:
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq_list = [s.index(uniq) for uniq in set(s) if s.count(uniq) == 1]
        if uniq_list:
            return min(uniq_list)
        else:
            return -1


if __name__ == '__main__':
    a = Solution()
    print(a.firstUniqChar("leetcode") == 0)
    print(a.firstUniqChar("aadadaad") == -1)
    print(a.firstUniqChar("") == -1)
    print(a.firstUniqChar("za") == 0)
    print(a.firstUniqChar("aa") == -1)
    print(a.firstUniqChar("loveleetcode") == 2)
    print(a.firstUniqChar("z") == 0)

"""
My other solutions:

version 1:
    def firstUniqChar(self, s: str) -> int:
        if s == "" or len(set(s)) == 1 and len(s) > 1:
            return -1
        elif len(s) == 1 or len(set(s)) == len(s):
            return 0
        else:
            uniq_list = [s.index(uniq) for uniq in set(s) if s.count(uniq) == 1]
            if uniq_list:
                return min(uniq_list)
            else:
                return -1
version 2:
    def firstUniqChar(self, s: str) -> int:
        uniq_list = [s.index(uniq) for uniq in set(s) if s.count(uniq) == 1]
        if uniq_list:
            return min(uniq_list)
        else:
            return -1

Other solutions:
   def firstUniqChar(self, s):
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
"""
