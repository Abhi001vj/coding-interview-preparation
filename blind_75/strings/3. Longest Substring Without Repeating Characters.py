
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Code


# Testcase
# Test Result
# Test Result
# 3. Longest Substring Without Repeating Characters
# Medium
# Topics
# Companies
# Hint
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

"""
APPROACH 1: Sliding Window with Set
- Most intuitive solution
- Uses sliding window technique
- O(n) time complexity
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        # Initialize sliding window
        char_set = set()
        max_length = 0
        left = 0
        
        # Iterate through string with right pointer
        for right in range(len(s)):
            # Shrink window while we have duplicate
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add new character and update max length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            
        return max_length

"""
VISUALIZATION OF SLIDING WINDOW:
Example: "abcabcbb"

Step by step:
1. "a" -> {a} -> length=1
   a|bcabcbb
   ^

2. "ab" -> {a,b} -> length=2
   ab|cabcbb
   ^^

3. "abc" -> {a,b,c} -> length=3
   abc|abcbb
   ^^^

4. Found 'a' again:
   Remove 'a' from start, add new 'a'
   bca|bcbb
   ^^^

And so on...

APPROACH 2: Optimized with Dictionary
- Keeps track of last position of each character
- Allows jumping left pointer
"""

class OptimizedSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        # Dictionary to store last position of each char
        char_pos = {}
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            # If char is seen and its last position is >= left
            if char in char_pos and char_pos[char] >= left:
                left = char_pos[char] + 1
            else:
                max_length = max(max_length, right - left + 1)
                
            char_pos[char] = right
            
        return max_length

"""
VISUALIZATION OF OPTIMIZED APPROACH:
Example: "abcabcbb"

Dictionary state:
1. {a:0, b:1, c:2}
   abc|abcbb
   ^^^

2. Found 'a': Jump left to position 1
   {a:3, b:1, c:2}
   bca|bcbb
   ^^^

3. Found 'b': Jump left to position 2
   {a:3, b:4, c:2}
   cab|cbb
   ^^^

APPROACH 3: Array-based (for ASCII)
- Most efficient for strings with ASCII chars
- Uses fixed size array instead of hash map
- Better cache performance
"""

class ASCIISolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        # Initialize array for ASCII chars
        char_index = [-1] * 128
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            # Get ASCII value
            idx = ord(char)
            
            # Update left pointer if needed
            left = max(left, char_index[idx] + 1)
            
            # Update max length
            max_length = max(max_length, right - left + 1)
            
            # Store current position
            char_index[idx] = right
            
        return max_length

"""
COMPLEXITY ANALYSIS:

1. Set Solution:
   Time: O(n)
   Space: O(min(m,n)) where m is charset size
   - Each character processed at most twice
   - Set size limited by unique chars

2. Dict Solution:
   Time: O(n)
   Space: O(min(m,n))
   - Single pass through string
   - Constant time lookups
   - Better average case

3. Array Solution:
   Time: O(n)
   Space: O(1) for ASCII
   - Most memory efficient
   - Better cache performance
   - Limited to ASCII

EXAMPLE WALKTHROUGH:
s = "abcabcbb"

Window Movement:
[a] -> 1
[ab] -> 2
[abc] -> 3
b[ca] -> 2
c[ab] -> 2
a[bc] -> 2
b[c] -> 1
[b] -> 1

Max length = 3
"""

