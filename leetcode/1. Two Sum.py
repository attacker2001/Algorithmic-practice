# coding=utf-8
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution:
    def twoSum(self, nums, target: int):
        for i, n in enumerate(nums):
            if target - n in nums and nums.index(target-n) != i:
                return sorted([i, nums.index(target - n)])


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([0, 4, 2, 0], 0))
    print(a.twoSum([2, 7, 11, 15], 9))
    print(a.twoSum([3, 2, 4], 6))
    print(a.twoSum([3, 3], 6))
    print(a.twoSum([2, 2, 4, 2], 6))
