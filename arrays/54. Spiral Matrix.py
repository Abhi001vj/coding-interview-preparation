# https://leetcode.com/problems/spiral-matrix/description/
# 54. Spiral Matrix
# Medium
# Topics
# Companies
# Hint
# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n  = len(matrix), len(matrix[0])
        ans = []
        i, j = 0,0
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        direction = RIGHT

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1

        while len(ans) != m*n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                RIGHT_WALL -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                DOWN_WALL -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                LEFT_WALL += 1
                direction = UP
            else:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1

                i, j = i + 1, j + 1
                UP_WALL += 1
                direction = RIGHT

        return ans
    
```python
"""
Spiral Matrix Problem - Comprehensive Solution
===========================================

Problem Understanding:
-------------------
For a given m×n matrix, we need to traverse it in a spiral order from outside to inside.
The spiral goes: right → down → left → up, and repeats inward.

Visual Example:
-------------
Input Matrix:
[1, 2, 3]    Spiral Path:
[4, 5, 6] →  1 → 2 → 3 → 6 → 9 → 8 → 7 → 4 → 5
[7, 8, 9]

Traversal Pattern:
→ → →  First we go right
↓      Then down
←  ←   Then left
↑      Then up
→ →    Then right again (inner layer)
"""

from typing import List

class SpiralMatrix:
    def approach1_boundary_traversal(self, matrix: List[List[int]]) -> List[int]:
        """
        Layer-by-Layer Boundary Traversal Approach
        ----------------------------------------
        Strategy: Traverse the matrix layer by layer from outside to inside.
        For each layer, go: right → down → left → up
        
        Time Complexity: O(m*n) - visit each element once
        Space Complexity: O(1) - output array not counted
        
        Visual example for 3×3 matrix:
        Layer 1:    Layer 2:
        → → →      ⬚ ⬚ ⬚
        ↓   ↑  →   ⬚ 5 ⬚
        ↓ ← ↑      ⬚ ⬚ ⬚
        """
        if not matrix:
            return []
            
        result = []
        left, right = 0, len(matrix[0]) - 1  # Column boundaries
        top, bottom = 0, len(matrix) - 1      # Row boundaries
        
        while left <= right and top <= bottom:
            # Traverse right: (top, left) → (top, right)
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # Traverse down: (top, right) → (bottom, right)
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:  # Check if there are remaining rows
                # Traverse left: (bottom, right) → (bottom, left)
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            if left <= right:  # Check if there are remaining columns
                # Traverse up: (bottom, left) → (top, left)
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
                
        return result

    def approach2_direction_array(self, matrix: List[List[int]]) -> List[int]:
        """
        Direction Array Approach
        ----------------------
        Strategy: Use direction arrays to control movement.
        Change direction when we hit a boundary or visited cell.
        
        Time Complexity: O(m*n) - visit each element once
        Space Complexity: O(m*n) - visited array
        
        Direction Changes:
        right (0) → down (1) → left (2) → up (3) → right (0)
        """
        if not matrix:
            return []
            
        m, n = len(matrix), len(matrix[0])
        result = []
        visited = [[False] * n for _ in range(m)]
        
        # Direction arrays for [right, down, left, up]
        dr = [0, 1, 0, -1]  # Row changes
        dc = [1, 0, -1, 0]  # Column changes
        
        # Starting position and direction
        r = c = d = 0       # Start at (0,0) going right
        
        for _ in range(m * n):  # Total elements to visit
            result.append(matrix[r][c])
            visited[r][c] = True
            
            # Check next position
            new_r = r + dr[d]
            new_c = c + dc[d]
            
            # Change direction if we hit boundary or visited cell
            if (new_r < 0 or new_r >= m or 
                new_c < 0 or new_c >= n or 
                visited[new_r][new_c]):
                d = (d + 1) % 4  # Rotate direction
                new_r = r + dr[d]
                new_c = c + dc[d]
                
            r, c = new_r, new_c
            
        return result

def demonstrate_solutions():
    """
    Demonstrate both approaches with examples and visualizations.
    """
    test_cases = [
        ([[1,2,3],
          [4,5,6],
          [7,8,9]], "3×3 Square Matrix"),
          
        ([[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]], "3×4 Rectangle Matrix"),
          
        ([[1]], "1×1 Matrix"),
        
        ([[1,2],
          [3,4]], "2×2 Matrix")
    ]
    
    solver = SpiralMatrix()
    
    for matrix, desc in test_cases:
        print(f"\nTesting {desc}:")
        print("Input Matrix:")
        for row in matrix:
            print(row)
            
        result1 = solver.approach1_boundary_traversal(matrix)
        result2 = solver.approach2_direction_array(matrix)
        
        print("Boundary Traversal Result:", result1)
        print("Direction Array Result:", result2)

if __name__ == "__main__":
    demonstrate_solutions()

"""
DSA Patterns and Insights:
------------------------
1. Matrix Traversal Patterns:
   - Boundary traversal
   - Layer-by-layer processing
   - Direction array technique
   - Visited cell tracking

2. Implementation Patterns:
   - Boundary variable manipulation
   - Direction change handling
   - Edge case management
   - State tracking

3. Common Edge Cases:
   - Empty matrix
   - Single row/column
   - Square vs rectangular
   - Single element

4. Optimization Techniques:
   - Boundary updating
   - Direction arrays
   - Early termination checks
   - Efficient space usage
"""
```

Key insights about this problem:

1. **Boundary Approach**:
   - Simpler to understand and implement
   - No need for extra space
   - Good for interviews due to clarity
   - Requires careful boundary management

2. **Direction Array Approach**:
   - More general technique for matrix traversal
   - Useful for similar problems
   - Uses extra space but more flexible
   - Better for extending to different patterns

3. **Common Pitfalls**:
   - Missing elements in last row/column
   - Duplicating elements at corners
   - Incorrect boundary updates
   - Not handling rectangular matrices

Would you like me to elaborate on any specific aspect of these solutions?