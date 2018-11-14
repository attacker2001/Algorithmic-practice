# coding=utf-8

"""
https://www.codewars.com/kata/55de3f83e92c3e521a00002a
Description:

    Input: Integer n
    Output: String

Example:

a(4) prints as

   A
  A A
 A A A
A     A

a(8) prints as

       A
      A A
     A   A
    A     A
   A A A A A
  A         A
 A           A
A             A

a(12) prints as

           A
          A A
         A   A
        A     A
       A       A
      A         A
     A A A A A A A
    A             A
   A               A
  A                 A
 A                   A
A                     A

Note:

    Each line's length is 2n - 1
    Each line should be concatenate by line break "\n"
    If n is less than 4, it should return ""
    If n is odd, a(n) = a(n - 1), eg a(5) == a(4); a(9) == a(8)
"""


def a(n):
    if n < 4:
        return ""
    if n % 2 == 1:
        n -= 1
    string = ""
    for row in xrange(1, n+1):
        # every row consists of five part
        # part 1: space
        string += ' ' * (n - row)
        # part 2: left letter
        string += 'A'
        # part 3: space
        if row > 1 and row != n/2 + 1:
            string += ' ' * (2*row - 3)
        if row == n/2 + 1:
            for j in range(n-1):
                if j % 2 == 0:
                    string += ' '
                else:
                    string += 'A'
        # part 4: right letter
        if row > 1:
            string += 'A'
        # part 5: right space
        string += ' ' * (n - row)
        # part 6: LF:
        if row != n:
            string += '\n'

    return string


if __name__ == "__main__":
    print a(6)

"""
def a(n):
    if n % 2 != 0:
        n = n - 1
    if n < 4:
        return ''
    side = " " * (n - 1)
    li = [side + "A" + side]
    for i in range(1, n):
        side = side[1:]
        middle = "A " * (i - 1) if i == (n / 2) else "  " * (i - 1)
        li.append(side + "A " + middle + "A" + side)
    return "\n".join(li)
"""