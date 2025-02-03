# https://leetcode.com/problems/valid-anagram/description/
# Code


# Testcase
# Test Result
# Test Result
# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


"""
Hash Map Solution for Unicode Anagrams
Demonstrates how hash maps naturally handle Unicode characters

1. Basic Hash Map Solution with Unicode Support:
"""

from collections import Counter
import unicodedata

class UnicodeSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Hash map naturally handles Unicode because:
        1. Python strings are Unicode by default
        2. Dictionary keys can be any Unicode character
        3. Counter treats each Unicode code point as a distinct key
        
        Example with Unicode:
        s = "café☕"
        t = "éfac☕"
        
        Visualization of Counter:
        {
            'c': 1,
            'a': 1,
            'f': 1,
            'é': 1,    # single Unicode character
            '☕': 1     # emoji is treated as single character
        }
        """
        # Normalize strings to handle combining characters
        s = unicodedata.normalize('NFC', s)
        t = unicodedata.normalize('NFC', t)
        
        return Counter(s) == Counter(t)

"""
2. Detailed Example with Different Unicode Cases:
"""

def demonstrate_unicode_cases():
    """
    Different Unicode scenarios the hash map handles:
    
    1. Basic Unicode:
    s = "Hello世界"
    t = "界世lloHe"
    Counter: {
        'H': 1, 'e': 1, 'l': 2, 'o': 1,
        '世': 1, '界': 1
    }
    
    2. Combining Characters:
    s = "café"      # é as single character
    t = "cafe\u0301" # e + combining acute accent
    After normalization:
    Counter: {
        'c': 1, 'a': 1, 'f': 1,
        'é': 1  # normalized to single character
    }
    
    3. Emojis:
    s = "hello👨‍👩‍👧"
    t = "olleh👨‍👩‍👧"
    Counter: {
        'h': 1, 'e': 1, 'l': 2, 'o': 1,
        '👨‍👩‍👧': 1  # family emoji treated as single character
    }
    """
    pass

"""
3. Performance Analysis for Unicode:

Time Complexity: O(n)
- String normalization: O(n)
- Counter creation: O(n)
- Counter comparison: O(k) where k is unique characters

Space Complexity: O(k)
- k is number of unique Unicode characters
- Each character takes more space than ASCII
- Still O(k) theoretically, but k could be large

Memory Usage Comparison:
ASCII: 1 byte per character
Unicode: 1-4 bytes per character
Extended Unicode: Can be larger for complex emojis

Example Memory Analysis:
"""

def analyze_memory_usage():
    """
    Memory comparison for different character types:
    
    1. ASCII string: "hello"
    Size: 5 bytes
    Counter size: ~40 bytes (4 unique chars)
    
    2. Unicode string: "你好世界"
    Size: 8-12 bytes (2-3 bytes per char)
    Counter size: ~80 bytes (4 unique chars)
    
    3. Emoji string: "😊🌍🎉"
    Size: 12-16 bytes (4+ bytes per char)
    Counter size: ~120 bytes (3 unique chars)
    """
    pass

"""
4. Advanced Unicode Handling:
"""

class AdvancedUnicodeSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Handles all Unicode edge cases:
        1. Different normalization forms
        2. Combining characters
        3. Width variations
        4. Emoji modifiers
        
        Example:
        s = "cafe\u0301"  # é as combining
        t = "éfac"        # é as single char
        
        Steps:
        1. Normalize both strings
        2. Create Counters
        3. Compare
        """
        # Handle different Unicode normalization forms
        s = unicodedata.normalize('NFC', s)
        t = unicodedata.normalize('NFC', t)
        
        # Optional: Case folding for case-insensitive comparison
        # s = s.casefold()
        # t = t.casefold()
        
        return Counter(s) == Counter(t)

"""
5. Hash Map Advantages for Unicode:

1. Flexibility:
   - Automatically handles any Unicode character
   - No fixed size limitation
   - Works with future Unicode additions

2. Simplicity:
   - No need to pre-allocate space
   - No need to know character ranges
   - Natural handling of sparse character sets

3. Correctness:
   - Properly counts all characters
   - Works with normalization
   - Handles complex Unicode sequences

4. Maintainability:
   - Easy to modify for new requirements
   - Clear and readable code
   - Well-supported by Python

Example Usage with Complex Unicode:
"""

def demonstrate_complex_unicode():
    # Various Unicode test cases
    test_cases = [
        ("Hello世界", "界世Hello"),           # Mixed ASCII/Unicode
        ("café☕", "éfac☕"),                 # Accents and emoji
        ("👨‍👩‍👧👨‍👩‍👧", "👨‍👩‍👧👨‍👩‍👧"),         # Complex emoji
        ("ＨｅＬＬｏ", "ｏＬＬｅＨ"),           # Full-width
        ("가나다라", "라다나가")              # Korean
    ]
    
    solution = UnicodeSolution()
    for s, t in test_cases:
        result = solution.isAnagram(s, t)
        print(f"{s} and {t}: {result}")

"""
When to Use Hash Map for Unicode:

1. Best For:
   - General purpose Unicode handling
   - Unknown character ranges
   - Mixed character sets
   - Complex Unicode sequences
   - Maintenance and readability

2. Trade-offs:
   Pros:
   + Flexible
   + Simple implementation
   + Handles all Unicode
   + Easy to modify
   
   Cons:
   - More memory than array for ASCII
   - Slightly slower than array for ASCII
   - Hash collisions possible (rare)
   - Memory overhead per entry

3. Interview Discussion Points:
   - Unicode normalization importance
   - Memory vs speed trade-offs
   - Hash map collision handling
   - Future Unicode compatibility
"""

