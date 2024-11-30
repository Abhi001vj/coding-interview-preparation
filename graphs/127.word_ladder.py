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
    
1. Breadth First Search - I
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        n, m = len(wordList), len(wordList[0])
        adj = [[] for _ in range(n)]
        mp = {}
        for i in range(n):
            mp[wordList[i]] = i

        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        cnt += 1
                if cnt == 1:
                    adj[i].append(j)
                    adj[j].append(i)
        
        q, res = deque(), 1
        visit = set()
        for i in range(m):
            for c in range(97, 123):
                if chr(c) == beginWord[i]:
                    continue
                word = beginWord[:i] + chr(c) + beginWord[i + 1:]
                if word in mp and mp[word] not in visit:
                    q.append(mp[word])
                    visit.add(mp[word])
        
        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return res
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            
        return 0
Time & Space Complexity
Time complexity: 
O
(
n
2
∗
m
)
O(n 
2
 ∗m)
Space complexity: 
O
(
n
2
)
O(n 
2
 )
Where 
n
n is the number of words and 
m
m is the length of the word.
2. Breadth First Search - II
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        words, res = set(wordList), 0
        q = deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                for i in range(len(node)):
                    for c in range(97, 123):
                        if chr(c) == node[i]:
                            continue
                        nei = node[:i] + chr(c) + node[i + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        return 0
Time & Space Complexity
Time complexity: 
O
(
m
2
∗
n
)
O(m 
2
 ∗n)
Space complexity: 
O
(
m
2
∗
n
)
O(m 
2
 ∗n)
Where 
n
n is the number of words and 
m
m is the length of the word.
3. Breadth First Search - III
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
Time & Space Complexity
Time complexity: 
O
(
m
2
∗
n
)
O(m 
2
 ∗n)
Space complexity: 
O
(
m
2
∗
n
)
O(m 
2
 ∗n)
Where 
n
n is the number of words and 
m
m is the length of the word.
4. Meet In The Middle (BFS)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        m = len(wordList[0])
        wordSet = set(wordList)
        qb, qe = deque([beginWord]), deque([endWord])
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}
        
        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromBegin, fromEnd = fromEnd, fromBegin
            for _ in range(len(qb)):
                word = qb.popleft()
                steps = fromBegin[word]
                for i in range(m):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        nei = word[:i] + chr(c) + word[i + 1:]
                        if nei not in wordSet:
                            continue
                        if nei in fromEnd:
                            return steps + fromEnd[nei]
                        if nei not in fromBegin:
                            fromBegin[nei] = steps + 1
                            qb.append(nei)
        return 0
Time & Space Complexity
Time complexity: 
O
(
m
2
∗
n
)
O(m 
2
 ∗n)
Space complexity: 
O
(
m
2
∗
n
)
O(m 
2
 ∗n)
Where 
n
n is the number of words and 
m
m is the length of the word.