# https://leetcode.com/problems/longest-palindrome/description/
# Code
# Testcase
# Test Result
# Test Result
# 409. Longest Palindrome
# Easy
# Topics
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 862.4K
# Submissions
# 1.6M
# Acceptance Rate
# 55.4%
# Topics
# Hash Table
# String
# Greedy
# Companies
# 0 - 3 months
# Google
# 3
# HP
# 2
# 0 - 6 months
# Amazon
# 2
# 6 months ago
# Bloomberg
# 7
# Meta
# 5
# Microsoft
# 5
# Oracle
# 3
# Apple
# 2
# Walmart Labs
# 2

"""
Longest Palindrome Builder - Pattern Analysis and Solution
-------------------------------------------------------

Core Patterns:
1. Character Frequency Counting
2. Greedy Selection of Pairs
3. Optional Center Character

Time Complexity: O(n) - single pass through string
Space Complexity: O(1) - bounded by alphabet size (52 characters)

Visual Pattern Recognition:
-------------------------
Example: s = "abccccdd"

Character Frequencies:
a: 1 → □           Can use: 0 + middle
b: 1 → □           Can use: 0
c: 4 → □□□□        Can use: 4 (2 pairs)
d: 2 → □□          Can use: 2 (1 pair)

Palindrome Building Rules:
┌─────────────────┐
│ Even counts     │ → Use all characters
│ Odd counts      │ → Use (count-1) + maybe middle
│ Multiple odds   │ → Only one can be middle
└─────────────────┘

Palindrome Structure:
left_half | middle | right_half
(pairs)   │(0/1)  │ (pairs reversed)
"""

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Calculate length of longest possible palindrome.
        
        Approach:
        1. Count character frequencies
        2. Use all pairs of characters
        3. Optionally add one character in middle
        
        Example Visualization:
        s = "abccccdd"
        
        Palindrome Formation:
        d c c | a | c c d
        ↑     │ ↑ │     ↑
        pair  │odd│   pair
        
        Time: O(n) - one pass through string
        Space: O(1) - fixed size counter
        """
        # Count character frequencies
        char_count = Counter(s)
        
        """
        Counter Visualization:
        For s = "abccccdd":
        
        char | count | pairs | remainder
        -----+-------+-------+----------
        a    |   1   |   0   |    1
        b    |   1   |   0   |    1
        c    |   4   |   2   |    0
        d    |   2   |   1   |    0
        """
        
        # Track palindrome length and odd count existence
        length = 0
        has_odd = False
        
        # Process each character count
        for count in char_count.values():
            # Add complete pairs
            length += (count // 2) * 2
            # Track if we have an odd count
            if count % 2:
                has_odd = True
                
        """
        Pair Processing Example:
        count = 4 (for 'c'):
        - count//2 = 2 (pairs)
        - 2 * 2 = 4 (characters used)
        
        count = 1 (for 'a'):
        - count//2 = 0 (pairs)
        - has_odd = True
        """
        
        # Add middle character if we have odds
        return length + (1 if has_odd else 0)

"""
Test Cases Analysis:
------------------

1. Basic Case: "abccccdd"
   Counts: a(1), b(1), c(4), d(2)
   Pairs: 0 + 0 + 4 + 2 = 6
   Odd exists: Yes
   Result: 6 + 1 = 7
   
   Visualization:
   d c c | a | c c d
   
2. Single Character: "a"
   Counts: a(1)
   Pairs: 0
   Odd exists: Yes
   Result: 0 + 1 = 1
   
   Visualization:
   | a |
   
3. All Pairs: "aaaa"
   Counts: a(4)
   Pairs: 4
   Odd exists: No
   Result: 4
   
   Visualization:
   a a | | a a
   
4. Case Sensitive: "Aa"
   Counts: A(1), a(1)
   Pairs: 0
   Odd exists: Yes
   Result: 0 + 1 = 1

Edge Cases:
----------
1. Empty string: ""
   - Returns 0 (no characters)
   
2. All unique: "abc"
   - Can only use one character in middle
   - Returns 1
   
3. All same: "aaaaa"
   - Use all pairs + middle
   - Returns 5

Why This Solution is Optimal:
--------------------------
1. Single Pass:
   - Only need to count frequencies once
   - Process each count once
   
2. No Sorting Required:
   - Don't need character order
   - Only care about counts
   
3. No Actual Construction:
   - Don't need to build palindrome
   - Only need length

Alternative Approaches Considered:
------------------------------
1. Sorting approach:
   - Sort string first
   - Count consecutive same characters
   - O(n log n) - worse
   
2. Set approach:
   - Track odd/even counts in sets
   - More complex, same complexity
   
3. Array approach:
   - Use array instead of Counter
   - Similar complexity, less readable
"""