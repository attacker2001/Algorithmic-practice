# coding=utf-8

"""
给你两个正整数a和b， 输出它们的最小公倍数
"""

a, b = 25, 125
# #################_Submitted code as follows_###########################
x, y = a, b
if a <= b:
    a, b = b, a
while b != 0:
    a, b = b, a % b
print x * y / a
