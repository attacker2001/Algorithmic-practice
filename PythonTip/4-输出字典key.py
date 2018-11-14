# coding=utf-8

"""
给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','链接，如‘1,2,3'。
"""

a = {1: 1, 2: 2, 3: 3}

# #################_Submitted code as follows_###########################
# keys = ''
# for i in a:
#     keys += str(i) + ','
# print keys[:-1]

# #################_Submitted code as follows_###########################
print ','.join([str(x) for x in a.keys()])
