#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 204. Count Primes.py 
@time: 2019/05/05


Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def is_prime(self, num):
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            num_list = list(range(2, n))
            count = 0

            for i in num_list:
                if self.is_prime(i):
                    count += 1

                    for j in range(2, n // i + 1):
                        if j * i in num_list:
                            num_list.remove(j * i)

        return count


if __name__ == '__main__':
    a = Solution()
    print(a.countPrimes(2))
    print(a.countPrimes(3))
    print(a.countPrimes(20))
    print(a.countPrimes(499979))

"""
Other solutions:

def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)

def countPrimes(self, n):
    if n <= 2:
        return 0
    res = [True] * n
    res[0] = res[1] = False
    for i in xrange(2, n):
        if res[i] == True:
            for j in xrange(2, (n-1)//i+1):
                res[i*j] = False
    return sum(res)
    

class Solution(object):
    def countPrimes(self, n):
        # Sieve of Eratosthenes

        # We are only interested in numbers LESS than the input number
        # exit early for numbers LESS than 2; (two is prime)
        if n < 2:
            return 0
        
        # create strike list for the input range, initializing all indices to
        # prime (1).
        strikes = [1] * n

        # we know that 0 and 2 are not prime
        strikes[0] = 0
        strikes[1] = 0
        
        # Now set multiples of remaining numbers that are marked as prime to
        # not prime.  It is safe ignore numbers alreay marked as not prime
        # because there are factor(s) that divide evenly into this number and
        # all its multiples.  Use upper limit of (n**0.5)+1, because:
        #  (a) the smallest factor of a non-prime number will not be > sqrt(n).
        #      Ex. non-prime = 100, 
        #           5*20
        #           10*10, 
        #           20*5   # !! we have seen 5 before.
        for i in range(2, int(n**0.5)+1):
            if  strikes[i] != 0:
                # slow:
                #for j in range(i*i, n, i):
                #    strikes[j] = 0

                # 3x faster:
                # strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
                # n = 11
                # i = 2
                # (n-1-i*i)//i + 1
                # (n-1)               # get total # of indicies for n (non-inclusive)
                #     -i*i            # shift to get # of slots in range of interest
                #          //i        # get number of groups
                #              + 1    # get number of slots
                # strikes[2*2:11:2]  = [0] * ((11-1-2*2)//2 + 1
                # strikes[4:11:2]    = [0] * 4
                # s[4], s[6], s[8], s10] = 0, 0, 0, 0
                strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)

        return sum(strikes)
"""
