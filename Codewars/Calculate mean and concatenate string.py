# coding=utf-8
"""
You will be given a list of strings which will include both integers and characters.

Return a list of length 2 with lst[0] representing the mean of the integers to a single decimal place.
There will always be 10 integers and 10 characters.
Create a single string with the characters and return it as lst[1] while maintaining the original order.

lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
Here is an example of your return
[3.6, 'udiwstagwo']
"""


def mean(lst):
    # average = 0
    # temp = lst[:]
    # for i in temp:
    #     if '0' <= i <= '9':
    #         average += int(i)
    #         lst.remove(i)
    # return [average/10.0, ''.join(lst)]
    return [sum(int(n) for n in lst if n.isdigit()) / 10.0, ''.join(c for c in lst if c.isalpha())]

if __name__ == '__main__':
    lst1 = ['1', '1', 'h', 'r', '6', '5', '7', '1', 'a', 'w', '0', 'c', 'd', '2', 'z', 'y', 'd', '0', '4', 'y']
    print mean(lst1)

"""
    题目要求:
    数字求平均数, 把字母放一起
    the mean of the integers 平均数

太简单,没啥可说的
"""