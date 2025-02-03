# https://leetcode.com/problems/shortest-palindrome/description/
# Code
# Testcase
# Test Result
# Test Result
# 214. Shortest Palindrome
# Hard
# Topics
# Companies
# You are given a string s. You can convert s to a 
# palindrome
#  by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

 

# Example 1:

# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: s = "abcd"
# Output: "dcbabcd"
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only.

"""
Shortest Palindrome Problem Analysis

Key Insight:
We need to find the longest palindrome prefix in the string and only add characters at the front.

1. Brute Force Solution: Check each prefix
Time Complexity: O(n²)
Space Complexity: O(1)
"""

class BruteForceSolution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Find longest palindrome prefix by checking each position.
        
        Example visualization for "aacecaaa":
        
        Step 1: Check each prefix from longest to shortest
        Length 8: "aacecaaa" - not palindrome
        Length 7: "aacecaa" - not palindrome
        Length 6: "aaceca" - not palindrome
        Length 5: "aacec" - not palindrome
        Length 4: "aace" - not palindrome
        Length 3: "aac" - not palindrome
        Length 2: "aa" - is palindrome! ✓
        
        Step 2: Add remaining reversed chars to front
        Original: "aacecaaa"
        Add "aaa" to front
        Result: "aaacecaaa"
        """
        if not s:
            return ""
            
        def is_palindrome(s: str, length: int) -> bool:
            left, right = 0, length - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        # Find longest palindrome prefix
        for i in range(len(s), 0, -1):
            if is_palindrome(s, i):
                # Add reversed remaining characters to front
                return s[i:][::-1] + s

"""
2. KMP (Knuth-Morris-Pratt) Solution
Time Complexity: O(n)
Space Complexity: O(n)

Key Idea: Use KMP pattern matching to find longest palindrome prefix efficiently.
"""

class KMPSolution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Use KMP to find longest palindrome prefix.
        
        Example for "aacecaaa":
        
        Step 1: Create pattern string
        s = "aacecaaa"
        rev = "aaacecaa"
        pattern = "aacecaaa#aaacecaa"
        
        Step 2: Build KMP table
        Pattern:    a a c e c a a a # a a a c e c a a
        Index:      0 1 2 3 4 5 6 7 8 9 10111213141516
        KMP table:  0 1 0 0 0 1 2 3 0 1 2 3 0 0 0 1 2
        
        Step 3: Length of longest palindrome prefix
        = len(s) - KMP table[last]
        = 8 - 2 = 6
        
        Step 4: Add remaining chars reversed
        Add "aaa" to front of "aacecaaa"
        Result: "aaacecaaa"
        """
        if not s:
            return ""
            
        def build_kmp_table(pattern: str) -> List[int]:
            table = [0] * len(pattern)
            i = 1
            length = 0
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    table[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = table[length - 1]
                    else:
                        table[i] = 0
                        i += 1
            return table
        
        # Create pattern string
        pattern = s + "#" + s[::-1]
        
        # Build KMP table
        table = build_kmp_table(pattern)
        
        # Get length of palindrome prefix
        palindrome_length = len(s) - table[-1]
        
        # Add required characters to front
        return s[palindrome_length:][::-1] + s

"""
3. Two Pointers Solution with Rolling Hash
Time Complexity: O(n)
Space Complexity: O(1)
"""

class RollingHashSolution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Use rolling hash to check palindrome prefixes.
        
        Example for "aacecaaa":
        
        Step 1: Initialize rolling hashes
        forward_hash = hash("a") = 1
        reverse_hash = hash("a") = 1
        
        Step 2: Update hashes for each position
        Position 1:
        forward = hash("aa") = 27
        reverse = hash("aa") = 27 ✓
        
        Position 2:
        forward = hash("aac") = 729
        reverse = hash("caa") = 3078 ✗
        
        Found longest palindrome prefix = 2
        
        Step 3: Add remaining chars reversed
        Result: "aaacecaaa"
        """
        if not s:
            return ""
            
        BASE = 26
        MOD = 10**9 + 7
        
        # Find longest palindrome prefix
        forward_hash = 0
        reverse_hash = 0
        longest = 0
        power = 1
        
        for i in range(len(s)):
            forward_hash = (forward_hash * BASE + ord(s[i]) - ord('a')) % MOD
            reverse_hash = (reverse_hash + 
                          (ord(s[i]) - ord('a')) * power) % MOD
            
            if forward_hash == reverse_hash:
                # Verify to avoid hash collisions
                left, right = 0, i
                is_palindrome = True
                while left < right:
                    if s[left] != s[right]:
                        is_palindrome = False
                        break
                    left += 1
                    right -= 1
                if is_palindrome:
                    longest = i + 1
                    
            power = (power * BASE) % MOD
            
        return s[longest:][::-1] + s

"""
Solution Comparison:

1. Brute Force:
   Time: O(n²)
   Space: O(1)
   Pros:
   - Simple to understand
   - No extra space
   Cons:
   - Slow for large strings
   - Redundant comparisons

2. KMP:
   Time: O(n)
   Space: O(n)
   Pros:
   - Linear time complexity
   - No hash collisions
   Cons:
   - Complex implementation
   - Extra space needed

3. Rolling Hash:
   Time: O(n)
   Space: O(1)
   Pros:
   - Linear time
   - Constant space
   Cons:
   - Need to handle collisions
   - May need verification

Interview Tips:

1. Start with problem understanding:
   - Adding chars only at front
   - Need shortest possible addition
   - Must maintain palindrome property

2. Solution progression:
   - Start with brute force
   - Optimize with KMP
   - Discuss rolling hash trade-offs

3. Edge cases:
   - Empty string
   - Single character
   - Already palindrome
   - No palindrome prefix

4. Testing approach:
   - Small examples first
   - Edge cases
   - Large strings
   - Repeated characters

Example Cases:

1. "aacecaaa":
   - Longest palindrome prefix: "aa"
   - Add "aaa" to front
   - Result: "aaacecaaa"

2. "abcd":
   - No palindrome prefix except "a"
   - Add "dcb" to front
   - Result: "dcbabcd"

3. Empty string:
   - Return empty string

4. "a":
   - Already palindrome
   - Return "a"

Time Complexity Derivation:

1. Brute Force:
   - Check each prefix: O(n)
   - Each check takes O(n)
   Total: O(n²)

2. KMP:
   - Build pattern: O(n)
   - Build table: O(n)
   - Single pass: O(n)
   Total: O(n)

3. Rolling Hash:
   - Single pass: O(n)
   - Verification: O(n)
   Total: O(n)
"""