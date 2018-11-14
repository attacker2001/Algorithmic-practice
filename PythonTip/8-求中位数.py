# coding=utf-8

"""
给你一个list L, 如 L=[0,1,2,3,4], 输出L的中位数（若结果为小数，则保留一位小数0）
"""

L = [0, 1, 2, 3, 4, 5, 10, 1, 1, 1]
# #################_Submitted code as follows_###########################
L.sort()
if len(L) % 2 != 0:
    print L[len(L) / 2]
else:
    print '%.1f' % ((L[len(L)/2] + L[len(L)/2-1]) / 2.0)
