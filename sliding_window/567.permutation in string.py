# https://leetcode.com/problems/permutation-in-string/description/

# Code
# Testcase
# Test Result
# Test Result
# 567. Permutation in String
# Medium
# Topics
# Companies
# Hint
# Given two strings s1 and s2, return true if s2 contains a 
# permutation
#  of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


```python
"""
PERMUTATION IN STRING: Complete Analysis
====================================

Pattern Recognition:
1. Sliding Window
2. Hash Map Counter
3. Fixed-size Window
4. Character Frequency Matching

Key Insights:
1. Window size = len(s1)
2. Order doesn't matter (permutation)
3. All lowercase letters (26 possible characters)
4. Need to match character frequencies
"""

def brute_force_solution(s1: str, s2: str) -> bool:
    """
    Approach 1: Generate All Permutations
    Pattern: Backtracking + String Search
    
    Example: s1 = "ab", s2 = "eidbaooo"
    
    1. Generate all permutations of s1:
       "ab" -> ["ab", "ba"]
    
    2. Search each in s2:
       Check "ab" in "eidbaooo" -> False
       Check "ba" in "eidbaooo" -> True
    
    Time: O(n! * m) where n = len(s1), m = len(s2)
    Space: O(n!) for storing permutations
    """
    from itertools import permutations
    
    # Generate all permutations
    perms = [''.join(p) for p in permutations(s1)]
    
    # Check each permutation
    for perm in perms:
        if perm in s2:
            return True
    return False

def sliding_window_counter(s1: str, s2: str) -> bool:
    """
    Approach 2: Sliding Window with Counter
    Pattern: Fixed-size Window + Counter
    
    Example: s1 = "ab", s2 = "eidbaooo"
    Window size = 2
    
    Visual step-by-step:
    s2: [ei]dbaooo  Counter{'e':1, 'i':1} != Counter{'a':1, 'b':1}
        e[id]baooo  Counter{'i':1, 'd':1} != Counter{'a':1, 'b':1}
        ei[db]aooo  Counter{'d':1, 'b':1} != Counter{'a':1, 'b':1}
        eid[ba]ooo  Counter{'b':1, 'a':1} == Counter{'a':1, 'b':1} ✓
    
    Time: O(k * (n-k)) where k = len(s1), n = len(s2)
    Space: O(k) for counters
    """
    from collections import Counter
    
    # Edge cases
    if len(s1) > len(s2):
        return False
        
    s1_count = Counter(s1)
    window_size = len(s1)
    
    # Initial window
    window_count = Counter(s2[:window_size])
    if window_count == s1_count:
        return True
    
    # Slide window
    for i in range(len(s2) - window_size):
        # Remove left character
        window_count[s2[i]] -= 1
        if window_count[s2[i]] == 0:
            del window_count[s2[i]]
            
        # Add right character
        window_count[s2[i + window_size]] += 1
        
        # Check if current window is valid
        if window_count == s1_count:
            return True
            
    return False

def array_sliding_window(s1: str, s2: str) -> bool:
    """
    Approach 3: Optimized Array Counts
    Pattern: Fixed-size Window + Array Counter
    
    Example: s1 = "ab", s2 = "eidbaooo"
    
    Initial arrays (a-z counts):
    s1_count:  [1,1,0,0,0,...]  # 'a'=1, 'b'=1
    cur_count: [0,0,0,0,1,...]  # 'e'=1
    
    Window Evolution:
    Window      Matches  Array State
    [ei]        0       [0,0,0,1,1,...]
    [id]        0       [0,0,0,1,1,...]
    [db]        1       [0,1,0,1,0,...]
    [ba]        2       [1,1,0,0,0,...] ✓
    
    Time: O(n) where n = len(s2)
    Space: O(1) - fixed size array
    """
    if len(s1) > len(s2):
        return False
    
    # Initialize count arrays (26 lowercase letters)
    s1_count = [0] * 26
    window_count = [0] * 26
    
    # Fill s1 counts
    for c in s1:
        s1_count[ord(c) - ord('a')] += 1
    
    # Initial window
    window_size = len(s1)
    for i in range(window_size):
        window_count[ord(s2[i]) - ord('a')] += 1
    
    # Check initial window
    if s1_count == window_count:
        return True
    
    # Slide window
    for i in range(len(s2) - window_size):
        # Update window counts
        window_count[ord(s2[i]) - ord('a')] -= 1
        window_count[ord(s2[i + window_size]) - ord('a')] += 1
        
        # Check current window
        if s1_count == window_count:
            return True
    
    return False

def optimized_sliding_window(s1: str, s2: str) -> bool:
    """
    Approach 4: Match Count Optimization
    Pattern: Fixed-size Window + Match Counter
    
    Example: s1 = "ab", s2 = "eidbaooo"
    
    Track matches instead of comparing full arrays:
    1. Start: matches = 0 out of 26 needed
    2. When character count matches in both arrays:
       matches += 1
    3. When character count differs:
       matches -= 1
    4. Return True if matches == 26
    
    Time: O(n) where n = len(s2)
    Space: O(1)
    """
    if len(s1) > len(s2):
        return False
        
    s1_count = [0] * 26
    window_count = [0] * 26
    matches = 0
    
    # Initialize s1 counts
    for c in s1:
        idx = ord(c) - ord('a')
        s1_count[idx] += 1
    
    # Initial window
    window_size = len(s1)
    for i in range(window_size):
        idx = ord(s2[i]) - ord('a')
        window_count[idx] += 1
        if window_count[idx] == s1_count[idx]:
            matches += 1
        elif window_count[idx] == s1_count[idx] + 1:
            matches -= 1
    
    if matches == 26:
        return True
    
    # Slide window
    for i in range(len(s2) - window_size):
        # Remove left character
        left_idx = ord(s2[i]) - ord('a')
        if window_count[left_idx] == s1_count[left_idx]:
            matches -= 1
        elif window_count[left_idx] == s1_count[left_idx] + 1:
            matches += 1
        window_count[left_idx] -= 1
        
        # Add right character
        right_idx = ord(s2[i + window_size]) - ord('a')
        window_count[right_idx] += 1
        if window_count[right_idx] == s1_count[right_idx]:
            matches += 1
        elif window_count[right_idx] == s1_count[right_idx] + 1:
            matches -= 1
            
        if matches == 26:
            return True
            
    return False

"""
EDGE CASES AND HANDLING
=====================
1. Empty strings:
   s1 = ""     -> True (empty string is permutation of itself)
   s2 = ""     -> False if s1 not empty
   
2. Length comparison:
   len(s1) > len(s2) -> False
   
3. Single characters:
   s1 = "a", s2 = "a" -> True
   s1 = "a", s2 = "b" -> False
   
4. Repeated characters:
   s1 = "aaa", s2 = "aaaa" -> True
   
5. No common characters:
   s1 = "abc", s2 = "xyz" -> False

OPTIMIZATION TECHNIQUES
====================
1. Early termination:
   - Check lengths first
   - Return true as soon as match found
   
2. Space optimization:
   - Use array instead of hash map
   - Track matches instead of comparing arrays
   
3. Time optimization:
   - Fixed size window (no need to try different sizes)
   - O(1) lookups with arrays
   
4. Memory optimization:
   - Reuse arrays
   - In-place counting where possible
"""