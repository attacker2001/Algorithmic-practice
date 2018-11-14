# coding=UTF-8

'''
Description:

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect


'''
import math

def find_next_square(sq):
    temp = math.sqrt(sq)
    if math.floor(temp) == temp:
        return int((temp+1)**2)
    else:
        return -1

def main():
    x = 121
    print find_next_square(x)

if __name__ == '__main__':
    main()

'''
Other Solutions:


def find_next_square(sq):
    root = sq ** 0.5        # 开方
    if root.is_integer():
        return (root + 1)**2
    return -1


from math import sqrt
def find_next_square(sq):
    return (sqrt(sq)+1)**2 if sqrt(sq)%1 == 0 else -1

'''

'''
####  Method !!!
# judge a number is integer:

# x.is_integer()
#
# sqrt(x)%1 == 0

'''