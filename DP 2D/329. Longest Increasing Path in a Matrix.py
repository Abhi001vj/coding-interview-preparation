# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
# 329. Longest Increasing Path in a Matrix
# Hard
# Topics
# Companies
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

# Example 1:


# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:


# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:

# Input: matrix = [[1]]
# Output: 1
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1

```python
"""
LONGEST INCREASING PATH IN MATRIX ANALYSIS
Example matrix = [[9,9,4],
                 [6,6,8],
                 [2,1,1]]

1. RECURSIVE SOLUTION (DFS)
--------------------------
For matrix[0][0] = 9, visualizing path exploration:

DFS Tree from (0,0):
                    9(0,0)
                 /     |     \
           6(1,0)  9(0,1)  4(0,2)
           /          /        \
       2(2,0)     6(1,1)     8(1,2)
         |          /           |
       1(2,1)    2(2,0)      1(2,2)
                    |
                 1(2,1)

Complete state exploration:
- Each cell shows value(row,col)
- Each level shows decreasing values possible
- Maximum path length is tracked at each node
"""
def recursive_solution(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
    
    def dfs(i: int, j: int) -> int:
        # Base case: Start counting from 1 (current cell)
        max_len = 1
        
        # Explore all 4 directions for increasing values
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < ROWS and 0 <= nj < COLS and 
                matrix[ni][nj] > matrix[i][j]):
                curr_len = 1 + dfs(ni, nj)
                max_len = max(max_len, curr_len)
        
        return max_len
    
    return max(dfs(i, j) for i in range(ROWS) for j in range(COLS))

"""
2. MEMOIZED SOLUTION
-------------------
For example matrix, showing DP table evolution:

Initial DP state:
[[-1,-1,-1],
 [-1,-1,-1],
 [-1,-1,-1]]

After exploring (0,0)=9:
[[4,-1,-1],
 [-1,-1,-1],
 [-1,-1,-1]]

After exploring all paths:
[[4,4,3],
 [3,3,2],
 [2,1,1]]

Each cell shows longest path starting from that position
"""
def memoized_solution(matrix):
    if not matrix:
        return 0
        
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = {}  # (i,j) -> longest path from (i,j)
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def dfs(i: int, j: int) -> int:
        # Return cached result if available
        if (i,j) in dp:
            return dp[(i,j)]
            
        max_len = 1  # Base case: single cell path
        
        # Try all directions for increasing values
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < ROWS and 0 <= nj < COLS and 
                matrix[ni][nj] > matrix[i][j]):
                curr_len = 1 + dfs(ni, nj)
                max_len = max(max_len, curr_len)
                
        dp[(i,j)] = max_len
        return max_len

"""
3. EXAMPLE PATH TRACING
For matrix = [[9,9,4],
              [6,6,8],
              [2,1,1]]

Longest path: 1 -> 2 -> 6 -> 9
Path visualization:
Step 1: Start at 1(2,1)
[[9,9,4],
 [6,6,8],
 [2,*1,1]]

Step 2: Move to 2(2,0)
[[9,9,4],
 [6,6,8],
 [*2,*1,1]]

Step 3: Move to 6(1,0)
[[9,9,4],
 [*6,6,8],
 [*2,*1,1]]

Step 4: Move to 9(0,0)
[[*9,9,4],
 [*6,6,8],
 [*2,*1,1]]

Final path length = 4
"""

def optimized_solution(matrix):
    """
    Space-optimized solution tracking just maximum length.
    Step-by-step processing:
    
    1. For matrix[2][1]=1:
       - No increasing neighbors
       - Max length = 1
    
    2. For matrix[2][0]=2:
       - Can move to 6
       - Max length = 2
    
    3. For matrix[1][0]=6:
       - Can move to 9
       - Max length = 3
       
    4. For matrix[0][0]=9:
       - No further moves
       - Max length = 4
    """
    if not matrix:
        return 0
        
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = {}
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def dfs(i: int, j: int) -> int:
        if (i,j) in dp:
            return dp[(i,j)]
            
        max_len = 1
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < ROWS and 0 <= nj < COLS and 
                matrix[ni][nj] > matrix[i][j]):
                curr_len = 1 + dfs(ni, nj)
                max_len = max(max_len, curr_len)
                
        dp[(i,j)] = max_len
        return max_len
        
    return max(dfs(i, j) for i in range(ROWS) for j in range(COLS))

# Test cases showing different scenarios
def test_cases():
    matrices = [
        # Example 1: Multiple paths
        [[9,9,4],
         [6,6,8],
         [2,1,1]],
         
        # Example 2: Diagonal-like path
        [[3,4,5],
         [3,2,6],
         [2,2,1]],
         
        # Example 3: Single cell
        [[1]]
    ]
    
    for matrix in matrices:
        print(f"Matrix: {matrix}")
        print(f"Longest path length: {optimized_solution(matrix)}")
```

