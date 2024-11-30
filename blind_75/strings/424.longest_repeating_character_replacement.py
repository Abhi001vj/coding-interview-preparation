# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# Code
# Testcase
# Test Result
# Test Result
# 424. Longest Repeating Character Replacement
# Medium
# Topics
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length
"""
APPROACH:
Sliding Window with Character Count

Key Insights:
1. Window contains: most_frequent_char + k other chars
2. Valid window: window_size - most_frequent_char <= k
3. Track character frequencies in window

VISUALIZATION:
s = "AABABBA", k = 1

Window movement:
[A] -> count={A:1}, valid=1
[AA] -> count={A:2}, valid=2
[AAB] -> count={A:2,B:1}, valid=3
[AABA] -> count={A:3,B:1}, valid=4
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Edge case
        if not s:
            return 0
        
        # Initialize window
        char_count = {}
        max_length = 0
        max_count = 0  # Track max frequency in current window
        left = 0
        
        # Slide window
        for right in range(len(s)):
            # Add new character to window
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_count = max(max_count, char_count[s[right]])
            
            # Check if window is valid
            # Window length - most frequent char count <= k
            window_size = right - left + 1
            if window_size - max_count > k:
                # Shrink window
                char_count[s[left]] -= 1
                left += 1
            else:
                max_length = max(max_length, window_size)
        
        return max_length

"""
DETAILED WALKTHROUGH:
Example: "AABABBA", k = 1

Step by Step:
1. Window: "A"
   char_count = {A:1}
   max_count = 1
   valid: 1-1 <= 1 ✓
   max_length = 1

2. Window: "AA"
   char_count = {A:2}
   max_count = 2
   valid: 2-2 <= 1 ✓
   max_length = 2

3. Window: "AAB"
   char_count = {A:2, B:1}
   max_count = 2
   valid: 3-2 <= 1 ✓
   max_length = 3

4. Window: "AABA"
   char_count = {A:3, B:1}
   max_count = 3
   valid: 4-3 <= 1 ✓
   max_length = 4

Alternative Implementation with Optimization:
"""

class OptimizedSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Optimized version using array for counts
        and avoiding max operation
        """
        count = [0] * 26  # For uppercase letters
        max_count = 0
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            # Add new character
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            max_count = max(max_count, count[idx])
            
            # Check window validity
            window_size = right - left + 1
            
            # If invalid window
            if window_size - max_count > k:
                # Remove leftmost character
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            else:
                max_length = window_size
        
        return max_length

"""
KEY INSIGHTS AND OPTIMIZATIONS:

1. Window Validity:
   - window_size - max_count <= k
   - This means we can replace k characters
   - Remaining characters are the most frequent one

2. Max Count Optimization:
   - Don't need to recalculate max_count when shrinking
   - Only update when adding characters
   - This works because max_length only increases

3. Memory Optimization:
   - Use array instead of dictionary for uppercase letters
   - Better cache performance
   - Constant space O(26)

VISUAL STATE TRACKING:

Example: "AABABBA", k=1
Window States:

1. [A]ABABBA
   count={A:1}
   max_count=1
   valid: 1-1 ≤ 1 ✓

2. [AA]BABBA
   count={A:2}
   max_count=2
   valid: 2-2 ≤ 1 ✓

3. [AAB]ABBA
   count={A:2,B:1}
   max_count=2
   valid: 3-2 ≤ 1 ✓

4. [AABA]BBA
   count={A:3,B:1}
   max_count=3
   valid: 4-3 ≤ 1 ✓

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Solution 1: Sliding Window with Character Count
def characterReplacement(s: str, k: int) -> int:
    """
    Time Complexity: O(n) where n is length of string
    Space Complexity: O(1) since we only store 26 characters max
    """
    # Initialize window boundaries and max frequency
    left = 0
    counts = {}
    max_count = 0
    max_length = 0
    
    # Iterate through the string with right pointer
    for right in range(len(s)):
        # Update frequency count for current character
        counts[s[right]] = counts.get(s[right], 0) + 1
        max_count = max(max_count, counts[s[right]])
        
        # Current window size is (right - left + 1)
        # If window_size - max_frequency > k, we need more changes than allowed
        current_length = right - left + 1
        if current_length - max_count > k:
            # Window is invalid, shrink it
            counts[s[left]] -= 1
            left += 1
        
        # Update max_length 
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Solution 2: Optimized Sliding Window with Binary Search
def characterReplacement_binary_search(s: str, k: int) -> int:
    """
    Time Complexity: O(n log n) where n is length of string
    Space Complexity: O(1)
    """
    def can_form_substring(length):
        counts = {}
        # Try each window of given length
        for i in range(length):
            counts[s[i]] = counts.get(s[i], 0) + 1
            
        if max(counts.values()) + k >= length:
            return True
            
        # Slide the window
        for i in range(length, len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            counts[s[i - length]] -= 1
            if counts[s[i - length]] == 0:
                del counts[s[i - length]]
            if max(counts.values()) + k >= length:
                return True
                
        return False
    
    # Binary search for the length
    left, right = 1, len(s)
    result = 1
    
    while left <= right:
        mid = (left + right) // 2
        if can_form_substring(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

# Test cases
def test_solutions():
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("ABCD", 1, 2),
        ("", 1, 0)
    ]
    
    for s, k, expected in test_cases:
        assert characterReplacement(s, k) == expected
        assert characterReplacement_binary_search(s, k) == expected
        print(f"Test passed for s={s}, k={k}, expected={expected}")

# Visualization function
def visualize_window_sliding(s: str, k: int):
    """
    Helper function to visualize how the window slides
    """
    current_window = []
    counts = {}
    left = 0
    
    print("Visualization of window sliding for:", s)
    print("k =", k)
    print("-" * 50)
    
    for right in range(len(s)):
        current_window.append(s[right])
        counts[s[right]] = counts.get(s[right], 0) + 1
        max_count = max(counts.values())
        
        while (right - left + 1) - max_count > k:
            counts[s[left]] -= 1
            current_window.pop(0)
            left += 1
            
        print(f"Window: {''.join(current_window)}")
        print(f"Counts: {counts}")
        print(f"Max frequency: {max_count}")
        print(f"Changes needed: {(right - left + 1) - max_count}")
        print("-" * 50)

# Example usage of visualization
visualize_window_sliding("ABAB", 2)