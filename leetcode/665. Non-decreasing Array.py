#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 665. Non-decreasing Array.py 
@time: 2019/05/09

Description:
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000].
"""


class Solution(object):
    def checkPossibility(self, nums: list) -> bool:
        if len(nums) < 3:
            return True
        else:
            count = 0
            i = 1
            while i < len(nums) - 1:
                if count == 2:
                    return False
                if nums[i - 1] <= nums[i] <= nums[i + 1]:
                    pass
                elif nums[i - 1] <= nums[i] and nums[i] > nums[i + 1]:
                    if nums[i - 1] <= nums[i + 1]:
                        nums[i] = nums[i - 1]
                    else:
                        nums[i + 1] = nums[i]
                    count += 1
                elif nums[i - 1] > nums[i] > nums[i + 1]:
                    return False
                elif nums[i - 1] > nums[i] and nums[i] <= nums[i + 1]:
                    count += 1

                i += 1
            if count == 2:
                return False
            else:
                return True


if __name__ == '__main__':
    a = Solution()
    print(a.checkPossibility([-1, 4, 2, 3]))
    print(a.checkPossibility([3, 4, 2, 3]))
    print(a.checkPossibility([1, 2, 3, 2]))
    print(a.checkPossibility([0]))
    print(a.checkPossibility([1]))
    print(a.checkPossibility([4, 2, 3]))
    print(a.checkPossibility([4, 2, 1]))

"""
My other solutions:


Other solutions:

(1) https://leetcode.com/problems/non-decreasing-array/discuss/106816/Python-Extremely-Easy-to-Understand

First, find a pair where the order is wrong. 
Then there are two possibilities, either the first in the pair can be modified or the second can be modified 
to create a valid sequence. 

We simply modify both of them and check for validity of the modified arrays by comparing with the array after sorting.

I find this approach the easiest to reason about and understand.
class Solution(object):
    def checkPossibility(self, nums):
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)

"""
