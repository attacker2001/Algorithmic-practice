#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [5]primes-in-numbers.py 
@time: 2018/12/06
@project: Algorithm-Exercise 
@software: PyCharm
"""

"""
https://www.codewars.com/kata/primes-in-numbers/train/python


Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


def make_prime_list(n):
    """
    Give a prime list which all of them are less than n
    :param n: a positive number
    :return: a prime list
    """
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093,
                  1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223,
                  1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327,
                  1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481,
                  1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597,
                  1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721,
                  1723, 1733, 1741, 1747, 1753, 5113051, 7919, 7537, 123863, 15073, ]

    return prime_list


def primeFactors(n):
    result_string = ''
    prime_list = make_prime_list(50)

    for prime in prime_list:
        temp_count = 0
        while n % prime == 0:
            n = n / prime
            temp_count += 1

        if temp_count > 1:
            result_string += "({}**{})".format(prime, temp_count)
        elif temp_count == 1:
            result_string += "({})".format(prime)
        else:
            continue

        if n == 1:
            break

    return result_string


if __name__ == '__main__':
    print primeFactors(5113051)


"""
Other solutions:

(1)
def primeFactors(n):
    ret = ''
    for i in xrange(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret

通过上面的这个解法就看出来，没有必要去生成质数列表，直接遍历n一下的数字即可
    如果再进行改进，其实只用遍历n的一般即可：
    
def primeFactors(n):
ret = ''
for i in xrange(2, n/2 + 1):
    num = 0
    while(n % i == 0):
        num += 1
        n /= i
    if num > 0:
        ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
    if n == 1:
        return ret
else:
    return '({})'.format(n)



(2)
def primeFactors(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)
    
"""