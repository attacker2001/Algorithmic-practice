#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 14. Longest Common Prefix.py 
@time: 2020/02/17

URL:
https://leetcode.com/problems/longest-common-prefix/

Description:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if strs:
            shortest_str = min(strs, key=len)
            for prefix in range(len(shortest_str), 0, -1):
                for s in strs:
                    if not s.startswith(shortest_str[:prefix]):
                        break
                else:
                    return shortest_str[:prefix]

        return ""


if __name__ == '__main__':
    a = Solution()
    print(a.longestCommonPrefix(["flower","flow","flight"]) == 'fl')
    print(a.longestCommonPrefix(["dog","racecar","car"]) == '')

"""
My solutions:


Other solutions:
def longestCommonPrefix(self, strs):
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest 



strs = ["flower","flow","flight"]
l = list(zip(*strs))
>>> l = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]

def longestCommonPrefix(self, strs: List[str]) -> str:
    l = list(zip(*strs))
    prefix = ""
    for i in l:
        if len(set(i))==1:
            prefix += i[0]
        else:
            break
    return prefix

"""
