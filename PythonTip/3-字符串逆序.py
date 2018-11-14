# coding=utf-8

"""
给你一个字符串 a， 如a=‘12345’，对a进行逆序输出a。
"""

a = '12345'

# #################_Submitted code as follows_###########################

# print a[::-1]


# #################_Submitted code as follows_###########################
# 方法 2:
# 字符串没有reverse() 内置方法, 所以先转换成list类型, 倒序后, 再转换成字符串
# a = list(a)
# a.reverse()
# print ''.join(a)

print reversed(a)