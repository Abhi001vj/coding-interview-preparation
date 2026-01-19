# 407. Trapping Rain Water II

**Difficulty:** Hard
**Pattern:** Min-Heap (Priority Queue) / BFS (Boundary Shrinking)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

**Interview Scenario (The "Island Reservoir" Prompt):**
"We are modeling a mountainous island terrain represented by a grid of heights. Heavy rain fills all the valleys and depressions. The water eventually flows off the edge of the island into the ocean (height 0, effectively). We need to calculate the total volume of water that remains trapped in the lakes and pools formed within the island's interior. Water spills over the lowest boundary of any depression."

**Why this transformation?**
*   It emphasizes the **boundary condition**: water is held in by the *perimeter*.
*   It builds intuition: The water level of a cell is determined by the *lowest* point in the barrier surrounding it.

---

## 2. Clarifying Questions (Phase 1)

1.  **Edges:** "Does water leak from the borders?" (Yes, the grid boundary is the 'drain'. Water cannot rise higher than the lowest border cell without spilling).
2.  **Diagonals:** "Does water flow diagonally?" (No, usually 4-directional flow for grid problems).
3.  **Negative Heights:** "Are heights non-negative?" (Yes).
4.  **Input Size:** "Constraints?" ($200 \times 200$. $O(MN \log(MN))$ is acceptable).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Min-Heap (Boundary Shrinking).

**Intuition (The "Sea Level Rise" Approach):**
Imagine the outside of the grid is the ocean.
The water level starts at the height of the *lowest* cell on the boundary.
If we "walk" from the lowest boundary cell inwards:
1.  If the inner neighbor is shorter, it will definitely fill up with water to at least the current boundary level. Why? Because this boundary cell is the *lowest* exit point we've seen so far. The water can't leak out anywhere else at a lower level.
2.  If the inner neighbor is taller, it becomes a new part of the boundary (a new dam wall).

**Algorithm:**
1.  Add all boundary cells to a **Min-Heap**. Mark them as visited.
2.  Track the `current_sea_level` (initially 0).
3.  While the heap is not empty:
    *   Pop the cell with the smallest height (`h`, `r`, `c`).
    *   `current_sea_level = max(current_sea_level, h)`.
    *   Check its 4 neighbors.
    *   For each unvisited neighbor (`nh`, `nr`, `nc`):
        *   If `nh < current_sea_level`, it traps water! Volume += `current_sea_level - nh`.
        *   Push the neighbor to the heap. Crucially, push it with height `max(nh, current_sea_level)` (or just its raw height, and handle the max logic at pop time. Standard approach is to effectively "raise" the neighbor's height to the water level if it was submerged).
        *   Mark as visited.

---

## 4. Base Template & Modification

**Standard Dijkstra/Prim Template:**
```python
heap = [(start_cost, start_node)]
while heap:
    cost, node = heapq.heappop(heap)
    for neighbor in adj[node]:
        if not visited:
            heapq.heappush(heap, (new_cost, neighbor))
```

**Modified Logic:**
*   Start with *all* border cells.
*   Cost function is simply height.
*   Volume logic inside the loop.

---

## 5. Optimal Solution

```python
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
            
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        # 1. Add all boundary cells to the Min-Heap
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True
                    
        total_water = 0
        current_sea_level = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # 2. Process cells from the outside in (lowest wall first)
        while min_heap:
            height, r, c = heapq.heappop(min_heap)
            
            # The water level is determined by the max height encountered on the path 
            # from the boundary to the current cell.
            current_sea_level = max(current_sea_level, height)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    neighbor_height = heightMap[nr][nc]
                    
                    # If the neighbor is lower than the current water level, it traps water
                    if neighbor_height < current_sea_level:
                        total_water += (current_sea_level - neighbor_height)
                    
                    # Push the neighbor to the heap.
                    # IMPORTANT: The effective height of this cell becomes max(neighbor_height, current_sea_level)
                    # because it is now filled with water up to that level, acting as a wall for inner cells.
                    # We can push just neighbor_height and let the `max` logic at the top of the loop handle it, 
                    # OR push the filled height. Pushing raw height is cleaner if logic is consistent.
                    # Let's push raw height and let `current_sea_level = max(...)` handle it.
                    heapq.heappush(min_heap, (neighbor_height, nr, nc))
                    visited[nr][nc] = True
                    
        return total_water
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(MN \log(MN))$
    *   Each cell is pushed onto the heap exactly once.
    *   Heap insertion/deletion takes $O(\log(\text{heap size}))$. Heap size is at most $MN$.
*   **Space Complexity:** $O(MN)$
    *   Visited array and heap.

---

## 7. Follow-up & Extensions

**Q: Why doesn't simple DFS/BFS work?**
**A:** Simple DFS doesn't guarantee we enter a cell from its *lowest* boundary. We might enter a valley from a high wall, think we can fill it to the brim, but there's a leak on the other side (a lower wall) we haven't seen yet. The Min-Heap ensures we always process the "leak" (lowest wall) first.

**Q: 1D Version (Trapping Rain Water I)?**
**A:** Two Pointers approach ($O(N)$) is optimal there. The Heap approach works for 1D too but is overkill ($O(N \log N)$).

```