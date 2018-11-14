
# coding=UTF-8
'''

In this kata you will be given a positive integer, val and you have to create the function next_pal()(nextPal Javascript) that will output the smallest palindrome number higher than val.

For Python
next_pal(11) == 22

next_pal(188) == 191

next_pal(191) == 202

next_pal(2541) == 2552
'''

def palindrome(x):
    return str(x)[::-1] == str(x)

def next_pal(val):
    val += 1
    while not palindrome(val):
        val += 1
    return val

def main():
    print next_pal(11)

if __name__ == '__main__':
    main()

'''
How to judge a number is palindrome:
def palindrome(x):
    return str(x)[::-1] == str(x)

'''