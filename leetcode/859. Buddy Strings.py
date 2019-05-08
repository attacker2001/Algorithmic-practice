#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 859. Buddy Strings.py 
@time: 2019/05/07

Description:
Given two strings A and B of lowercase letters, return true
if and only if we can swap two letters in A so that the result equals B.


Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""


class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(A):
            return True

        dif = [(a, b) for a, b in zip(A, B) if a != b]

        return len(dif) == 2 and dif[0] == dif[1][::-1]


if __name__ == '__main__':
    a = Solution()
    print(a.buddyStrings("abcd", "abcd"))
    print(a.buddyStrings("abcd", "abcd"))
    print(a.buddyStrings("aaa", "aaa"))
    print(a.buddyStrings("aaa", "aa"))
    print(a.buddyStrings("aaaaaaabc", "aaaaaaacb"))

"""
My other solutions:


Other solutions:
https://leetcode.com/problems/buddy-strings/discuss/141780/Easy-Understood

If A.length() != B.length(): no possible swap
If A == B, we need swap two same characters. Check is duplicated char in A.
In other cases, we find index for A[i] != B[i]. There should be only 2 diffs and it's our one swap.

def buddyStrings(self, A, B):
    if len(A) != len(B): return False
    if A == B and len(set(A)) < len(A): return True  # Check is duplicated char in A, here is a little difficult to get.
    dif = [(a, b) for a, b in zip(A, B) if a != b]
    return len(dif) == 2 and dif[0] == dif[1][::-1]

"""
