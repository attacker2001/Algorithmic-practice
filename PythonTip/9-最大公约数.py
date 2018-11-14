# coding=utf-8

"""
给你两个正整数a和b， 输出它们的最大公约数。
"""

a, b = 25, 125
# #################_Submitted code as follows_###########################
while b != 0:
    a, b = b, a % b
print a
