#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 1108. Defanging an IP Address.py 
@time: 2020/02/17
"""

"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == "__main__":
    a = Solution()
    print(a.defangIPaddr('1.1.1.1'))
    print(a.defangIPaddr('1.1.250.1'))
