# coding=UTF-8
'''
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

test.describe("Example")
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
即找出列表中　出现次数为奇数的元素

'''
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
                return i
    return None

def main():
    numbers = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
    print find_it(numbers)
if __name__ == "__main__":
    main()
    
    
'''
Other Soluntion:
import operator

def find_it(xs):
    return reduce(operator.xor, xs)
    
'''