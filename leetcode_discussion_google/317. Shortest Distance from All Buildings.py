<!-- https://leetcode.com/problems/shortest-distance-from-all-buildings/description/
317. Shortest Distance from All Buildings
Hard
Topics
Companies
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

Example 1:


Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
188.5K
Submissions
431.7K
Acceptance Rate
43.7%
Topics
Companies
0 - 3 months
Meta
5
DoorDash
3
Google
2
Microsoft
2
0 - 6 months
Apple
2
Zenefits
2
6 months ago
Amazon
2
ByteDance
2
TikTok
2
Snap
2 -->

"""
SHORTEST DISTANCE FROM ALL BUILDINGS

Key Insights:
1. Need to find distances from each building to all empty lands
2. Use BFS from each building
3. Track total distances and accessibility for each empty land

Visualization of Example:
[[1,0,2,0,1],
 [0,0,0,0,0],
 [0,0,1,0,0]]

Buildings: (0,0), (0,4), (2,2)
Obstacle: (0,2)

BFS Process for first building (0,0):
Step 1:
1 [1][0][2][0][1]  Initial state
  0  1  2  3  4
0 B  1  X  1  B    B: Building
1 1  2  3  2  1    X: Obstacle
2 2  3  B  3  2    Numbers: Distance

BFS for second building and third building...
Then sum up distances for each empty land.
"""

from collections import deque
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
            
        rows, cols = len(grid), len(grid[0])
        total_buildings = sum(cell == 1 for row in grid for cell in row)
        
        # For each empty land:
        # - distances[i][j] stores total distance to all buildings
        # - reach_count[i][j] stores number of buildings that can reach this point
        distances = [[0] * cols for _ in range(rows)]
        reach_count = [[0] * cols for _ in range(rows)]
        
        def bfs(row: int, col: int) -> None:
            """
            BFS from building at (row, col) to find distances to all empty lands
            
            Visualization of BFS:
            * represents current position
            # represents visited positions
            [] represents queue positions
            
            Start from building:
            1 0 2 0 1
            * [ ] [ ]
              [ ] [ ]
                1
            """
            visited = set()
            queue = deque([(row, col, 0)])  # (row, col, distance)
            visited.add((row, col))
            
            while queue:
                curr_row, curr_col, dist = queue.popleft()
                
                # Check all 4 directions
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    next_row, next_col = curr_row + dx, curr_col + dy
                    
                    if (0 <= next_row < rows and 
                        0 <= next_col < cols and 
                        (next_row, next_col) not in visited and 
                        grid[next_row][next_col] == 0):
                        
                        # Update total distance and reach count
                        distances[next_row][next_col] += dist + 1
                        reach_count[next_row][next_col] += 1
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col, dist + 1))
        
        # Run BFS from each building
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    bfs(i, j)
        
        # Find minimum total distance among all valid empty lands
        min_distance = float('inf')
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == 0 and 
                    reach_count[i][j] == total_buildings):
                    min_distance = min(min_distance, distances[i][j])
        
        return min_distance if min_distance != float('inf') else -1

"""
Step-by-step process for example:
grid = [[1,0,2,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]]

1. Count buildings: total_buildings = 3

2. BFS from first building (0,0):
   distances after first BFS:
   B 1 X 3 4
   1 2 3 4 5
   2 3 4 5 6

3. BFS from second building (0,4):
   Updated distances:
   B 5 X 3 B
   5 4 3 2 1
   6 5 4 3 2

4. BFS from third building (2,2):
   Final distances:
   B  5  X  3  B
   5  4  3  2  1
   6  5  B  3  2

5. Find minimum valid distance:
   - Must be reachable from all buildings
   - Must be an empty land (0)
   - Answer: 7 at position (1,2)

Time Complexity: O(B * M * N) where:
- B is number of buildings
- M, N are grid dimensions
- Each BFS takes O(M * N)

Space Complexity: O(M * N) for:
- distances array
- reach_count array
- BFS queue and visited set
"""