# https://leetcode.com/problems/palindrome-permutation/
# 266. Palindrome Permutation
# Easy
# Topics
# Companies
# Hint
# Given a string s, return true if a permutation of the string could form a 
# palindrome
#  and false otherwise.

 

# Example 1:

# Input: s = "code"
# Output: false
# Example 2:

# Input: s = "aab"
# Output: true
# Example 3:

# Input: s = "carerac"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5000
# s consists of only lowercase English letters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 216.6K
# Submissions
# 318.6K
# Acceptance Rate
# 68.0%
# Topics
# Companies
# 0 - 3 months
# Meta
# 3
# Microsoft
# 2
# 0 - 6 months
# Google
# 2
# Bloomberg
# 2
# Uber
# 2
# 6 months ago
# Nordstrom
# 3
# Docusign
# 2
# Hint 1
# Consider the palindromes of odd vs even length. What difference do you notice?
# Hint 2
# Count the frequency of each character.
# Hint 3
# If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        if len(s) == 1:
            return True
        char_count = Counter(s)

        total_count = 0
        odd_count = 0
        for count in char_count.values():
            total_count += (count // 2) * 2
            if count % 2:
                odd_count += 1
        
        if odd_count > 1:
            return False
        
        return (total_count + odd_count) == len(s)
                
"""
Problem: Palindrome Permutation
Given a string, determine if its permutation can form a palindrome.

Key Insights:
1. A string can form a palindrome if and only if:
   - All characters appear an even number of times (for even length strings)
   - All characters but one appear an even number of times (for odd length strings)

2. Examples:
   "carerac" -> True
   Visualization:
   c a r e r a c
   Step 1: Count frequencies
   c: 2, a: 2, r: 2, e: 1
   Step 2: Check if at most one character has odd frequency
   c(2) a(2) r(2) e(1) ✓
   Step 3: Can form palindrome: "racecar"

Solutions:

1. Brute Force Solution - Generate All Permutations
Time Complexity: O(n! * n)
Space Complexity: O(n!)
"""

from itertools import permutations

class Solution1:
    def canPermutePalindrome(self, s: str) -> bool:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        # Generate all permutations and check each one
        perms = [''.join(p) for p in permutations(s)]
        return any(is_palindrome(p) for p in perms)

"""
2. Hash Map Solution - Count Frequencies
Time Complexity: O(n)
Space Complexity: O(k) where k is size of character set (26 for lowercase letters)
"""

from collections import Counter

class Solution2:
    def canPermutePalindrome(self, s: str) -> bool:
        # Count character frequencies
        char_count = Counter(s)
        
        # Count characters with odd frequencies
        odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
        
        # Can form palindrome if at most one character has odd frequency
        return odd_count <= 1

"""
3. Bit Vector Solution - Space Optimized
Time Complexity: O(n)
Space Complexity: O(1) - uses only an integer (32/64 bits)

Key Insight: We only need to track if a character appears odd/even times
- Use a bit to represent odd/even occurrence of each character
- Toggle bit when character is encountered
- At end, bit vector should have at most one bit set
"""

class Solution3:
    def canPermutePalindrome(self, s: str) -> bool:
        # Use integer as bit vector
        bit_vector = 0
        
        # Toggle bit for each character
        for char in s:
            bit_vector ^= 1 << (ord(char) - ord('a'))
        
        # Check if at most one bit is set
        # x & (x-1) clears rightmost set bit
        # If result is 0, at most one bit was set
        return bit_vector & (bit_vector - 1) == 0

"""
4. Set Solution - Track Odd Occurrences
Time Complexity: O(n)
Space Complexity: O(k) where k is size of character set
"""

class Solution4:
    def canPermutePalindrome(self, s: str) -> bool:
        # Set to track characters with odd count
        odd_chars = set()
        
        # Add char to set if appears odd times, remove if even
        for char in s:
            if char in odd_chars:
                odd_chars.remove(char)
            else:
                odd_chars.add(char)
        
        # Can form palindrome if at most one char appears odd times
        return len(odd_chars) <= 1

"""
Big O Analysis Breakdown:

1. Brute Force (Solution1):
   - Time: O(n! * n)
     * n! to generate all permutations
     * n to check each permutation for palindrome
   - Space: O(n!)
     * Stores all permutations

2. Hash Map (Solution2):
   - Time: O(n)
     * One pass to count frequencies: O(n)
     * One pass over frequency counts: O(k) where k ≤ 26
   - Space: O(k)
     * Stores frequency count for each unique char
     * k ≤ 26 for lowercase English letters

3. Bit Vector (Solution3):
   - Time: O(n)
     * One pass through string: O(n)
     * Bit operations are O(1)
   - Space: O(1)
     * Uses single integer (32/64 bits)
     * Independent of input size

4. Set (Solution4):
   - Time: O(n)
     * One pass through string: O(n)
     * Set operations are O(1)
   - Space: O(k)
     * Stores at most k unique chars
     * k ≤ 26 for lowercase English letters

Recommended Solution:
The Bit Vector solution (Solution3) is optimal for this problem because:
1. O(n) time complexity - single pass through input
2. O(1) space complexity - uses constant extra space
3. Simple and efficient bit operations
4. Works well for given constraints (lowercase English letters)

Example Walkthrough for "carerac":
Bit Vector State (showing only relevant bits):
Initial: 000000
c: 000001
a: 000011
r: 001011
e: 011011
r: 010011
a: 010001
c: 010000
Final: 010000 (only 'e' appears odd times)
010000 & 001111 = 0 ✓ Can form palindrome
"""