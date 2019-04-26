#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [6]simple-fun-number-319-number-and-ip-address.py 
@time: 2018/12/13
@project: Algorithm-Exercise 
@software: PyCharm


https://www.codewars.com/kata/simple-fun-number-319-number-and-ip-address/train/python

Task
An IP address contains four numbers(0-255) and separated by dots. It can be converted to a number by this way:

Given a string s represents a number or an IP address. Your task is to convert it to another representation(number to IP address or IP address to number).

You can assume that all inputs are valid.

Example
Example IP address: 10.0.3.193

Convert each number to a 8-bit binary string (may needs to pad leading zeros to the left side):

10  -->  00001010
0   -->  00000000
3   -->  00000011
193 -->  11000001
Combine these four strings: 00001010 00000000 00000011 11000001 and then convert them to a decimal number: 167773121

Input/Output
[input] string s

A number or IP address in string format.

[output] a string

A converted number or IP address in string format.

Example
For s = "10.0.3.193", the output should be "167773121".

For s = "167969729", the output should be "10.3.3.193".

"""


def numberAndIPaddress(s):
    if '.' in s:
        return str(int("".join(["{:0>08b}".format(int(i)) if 0 <= int(i) <= 256 else False for i in s.split('.')]), 2))

    else:
        ip_str = bin(int(s)).replace('0b', '')
        ip_str = (32 - len(ip_str)) * '0' + ip_str
        return ".".join([str(int(ip_str[i:i + 8], 2)) for i in range(0, len(ip_str), 8)])


if __name__ == '__main__':
    print numberAndIPaddress("10.0.3.193"), "167773121"
    print numberAndIPaddress("167969729"), "10.3.3.193"

"""
Other solutions:
(1)
from ipaddress import IPv4Address

def numberAndIPaddress(s):
    return str(int(IPv4Address(s))) if '.' in s else str(IPv4Address(int(s)))

(2)
import socket
import struct

def numberAndIPaddress(s):
    if '.' in s:
        return str(struct.unpack('>I', socket.inet_aton(s))[0])
    else:
        return socket.inet_ntoa(struct.pack('>I', int(s)))

"""
