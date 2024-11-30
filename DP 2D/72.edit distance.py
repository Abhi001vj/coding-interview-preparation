# https://leetcode.com/problems/edit-distance/description/
# 72. Edit Distance
# Solved
# Medium
# Topics
# Companies
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.

# Edit Distance Solutions: Top-down and Bottom-up approaches

def minDistance_recursive(word1: str, word2: str) -> int:
    """
    Top-down recursive solution with memoization
    
    Visualization of decision tree for word1="horse", word2="ros":
                        (0,0) h->r
                    /       |        \
            Insert     Replace      Delete
            (0,1)      (1,1)       (1,0)
            h->ro    o->o          o->r
           /  |  \   /  |  \      /  |  \
         ...  ... ... ... ... ... ... ... ...
    
    At each state (i,j), we have three choices:
    1. Insert: (i,j+1) - insert char from word2
    2. Delete: (i+1,j) - delete char from word1
    3. Replace: (i+1,j+1) - replace if chars different
                           or match if chars same
    """
    def dfs(i, j, memo={}):
        # Base cases:
        # If word1 is empty, insert all remaining chars from word2
        if i == len(word1): 
            return len(word2) - j
        # If word2 is empty, delete all remaining chars from word1
        if j == len(word2): 
            return len(word1) - i
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        # If characters match, move to next characters
        if word1[i] == word2[j]:
            memo[(i,j)] = dfs(i+1, j+1, memo)
        else:
            # Try all three operations and take minimum
            insert = 1 + dfs(i, j+1, memo)    # Insert word2[j]
            delete = 1 + dfs(i+1, j, memo)    # Delete word1[i]
            replace = 1 + dfs(i+1, j+1, memo) # Replace word1[i] with word2[j]
            memo[(i,j)] = min(insert, delete, replace)
            
        return memo[(i,j)]
    
    return dfs(0, 0)

def minDistance_dp(word1: str, word2: str) -> int:
    """
    Bottom-up DP solution
    
    DP Table visualization for word1="horse", word2="ros":
    
        ''  r   o   s
    ''   0  1   2   3
    h    1  1   2   3
    o    2  2   1   2
    r    3  2   2   2
    s    4  3   3   2
    e    5  4   4   3
    
    dp[i][j] = min operations to convert word1[0:i] to word2[0:j]
    
    For each cell, take minimum of:
    1. Insert:  dp[i][j-1] + 1
    2. Delete:  dp[i-1][j] + 1
    3. Replace: dp[i-1][j-1] + (1 if chars different, 0 if same)
    
    Space complexity optimization:
    - Only need previous row to compute current row
    - Can use two arrays instead of full table
    """
    m, n = len(word1), len(word2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting chars from word1
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting chars from word2
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                # Characters match - no operation needed
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take minimum of three operations
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]

# Space optimized version
def minDistance_optimized(word1: str, word2: str) -> int:
    """
    Space-optimized DP solution using only two rows
    
    Evolution of dp arrays for word1="horse", word2="ros":
    
    Initial:  [0, 1, 2, 3]  prev_row
             [1, 0, 0, 0]  curr_row
    
    After h:  [1, 1, 2, 3]
             [2, 0, 0, 0]
    
    After o:  [2, 2, 1, 2]
             [3, 0, 0, 0]
    
    And so on...
    
    Space complexity reduced from O(m*n) to O(n)
    Time complexity remains O(m*n)
    """
    m, n = len(word1), len(word2)
    
    # Use only two rows
    prev_row = list(range(n + 1))
    curr_row = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr_row[0] = i  # Initialize first column
        
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr_row[j] = prev_row[j-1]
            else:
                curr_row[j] = 1 + min(
                    prev_row[j],    # Delete
                    curr_row[j-1],  # Insert
                    prev_row[j-1]   # Replace
                )
        
        # Swap rows
        prev_row, curr_row = curr_row, prev_row
    
    return prev_row[n]
