#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [5]int32-to-ipv4.py 
@time: 2018/11/21
@project: Algorithm-Exercise 
@software: PyCharm
"""

"""
https://www.codewars.com/kata/int32-to-ipv4/train/python

Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

Examples
2149583361 ==> "128.32.10.1"
32         ==> "0.0.0.32"
0          ==> "0.0.0.0"

"""


def int32_to_ip(int32):
    """
    standard format: 10000000.00100000.00001010.00000001
                     2**31 + 2**30 + 2**29 + ...... + 2**0
    """
    ip = ''

    for i in range(32)[::-1]:
        if int32 >= 2 ** i:
            ip += '1'
            int32 -= 2 ** i
        else:
            ip += '0'

    ip = ".".join([str(int(ip[i:i + 8], 2)) for i in range(0, len(ip), 8)])

    return ip


if __name__ == '__main__':
    print int32_to_ip(2154959208), "128.114.17.104"
    print int32_to_ip(0), "0.0.0.0"
    print int32_to_ip(2149583361), "128.32.10.1"


"""
Other solutions:

(1)
def int32_to_ip(int32):
    return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))


(2)
from ipaddress import IPv4Address

def int32_to_ip(int32):
    return str(IPv4Address(int32))

(3)
from re import sub
def int32_to_ip(int32):
  return sub(r'(\d{8})', lambda x: str(int(x.group(), 2))+'.' , '{0:32b}'.format(int32).replace(' ', '0'))[:-1]



Key points:
Python binary to decimal:
    print(int("100111",2))
"""