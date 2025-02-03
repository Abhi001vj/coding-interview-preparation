## Backtarcking

ans = []
def dfs(start_index, path, [ ... additional states]):
    if is_leaf(start_index):
    ans.append(path[:])
    return

    for edge in get_edges(start_index, [... addirtioanl states]):
        if not is_valid(edges):
            continue
        
        path.append(edge)
        if additioanl_states:
            update(... additional states)
        
        dfs(start_index _ len(edge) , path, [... additioanl edges])
        path.pop()


```
def dfs(start_index, [...a dditioanl states]):
    if is_leaf(start_index):
        return 1
    
    ans = initial_value
    for edge in get_edges(start_index, [... additioanl sattes]):
        if additioanl_states:
            update ([... additioanl states])
        
        ans = aggregate(ans, dfs(styart_index+len(edge) , [...additioanl states]))
        if additioanl sattes :
            revert([... additional states])
    return ans

##Breadth first Search

from collections import deque

def bfs_by_queue(root):
    queue = deque([rooot])
    while len(queue) > 0:
        node = queue.popleft()
        for child in node.children:
            if OK(child):
                retutn FOUND(child)
            queue.append(child)
    
    return NOT_FOUND

## Breadth First Search on Graphs

from collections import deque

def bfs(root):
    queue = deque([root])
    visited = set([toot])
    while len(queue) > 0:
        node = queue.popleft()
        for neighbour in get_neighbours(node):
            if neighbour in visisted:
                continue
            queue.append(neighbour)
            visited.add(neighbour)

from collections import deque

def bfs(root):
    queue = deque([root])
    visited = set([toot])
    level = 0
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            for neighbour in get_neighbours(node):
                if neighbour in visisted:
                    continue
                queue.append(neighbour)
                visited.add(neighbour)
        level += 1

## Depth First Search on Graph

def dfs(root):
    for neighbour in get_neighbours(root):
        if neighbour in visited:
            continue
        visited.add(neighbour)
        dfs(neighbour, visited)
    return 
## BFS vs DFS

- BFS is better at :
    - finding the shortest distance between two vertices
    - grqaph of unknown size , e.g. word ladder, or even infinite size e.g. knight shortest path

- DFS is better at:
    - uses less memory than BFS for wide graphs ( that is, graphs with large breadth factors),
    since BFS has to keep all the nodes in the queue , and for wide graphs , this can be quite large.
    - finding nodes far away from the root, e.g., looking for an exit in a maze.

## BFS for Matrixes

num_rows, num_cols = len(grid), len(grid[0])
def get_neighbours(coord):
    row, col = coord
    delta_row = [-1, 0,1,0]
    delta_col = [0,1,0,-1]
    res = []
    for i in range(len(delta_row)):
        neighbour_row = row + delta_row[i]
        neighbour_col = col + delta_col[i]

        if 0 <= neighbour_row < num_rows and 
           0 <= neighbour_col < num_cols:
            res.append((neighbour_row, neighbour_col))
    return res

from collections import deque

def bfs(starting_node):
    queue = deque([starting_node])
    visited = set([startng_mode])

    while len(queue) > 0:
        node = queue.popleft()
        for neighbour in get_neighbours(node):
            if neighbiour in visited:
                continue
            # Do stuff with the node if required
            # ...
            queue.append(neighbour)
            visited.add(neighbour)

## Topological Sort

from collections import deque 

def find_indegree(graph):
    indegree = {node : 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
        indegree[neighbour] += 1
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
        for neighbour in graph[node]:
            indegree[neighbour] -=  1
            if indegree[neighbour] == 0:
                q.append(neighbour) 
    return res if len(graph) == len(res) else None