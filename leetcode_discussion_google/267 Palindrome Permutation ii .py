# https://leetcode.com/problems/palindrome-permutation-ii/description/
# 267. Palindrome Permutation II
# Medium
# Topics
# Companies
# Hint
# Given a string s, return all the palindromic permutations (without duplicates) of it.

# You may return the answer in any order. If s has no palindromic permutation, return an empty list.

 

# Example 1:

# Input: s = "aabb"
# Output: ["abba","baab"]
# Example 2:

# Input: s = "abc"
# Output: []
 

# Constraints:

# 1 <= s.length <= 16
# s consists of only lowercase English letters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 72.1K
# Submissions
# 171.9K
# Acceptance Rate
# 42.0%
# Topics
# Companies
# Hint 1
# If a palindromic permutation exists, we just need to generate the first half of the string.
# Hint 2
# To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.

"""
Palindrome Permutation II Solutions

Key Insights:
1. Valid palindrome needs at most one character with odd frequency
2. Only need to generate half of the palindrome
3. Can use character frequencies to generate permutations

1. Complete Solution with Backtracking:
"""

from collections import Counter

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        """
        Example visualization for "aabb":
        
        Step 1: Count frequencies
        a: 2
        b: 2
        
        Step 2: Split into half chars
        half_chars = ['a', 'b']  # We'll permute these
        center = ''              # No odd character
        
        Step 3: Generate permutations
        [a,b] -> "ab" + "" + "ba" = "abba"
        [b,a] -> "ba" + "" + "ab" = "baab"
        
        Time Complexity: O(n/2)! for permutations
        Space Complexity: O(n) for storing results
        """
        # Step 1: Count character frequencies
        char_count = Counter(s)
        
        # Step 2: Check if valid palindrome is possible
        odd_chars = [char for char, count in char_count.items() if count % 2]
        if len(odd_chars) > 1:
            return []
            
        # Step 3: Prepare characters for permutation
        center = odd_chars[0] if odd_chars else ''
        half_chars = []
        for char, count in char_count.items():
            half_chars.extend([char] * (count // 2))
            
        # Step 4: Generate permutations
        def backtrack(chars, used, curr):
            if len(curr) == len(chars):
                # Form palindrome: curr + center + curr reversed
                half = ''.join(curr)
                return [half + center + half[::-1]]
                
            result = []
            for i in range(len(chars)):
                # Skip if used or if same as previous unused char
                if used[i] or (i > 0 and chars[i] == chars[i-1] and not used[i-1]):
                    continue
                    
                used[i] = True
                curr.append(chars[i])
                result.extend(backtrack(chars, used, curr))
                curr.pop()
                used[i] = False
            return result
            
        # Sort characters to handle duplicates
        half_chars.sort()
        return backtrack(half_chars, [False] * len(half_chars), [])

"""
2. Iterative Solution using Next Permutation:
"""

class IterativeSolution:
    def generatePalindromes(self, s: str) -> List[str]:
        """
        Uses next permutation concept instead of backtracking.
        
        Example for "aabb":
        1. Get half chars: ['a', 'b']
        2. Generate next permutation until back to original:
           'ab' -> 'ba' -> 'ab' (stop)
        """
        # Count frequencies
        char_count = Counter(s)
        
        # Check palindrome possibility
        center = ''
        odd_count = 0
        for char, count in char_count.items():
            if count % 2:
                center = char
                odd_count += 1
                if odd_count > 1:
                    return []
        
        # Get half characters
        half = []
        for char, count in char_count.items():
            half.extend([char] * (count // 2))
        
        def next_permutation(arr):
            """
            Find next lexicographically greater permutation
            """
            # Find longest non-increasing suffix
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
                
            if i >= 0:
                # Find successor to pivot
                j = len(arr) - 1
                while arr[j] <= arr[i]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                
            # Reverse suffix
            left = i + 1
            right = len(arr) - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
                
            return i >= 0
        
        # Generate all permutations
        result = []
        half.sort()
        first_perm = half.copy()
        
        while True:
            # Form palindrome
            curr = ''.join(half)
            result.append(curr + center + curr[::-1])
            
            if not next_permutation(half):
                break
                
            # Check if we're back to first permutation
            if half == first_perm:
                break
                
        return result

"""
3. Using Python's itertools (Not for interview):
"""

from itertools import permutations

class LibrarySolution:
    def generatePalindromes(self, s: str) -> List[str]:
        # Count frequencies
        char_count = Counter(s)
        
        # Check palindrome possibility
        center = ''
        odd_count = 0
        for char, count in char_count.items():
            if count % 2:
                center = char
                odd_count += 1
                if odd_count > 1:
                    return []
        
        # Get half characters
        half = []
        for char, count in char_count.items():
            half.extend([char] * (count // 2))
        
        # Generate unique permutations
        result = set()
        for p in permutations(half):
            curr = ''.join(p)
            result.add(curr + center + curr[::-1])
            
        return list(result)

"""
Algorithm Analysis:

Time Complexity Breakdown:

1. Backtracking Solution:
   - Character counting: O(n)
   - Generating permutations: O((n/2)!)
   - Total: O(n + (n/2)!)

2. Iterative Solution:
   - Character counting: O(n)
   - Next permutation: O(n)
   - Number of permutations: O((n/2)!)
   - Total: O(n * (n/2)!)

3. Library Solution:
   - Character counting: O(n)
   - Permutations: O((n/2)!)
   - Total: O(n + (n/2)!)

Space Complexity:
- All solutions: O(n) for storing results
- Backtracking: O(n) additional for recursion stack

Visualization of Process:

For input "aabb":

1. Initial State:
   Frequencies: {'a': 2, 'b': 2}
   Half chars: ['a', 'b']
   Center: ""

2. Permutation Tree:
   ```
   root
   ├── a
   │   └── b -> "abba"
   └── b
       └── a -> "baab"
   ```

3. Results Formation:
   ab -> abba
   ba -> baab

Optimization Techniques:

1. Early Validation:
   - Check palindrome possibility first
   - Return empty list early if impossible

2. Duplicate Handling:
   - Sort characters to handle duplicates
   - Skip same characters in backtracking

3. Memory Efficiency:
   - Only store half of palindrome during generation
   - Generate other half on demand

Interview Tips:

1. Start with:
   - Explain palindrome property
   - Show how to validate possibility
   - Describe permutation strategy

2. Optimize by:
   - Using character counting
   - Handling duplicates
   - Generating only half

3. Edge Cases:
   - Empty string
   - Single character
   - All same characters
   - No palindrome possible
   - Odd vs even length

Example Edge Cases:
```python
assert generatePalindromes("") == [""]
assert generatePalindromes("a") == ["a"]
assert generatePalindromes("aaa") == ["aaa"]
assert generatePalindromes("abc") == []
assert generatePalindromes("aaaa") == ["aaaa"]
```
"""
# Initial setup:
char_count = {'a': 2, 'b': 2}
odd_chars = []  # No odd frequency characters
center = ""    # No center character needed
half_chars = ['a', 'b']  # Only one of each! This is key
                        # We take half of each character's count

Let's trace the backtracking with the corrected half_chars:

Stack Trace Level 1 (Starting with 'a'):
backtrack(chars=['a','b'], used=[F,F], curr=[])
    i = 0: Choose 'a'
    used = [T,F]
    curr = ['a']
    |
    ├─── Stack Level 2:
    |    backtrack(chars=['a','b'], used=[T,F], curr=['a'])
    |    i = 1: Choose 'b'
    |    used = [T,T]
    |    curr = ['a','b']
    |    len(curr) == len(chars), so create palindrome:
    |    half = "ab"
    |    Return ["ab" + "" + "ba"] = ["abba"]
    |    
    |    Backtrack: Remove 'b'
    |    curr = ['a']
    |    used = [T,F]
    |
    Backtrack: Remove 'a'
    curr = []
    used = [F,F]

Stack Trace Level 1 (Starting with 'b'):
backtrack(chars=['a','b'], used=[F,F], curr=[])
    i = 1: Choose 'b'
    used = [F,T]
    curr = ['b']
    |
    ├─── Stack Level 2:
    |    backtrack(chars=['a','b'], used=[F,T], curr=['b'])
    |    i = 0: Choose 'a'
    |    used = [T,T]
    |    curr = ['b','a']
    |    len(curr) == len(chars), so create palindrome:
    |    half = "ba"
    |    Return ["ba" + "" + "ab"] = ["baab"]