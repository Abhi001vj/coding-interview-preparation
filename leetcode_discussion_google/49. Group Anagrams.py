
# https://leetcode.com/problems/group-anagrams/description/
# Code


# Testcase
# Test Result
# Test Result
# 49. Group Anagrams
# Solved
# Medium
# Topics
# Companies
# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = collections.defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())        
    
    """
Group Anagrams Solutions and Analysis

1. Sorting Solution (Your Current Approach):
Time Complexity: O(N * K * log K) where N = number of strings, K = max string length
Space Complexity: O(N * K) for storing all strings
"""

from collections import defaultdict

class SortingSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Visualization for ["eat","tea","tan","ate","nat","bat"]:
        
        Step 1: Sort each string
        "eat" -> "aet" ----┐
        "tea" -> "aet" ----┼--> ["eat","tea","ate"]
        "ate" -> "aet" ----┘
        "tan" -> "ant" ----┐
        "nat" -> "ant" ----┘--> ["tan","nat"]
        "bat" -> "abt" ---------> ["bat"]
        
        Map state:
        {
            "aet": ["eat", "tea", "ate"],
            "ant": ["tan", "nat"],
            "abt": ["bat"]
        }
        """
        groups = defaultdict(list)
        
        for s in strs:
            # Create sorted key
            key = ''.join(sorted(s))
            # Group strings by sorted form
            groups[key].append(s)
            
        return list(groups.values())

"""
2. Character Count Solution:
Time Complexity: O(N * K) where N = number of strings, K = max string length
Space Complexity: O(N * K)
"""

class CountingSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Uses character count as key instead of sorting.
        
        Example for "eat":
        Count array: [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
                     a b c d e f g h i j k l m n o p q r s t u v w x y z
        
        Key format: "#1#0#0#0#1#0...#1#0" (counts separated by #)
        """
        groups = defaultdict(list)
        
        for s in strs:
            # Initialize count array
            count = [0] * 26
            
            # Count characters
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Create key from count array
            key = '#'.join(map(str, count))
            groups[key].append(s)
            
        return list(groups.values())

"""
3. Prime Product Solution:
Time Complexity: O(N * K)
Space Complexity: O(N * K)
Uses unique prime number for each character
"""

class PrimeSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Assign prime number to each character:
        a->2, b->3, c->5, d->7, e->11, ...
        
        Example:
        "eat" = 2 * 11 * 19 = 418
        "tea" = 19 * 11 * 2 = 418
        
        Same product = anagram!
        """
        # First 26 prime numbers for 26 letters
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 
                 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 
                 79, 83, 89, 97, 101]
        
        groups = defaultdict(list)
        
        for s in strs:
            # Calculate product of prime numbers
            key = 1
            for c in s:
                key *= primes[ord(c) - ord('a')]
            groups[key].append(s)
            
        return list(groups.values())

"""
4. Multi-prime Solution (Handles Duplicates Better):
Time Complexity: O(N * K)
Space Complexity: O(N * K)
"""

class MultiPrimeSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use prime powers to handle duplicates:
        "aab" = 2^2 * 3 (not 2 * 2 * 3)
        
        Example:
        "eat" = 2^1 * 11^1 * 19^1
        "eeat" = 2^1 * 11^2 * 19^1
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 
                 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 
                 79, 83, 89, 97, 101]
                 
        groups = defaultdict(list)
        
        for s in strs:
            # Initialize count array
            count = [0] * 26
            
            # Count characters
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Calculate product using prime powers
            key = 1
            for i in range(26):
                if count[i] > 0:
                    key *= primes[i] ** count[i]
                    
            groups[key].append(s)
            
        return list(groups.values())

"""
Comparison of Solutions:

1. Sorting Solution:
   Pros:
   + Simple to understand and implement
   + Works with any character set
   + Easy to modify for case sensitivity
   Cons:
   - O(N * K * log K) time complexity
   - Not optimal for short strings
   
2. Character Count Solution:
   Pros:
   + Better time complexity O(N * K)
   + No sorting required
   + Easy to modify for different constraints
   Cons:
   - Larger key size
   - String concatenation overhead
   
3. Prime Product Solution:
   Pros:
   + Elegant mathematical approach
   + Compact key
   + O(N * K) time complexity
   Cons:
   - Risk of integer overflow
   - Limited by max integer size
   - Only works for small strings
   
4. Multi-prime Solution:
   Pros:
   + Handles duplicates well
   + O(N * K) time complexity
   + Mathematical elegance
   Cons:
   - Complex implementation
   - Risk of overflow for long strings
   
Big O Analysis:

Let N = number of strings
Let K = maximum string length

1. Sorting Solution:
   Time: O(N * K * log K)
   - N strings
   - Each string sorting: O(K * log K)
   Space: O(N * K)
   - Storing N strings
   - Each string length K
   
2. Character Count Solution:
   Time: O(N * K)
   - N strings
   - Each string counting: O(K)
   Space: O(N * K)
   - Hash map with N entries
   - Each key/value: O(K)
   
3. Prime/Multi-prime Solutions:
   Time: O(N * K)
   - N strings
   - Each string processing: O(K)
   Space: O(N * K)
   - Hash map storage
   
Recommended Solution:
For interviews, use Character Count Solution because:
1. Optimal time complexity O(N * K)
2. No risk of overflow
3. Easy to explain and implement
4. Flexible for modifications

For production:
1. Small strings: Sorting Solution
2. Memory constraints: Prime Solution
3. Large strings: Character Count Solution
"""