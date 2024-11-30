1. Depth First Search
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
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
n is the number of columns in the 
g
r
i
d
grid.
2. Breadth First Search
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()  
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == 0
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))

        return area
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
n is the number of columns in the 
g
r
i
d
grid.
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
    
    def getSize(self, node):
        par = self.find(node)
        return self.Size[par]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or
                            nc >= COLS or grid[nr][nc] == 0
                        ):
                            continue
                            
                        dsu.union(index(r, c), index(nr, nc))

                    area = max(area, dsu.getSize(index(r, c)))

        return area
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
n is the number of columns in the 
g
r
i
d
grid.