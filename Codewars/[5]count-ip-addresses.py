#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [5]count-ip-addresses.py 
@time: 2018/11/27
@project: Algorithm-Exercise 
@software: PyCharm
"""

"""
https://www.codewars.com/kata/count-ip-addresses/train/python

Write a function that accepts a starting and ending IPv4 address, and the number of IP addresses from start to end, excluding the end IP address.

All input to the function will be valid IPv4 addresses in the form of strings. The ending address will be at least one address higher than the starting address.

Examples
ipsBetween("10.0.0.0", "10.0.0.50")  =>   50 
ipsBetween("10.0.0.0", "10.0.1.0")   =>  256 
ipsBetween("20.0.0.10", "20.0.1.0")  =>  246

"""


def ip_str_to_binary_str(ip):
    """
    Convert ip address format from "x.x.x.x" to '0b00010100000000000000000000001010'
    :param ip: the standard ip format.
    :return: the binary ip address string with 32 length.
    """
    return "".join(
        [
            '0' * (8 - len(bin(int(i)).replace('0b', ''))) + bin(int(i)).replace('0b', '')
            for i in ip.split('.')
        ]
    )


def ips_between(start, end):
    start_ip_number = ip_str_to_binary_str(start)
    end_ip_number = ip_str_to_binary_str(end)

    return int(end_ip_number, 2) - int(start_ip_number, 2)


if __name__ == '__main__':
    print ips_between("10.0.0.0", "10.0.0.50"), 50
    print ips_between("20.0.0.10", "20.0.1.0"), 246
    print ips_between("216.56.104.29", "218.243.210.37"), 45836808

"""
Other solutions:

(1)
from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))

# 个人认为这个最具备实际工程的意义，但是这里主要看算法，所以并不是最好

(2)
def ips_between(start, end):
    return sum((int(b) - int(a)) * 256 ** i for i, (b, a) in enumerate(reversed(zip(end.split('.'), start.split('.')))))

# 这个解法就是将4段IP，分别求差，再加起来
# 也算是对Python一些遍历技巧的整合了

(3)
def ips_between(start, end):
    return ipToNumber(end) - ipToNumber(start)

def ipToNumber(p1):
    rets = ''
    for t in p1.split('.'):
        rets += '{0:08b}'.format(int(t))
    return int(rets,2)
    
# 这个解法就和我一模一样了，但是巧妙利用format的“填充与对齐”功能。学习了。

# Python format填充与对齐 examples:

In [15]: '{:>8}'.format('189')
Out[15]: '     189'
In [16]: '{:0>8}'.format('189')
Out[16]: '00000189'
In [17]: '{:a>8}'.format('189')
Out[17]: 'aaaaa189'



In [54]: '{:b}'.format(17)
Out[54]: '10001'
In [55]: '{:d}'.format(17)
Out[55]: '17'
In [56]: '{:o}'.format(17)
Out[56]: '21'
In [57]: '{:x}'.format(17)
Out[57]: '11'

"""
