# coding=utf-8
"""
 Total Accepted: 88401 Total Submissions: 182750 Difficulty: Easy

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # while num > 9:
        #     num = [int(i) for i in str(num)]
        #     num = sum(num)
        # return num
        return (num - 1) / 9 + 1


if __name__ == "__main__":
    a = Solution()
    print(a.addDigits(38))

"""
Other soluntion:

if num == 0:
    return 0
else:
    return ((num - 1) % 9 + 1)
"""
