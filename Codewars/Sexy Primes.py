# coding=UTF-8

'''
Sexy primes are pairs of two primes that are 6 apart. In this kata, your job is to complete the function sexy_prime(x, y) which returns true if x & y are sexy, false otherwise.
Examples:

sexy_prime(5,11)
--> True

sexy_prime(61,67)
--> True

sexy_prime(7,13)
--> True

sexy_prime(5,7)
--> False

'''
def isprime(x):
    return x > 1 and all(x % i != 0 for i in xrange(2, int(x**0.5) + 1))

def sexy_prime(x, y):
    return isprime(x) and isprime(y) and abs(x-y)==6

def main():
    x, y = 13, 19
    print sexy_prime(x, y)

if __name__ == '__main__':
    main()