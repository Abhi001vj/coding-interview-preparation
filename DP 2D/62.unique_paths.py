# https://leetcode.com/problems/unique-paths/description/
# 62. Unique Paths
# Solved
# Medium
# Topics
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100
"""
3x7 Grid Visualization:
[0,0][0,1][0,2][0,3][0,4][0,5][0,6]
[1,0][1,1][1,2][1,3][1,4][1,5][1,6]
[2,0][2,1][2,2][2,3][2,4][2,5][2,6]

1. Two-Array Approach (First Version):
-----------------------------------
Initial state (bottom row - row 2):
row = [1, 1, 1, 1, 1, 1, 1]

Step 1: Processing middle row (row 1)
Previous row:  [1, 1, 1, 1, 1, 1, 1]
New row starts: [1, 1, 1, 1, 1, 1, 1]

Processing right to left:
Position [1,5]: newRow[5] = newRow[6](1) + row[5](1) = 2
Position [1,4]: newRow[4] = newRow[5](2) + row[4](1) = 3
Position [1,3]: newRow[3] = newRow[4](3) + row[3](1) = 4
Position [1,2]: newRow[2] = newRow[3](4) + row[2](1) = 5
Position [1,1]: newRow[1] = newRow[2](5) + row[1](1) = 6
Position [1,0]: newRow[0] = newRow[1](6) + row[0](1) = 7

After step 1: newRow = [7, 6, 5, 4, 3, 2, 1]

Step 2: Processing top row (row 0)
Previous row: [7, 6, 5, 4, 3, 2, 1]
New row starts: [1, 1, 1, 1, 1, 1, 1]

Position [0,5]: newRow[5] = newRow[6](1) + row[5](2) = 3
Position [0,4]: newRow[4] = newRow[5](3) + row[4](3) = 6
Position [0,3]: newRow[3] = newRow[4](6) + row[3](4) = 10
Position [0,2]: newRow[2] = newRow[3](10) + row[2](5) = 15
Position [0,1]: newRow[1] = newRow[2](15) + row[1](6) = 21
Position [0,0]: newRow[0] = newRow[1](21) + row[0](7) = 28

Final result: 28 paths

2. Single-Array Approach (Optimal Version):
---------------------------------------
Initial state:
dp = [1, 1, 1, 1, 1, 1, 1]

Step 1: Processing middle row
Initial: [1, 1, 1, 1, 1, 1, 1]
After j=5: [1, 1, 1, 1, 1, 2, 1]
After j=4: [1, 1, 1, 1, 3, 2, 1]
After j=3: [1, 1, 1, 4, 3, 2, 1]
After j=2: [1, 1, 5, 4, 3, 2, 1]
After j=1: [1, 6, 5, 4, 3, 2, 1]
After j=0: [7, 6, 5, 4, 3, 2, 1]

Step 2: Processing top row
Initial: [7, 6, 5, 4, 3, 2, 1]
After j=5: [7, 6, 5, 4, 3, 3, 1]
After j=4: [7, 6, 5, 4, 6, 3, 1]
After j=3: [7, 6, 5, 10, 6, 3, 1]
After j=2: [7, 6, 15, 10, 6, 3, 1]
After j=1: [7, 21, 15, 10, 6, 3, 1]
After j=0: [28, 21, 15, 10, 6, 3, 1]

Performance Analysis:
-------------------
1. Why the single-array version is faster:

a) Memory Operations:
   Two-Array Version:
   - Creates new array for each row
   - Copies values between arrays
   - More memory allocations/deallocations
   
   Single-Array Version:
   - Uses same array throughout
   - No array copying
   - No new memory allocations

b) Cache Performance:
   Two-Array Version:
   - Works with two arrays
   - More cache misses possible
   - Higher memory bandwidth usage
   
   Single-Array Version:
   - Better cache utilization
   - Data locality is better
   - Less memory bandwidth needed

c) Operations Count:
   Two-Array Version:
   - Array creation: O(n) per row
   - Value updates: O(n) per row
   - Array assignment: O(n) per row
   
   Single-Array Version:
   - Only value updates: O(n) per row
   - No additional operations

Total Time Complexity remains O(m*n) for both, but single-array has:
- Lower constant factors
- Better memory usage
- Better cache performance
"""

