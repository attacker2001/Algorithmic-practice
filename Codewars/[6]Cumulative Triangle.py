# coding=utf-8

"""
Description:

    Starting with the number "1", "1" is positioned at the top of the triangle.
    As this is the 1st row, it can only support a single number.
    The 2nd row can support the next 2 numbers: "2" and "3"
    Likewise, the 3rd row, can only support the next 3 numbers: "4", "5", "6"
    And so on; this pattern continues.

    1
   2 3
  4 5 6
 7 8 9 10
...

Given N, return the sum of all numbers on the Nth Row:

1 <= N <= 10,000

test.describe("Example Tests")

test.it('Row 1')
test.assert_equals(cumulative_triangle(1), 1)

test.it('Row 3')
test.assert_equals(cumulative_triangle(3), 15)

test.it('Row 4')
test.assert_equals(cumulative_triangle(4), 34)

"""


def cumulative_triangle(n):
    start = 1
    count = 1
    for i in xrange(2, 1000000):
        if count == n:
            break
        start += i
        count += 1

    amount = 0
    for i in xrange(n):
        amount += start
        start -= 1

    return amount


if __name__ == '__main__':
    print cumulative_triangle(4)


"""
Other Solution:

def cumulative_triangle(n):
    return n*(n*n+1)/2

分析:
题目的实际意思是求:
    指定第n行所有数字的和
那么每行都是等差数列:
    使用求和公式: (首项+尾项)*项数/2

每一行的"首项+尾项" 刚好是 n*n+1
       "项数"     刚好是 n
"""