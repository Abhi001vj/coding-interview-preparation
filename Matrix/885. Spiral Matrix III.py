"""
885. Spiral Matrix III (Medium)
Pattern: Matrix Traversal / Simulation

--------------------------------------------------------------------------------
PROBLEM UNDERSTANDING
--------------------------------------------------------------------------------
Starting at (r0, c0) in an R x C matrix, move in a spiral pattern,
recording visited coordinates. The pattern of movement changes direction
after 1, 1, 2, 2, 3, 3, ... steps. That is, it takes 1 step right, 1 step down,
2 steps left, 2 steps up, 3 steps right, 3 steps down, and so on.

Input: R, C, r0, c0
Output: List of [r, c] coordinates.

--------------------------------------------------------------------------------
INTUITION: The "Growing Steps" Spiral
--------------------------------------------------------------------------------
Instead of a fixed spiral, this one expands its step length.
- Right: 1 step
- Down: 1 step
- Left: 2 steps
- Up: 2 steps
- Right: 3 steps
- Down: 3 steps
- ... and so on.

The number of steps in each direction increases by 1 every two directions.

Visualize: 
Start at (r0, c0)
-> Move RIGHT 1 step
-> Move DOWN 1 step
-> Move LEFT 2 steps
-> Move UP 2 steps
-> Move RIGHT 3 steps
-> Move DOWN 3 steps
...

--------------------------------------------------------------------------------
ALGORITHM
--------------------------------------------------------------------------------
1. Initialize `ans` with `[r0, c0]`. `count = 1` (since we start at r0, c0).
2. Define directions: `dr = [0, 1, 0, -1]` (Right, Down, Left, Up)
                        `dc = [1, 0, -1, 0]`
3. Initialize `curr_r, curr_c = r0, c0`.
4. Initialize `step_len = 1`.
5. Loop until `count == R * C` (all cells visited):
   a. Iterate through 4 directions (`d` from 0 to 3).
   b. For each `d`, move `step_len` times (e.g., if `d=0`, move right `step_len` times).
      i. For each step:
         - Update `curr_r, curr_c`.
         - If `(curr_r, curr_c)` is within bounds (`0 <= curr_r < R` and `0 <= curr_c < C`):
           - Add `[curr_r, curr_c]` to `ans`.
           - Increment `count`.
   c. After moving in two directions (Right and Down, or Left and Up), increment `step_len`.
      (i.e., `step_len` increases every `d % 2 == 0` when `d` is 0, 1, 2, 3).
      Specifically, `step_len` increases after directions 0 (Right), 2 (Left), 4 (Right), ...
      So, it increases after processing directions `d=0` and `d=2`. This can be simplified by checking `d % 2 == 0` for `d` in [0, 1, 2, 3].
      No, `step_len` increases after 2 directions. The logic should be: `step_len` increases if `d` is 0 or 2.
      A simpler way: increment `step_len` AFTER every 2 directions (Right, Down -> len=2; Left, Up -> len=3).
      So, `step_len` increments after direction `d=1` and `d=3`. This means after `d=1` we use `step_len` 2 times, then after `d=3` we use `step_len` 3 times.
      Let's use `k` for `step_len` and update it after every two directions.
      `k = 1` for `d=0, d=1`
      `k = 2` for `d=2, d=3`
      `k = 3` for `d=0, d=1` (next iteration)
      This means `k` increases when `d` is `0` or `2` (after completing 2 directions).

Complexity: O(R * C) Time, O(R * C) Space.
--------------------------------------------------------------------------------
"""

from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r0: int, c0: int) -> List[List[int]]:
        ans = [[r0, c0]]
        count = 1
        
        curr_r, curr_c = r0, c0
        
        # Directions: Right, Down, Left, Up
        dr = [0, 1, 0, -1] # Change in row
        dc = [1, 0, -1, 0] # Change in col
        
        step_len = 0 # Current step length for movement
        d_idx = 0    # Current direction index
        
        while count < rows * cols:
            # After every two directions, increment step_len
            # E.g., after Right (d_idx=0) and Down (d_idx=1), step_len increases.
            # So, step_len increases when d_idx is 0 or 2
            if d_idx == 0 or d_idx == 2:
                step_len += 1
            
            # Move `step_len` times in current direction
            for _ in range(step_len):
                curr_r += dr[d_idx]
                curr_c += dc[d_idx]
                
                if 0 <= curr_r < rows and 0 <= curr_c < cols:
                    ans.append([curr_r, curr_c])
                    count += 1
            
            d_idx = (d_idx + 1) % 4 # Move to next direction
            
        return ans

if __name__ == "__main__":
    sol = Solution()
    R, C, r0, c0 = 1, 4, 0, 0
    print(f"R={R}, C={C}, r0={r0}, c0={c0} -> {sol.spiralMatrixIII(R, C, r0, c0)}")
    # Expected: [[0,0],[0,1],[0,2],[0,3]]
    
    R, C, r0, c0 = 5, 6, 1, 1
    print(f"R={R}, C={C}, r0={r0}, c0={c0} -> {sol.spiralMatrixIII(R, C, r0, c0)}")
    # Expected: [[1,1],[1,2],[1,3],[1,0],[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[4,4],[4,3],[4,2],[4,1],[4,0],[3,0],[2,0],[1,0],[0,0],[0,1],[0,2],[0,3],[0,4],[0,5]]
