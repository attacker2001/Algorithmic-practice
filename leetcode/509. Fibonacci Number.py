#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 509. Fibonacci Number.py 
@time: 2019/04/27



The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).



Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Note:

0 ≤ N ≤ 30.
"""


class Solution:

    def fib(self, n: int) -> int:
        fib_list = [0, 1]
        if n == 0 or n == 1:
            return fib_list[n]
        else:
            for _ in range(n - 1):
                temp = fib_list[-1] + fib_list[-2]
                fib_list.append(temp)
                # print(fib_list)
            return fib_list[-1]


if __name__ == "__main__":
    a = Solution()

    for i in range(2000):
        print("Round %d:%d\n" % (i, a.fib(i)))

"""
Other solutions:
# Python: no extra memory solution
class Solution:
    def fib(self, N: int) -> int:
        if not N:
            return 0
        first, second = 0, 1
        for i in range(N - 1):
            first, second = second, first + second
        return second
        

# Recursive solution
class Solution(object):
    def fib(self, N):
        if N == 0:
            return 0
        elif N == 1:
            return 1
        return self.fib(N-1) + self.fib(N-2)
"""