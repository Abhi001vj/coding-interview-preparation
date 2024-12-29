# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/
# 3286. Find a Safe Walk Through a Grid
# Medium
# Topics
# Companies
# Hint
# You are given an m x n binary matrix grid and an integer health.

# You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

# You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

# Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

# Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

 

# Example 1:

# Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

# Output: true

# Explanation:

# The final cell can be reached safely by walking along the gray cells below.


# Example 2:

# Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

# Output: false

# Explanation:

# A minimum of 4 health points is needed to reach the final cell safely.


# Example 3:

# Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

# Output: true

# Explanation:

# The final cell can be reached safely by walking along the gray cells below.



# Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 2 <= m * n
# 1 <= health <= m + n
# grid[i][j] is either 0 or 1.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 25.3K
# Submissions
# 86.9K
# Acceptance Rate
# 29.2%
# Topics
# Companies
# 0 - 3 months
# Google
# 2
# 0 - 6 months
# Bloomberg
# 2
# Hint 1
# Use 01 BFS.

"""
Problem: Find a Safe Walk Through a Grid (LeetCode 3286)

Core Challenge:
- Navigate from top-left (0,0) to bottom-right (m-1,n-1) of a binary grid
- Each cell with value 1 reduces health by 1
- Need to reach destination with health > 0
- Can move in 4 directions: up, down, left, right

Key Patterns Identified:
1. Graph Traversal (Grid as Graph)
2. Shortest Path with Constraints
3. 0-1 BFS (Binary Search)

Key Insight:
This is not a standard shortest path problem because:
1. We don't need the shortest path
2. We need to track health at each position
3. Some paths might be impossible due to health constraints

Let's analyze multiple approaches:

Approach 1: Standard BFS (Not Optimal)
Time: O(m*n*health) - visiting each cell multiple times with different health
Space: O(m*n*health) for the queue and visited set

Visual Example:
grid = [
[0,1,0]
[0,1,0]
[0,0,0]
]
health = 2

BFS Visualization (showing health at each step):
2→1→2
↓ ↓ ↓
2→1→2
↓ ↓ ↓
2→2→2

* Numbers represent health remaining when reaching that cell
* Arrows show possible movements
"""

from collections import deque
from typing import List

def is_safe_path_bfs(grid: List[List[int]], health: int) -> bool:
    """
    Standard BFS approach (not optimal)
    Time: O(m*n*health)
    Space: O(m*n*health)
    """
    if not grid or not grid[0]:
        return False
    
    m, n = len(grid), len(grid[0])
    # If health is insufficient for minimum possible damage
    if health <= 0:
        return False
        
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Queue stores: (row, col, current_health)
    queue = deque([(0, 0, health - grid[0][0])])
    # Visited set stores: (row, col, health) to avoid cycles
    visited = {(0, 0, health - grid[0][0])}
    
    while queue:
        row, col, curr_health = queue.popleft()
        
        # If reached destination with health > 0
        if row == m-1 and col == n-1 and curr_health > 0:
            return True
            
        # Try all four directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check bounds and health
            if (0 <= new_row < m and 
                0 <= new_col < n and 
                curr_health > 0):
                
                # Calculate new health after moving
                new_health = curr_health - grid[new_row][new_col]
                state = (new_row, new_col, new_health)
                
                # Only visit if new state hasn't been seen
                if new_health > 0 and state not in visited:
                    queue.append(state)
                    visited.add(state)
    
    return False

"""
Approach 2: 0-1 BFS (Optimal Solution)
Time: O(m*n) - each cell visited at most once with optimal health
Space: O(m*n) for the deque and visited set

Key Insight:
- Treat safe cells (0) and unsafe cells (1) differently
- Safe cells can be processed immediately (add to front of deque)
- Unsafe cells should be processed later (add to back of deque)
- This ensures we process paths with minimum health loss first

Visual Example:
grid = [
[0,1,0]
[0,1,0]
[0,0,0]
]
health = 2

0-1 BFS Processing Order:
1→3→5
↓ ↓ ↓
2→4→6
↓ ↓ ↓
7→8→9

* Numbers show processing order
* Safe cells (0) processed before unsafe cells (1)
"""

def is_safe_path_01bfs(grid: List[List[int]], health: int) -> bool:
    """
    0-1 BFS optimal solution
    Time: O(m*n)
    Space: O(m*n)
    """
    if not grid or not grid[0]:
        return False
    
    m, n = len(grid), len(grid[0])
    if health <= 0:
        return False
    
    # Initialize distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = grid[0][0]  # Initial health loss
    
    # Deque stores: (row, col, health_loss)
    deque_01 = deque([(0, 0, grid[0][0])])
    
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while deque_01:
        row, col, health_loss = deque_01.popleft()
        
        # Skip if we've found a better path to this cell
        if health_loss > dist[row][col]:
            continue
        
        # Try all four directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            if (0 <= new_row < m and 
                0 <= new_col < n):
                
                # Calculate new health loss
                new_loss = health_loss + grid[new_row][new_col]
                
                # Only proceed if new path is better and health sufficient
                if new_loss < dist[new_row][new_col] and new_loss < health:
                    dist[new_row][new_col] = new_loss
                    
                    # Add to front if safe cell, back if unsafe
                    if grid[new_row][new_col] == 0:
                        deque_01.appendleft((new_row, new_col, new_loss))
                    else:
                        deque_01.append((new_row, new_col, new_loss))
    
    # Check if destination reachable with sufficient health
    return dist[m-1][n-1] < health

"""
Why 0-1 BFS is Better:

1. Optimal Processing Order:
   - Processes safer paths first
   - Avoids redundant exploration
   - Guarantees minimum health loss path found first

2. Time Complexity:
   Standard BFS: O(m*n*health)
   0-1 BFS: O(m*n)
   
3. Space Complexity:
   Standard BFS: O(m*n*health)
   0-1 BFS: O(m*n)

Example Test Cases:

1. Basic case with single path:
grid = [
[0,1,0],
[0,1,0],
[0,0,0]
]
health = 2
Output: true

2. No possible path:
grid = [
[0,1,1],
[1,1,1],
[1,1,0]
]
health = 3
Output: false

3. Multiple possible paths:
grid = [
[0,0,0],
[1,1,0],
[0,0,0]
]
health = 2
Output: true
"""

# Test function to verify both implementations
def test_solutions():
    test_cases = [
        {
            "grid": [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]],
            "health": 1,
            "expected": True
        },
        {
            "grid": [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]],
            "health": 3,
            "expected": False
        },
        {
            "grid": [[1,1,1],[1,0,1],[1,1,1]],
            "health": 5,
            "expected": True
        }
    ]
    
    for i, test in enumerate(test_cases):
        bfs_result = is_safe_path_bfs(test["grid"], test["health"])
        bfs_01_result = is_safe_path_01bfs(test["grid"], test["health"])
        
        assert bfs_result == test["expected"], f"BFS failed case {i + 1}"
        assert bfs_01_result == test["expected"], f"0-1 BFS failed case {i + 1}"
        
    print("All test cases passed!")