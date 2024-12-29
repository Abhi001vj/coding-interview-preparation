# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
# 2290. Minimum Obstacle Removal to Reach Corner
# Hard
# Topics
# Companies
# Hint
# You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

# 0 represents an empty cell,
# 1 represents an obstacle that may be removed.
# You can move up, down, left, or right from and to an empty cell.

# Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

 

# Example 1:


# Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
# Output: 2
# Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
# It can be shown that we need to remove at least 2 obstacles, so we return 2.
# Note that there may be other ways to remove 2 obstacles to create a path.
# Example 2:


# Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
# Output: 0
# Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 2 <= m * n <= 105
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 104.1K
# Submissions
# 148.8K
# Acceptance Rate
# 70.0%
# Topics
# Companies
# Hint 1
# Model the grid as a graph where cells are nodes and edges are between adjacent cells. Edges to cells with obstacles have a cost of 1 and all other edges have a cost of 0.
# Hint 2
# Could you use 0-1 Breadth-First Search or Dijkstra’s algorithm?

```python
"""
MINIMUM OBSTACLE REMOVAL USING 0-1 BFS
------------------------------------

What is 0-1 BFS?
- Special case of BFS where edge weights are only 0 or 1
- More efficient than Dijkstra's for this specific case
- Uses deque to process 0-weight edges before 1-weight edges

Comparison with Regular BFS and Dijkstra:

1. Regular BFS:
   - All edges have same weight
   - Uses simple queue
   - Time: O(V + E)

2. Dijkstra's:
   - Edges can have any weight
   - Uses priority queue
   - Time: O((V + E)logV)

3. 0-1 BFS:
   - Edges have weight 0 or 1
   - Uses deque (double-ended queue)
   - Time: O(V + E)

Example of why appendleft for weight 0:
grid = [
    [0,1,0],
    [0,1,0]
]

Step 1: At (0,0)
Queue: [(0,0,0)]  # (obstacles, row, col)
        
Grid:
[0 1 1]  # We're at (0,0)
[0 1 0]
[1 1 0]

Next moves:
(0,0) → (0,1): Cost 1 obstacle
(0,0) → (1,0): Cost 0 obstacles

Queue order:
1. (0,1,0)  # 0 obstacles, position (1,0)
2. (1,0,1)  # 1 obstacle, position (0,1)
This ensures we process all paths with fewer obstacles first!
"""

from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        """
        Distance Array Visualization:
        Initially:
        ∞ ∞ ∞
        ∞ ∞ ∞
        ∞ ∞ ∞
        
        After processing (0,0):
        0 1 ∞
        1 ∞ ∞
        ∞ ∞ ∞
        """
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Queue stores: (obstacles_removed, row, col)
        queue = deque([(0, 0, 0)])
        
        while queue:
            obstacles, row, col = queue.popleft()
            
            # Skip if we found better path
            if obstacles > dist[row][col]:
                continue
            
            # Check all 4 directions
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if (0 <= new_row < m and 
                    0 <= new_col < n):
                    """
                    Weight Decision Logic:
                    - Empty cell (0): No additional obstacle removal
                    - Obstacle (1): Need to remove it (cost 1)
                    
                    Example:
                    Current: (0,0), obstacles=0
                    Next cells:
                    - (0,1)=1: Cost 1, append right
                    - (1,0)=0: Cost 0, append left
                    """
                    new_obstacles = obstacles + grid[new_row][new_col]
                    
                    # Only update if found better path
                    if new_obstacles < dist[new_row][new_col]:
                        dist[new_row][new_col] = new_obstacles
                        # Key 0-1 BFS Logic:
                        if grid[new_row][new_col] == 0:
                            # No obstacle = weight 0 = add to front
                            queue.appendleft((new_obstacles, new_row, new_col))
                        else:
                            # Obstacle = weight 1 = add to back
                            queue.append((new_obstacles, new_row, new_col))
        
        return dist[m-1][n-1]

"""
ALTERNATIVE: DIJKSTRA'S APPROACH
------------------------------
def minimumObstacles_dijkstra(self, grid):
    m, n = len(grid), len(grid[0])
    heap = [(0, 0, 0)]  # (obstacles, row, col)
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    
    while heap:
        obstacles, row, col = heapq.heappop(heap)
        
        if (row, col) == (m-1, n-1):
            return obstacles
            
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < m and 0 <= new_col < n:
                new_obstacles = obstacles + grid[new_row][new_col]
                if new_obstacles < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_obstacles
                    heapq.heappush(heap, (new_obstacles, new_row, new_col))
                    
Time Complexities:
1. 0-1 BFS: O(V + E) where:
   - V = m * n (total cells)
   - E = 4 * m * n (each cell has 4 edges)
   
2. Dijkstra's: O((V + E)logV) where:
   - V = m * n
   - E = 4 * m * n
   - Additional logV factor from heap operations

Space Complexity for both: O(m * n)
- Distance array: m * n
- Queue/Heap: O(m * n)
"""
```

