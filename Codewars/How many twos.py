# coding=UTF8
'''
Description:

Write a function that returns the number of '2's in the factorization of a number.
For example,

two_count(24)

should return 3, since the factorization of 24 is 2^3 x 3

two_count(17280)

should return 7, since the factorization of 17280 is 2^7 x 5 x 3^3
The number passed to two_count (twoCount) will always be a positive integer greater than or equal to 1.

'''

def two_count(n):
    cnt = 0
    while(n % 2 == 0):
        cnt += 1
        n /= 2
    return cnt

def main():
    x = 28
    print two_count(x)

if __name__ == "__main__":
    main()


'''
Other Solutions:

def two_count(n):
    return bin(n)[::-1].index('1')

'''