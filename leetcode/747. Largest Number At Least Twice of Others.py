#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 747. Largest Number At Least Twice of Others.py 
@time: 2019/05/11

Description:
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.


Example 1:
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


Note:
nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""


class Solution:
    def dominantIndex(self, nums: list) -> int:
        new_nums = sorted(list(set(nums)))

        if len(new_nums) == 1:
            return 0
        else:
            if new_nums[-1] >= new_nums[-2]*2:
                return nums.index(new_nums[-1])
            else:
                return -1


if __name__ == '__main__':
    a = Solution()
    print(a.dominantIndex([1, 1, 1, 1, 1]))
    print(a.dominantIndex([1]))
    print(a.dominantIndex([3, 6, 1, 0]))
    print(a.dominantIndex([1, 2, 3, 4]))

"""
My solutions:
First:
class Solution:
    def dominantIndex(self, nums: list) -> int:

        if len(set(nums)) == 1:
            return 0

        bigest_num, bigest_num_index = max(nums), nums.index(max(nums))
        new_nums = [x * 2 for x in list(set(nums)) if x != bigest_num]

        if len(new_nums) and max(new_nums) > bigest_num:
            return -1
        else:
            return bigest_num_index

Second:
class Solution:
    def dominantIndex(self, nums: list) -> int:
        new_nums = sorted(list(set(nums)))

        if len(new_nums) == 1:
            return 0
        else:
            if new_nums[-1] >= new_nums[-2]*2:
                return nums.index(new_nums[-1])
            else:
                return -1

Other solutions:
https://leetcode.com/problems/largest-number-at-least-twice-of-others/discuss/110120/Python-O(n)-time-and-O(1)-space-without-fancy-builtins

class Solution:
    def dominantIndex(self, nums):
        if len(nums) == 0: return -1

        highest = -1
        secondHighest = -1
        highestIndex = 0
        
        for i,n in enumerate(nums):
            if n >= highest:
                secondHighest = highest
                highest = n
                highestIndex = i
            elif n > secondHighest:
                secondHighest = n

        if highest < secondHighest*2:
            highestIndex = -1
        
        return highestIndex

"""