"""
Valid Anagram Solutions with Unicode Support
Problem: Determine if two strings are anagrams of each other

Key Insights:
1. Two strings are anagrams if they have the same characters with same frequencies
2. Need to handle:
   - ASCII (lowercase English letters)
   - Unicode (follow-up case)
   - Empty strings
   - Different length strings
   - Case sensitivity (as specified)

1. Sorting Solution
Time: O(n log n)
Space: O(n) or O(1) depending on sorting implementation
"""

class SortingSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Visualization for s="anagram", t="nagaram":
        
        Original:
        s = "anagram"
        t = "nagaram"
        
        Sorted:
        s = "aaagmnr"
        t = "aaagmnr"
        
        Compare: True
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
    def isAnagramUnicode(self, s: str, t: str) -> bool:
        """
        Unicode-aware sorting solution
        Handles full Unicode range including combining characters
        
        Example with Unicode:
        s = "café"      # 'e' with acute accent as single char
        t = "cafe\u0301" # 'e' followed by combining acute accent
        
        Normalize first:
        s = "cafe\u0301"
        t = "cafe\u0301"
        """
        import unicodedata
        
        # Normalize to handle combining characters
        s = unicodedata.normalize('NFC', s)
        t = unicodedata.normalize('NFC', t)
        
        return sorted(s) == sorted(t)

"""
2. Hash Map Solution
Time: O(n)
Space: O(k) where k is size of character set
"""

from collections import Counter

class HashMapSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Visualization for s="anagram", t="nagaram":
        
        Step 1: Count s
        {
            'a': 3,
            'n': 1,
            'g': 1,
            'r': 1,
            'm': 1
        }
        
        Step 2: Subtract t
        'n': 0
        'a': 2 → 1 → 0
        'g': 0
        'a': 0
        'r': 0
        'a': 0
        'm': 0
        
        Step 3: Check all counts are 0
        """
        if len(s) != len(t):
            return False
        
        char_count = Counter(s)
        
        for char in t:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        
        return True
    
    def isAnagramUnicode(self, s: str, t: str) -> bool:
        """
        Unicode-aware hash map solution using code points
        
        Example with Unicode:
        s = "Hello世界"
        t = "界世lloHe"
        
        Counter will automatically handle Unicode code points
        """
        if len(s) != len(t):
            return False
        
        # Normalize strings first
        import unicodedata
        s = unicodedata.normalize('NFC', s)
        t = unicodedata.normalize('NFC', t)
        
        return Counter(s) == Counter(t)

"""
3. Array Solution (for ASCII only)
Time: O(n)
Space: O(1) - fixed size array
"""

class ArraySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Visualization for s="anagram", t="nagaram":
        
        Array indices represent 'a' through 'z'
        Initial array: [0] * 26
        
        After processing 's':
        [3,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0]
         a b c d e f g h i j k l m n o p q r s t u v w x y z
        
        After processing 't':
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        All zeros = anagram
        """
        if len(s) != len(t):
            return False
        
        # Use array for lowercase English letters
        counts = [0] * 26
        
        # Count characters in s
        for char in s:
            counts[ord(char) - ord('a')] += 1
            
        # Subtract characters in t
        for char in t:
            counts[ord(char) - ord('a')] -= 1
            if counts[ord(char) - ord('a')] < 0:
                return False
        
        return all(count == 0 for count in counts)

"""
4. XOR Solution (for ASCII only)
Time: O(n)
Space: O(1)
Note: This only works for single-occurrence characters
"""

class XORSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Only works for strings where each character appears once!
        
        Example: "abc" and "cba"
        XOR all chars:
        result = a^b^c^c^b^a = 0
        """
        if len(s) != len(t):
            return False
            
        result = 0
        for char in s:
            result ^= ord(char)
        for char in t:
            result ^= ord(char)
            
        return result == 0

"""
Unicode Handling Considerations:

1. Normalization Forms:
   - NFC: Canonical composition
   - NFD: Canonical decomposition
   - NFKC: Compatibility composition
   - NFKD: Compatibility decomposition

2. Special Cases:
   - Combining characters: é can be e + ́
   - Width variations: full-width vs. half-width
   - Case folding: different rules per locale
   - Emoji: skin tone modifiers, ZWJ sequences

3. Performance Considerations:
   - Unicode strings take more memory
   - Comparison is more complex
   - Need to handle larger character set

Recommended Solution:

For ASCII (given constraint):
- Use Array Solution
  * O(n) time
  * O(1) space
  * Simple and efficient
  * Perfect for lowercase English letters

For Unicode (follow-up):
- Use Hash Map Solution with normalization
  * Handles full Unicode range
  * Correctly processes combining characters
  * Reasonable space usage
  * More flexible for extensions

Interview Tips:
1. Start with ASCII solution
2. Mention Unicode considerations
3. Discuss trade-offs:
   - Sorting: Simple but slower
   - Hash Map: Fast but more space
   - Array: Perfect for ASCII
   - XOR: Limited use case
4. Optimize based on:
   - Input size
   - Character set
   - Memory constraints
   - Performance requirements
"""