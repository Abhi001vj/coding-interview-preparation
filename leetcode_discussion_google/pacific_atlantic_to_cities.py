# Problem: Find the minimum height city from where water can flow to two given cities
# Key differences from Pacific Atlantic:
# 1. Instead of reaching oceans, we need to reach specific cities
# 2. We need to find minimum height that can reach both
# 3. Water flows from higher to lower or equal height

from typing import List, Set, Tuple
from collections import deque

class Solution:
    def findWaterSource(self, grid: List[List[int]], city1: Tuple[int, int], 
                       city2: Tuple[int, int]) -> Tuple[int, int]:
        """
        Find city with minimum height that can flow water to both target cities
        Args:
            grid: Height map where grid[r][c] represents city height
            city1: (row, col) coordinates of first target city
            city2: (row, col) coordinates of second target city
        Returns:
            (row, col) of source city with minimum height that can reach both targets
        
        Example:
        grid = [
            [5, 4, 3],
            [4, 2, 1],
            [3, 1, 2]
        ]
        city1 = (1, 1)  # height 2
        city2 = (2, 2)  # height 2
        
        Water flow visualization for height 4:
        5 4 3     5 4 3     5 4→3
        4 2 1  →  4↓2 1  →  4↓2↓1
        3 1 2     3 1 2     3→1←2
        """
        if not grid or not len(grid[0]):
            return None
            
        rows, cols = len(grid), len(grid[0])
        
        def can_flow_to_cities(start_r: int, start_c: int) -> bool:
            """Check if water can flow from start position to both cities"""
            visited = set()
            
            def dfs(r: int, c: int, target_r: int, target_c: int, 
                   curr_height: int) -> bool:
                # Base cases
                if r == target_r and c == target_c:
                    return True
                if (r < 0 or r >= rows or c < 0 or c >= cols or
                    (r, c) in visited or grid[r][c] > curr_height):
                    return False
                
                visited.add((r, c))
                # Try all 4 directions
                # Water can flow if next cell height <= current height
                next_height = grid[r][c]
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                
                for dr, dc in directions:
                    if dfs(r + dr, c + dc, target_r, target_c, next_height):
                        return True
                        
                return False
            
            # Clear visited set between searches for each city
            can_reach_city1 = dfs(start_r, start_c, city1[0], city1[1], 
                                grid[start_r][start_c])
            visited.clear()
            can_reach_city2 = dfs(start_r, start_c, city2[0], city2[1], 
                                grid[start_r][start_c])
                                
            return can_reach_city1 and can_reach_city2

        # Find minimum height city that can reach both targets
        min_height = float('inf')
        result = None
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < min_height and can_flow_to_cities(r, c):
                    min_height = grid[r][c]
                    result = (r, c)
                    
        return result

    def findWaterSourceBFS(self, grid: List[List[int]], city1: Tuple[int, int],
                          city2: Tuple[int, int]) -> Tuple[int, int]:
        """
        Follow-up: Find city that can reach both targets in shortest path
        Using bidirectional BFS from both target cities
        """
        rows, cols = len(grid), len(grid[0])
        
        def bfs_from_city(start_r: int, start_c: int) -> Set[Tuple[int, int]]:
            reachable = set()
            queue = deque([(start_r, start_c)])
            visited = {(start_r, start_c)}
            
            while queue:
                r, c = queue.popleft()
                curr_height = grid[r][c]
                reachable.add((r, c))
                
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or
                        (nr, nc) in visited or grid[nr][nc] < curr_height):
                        continue
                        
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    
            return reachable
            
        # Find cells reachable from both cities
        reachable_from_1 = bfs_from_city(city1[0], city1[1])
        reachable_from_2 = bfs_from_city(city2[0], city2[1])
        
        # Find intersection with minimum height
        common = reachable_from_1 & reachable_from_2
        if not common:
            return None
            
        return min(common, key=lambda x: grid[x[0]][x[1]])

# Test cases
def test():
    solution = Solution()
    
    # Test case 1: Simple grid
    grid1 = [
        [5, 4, 3],
        [4, 2, 1],
        [3, 1, 2]
    ]
    city1 = (1, 1)  # height 2
    city2 = (2, 2)  # height 2
    assert solution.findWaterSource(grid1, city1, city2) == (0, 1)  # height 4
    
    # Test case 2: Equal heights path
    grid2 = [
        [2, 2, 2],
        [2, 1, 2],
        [2, 2, 2]
    ]
    city1 = (1, 1)  # height 1
    city2 = (0, 0)  # height 2
    assert solution.findWaterSource(grid2, city1, city2) == (0, 0)
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()
"""
Key differences from Pacific Atlantic solution:

1. Target-based DFS:
   - Instead of checking ocean boundaries
   - We check if we reach specific target coordinates
   - Need separate DFS for each target city

2. Height constraints:
   - Original: water flows from lower to higher
   - Modified: water flows from higher to lower/equal

3. Result criteria:
   - Original: find all cells reaching both oceans
   - Modified: find minimum height cell reaching both cities

State tracking visualization:
---------------------------
Example grid:
5 4 3
4 2 1
3 1 2

For start at (0,1) height 4:
Visit sequence to city1(1,1):
5 4 3     5 4 3
4 2 1  →  4↓2 1
3 1 2     3 1 2

Visit sequence to city2(2,2):
5 4→3
4 2↓1
3 1←2

The solution works because:
1. DFS ensures we explore all possible paths
2. Height check ensures water flows correctly
3. Separate visited sets prevent path interference
4. Minimum height tracking finds optimal source
"""