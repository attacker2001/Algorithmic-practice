#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 842. Split Array into Fibonacci Sequence.py 
@time: 2019/04/29


Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes,
 except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.
"""


class Solution(object):
    def splitIntoFibonacci(self, S):
        for i in range(min(10, len(S))):
            x = S[:i + 1]
            if x != '0' and x.startswith('0'): break  # 排除0开头但不是0的数据，如01，023
            a = int(x)
            for j in range(i + 1, min(i + 10, len(S))):
                y = S[i + 1: j + 1]
                if y != '0' and y.startswith('0'): break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2 ** 31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        return []


if __name__ == '__main__':
    a = Solution()
    print(a.splitIntoFibonacci("123456579"))
    print(a.splitIntoFibonacci("11235813"))
    print(a.splitIntoFibonacci("112358130"))
    print(a.splitIntoFibonacci("0123"))
    print(a.splitIntoFibonacci("1101111"))

"""
Intuition:
The first two elements of the array uniquely determine the rest of the sequence.

For each of the first two elements, assuming they have no leading zero, let's iterate through the rest of the string.
At each stage, we expect a number less than or equal to 2^31 - 1 that starts with the sum of the two previous numbers.

Other solutions:

class Solution(object):
    def splitIntoFibonacci(self, S):
        n = len(S)
        for i in xrange(1, 11):
            for j in xrange(1, 11):
                if i + j >= n:
                    break
                L = self.buildFibo(S, i, j)
                if L:
                    return L
        return []
    
    def buildFibo(self, s, i, j):
        a = s[:i]
        b = s[i:i+j]
        if a[0] == '0' and i > 1:
            return []
        if b[0] == '0' and j > 1:
            return []
        
        offset = i + j
        n = len(s)
        x, y = int(a), int(b)
        arr = [x, y]
        while offset < n:
            z = x + y
            if z > 2147483647:
                return []
            
            c = str(z)
            k = len(c)
            if offset + k > n or s[offset:offset+k] != c:
                return []
            offset += k
            arr.append(z)
            x, y = y, z
        return arr
        

class Solution:
    def splitIntoFibonacci(self, S):
        limit=2**31 - 1
        for i in range(1,len(S)):
            if S[0]=="0" and i!=1:
                break
            for j in range(i+1,len(S)):
                if S[i]=="0" and j!=i+1:
                    break
                pre=int(S[:i])
                cur=int(S[i:j])
                ans=[pre,cur]
                k=j
                while k<len(S):
                    cur,pre=pre+cur,cur
                    if cur<=limit and str(cur)==S[k:k+len(str(cur))]:
                        ans.append(cur)
                        k=k+len(str(cur))
                    else:
                        break
                if k==len(S):
                    return ans
        return []
"""
