# 48. Rotate Image

**Difficulty:** Medium
**Pattern:** Matrix Manipulation / Math

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

**Interview Scenario (The "Buffer Constraint" Prompt):**
"You are writing a low-level graphics driver for an embedded device with extremely limited memory. You have a square pixel buffer. You need to rotate the image 90 degrees clockwise for portrait/landscape switching. Because memory is tight, you cannot allocate a secondary buffer of the same size. You must perform the operation using only the existing memory (plus a few constant variables)."

**Why this transformation?**
*   It forces the **In-Place** constraint immediately.
*   It removes the temptation to just do `new_matrix[j][n-1-i] = old_matrix[i][j]`.

---

## 2. Clarifying Questions (Phase 1)

1.  **Direction:** "Clockwise or Counter-Clockwise?" (Clockwise).
2.  **Dimensions:** "Is it always square ($N \times N$)?" (Yes).
3.  **Data Type:** "Integers, Floats, or Objects?" (Integers/Pixels, doesn't matter for logic).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Transpose and Reverse.

**The Math Trick:**
Rotating a matrix 90 degrees clockwise is mathematically equivalent to two simpler operations performed in sequence:
1.  **Transpose:** Flip across the main diagonal ($[i][j] \leftrightarrow [j][i]$).
2.  **Reverse Rows:** Flip each row horizontally ($[i][j] \leftrightarrow [i][n-1-j]$).

Alternatively:
1.  **Reverse Rows** (Flip upside down).
2.  **Transpose**.
This results in Counter-Clockwise? Or different?
Let's trace:
`[[1,2], [3,4]]`
Transpose -> `[[1,3], [2,4]]`
Rev Rows -> `[[3,1], [4,2]]` (This is 90 deg clockwise: 1 moved from top-left to top-right... wait.
Original:
1 2
3 4

Target (90 deg CW):
3 1
4 2

My trace: `[[3,1], [4,2]]`. Correct.
So **Transpose + Reverse Rows = 90 deg Clockwise**.

**Cycle method:**
We can also move pixels in groups of 4:
`Top-Left -> Top-Right -> Bottom-Right -> Bottom-Left -> Top-Left`.
This is harder to implement (index heavy) but also $O(1)$ space. Transpose+Reverse is cleaner code.

---

## 4. Base Template & Modification

**Transpose Template:**
```python
for i in range(n):
    for j in range(i + 1, n): # Only traverse upper triangle to avoid double swap
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

**Reverse Template:**
```python
for row in matrix:
    row.reverse()
```

---

## 5. Optimal Solution

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Step 1: Transpose (Swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        # After transpose, the first column is the first row. 
        # We need that first row to be the last column for 90 deg rotation.
        # Wait, let's re-verify the logic.
        # Original: 
        # 1 2 3
        # 4 5 6
        # 7 8 9
        
        # Transpose:
        # 1 4 7
        # 2 5 8
        # 3 6 9
        
        # Reverse Rows:
        # 7 4 1
        # 8 5 2
        # 9 6 3
        
        # Target (90 CW):
        # 7 4 1
        # 8 5 2
        # 9 6 3
        # Logic holds.
        
        for i in range(n):
            matrix[i].reverse()
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N^2)$
    *   Transpose traverses approx $N^2/2$ elements.
    *   Reverse traverses $N^2$ elements.
    *   Total is proportional to total pixels.
*   **Space Complexity:** $O(1)$
    *   In-place modifications only.

---

## 7. Follow-up & Extensions

**Q: Rotate Counter-Clockwise?**
**A:** Transpose first, then **Reverse Columns** (or Reverse Rows *then* Transpose).
Actually:
Original:
1 2
3 4
Target (90 CCW):
2 4
1 3
Transpose:
1 3
2 4
Reverse Columns (top to bottom flip? No, `matrix[::-1]`):
2 4
1 3
Yes. **Transpose + Reverse Matrix (rows order)** = CCW.

**Q: Rotate 180 degrees?**
**A:** Rotate 90 twice. Or: Reverse Rows + Reverse Columns (Flip Vertical + Flip Horizontal).

```