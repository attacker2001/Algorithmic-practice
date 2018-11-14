# coding=UTF-8

"""
Write a simple regex to validate a username.

Allowed characters are:

-lowercase letters -numbers -underscore

length should be between 4 and 16 characters.
"""


import re
def validate_usr(username):
    #your code here
    return re.search(username, "\w*")

def main():
    str = "asddsa"
    validate_usr(str)

if __name__ == '__main__':
    main()