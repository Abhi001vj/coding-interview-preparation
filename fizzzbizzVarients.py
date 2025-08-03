from typing import List
from collections import defaultdict, Counter

class AdvancedWordProblems:
    
    def findWordsContainingAll(self, words: List[str], chars: List[str]) -> List[int]:
        """
        Find words containing ALL characters from the given list.
        Time: O(n * m * k) where k is len(chars)
        Space: O(1)
        """
        result = []
        char_set = set(chars)
        
        for i, word in enumerate(words):
            word_chars = set(word)
            if char_set.issubset(word_chars):
                result.append(i)
        
        return result
    
    def findWordsWithCharFrequency(self, words: List[str], x: str, k: int) -> List[int]:
        """
        Find words where character x appears at least k times.
        Time: O(n * m) where m is average word length
        Space: O(1)
        """
        result = []
        
        for i, word in enumerate(words):
            if word.count(x) >= k:
                result.append(i)
        
        return result
    
    def findWordsContainingSubsequence(self, words: List[str], subseq: str) -> List[int]:
        """
        Find words containing the given subsequence.
        Time: O(n * m * s) where s is len(subseq)
        Space: O(1)
        """
        def contains_subsequence(word: str, subseq: str) -> bool:
            i = j = 0
            while i < len(word) and j < len(subseq):
                if word[i] == subseq[j]:
                    j += 1
                i += 1
            return j == len(subseq)
        
        result = []
        for i, word in enumerate(words):
            if contains_subsequence(word, subseq):
                result.append(i)
        
        return result
    
    def findWordsContainingPattern(self, words: List[str], pattern: str) -> List[int]:
        """
        Find words matching a pattern where '.' matches any character.
        Example: pattern "a.c" matches "abc", "axc", etc.
        Time: O(n * m)
        Space: O(1)
        """
        def matches_pattern(word: str, pattern: str) -> bool:
            if len(word) != len(pattern):
                return False
            
            for i in range(len(word)):
                if pattern[i] != '.' and pattern[i] != word[i]:
                    return False
            return True
        
        result = []
        for i, word in enumerate(words):
            if matches_pattern(word, pattern):
                result.append(i)
        
        return result
    
    def findWordsContainingSubstring(self, words: List[str], substring: str) -> List[int]:
        """
        Find words containing the exact substring.
        Time: O(n * m) using built-in string search
        Space: O(1)
        """
        result = []
        for i, word in enumerate(words):
            if substring in word:
                result.append(i)
        return result
    
    def findWordsWithEditDistance(self, words: List[str], target: str, max_dist: int) -> List[int]:
        """
        Find words within max_dist edit distance from target.
        Time: O(n * m * t) where t is len(target)
        Space: O(m * t)
        """
        def edit_distance(word1: str, word2: str) -> int:
            m, n = len(word1), len(word2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            
            for i in range(m + 1):
                dp[i][0] = i
            for j in range(n + 1):
                dp[0][j] = j
            
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            
            return dp[m][n]
        
        result = []
        for i, word in enumerate(words):
            if edit_distance(word, target) <= max_dist:
                result.append(i)
        
        return result

class MultiQueryWordSearch:
    """
    Efficient solution for multiple character containment queries.
    Preprocessing: O(n * m) where n is number of words, m is average word length
    Query time: O(1) per query
    """
    
    def __init__(self, words: List[str]):
        self.words = words
        # Build inverted index: char -> list of word indices containing that char
        self.char_to_indices = defaultdict(list)
        
        for i, word in enumerate(words):
            unique_chars = set(word)
            for char in unique_chars:
                self.char_to_indices[char].append(i)
    
    def findWordsContaining(self, x: str) -> List[int]:
        """Query time: O(1)"""
        return self.char_to_indices[x][:]  # Return copy
    
    def findWordsContainingAny(self, chars: List[str]) -> List[int]:
        """Find words containing ANY of the given characters"""
        result_set = set()
        for char in chars:
            result_set.update(self.char_to_indices[char])
        return sorted(list(result_set))
    
    def findWordsContainingAll(self, chars: List[str]) -> List[int]:
        """Find words containing ALL of the given characters"""
        if not chars:
            return []
        
        # Start with indices for first character
        result_set = set(self.char_to_indices[chars[0]])
        
        # Intersect with indices for each subsequent character
        for char in chars[1:]:
            result_set &= set(self.char_to_indices[char])
        
        return sorted(list(result_set))

class TrieWordSearch:
    """
    Trie-based solution for prefix and suffix matching.
    """
    
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word_indices = []  # Store indices of words ending here
    
    def __init__(self, words: List[str]):
        self.words = words
        self.prefix_trie = self.TrieNode()
        self.suffix_trie = self.TrieNode()
        
        # Build prefix trie
        for i, word in enumerate(words):
            node = self.prefix_trie
            for char in word:
                if char not in node.children:
                    node.children[char] = self.TrieNode()
                node = node.children[char]
                node.word_indices.append(i)
        
        # Build suffix trie (reverse words)
        for i, word in enumerate(words):
            node = self.suffix_trie
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = self.TrieNode()
                node = node.children[char]
                node.word_indices.append(i)
    
    def findWordsWithPrefix(self, prefix: str) -> List[int]:
        """Find words starting with the given prefix"""
        node = self.prefix_trie
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all word indices from this subtree
        result = set()
        stack = [node]
        while stack:
            current = stack.pop()
            # Only add indices of words that actually end at or after this prefix
            for idx in current.word_indices:
                if len(self.words[idx]) >= len(prefix):
                    result.add(idx)
            stack.extend(current.children.values())
        
        return sorted(list(result))
    
    def findWordsWithSuffix(self, suffix: str) -> List[int]:
        """Find words ending with the given suffix"""
        node = self.suffix_trie
        for char in reversed(suffix):
            if char not in node.children:
                return []
            node = node.children[char]
        
        result = set()
        stack = [node]
        while stack:
            current = stack.pop()
            for idx in current.word_indices:
                if len(self.words[idx]) >= len(suffix):
                    result.add(idx)
            stack.extend(current.children.values())
        
        return sorted(list(result))

# Example usage and test cases
if __name__ == "__main__":
    words = ["leet", "code", "leetcode", "programming", "algorithm"]
    
    # Test advanced problems
    solver = AdvancedWordProblems()
    
    # Test 1: Words containing all characters
    print("Words containing all ['e', 't']:", solver.findWordsContainingAll(words, ['e', 't']))
    
    # Test 2: Words with character frequency
    print("Words with 'e' appearing at least 2 times:", solver.findWordsWithCharFrequency(words, 'e', 2))
    
    # Test 3: Words containing subsequence
    print("Words containing subsequence 'eet':", solver.findWordsContainingSubsequence(words, 'eet'))
    
    # Test 4: Multi-query search
    multi_search = MultiQueryWordSearch(words)
    print("Multi-query - words containing 'e':", multi_search.findWordsContaining('e'))
    print("Multi-query - words containing any of ['a', 'o']:", multi_search.findWordsContainingAny(['a', 'o']))
    
    # Test 5: Trie-based search
    trie_search = TrieWordSearch(words)
    print("Words with prefix 'lee':", trie_search.findWordsWithPrefix('lee'))
    print("Words with suffix 'ing':", trie_search.findWordsWithSuffix('ing'))