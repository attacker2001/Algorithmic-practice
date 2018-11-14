# coding=UTF-8

'''
Your job is to build a function which determines whether or not there are double characters in a string (including whitespace characters). For example aa, !! or .

You want the function to return true if the string contains double characters and false if not.

Examples:

  double_check("abca")
  #returns False

  double_check("aabc")
  #returns True

  double_check("a 11 c d")
  #returns True

  double_check("AabBcC")
  #returns True

  double_check("a b  c")
  #returns True

  double_check("a b c d e f g h i h k")
  #returns False

  double_check("2020")
  #returns False

'''
def double_check(strng):
    if strng == "" or strng == " ":
        return True
    for i in range(len(strng)-1):
        if strng[i+1].lower() == strng[i] or \
           strng[i+1] == strng[i].lower():
            return True
    return False

def main():
    str = "AabBcC"
    print double_check(str)

if __name__ == '__main__':
    main()


'''
Other Solutions:

import re

def double_check(str):
    return bool(re.search(r"(.)\1", str.lower()))

'''
