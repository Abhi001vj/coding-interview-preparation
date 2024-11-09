# https://leetcode.com/problems/word-ladder/description/
# 127. Word Ladder

# Hard
# Topics
# Companies
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # First check if endWord in wordList
        if endWord not in wordList:
            return 0
            
        word_set = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, length = queue.popleft()
            
            # Try changing each position to each letter
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    
                    # CORRECTED: Check if next_word in word_set first!
                    if next_word in word_set:
                        if next_word == endWord:
                            return length + 1
                            
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append((next_word, length + 1))
        
        return 0
    

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        pattern_dict = collections.defaultdict(list)
        word_len = len(beginWord)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_dict[pattern].append(word)

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:

            word, length = queue.popleft()

            for i in range(word_len):
                pattern = word[:i] + "*" + word[i+1:]
                for next_word in pattern_dict[pattern]:
                    if next_word == endWord:
                        return length + 1
                    
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length + 1 ))

                pattern_dict[pattern] = []

        return 0