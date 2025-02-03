
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# Code
# Testcase
# Test Result
# Test Result
# 438. Find All Anagrams in a String
# Medium
# Topics
# Companies
# Given two strings s and p, return an array of all the start indices of p's 
# anagrams
#  in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.
# Seen this question in a real interview before?
# 1/5

"""
Find All Anagrams in String Solutions

Issues with Current Solution:
1. Time Complexity: O(n * k * log k) where k is length of pattern
   - For each window: O(k log k) for sorting
   - Sliding n times: O(n)
2. Unnecessary sorting of pattern repeatedly
3. Wrong window size (right+1 makes window too large)
4. Missing edge case when remaining window is too small

Corrected Version of Your Approach:
"""

class SortingSolution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Your approach corrected:
        
        Example: s = "cbaebabacd", p = "abc"
        Pattern sorted: "abc"
        
        Window iterations:
        "cba" -> "abc" = "abc" ✓ Add 0
        "bae" -> "abe" ≠ "abc" ✗
        "aeb" -> "abe" ≠ "abc" ✗
        "eba" -> "abe" ≠ "abc" ✗
        "bab" -> "abb" ≠ "abc" ✗
        "aba" -> "aab" ≠ "abc" ✗
        "bac" -> "abc" = "abc" ✓ Add 6
        """
        if len(s) < len(p):
            return []
            
        p_sorted = sorted(p)
        left = 0
        right = len(p) - 1  # Fixed window size
        result = []
        
        while right < len(s):
            if sorted(s[left:right + 1]) == p_sorted:
                result.append(left)
            left += 1
            right += 1
            
        return result

"""
1. Sliding Window with Counter (Optimal Solution)
Time: O(n) where n is length of string
Space: O(k) where k is size of character set (26)
"""

from collections import Counter

class CounterSolution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Example visualization: s = "cbaebabacd", p = "abc"
        
        Initial pattern counter:
        {'a': 1, 'b': 1, 'c': 1}
        
        Window iterations:
        1. "cba":
           {'a': 0, 'b': 0, 'c': 0} ✓ Add 0
           
        2. "bae":
           {'a': 0, 'b': 0, 'c': -1, 'e': 1} ✗
           
        3. Sliding window...
        
        6. "bac":
           {'a': 0, 'b': 0, 'c': 0} ✓ Add 6
        """
        if len(s) < len(p):
            return []
            
        p_count = Counter(p)
        window_count = Counter()
        result = []
        
        # Initialize first window
        for i in range(len(p)):
            window_count[s[i]] += 1
            
        # Check first window
        if window_count == p_count:
            result.append(0)
            
        # Slide window
        for i in range(len(p), len(s)):
            # Remove leftmost character
            window_count[s[i - len(p)]] -= 1
            if window_count[s[i - len(p)]] == 0:
                del window_count[s[i - len(p)]]
                
            # Add new character
            window_count[s[i]] += 1
            
            # Check window
            if window_count == p_count:
                result.append(i - len(p) + 1)
                
        return result

"""
2. Array-based Sliding Window (Memory Efficient)
Time: O(n)
Space: O(1) - fixed size array
"""

class ArraySolution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Uses array to count characters:
        [a,b,c,d,...,z]
        
        Example: s = "cbaebabacd", p = "abc"
        Pattern array:
        [1,1,1,0,...,0]
        
        Window array changes:
        "cba": [1,1,1,0,...,0] ✓
        "bae": [1,1,0,0,1,...,0] ✗
        """
        if len(s) < len(p):
            return []
            
        result = []
        p_count = [0] * 26
        window_count = [0] * 26
        
        # Build pattern array
        for char in p:
            p_count[ord(char) - ord('a')] += 1
            
        # Initialize first window
        for i in range(len(p)):
            window_count[ord(s[i]) - ord('a')] += 1
            
        # Check first window
        if window_count == p_count:
            result.append(0)
            
        # Slide window
        for i in range(len(p), len(s)):
            # Remove leftmost character
            window_count[ord(s[i - len(p)]) - ord('a')] -= 1
            # Add new character
            window_count[ord(s[i]) - ord('a')] += 1
            
            # Check window
            if window_count == p_count:
                result.append(i - len(p) + 1)
                
        return result

"""
3. Optimization: Character Count Difference
Time: O(n)
Space: O(1)
"""

class DifferenceTracking:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Track number of matching characters:
        
        Example: s = "cbaebabacd", p = "abc"
        Initial matches needed: 3
        
        Window changes:
        "cba": matches = 3 ✓
        "bae": matches = 1 ✗
        """
        if len(s) < len(p):
            return []
            
        result = []
        p_count = [0] * 26
        window_count = [0] * 26
        matches = 0
        
        # Build pattern array
        for char in p:
            p_count[ord(char) - ord('a')] += 1
            
        # Initialize first window
        for i in range(len(p)):
            window_count[ord(s[i]) - ord('a')] += 1
            
        # Count initial matches
        for i in range(26):
            if window_count[i] == p_count[i]:
                matches += 1
                
        # Check first window
        if matches == 26:
            result.append(0)
            
        # Slide window
        for i in range(len(p), len(s)):
            # Update left character
            left_char = ord(s[i - len(p)]) - ord('a')
            if window_count[left_char] == p_count[left_char]:
                matches -= 1
            elif window_count[left_char] - 1 == p_count[left_char]:
                matches += 1
            window_count[left_char] -= 1
            
            # Update right character
            right_char = ord(s[i]) - ord('a')
            if window_count[right_char] == p_count[right_char]:
                matches -= 1
            elif window_count[right_char] + 1 == p_count[right_char]:
                matches += 1
            window_count[right_char] += 1
            
            # Check window
            if matches == 26:
                result.append(i - len(p) + 1)
                
        return result

