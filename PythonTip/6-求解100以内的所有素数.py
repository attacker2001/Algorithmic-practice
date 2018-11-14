# coding=utf-8

"""
输出100以内的所有素数，素数之间以一个空格区分
"""

# #################_Submitted code as follows_###########################


def isprime(num):
    for j in xrange(2, int(num ** 0.5 + 1)):
        if num % j == 0:
            return False
    return True

for i in xrange(2, 101):
    if isprime(i):
        print i,
print
