# https://leetcode.com/problems/minimum-window-substring/description/
# 76. Minimum Window Substring
# Solved
# Hard
# Topics
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?


# Solution 1: Sliding Window with Character Frequency
def minWindow_v1(s: str, t: str) -> str:
    """
    Time: O(n) where n is length of s
    Space: O(k) where k is unique chars in t
    """
    if not s or not t:
        return ""
        
    # Initialize target frequency map
    target = {}
    for char in t:
        target[char] = target.get(char, 0) + 1
    
    # Variables for window
    required = len(target)  # Number of unique chars needed
    formed = 0     # Number of chars satisfied
    window = {}    # Current window frequencies
    
    # Result tracking
    min_len = float('inf')
    result = ""
    left = 0
    
    for right in range(len(s)):
        # Add character to window
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        # Check if we've satisfied this character's frequency
        if char in target and window[char] == target[char]:
            formed += 1
            
        # Try to minimize window
        while formed == required:
            # Update result if smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
                
            # Remove leftmost character
            char = s[left]
            window[char] -= 1
            if char in target and window[char] < target[char]:
                formed -= 1
            left += 1
            
    return result

# Solution 2: Optimized Sliding Window with Array (for interview discussion)
def minWindow_v2(s: str, t: str) -> str:
    """
    Time: O(n) where n is length of s
    Space: O(1) since we use fixed array size
    
    Optimization: Use array instead of hashmap for ASCII chars
    """
    if not s or not t:
        return ""
        
    # Use array for counting (faster than dict for ASCII)
    target = [0] * 128
    window = [0] * 128
    required = 0
    
    # Build target frequency array
    for char in t:
        if target[ord(char)] == 0:
            required += 1
        target[ord(char)] += 1
    
    formed = 0
    min_len = float('inf')
    result = ""
    left = 0
    
    for right in range(len(s)):
        # Add right char
        char = s[right]
        window[ord(char)] += 1
        
        # Check if frequency matches
        if char in t and window[ord(char)] == target[ord(char)]:
            formed += 1
            
        # Minimize window
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
                
            char = s[left]
            window[ord(char)] -= 1
            if char in t and window[ord(char)] < target[ord(char)]:
                formed -= 1
            left += 1
            
    return result

# Debug Visualization Helper
def debug_window(s: str, t: str, left: int, right: int, window: dict, target: dict) -> str:
    """Helper to visualize window state for debugging"""
    output = []
    output.append(f"\nWindow Analysis:")
    output.append("-" * 50)
    
    # Visualize string with window
    chars = list(s)
    chars.insert(right + 1, "|")
    chars.insert(left, "|")
    output.append("".join(chars))
    
    # Window details
    output.append(f"Current window: {s[left:right+1]}")
    output.append(f"Window counts: {dict(window)}")
    output.append(f"Target counts: {dict(target)}")
    
    # Check validity
    valid = all(
        char in window and window[char] >= count
        for char, count in target.items()
    )
    output.append(f"Valid window? {valid}")
    
    return "\n".join(output)

# Test function with visualization
def test_with_viz(s: str, t: str):
    print(f"\nTesting s='{s}', t='{t}'")
    print("=" * 50)
    
    # Run both solutions
    result1 = minWindow_v1(s, t)
    result2 = minWindow_v2(s, t)
    
    print(f"Solution 1 result: '{result1}'")
    print(f"Solution 2 result: '{result2}'")
    assert result1 == result2, "Solutions produce different results!"