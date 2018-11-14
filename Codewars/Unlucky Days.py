# coding=utf-8

"""
Friday 13th or Black Friday is considered as unlucky day.
Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year as an integer.
Output: Number of Black Fridays in the year as an integer.
Precondition: 1000 < |year| < 3000
Examples:

unluckyDays(2015) == 3
unluckyDays(1986) == 1
"""
import datetime


def unlucky_days(year):
    return sum(datetime.date(year, m, 13).weekday() == 4 for m in range(1, 13))


if __name__ == '__main__':
    for i in range(2000, 2016):
        print unlucky_days(i),
    print
    print unlucky_days(1986)


"""
    题目要求:   每个月的第13天是周五 的 总数
解题关键:
    date(year, month, day).weekday()
    date对象的weekday() 方法能够获取当天的星期 !!!


"""