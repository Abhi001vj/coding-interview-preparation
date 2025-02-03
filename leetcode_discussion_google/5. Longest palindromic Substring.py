# https://leetcode.com/problems/longest-palindromic-substring/description/

# Code
# Testcase
# Testcase
# Test Result
# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3.5M
# Submissions
# 10.1M
# Acceptance Rate
# 34.9%
# Topics
# Companies
# Hint 1
# How can we reuse a previously computed palindrome to compute a larger palindrome?
# Hint 2
# If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
# Hint 3
# Complexity based hint:
# If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        def expand_around_center(left, right):
            while 0 <= left and right < len(s) and s[left] == s [right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            l1, r1 = expand_around_center(i,i)
            l2, r2 = expand_around_center(i,i+1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        
        return s[start:end+1]

"""
Framework for Analyzing Time Complexity in Two-Pointer Approaches

1. Two-Pointer Time Complexity Analysis Framework:

   Step 1: Identify the loops and their ranges
   - Outer loop range: How many starting positions?
   - Inner loop range: How far can pointers move?
   
   Step 2: Calculate maximum operations
   - Outer loop iterations × Max inner loop operations
   
   Step 3: Find worst-case scenario
   - What input causes maximum operations?

2. Analysis of Longest Palindromic Substring:

Example Visualization for "racecar":
Index:  0 1 2 3 4 5 6
String: r a c e c a r
        ↑         ↑
        L         R

Odd-length palindrome expansion at 'e':
Step 0:   r a c e c a r    Compare e-e:        1 operation
Step 1:   r a c(e)c a r    Compare c-c:        2 operations
Step 2:   r a(c e c)a r    Compare a-a:        3 operations
Step 3:   r(a c e c a)r    Compare r-r:        4 operations
Step 4:  (r a c e c a r)   Failed comparison:  5 operations

Time Complexity Breakdown:

1. Outer Loop Analysis:
   - Iterates through each character: O(n)
   - For string length n, we have n iterations

2. Inner Loop Analysis (expand_around_center):
   - For each position i:
     * Odd-length: expands around i
     * Even-length: expands around i and i+1
   - Maximum expansion: min(i, n-i-1) steps
   
3. Total Operations Analysis:
   For position i:
   - Left pointer can go: i steps left
   - Right pointer can go: (n-i-1) steps right
   Total for position i = min(i, n-i-1)

4. Worst Case Scenario:
   - Middle position (i ≈ n/2)
   - Can expand n/2 steps in both directions
   - Each expansion takes O(n) operations

Total Time Complexity:
- Outer loop: O(n) positions
- For each position: O(n) expansion steps
- Final complexity: O(n²)

Space Complexity: O(1) - only using constant extra space
"""

def visualize_time_complexity():
    """
    Visual example of operations for string "racecar":
    
    Position 0 (r):
    r|a c e c a r
    r a|c e c a r
    Max steps: 1
    
    Position 1 (a):
    r a|c e c a r
    r a c|e c a r
    Max steps: 2
    
    Position 2 (c):
    r a c|e c a r
    r a c e|c a r
    Max steps: 3
    
    Position 3 (e) - Center:
    r a c e|c a r
    r a c e c|a r
    r a c e c a|r
    Max steps: 3
    
    Total operations = Sum of steps at each position
    O(n) positions × O(n) max steps = O(n²)
    """
    pass

"""
Framework Application to Similar Problems:

1. Two Sum II (Sorted Array):
   ```python
   def twoSum(self, numbers: List[int], target: int) -> List[int]:
       left, right = 0, len(numbers) - 1
       while left < right:
           curr_sum = numbers[left] + numbers[right]
           if curr_sum == target:
               return [left + 1, right + 1]
           elif curr_sum < target:
               left += 1
           else:
               right -= 1
   ```
   Analysis:
   - One pointer moves right, one moves left
   - Each pointer moves at most n steps
   - Total: O(n) as pointers move linearly

2. Container With Most Water:
   ```python
   def maxArea(self, height: List[int]) -> int:
       left, right = 0, len(height) - 1
       max_area = 0
       while left < right:
           area = min(height[left], height[right]) * (right - left)
           max_area = max(max_area, area)
           if height[left] < height[right]:
               left += 1
           else:
               right -= 1
       return max_area
   ```
   Analysis:
   - Pointers move towards each other
   - Each position visited once
   - Total: O(n) linear time

3. Longest Palindromic Substring (Our Case):
   ```python
   def expand_around_center(self, s: str, left: int, right: int) -> tuple:
       while left >= 0 and right < len(s) and s[left] == s[right]:
           left -= 1
           right += 1
       return left + 1, right - 1
   ```
   Analysis:
   - For each center: O(n) positions
   - For each expansion: O(n) steps
   - Total: O(n²) quadratic time

Framework Summary for Two-Pointer Problems:

1. Linear Movement (O(n)):
   - Pointers move in one direction
   - Each element visited once
   - Example: Two Sum II

2. Convergent Movement (O(n)):
   - Pointers move towards each other
   - Each element visited once
   - Example: Container With Most Water

3. Expansive Movement (O(n²)):
   - Pointers move outward
   - Each center expands to edges
   - Example: Longest Palindromic Substring

Key Questions for Analysis:
1. How do pointers move? (Linear/Convergent/Expansive)
2. How many starting positions?
3. How many steps per position?
4. Are elements revisited?
"""