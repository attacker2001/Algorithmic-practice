# coding=utf-8

"""
我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。

今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。
注：所给数据都有解，不用考虑无解的情况。
"""
a, b = 108, 6
# #################_Submitted code as follows_###########################
if a > b:
    big, small = a, b
else:
    big, small = b, a

ran = big / small
he = 99999999

for i in range(1, ran):
    x = small * i
    for j in range(1, ran):
        y = small * j
        if x * y == small * big and x + y < he:
            a, b = x, y
            he = x + y
print a, b
