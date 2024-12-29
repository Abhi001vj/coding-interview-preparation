# https://leetcode.com/problems/add-bold-tag-in-string/description/
# 616. Add Bold Tag in String
# Medium
# Topics
# Companies
# You are given a string s and an array of strings words.

# You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words.

# If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.
# If two substrings wrapped by bold tags are consecutive, you should combine them.
# Return s after adding the bold tags.

 

# Example 1:

# Input: s = "abcxyz123", words = ["abc","123"]
# Output: "<b>abc</b>xyz<b>123</b>"
# Explanation: The two strings of words are substrings of s as following: "abcxyz123".
# We add <b> before each substring and </b> after each substring.
# Example 2:

# Input: s = "aaabbb", words = ["aa","b"]
# Output: "<b>aaabbb</b>"
# Explanation: 
# "aa" appears as a substring two times: "aaabbb" and "aaabbb".
# "b" appears as a substring three times: "aaabbb", "aaabbb", and "aaabbb".
# We add <b> before each substring and </b> after each substring: "<b>a<b>a</b>a</b><b>b</b><b>b</b><b>b</b>".
# Since the first two <b>'s overlap, we merge them: "<b>aaa</b><b>b</b><b>b</b><b>b</b>".
# Since now the four <b>'s are consecutive, we merge them: "<b>aaabbb</b>".
 

# Constraints:

# 1 <= s.length <= 1000
# 0 <= words.length <= 100
# 1 <= words[i].length <= 1000
# s and words[i] consist of English letters and digits.
# All the values of words are unique.
 

# Note: This question is the same as 758. Bold Words in String.

"""
Problem: Add Bold Tag in String (LeetCode 616)

Core Challenge:
- We need to identify all substrings from the words array in the main string
- Mark these substrings as bold by adding <b> and </b> tags
- Handle overlapping and consecutive bold regions by merging them
- Return the final string with appropriate bold tags

Key Patterns Identified:
1. String Matching
2. Interval Merging
3. Array/String Manipulation

Let's analyze multiple approaches:

Approach 1: Brute Force with Boolean Array
Time: O(N * K * M) where N = len(s), K = len(words), M = average length of word
Space: O(N) for the boolean array

The idea:
1. Create a boolean array to mark which characters should be bold
2. For each word in words:
   - Find all occurrences in s
   - Mark corresponding positions as True in boolean array
3. Convert boolean array to string with tags

Visual Example:
s = "abcxyz123", words = ["abc","123"]

1. Initial string:
a b c x y z 1 2 3
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
F F F F F F F F F  (boolean array)

2. After marking "abc":
a b c x y z 1 2 3
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
T T T F F F F F F

3. After marking "123":
a b c x y z 1 2 3
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
T T T F F F T T T

4. Final result:
<b>abc</b>xyz<b>123</b>
"""

def addBoldTag_bruteforce(s: str, words: list[str]) -> str:
    # Step 1: Create boolean array to track bold positions
    n = len(s)
    bold = [False] * n
    
    # Step 2: Mark all positions that should be bold
    for word in words:
        word_len = len(word)
        for i in range(n - word_len + 1):
            # If we find the word at position i
            if s[i:i + word_len] == word:
                # Mark all positions of this word as bold
                for j in range(i, i + word_len):
                    bold[j] = True
    
    # Step 3: Build result string with bold tags
    result = []
    i = 0
    while i < n:
        if not bold[i]:
            # If current char shouldn't be bold, add it directly
            result.append(s[i])
            i += 1
        else:
            # Start of bold section
            result.append("<b>")
            # Add all consecutive bold characters
            while i < n and bold[i]:
                result.append(s[i])
                i += 1
            # End bold section
            result.append("</b>")
    
    return "".join(result)

