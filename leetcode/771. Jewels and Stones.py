#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 771. Jewels and Stones.py 
@time: 2019/05/05
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.

Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in J:
            count += S.count(i)
        return count


if __name__ == '__main__':
    a = Solution()
    print(a.numJewelsInStones("aA", "aAAbbbb"))
    print(a.numJewelsInStones("z", "ZZ"))


"""
Other solutions:
def numJewelsInStones(self, J, S):
    return sum(map(J.count, S))
    
def numJewelsInStones(self, J, S):
    return sum(map(S.count, J))               # this one after seeing https://discuss.leetcode.com/post/244105

def numJewelsInStones(self, J, S):
    return sum(s in J for s in S)
"""