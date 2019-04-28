#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 70. Climbing Stairs.py 
@time: 2019/04/28


You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs_by_steps(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climbStairs_by_steps(i + 1, n, memo) + self.climbStairs_by_steps(i + 2, n, memo)
        return memo[i]

    def climbStairs(self, n: int) -> int:
        m = [0] * (n + 1)
        return self.climbStairs_by_steps(0, n, m.copy())


if __name__ == '__main__':
    a = Solution()
    print(a.climbStairs(35))

"""
Explanations:
Same simple algorithm written in every offered language. 
Variable a tells you the number of ways to reach the current step, 
and b tells you the number of ways to reach the next step. 

So for the situation one step further up, the old b becomes the new a, and the new b is the old a+b, 
since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.

说白了就是斐波那契数列，只不过是换了一种说法。

Other solutions:
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
    

Dynamic Programming:
https://leetcode.com/articles/climbing-stairs/
https://leetcode.com/problems/climbing-stairs/discuss/163347/Python-3000DP-or-tm


# Solution 1: Recursion (TLE)
class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Solution 2: Top-Down (using array)
class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        res = [-1 for i in range(n)]
        res[0], res[1] = 1, 2
        return self.dp(n-1, res)
        
    def dp(self, n, res):
        if res[n] == -1:
            res[n] = self.dp(n - 1, res) + self.dp(n - 2, res)
        return res[n]


# Solution 3: Bottom-Up (using array)
class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]


# Solution 3: Bottom-Up (Constant Space)
class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b

"""