"""
Edit Distance: Comprehensive Solution Analysis
===========================================

Example being traced throughout: word1 = "horse", word2 = "ros"
We will visualize complete paths and state transitions for all approaches.
"""
"""
Complete Edit Distance Path Visualization for Example 2: "intention" → "execution"

1. Complete Recursive Tree Path (showing key branches):

                                    (0,0) intention→execution
                        /                    |                     \
            (1,0) ntention→execution  (0,1) intention→xecution  (1,1) ntention→xecution
                /     |      \           /     |      \           /     |      \
        Delete  Insert Replace      Delete  Insert Replace     Delete Insert  Replace
        't'     'e'    'i'→'e'     'i'     'e'    'i'→'e'    't'    'e'    'n'→'x'
        ...     ...     ...        ...     ...     ...        ...    ...     ...

2. Complete DP Table Evolution:
                     e    x    e    c    u    t    i    o    n
                     1    2    3    4    5    6    7    8    9
intention     1  [   1    2    3    4    5    6    7    8    9   ]
intention     2  [   1    2    3    4    5    6    7    8    9   ]
intention     3  [   2    2    3    4    5    6    7    8    8   ]
intention     4  [   3    3    3    4    5    6    7    7    8   ]
intention     5  [   4    4    4    4    5    6    6    7    8   ]
intention     6  [   5    5    5    5    5    5    6    7    8   ]
intention     7  [   6    6    6    6    6    6    5    6    7   ]
intention     8  [   7    7    7    7    7    7    6    5    6   ]
intention     9  [   8    8    8    8    8    8    7    6    5   ]

3. Complete State Evolution with Operation Choices:
Step 1: intention → inention (Delete 't')
        State (5,5): Looking at 't' and 'u'
        Options: {Delete: 5, Insert: 6, Replace: 6}
        Choice: Delete (cost = 5)

Step 2: inention → enention (Replace 'i' with 'e')
        State (0,0): Looking at 'i' and 'e'
        Options: {Delete: 6, Insert: 6, Replace: 5}
        Choice: Replace (cost = 5)

Step 3: enention → exention (Replace 'n' with 'x')
        State (2,2): Looking at 'n' and 'x'
        Options: {Delete: 6, Insert: 6, Replace: 5}
        Choice: Replace (cost = 5)

Step 4: exention → exection (Replace 'n' with 'c')
        State (4,4): Looking at 'n' and 'c'
        Options: {Delete: 6, Insert: 6, Replace: 5}
        Choice: Replace (cost = 5)

Step 5: exection → execution (Insert 'u')
        State (5,5): Looking at empty and 'u'
        Options: {Delete: 6, Insert: 5, Replace: 6}
        Choice: Insert (cost = 5)

4. Complete Space-Optimized Array Evolution:
Initial:  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Step 1:   [8, 7, 6, 6, 5, 4, 3, 2, 1, 1]
Step 2:   [7, 6, 6, 5, 5, 4, 3, 2, 2, 2]
Step 3:   [6, 6, 5, 5, 4, 4, 3, 3, 3, 3]
Step 4:   [5, 5, 5, 4, 4, 4, 4, 4, 4, 4]
Step 5:   [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

5. Final Path with Detailed State Changes:
intention → inention  (Delete 't', state: (5,5) → (5,6))
    ↓
inention → enention  (Replace 'i'→'e', state: (0,0) → (1,1))
    ↓
enention → exention  (Replace 'n'→'x', state: (2,2) → (3,3))
    ↓
exention → exection  (Replace 'n'→'c', state: (4,4) → (5,5))
    ↓
exection → execution (Insert 'u', state: (5,5) → (6,6))

Total Operations: 5 (1 Delete + 3 Replace + 1 Insert)
Minimum Edit Distance: 5
"""
def minDistance(word1: str, word2: str) -> int:
    """
    Complete solution demonstration with all approaches.
    Example: Transform "horse" → "ros"
    
    Complete transformation paths:
    1. horse → rorse (replace 'h' with 'r')
    2. rorse → rose (delete 'r')
    3. rose → ros (delete 'e')
    """
    
    def recursive_solution(word1: str, word2: str) -> int:
        """
        Complete Recursive Path Visualization:
        
        Starting state: (horse, ros)
                                (0,0) horse→ros
                        /           |            \
            (1,0) orse→ros  (1,1) orse→os  (0,1) horse→os
                /   |    \      /    |    \     /    |    \
        (2,0)→  (2,1)→  (1,1)→ (2,1)→ (2,2)→...  ...   ...
        rse→ros  rse→os  orse→os  rse→os  se→s
        
        Complete path for optimal solution:
        (0,0) horse→ros [Replace h→r, cost: 1]
        └── (1,1) orse→os [Delete r, cost: 1]
            └── (2,1) se→os [Delete e, cost: 1]
                └── (3,1) e→os [Match s, cost: 0]
                    └── Return total cost: 3
        """
        def dfs(i: int, j: int) -> int:
            # Base cases with complete paths
            if i == len(word1): 
                # Example: "" → "os" requires 2 insertions
                # Complete path: "" → "o" → "os"
                return len(word2) - j
            if j == len(word2):
                # Example: "rse" → "" requires 3 deletions
                # Complete path: "rse" → "se" → "e" → ""
                return len(word1) - i
            
            if word1[i] == word2[j]:
                # Characters match, no operation needed
                # Example: "rose" → "ros", 'e' matches
                return dfs(i + 1, j + 1)
            
            # Try all three operations with complete paths
            delete = dfs(i + 1, j)      # Delete word1[i]
            insert = dfs(i, j + 1)      # Insert word2[j]
            replace = dfs(i + 1, j + 1)  # Replace word1[i] with word2[j]
            
            return 1 + min(delete, insert, replace)
            
        return dfs(0, 0)

    def memoized_solution(word1: str, word2: str) -> int:
        """
        Complete Memoization State Map for "horse" → "ros":
        
        dp = {
            (0,0): 3  # horse → ros = Replace + Delete + Delete
                ├── Replace 'h' with 'r': (1,1): 2
                │   └── Delete 'r': (2,1): 1
                │       └── Match 's': (3,2): 1
                │           └── Delete 'e': (4,2): 0
                ├── Delete 'h': (1,0): 3
                │   └── [Further states...]
                └── Insert 'r': (0,1): 4
                    └── [Further states...]
            
            Full path reconstruction:
            (0,0) horse→ros
            └── (1,1) orse→os [Replace h→r]
                └── (2,1) se→os [Delete r]
                    └── (3,2) e→s [Delete e]
                        └── (4,3) →"" [Complete]
        """
        memo = {}
        
        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == len(word1): return len(word2) - j
            if j == len(word2): return len(word1) - i
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = 1 + min(
                    dfs(i + 1, j),    # Delete
                    dfs(i, j + 1),    # Insert
                    dfs(i + 1, j + 1) # Replace
                )
            return memo[(i, j)]
            
        return dfs(0, 0)
    
    def tabulation_solution(word1: str, word2: str) -> int:
        """
        Complete DP Table Evolution for "horse" → "ros":
        
        Initial table:
            ''  r   o   s
        ''   0   1   2   3
        h    1   ?   ?   ?
        o    2   ?   ?   ?
        r    3   ?   ?   ?
        s    4   ?   ?   ?
        e    5   ?   ?   ?
        
        After processing 'h':
            ''  r   o   s
        ''   0   1   2   3
        h    1   1   2   3
        o    2   ?   ?   ?
        r    3   ?   ?   ?
        s    4   ?   ?   ?
        e    5   ?   ?   ?
        
        Complete final table:
            ''  r   o   s
        ''   0   1   2   3
        h    1   1   2   3
        o    2   2   1   2
        r    3   2   2   2
        s    4   3   3   2
        e    5   4   4   3
        
        Path reconstruction:
        (0,0) → (1,1) [Replace h→r]
             → (2,2) [Match o]
             → (3,2) [Delete r]
             → (4,3) [Match s]
             → (5,3) [Delete e]
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize with deletion/insertion costs
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # Fill table with detailed state transitions
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # Delete
                        dp[i][j-1],    # Insert
                        dp[i-1][j-1]   # Replace
                    )
        return dp[m][n]
    
    def optimized_solution(word1: str, word2: str) -> int:
        """
        Complete State Evolution with Space Optimization:
        
        For "horse" → "ros":
        
        Initial:
        prev_row =  [0, 1, 2, 3]  # Base case: "" → "ros"
        
        After 'h':
        prev_row =  [1, 1, 2, 3]  # Cases: h→"", h→r, h→ro, h→ros
        
        After 'o':
        prev_row =  [2, 2, 1, 2]  # Cases: ho→"", ho→r, ho→ro, ho→ros
        
        After 'r':
        prev_row =  [3, 2, 2, 2]  # hor→"", hor→r, hor→ro, hor→ros
        
        After 's':
        prev_row =  [4, 3, 3, 2]  # hors→"", hors→r, hors→ro, hors→ros
        
        After 'e':
        prev_row =  [5, 4, 4, 3]  # horse→"", horse→r, horse→ro, horse→ros
        
        Complete transformation path:
        1. horse → rorse (replace 'h'→'r', using dp[i-1][j-1]+1)
        2. rorse → rose (delete 'r', using dp[i-1][j])
        3. rose → ros (delete 'e', using dp[i-1][j])
        """
        if len(word1) < len(word2):
            word1, word2 = word2, word1
            
        m, n = len(word1), len(word2)
        prev_row = list(range(n + 1))
        
        for i in range(m):
            current_row = [i + 1] + [0] * n
            for j in range(n):
                if word1[i] == word2[j]:
                    current_row[j + 1] = prev_row[j]
                else:
                    current_row[j + 1] = 1 + min(
                        prev_row[j],      # Replace
                        prev_row[j + 1],  # Delete
                        current_row[j]    # Insert
                    )
            prev_row = current_row
        
        return prev_row[n]
    
    # Return optimized solution with complete path visualization
    return optimized_solution(word1, word2)

# Test cases with complete path visualization
def test_edit_distance():
    """
    Test Suite with Complete Path Visualizations:
    
    1. Basic case: "horse" → "ros"
       Path: horse → rorse → rose → ros
       Operations: Replace(h→r) + Delete(r) + Delete(e)
       Cost: 3
    
    2. Complex case: "intention" → "execution"
       Path: intention → inention → enention → exention → 
             exection → execution
       Operations: Delete(t) + Replace(i→e) + Replace(n→x) +
                  Replace(n→c) + Insert(u)
       Cost: 5
    
    3. Empty string: "" → "abc"
       Path: "" → a → ab → abc
       Operations: Insert(a) + Insert(b) + Insert(c)
       Cost: 3
    
    4. Same strings: "same" → "same"
       Path: No operations needed
       Cost: 0
    """
    test_cases = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "abc", 3),
        ("abc", "", 3),
        ("same", "same", 0)
    ]
    
    for word1, word2, expected in test_cases:
        result = minDistance(word1, word2)
        assert result == expected, \
            f"Failed: {word1} → {word2}, got {result}, expected {expected}"
    print("All test cases passed!")

if __name__ == "__main__":
    test_edit_distance()

    def minDistance(word1: str, word2: str) -> int:
    """
    Complete solution demonstration with all approaches.
    Example: Transform "intention" → "execution"
    
    Complete transformation paths:
    1. intention → inention (remove 't')
    2. inention → enention (replace 'i' with 'e')
    3. enention → exention (replace 'n' with 'x')
    4. exention → exection (replace 'n' with 'c')
    5. exection → execution (insert 'u')
    """
    
    def recursive_solution(word1: str, word2: str) -> int:
        """
        Complete Recursive Path Visualization:
        
        Starting state: (intention, execution)
                                (0,0) intention→execution
                        /                |                   \
        (1,0) ntention→execution  (1,1) ntention→xecution  (0,1) intention→xecution
            /     |        \         /        |       \        /       |        \
    (2,0)→    (2,1)→     (1,1)→   (2,1)→   (2,2)→  ...    ...      ...      ...
    tention→  tention→   ntention→ tention→  ention→
    execution execution   xecution execution  xecution
        
        Complete path for optimal solution:
        (0,0) intention→execution [Delete t, cost: 1]
        └── (1,1) inention→execution [Replace i→e, cost: 1]
            └── (2,2) nention→xecution [Replace n→x, cost: 1]
                └── (4,4) ention→ecution [Replace n→c, cost: 1]
                    └── (5,5) ention→execution [Insert u, cost: 1]
                        └── Return total cost: 5
        """
        def dfs(i: int, j: int) -> int:
            # Implementation remains the same but state visualization changed
            
    def memoized_solution(word1: str, word2: str) -> int:
        """
        Complete Memoization State Map for "intention" → "execution":
        
        dp = {
            (0,0): 5  # intention → execution = Delete + Replace + Replace + Replace + Insert
                ├── Delete 't': (5,5): 4
                │   └── Replace 'i' with 'e': (0,0): 3
                │       └── Replace 'n' with 'x': (2,2): 2
                │           └── Replace 'n' with 'c': (4,4): 1
                │               └── Insert 'u': (5,5): 0
                ├── Replace 'i' with 'e': (0,0): 6
                │   └── [Further states...]
                └── Insert 'e': (0,1): 6
                    └── [Further states...]
            
            Full path reconstruction:
            (0,0) intention→execution
            └── (5,5) inention→execution [Delete t]
                └── (0,0) enention→execution [Replace i→e]
                    └── (2,2) exention→execution [Replace n→x]
                        └── (4,4) exection→execution [Replace n→c]
                            └── (5,5) execution [Insert u]
        """
        
    def tabulation_solution(word1: str, word2: str) -> int:
        """
        Complete DP Table Evolution for "intention" → "execution":
        
        Initial table:
            ''  e   x   e   c   u   t   i   o   n
        ''   0   1   2   3   4   5   6   7   8   9
        i    1   ?   ?   ?   ?   ?   ?   ?   ?   ?
        n    2   ?   ?   ?   ?   ?   ?   ?   ?   ?
        t    3   ?   ?   ?   ?   ?   ?   ?   ?   ?
        e    4   ?   ?   ?   ?   ?   ?   ?   ?   ?
        n    5   ?   ?   ?   ?   ?   ?   ?   ?   ?
        t    6   ?   ?   ?   ?   ?   ?   ?   ?   ?
        i    7   ?   ?   ?   ?   ?   ?   ?   ?   ?
        o    8   ?   ?   ?   ?   ?   ?   ?   ?   ?
        n    9   ?   ?   ?   ?   ?   ?   ?   ?   ?
        
        Complete final table:
            ''  e   x   e   c   u   t   i   o   n
        ''   0   1   2   3   4   5   6   7   8   9
        i    1   1   2   3   4   5   6   6   7   8
        n    2   2   2   3   4   5   6   7   7   7
        t    3   3   3   3   4   5   5   6   7   8
        e    4   3   4   3   4   5   6   7   8   9
        n    5   4   4   4   4   5   6   7   8   8
        t    6   5   5   5   5   5   5   6   7   8
        i    7   6   6   6   6   6   6   5   6   7
        o    8   7   7   7   7   7   7   6   5   6
        n    9   8   8   8   8   8   8   7   6   5
        
        Path reconstruction:
        (0,0) → (5,5) [Delete t]
             → (0,0) [Replace i→e]
             → (2,2) [Replace n→x]
             → (4,4) [Replace n→c]
             → (5,5) [Insert u]
        """
        
    def optimized_solution(word1: str, word2: str) -> int:
        """
        Complete State Evolution with Space Optimization:
        
        For "intention" → "execution":
        
        Initial:
        prev_row = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Base case: "" → "execution"
        
        After 'i':
        prev_row = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8]  # Cases: i→"", i→e, i→ex, ...
        
        After 'n':
        prev_row = [2, 2, 2, 3, 4, 5, 6, 7, 7, 7]  # Cases: in→"", in→e, in→ex, ...
        
        Each row represents one character processing from intention, building
        minimum edit distances for all prefixes of execution.
        
        Complete transformation path:
        1. intention → inention (delete 't', using dp[i-1][j])
        2. inention → enention (replace 'i'→'e', using dp[i-1][j-1]+1)
        3. enention → exention (replace 'n'→'x', using dp[i-1][j-1]+1)
        4. exention → exection (replace 'n'→'c', using dp[i-1][j-1]+1)
        5. exection → execution (insert 'u', using dp[i][j-1]+1)
        """
        # Implementation remains the same but visualizations updated for new example