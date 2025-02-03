# https://leetcode.com/problems/next-greater-element-iii/description/
# 556. Next Greater Element III
# Solved
# Medium
# Topics
# Companies
# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

# Example 1:

# Input: n = 12
# Output: 21
# Example 2:

# Input: n = 21
# Output: -1
 

# Constraints:

# 1 <= n <= 231 - 1

"""
Next Greater Element III - Detailed Solution
-----------------------------------------

Problem Understanding:
--------------------
Given a positive integer n, we need to find the smallest integer greater than n
that contains exactly the same digits as n.

Example: n = 12
- Possible numbers with same digits: 12, 21
- Answer: 21 (as it's the next greater number)

Example: n = 21
- Already the largest possible number with these digits
- Answer: -1

Key Insights:
------------
1. This is a "next permutation" problem
2. We need to find the lexicographically next greater permutation
3. If no such permutation exists, return -1
4. Result must fit in 32-bit integer

Visual Algorithm Steps:
---------------------
Example: n = 1234321

1. Find first decreasing digit from right:
   1 2 3 4 3 2 1
         ↑
   Found 4 > 3

2. Find smallest digit > 3 on right side:
   1 2 3 4 3 2 1
         ↑   ↑
   Found 2

3. Swap these digits:
   1 2 3 2 3 4 1

4. Reverse everything after position i:
   1 2 3 2 1 4 3

Time Complexity: O(n) where n is number of digits
Space Complexity: O(n) for storing digits array
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert to list of digits for easier manipulation
        # Time: O(log n) for conversion, Space: O(log n) for digits array
        digits = list(str(n))
        length = len(digits)
        
        """
        Step 1: Find first decreasing digit from right
        Example: In 1234321
        Compare: 1-2, 2-3, 3-4, 4-3 ← Found! (i points to 3)
        Time: O(n) worst case, usually better in practice
        """
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        # If no such digit found, we have largest permutation
        if i == -1:
            return -1
            
        """
        Step 2: Find smallest digit on right that's greater than digits[i]
        Example: In 1234321, after finding i=3:
        Look through 4,3,2,1 to find smallest > 3
        Found 4 at position j
        Time: O(n) worst case
        """
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
            
        """
        Step 3: Swap the digits at i and j
        Example: 1234321 becomes 1234421
        Time: O(1)
        """
        digits[i], digits[j] = digits[j], digits[i]
        
        """
        Step 4: Reverse subarray to right of i
        This gives us smallest possible number with these digits
        Example: 1234421 becomes 1234124
        Time: O(n)
        """
        left = i + 1
        right = length - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1
        
        # Convert back to integer and check constraints
        # Time: O(n) for join and conversion
        result = int(''.join(digits))
        
        # Check 32-bit integer constraint
        return result if result <= (2**31 - 1) else -1

"""
Example Test Cases:
------------------
1. n = 12
   - Find decreasing: None from right in 12
   - Swap 1 and 2
   - Result: 21

2. n = 21
   - Find decreasing: None from right in 21
   - Return -1 (already largest)

3. n = 123
   - Find decreasing: 2 < 3
   - Swap 2 with 3
   - Result: 132

4. n = 1234321
   - Find decreasing: 3 < 4
   - Find next greater: 4
   - Swap: 1234421
   - Reverse after: 1234124

Edge Cases:
----------
1. Single digit numbers: Always return -1
2. Numbers exceeding 32-bit int: Return -1
3. Descending digits (54321): Return -1
4. All same digits (1111): Return -1

Time Complexity:
--------------
- Overall: O(n) where n is number of digits
- Each step is at most O(n)
- Number of digits = O(log N) where N is input number
- Therefore, in terms of input number: O(log N)

Space Complexity:
---------------
- O(n) where n is number of digits
- O(log N) where N is input number
"""