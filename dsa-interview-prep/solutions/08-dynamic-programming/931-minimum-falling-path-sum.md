# 931. Minimum Falling Path Sum

**Difficulty:** Medium
**Pattern:** Dynamic Programming (2D Grid / Bottom-Up)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an `n x n` array of integers `matrix`, return the minimum sum of any falling path through `matrix`. A falling path starts at any element in the first row and chooses one element from each row. The next element must be in a column that is different from the previous element's column by at most one. That is, if you are at `(row, col)`, your next element can be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

**Interview Scenario (The "Robot Pathfinding" Prompt):
"You have a robot navigating a grid-based environment. Each cell has a 'cost' to traverse. The robot starts at any cell in the top row and must reach any cell in the bottom row. From its current cell, it can move to the cell directly below it, or diagonally left/right below it. What is the minimum total cost for the robot to complete its journey?"

**Why this transformation?**
* It frames the problem as a pathfinding/optimization task, a common DP scenario.
* It emphasizes the "minimum sum" and "allowed moves".

---

## 2. Clarifying Questions (Phase 1)

1.  **Dimensions:** "Is it always a square matrix ($n \times n$) ?" (Yes).
2.  **Values:** "Can values be negative?" (Yes, this affects minimum sums).
3.  **Path:** "Does it have to reach *any* cell in the last row, or a specific one?" (Any cell).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Dynamic Programming (2D Grid).

**The Overlapping Subproblems / Optimal Substructure:**
The minimum falling path sum to reach `(row, col)` depends on the minimum falling path sums to reach `(row-1, col-1)`, `(row-1, col)`, and `(row-1, col+1)`.

**State Definition:**
`dp[r][c]` = minimum sum of a falling path ending at `(r, c)`.

**Recurrence Relation:**
`dp[r][c] = matrix[r][c] + min(dp[r-1][c-1], dp[r-1][c], dp[r-1][c+1])`
(Carefully handle boundary conditions for `c-1` and `c+1`).

**Base Case:**
`dp[0][c] = matrix[0][c]` (The first row's values are their own minimums).

---

## 4. Base Template & Modification

**Standard 2D DP Template (Iterating Rows):**
```python
dp = [[0] * n for _ in range(n)]
# Base case for first row
for r in range(1, n):
    for c in range(n):
        # Calculate dp[r][c] based on dp[r-1][...] and current value
return min(dp[n-1]) # Min of last row
```

**Modified Logic (In-place DP):**
We can modify the input `matrix` directly to store `dp` values, saving space.

---

## 5. Optimal Solution (In-place DP)

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # Iterate from the second row down to the last row
        # For each cell, calculate the minimum path sum to reach it
        # by considering the cells in the row above.
        for r in range(1, n):
            for c in range(n):
                # Calculate the minimum sum from the three possible cells in the previous row
                # Handle boundary conditions for columns (c-1, c, c+1)
                
                # Option 1: Directly above (r-1, c)
                min_prev_row = matrix[r-1][c]
                
                # Option 2: Diagonally left (r-1, c-1)
                if c > 0:
                    min_prev_row = min(min_prev_row, matrix[r-1][c-1])
                    
                # Option 3: Diagonally right (r-1, c+1)
                if c < n - 1:
                    min_prev_row = min(min_prev_row, matrix[r-1][c+1])
                    
                # Update the current cell's value in the matrix itself
                # (using the matrix for DP storage, saving explicit DP array space)
                matrix[r][c] += min_prev_row
                
        # The minimum falling path sum will be the minimum value in the last row
        return min(matrix[n-1])
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N^2)$
    *   Two nested loops iterate through all $N^2$ cells of the matrix once.
*   **Space Complexity:** $O(1)$ (if modifying in-place)
    *   If a separate DP table is used, it would be $O(N^2)$. Modifying in-place makes it $O(1)$ auxiliary space.

---

## 7. Follow-up & Extensions

**Q: What if paths could start from any row and end at any row?**
**A:** This would become a more complex graph problem, possibly involving all-pairs shortest path or flow algorithms, depending on constraints.

**Q: What if the matrix was rectangular ($M \times N$)?**
**A:** The logic remains the same, just iterate `r` from `0` to `M-1` and `c` from `0` to `N-1`. The boundary conditions for columns would adjust for `N`.

```