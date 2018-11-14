# coding=utf-8

"""
给你一个正整数列表 L, 如 L=[2,8,3,50], 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
奇数输出1,偶数输出0. 如样例输出应为0
"""

L = [2, 8, 3, 50]
# #################_Submitted code as follows_###########################
"""
    如果能够被10整除,就除以10
    一直判断乘积, 如果不能被2整除, 就是奇数
"""
temp = 1
isodd = 0

for i in L:
    temp *= i
    while temp % 10 == 0:
        temp /= 10
    if temp % 2 != 0:
        isodd = 1
print isodd
