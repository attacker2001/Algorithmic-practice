#!/usr/bin/env python
# coding=utf-8

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.

"""

#
# def solution(number):
#     num_list = []
#     for i in xrange(number):
#         if i % 3 == 0 or i % 5 == 0:
#             num_list.append(i)
#     return sum(num_list)


def solution(number):
    return sum(x for x in xrange(number) if x % 3 == 0 or x % 5 == 0)


if __name__ == '__main__':
    print solution(10)
    print solution(20)

"""
Solution 1:
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
"""