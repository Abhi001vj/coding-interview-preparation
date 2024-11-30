
# https://leetcode.com/problems/valid-anagram/description/
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
# Solution 1: Sorting Approach
def isAnagram_sort(s: str, t: str) -> bool:
    """
    Time: O(n log n) for sorting
    Space: O(n) for sorting in Python (TimSort)
    
    Pros: Simple, handles Unicode
    Cons: Not optimal time complexity
    """
    return sorted(s) == sorted(t)

# Solution 2: Character Count with HashMap
def isAnagram_hashmap(s: str, t: str) -> bool:
    """
    Time: O(n)
    Space: O(k) where k is unique characters
    
    Pros: Optimal time, handles Unicode
    Cons: Extra space
    """
    if len(s) != len(t):
        return False
        
    char_count = {}
    
    # Count characters in s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    # Decrement for t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
            
    return len(char_count) == 0

# Solution 3: Array for ASCII (Optimized for given constraints)
def isAnagram_array(s: str, t: str) -> bool:
    """
    Time: O(n)
    Space: O(1) - fixed size array
    
    Pros: Most efficient for ASCII
    Cons: Limited to lowercase English letters
    """
    if len(s) != len(t):
        return False
        
    # Array for lowercase letters
    counts = [0] * 26
    
    # Single pass counting both strings
    for i in range(len(s)):
        counts[ord(s[i]) - ord('a')] += 1
        counts[ord(t[i]) - ord('a')] -= 1
    
    # Check if all counts are 0
    return all(count == 0 for count in counts)

# Solution 4: Sum and Product Check (for discussion of why it's problematic)
def isAnagram_math(s: str, t: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    
    NOTE: This is for discussion only - has issues with:
    1. Integer overflow
    2. Hash collisions
    """
    if len(s) != len(t):
        return False
        
    # Using prime numbers to minimize collisions
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
              
    sum_s = sum(primes[ord(c) - ord('a')] for c in s)
    sum_t = sum(primes[ord(c) - ord('a')] for c in t)
    
    return sum_s == sum_t

# Testing and Visualization
def test_anagram_solutions():
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("aa", "bb", False),
        ("aacc", "ccac", False)
    ]
    
    for s, t, expected in test_cases:
        print(f"\nTesting s='{s}', t='{t}'")
        print("="*50)
        
        # Test each solution
        results = {
            "Sorting": isAnagram_sort(s, t),
            "HashMap": isAnagram_hashmap(s, t),
            "Array": isAnagram_array(s, t),
            "Math": isAnagram_math(s, t)
        }
        
        # Print character frequencies for visualization
        print("Character frequencies:")
        freq_s = {}
        freq_t = {}
        for c in s: freq_s[c] = freq_s.get(c, 0) + 1
        for c in t: freq_t[c] = freq_t.get(c, 0) + 1
        print(f"s: {freq_s}")
        print(f"t: {freq_t}")
        
        # Print results
        for method, result in results.items():
            print(f"{method}: {result}")
            assert result == expected, f"{method} failed!"

# Run tests
test_anagram_solutions()