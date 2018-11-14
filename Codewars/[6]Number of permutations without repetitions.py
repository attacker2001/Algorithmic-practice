# coding=utf-8

"""
Write a function that takes a number or a string and gives back the number of permutations
without repetitions that can generated using all its element.; more on permutations here.

For example, starting with:

1
45
115
"abc"

You could respectively generate:

1
45,54
115,151,511
"abc","acb","bac","bca","cab","cba"

So you should have, in turn:


Test.describe("Basic tests")
Test.assert_equals(perms(2), 1)
Test.assert_equals(perms(25), 2)
Test.assert_equals(perms(342), 6)
Test.assert_equals(perms(1397), 24)
Test.assert_equals(perms(76853), 120)
Test.assert_equals(perms("a"), 1)
Test.assert_equals(perms("ab"), 2)
Test.assert_equals(perms("abc"), 6)
Test.assert_equals(perms(737), 3)
Test.assert_equals(perms(66666), 1)
"""
from collections import Counter
import math


def perms(element):
    stringElement = str(element)
    tally = Counter(stringElement)

    topPart = math.factorial(len(stringElement))

    product = 1
    for t in tally:
        product *= math.factorial(tally[t])

    print tally
    return topPart / product

if __name__ == '__main__':
    print perms(6622)
