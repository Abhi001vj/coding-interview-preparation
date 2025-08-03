## Backtracking Aggregation

```
def dfs(start_index, [..additional_states]):
    if is_leaf(start_index):
        return 1
    ans = initial_value
    for edge in get_edges(start_index, [.. additional_states]):
        if additioanl_states:
            update([.. additional_states])
        ans = aggreagte(ans, dfs(start_index + len(edge), [.. additional_states]))
        if additional_states:
            revert([.. additional_states])
    return ans
```
## Backtracking Simple

```python

ans = []

def dfs(start_index, path, [..additional_states]):
    if is_leaf(start_index):
        ans.append(path[:])
        return
    
    for edge in get_edges(start_index, [..additional_states]):
        if not is_valid(edge):
            continue
        path.append(edge)
        if additioanl_states:
            update([..additional_states])
        dfs(start_index + len(edge), path, [..additioanl_state])
        revert([..additional_states])
        path.pop()

        
```

## Binary Search

```python

def bianry_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1
    while left <= right:
        mid = (left + right ) // 2
        if feasible(mid):
            first_true_index = mid
            right = mid -1
        else:
            left = mid + 1
    return first_true_index

```

## BFS on Tree

```python

def bfs(root):
    queue = deque([root])
    while queue:
        node =  queue.popleft()
        for child in node.children:
            if is_goal(child):
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND

```

## DFS on Tree

```python

def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    left = dfs(root.left, target)
    if left is not None:
        return left
    return dfs(root.right, target)
```

## BFS on Graphs

```python

def bfs(root):
    queue = deque([root])
    visited = set([root])
    while len(queue) > 0:
        node = queue.popleft(queue)
        for neighbour in node.neighbours:
            if neighbour in visited:
                continue
            queue.append(neighbour)
            visited.append(neighbour)
```

## DFS on graph

```python
def dfs(root, visited):
    for neighbour in get_neighbours(root):
        if neighbour in visited:
            continue
        visited.add(neighbour)
        dfs(neighbour, visited)
```

## BFS on matrix
```python

num_rows, num_cols = len(grid), len(grid[0])
def get_neighbours(coord):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []
    for i in range(len(delta_row)):
        neighbour_row = row + delta_row[i]
        neighbour_col = col + delta_col[i]

        if 0 <= neighbour_row < num_rows and 0 <= neighbour_col < num_cols:
            res.append(grid[neighbour_row][neighbour_col])
    return res

```

## Mono Stack

```python
def mono_stack(insert_entries):
    stack = []
    for entry in insert_entries:
        while stack and stack[-1] <= entry:
            stack.pop()
            # So something with the popped item
        stack.append(entry)
```

## Prefix Sum

```python

def build_prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] =  arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    prefix_sum

def query_range(prefix_sum, left, right):
    if left == 0:
        return prefix_sum[right]
    return prefix_sum[right] - prefix_sum[left-1]
```

## Sliding Window (Fixed Size)

```python

def sliding_window_fixed(input, window_size):
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        remove input[left] from window
        append input[right] to window
        ans = optimal(ans, window)
    return ans

```

## Sliding Window Flexible - Longest

```python

def sliding_window_flexible_longest(input):
    initialize window , ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while invalid(window): # update the left until the window is valid again
            remove input[left] from window
            left += 1
        ans = max(ans, window) # window is guarenteed to be valid here
```

## Sliding Window Flexible - Shorted

```python
def sliding_window_flexible_shortest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        appent input[right] to window
        while vaid(window):
            ans = min(ans, window) # window is guarentted to be valid here
            remove input[left] from widnow
            left += 1
    return ans
```

## Two Pointers (Opposite Direction)

```python

def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # process current elements
        current = process(arr[left],arr[right])

        # update the pointers based on condition
        if condition(arr[left], arr[right]):
            left += 1
        else:
            right -= 1
```

## Two Pointers (Same Direction)

```python

def two_pointers_same(arr):
    slow, fast = 0, 0
    while fast < len(arr):
        # process current elements
        current = process(arr[slow], arr[fast])

        # udpate pointers based on condition
        if condition(arr[slow], arr[fast]):
            slow += 1
        # fast pointer always moves forward
        fast += 1
```

## Topological Sort

```python
def find_indegree(graph):
    indegree = { node: 0 for node in graph }  # dict
    for node in graph:
        for neighbor in graph[node]:
            indgree[neighbor] += 1
    return indegree


def topo_sort(graph):
    res = []
    q = deque()
    indegree = find_indegree(graph)
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return res if len(graph) == len(res) else None

```

## Trie

```python

class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
    
    def insert(self, s, idx):
        # idx: index of the current character in s
        if idx != len(s):
            self.children.setdefault(s[idx], Node(s[idx]))
            self.children.get(s[idx]).insert(s, idx+1)
```


## Union Find

```python
class UnionFind:
    def __init__(self):
        slef.id = {}
    
    def find(slef, x):
        y = self.id.get(x,x)
        if y ! = x:
            slef.id[x] = y = self.find(y)
        return y
    
    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)
```
