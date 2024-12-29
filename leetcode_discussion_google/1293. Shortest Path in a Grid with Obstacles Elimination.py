# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
# 1293. Shortest Path in a Grid with Obstacles Elimination
#     Hard
# Topics
# Companies
# Hint
# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

# Example 1:


# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# Example 2:


# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 226.6K
# Submissions
# 499K
# Acceptance Rate
# 45.4%
# Topics
# Companies
# 0 - 3 months
# Pinterest
# 6
# AppFolio
# 2
# 0 - 6 months
# Google
# 7
# Amazon
# 4
# TikTok
# 2
# IMC
# 2
# 6 months ago
# Meta
# 4
# Snap
# 4
# Apple
# 3
# Hint 1
# Use BFS.
# Hint 2
# BFS on (x,y,r) x,y is coordinate, r is remain number of obstacles you can remove.
```python
"""
SHORTEST PATH WITH OBSTACLES ELIMINATION
-------------------------------------

Key Insight:
1. BFS with state = (row, col, remaining_k)
2. Need to track visited states to avoid cycles
3. Can move to obstacle if k > 0

Example Visualization:
grid = [
    [0,0,0],
    [1,1,0],  k = 1
    [0,0,0]
]

States shown as (row,col,k):
(0,0,1) → (0,1,1) → (0,2,1) →
                     (1,2,1) →
                     (2,2,1)

If we hit obstacle at (1,1):
(row,col,k) -> (1,1,0)  # k reduced
"""

from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # If k is large enough, we can go directly
        # Manhattan distance is minimum possible steps
        if k >= m + n - 2:
            return m + n - 2
        
        # Directions: right, down, left, up
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # Queue: (row, col, remaining_k, steps)
        queue = deque([(0, 0, k, 0)])
        # Visited: (row, col, remaining_k)
        visited = {(0, 0, k)}
        
        """
        Example State Transitions:
        Start: (0,0,k,0)
        
        If next cell is empty (0):
        (0,0,k,0) → (0,1,k,1)
        
        If next cell is obstacle (1):
        (0,0,k,0) → (0,1,k-1,1)
        
        Invalid moves:
        - Out of bounds
        - Obstacle when k=0
        - Already visited state
        """
        
        while queue:
            row, col, obstacles, steps = queue.popleft()
            
            # Reached target
            if (row, col) == (m-1, n-1):
                return steps
            
            # Try all 4 directions
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                # Check bounds
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_obstacles = obstacles
                    
                    # If hit obstacle and can remove it
                    if grid[new_row][new_col] == 1:
                        if obstacles == 0:  # Can't remove more obstacles
                            continue
                        new_obstacles = obstacles - 1
                    
                    new_state = (new_row, new_col, new_obstacles)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_row, new_col, new_obstacles, steps + 1))
        
        return -1

"""
Time Complexity: O(m*n*k)
- For each cell (m*n)
- We can have k+1 states
- Each state processed once
- Total states possible: m*n*(k+1)

Space Complexity: O(m*n*k)
- Queue and visited set store states
- Each state is (row, col, k)
- Maximum m*n*(k+1) states

Detailed Example:
grid = [[0,0,0],
        [1,1,0],
        [0,0,0]], k = 1

1. Start: (0,0,1,0)
   Queue: [(0,0,1,0)]
   Visited: {(0,0,1)}

2. Process (0,0,1,0):
   Can move to: (0,1,1,1), (1,0,0,1)
   Queue: [(0,1,1,1), (1,0,0,1)]
   
3. Process (0,1,1,1):
   Can move to: (0,2,1,2)
   Queue: [(1,0,0,1), (0,2,1,2)]
   
4. Continue until reach (2,2,x,steps)
   or exhaust all possibilities

Why BFS works:
1. First path to target is shortest
2. State tracking prevents cycles
3. k-state ensures valid obstacle removal
"""
```