# https://leetcode.com/problems/distinct-subsequences/description/
# 115. Distinct Subsequences
# Hard
# Topics
# Companies
# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

 

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
 

# Constraints:

# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.

# Problem: Distinct Subsequences
# Pattern: Dynamic Programming (String matching with subsequences)
# Time Complexity: O(m*n) where m = len(s), n = len(t)
# Space Complexity: O(m*n)

def numDistinct(s: str, t: str) -> int:
    """
    Calculate the number of distinct subsequences of s that equal t.
    
    Visualization for s = "rabbbit", t = "rabbit":
    
    dp table visualization:
        ''  r  a  b  b  i  t
    ''   1  1  1  1  1  1  1
    r    0  1  1  1  1  1  1
    a    0  0  1  1  1  1  1
    b    0  0  0  1  2  2  2
    b    0  0  0  0  1  1  1
    b    0  0  0  0  0  0  0
    i    0  0  0  0  0  1  1
    t    0  0  0  0  0  0  3
    
    Key insights:
    1. If characters match, we can either:
       - Use current char: dp[i-1][j-1]
       - Skip current char: dp[i][j-1]
    2. If characters don't match:
       - Only option is to skip: dp[i][j-1]
    """
    m, n = len(s), len(t)
    
    # Create DP table with padding
    # dp[i][j] represents number of ways to form t[:i] from s[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Empty string is a subsequence of any string once
    for j in range(m + 1):
        dp[0][j] = 1
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters match, we can either use or skip current char
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            # If characters don't match, can only skip current char
            else:
                dp[i][j] = dp[i][j-1]
    
    return dp[n][m]

# Test cases
def test_numDistinct():
    """
    Test cases to verify the solution
    """
    assert numDistinct("rabbbit", "rabbit") == 3, "Test case 1 failed"
    assert numDistinct("babgbag", "bag") == 5, "Test case 2 failed"
    print("All test cases passed!")

# Space optimized version
def numDistinct_optimized(s: str, t: str) -> int:
    """
    Space optimized version using 1D DP array
    Time Complexity: O(m*n)
    Space Complexity: O(n)
    """
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    # Process each character in s
    for j in range(1, m + 1):
        # Go backwards to avoid overwriting needed values
        for i in range(n, 0, -1):
            if t[i-1] == s[j-1]:
                dp[i] += dp[i-1]
    
    return dp[n]


# 1. RECURSIVE SOLUTION
def numDistinct(s: str, t: str) -> int:
    """
    Complete visualization for recursive solution with example s="rabbbit", t="rabbit":
    
                                (0,0)'r'[s[0]=r,t[0]=r] -> MATCH
                    /                                           \
        (1,1)'a'[s[1]=a,t[1]=a]                     (1,0)'r'[s[1]=a,t[0]=r]
        MATCH                                        NO MATCH
        /                     \                      /                    \
    (2,2)'b'              (2,1)'a'              (2,0)'r'             (3,0)'r' 
    [s[2]=b,t[2]=b]       [s[2]=b,t[1]=a]       [s[2]=b,t[0]=r]     ...
    MATCH                  NO MATCH               NO MATCH
    /         \           /           \          /          \
(3,3)'b'   (3,2)'b'   (3,1)'a'    (3,1)'a'  (3,0)'r'   (4,0)'r'
MATCH      ...        ...          ...       ...         ...
    
    Base cases:
    - If j == len(t): Found complete match, return 1
    - If i == len(s): Can't match anymore, return 0
    
    Choice at each step:
    1. Always try skipping current char in s (i+1, j)
    2. If chars match s[i]==t[j], also try using char (i+1, j+1)
    
    Time complexity: O(2^m) - each char gives 2 choices
    Space complexity: O(m) - recursion stack depth
    """
    if len(t) > len(s): return 0
    def dfs(i, j):
        if j == len(t): return 1  # Found a valid subsequence
        if i == len(s): return 0  # Reached end without match
        res = dfs(i + 1, j)  # Skip current char
        if s[i] == t[j]: 
            res += dfs(i + 1, j + 1)  # Use current char if matches
        return res
    return dfs(0, 0)

# 2. MEMOIZED SOLUTION 
def numDistinct(s: str, t: str) -> int:
    """
    Complete state evolution for s="rabbbit", t="rabbit":
    
    dp cache building visualization (key states):
    {
        (0,0): 3    <- Final answer: 3 ways to form "rabbit" from "rabbbit"
        │
        ├── (1,1): 2    <- Ways to form "abbit" from "abbbit" after matching 'r'
        │   │
        │   ├── (2,2): 1    <- Ways to form "bbit" from "bbit" after matching 'a'
        │   │   │
        │   │   ├── (3,3): 1    <- Ways to form "bit" from "bit" after matching 'b'
        │   │   └── (3,2): 1    <- Ways to form "bbit" from "bit" skipping 'b'
        │   │
        │   └── (2,1): 1    <- Ways to form "abbit" from "bbit" skipping 'a'
        │
        └── (1,0): 1    <- Ways to form "rabbit" from "abbbit" skipping 'r'
    
    Cache prevents recomputing:
    - Without memo: Calculate every path in tree
    - With memo: Each state (i,j) computed once
    
    Time reduced from O(2^m) to O(m*n)
    Space now O(m*n) for cache
    """
    if len(t) > len(s): return 0
    dp = {}
    def dfs(i, j):
        if j == len(t): return 1
        if i == len(s): return 0
        if (i, j) in dp: return dp[(i, j)]
        res = dfs(i + 1, j)
        if s[i] == t[j]:
            res += dfs(i + 1, j + 1)
        dp[(i, j)] = res
        return res
    return dfs(0, 0)

