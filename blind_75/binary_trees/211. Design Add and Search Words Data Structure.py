
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# Testcase
# Test Result
# Test Result
# 211. Design Add and Search Words Data Structure
# Medium
# Topics
# Companies
# Hint
# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

class WordDictionary:

    def __init__(self):
        

    def addWord(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode mapping
        self.is_end = False

class WordDictionary:
    def __init__(self):
        """
        Initialize with root node
        Visual: root[]
        """
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        """
        Add word to trie, similar to basic trie
        Example: 'bad'
        root[] -> b[] -> a[] -> d[✓]
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        """
        DFS search with dot pattern matching
        Example: '.ad'
        Need to check: bad, dad, mad, etc.
        """
        def dfs(node: TrieNode, i: int) -> bool:
            # Base case: reached end of word
            if i == len(word):
                return node.is_end
            
            char = word[i]
            if char == '.':
                # Try all possible characters at this position
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # Normal trie search
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
        
        return dfs(self.root, 0)
```

Now, let's optimize it:


```python
class TrieNode:
    __slots__ = ['children', 'is_end']
    
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        """
        Initialize with:
        1. Root node
        2. Length-based word mapping for quick filtering
        Visual: 
        root[]
        words_by_length = {
            3: {'bad', 'dad', 'mad'},
            4: {'test', 'best'},
            ...
        }
        """
        self.root = TrieNode()
        self.words_by_length = {}  # Length -> Set of words
    
    def addWord(self, word: str) -> None:
        """
        1. Add to trie
        2. Store in length mapping
        """
        # Add to length-based lookup
        length = len(word)
        if length not in self.words_by_length:
            self.words_by_length[length] = set()
        self.words_by_length[length].add(word)
        
        # Add to trie
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True
    
    def search(self, word: str) -> bool:
        """
        Optimized search:
        1. Quick length check
        2. Handle no-dot case efficiently
        3. Use DFS for dot patterns
        """
        length = len(word)
        
        # Length optimization
        if length not in self.words_by_length:
            return False
            
        # Optimization for words without dots
        if '.' not in word:
            return word in self.words_by_length[length]
            
        def dfs(node: TrieNode, i: int) -> bool:
            if i == length:
                return node.is_end
                
            char = word[i]
            if char == '.':
                # Count dots for early termination
                dot_count = 1
                while i + dot_count < length and word[i + dot_count] == '.':
                    dot_count += 1
                    
                # If all remaining chars are dots
                if i + dot_count == length:
                    # Check if any path reaches end
                    def check_end(n: TrieNode, depth: int) -> bool:
                        if depth == dot_count:
                            return n.is_end
                        return any(check_end(child, depth + 1) 
                                 for child in n.children.values())
                    return check_end(node, 1)
                
                # Normal dot handling
                return any(dfs(child, i + 1) for child in node.children.values())
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
                
        return dfs(self.root, 0)
```

Key optimizations:
1. Length-based filtering
2. Fast path for no-dot words
3. Multiple dot optimization
4. Memory optimization with __slots__
5. Early termination checks

Time complexity:
- addWord: O(n) where n is word length
- search: 
  - Best case O(1) for no-dot exact match
  - Worst case O(26^m) for all dots, where m is word length
  - Average case much better due to optimizations

Want me to detail any specific optimization?