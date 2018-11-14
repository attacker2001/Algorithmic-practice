# coding=utf-8

"""
Unicode Total

You'll be given a string, and have to return the total of all the unicode characters as an int.
Should be able to handle any characters sent at it.

examples:

uniTotal("a") == 97 uniTotal("aaa") == 291

"""


def uni_total(string):
    return sum([ord(i) for i in string])


if __name__ == '__main__':
    print uni_total('aaa')


"""
Other solution:
def uni_total(string):
    return sum(map(ord, string))

The key is using this function: map()

"""