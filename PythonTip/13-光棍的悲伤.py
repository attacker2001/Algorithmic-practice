# coding=utf-8

"""
光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。
鄙人光棍几十载，光棍自有光棍的快乐。让我们勇敢面对光棍的身份吧，
现在就证明自己：给你一个整数a，数出a在二进制表示下1的个数，并输出
"""
a = 15

# #################_Submitted code as follows_###########################
count = 0
for i in str(bin(a)):
    if i == '1':
        count += 1
print count

# #################_Submitted code as follows_###########################
# 方法2:
num = [i for i in str(bin(a)) if i == '1']
print len(num)

# #################_Submitted code as follows_###########################
# 方法3:
print str(bin(a)).count('1')
