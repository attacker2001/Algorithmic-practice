# coding=UTF-8

'''
An abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself.

The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).

Derive function abundantNumber(num)/abundant_number(num) which returns true/True if num is abundant, false/False if not.

'''
import math
def abundant_number(num):
    sum = 1
    for i in range(2, int(math.ceil(math.sqrt(num))) ):
        if num % i == 0:
            sum += i
            sum += num/i
    if sum > num:
        return True
    else:
        return False

def main():
    x = 37
    print abundant_number(x)

if __name__ == '__main__':
    main()