# coding=utf-8

"""
给你两个正整数a,b,  输出它们公约数的个数。
"""
a, b = 15, 25
# #################_Submitted code as follows_###########################
count = 0
if a > b:
    a, b = b, a
# 公约数把 1 也考虑进去了
for i in xrange(1, a+1):
    if a % i == 0 and b % i == 0:
        count += 1
print count
