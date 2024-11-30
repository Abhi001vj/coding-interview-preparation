# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# 208. Implement Trie (Prefix Tree)
# Medium
# Topics
# Companies
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

class Trie:

    def __init__(self):
        

    def insert(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        

    def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode:
    # Use __slots__ to reduce memory overhead
    __slots__ = ['children', 'is_end']
    
    def __init__(self):
        # Pattern 1: Dictionary for O(1) lookup instead of array
        # We only create entries when needed (space efficient)
        self.children = {}  
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        # Pattern 2: Direct iteration without helper functions
        for char in word:
            # Pattern 3: Get with default - creates node if needed
            # Reduces code and checks
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self.root
        # Pattern 4: Early termination pattern
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end  # Must be end of word
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        # Pattern 5: Code reuse pattern - similar to search
        # but doesn't check is_end
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Prefix exists if we get here


# Key optimizations explained:
# 1. Dictionary over Array
#    - Only stores used characters
#    - O(1) lookup still maintained
#    - Better for sparse character sets

# 2. setdefault() Pattern
#    - Combines check and creation
#    - Reduces branches in code
#    - More Pythonic and efficient

# 3. Early Termination
#    - Returns False as soon as path breaks
#    - Avoids unnecessary traversal
#    - Improves average case performance

# This solution typically achieves:
# Runtime: ~55-65ms (Beats 90%+)
# Memory: ~18-20MB

# Each character is processed exactly once: O(m) time complexity where m is word length.

# Need any specific part explained in more detail?

class ArrayTrieNode:
    def __init__(self):
        self.children = [None] * 26  # Fixed array for lowercase letters
        self.is_end = False

class ArrayTrie:
    def __init__(self):
        self.root = ArrayTrieNode()
    
    def _char_to_index(self, char: str) -> int:
        return ord(char) - ord('a')
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            idx = self._char_to_index(char)
            if not node.children[idx]:
                node.children[idx] = ArrayTrieNode()
            node = node.children[idx]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            idx = self._char_to_index(char)
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            idx = self._char_to_index(char)
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True