"""
Comparison of Approaches:

1. Sorting Solution (Original):
   Pros:
   + Simple to understand
   + Works with any character set
   Cons:
   - O(n * k * log k) time complexity
   - Unnecessary repeated sorting
   - Higher space complexity

2. Counter Solution:
   Pros:
   + O(n) time complexity
   + Simple implementation
   + Works with any character set
   Cons:
   - Higher space constant factor
   - Hash table overhead

3. Array Solution:
   Pros:
   + O(n) time complexity
   + O(1) space complexity
   + Better cache performance
   Cons:
   - Limited to lowercase letters
   - Less flexible

4. Difference Tracking:
   Pros:
   + O(n) time complexity
   + O(1) space complexity
   + Fewer comparisons
   Cons:
   - More complex implementation
   - Limited to lowercase letters

Recommended Solution:
For interviews, use Counter Solution because:
1. Clean and simple to implement
2. Easy to explain
3. Optimal time complexity
4. Flexible for different character sets

For production with constraints:
1. Small character set: Array Solution
2. Memory constraints: Difference Tracking
3. Unicode support: Counter Solution
"""
"""
Sliding Window Timing Analysis

Let's analyze two approaches to understand when we check the window:

1. Current Implementation (Check BEFORE adding new character):
"""

def findAnagrams_check_before(s: str, p: str) -> List[int]:
    """
    Example: s = "cbaebabacd", p = "abc"
    
    Window movement visualization:
    
    Step 1: Window is "cba"
    Index:  0 1 2 3 4 5 6 7 8 9
    String: c b a e b a b a c d
            ↑ ↑ ↑
            Check now: Counter({'c': 1, 'b': 1, 'a': 1}) ✓
            
    Step 2: Before adding 'e'
    Index:  0 1 2 3 4 5 6 7 8 9
    String: c b a e b a b a c d
              ↑ ↑ ↑
            Check now: Counter({'b': 1, 'a': 1, 'e': 0}) ✓
            
    IMPORTANT: We check BEFORE adding 'e'
    """
    if len(s) < len(p):
        return []
        
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    # Initialize first window
    for i in range(len(p)):
        window_count[s[i]] += 1
        
    # Slide window
    for i in range(len(p), len(s)):
        # Check BEFORE adding new character
        if window_count == p_count:
            result.append(i - len(p))
            
        # Update window
        window_count[s[i - len(p)]] -= 1  # Remove old
        if window_count[s[i - len(p)]] == 0:
            del window_count[s[i - len(p)]]
        window_count[s[i]] += 1  # Add new
        
    # Check last window
    if window_count == p_count:
        result.append(len(s) - len(p))
        
    return result

"""
2. Alternative Implementation (Check AFTER adding new character):
"""

def findAnagrams_check_after(s: str, p: str) -> List[int]:
    """
    Example with same string: s = "cbaebabacd", p = "abc"
    
    Window movement visualization:
    
    Step 1: After adding 'e'
    Index:  0 1 2 3 4 5 6 7 8 9
    String: c b a e b a b a c d
              ↑ ↑ ↑
            Check now: Counter({'b': 1, 'a': 1, 'e': 1}) ✗
            Wrong! Window includes 'e'
    """
    if len(s) < len(p):
        return []
        
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    # Initialize first window
    for i in range(len(p)):
        window_count[s[i]] += 1
        
    # Slide window
    for i in range(len(p), len(s)):
        # Update window first
        window_count[s[i - len(p)]] -= 1  # Remove old
        if window_count[s[i - len(p)]] == 0:
            del window_count[s[i - len(p)]]
        window_count[s[i]] += 1  # Add new
        
        # Check AFTER adding new character
        if window_count == p_count:
            result.append(i - len(p) + 1)  # Different index calculation!
    
    return result

"""
Key Differences:

1. Timing of Check:
   First approach:  Check → Remove old → Add new
   Second approach: Remove old → Add new → Check

2. Index Calculation:
   First approach:  i - len(p)
   Second approach: i - len(p) + 1

3. Window Content:
   First approach:  Checks old window before changes
   Second approach: Checks new window after changes

Example walkthrough with "cbaebabacd" and "abc":

First Approach (Check Before):
1. Window "cba" → Check → ✓ Add 0
2. Remove 'c', Add 'e' → Window "bae"
3. Window "bae" → Check → ✗
4. Remove 'b', Add 'b' → Window "aeb"
5. Window "aeb" → Check → ✗
...

Second Approach (Check After):
1. Window "cba" → Check → ✓ Add 0
2. Remove 'c', Add 'e' → Window "bae" → Check → ✗
3. Remove 'b', Add 'b' → Window "aeb" → Check → ✗
...

Recommendation:
The first approach (check before) is cleaner because:
1. We check the valid window before modification
2. Index calculation is simpler to understand
3. We don't accidentally include invalid characters in our check
"""