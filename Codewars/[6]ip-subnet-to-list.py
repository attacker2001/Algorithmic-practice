#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [6]ip-subnet-to-list.py 
@time: 2018/12/07
@project: Algorithm-Exercise 
@software: PyCharm



https://www.codewars.com/kata/ip-subnet-to-list/train/python

Generate list all possible ip addresses from a network.

Examples:

 Input = 192.168.1.0/31
 Output = ['192.168.1.0, 192.168.1.1']

 For a subnet that is not appear to be an IPv4 or IPv6 network generate exception:
 Input = 213.256.46.160/28
 Output = "not appear to be an IPv4 or IPv6 network"

"""

import ipaddress


def ipsubnet2list(subnet):
    ip_split_list = ['{:0>08b}'.format(int(i)) if 0 <= int(i) < 256 else False for i in subnet.split('/')[0].split('.')]
    if False in ip_split_list:
        return "not appear to be an IPv4 or IPv6 network"

    return ", ".join([str(i) for i in list(ipaddress.ip_network(subnet).hosts())])


# def ipsubnet2list(subhnet):
# #     result = ''
# #     ip_string, mask_string = subhnet.split('/')[0], subhnet.split('/')[1]
# #
# #     # pre-check
# #     ip_split_list = ['{:0>08b}'.format(int(i)) if 0 <= int(i) < 256 else False for i in ip_string.split('.')]
# #     if False in ip_split_list:
# #         return "not appear to be an IPv4 or IPv6 network"
# #
# #     ip_binary_string = int(''.join(ip_split_list), 2)
# #
# #     for i in range(2 ** (32 - int(mask_string))):
# #         ip = str(bin(ip_binary_string + int(i))).replace('0b', '')
# #         print ip, ".".join([str(int(ip[j:j + 8], 2)) for j in range(0, len(ip), 8)])
# #
# #
# #         result += ".".join([str(int(ip[j:j + 8], 2)) for j in range(0, len(ip), 8)])
# #
# #         # print ".".join([str(int(ip[j:j + 8], 2)) for j in range(0, len(ip), 8)])
# #
# #         result += ', '
# #
# #     return result[:-2]

if __name__ == '__main__':
    print (ipsubnet2list('192.168.1.0/31') == '192.168.1.0, 192.168.1.1')
    print (ipsubnet2list('195.20.15.0/28') ==
           '195.20.15.1, 195.20.15.2, 195.20.15.3, 195.20.15.4, 195.20.15.5, 195.20.15.6, 195.20.15.7, 195.20.15.8, 195.20.15.9, 195.20.15.10, 195.20.15.11, 195.20.15.12, 195.20.15.13, 195.20.15.14')
    print (ipsubnet2list('174.0.153.152/29') ==
           '174.0.153.153, 174.0.153.154, 174.0.153.155, 174.0.153.156, 174.0.153.157, 174.0.153.158')
    print (ipsubnet2list('213.192.46.160/28') ==
           '213.192.46.161, 213.192.46.162, 213.192.46.163, 213.192.46.164, 213.192.46.165, 213.192.46.166, 213.192.46.167, 213.192.46.168, 213.192.46.169, 213.192.46.170, 213.192.46.171, 213.192.46.172, 213.192.46.173, 213.192.46.174')
    print (ipsubnet2list('213.256.46.160/28') == "not appear to be an IPv4 or IPv6 network")