"""
Approach 2: Optimized Solution using Trie + Interval Merging
Time: O(N * M + K) where N = len(s), M = max length of word in words
Space: O(K) for the Trie structure

The idea:
1. Build a Trie from the words array for efficient string matching
2. Use Trie to find all bold intervals
3. Merge overlapping intervals
4. Build final string with bold tags

Visual Example:
s = "aaabbb", words = ["aa","b"]

1. Trie Structure:
    root
     ↓
     a → a
     ↓
     b

2. Found Intervals (start, end):
[0,2]  # First "aa"
[1,3]  # Second "aa"
[3,4]  # First "b"
[4,5]  # Second "b"
[5,6]  # Third "b"

3. After Merging:
[0,6]  # All intervals merged

4. Final Result:
<b>aaabbb</b>
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def find_words_starting_at(self, s: str, start: int) -> list[int]:
        """Returns end positions of all words starting at given position"""
        node = self.root
        result = []
        i = start
        
        while i < len(s) and s[i] in node.children:
            node = node.children[s[i]]
            if node.is_word:
                result.append(i + 1)
            i += 1
        
        return result

def addBoldTag_optimized(s: str, words: list[str]) -> str:
    # Step 1: Build Trie
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    # Step 2: Find all intervals that should be bold
    intervals = []
    for i in range(len(s)):
        end_positions = trie.find_words_starting_at(s, i)
        for end in end_positions:
            intervals.append([i, end])
    
    # Step 3: Merge overlapping intervals
    if not intervals:
        return s
    
    intervals.sort()
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    
    # Step 4: Build result string with bold tags
    result = []
    last_pos = 0
    for start, end in merged:
        # Add any non-bold text before this interval
        result.append(s[last_pos:start])
        # Add the bold text
        result.append("<b>")
        result.append(s[start:end])
        result.append("</b>")
        last_pos = end
    
    # Add any remaining non-bold text
    result.append(s[last_pos:])
    
    return "".join(result)

"""
Space & Time Complexity Analysis:

Brute Force Approach:
Time: O(N * K * M)
- For each position in s (N)
  - For each word in words (K)
    - Compare up to M characters
Space: O(N) for the boolean array

Optimized Trie Approach:
Time: O(N * M + K)
- Building Trie: O(K) where K is total length of all words
- Finding intervals: O(N * M) where M is max word length
  - For each position (N), we might traverse up to M chars in Trie
- Merging intervals: O(N log N) for sorting
Space: O(K) for the Trie structure
- Each character in words array needs a node
- Additional O(N) for the result string

The Trie approach is more efficient when:
1. There are many words with common prefixes
2. Words are long
3. Multiple words might match at each position

Trade-offs:
Brute Force:
+ Simpler to implement
+ Better for small inputs
- Inefficient for large inputs
- Repeated string comparisons

Trie Approach:
+ More efficient for larger inputs
+ Handles common prefixes efficiently
- More complex implementation
- Higher initial space overhead

Example Test Cases:

1. Basic case:
s = "abcxyz123"
words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"

2. Overlapping words:
s = "aaabbb"
words = ["aa","b"]
Output: "<b>aaabbb</b>"

3. No matches:
s = "xyz"
words = ["abc"]
Output: "xyz"

4. Multiple overlapping:
s = "aaabbcc"
words = ["aaa","aab","bc"]
Output: "<b>aaabbc</b>c"
"""

# Test function to verify both implementations
def test_solutions():
    test_cases = [
        {
            "s": "abcxyz123",
            "words": ["abc","123"],
            "expected": "<b>abc</b>xyz<b>123</b>"
        },
        {
            "s": "aaabbb",
            "words": ["aa","b"],
            "expected": "<b>aaabbb</b>"
        },
        {
            "s": "xyz",
            "words": ["abc"],
            "expected": "xyz"
        }
    ]
    
    for i, test in enumerate(test_cases):
        brute_result = addBoldTag_bruteforce(test["s"], test["words"])
        optimized_result = addBoldTag_optimized(test["s"], test["words"])
        
        assert brute_result == test["expected"], f"Brute force failed case {i + 1}"
        assert optimized_result == test["expected"], f"Optimized failed case {i + 1}"
        
    print("All test cases passed!")