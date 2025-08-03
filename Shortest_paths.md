# Graph Algorithms Reference Guide

## Algorithm Comparison Table

| # | Algorithm & Trigger Words | Edge Weights | Graph Type / Constraints | Stops / Edge-Count Limit? | Time | Extra Space | Typical LC Problems |
|---|---------------------------|--------------|--------------------------|---------------------------|------|-------------|---------------------|
| 1 | **Breadth-First Search (BFS)**<br/>"un-weighted", "each step = cost 1" | 0/1 or equal | Any, usually sparse | No limit | O(V + E) | O(V) | 1926 (Nearest Exit in Maze), 200 (Island Ladders), 994 (Rotting Oranges) |
| 2 | **0-1 BFS (deque)** | edge ∈ {0,1} | Any | No limit | O(V + E) | O(V) | 1368 (Min Cost to Make Path), 847 (Shortest Path in Graph with 0/1 Edges) |
| 3 | **Dijkstra (min-heap)** | positive | Sparse / non-neg | No limit | O((V + E) log V) | O(V) | 743 (Network Delay), 1631 (Path With Min Effort), 1514 (Path With Prob) |
| 4 | **Bellman–Ford** | Negative allowed, small bound on edges (k stops) or want neg-cycle detect | Any | Optional ≤ k by truncating loops | O(K · E) | O(V) | 787 (Cheapest Flights Within K Stops) – truncated; Bellman–Ford proper for neg cycles |
| 5 | **SPFA (queue-based BF)** | Negative, no tight edge bound | Sparse, practical | No | Amortised faster than BF, worst O(KE) | O(V) | Rare in LC (but sometimes used for grids with −ve cost portals) |
| 6 | **Topo-DP on DAG** | Any (can include negative) | Directed Acyclic | No limit | O(V + E) | O(V) | 1494 (Parallel Courses II), 472 (Concatenated Words — path len) |
| 7 | **Floyd-Warshall** | Any, incl. negative (no neg cycles) | Dense, need all-pairs | No limit | O(V³) | O(V²) | 1334 (Find City With Smallest Reach), 2642 (Crit City) |
| 8 | **Multi-source BFS / Dijkstra** | See 1–3 | Many sources simultaneously | No | As per algo | As per algo | 505 (The Maze II), 310 (Min Height Trees) |
| 9 | **A* (Heuristic Dijkstra)** | Positive | Grid / coordinate with good heuristic | No | Best-case sub-Dijkstra | O(V) worst | O(V) |

## Mini Code Templates

### 1. BFS (unit cost)

```python
from collections import deque

def bfs(start):
    dist = {start: 0}
    dq = deque([start])
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                dq.append(v)
    return dist
```

### 2. Dijkstra (positive weights)

```python
import heapq

def dijkstra(src):
    INF = 10**18
    dist = [INF]*n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: 
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

### 3. Truncated Bellman-Ford (K edges)

```python
def k_edge_bellman(src, K):
    dist = [inf]*n
    dist[src] = 0
    for _ in range(K):
        nd = dist[:]            # snapshot
        for u, v, w in edges:
            if dist[u] != inf and dist[u]+w < nd[v]:
                nd[v] = dist[u]+w
        dist = nd
    return dist
```

### 4. Topological DP (DAG)

```python
def dag_shortest(src):
    topo = topological_sort()
    dist = [inf]*n
    dist[src] = 0
    for u in topo:
        if dist[u] == inf: 
            continue
        for v, w in adj[u]:
            dist[v] = min(dist[v], dist[u]+w)
    return dist
```

## How to Spot Which Algorithm to Apply

| Clue in prompt | Likely algorithm(s) |
|----------------|---------------------|
| "each move costs 1 / minimum steps / unweighted grid" | BFS |
| "positive weights" & need single-source → cheapest route | Dijkstra |
| "at most k stops / edges" | Truncated Bellman–Ford or layered BFS |
| "negative edge weights, detect cycle" | Bellman–Ford (full) |
| "graph is acyclic / tasks have prerequisites" | Topological DP |
| "dense graph & need all-pairs" | Floyd–Warshall |
| "maze grid with heuristic distance" | A* |
| "multiple starting points infect/ spread" | Multi-source BFS / Dijkstra |

## Comparing Dijkstra vs. Truncated Bellman–Ford vs. BFS in LC 787

| Feature | Dijkstra | Truncated BF (code shown) | BFS |
|---------|----------|---------------------------|-----|
| **Edge weights** | Positive | Positive | Unit |
| **Stops limit** | Needs extra state ((node, stops)) making it O((k+1)E log V) | Natural: run ≤ k+1 rounds | Not valid (weights ≠ 1) |
| **Implementation** | Priority queue | Two arrays, k+1 passes | Simple |

The provided code chooses truncated Bellman–Ford because it's minimal for the "≤ k stops" constraint and small k (≤ 100 in the problem).

## Quick Heuristics to Modify Algorithms

- **Need path length constraint?** → add a loop counter in Bellman-Ford or add (node, steps) state in Dijkstra.
- **0/1 weights?** → convert Dijkstra's heap to a deque (0-1 BFS).
- **All targets same weight grid?** → BFS multi-source (set of starts).
- **Dense + small V?** → avoid heap overhead; simple O(V²) Dijkstra with array minimum extraction.
- **Huge E but small weights range?** → Dial's algorithm / buckets.

## TL;DR

1. **Check weight type** → unit / 0-1 / positive / negative.
2. **Check special constraints** → DAG, limited stops, multiple sources.
3. **Pick algorithm from the table, apply template, tweak as above.**