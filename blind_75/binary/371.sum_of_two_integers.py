# https://leetcode.com/problems/sum-of-two-integers/description/


# Code
# Testcase
# Test Result
# Test Result
# 371. Sum of Two Integers
# Solved
# Medium
# Topics
# Companies
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while (b & mask) !=0:
            carry = ((a & b) << 1 ) & mask
            a = (a ^ b ) & mask
            b = carry
        
        if (a >> 31) & 1:
            return ~(~a & mask)
        return a & mask