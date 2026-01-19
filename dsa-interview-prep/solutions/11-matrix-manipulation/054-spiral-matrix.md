# 54. Spiral Matrix

**Difficulty:** Medium
**Pattern:** Matrix Traversal

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an `m x n` matrix, return all elements of the matrix in spiral order.

**Interview Scenario (The "Robot Navigation" Prompt):**
"Imagine you have a robot exploring a rectangular grid (like a warehouse floor or a data center rack). The robot must visit every cell exactly once, starting from the top-left, and moving in a spiral path (right, down, left, up, then inward). Record the order in which the robot visits each cell. How would you program the robot's movement?"

**Why this transformation?**
* It frames the problem as a physical traversal, making the boundary conditions and direction changes more intuitive.
* It emphasizes visiting each cell once.

---

## 2. Clarifying Questions (Phase 1)

1.  **Dimensions:** "Can `m` or `n` be 0? What if it's a single row or single column?" (Handle empty, single row/column cases).
2.  **Direction:** "Always clockwise spiral?" (Yes).
3.  **Output:** "Return a list of elements?" (Yes).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Boundary Traversal / Simulation.

**The Logic:**
We can simulate the robot's movement by keeping track of four boundaries: `top`, `bottom`, `left`, `right`. The robot traverses one layer of the spiral, then shrinks the boundaries and repeats until `top > bottom` or `left > right`.

**Steps per layer:**
1.  **Go Right:** From `(top, left)` to `(top, right)`. Increment `top`.
2.  **Go Down:** From `(top, right)` to `(bottom, right)`. Decrement `right`.
3.  **Go Left:** From `(bottom, right)` to `(bottom, left)`. Decrement `bottom`.
4.  **Go Up:** From `(bottom, left)` to `(top, left)`. Increment `left`.

**Crucial Edge Case:** For step 3 and 4, ensure `top <= bottom` and `left <= right` *before* execution. This handles single-row/single-column remaining layers correctly.

---

## 4. Base Template & Modification

**Standard Iterative Traversal Template:**
```python
result = []
top, bottom = 0, len(matrix) - 1
left, right = 0, len(matrix[0]) - 1

while top <= bottom and left <= right:
    # Logic for each direction
    # Update boundaries
    # Handle single row/column remaining
```

**Modified Logic:**
Implement the four distinct traversal phases within the loop.

---

## 5. Optimal Solution

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or not matrix[0]:
            return result
            
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse Right (from left to right along top row)
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1 # Move top boundary down
            
            # 2. Traverse Down (from top to bottom along right column)
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1 # Move right boundary left
            
            # IMPORTANT: Check boundaries again before traversing left and up
            # This prevents double counting for single row/column remaining cases
            if top <= bottom:
                # 3. Traverse Left (from right to left along bottom row)
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1 # Move bottom boundary up
            
            if left <= right:
                # 4. Traverse Up (from bottom to top along left column)
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1 # Move left boundary right
                
        return result
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(M \times N)$
    *   Every element in the matrix is visited exactly once.
*   **Space Complexity:** $O(1)$ (excluding output list)
    *   We use a constant amount of extra variables for boundaries and indices.

---

## 7. Follow-up & Extensions

**Q: What if the spiral order needs to fill a matrix (e.g., generate a spiral matrix)?**
**A:** The same boundary traversal logic applies, but instead of `append`, you would assign values to `matrix[row][col]` in the order of traversal.

**Q: Print the matrix in a different spiral direction (e.g., counter-clockwise or inward-out)?**
**A:** The order of the four traversal loops and the direction of pointer updates would change.

```