# 3. BOTTOM-UP DP 
def numDistinct(s: str, t: str) -> int:
    """
    Complete DP table evolution for s="rabbbit", t="rabbit":
    
    Initial state:
    dp[i][j] = number of ways to form t[i:] from s[j:]
    
           r  a  b  b  b  i  t  ''
    r      ?  ?  ?  ?  ?  ?  ?   1
    a      ?  ?  ?  ?  ?  ?  ?   1
    b      ?  ?  ?  ?  ?  ?  ?   1
    b      ?  ?  ?  ?  ?  ?  ?   1
    i      ?  ?  ?  ?  ?  ?  ?   1
    t      ?  ?  ?  ?  ?  ?  ?   1
    ''     0  0  0  0  0  0  0   1
    
    Final filled table:
           r  a  b  b  b  i  t  ''
    r      3  2  2  2  1  1  1   1
    a      0  2  2  2  1  1  1   1
    b      0  0  2  2  1  1  1   1
    b      0  0  0  1  1  1  1   1
    i      0  0  0  0  1  1  1   1
    t      0  0  0  0  0  1  1   1
    ''     0  0  0  0  0  0  0   1
    
    Fill direction: Bottom-up, right-to-left
    - dp[i][j] = dp[i+1][j] (skip current char)
    - If s[i]==t[j]: dp[i][j] += dp[i+1][j+1] (use current char)
    """
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][n] = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = dp[i + 1][j]
            if s[i] == t[j]:
                dp[i][j] += dp[i + 1][j + 1]
    return dp[0][0]

# 4. SPACE-OPTIMIZED DP
def numDistinct(s: str, t: str) -> int:
    """
    Complete array evolution for s="rabbbit", t="rabbit":
    
    Key insight: We only need previous row's values
    
    State evolution:
    1. Initial:
       dp:     [0, 0, 0, 0, 0, 0, 1]
       nextDp: [0, 0, 0, 0, 0, 0, 1]
       
    2. After processing 't':
       dp:     [0, 0, 0, 0, 0, 1, 1]
       nextDp: [0, 0, 0, 0, 0, 1, 1]
       
    3. After processing 'i':
       dp:     [0, 0, 0, 0, 1, 1, 1]
       nextDp: [0, 0, 0, 0, 1, 1, 1]
       
    4. After processing 'b':
       dp:     [0, 0, 0, 1, 1, 1, 1]
       nextDp: [0, 0, 0, 1, 1, 1, 1]
       
    And so on...
    
    Space reduced from O(m*n) to O(n)
    Still need two arrays to avoid overwriting needed values
    """
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    nextDp = [0] * (n + 1)
    dp[n] = nextDp[n] = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            nextDp[j] = dp[j]
            if s[i] == t[j]:
                nextDp[j] += dp[j + 1]
        dp = nextDp[:]
    return dp[0]

# 5. OPTIMAL SPACE DP
def numDistinct(s: str, t: str) -> int:
    """
    Complete evolution for s="rabbbit", t="rabbit":
    
    Key insight: Use single array + prev variable
    
    State evolution with detailed steps:
    1. Initial state: 
       dp = [0, 0, 0, 0, 0, 0, 1]
                                ^ empty string case
    
    2. Process 't' (last char):
       prev = 1
       dp = [0, 0, 0, 0, 0, 1, 1]
                           ^ matched 't'
    
    3. Process 'i':
       prev = 1
       dp = [0, 0, 0, 0, 1, 1, 1]
                        ^ matched 'i'
    
    4. Process 'b':
       prev = 1
       dp = [0, 0, 0, 1, 1, 1, 1]
                     ^ matched 'b'
    
    For each position:
    - prev holds value that would be dp[j+1] in 2D table
    - old_dpj saves current dp[j] before update
    - Update logic same as 2D: dp[j] += prev if chars match
    
    Further space optimization:
    - Single array instead of two
    - Only one extra variable (prev)
    """
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[n] = 1
    for i in range(m - 1, -1, -1):
        prev = 1
        for j in range(n - 1, -1, -1):
            old_dpj = dp[j]
            if s[i] == t[j]:
                dp[j] += prev
            prev = old_dpj
    return dp[0]
# Example walkthrough with s = "rabbbit", t = "rabbit"
# dp array length = len(t) + 1 = 7

# Initial state:
# dp = [0, 0, 0, 0, 0, 0, 1]
#       r  a  b  b  i  t  ''

# After processing last 't' in s:
# dp = [0, 0, 0, 0, 0, 1, 1]
#       r  a  b  b  i  t  ''

# After processing 'i':
# dp = [0, 0, 0, 0, 1, 1, 1]
#       r  a  b  b  i  t  ''

# After processing second 'b':
# dp = [0, 0, 0, 2, 1, 1, 1]
#       r  a  b  b  i  t  ''

# After processing first 'b':
# dp = [0, 0, 1, 2, 1, 1, 1]
#       r  a  b  b  i  t  ''

# After processing 'a':
# dp = [0, 1, 1, 2, 1, 1, 1]
#       r  a  b  b  i  t  ''

# After processing 'r':
# dp = [3, 1, 1, 2, 1, 1, 1]
#       r  a  b  b  i  t  ''

def numDistinct_with_prints(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[n] = 1  # Base case: empty string
    
    print(f"Initial dp: {dp}")
    
    for i in range(m - 1, -1, -1):
        prev = 1
        for j in range(n - 1, -1, -1):
            old_dpj = dp[j]
            if s[i] == t[j]:
                dp[j] += prev
            prev = old_dpj
        print(f"After processing {s[i]}: {dp}")
                
    return dp[0]

# Test with example
s = "rabbbit"
t = "rabbit"
result = numDistinct_with_prints(s, t)
print(f"\nFinal result: {result}")