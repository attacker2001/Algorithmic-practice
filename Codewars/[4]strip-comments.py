#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [4]strip-comments.py 
@time: 2018/12/14
@project: Algorithm-Exercise 
@software: PyCharm


https://www.codewars.com/kata/strip-comments/train/python

Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def solution(string, markers):
    lines = string.split('\n')
    for i, line in enumerate(lines):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        lines[i] = line.rstrip(' ')
    return '\n'.join(lines)


if __name__ == '__main__':
    print solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) == "apples, pears\ngrapes\nbananas"
    print solution("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd"
    print solution(
        ". avocados pears . ' apples\nbananas oranges cherries , pears ^\napples watermelons avocados oranges\napples strawberries strawberries\n^ apples",
        ['^', '!', ',',
         '@']) == ". avocados pears . ' apples\nbananas oranges cherries\napples watermelons avocados oranges\napples strawberries strawberries\n"

"""
other solutions:

(1)
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

(2)
from re import split, escape


def solution(string, markers):
    if markers:
        pattern = "[" + escape("".join(markers)) + "]"
    else:
        pattern = ''
    return '\n'.join(split(pattern, line)[0].rstrip() for line in string.splitlines())
    

"""