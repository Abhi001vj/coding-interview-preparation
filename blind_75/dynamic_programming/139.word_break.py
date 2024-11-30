# https://leetcode.com/problems/word-break/description/
# 139. Word Break
# Solved
# Medium
# Topics
# Companies
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

1. Recursion
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(i):
            if i == len(s):
                return True
            
            for w in wordDict:
                if ((i + len(w)) <= len(s) and 
                     s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        return True
            return False
        
        return dfs(0)
Time & Space Complexity
Time complexity: 
O
(
t
∗
m
n
)
O(t∗m 
n
 )
Space complexity: 
O
(
n
)
O(n)
Where 
n
n is the length of the string 
s
s, 
m
m is the number of words in 
w
o
r
d
D
i
c
t
wordDict and 
t
t is the maximum length of any word in 
w
o
r
d
D
i
c
t
wordDict.
2. Recursion (Hash Set)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True
            
            for j in range(i, len(s)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        return True
            return False
        
        return dfs(0)
Time & Space Complexity
Time complexity: 
O
(
(
n
∗
2
n
)
+
m
)
O((n∗2 
n
 )+m)
Space complexity: 
O
(
n
+
(
m
∗
t
)
)
O(n+(m∗t))
Where 
n
n is the length of the string 
s
s and 
m
m is the number of words in 
w
o
r
d
D
i
c
t
wordDict.
3. Dynamic Programming (Top-Down)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if ((i + len(w)) <= len(s) and 
                     s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)
Time & Space Complexity
Time complexity: 
O
(
n
∗
m
∗
t
)
O(n∗m∗t)
Space complexity: 
O
(
n
)
O(n)
Where 
n
n is the length of the string 
s
s, 
m
m is the number of words in 
w
o
r
d
D
i
c
t
wordDict and 
t
t is the maximum length of any word in 
w
o
r
d
D
i
c
t
wordDict.
4. Dynamic Programming (Hash Set)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = 0
        for w in wordDict:
            t = max(t, len(w))

        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            for j in range(i, min(len(s), i + t)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)
Time & Space Complexity
Time complexity: 
O
(
(
t
2
∗
n
)
+
m
)
O((t 
2
 ∗n)+m)
Space complexity: 
O
(
n
+
(
m
∗
t
)
)
O(n+(m∗t))
Where 
n
n is the length of the string 
s
s, 
m
m is the number of words in 
w
o
r
d
D
i
c
t
wordDict and 
t
t is the maximum length of any word in 
w
o
r
d
D
i
c
t
wordDict.
5. Dynamic Programming (Bottom-Up)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
Time & Space Complexity
Time complexity: 
O
(
n
∗
m
∗
t
)
O(n∗m∗t)
Space complexity: 
O
(
n
)
O(n)
Where 
n
n is the length of the string 
s
s, 
m
m is the number of words in 
w
o
r
d
D
i
c
t
wordDict and 
t
t is the maximum length of any word in 
w
o
r
d
D
i
c
t
wordDict.
6. Dynamic Programming (Trie)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, s, i, j):
        node = self.root
        for idx in range(i, j + 1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        return node.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        t = 0
        for w in wordDict:
            t = max(t, len(w))
        
        for i in range(len(s), -1, -1):
            for j in range(i, min(len(s), i + t)):
                if trie.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break

        return dp[0]
Time & Space Complexity
Time complexity: 
O
(
(
n
∗
t
2
)
+
m
)
O((n∗t 
2
 )+m)
Space complexity: 
O
(
n
+
(
m
∗
t
)
)
O(n+(m∗t))
Where 
n
n is the length of the string 
s
s, 
m
m is the number of words in 
w
o
r
d
D
i
c
t
wordDict and 
t
t is the maximum length of any word in 
w
o
r
d
D
i
c
t
wordDict.