```python
"""
PROBLEM ANALYSIS: Longest Increasing Path in Matrix
Example matrix: 
[
    [9,9,4],
    [6,6,8],
    [2,1,1]
]

1. RECURSIVE DFS SOLUTION
------------------------
Approach: For each cell, try all 4 directions recursively.

Decision Tree for starting at matrix[0][0] = 9:
              (0,0)=9
           /     |     \
   (0,1)=9  (1,0)=6  (0,-1)=X
     |          |
(1,1)=6    (2,0)=2
     |          |
(2,1)=1    (2,1)=1

Full path exploration visualization:
* → current cell
# → visited cells
. → unvisited cells

For path 9→6→2→1:
Step 1:    Step 2:    Step 3:    Step 4:
*9 9 4    #9 9 4    #9 9 4    #9 9 4
 6 6 8    *6 6 8    #6 6 8    #6 6 8
 2 1 1     2 1 1    *2 1 1    #2 *1 1
"""
def recursive_solution(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
    
    def dfs(r: int, c: int, prevVal: int) -> int:
        # Base case: out of bounds or not increasing
        if (min(r, c) < 0 or r >= ROWS or 
            c >= COLS or matrix[r][c] <= prevVal):
            return 0
            
        # Try all directions and take maximum path length
        res = 1  # Count current cell
        for d in directions:
            res = max(res, 1 + dfs(r + d[0], c + d[1], matrix[r][c]))
        return res
    
    return max(dfs(r, c, float('-inf')) 
              for r in range(ROWS) 
              for c in range(COLS))

"""
2. MEMOIZED SOLUTION (TOP-DOWN DP)
--------------------------------
Visualization of DP table evolution for matrix[0][0]:

Initial state:
dp = {}  # Empty cache

After exploring (0,0):
dp = {
    (0,0): 4,  # Longest path from 9
    (1,0): 3,  # Longest path from 6
    (2,0): 2,  # Longest path from 2
    (2,1): 1   # Longest path from 1
}

State transitions:
(r,c) -> max length = 1 + max(length from neighbors)

Complete dp cache after all explorations:
dp = {
    (0,0): 4, (0,1): 4, (0,2): 3,
    (1,0): 3, (1,1): 3, (1,2): 2,
    (2,0): 2, (2,1): 1, (2,2): 1
}
"""
def memoized_solution(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = {}  # Cache for (r,c) -> longest path length
    
    def dfs(r: int, c: int, prevVal: int) -> int:
        if (r < 0 or r == ROWS or 
            c < 0 or c == COLS or 
            matrix[r][c] <= prevVal):
            return 0
            
        if (r, c) in dp:
            return dp[(r, c)]
        
        # Check all four directions
        res = 1
        res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))  # down
        res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))  # up
        res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))  # right
        res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))  # left
        
        dp[(r, c)] = res
        return res

"""
3. TOPOLOGICAL SORT SOLUTION
--------------------------
Using same matrix:
[
    [9,9,4],
    [6,6,8],
    [2,1,1]
]

Indegree calculation:
1. For each cell, count smaller neighbors
2. Indegree matrix shows dependencies:

Initial indegree:
[[2,2,1],
 [1,2,1],
 [0,0,0]]

Processing levels:
Level 1: Start with indegree=0 cells (values 1,1,2)
Level 2: Process cells with indegree=0 after removing level 1 (values 6,6,8)
Level 3: Process remaining cells (values 9,9,4)

Visualization of processing:
Level 1:    Level 2:    Level 3:
2 1 1   →   6 6 8   →   9 9 4
(processed) (processed) (processed)

Final path length = number of levels = 4
"""
def topological_sort_solution(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    # Calculate indegree for each cell
    indegree = [[0] * COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            for d in directions:
                nr, nc = d[0] + r, d[1] + c
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    matrix[nr][nc] < matrix[r][c]):
                    indegree[r][c] += 1
    
    # Start with cells having no smaller neighbors
    q = deque()
    for r in range(ROWS):
        for c in range(COLS):
            if indegree[r][c] == 0:
                q.append([r, c])
    
    # Process level by level
    LIS = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    matrix[nr][nc] > matrix[r][c]):
                    indegree[nr][nc] -= 1
                    if indegree[nr][nc] == 0:
                        q.append([nr, nc])
        LIS += 1
    return LIS
```
```python
"""
SOLUTION COMPARISON
------------------

1. FIRST SOLUTION: Dictionary-based Memoization
---------------------------------------------
Key characteristics:
- Uses dictionary for memoization
- Passes previous value through recursion
- Uses directions array
- Handles bounds checking first
"""
def solution1(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    dp = {}  # Key: (r,c) -> Value: longest path from (r,c)
    
    def dfs(r, c, prevVal):
        # First check: bounds and increasing condition
        if (min(r, c) < 0 or r >= ROWS or 
            c >= COLS or matrix[r][c] <= prevVal):
            return 0
            
        # Second check: memoization
        if (r,c) in dp:
            return dp[(r,c)]
        
        # Calculate result using directions array
        res = 1
        for d in directions:
            res = max(res, 1 + dfs(r + d[0], c + d[1], matrix[r][c]))
        dp[(r, c)] = res
        return res

"""
2. SECOND SOLUTION: 2D Array Memoization
--------------------------------------
Key characteristics:
- Uses 2D array for memoization
- Checks current value against neighbors
- Inline direction checks
- Handles memoization check first
"""
def solution2(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for i in range(rows)]  # 2D array initialization
    
    def dfs(i, j):
        # First check: memoization
        if not dp[i][j]:
            val = matrix[i][j]
            # Check all four directions inline with bounds checking
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < rows - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < cols - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

"""
KEY DIFFERENCES:
--------------

1. Memoization Structure:
   Solution 1: Dictionary {(r,c): length}
   Solution 2: 2D array dp[r][c]
   
   Memory usage comparison:
   Dictionary: O(m*n) but with hash table overhead
   2D Array: O(m*n) with direct access

2. Parameter Passing:
   Solution 1: Passes prevVal through recursion
   Solution 2: Compares current value with neighbors directly
   
   Example for cell (1,1) = 6:
   Solution 1: dfs(1,1,prevVal=4) checks 6>4
   Solution 2: dfs(1,1) checks matrix[1][1]>matrix[0][1]

3. Direction Handling:
   Solution 1: Uses directions array and loop
   Solution 2: Inline checks for each direction
   
   for cell (1,1):
   Solution 1:
   [[-1,0], [1,0], [0,-1], [0,1]] → check each
   
   Solution 2:
   up, down, left, right checked separately

4. Bounds Checking:
   Solution 1: Checks bounds first, then processes
   Solution 2: Combines bounds and value checks
   
   Example:
   Solution 1: if min(r,c) < 0 or r >= ROWS...
   Solution 2: if i and val > matrix[i-1][j]...

5. Return Value Access:
   Solution 1: return max(dp.values())
   Solution 2: return max(max(x) for x in dp)
   
   Dictionary vs 2D array traversal
"""

# Example matrix for visualization:
matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]

"""
Memory State Comparison:
----------------------
For the example matrix:

Solution 1 dp (dictionary):
{
    (0,0): 4, (0,1): 4, (0,2): 3,
    (1,0): 3, (1,1): 3, (1,2): 2,
    (2,0): 2, (2,1): 1, (2,2): 1
}

Solution 2 dp (2D array):
[
    [4, 4, 3],
    [3, 3, 2],
    [2, 1, 1]
]
"""