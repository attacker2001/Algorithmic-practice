#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 448. Find All Numbers Disappeared in an Array.py 
@time: 2020/02/16
"""

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        num_list = []

        for i in nums:
            location = abs(i) - 1
            nums[location] = - abs(nums[location]) if nums[location] > 0 else nums[location]

        for i in range(len(nums)):
            if nums[i] > 0:
                num_list.append(i + 1)

        return num_list


if __name__ == "__main__":
    a = Solution()
    print(a.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(a.findDisappearedNumbers([3, 2, 2, 7, 8, 2, 3, 1]))

"""
My solution 1: (Time Limit Exceeded)
def findDisappearedNumbers(self, nums: list) -> list:
    num_list = list(range(1, len(nums) + 1))

    for i in set(nums):
        num_list.remove(i)

    return num_list



My solution 2: (Accepted, Runtime: 348 ms, Memory Usage: 19.9 MB)
def findDisappearedNumbers(self, nums: list) -> list:
    num_list = []
    # 设置一个标记数组，长度和输入数组的长度一样
    emp_list = [0] * len(nums)

    # 遍历输入的数组，如果对应位置的数字出现，标记那个位置为1
    for i in nums:
        emp_list[i - 1] = 1

    # 遍历标记数组，如果对应位置为0，代表该数字未出现，那么加入数组
    for i, j in enumerate(emp_list):
        if j == 0:
            num_list.append(i + 1)

    return num_list


Other Solutions:
def findDisappearedNumbers(self, nums):
    # For each number i in nums, we mark the number that i points as negative.
    # Then we filter the list, get all the indexes who points to a positive number
    for i in xrange(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]

explanation: 
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/344583/Python%3A-O(1)-space-solution

利用上述解法，比我的第二种解法就好在不需要开辟额外的空间了。

"""
