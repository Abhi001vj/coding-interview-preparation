# https://leetcode.com/problems/surrounded-regions/description/
# 130. Surrounded Regions
# Solved
# Medium
# Topics
# Companies
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

 

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# 1. Depth First Search
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or 
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
Time & Space Complexity
Time complexity: 
O
(
m
∗
n
)
O(m∗n)
Space complexity: 
O
(
m
∗
n
)
O(m∗n)
Where 
m
m is the number of rows and 
n
n is the number of columns of the 
b
o
a
r
d
board.
2. Breadth First Search
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if (r == 0 or r == ROWS - 1 or 
                        c == 0 or c == COLS - 1 and 
                        board[r][c] == "O"
                    ):
                        q.append((r, c))
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            q.append((nr, nc))
        
        capture()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
Time & Space Complexity
Time complexity: 
O
(
m
∗
n
)
O(m∗n)
Space complexity: 
O
(
m
∗
n
)
O(m∗n)
Where 
m
m is the number of rows and 
n
n is the number of columns of the 
b
o
a
r
d
board.
3. Disjoint Set Union
class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dsu = DSU(ROWS * COLS + 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != "O":
                    continue
                if (r == 0 or c == 0 or 
                    r == (ROWS - 1) or c == (COLS - 1)
                ):
                    dsu.union(ROWS * COLS, r * COLS + c)
                else:
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if board[nr][nc] == "O":
                            dsu.union(r * COLS + c, nr * COLS + nc)

        for r in range(ROWS):
            for c in range(COLS):
                if not dsu.connected(ROWS * COLS, r * COLS + c):
                    board[r][c] = "X"
Time & Space Complexity
Time complexity: 
O
(
m
∗
n
)
O(m∗n)
Space complexity: 
O
(
m
∗
n
)
O(m∗n)
Where 
m
m is the number of rows and 
n
n is the number of columns of the 
b
o
a
r
d
board.