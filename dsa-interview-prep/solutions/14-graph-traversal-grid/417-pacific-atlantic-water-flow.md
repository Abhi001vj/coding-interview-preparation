# 417. Pacific Atlantic Water Flow

**Difficulty:** Medium
**Pattern:** Graph Traversal (DFS/BFS from Boundaries)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the left and top edges, and the Atlantic Ocean touches the right and bottom edges. The island is partitioned into a grid of square cells. You are given an integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at `(r, c)`. Rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean. Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to **both** the Pacific and Atlantic oceans.

**Interview Scenario (The "Continental Divide" Prompt):**
"We are analyzing the hydrology of a continent. Water flows downhill. Some water eventually reaches the West Coast (Pacific), and some reaches the East Coast (Atlantic). We want to identify the 'high ground' or the 'continental divide'—specifically, the set of all locations from which a drop of water could theoretically flow to *both* oceans."

**Why this transformation?**
*   It clarifies the goal: finding the intersection of two reachability sets.
*   It hints at the efficiency hack: instead of simulating water flowing *down* from every cell (which is slow), simulate water climbing *up* from the oceans.

---

## 2. Clarifying Questions (Phase 1)

1.  **Strict Inequality:** "Does water flow only to strictly lower cells?" (No, equal height is allowed).
2.  **Output Format:** "Does order matter?" (No).
3.  **Input Size:** "Dimensions?" ($200 \times 200$, implying $O(MN)$ is needed).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Reverse DFS/BFS.

**The Naive Approach (Downhill):**
For every cell, run a DFS to see if it reaches Pacific. Run another to see if it reaches Atlantic.
Complexity: $O((MN) \times (MN)) = O(M^2 N^2)$. Too slow.

**The Optimized Approach (Uphill/Reverse):**
Start from the ocean boundaries and flow *uphill*.
1.  **Pacific Reachable:** Start BFS/DFS from all Top and Left border cells. Move to neighbors if `neighbor_height >= current_height`. Mark reachable cells in a set `pacific_set`.
2.  **Atlantic Reachable:** Start BFS/DFS from all Bottom and Right border cells. Move to neighbors if `neighbor_height >= current_height`. Mark reachable cells in a set `atlantic_set`.
3.  **Intersection:** Iterate through all cells. If a cell is in both sets, add to result.

Complexity: $O(MN)$.

---

## 4. Base Template & Modification

**Standard Grid DFS Template:**
```python
def dfs(r, c, visited_set):
    visited_set.add((r, c))
    for dr, dc in dirs:
        # Check bounds and if neighbor >= current (uphill)
        if valid and (nr, nc) not in visited_set:
            dfs(nr, nc, visited_set)
```

**Modified Logic:**
Apply this DFS twice with different starting sets.

---

## 5. Optimal Solution

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, visited):
            visited.add((r, c))
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # Check already visited
                    if (nr, nc) in visited:
                        continue
                    
                    # REVERSE FLOW CONDITION:
                    # Water flows from (r, c) TO (nr, nc) if heights[r][c] >= heights[nr][nc].
                    # Since we are going BACKWARDS from ocean to source,
                    # we only move if heights[nr][nc] >= heights[r][c].
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)
        
        # 1. Start DFS from Pacific Borders (Top and Left)
        for c in range(n):
            dfs(0, c, pacific_reachable) # Top row
        for r in range(m):
            dfs(r, 0, pacific_reachable) # Left col
            
        # 2. Start DFS from Atlantic Borders (Bottom and Right)
        for c in range(n):
            dfs(m - 1, c, atlantic_reachable) # Bottom row
        for r in range(m):
            dfs(r, n - 1, atlantic_reachable) # Right col
            
        # 3. Find Intersection
        return list(pacific_reachable.intersection(atlantic_reachable))
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(M \times N)$
    *   We traverse the grid at most twice (once for Pacific, once for Atlantic).
*   **Space Complexity:** $O(M \times N)$
    *   To store the `visited` sets and recursion stack.

---

## 7. Follow-up & Extensions

**Q: Can we optimize space?**
**A:** We can use a single `visited` matrix with bitmasks (1 for Pacific, 2 for Atlantic, 3 for Both) to avoid hash set overhead, but asymptotic space remains $O(MN)$ due to recursion/queue.

**Q: What if we want the longest flow path?**
**A:** This becomes "Longest Increasing Path in a Matrix" (LeetCode 329), which uses DFS + Memoization.

```
