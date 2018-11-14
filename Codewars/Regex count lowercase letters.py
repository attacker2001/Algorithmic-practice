# coding=UTF-8

# def lowercase_count(strng):
#     count = 0
#     for cha in strng:
#         # if cha >= 'a' and cha <= 'z':
#         if cha.islower():
#             count += 1
#     return count
def lowercase_count(strng):
    return sum(cha.islower() for cha in strng)


def main():
    str = "abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"
    print lowercase_count(str)

if __name__ == '__main__':
    main()

'''
Other solutions:
def lowercase_count(strng):
    return sum(a.islower() for a in strng)

'''

'''
####  Method !!!
# judge a character is lower or not :
#
# cha.islower()
#
# cha >= 'a' and cha <= 'z'

'''