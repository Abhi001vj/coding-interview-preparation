# https://leetcode.com/problems/rotate-image/description/
# 48. Rotate Image
# Medium
# Topics
# Companies
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


```python
"""
Matrix Rotation (90 Degrees Clockwise) - Comprehensive Solution
===========================================================

Core Concept:
-----------
To rotate a matrix 90° clockwise in-place, we can use two steps:
1. Transpose the matrix (flip across main diagonal)
2. Reverse each row

Visual Example for 3x3 Matrix:
Original:     After Transpose:    After Row Reverse:
1 2 3         1 4 7              7 4 1
4 5 6   ->    2 5 8      ->      8 5 2
7 8 9         3 6 9              9 6 3

The key insight is that we can break down the complex rotation into simpler operations.
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix 90 degrees clockwise in-place.
        
        Time Complexity: O(n²) where n is the side length
        Space Complexity: O(1) as we modify in-place
        
        Visual explanation for each step using 3x3 matrix:
        
        Step 1 - Original:
        1  2  3
        4  5  6
        7  8  9
        
        Step 2 - After transpose:
        1  4  7
        2  5  8
        3  6  9
        
        Step 3 - After row reversal:
        7  4  1
        8  5  2
        9  6  3
        """
        n = len(matrix)
        
        # Step 1: Transpose matrix
        # We only need to process upper triangle to avoid double swapping
        for i in range(n):
            for j in range(i, n):
                # Swap matrix[i][j] with matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
            
    def rotate_four_way_swap(self, matrix: List[List[int]]) -> None:
        """
        Alternative solution using four-way rotation.
        Process matrix in layers, rotating four elements at a time.
        
        Time Complexity: O(n²)
        Space Complexity: O(1)
        
        Visual explanation of one four-way swap:
        [1] → [3]    The four corners of current square
         ↑     ↓     are rotated in a single operation
        [4] ← [2]
        """
        n = len(matrix)
        
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            
            for i in range(first, last):
                offset = i - first
                
                # Save top element
                top = matrix[first][i]
                
                # Move left to top
                matrix[first][i] = matrix[last-offset][first]
                
                # Move bottom to left
                matrix[last-offset][first] = matrix[last][last-offset]
                
                # Move right to bottom
                matrix[last][last-offset] = matrix[i][last]
                
                # Move top to right
                matrix[i][last] = top

def visualize_rotation(matrix: List[List[int]]) -> None:
    """
    Helper function to visualize the rotation process.
    """
    def print_matrix(mat, step):
        print(f"\n{step}:")
        for row in mat:
            print(" ".join(f"{x:2d}" for x in row))
    
    n = len(matrix)
    
    # Print original
    print_matrix(matrix, "Original Matrix")
    
    # Create copy for visualization
    temp = [row[:] for row in matrix]
    
    # Show transpose step
    for i in range(n):
        for j in range(i, n):
            temp[i][j], temp[j][i] = temp[j][i], temp[i][j]
    print_matrix(temp, "After Transpose")
    
    # Show row reversal step
    for i in range(n):
        temp[i].reverse()
    print_matrix(temp, "After Row Reversal (Final Result)")

def demonstrate_solutions():
    """
    Test and demonstrate both rotation approaches.
    """
    test_cases = [
        [[1,2,3],
         [4,5,6],
         [7,8,9]],
        
        [[5,1,9,11],
         [2,4,8,10],
         [13,3,6,7],
         [15,14,12,16]]
    ]
    
    solution = Solution()
    
    for matrix in test_cases:
        print("\nTesting matrix:")
        matrix_copy = [row[:] for row in matrix]
        
        # Visualize the process
        visualize_rotation(matrix_copy)
        
        # Perform actual rotation
        solution.rotate(matrix)
        print("\nFinal result using transpose method:")
        for row in matrix:
            print(row)
            
        # Reset matrix and try alternative method
        matrix = [row[:] for row in matrix_copy]
        solution.rotate_four_way_swap(matrix)
        print("\nFinal result using four-way swap:")
        for row in matrix:
            print(row)

if __name__ == "__main__":
    demonstrate_solutions()

"""
Key Insights and Patterns:
------------------------
1. Matrix Transformation Patterns:
   - Transpose + Reverse = 90° Rotation
   - Layer by Layer processing
   - Four-way element swapping
   - In-place modifications

2. Implementation Techniques:
   - Using matrix symmetry
   - Processing layers from outside in
   - Careful index manipulation
   - Minimizing extra space usage

3. Common Pitfalls:
   - Double swapping in transpose
   - Incorrect layer boundaries
   - Index calculation errors
   - Wrong rotation direction

4. Optimization Strategies:
   - Combine operations where possible
   - Use index math to avoid extra variables
   - Leverage matrix properties
   - Minimize array access
"""
```

I've provided two different approaches to solve this problem:

1. **Transpose and Reverse Method**:
   - More intuitive to understand
   - Breaks problem into two simple steps
   - Easier to verify correctness
   - Good for explaining in interviews

2. **Four-way Swap Method**:
   - More direct approach
   - Processes matrix in layers
   - Requires careful index management
   - More efficient in terms of operations

Key points to understand:
1. The relationship between transpose and rotation
2. How to process matrix elements in-place
3. The pattern of element movement in rotation
4. Edge cases and boundary conditions

Would you like me to explain any specific part in more detail or provide additional examples?