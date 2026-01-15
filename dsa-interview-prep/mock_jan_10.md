# Mock Interview - January 10, 2026

## Interview Setup
- **Duration**: 45 minutes per problem
- **Format**: Google L5 Style
- **Problems**: 5 scenarios (Graph + DP focus)
- **Environment**: No IDE, No autocomplete (simulate Google Docs)

---

# Problem 1: Flight Budget Optimizer (LC 787 - Cheapest Flights Within K Stops)

**LeetCode Link**: [https://leetcode.com/problems/cheapest-flights-within-k-stops/](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

## Google-Style Scenario Presentation

> **Interviewer**: "You're working on Google Travel. We have a feature where users want to find the cheapest flight between two cities, but they have a constraint - they can only tolerate a certain number of layovers.
>
> Given our flight network, help users find the cheapest route. Oh, and sometimes there might not be a valid route at all."

### What Google Left Vague (Clarifying Questions Needed)
- What does "layover" mean? (stops in between, not including source/destination)
- Can there be multiple flights between same cities with different prices?
- Are all prices positive?
- What if source equals destination?
- What should we return if no valid path exists?

---

## Clarifying Questions to Ask

**Candidate**: "Let me make sure I understand the problem correctly..."

1. **"When you say 'layovers', do you mean intermediate stops between source and destination?"**
   - *Interviewer*: "Yes, exactly. If someone flies NYC → Chicago → LA, that's 1 layover."

2. **"Can there be multiple direct flights between the same two cities with different prices?"**
   - *Interviewer*: "Good question. No, assume at most one direct flight between any two cities."

3. **"Are all flight prices positive? Can there be zero-cost flights?"**
   - *Interviewer*: "All prices are positive integers, ranging from 1 to 10,000."

4. **"How many cities and flights are we dealing with? This helps me think about time complexity."**
   - *Interviewer*: "Up to 100 cities and around 5000 flights. The layover limit can be up to 100."

5. **"What should I return if there's no valid path within the layover constraint?"**
   - *Interviewer*: "Return -1 in that case."

6. **"Is the source guaranteed to be different from the destination?"**
   - *Interviewer*: "Yes, they'll always be different."

---

## Problem Restatement After Clarification

```
Given:
- n cities labeled 0 to n-1
- flights[i] = [from, to, price] (directed edges)
- src: source city
- dst: destination city
- k: maximum number of stops (layovers) allowed

Return: Minimum cost to reach dst from src with at most k stops
        Return -1 if no such route exists
```

---

## Test Cases

```python
# Example 1: Basic case
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0, dst = 3, k = 1
# Expected: 700 (0 -> 1 -> 3)

# Example 2: Cheaper with more stops
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
# Expected: 200 (0 -> 1 -> 2)

# Example 3: No valid path
n = 3
flights = [[0,1,100],[1,2,100]]
src = 0, dst = 2, k = 0
# Expected: -1 (need 1 stop but k=0)

# Edge case: Direct flight exists
n = 2
flights = [[0,1,100]]
src = 0, dst = 1, k = 0
# Expected: 100
```

---

## Approach Discussion

### Brute Force: DFS with All Paths
**Idea**: Explore all possible paths from source to destination, track minimum cost.

```python
def findCheapestPrice_bruteforce(n, flights, src, dst, k):
    """
    Brute Force: DFS exploring all paths
    Time: O(n^k) - exponential, explores all possible paths
    Space: O(n) - recursion stack
    """
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    min_cost = [float('inf')]

    def dfs(node, stops_remaining, current_cost):
        # Base case: reached destination
        if node == dst:
            min_cost[0] = min(min_cost[0], current_cost)
            return

        # Pruning: no more stops allowed
        if stops_remaining < 0:
            return

        # Pruning: current path already more expensive
        if current_cost >= min_cost[0]:
            return

        for neighbor, price in graph[node]:
            dfs(neighbor, stops_remaining - 1, current_cost + price)

    # k stops means k+1 edges allowed
    dfs(src, k, 0)

    return min_cost[0] if min_cost[0] != float('inf') else -1
```

**Problems with Brute Force**:
- Exponential time complexity
- Explores many redundant paths
- Will TLE for large inputs

---

### Optimized Solution 1: Bellman-Ford Variant (Recommended for Interview)

**Key Insight**: This is a shortest path problem with an edge count constraint. Bellman-Ford naturally handles this!

**Why Bellman-Ford?**
- Standard Bellman-Ford: After i iterations, we have shortest paths using at most i edges
- With k stops allowed, we need at most k+1 edges
- Run Bellman-Ford for exactly k+1 iterations

```python
def findCheapestPrice_bellman_ford(n: int, flights: List[List[int]],
                                    src: int, dst: int, k: int) -> int:
    """
    Bellman-Ford with k+1 iterations
    Time: O(k * E) where E = number of flights
    Space: O(n) for the distance array

    Pattern: Modified Bellman-Ford for edge-constrained shortest path
    """
    # Initialize distances
    # dist[i] = minimum cost to reach city i
    dist = [float('inf')] * n
    dist[src] = 0

    # Relax edges k+1 times (k stops = k+1 edges maximum)
    for i in range(k + 1):
        # CRITICAL: Use a copy to avoid using updates from same iteration
        # This ensures we only use paths with exactly one more edge
        temp = dist.copy()

        for u, v, price in flights:
            if dist[u] != float('inf'):
                temp[v] = min(temp[v], dist[u] + price)

        dist = temp

    return dist[dst] if dist[dst] != float('inf') else -1
```

**Why the copy is CRITICAL**:
```
Without copy: dist[A] updates, then dist[B] uses updated dist[A] in same iteration
             This allows more edges than intended!
With copy:    All updates use values from previous iteration
             Guarantees exactly one more edge per iteration
```

---

### Optimized Solution 2: BFS with Level-by-Level Processing

```python
from collections import deque, defaultdict

def findCheapestPrice_bfs(n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:
    """
    BFS approach - process level by level (each level = one more stop)
    Time: O(k * E)
    Space: O(n) for the distance array + O(E) for graph

    Pattern: Level-order BFS with cost tracking
    """
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    # dist[i] = minimum cost to reach city i
    dist = [float('inf')] * n
    dist[src] = 0

    # BFS queue: (current_city, current_cost)
    queue = deque([(src, 0)])
    stops = 0

    while queue and stops <= k:
        # Process all nodes at current level
        level_size = len(queue)

        for _ in range(level_size):
            curr_city, curr_cost = queue.popleft()

            for next_city, price in graph[curr_city]:
                new_cost = curr_cost + price

                # Only proceed if this path is cheaper
                if new_cost < dist[next_city]:
                    dist[next_city] = new_cost
                    queue.append((next_city, new_cost))

        stops += 1

    return dist[dst] if dist[dst] != float('inf') else -1
```

---

### Optimized Solution 3: Dijkstra with State (city, stops)

```python
import heapq
from collections import defaultdict

def findCheapestPrice_dijkstra(n: int, flights: List[List[int]],
                                src: int, dst: int, k: int) -> int:
    """
    Modified Dijkstra with state = (cost, city, stops_used)
    Time: O(E * k * log(E * k))
    Space: O(n * k) for visited states

    Pattern: Dijkstra with extended state space
    """
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    # Priority queue: (cost, city, stops_used)
    pq = [(0, src, 0)]

    # visited[city] = minimum stops used to reach this city with best cost
    # We can revisit a city if we used fewer stops (might find better path later)
    visited = {}  # city -> minimum stops to reach it

    while pq:
        cost, city, stops = heapq.heappop(pq)

        # Reached destination
        if city == dst:
            return cost

        # Skip if we've visited this city with fewer/equal stops
        if city in visited and visited[city] <= stops:
            continue
        visited[city] = stops

        # Can't take more flights
        if stops > k:
            continue

        for next_city, price in graph[city]:
            heapq.heappush(pq, (cost + price, next_city, stops + 1))

    return -1
```

---

## Code Walkthrough with Example

```
Input: n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
       src=0, dst=3, k=1

Graph:
    0 --100--> 1 --100--> 2
    ^         |          |
    |         600        200
    +--100----+          |
              +--->3<----+

Bellman-Ford Execution:
Initial: dist = [0, inf, inf, inf]

Iteration 1 (1 edge):
  - Edge (0,1,100): dist[1] = min(inf, 0+100) = 100
  - Edge (1,2,100): dist[2] = min(inf, inf+100) = inf (1 not updated yet in temp)
  - Edge (1,3,600): dist[3] = min(inf, inf+600) = inf
  After: dist = [0, 100, inf, inf]

Iteration 2 (2 edges, k+1=2):
  - Edge (0,1,100): dist[1] = min(100, 0+100) = 100
  - Edge (1,2,100): dist[2] = min(inf, 100+100) = 200
  - Edge (1,3,600): dist[3] = min(inf, 100+600) = 700
  - Edge (2,3,200): dist[3] = min(700, inf+200) = 700 (2 not updated yet in temp)
  After: dist = [0, 100, 200, 700]

Result: dist[3] = 700
```

---

## Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force DFS | O(n^k) | O(n) | Exponential, TLE |
| Bellman-Ford | O(k * E) | O(n) | **Best for interview** |
| BFS Level-order | O(k * E) | O(n + E) | Easy to understand |
| Dijkstra + State | O(E*k*log(E*k)) | O(n*k) | Overkill for this problem |

**Recommendation**: Use Bellman-Ford for interview - it's clean, optimal, and shows deep understanding.

---

## Common Bugs to Avoid

1. **Not using temp array in Bellman-Ford** - allows unlimited edges
2. **Off-by-one with k** - k stops means k+1 edges
3. **Forgetting to handle unreachable case** - return -1
4. **Using visited set incorrectly in Dijkstra** - need to track (city, stops) together

---

## DSA Pattern: Modified Bellman-Ford

```
When to use:
- Shortest path with EDGE COUNT constraint
- Negative edges allowed (but not negative cycles)
- Need to find path with exactly/at most K edges

Template:
1. Initialize dist array with infinity, dist[src] = 0
2. For i in range(max_edges):
    - Create temp copy of dist
    - Relax all edges using dist, store in temp
    - dist = temp
3. Return dist[dst]
```

---

# Problem 2: Data Pipeline Dependencies (LC 329 - Longest Increasing Path in a Matrix)

**LeetCode Link**: [https://leetcode.com/problems/longest-increasing-path-in-a-matrix/](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

## Google-Style Scenario Presentation

> **Interviewer**: "You're working on a data pipeline system at Google Cloud. We have a grid of data processing nodes, each with a priority level. Data can only flow from a lower priority node to an adjacent higher priority node (up, down, left, right).
>
> We need to find the longest possible data flow path through the grid. This helps us understand the maximum processing depth in our pipeline."

### What Google Left Vague
- What does "adjacent" mean? (4-directional? 8-directional?)
- Can a node be visited multiple times in a path?
- What if the grid is empty?
- Are there ties in priority? Can we move to equal priority?

---

## Clarifying Questions

1. **"By adjacent, do you mean only up/down/left/right, or diagonals too?"**
   - *Interviewer*: "Just the 4 cardinal directions."

2. **"Can the same node appear multiple times in a single path?"**
   - *Interviewer*: "No, each node can only be visited once per path. But since we only move to strictly higher values, this is naturally enforced."

3. **"If two adjacent nodes have equal priority, can data flow between them?"**
   - *Interviewer*: "No, strictly increasing only."

4. **"What's the grid size we're dealing with?"**
   - *Interviewer*: "Up to 200x200."

---

## Problem Restatement

```
Given: m x n matrix of integers
Find: Length of longest increasing path

Rules:
- Can move in 4 directions: up, down, left, right
- Next cell must have strictly greater value
- Return the length of the longest path
```

---

## Test Cases

```python
# Example 1: Diagonal increasing path
matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
# Expected: 4 (path: 1 -> 2 -> 6 -> 9)

# Example 2: Snake pattern
matrix = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
# Expected: 4 (path: 3 -> 4 -> 5 -> 6)

# Example 3: Single cell
matrix = [[1]]
# Expected: 1

# Example 4: All same values
matrix = [[1, 1], [1, 1]]
# Expected: 1 (can't move anywhere)
```

---

## Approach Discussion

### Brute Force: DFS from Every Cell

```python
def longestIncreasingPath_bruteforce(matrix: List[List[int]]) -> int:
    """
    Brute Force: DFS from every cell, no memoization
    Time: O(m*n * 4^(m*n)) - exponential
    Space: O(m*n) - recursion stack
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(row, col):
        max_length = 1

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[row][col]:
                max_length = max(max_length, 1 + dfs(nr, nc))

        return max_length

    result = 0
    for i in range(m):
        for j in range(n):
            result = max(result, dfs(i, j))

    return result
```

**Why it's slow**: Same cells are recomputed many times!

---

### Optimized: DFS + Memoization

**Key Insight**: The longest path from cell (i,j) is deterministic - it only depends on the matrix values, which don't change. We can cache results!

```python
def longestIncreasingPath(matrix: List[List[int]]) -> int:
    """
    DFS with Memoization
    Time: O(m * n) - each cell computed once
    Space: O(m * n) - memo table + recursion stack

    Pattern: DFS + Memoization on Grid (Top-Down DP)
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # memo[i][j] = longest increasing path starting from (i, j)
    memo = {}

    def dfs(row: int, col: int) -> int:
        # Check cache first
        if (row, col) in memo:
            return memo[(row, col)]

        # Base case: at minimum, path length is 1 (the cell itself)
        max_length = 1

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            # Valid cell AND strictly increasing
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[row][col]:
                max_length = max(max_length, 1 + dfs(nr, nc))

        # Cache result before returning
        memo[(row, col)] = max_length
        return max_length

    # Try starting from every cell
    result = 0
    for i in range(m):
        for j in range(n):
            result = max(result, dfs(i, j))

    return result
```

---

### Alternative: Topological Sort (BFS)

**Insight**: If we process cells in increasing order of value, each cell's answer depends only on already-computed neighbors.

```python
from collections import deque

def longestIncreasingPath_topo(matrix: List[List[int]]) -> int:
    """
    Topological Sort BFS approach
    Time: O(m * n)
    Space: O(m * n)

    Pattern: Topological Sort on implicit DAG
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # outdegree[i][j] = number of neighbors with SMALLER values
    # (cells we can come FROM)
    outdegree = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    outdegree[i][j] += 1

    # Start BFS from cells with outdegree 0 (local maxima)
    queue = deque()
    for i in range(m):
        for j in range(n):
            if outdegree[i][j] == 0:
                queue.append((i, j))

    # BFS level by level
    length = 0
    while queue:
        length += 1
        level_size = len(queue)

        for _ in range(level_size):
            x, y = queue.popleft()

            for dr, dc in directions:
                nx, ny = x + dr, y + dc

                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] < matrix[x][y]:
                    outdegree[nx][ny] -= 1
                    if outdegree[nx][ny] == 0:
                        queue.append((nx, ny))

    return length
```

---

## Code Walkthrough

```
Input:
matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

DFS with Memo Execution:

Starting from (2,1) with value 1:
  - Check neighbors: (2,0)=2 > 1, (2,2)=1 not >, (1,1)=6 > 1
  - dfs(2,0): value=2, neighbors (1,0)=6 > 2
    - dfs(1,0): value=6, neighbors (0,0)=9 > 6
      - dfs(0,0): value=9, no valid neighbors
      - memo[(0,0)] = 1
    - memo[(1,0)] = 1 + 1 = 2
  - memo[(2,0)] = 1 + 2 = 3
  - dfs(1,1): value=6, neighbors (0,1)=9 > 6
    - dfs(0,1): value=9, no valid neighbors
    - memo[(0,1)] = 1
  - memo[(1,1)] = 1 + 1 = 2

  max_length from (2,1) = max(1+3, 1+2) = 4
  memo[(2,1)] = 4

Final: max over all cells = 4
Path: 1 -> 2 -> 6 -> 9
```

---

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Brute Force DFS | O(m*n * 4^(m*n)) | O(m*n) |
| DFS + Memoization | O(m*n) | O(m*n) |
| Topological Sort | O(m*n) | O(m*n) |

---

## DSA Pattern: DFS + Memoization on Grid

```python
# Template for grid DFS with memoization
def solve_grid_dp(grid):
    m, n = len(grid), len(grid[0])
    memo = {}
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        result = BASE_CASE
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if is_valid(ni, nj) and can_move(i, j, ni, nj):
                result = combine(result, dfs(ni, nj))

        memo[(i, j)] = result
        return result

    return aggregate(dfs(i, j) for all i, j)
```

---

# Problem 3: Email Account Deduplication (LC 721 - Accounts Merge)

**LeetCode Link**: [https://leetcode.com/problems/accounts-merge/](https://leetcode.com/problems/accounts-merge/)

## Google-Style Scenario Presentation

> **Interviewer**: "At Gmail, we've noticed some users have accidentally created multiple accounts with the same email addresses. We want to merge accounts that belong to the same person.
>
> Given a list of accounts where each account has a name and a list of emails, merge all accounts belonging to the same person. Two accounts belong to the same person if they share at least one email."

### What Google Left Vague
- Can two different people have the same name?
- Should emails in the result be sorted?
- What format should the output be in?
- Can an account have duplicate emails?

---

## Clarifying Questions

1. **"Can two different people have the same name?"**
   - *Interviewer*: "Yes! John Smith might have accounts [John, a@mail.com] and a completely separate person named John Smith might have [John, b@mail.com]. They should NOT be merged."

2. **"How should I format the output?"**
   - *Interviewer*: "Each merged account should have the name first, followed by all emails sorted alphabetically."

3. **"Can a single account have duplicate emails?"**
   - *Interviewer*: "No, each email appears at most once per account."

4. **"What's the scale - how many accounts and emails?"**
   - *Interviewer*: "Up to 1000 accounts, each with up to 10 emails."

---

## Problem Restatement

```
Given: accounts[i] = [name, email1, email2, ...]

Merge: Two accounts belong to same person if they share any email

Return: Merged accounts with [name, sorted_emails...]
```

---

## Test Cases

```python
# Example 1: Overlapping emails merge accounts
accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]
# Expected:
# [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
#  ["Mary", "mary@mail.com"],
#  ["John", "johnnybravo@mail.com"]]
# Note: First two Johns merged (share johnsmith@mail.com)
#       Third John is different person!

# Example 2: Chain of merges
accounts = [
    ["A", "a@m.com", "b@m.com"],
    ["A", "b@m.com", "c@m.com"],
    ["A", "c@m.com", "d@m.com"]
]
# Expected: [["A", "a@m.com", "b@m.com", "c@m.com", "d@m.com"]]
# All three accounts merge via chain
```

---

## Approach Discussion

### Brute Force: Iterative Merging

```python
def accountsMerge_bruteforce(accounts):
    """
    Brute Force: Keep merging until no more merges possible
    Time: O(n^2 * m) where n=accounts, m=emails per account
    Space: O(n * m)
    """
    merged = [set(acc[1:]) for acc in accounts]
    names = [acc[0] for acc in accounts]

    changed = True
    while changed:
        changed = False
        for i in range(len(merged)):
            if merged[i] is None:
                continue
            for j in range(i + 1, len(merged)):
                if merged[j] is None:
                    continue
                # Check if any common email
                if merged[i] & merged[j]:
                    merged[i] |= merged[j]
                    merged[j] = None
                    changed = True

    result = []
    for i, emails in enumerate(merged):
        if emails:
            result.append([names[i]] + sorted(emails))

    return result
```

---

### Optimized: Union-Find (Disjoint Set Union)

**Key Insight**: This is a classic Union-Find problem! Each email is a node. If two emails appear in the same account, union them.

```python
class UnionFind:
    """
    Union-Find with path compression and union by rank
    """
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        # Add new element if not seen
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    """
    Union-Find approach
    Time: O(n * m * α(n*m)) ≈ O(n * m) where α is inverse Ackermann
    Space: O(n * m)

    Pattern: Union-Find for connected components
    """
    uf = UnionFind()

    # Map email -> account name
    email_to_name = {}

    # Step 1: Union all emails within each account
    for account in accounts:
        name = account[0]
        first_email = account[1]

        for email in account[1:]:
            email_to_name[email] = name
            uf.union(first_email, email)

    # Step 2: Group emails by their root
    from collections import defaultdict
    root_to_emails = defaultdict(list)

    for email in email_to_name:
        root = uf.find(email)
        root_to_emails[root].append(email)

    # Step 3: Build result
    result = []
    for root, emails in root_to_emails.items():
        name = email_to_name[root]
        result.append([name] + sorted(emails))

    return result
```

---

### Alternative: DFS on Graph

```python
from collections import defaultdict

def accountsMerge_dfs(accounts: List[List[str]]) -> List[List[str]]:
    """
    Build graph of emails, DFS to find connected components
    Time: O(n * m * log(n * m)) - sorting
    Space: O(n * m)

    Pattern: DFS for connected components
    """
    # Build graph: email -> set of connected emails
    graph = defaultdict(set)
    email_to_name = {}

    for account in accounts:
        name = account[0]
        emails = account[1:]

        for email in emails:
            email_to_name[email] = name

        # Connect all emails in this account
        for i in range(len(emails)):
            for j in range(i + 1, len(emails)):
                graph[emails[i]].add(emails[j])
                graph[emails[j]].add(emails[i])

    # DFS to find connected components
    visited = set()
    result = []

    def dfs(email, component):
        visited.add(email)
        component.append(email)

        for neighbor in graph[email]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for email in email_to_name:
        if email not in visited:
            component = []
            dfs(email, component)
            name = email_to_name[email]
            result.append([name] + sorted(component))

    return result
```

---

## Code Walkthrough

```
Input:
accounts = [
    ["John", "a@m", "b@m"],
    ["John", "a@m", "c@m"],
    ["Mary", "d@m"]
]

Union-Find Execution:

Step 1: Process each account
  Account 0: Union(a@m, b@m)
    parent = {a@m: a@m, b@m: a@m}

  Account 1: Union(a@m, c@m)
    find(a@m) = a@m
    find(c@m) = c@m (new)
    parent = {a@m: a@m, b@m: a@m, c@m: a@m}

  Account 2: d@m alone
    parent = {a@m: a@m, b@m: a@m, c@m: a@m, d@m: d@m}

Step 2: Group by root
  find(a@m) = a@m -> root_to_emails[a@m] = [a@m]
  find(b@m) = a@m -> root_to_emails[a@m] = [a@m, b@m]
  find(c@m) = a@m -> root_to_emails[a@m] = [a@m, b@m, c@m]
  find(d@m) = d@m -> root_to_emails[d@m] = [d@m]

Step 3: Build result
  [["John", "a@m", "b@m", "c@m"], ["Mary", "d@m"]]
```

---

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(n² * m) | O(n * m) |
| Union-Find | O(n * m * α(n*m)) ≈ O(n * m) | O(n * m) |
| DFS | O(n * m * log(n*m)) | O(n * m) |

---

## DSA Pattern: Union-Find Template

```python
class UnionFind:
    def __init__(self, n=None):
        self.parent = {} if n is None else {i: i for i in range(n)}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already connected
        if self.rank.get(px, 0) < self.rank.get(py, 0):
            px, py = py, px
        self.parent[py] = px
        if self.rank.get(px, 0) == self.rank.get(py, 0):
            self.rank[px] = self.rank.get(px, 0) + 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

---

# Problem 4: Auto-Complete Suggestion Distance (LC 72 - Edit Distance)

**LeetCode Link**: [https://leetcode.com/problems/edit-distance/](https://leetcode.com/problems/edit-distance/)

## Google-Style Scenario Presentation

> **Interviewer**: "You're working on Google Search's 'Did you mean?' feature. When a user types a misspelled query, we want to suggest the closest correct spelling.
>
> Given the user's input and a dictionary word, calculate how many character operations (insert, delete, replace) are needed to transform one into the other."

### What Google Left Vague
- Are operations one character at a time?
- Case sensitive?
- What counts as one operation?

---

## Clarifying Questions

1. **"What operations are allowed and how do they work?"**
   - *Interviewer*: "Three operations - insert one character anywhere, delete one character, or replace one character with another. Each counts as one operation."

2. **"Is this case-sensitive?"**
   - *Interviewer*: "Yes, 'A' and 'a' are different characters."

3. **"Can the words be empty?"**
   - *Interviewer*: "Yes. If one word is empty, the distance equals the length of the other."

4. **"What's the maximum word length?"**
   - *Interviewer*: "Up to 500 characters each."

---

## Problem Restatement

```
Given: Two strings word1 and word2
Operations: Insert, Delete, Replace (each costs 1)
Return: Minimum operations to transform word1 into word2
```

---

## Test Cases

```python
# Example 1
word1 = "horse"
word2 = "ros"
# Expected: 3
# horse -> rorse (replace h with r)
# rorse -> rose (delete r)
# rose -> ros (delete e)

# Example 2
word1 = "intention"
word2 = "execution"
# Expected: 5

# Edge cases
word1 = "", word2 = "abc"  # Expected: 3 (insert 3 chars)
word1 = "abc", word2 = ""  # Expected: 3 (delete 3 chars)
word1 = "abc", word2 = "abc"  # Expected: 0
```

---

## Approach Discussion

### Brute Force: Recursive with All Choices

```python
def minDistance_bruteforce(word1: str, word2: str) -> int:
    """
    Brute Force: Try all operations recursively
    Time: O(3^(m+n)) - exponential
    Space: O(m+n) - recursion stack
    """
    def helper(i, j):
        # Base cases
        if i == len(word1):
            return len(word2) - j  # Insert remaining chars
        if j == len(word2):
            return len(word1) - i  # Delete remaining chars

        # If characters match, no operation needed
        if word1[i] == word2[j]:
            return helper(i + 1, j + 1)

        # Try all three operations
        insert = 1 + helper(i, j + 1)      # Insert word2[j] into word1
        delete = 1 + helper(i + 1, j)      # Delete word1[i]
        replace = 1 + helper(i + 1, j + 1) # Replace word1[i] with word2[j]

        return min(insert, delete, replace)

    return helper(0, 0)
```

---

### Optimized: 2D Dynamic Programming

**Key Insight**: `dp[i][j]` = minimum operations to convert `word1[0:i]` to `word2[0:j]`

**Recurrence**:
- If `word1[i-1] == word2[j-1]`: `dp[i][j] = dp[i-1][j-1]` (no operation needed)
- Else: `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`
  - `dp[i-1][j]`: Delete from word1
  - `dp[i][j-1]`: Insert into word1
  - `dp[i-1][j-1]`: Replace in word1

```python
def minDistance(word1: str, word2: str) -> int:
    """
    2D DP solution
    Time: O(m * n)
    Space: O(m * n)

    Pattern: 2D DP on two strings
    """
    m, n = len(word1), len(word2)

    # dp[i][j] = min ops to convert word1[0:i] to word2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: empty string transformations
    for i in range(m + 1):
        dp[i][0] = i  # Delete all chars from word1
    for j in range(n + 1):
        dp[0][j] = j  # Insert all chars to get word2

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # Characters match - no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Take minimum of three operations
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # Delete
                    dp[i][j - 1],     # Insert
                    dp[i - 1][j - 1]  # Replace
                )

    return dp[m][n]
```

---

### Space-Optimized: 1D DP

```python
def minDistance_optimized(word1: str, word2: str) -> int:
    """
    Space-optimized 1D DP
    Time: O(m * n)
    Space: O(n)

    Key insight: We only need previous row to compute current row
    """
    m, n = len(word1), len(word2)

    # Previous row
    prev = list(range(n + 1))

    for i in range(1, m + 1):
        # Current row
        curr = [0] * (n + 1)
        curr[0] = i  # Base case: delete all from word1[0:i]

        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    prev[j],      # Delete
                    curr[j - 1],  # Insert
                    prev[j - 1]   # Replace
                )

        prev = curr

    return prev[n]
```

---

## Code Walkthrough

```
Input: word1 = "horse", word2 = "ros"

DP Table Construction:

        ""   r    o    s
    ""   0   1    2    3
    h    1   1    2    3
    o    2   2    1    2
    r    3   2    2    2
    s    4   3    3    2
    e    5   4    4    3

Trace back for understanding:
- dp[5][3] = 3

Operations:
1. horse -> rorse (replace 'h' with 'r')
2. rorse -> rose (delete second 'r')
3. rose -> ros (delete 'e')
```

---

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(3^(m+n)) | O(m+n) |
| 2D DP | O(m*n) | O(m*n) |
| 1D DP | O(m*n) | O(min(m,n)) |

---

## DSA Pattern: Two String DP

```python
# Template for DP on two strings
def solve_two_string_dp(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = BASE_CASE_1(i)
    for j in range(n + 1):
        dp[0][j] = BASE_CASE_2(j)

    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = MATCH_CASE(dp[i-1][j-1])
            else:
                dp[i][j] = NO_MATCH_CASE(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]
```

---

# Problem 5: Build System Dependencies (LC 207 - Course Schedule)

**LeetCode Link**: [https://leetcode.com/problems/course-schedule/](https://leetcode.com/problems/course-schedule/)

## Google-Style Scenario Presentation

> **Interviewer**: "You're working on the Bazel build system. Before building a target, all its dependencies must be built first. Sometimes developers accidentally create circular dependencies, which makes the build impossible.
>
> Given a list of build targets and their dependencies, determine if all targets can be built successfully."

### What Google Left Vague
- What's the format of dependencies?
- Are target IDs always integers?
- Is there always at least one target?

---

## Clarifying Questions

1. **"How are dependencies represented?"**
   - *Interviewer*: "As pairs [a, b] meaning 'target a depends on target b' - you must build b before a."

2. **"Can a target depend on itself?"**
   - *Interviewer*: "Not directly, but there could be indirect cycles like a->b->c->a."

3. **"What should I return?"**
   - *Interviewer*: "Return true if all targets can be built, false if there's a cycle."

4. **"How many targets and dependencies could there be?"**
   - *Interviewer*: "Up to 2000 targets and 5000 dependencies."

---

## Problem Restatement

```
Given:
- numCourses: total number of courses (0 to n-1)
- prerequisites: [a, b] means "take b before a"

Return: true if all courses can be finished (no cycle), false otherwise
```

---

## Test Cases

```python
# Example 1: Simple chain, no cycle
numCourses = 2
prerequisites = [[1, 0]]  # 1 depends on 0
# Expected: True (order: 0 -> 1)

# Example 2: Cycle exists
numCourses = 2
prerequisites = [[1, 0], [0, 1]]  # 1 depends on 0, 0 depends on 1
# Expected: False (cycle!)

# Example 3: Complex graph, no cycle
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# Expected: True (order: 0 -> 1,2 -> 3)

# Edge case: No prerequisites
numCourses = 3
prerequisites = []
# Expected: True (any order works)
```

---

## Approach Discussion

### Brute Force: Check All Orderings

```python
from itertools import permutations

def canFinish_bruteforce(numCourses, prerequisites):
    """
    Brute Force: Try all possible orderings
    Time: O(n! * e) - factorial!
    Space: O(n)
    """
    # Check if an ordering satisfies all prerequisites
    def is_valid(order):
        position = {course: i for i, course in enumerate(order)}
        for a, b in prerequisites:
            if position[b] >= position[a]:  # b must come before a
                return False
        return True

    for order in permutations(range(numCourses)):
        if is_valid(order):
            return True

    return False
```

---

### Optimized 1: DFS Cycle Detection

**Key Insight**: Build a graph and check for cycles using DFS with three states:
- WHITE (0): Not visited
- GRAY (1): Currently being processed (in current DFS path)
- BLACK (2): Completely processed

A cycle exists if we encounter a GRAY node during DFS.

```python
from collections import defaultdict

def canFinish_dfs(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    DFS with three-color marking for cycle detection
    Time: O(V + E)
    Space: O(V + E)

    Pattern: DFS Cycle Detection in Directed Graph
    """
    # Build adjacency list: course -> list of courses that depend on it
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)  # b -> a means take b before a

    # States: 0 = WHITE (unvisited), 1 = GRAY (in progress), 2 = BLACK (done)
    state = [0] * numCourses

    def has_cycle(node):
        if state[node] == 1:  # GRAY - cycle detected!
            return True
        if state[node] == 2:  # BLACK - already processed, no cycle from here
            return False

        # Mark as GRAY (processing)
        state[node] = 1

        # Check all neighbors
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True

        # Mark as BLACK (done)
        state[node] = 2
        return False

    # Check from every node (graph might be disconnected)
    for course in range(numCourses):
        if has_cycle(course):
            return False

    return True
```

---

### Optimized 2: Kahn's Algorithm (BFS Topological Sort)

**Key Insight**: Use in-degree based BFS. If we can process all nodes, there's no cycle.

```python
from collections import defaultdict, deque

def canFinish_bfs(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Kahn's Algorithm (BFS Topological Sort)
    Time: O(V + E)
    Space: O(V + E)

    Pattern: Topological Sort for Cycle Detection
    """
    # Build graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)  # b -> a
        in_degree[a] += 1

    # Start with nodes that have no dependencies
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)

    # BFS: process nodes with in-degree 0
    processed = 0

    while queue:
        course = queue.popleft()
        processed += 1

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we processed all courses, no cycle exists
    return processed == numCourses
```

---

### Extension: Course Schedule II (Return Valid Order)

```python
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Return a valid ordering if possible, else empty list
    Time: O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque([c for c in range(numCourses) if in_degree[c] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == numCourses else []
```

---

## Code Walkthrough

```
Input: numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]]

Graph (b -> a means "take b before a"):
  0 -> [1, 2]
  1 -> [3]
  2 -> [3]

In-degrees: [0, 1, 1, 2]

BFS Execution:
  Initial queue: [0] (only course with in-degree 0)

  Process 0:
    - processed = 1
    - Decrease in_degree[1]: 1 -> 0, add to queue
    - Decrease in_degree[2]: 1 -> 0, add to queue
    - queue = [1, 2]

  Process 1:
    - processed = 2
    - Decrease in_degree[3]: 2 -> 1
    - queue = [2]

  Process 2:
    - processed = 3
    - Decrease in_degree[3]: 1 -> 0, add to queue
    - queue = [3]

  Process 3:
    - processed = 4
    - queue = []

Result: processed (4) == numCourses (4) -> True
Valid order: [0, 1, 2, 3] or [0, 2, 1, 3]
```

---

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(n! * e) | O(n) |
| DFS 3-Color | O(V + E) | O(V + E) |
| Kahn's BFS | O(V + E) | O(V + E) |

---

## DSA Pattern: Topological Sort

```python
# Template: Kahn's Algorithm
def topological_sort(n, edges):
    """
    edges[i] = [a, b] means edge from b to a
    Returns topological order or empty list if cycle
    """
    graph = defaultdict(list)
    in_degree = [0] * n

    for a, b in edges:
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []
```

---

# Summary: DSA Patterns Covered

| Problem | LC # | Pattern | Key Technique |
|---------|------|---------|---------------|
| Flight Budget | [787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Graph + DP | Bellman-Ford with edge limit |
| Data Pipeline | [329](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | DFS + Memo | Grid DFS with memoization |
| Email Accounts | [721](https://leetcode.com/problems/accounts-merge/) | Union-Find | DSU for connected components |
| Auto-Complete | [72](https://leetcode.com/problems/edit-distance/) | 2D DP | Two string comparison |
| Build System | [207](https://leetcode.com/problems/course-schedule/) | Topological Sort | Cycle detection in DAG |

---

# Mock Interview Checklist

Before each problem:
- [ ] Clarify all ambiguities
- [ ] Confirm input/output format
- [ ] Discuss edge cases
- [ ] State time/space requirements

During coding:
- [ ] Narrate every decision
- [ ] No silent coding
- [ ] Use meaningful variable names
- [ ] Handle edge cases

After coding:
- [ ] Trace through with example
- [ ] Verify edge cases
- [ ] State complexities
- [ ] Discuss optimizations

---

**Good luck with your mock interview!**
