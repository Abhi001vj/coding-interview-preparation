# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
# 1091. Shortest Path in Binary Matrix
# Medium
# Topics
# Companies
# Hint
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 582.8K
# Submissions
# 1.2M
# Acceptance Rate
# 48.7%
# Topics
# Companies
# Hint 1
# Do a breadth first search to find the shortest path.
# Let me break down what "8-directionally connected" means with clear visuals:
# pythonCopy# From any cell (X), you can move in 8 directions:
# #    NW   N   NE
# #    ↖️    ↑    ↗️
# # W  ←    X    →  E
# #    ↙️    ↓    ↘️
# #    SW   S   SE

# # In code, these 8 directions are represented as:
# directions = [
#     (-1,-1), (-1,0), (-1,1),   # NW, N, NE
#     (0,-1),          (0,1),    # W,     E
#     (1,-1),  (1,0),  (1,1)     # SW, S, SE
# ]
# Example:
# CopyIf we're at cell marked 'X':
# 1 2 3
# 4 X 5
# 6 7 8

# X can move to ANY of the numbered cells because:
# - Cells 2,4,5,7 share an edge with X
# - Cells 1,3,6,8 share a corner with X
# In our BFS solution, we ensure 8-directional connectivity by:

# Defining all 8 possible moves:

# pythonCopydirections = [
#     (0,1),   (1,1),    # Right, Right-Down
#     (1,0),   (1,-1),   # Down, Left-Down
#     (0,-1),  (-1,-1),  # Left, Left-Up
#     (-1,0),  (-1,1)    # Up, Right-Up
# ]

# Checking each direction in BFS:

# pythonCopyfor dx, dy in directions:
#     new_row, new_col = row + dx, col + dy
#     # This ensures we only move to valid adjacent cells
# Visual Example of a Valid Path:
# CopyGrid:
# [0 0 0]
# [1 1 0]
# [1 1 0]

# Valid Path (marked with numbers showing order):
# [1→2→3]
# [× ×→4]
# [× ×→5]

# This path is valid because:
# - Each cell is 0
# - Each cell is connected to the previous cell by either:
#   * Sharing an edge (like 2→3)
#   * Sharing a corner (like 3→4)
# Invalid Path Example:
# Copy[1→2 0]
# [1 1→4]
# [1 1→3]

# This would NOT be valid because:
# 3 and 4 are not adjacent (don't share edge or corner)
# The BFS implementation automatically ensures proper 8-directional connectivity because:

# We only move to adjacent cells (through the 8 directions)
# Each move must be to a valid cell (value = 0)
# We track the path length by incrementing at each move
```python
"""
SHORTEST PATH IN BINARY MATRIX
----------------------------

Pattern Recognition:
1. Shortest Path Problem → BFS is ideal
2. 8-directional movement → Need all 8 neighbors
3. Binary matrix with obstacles → Need validation

Example 1 Visualization:
[0,1]  Start at (0,0)
[1,0]  End at (1,1)

Path: (0,0) → (1,1)
Length: 2 cells

Example 2 Visualization:
[0,0,0]  Start at (0,0)
[1,1,0]  End at (2,2)
[1,1,0]

Path: (0,0) → (0,1) → (0,2) → (1,2) → (2,2)
Length: 4 cells
"""

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
            
        n = len(grid)
        # All 8 directions: right, right-down, down, left-down, 
        # left, left-up, up, right-up
        directions = [
            (0,1), (1,1), (1,0), (1,-1),
            (0,-1), (-1,-1), (-1,0), (-1,1)
        ]
        
        """
        BFS State Visualization:
        For grid:
        [0,0,0]
        [1,1,0]
        [1,1,0]
        
        Initial queue: [(0,0,1)]  # (row, col, path_length)
        visited = {(0,0)}
        
        Step 1:
        Current: (0,0,1)
        Check neighbors: (0,1), (1,1), (1,0)
        Valid next: (0,1)
        Queue: [(0,1,2)]
        
        Step 2:
        Current: (0,1,2)
        Check neighbors...
        And so on.
        """
        
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        visited = {(0, 0)}
        
        while queue:
            row, col, path_length = queue.popleft()
            
            # If reached target
            if (row, col) == (n-1, n-1):
                return path_length
            
            # Check all 8 directions
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                # Validate new position
                if (0 <= new_row < n and 
                    0 <= new_col < n and 
                    grid[new_row][new_col] == 0 and
                    (new_row, new_col) not in visited):
                    
                    queue.append((new_row, new_col, path_length + 1))
                    visited.add((new_row, new_col))
        
        return -1

"""
Time Complexity Analysis: O(N²)
- In worst case, we might visit all cells
- For each cell, we check 8 directions
- N² cells total for N×N grid
- Each cell visited at most once due to visited set

Space Complexity: O(N²)
- Queue might contain O(N²) cells in worst case
- Visited set can store O(N²) cells
- N² space for N×N grid

Detailed Example Trace:
grid = [[0,0,0],
        [1,1,0],
        [1,1,0]]

1. Start at (0,0)
   Queue: [(0,0,1)]
   Visited: {(0,0)}

2. Process (0,0)
   Valid moves: (0,1)
   Queue: [(0,1,2)]
   Visited: {(0,0), (0,1)}

3. Process (0,1)
   Valid moves: (0,2)
   Queue: [(0,2,3)]
   Visited: {(0,0), (0,1), (0,2)}

4. Process (0,2)
   Valid moves: (1,2)
   Queue: [(1,2,4)]
   Visited: {(0,0), (0,1), (0,2), (1,2)}

5. Process (1,2)
   Valid moves: (2,2)
   Queue: [(2,2,5)]
   Visited: {(0,0), (0,1), (0,2), (1,2), (2,2)}

6. Process (2,2) - Target reached!
   Return path_length = 4

BFS guarantees shortest path because:
1. Processes cells level by level
2. First time reaching target is shortest path
3. All moves have same cost (1 cell)
"""
```