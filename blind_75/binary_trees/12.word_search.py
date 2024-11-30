https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Code
# Testcase
# Test Result
# Test Result
# 212. Word Search II
# Hard
# Topics
# Companies
# Hint
# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:


# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:


# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

class TrieNode:
    __slots__ = ['children', 'is_end']
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.words_by_length = {} 

        

    def addWord(self, word: str) -> None:
        length = len(word)
        if length not in self.words_by_length:
            self.words_by_length[length] = set()
        self.words_by_length[length].add(word)

        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        
        node.is_end = True


    def search(self, word: str) -> bool:
        length = len(word)
        
        if length not in self.words_by_length:
            return False
            
        if '.' not in word:
            return word in self.words_by_length[length]

        def dfs(node, i):
            if i ==len(word):
                return node.is_end
            
            char = word[i]
            if char == '.':
                dot_count = 1
                while i + dot_count < length and word[i + dot_count] == '.':
                    dot_count += 1
                if i + dot_count == length:
                    def check_end(n: TrieNode, depth: int) -> bool:
                        if depth == dot_count:
                            return n.is_end
                        return any(check_end(child, depth + 1) 
                                 for child in n.children.values())
                    return check_end(node, 1)
                return any(dfs(child, i + 1) for child in node.children.values())
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
            
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)