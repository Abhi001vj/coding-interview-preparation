# https://leetcode.com/problems/climbing-stairs/description/
# 70. Climbing Stairs
# Easy
# Topics
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

class Solution:
    def __init__(self):
        self.memo = {1:1, 2:2}
        
    def climbStairs(self, n: int) -> int:
        # Base case
        if n <= 2:
            return n
            
        # If already computed
        if n in self.memo:
            return self.memo[n]
            
        # Calculate and memoize
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]
    
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        for i in range(n-1):
            c = a + b
            a = b
            b = c

        return b
    
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        for i in range(n-2, -1, -1):
            c = a + b
            a = b
            b = c

        return b