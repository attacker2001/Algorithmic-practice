#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 728. Self Dividing Numbers.py 
@time: 2019/04/26

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""

"""
Other solutions:

class Solution:
    def toLowerCase(self, str): 
        '''
        Runtime: 36 ms, faster than 76.82% of Python3 online submissions for To Lower Case.
        Memory Usage: 13.1 MB, less than 5.45% of Python3 online submissions for To Lower Case.
        '''
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)


class Solution:
    def toLowerCase(self, str): 
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)
"""


class Solution:

    def _check_self_dividing(self, num):
        """
        Runtime: 56 ms, faster than 78.74% of Python3 online submissions for Self Dividing Numbers.
        Memory Usage: 13 MB, less than 6.29% of Python3 online submissions for Self Dividing Numbers.
        """
        for i in str(num):
            if i == '0' or num % int(i) != 0:
                return False
        else:
            return True

    def selfDividingNumbers(self, left: int, right: int) -> list:
        return list(num for num in range(left, right+1) if self._check_self_dividing(num))


if __name__ == '__main__':
    a = Solution()
    print(a.selfDividingNumbers(1, 22))


"""
Other solutions:

Basic version
    return [x for x in range(left, right+1) if all([int(i) != 0 and x % int(i)==0 for i in str(x)])]


Optimized version:
    return [x for x in range(left, right+1) if all((i and (x % i==0) for i in map(int, str(x))))]


Pretty self-explanatory.

- Yangshun

class Solution(object):
    def selfDividingNumbers(self, left, right):
        is_self_dividing = lambda num: '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
        return filter(is_self_dividing, range(left, right + 1))

As pointed out by @ManuelP, [num % int(digit) == 0 for digit in str(num)] creates an entire list 
which is not necessary. 
By leaving out the [ and ], we can make use of generators which are lazy and allows 
for short-circuit evaluation, i.e. all will terminate as soon as one of the digits fail the check.

The answer below improves the run time from 128 ms to 95 ms:

class Solution(object):
    def selfDividingNumbers(self, left, right):
        is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
        return filter(is_self_dividing, range(left, right + 1))

"""
