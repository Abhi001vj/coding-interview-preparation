# https://leetcode.com/problems/longest-common-subsequence/description/
# 1143. Longest Common Subsequence
# Medium
# Topics
# Companies
# Hint
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

"""
Let's analyze with example: text1 = "abcde", text2 = "ace"

Visual representation of how LCS works:
text1: a b c d e
text2: a   c   e
LCS:  a   c   e  (length = 3)

1. Recursive Solution (Brute Force)
---------------------------------
Base idea: For each character, we have two choices:
1. If current characters match: include and move both pointers
2. If they don't: try skipping character from either string

Visualization of recursive calls for "abcde" and "ace":
                    (0,0)a-a
                      |
                    (1,1)b-c
                   /        \
            (2,1)c-c      (1,2)b-e
               |    \        /    \
        (3,2)d-e  (2,2)c-e ...   ...

Decision tree shows exponential growth of recursive calls.

def lcs_recursive(text1: str, text2: str) -> int:
    def dfs(i, j):
        # Base case: if either string is exhausted
        if i == len(text1) or j == len(text2):
            return 0
            
        # If characters match, include them
        if text1[i] == text2[j]:
            return 1 + dfs(i + 1, j + 1)
            
        # Try skipping character from either string
        return max(dfs(i + 1, j), dfs(i, j + 1))
        
    return dfs(0, 0)

2. Memoization (Top-Down DP)
---------------------------
Improvement: Cache repeated subproblems

For "abcde" and "ace", memo table gradually fills:
   a  c  e
a  3  2  1
b  2  2  1
c  2  2  1
d  1  1  1
e  1  1  1

def lcs_memo(text1: str, text2: str) -> int:
    memo = {}
    
    def dfs(i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
            
        if text1[i] == text2[j]:
            memo[(i, j)] = 1 + dfs(i + 1, j + 1)
        else:
            memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            
        return memo[(i, j)]
        
    return dfs(0, 0)

3. Bottom-Up DP
--------------
Build solution iteratively from smaller subproblems.

For "abcde" and "ace", dp table fills like:
     a  c  e
  0  0  0  0
e 0  0  0  1
d 0  0  0  1
c 0  0  1  1
b 0  0  1  1
a 0  1  1  1
Final answer: dp[0][0] = 3

def lcs_bottomup(text1: str, text2: str) -> int:
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
    return dp[0][0]

4. Space-Optimized DP
--------------------
Key insight: We only need previous row to calculate current row

For "abcde" and "ace", using two rows:
Previous: [0, 0, 0, 0]
Current:  [0, 0, 0, 0]

After processing 'e':
Previous: [0, 0, 0, 1]
Current:  [0, 0, 0, 0]

After processing 'd':
Previous: [0, 0, 0, 1]
Current:  [0, 0, 0, 1]

And so on...

def lcs_optimized(text1: str, text2: str) -> int:
    # Use shorter string for second array to minimize space
    if len(text1) < len(text2):
        text1, text2 = text2, text1
        
    prev = [0] * (len(text2) + 1)
    curr = [0] * (len(text2) + 1)
    
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                curr[j] = 1 + prev[j + 1]
            else:
                curr[j] = max(curr[j + 1], prev[j])
        prev, curr = curr, prev
        
    return prev[0]

5. Most Optimal (Single Array)
----------------------------
Further optimization: Use single array with temp variable

For "abcde" and "ace":
Initial: [0, 0, 0, 0]
After 'e': [0, 0, 0, 1]
After 'd': [0, 0, 0, 1]
After 'c': [0, 0, 1, 1]
After 'b': [0, 0, 1, 1]
After 'a': [1, 1, 1, 1]

def lcs_most_optimal(text1: str, text2: str) -> int:
    if len(text1) < len(text2):
        text1, text2 = text2, text1
        
    dp = [0] * (len(text2) + 1)
    
    for i in range(len(text1) - 1, -1, -1):
        prev = 0  # represents dp[i+1][j+1] from 2D version
        for j in range(len(text2) - 1, -1, -1):
            temp = dp[j]  # save current before updating
            if text1[i] == text2[j]:
                dp[j] = 1 + prev
            else:
                dp[j] = max(dp[j], dp[j + 1])
            prev = temp  # update prev for next iteration
            
    return dp[0]
"""
"""
Example: text1 = "abcde", text2 = "ace"

1. Memoization (Top-Down) Table Filling
-------------------------------------
Each cell (i,j) represents: length of LCS starting from position i in text1 and j in text2

Step by step memo filling (- means not calculated yet):

Initial:
      a  c  e
  a   -  -  -
  b   -  -  -
  c   -  -  -
  d   -  -  -
  e   -  -  -

After base cases (last row and column):
      a  c  e
  a   -  -  -
  b   -  -  -
  c   -  -  -
  d   -  -  1
  e   1  1  1

Filling continues (showing key steps):
      a  c  e
  a   -  -  1  <- e matched
  b   -  2  1
  c   2  2  1
  d   1  1  1
  e   1  1  1

Final memo table:
      a  c  e
  a   3  2  1
  b   2  2  1
  c   2  2  1
  d   1  1  1
  e   1  1  1

2. Bottom-Up Table Filling
------------------------
Each cell (i,j) represents: length of LCS for text1[i:] and text2[j:]
We include extra row/column for base cases.

Initial state:
      a  c  e  $
  a   0  0  0  0
  b   0  0  0  0
  c   0  0  0  0
  d   0  0  0  0
  e   0  0  0  0
  $   0  0  0  0

Step 1 (starting from bottom-right):
      a  c  e  $
  a   0  0  0  0
  b   0  0  0  0
  c   0  0  0  0
  d   0  0  0  0
  e   0  0  1  0
  $   0  0  0  0

Step 2:
      a  c  e  $
  a   0  0  0  0
  b   0  0  0  0
  c   0  0  0  0
  d   0  0  1  0
  e   0  0  1  0
  $   0  0  0  0

Step 3:
      a  c  e  $
  a   0  0  0  0
  b   0  0  0  0
  c   0  1  1  0
  d   0  1  1  0
  e   0  1  1  0
  $   0  0  0  0

Step 4:
      a  c  e  $
  a   0  0  0  0
  b   0  1  1  0
  c   0  1  1  0
  d   0  1  1  0
  e   0  1  1  0
  $   0  0  0  0

Final table:
      a  c  e  $
  a   3  2  1  0
  b   2  2  1  0
  c   2  2  1  0
  d   1  1  1  0
  e   1  1  1  0
  $   0  0  0  0

3. Space-Optimized (Two Rows)
---------------------------
We only keep track of two rows at a time:

Initial:
prev: [0, 0, 0, 0]
curr: [0, 0, 0, 0]

After processing 'e':
prev: [0, 0, 1, 0]
curr: [0, 0, 0, 0]

After processing 'd':
prev: [0, 0, 1, 0]
curr: [0, 0, 1, 0]

After processing 'c':
prev: [0, 1, 1, 0]
curr: [0, 0, 1, 0]

After processing 'b':
prev: [0, 1, 1, 0]
curr: [0, 1, 1, 0]

After processing 'a':
prev: [3, 2, 1, 0]
curr: [0, 1, 1, 0]

4. Most Optimal (Single Array)
---------------------------
Using a single array with temp variable:

Initial:
dp: [0, 0, 0, 0]

After processing 'e':
dp: [0, 0, 1, 0]

After processing 'd':
dp: [0, 0, 1, 0]

After processing 'c':
dp: [0, 1, 1, 0]

After processing 'b':
dp: [0, 1, 1, 0]

After processing 'a':
dp: [3, 2, 1, 0]

Value Calculation Rules for all approaches:
1. If text1[i] == text2[j]:
   cell = 1 + diagonal value
2. If text1[i] != text2[j]:
   cell = max(right value, below value)
"""