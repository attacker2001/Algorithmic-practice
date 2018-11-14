# coding=utf-8

"""
For every positive integer N, there exists a unique sequence starting with 1 and ending with N and such that every number in the sequence is either the double of the preceeding number or the double plus 1. For example, given N = 13, the sequence is [1, 3, 6, 13].

Write a function that returns this sequence given a number N. Try generating the elements of the resulting list in ascending order, i.e., without resorting to a list reversal or prependig the elements to a list.

"""


# def climb(n):
#     seq = [n]
#     while n != 1:
#         if n % 2 == 0:
#             seq.append(n / 2)
#             n /= 2
#         else:
#             seq.append((n-1) / 2)
#             n -= 1
#             n /= 2
#     return sorted(seq)


def climb(n):
    if n == 1:
        return [1]
    else:
        return climb(n/2) + [n]


if __name__ == "__main__":
    print climb(13)

"""
def climb(n):
    result = []
    while n:
        result.append(n)
        n /= 2
    return result[::-1]

def climb(n):
    return [1] if n == 1 else climb(int(n/2)) + [n]
"""