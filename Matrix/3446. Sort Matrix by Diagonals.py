"""
3446. Sort Matrix by Diagonals (Medium)
Pattern: Matrix Traversal / Sorting

--------------------------------------------------------------------------------
PROBLEM UNDERSTANDING
--------------------------------------------------------------------------------
Sort the diagonals of an n x n matrix:
1. Bottom-Left Triangle (row >= col): Sort DESCENDING.
2. Top-Right Triangle (row < col): Sort ASCENDING.

--------------------------------------------------------------------------------
VISUALIZATION: DIAGONAL IDENTIFICATION
--------------------------------------------------------------------------------
A diagonal is defined by (row - col) = constant.
Example 3x3:

(0,0) (0,1) (0,2)   Diffs:  0  -1  -2
(1,0) (1,1) (1,2)           1   0  -1
(2,0) (2,1) (2,2)           2   1   0

- Diffs >= 0: Bottom-Left (Desc)
- Diffs < 0: Top-Right (Asc)

--------------------------------------------------------------------------------
ALGORITHM
--------------------------------------------------------------------------------
1. Collect elements for each diagonal using a Hash Map: 
   key = (row - col), value = list of elements.
2. Sort each list:
   - If key >= 0: Sort Reverse (Descending).
   - If key < 0: Sort Normal (Ascending).
3. Put elements back into the matrix.

Complexity: O(N^2 log N) due to sorting diagonals. Space O(N^2).
--------------------------------------------------------------------------------
"""

from typing import List
from collections import defaultdict

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)
        
        # 1. Collect
        for r in range(n):
            for c in range(n):
                diagonals[r - c].append(grid[r][c])
        
        # 2. Sort
        for diff, vals in diagonals.items():
            if diff >= 0:
                vals.sort(reverse=True) # Bottom-left: Descending
            else:
                vals.sort()             # Top-right: Ascending
        
        # 3. Place back
        # We need an iterator to pop elements efficiently
        iterators = {k: iter(v) for k, v in diagonals.items()}
        
        for r in range(n):
            for c in range(n):
                grid[r][c] = next(iterators[r - c])
                
        return grid

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,7,3],[9,8,2],[4,5,6]]
    # Diagonals:
    # 0: [1, 8, 6] -> Desc [8, 6, 1]
    # 1: [9, 5]    -> Desc [9, 5]
    # 2: [4]       -> Desc [4]
    # -1: [7, 2]   -> Asc [2, 7]
    # -2: [3]      -> Asc [3]
    print(sol.sortMatrix(grid))
