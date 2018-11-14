# coding=UTF-8

"""
Write a function that takes n and returns it's sXORe.
Examples
n 	        sXORe n
0 	        0
1 	        1
50 	        51
1000000 	1000000
"""


def sxore(n):
    result = False
    for i in xrange(n+1):
        result = result ^ i
    return result
"""
The result:
    OverflowError: Python int too large to convert to C long
"""

if __name__ == '__main__':
    n = 4
    print sxore(n)

"""
Others:
连续异或运算的公式

def sxore(n):
    return [n, 1, n + 1, 0][n % 4]
"""
