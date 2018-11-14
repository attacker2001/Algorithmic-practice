# coding=utf-8

"""
给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)
"""

L = [2, 8, 3, 50]
# #################_Submitted code as follows_###########################
temp, count = 1, 0
for i in xrange(0, len(L)):
    temp *= L[i]
    while temp % 10 == 0:       # 注意此处应是 while 而不是 if, 防止一次乘法出现两个以上的0
        temp /= 10
        count += 1
print count
