# 130. Surrounded Regions

**Difficulty:** Medium
**Pattern:** Graph Traversal (DFS/BFS) on Grid

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by `'X'`. A region is captured by flipping all `'O'`s in that region to `'X'`s.

**Interview Scenario (The "Resource Contamination" Prompt):**
"Imagine a grid-based map representing a containment area. `'X'` represents solid walls, and `'O'` represents open spaces where a contagious contaminant can spread. If an open space `'O'` is completely enclosed by walls `'X'` (meaning no path leads from it to the edge of the map), that entire enclosed region becomes contaminated and needs to be marked as `'X'`. Any open space directly or indirectly connected to the edge of the map is safe. How would you identify and mark the contaminated areas efficiently?"

**Why this transformation?**
*   It provides a more intuitive context for "surrounded" (contamination spreading from the edge).
*   It explicitly states the rule: connections to the edge mean safety.

---

## 2. Clarifying Questions (Phase 1)

1.  **Dimensions:** "Can `m` or `n` be small (1x1, 1x2)?" (Yes, handle edge cases. A single 'O' is never surrounded).
2.  **Modification:** "Must I modify the input `board` in-place?" (Yes, standard for this problem).
3.  **Connectivity:** "Is it 4-directional or 8-directional?" (4-directional, typical for grid problems).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** DFS or BFS (Graph Traversal).

**The Trap:**
Thinking about finding all `'O'`s and then checking if *they* are surrounded. This is hard because you need to check paths to boundaries for each 'O'.

**The Key Insight (Reverse Thinking):**
Instead of finding surrounded 'O's, find the *un-surrounded* 'O's first. An 'O' is un-surrounded if it is on the border, OR if it is connected to an 'O' that is on the border. All other 'O's must be surrounded.

**Algorithm:**
1.  Iterate through the **borders** of the matrix.
2.  If you find an `'O'` on the border, start a DFS/BFS from that `'O'`.
3.  During the DFS/BFS, mark all connected `'O'`s with a temporary character (e.g., `'E'` for "Escaped" or "Safe").
4.  After traversing all border 'O's and their connected components:
    *   Iterate through the entire matrix.
    *   Any cell with `'E'` remains `'O'` (it was safe).
    *   Any cell with `'O'` (that wasn't marked `'E'`) is surrounded, so flip it to `'X'`.
    *   Any cell with `'X'` remains `'X'`.

---

## 4. Base Template & Modification

**Standard DFS/BFS on Grid Template:**
```python
def dfs(row, col):
    if not (0 <= row < m and 0 <= col < n) or board[row][col] != 'O':
        return
    board[row][col] = 'TEMP' # Mark as visited/processed
    dfs(row+1, col)
    dfs(row-1, col)
    dfs(row, col+1)
    dfs(row, col-1)
```

**Modified Logic:**
Apply this DFS/BFS to all border 'O's. Then, a final pass to flip.

---

## 5. Optimal Solution

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
            
        m, n = len(board), len(board[0])
        
        # Helper DFS function to mark 'O's connected to the border as 'E' (Escaped)
        def dfs(r, c):
            # Boundary checks and only proceed if it's an 'O'
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != 'O':
                return
            
            # Mark the current 'O' as escaped
            board[r][c] = 'E'
            
            # Explore 4-directionally
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Step 1: Traverse the border cells.
        # If an 'O' is found on the border, start DFS from it to mark all connected 'O's.
        
        # First and last rows
        for c in range(n):
            if board[0][c] == 'O': # Top border
                dfs(0, c)
            if board[m - 1][c] == 'O': # Bottom border
                dfs(m - 1, c)
                
        # First and last columns (skip corners already covered by row traversal)
        for r in range(1, m - 1): # Start from 1 and end at m-2 to avoid corners
            if board[r][0] == 'O': # Left border
                dfs(r, 0)
            if board[r][n - 1] == 'O': # Right border
                dfs(r, n - 1)
                
        # Step 2: Traverse the entire board again.
        # Any 'O' that remains is truly surrounded (wasn't marked 'E') -> flip to 'X'.
        # Any 'E' (escaped 'O') should be restored to 'O'.
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X' # Surrounded 'O', flip to 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O' # Escaped 'O', restore to original 'O'
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(M \times N)$
    *   The initial border traversal is $O(M+N)$.
    *   Each DFS call visits each connected cell at most once. In the worst case, all cells are 'O' and form one large connected component, so the DFS visits all $M \times N$ cells.
    *   The final pass to update the board is also $O(M \times N)$.
    *   Overall, $O(M \times N)$.
*   **Space Complexity:** $O(M \times N)$ (for recursion stack)
    *   In the worst case (a board full of 'O's), the DFS recursion stack can go as deep as $M \times N$ (a path that visits every cell without branching significantly).

---

## 7. Follow-up & Extensions

**Q: Implement using BFS instead of DFS.**
**A:** Use a `collections.deque` as a queue for BFS. The logic remains the same: add border 'O's to the queue, mark them 'E', and then process neighbors from the queue.

**Q: What if the board was 8-directionally connected?**
**A:** The `dfs` function would need to check 8 neighbors instead of 4.

**Q: What if the board contains different types of cells, and only certain types are considered "walls"?**
**A:** The conditions `board[r][c] != 'O'` and `board[r][c] == 'O'` would need to be adapted to check for the new wall/open cell types.

```