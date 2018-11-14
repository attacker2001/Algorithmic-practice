# coding=utf-8
"""
Paths in the Grid

You have a grid with m rows and n columns.
Return number of ways that you can start from point A to reach point B.
you are only allowed to move right and up.

alt text

In the picture, there are 10 pathes from A to B.

Hint: Use mathematical permutation and combination

"""
import math


def number_of_routes(m, n):
    """
    total = (m+n)! / (m!*n!)
    """
    return math.factorial(m+n)/(math.factorial(m)*math.factorial(n))

if __name__ == '__main__':
    print number_of_routes(3, 4)