"""
Grid Example (3x7):
Initial State:
S [ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ]G

Where: S = Start (0,0), G = Goal (2,6)
"""
"""
Let's understand with a 3x3 grid example:

Initial Grid (showing coordinates):
[0,0][0,1][0,2]
[1,0][1,1][1,2]
[2,0][2,1][2,2]

Key Insight: We only need to remember the values in current row and previous row 
to calculate total paths to destination from any cell.

1. First Space-Optimized Version (Two Rows):
------------------------------------------
Base case: Bottom row initialized to 1s because from any cell in bottom row, 
there's only one way to reach destination (keep going right)
row = [1, 1, 1]

Step 1: Processing second-to-last row (index 1)
Previous row (bottom): [1, 1, 1]
New row starts as:     [1, 1, 1]

Processing (right to left):
Position [1,1]: 
- Paths = paths through right cell (newRow[2]=1) + paths through cell below (row[1]=1)
- newRow[1] = 1 + 1 = 2

Position [1,0]:
- Paths = paths through right cell (newRow[1]=2) + paths through cell below (row[0]=1)
- newRow[0] = 2 + 1 = 3

After step 1: newRow = [3, 2, 1]

Step 2: Processing top row (index 0)
Previous row: [3, 2, 1]
New row starts as: [1, 1, 1]

Processing (right to left):
Position [0,1]:
- Paths = paths through right cell (newRow[2]=1) + paths through cell below (row[1]=2)
- newRow[1] = 1 + 2 = 3

Position [0,0]:
- Paths = paths through right cell (newRow[1]=3) + paths through cell below (row[0]=3)
- newRow[0] = 3 + 3 = 6

Final state: [6, 3, 1]

2. Most Optimal Version (Single Array):
------------------------------------
Same logic but updates array in-place:

Initial state (bottom row): 
dp = [1, 1, 1]

Step 1: Processing second-to-last row
For position [1,1]:
- Current value (paths from below) = 1
- Add right neighbor (1)
- dp[1] = 1 + 1 = 2

For position [1,0]:
- Current value (paths from below) = 1
- Add right neighbor (2)
- dp[0] = 1 + 2 = 3

After step 1: dp = [3, 2, 1]

Step 2: Processing top row
For position [0,1]:
- Current value (paths from below) = 2
- Add right neighbor (1)
- dp[1] = 2 + 1 = 3

For position [0,0]:
- Current value (paths from below) = 3
- Add right neighbor (3)
- dp[0] = 3 + 3 = 6

Final state: dp = [6, 3, 1]

Visual Representation of Value Dependencies:
For any cell X:
[?][X][R]  # R is right value (newRow[j+1] or dp[j+1])
[B][?][?]  # B is below value (row[j] or original dp[j])
"""

def uniquePaths1(m: int, n: int) -> int:
    # Initialize bottom row
    row = [1] * n
    
    # Process each row from second-last to top
    for i in range(m - 1):
        newRow = [1] * n
        # Process each cell right to left
        for j in range(n - 2, -1, -1):
            # Add paths from right and below
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow
    return row[0]

def uniquePaths2(m: int, n: int) -> int:
    # Initialize bottom row
    dp = [1] * n
    
    # Process each row from second-last to top
    for i in range(m - 2, -1, -1):
        # Process each cell right to left, updating in-place
        for j in range(n - 2, -1, -1):
            # Add right neighbor to current value
            dp[j] += dp[j + 1]
    return dp[0]
# 1. Recursive Solution (DFS)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Visualization of recursive calls for 3x3 grid:
        
        Step 1: Start at S(0,0)
        S [ ][ ]
        [ ][ ][ ]
        [ ][ ]G
        
        Step 2: Branch into right(0,1) and down(1,0)
        S→1[ ][ ]
        ↓ [ ][ ]
        [ ][ ]G
        
        Step 3: Further branching
        S→1→1
        ↓ ↓ ↓
        1→1→1
        ↓ ↓ ↓
        1→1→G
        
        Each number represents paths reaching that cell
        Final paths count at G = sum of all possible paths = 6
        """
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i, j + 1) + dfs(i + 1, j)
        return dfs(0, 0)

# 2. Top-Down DP (Memoization)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Visualization of memoization for 3x3 grid:
        
        Initial memo state:
        -1 -1 -1
        -1 -1 -1
        -1 -1  1
        
        After few calls:
        -1 -1  1
        -1  2  1
         1  1  1
        
        Final memo state:
         6  3  1
         3  2  1
         1  1  1
        
        Numbers show cached path counts to goal from each position
        """
        memo = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]
        return dfs(0, 0)

# 3. Bottom-Up DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Visualization of bottom-up DP for 3x3 grid:
        
        Initial state (with padding):
        0 0 0 0
        0 0 0 0
        0 0 1 0
        0 0 0 0
        
        After first row:
        0 0 0 0
        0 0 1 0
        0 1 1 0
        0 0 0 0
        
        After second row:
        0 0 0 0
        0 2 1 0
        0 1 1 0
        0 0 0 0
        
        Final state:
        0 6 3 0
        0 3 2 0
        0 1 1 0
        0 0 0 0
        
        Answer is at dp[0][0] = 6
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if not (i == m - 1 and j == n - 1):
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]


# 4. Space-Optimized DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Visualization of space-optimized DP for 3x3 grid:
        
        Initial row:
        [1, 1, 1]
        
        After processing first row:
        Previous: [1, 1, 1]
        Current:  [3, 2, 1]
        
        After processing second row:
        Previous: [3, 2, 1]
        Current:  [6, 3, 1]
        
        Only storing and updating one row at a time
        Final answer is leftmost value = 6
        """
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

# 5. Most Optimal DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Visualization of optimal DP for 3x3 grid:
        
        Initial array:
        [1, 1, 1]
        
        After first update:
        [3, 2, 1]
        
        After second update:
        [6, 3, 1]
        
        In-place updates of single array
        Values represent paths from each position in current row
        """
        dp = [1] * n
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]
        return dp[0]

# 6. Mathematical Solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Visualization of mathematical solution for 3x3 grid:
        
        Total steps needed: 
        - Right steps (n-1) = 2
        - Down steps (m-1) = 2
        - Total steps = 4
        
        We need to choose positions for 2 right steps out of 4 total steps
        OR choose positions for 2 down steps out of 4 total steps
        
        Calculation:
        C(4,2) = 4!/(2!(4-2)!)
        = (4 * 3)/(2 * 1)
        = 12/2
        = 6
        
        This directly gives us the total number of unique paths
        """
        if m == 1 or n == 1:
            return 1
        if m < n:
            m, n = n, m
            
        res = j = 1
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1
        return res