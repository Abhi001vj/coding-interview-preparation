# https://leetcode.com/problems/number-of-islands/description/
# 200. Number of Islands
# Medium
# Topics
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r: int, c: int):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr, dc in directions:
                    r, c = row + dr , col + dc
                    if (0 <= r < rows) and (0 <= c < cols) and grid[r][c] == '1' and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        def dfs(r: int, c: int):
            # Check bounds and if it's a land cell
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] != "1"):
                return
            
            # Mark as visited by changing to "0"
            grid[r][c] = "0"
            
            # Check all 4 directions
            dfs(r+1, c)  # down
            dfs(r-1, c)  # up
            dfs(r, c+1)  # right
            dfs(r, c-1)  # left
        
        # Iterate through each cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1  # Found new island
                    dfs(r, c)    # Mark all connected land
        
        return islands

"""
Visual example of how it works:

Example 1:
Initial grid:
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0

Process:
1. Find first '1' at (0,0)
2. DFS marks all connected '1's as '0':

After first DFS:
0 0 0 0 0    <- All connected 1s become 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

Islands count = 1

Example 2:
Initial grid:
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

Process:
1. First island (top-left):
0 0 0 0 0    <- First DFS marks these
0 0 0 0 0
0 0 1 0 0    <- Second island remains
0 0 0 1 1    <- Third island remains
Islands = 1

2. Second island (middle):
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0    <- Second DFS marks this
0 0 0 1 1    <- Third island remains
Islands = 2

3. Third island (bottom-right):
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0    <- Final DFS marks these
Islands = 3

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols) for recursion stack in worst case
"""