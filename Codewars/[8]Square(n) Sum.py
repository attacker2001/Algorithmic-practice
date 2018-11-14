# coding=utf-8

"""
Complete the squareSum method so that it squares each number passed into it and then sums the results together.

For example:

square_sum([1, 2, 2]) # should return 9
"""


def square_sum(numbers):
    sum_num = 0
    for i in numbers:
        sum_num += i*i
    return sum_num


if __name__ == '__main__':
    print square_sum([1, 3, 5])
    print square_sum([1, 2])


"""
Other solution:

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


def square_sum(numbers):
    return sum(map(lambda x: x**2,numbers))

"""