```python
"""
Grid:
[0 1 1]
[1 1 0]
[1 1 0]

0-1 BFS TRANSITIONS
------------------
Format: (obstacles, row, col)

Initial:
Queue: [(0,0,0)]
Dist:  [0,∞,∞]
       [∞,∞,∞]
       [∞,∞,∞]

Step 1: Process (0,0,0)
Check neighbors:
- Right (0,1): Obstacle, cost 1
- Down (1,0): Obstacle, cost 1
Queue: [(1,0,1), (1,1,0)]
Dist:  [0,1,∞]
       [1,∞,∞]
       [∞,∞,∞]

Step 2: Process (1,0,1)
Check neighbors:
- Right (0,2): Obstacle, cost 2
- Down (1,1): Obstacle, cost 2
Queue: [(1,1,0), (2,0,2), (2,1,1)]
Dist:  [0,1,2]
       [1,2,∞]
       [∞,∞,∞]

Step 3: Process (1,1,0)
Check neighbors:
- Right (1,1): Obstacle, cost 2
- Down (2,0): Obstacle, cost 2
Queue: [(2,0,2), (2,1,1), (2,2,0)]
Dist:  [0,1,2]
       [1,2,2]
       [2,∞,∞]

And so on until reaching (2,2)

DIJKSTRA'S TRANSITIONS
--------------------
Format: (obstacles, row, col)

Initial:
Heap: [(0,0,0)]
Dist: Same as above

Step 1: Pop (0,0,0)
Add neighbors with their costs:
- Right: (1,0,1)
- Down: (1,1,0)
Heap: [(1,0,1), (1,1,0)]  # Sorted by obstacles

Step 2: Pop (1,0,1) AND (1,1,0) together
(Same cost paths processed together in Dijkstra's)
Add their neighbors:
- Right: (2,0,2)
- Down: (2,1,1)
Heap: [(2,0,2), (2,1,1)]

KEY DIFFERENCES:
1. Queue vs Heap:
   0-1 BFS: Uses deque with appendleft for cost 0
   Dijkstra: Uses min-heap, always sorted by cost

2. Processing Order:
   0-1 BFS: Processes all paths with k obstacles before k+1
   Dijkstra: Strictly processes by increasing obstacle count

3. Time Complexity:
   0-1 BFS: O(V + E) ≈ O(mn)
   Dijkstra: O((V + E)logV) ≈ O(mn log(mn))

Example Path Formation:
[0→1→1]  Each arrow represents
[1 1 0]  movement to next cell
[1 1 0]  with obstacle count increasing
"""

# 0-1 BFS Implementation for this example
def minimumObstacles_01BFS(grid):
    m, n = len(grid), len(grid[0])
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    queue = deque([(0, 0, 0)])  # (obstacles, row, col)
    
    while queue:
        obs, row, col = queue.popleft()
        if obs > dist[row][col]:
            continue
            
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < m and 0 <= new_col < n:
                new_obs = obs + grid[new_row][new_col]
                if new_obs < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_obs
                    if grid[new_row][new_col] == 0:
                        queue.appendleft((new_obs, new_row, new_col))
                    else:
                        queue.append((new_obs, new_row, new_col))
                        
    return dist[m-1][n-1]

# Dijkstra Implementation for comparison
def minimumObstacles_dijkstra(grid):
    m, n = len(grid), len(grid[0])
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]  # (obstacles, row, col)
    
    while heap:
        obs, row, col = heappop(heap)
        if obs > dist[row][col]:
            continue
            
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < m and 0 <= new_col < n:
                new_obs = obs + grid[new_row][new_col]
                if new_obs < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_obs
                    heappush(heap, (new_obs, new_row, new_col))
                    
    return dist[m-1][n-1]
```