# coding=utf-8

"""
Special Multiples

Some numbers have the property to be divisible by 2 and 3.
Other smaller subset of numbers have the property to be divisible by 2, 3 and 5.
Another subset with less abundant numbers may be divisible by 2, 3, 5 and 7.

These numbers have something in common: their prime factors are contiguous primes.

Create a function count_specMult() that finds the amount of numbers that have the first n primes
as factors below a given value, maxVal

Let's see some cases:

count_specMult(3, 200) -------> 6

/// the first 3 primes are 2, 3 and 5

and the found numbers below 200 are 30 < 60 < 90 < 120 < 150 < 180 < 200 (6 numbers)

Happy coding!!

"""
import math


def get_prime_number(n):
    prime_list = []
    for i in xrange(2, 1000000):
        for j in xrange(2, int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
            n -= 1
        if n == 0:
            return prime_list


def count_specMult(n, maxVal):
    prime = get_prime_number(n)

    base_number = 1
    for i in prime:
        base_number *= i

    # count = 0
    # for i in xrange(1, 100000000000):
    #     temp = base_number * i
    #     if temp <= maxVal:
    #         count += 1
    #     else:
    #         break
    # return count
    return maxVal // base_number


if __name__ == '__main__':
    print count_specMult(3, 200)

"""
Other solutions:
(1)
def count_specMult(n, m):
    return int(m / reduce(lambda x,y: x*y, [2,3,5,7,11,13,17,19,23][:n]))


(2)

from math import ceil, sqrt

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131]

def count_specMult(p_count, n_max):
    f = 1
    for i in range(p_count):
        f *= PRIMES[i]
    return n_max // f

"""