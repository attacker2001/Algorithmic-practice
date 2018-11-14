# coding=UTF-8
'''
Description:

A number is self-descriptive when the n'th digit describes the amount n appears in the number.

E.g. 21200:

There are two 0's in the number, so the first digit is 2.

There is one 1 in the number, so the second digit is 1.

There are two 2's in the number, so the third digit is 2.

There are no 3's in the number, so the fourth digit is 0.

There are no 4's in the number, so the fifth digit is 0

Numbers can be of any length up to 9 digits and are only full integers. For a given number derive a function selfDescriptive(num) that returns; true if the number is self-descriptive or false if the number is not.

Test.assert_equals(self_descriptive(21200), True)
Test.assert_equals(self_descriptive(3211000), True)
Test.assert_equals(self_descriptive(42101000), True)
Test.assert_equals(self_descriptive(21230), False)
Test.assert_equals(self_descriptive(11200), False)
Test.assert_equals(self_descriptive(1210), True)
Test.assert_equals(self_descriptive(51120111), False)
Test.assert_equals(self_descriptive(2020), True)
Test.assert_equals(self_descriptive(11201), False)
Test.assert_equals(self_descriptive(6210001000), True)
'''


def self_descriptive(num):
    length = len(str(num))
    for i in range(10):          # 遍历数字
        count = 0
        for j in str(num):
            if int(j) == i:
                count += 1
        if count != int(str(num)[i]):
            return False
        length -= 1
        if not length:
            break

    return True

def main():
    num = 51120111
    print self_descriptive(num)

if __name__ == '__main__':
    main()


'''
Other Solutions:


'''