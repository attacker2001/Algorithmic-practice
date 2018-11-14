# coding=utf-8
"""
The main mode is having a method named main inside a class and should return nothing
but should print a line to the standard output with the message Hello World!.

For Java the main method should receive String array as parameters
that can be specified when running from console with the command

    Solution.main("parameter1", "parameter2","parameter n")

    *Note:* please be sure to define main as static method

"""


class Solution(object):
    @staticmethod
    def main(*args):
        print 'Hello World!'
