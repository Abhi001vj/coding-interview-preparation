
# Code


# Testcase
# Testcase
# Test Result
# 1048. Longest String Chain
# Attempted
# Medium
# Topics
# Companies
# Hint
# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.

 

# Example 1:

# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
# Example 2:

# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
# Example 3:

# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of lowercase English letters.
# Approach 1: Trie + DFS Solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""

class Solution:
    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word
        return root
    
    def dfs(self, node, curr_length, curr_seq):
        if curr_length > self.max_length:
            self.max_length = curr_length
            self.longest_sequence = curr_seq[:]
        
        # Check all possible next words
        for child_char, child_node in node.children.items():
            if child_node.is_end:
                # Verify it's just one character longer
                if len(child_node.word) == len(node.word) + 1:
                    # Verify it's a prefix match
                    if child_node.word.startswith(node.word):
                        self.dfs(child_node, curr_length + 1, curr_seq + [child_node.word])
    
    def findLongestSequence(self, words):
        # Sort words by length for optimization
        words.sort(key=len)
        root = self.buildTrie(words)
        self.max_length = 0
        self.longest_sequence = []
        
        # Start DFS from each word
        for word in words:
            node = root
            for char in word:
                node = node.children[char]
            self.dfs(node, 1, [word])
            
        return self.longest_sequence

# Approach 2: DP Solution (similar to Longest String Chain)
def longestSequence(words):
    # Sort words by length
    words.sort(key=len)
    dp = {}  # word -> longest chain length ending at this word
    
    max_length = 1
    result = []
    parent = {}  # for reconstructing sequence
    
    for word in words:
        dp[word] = 1
        parent[word] = None
        
        # Try removing each character to find predecessor
        for i in range(len(word)):
            pred = word[:i] + word[i+1:]
            if pred in dp:
                # Check if it's a prefix
                if word.startswith(pred) and len(word) == len(pred) + 1:
                    if dp[pred] + 1 > dp[word]:
                        dp[word] = dp[pred] + 1
                        parent[word] = pred
                        if dp[word] > max_length:
                            max_length = dp[word]
                            result = word
    
    # Reconstruct sequence
    sequence = []
    curr = result
    while curr:
        sequence.append(curr)
        curr = parent[curr]
    
    return sequence[::-1]  # Reverse to get correct order

# Test
words = ["a", "ab", "abc", "abcd", "abcdef", "abcdefg", "abcdefgh", "abcdefghi"]
sol = Solution()
print("Trie+DFS solution:", sol.findLongestSequence(words))
print("DP solution:", longestSequence(words))