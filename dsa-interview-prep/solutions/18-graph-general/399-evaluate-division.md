# 399. Evaluate Division

**Difficulty:** Medium
**Pattern:** Graph Construction + DFS/BFS / Union Find

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable. You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the $j^{th}$ query where you must find the answer for `Cj / Dj = ?`.

**Interview Scenario (The "Currency Exchange" Prompt):**
"You are building a financial conversion service. You receive a stream of exchange rates (e.g., 'USD', 'EUR', 0.85). You need to answer queries about arbitrary currency pairs (e.g., 'How much is 1 USD in JPY?'). The direct rate might not be listed, but it might be inferable through a chain of intermediate currencies (e.g., USD -> EUR -> JPY). If a conversion is impossible or involves unknown currencies, return -1."

**Why this transformation?**
*   It grounds the abstract algebra in a very common real-world graph problem.
*   It highlights the transitive property: if $a/b = x$ and $b/c = y$, then $a/c = x \times y$. This is path multiplication in a graph.

---

## 2. Clarifying Questions (Phase 1)

1.  **Inverse Edges:** "If I know $A/B = 2.0$, do I automatically know $B/A$?" (Yes, it's $0.5$. This implies an undirected graph where edge weights differ by direction).
2.  **Disconnected Components:** "What if there is no path between $C$ and $D$?" (Return -1.0).
3.  **Unknown Variables:** "What if a query involves a variable we've never seen?" (Return -1.0).
4.  **Cycles/Conflicts:** "Are the equations consistent?" (Yes, assume no contradictions like $A/B=2$ and $A/B=3$).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Graph (Adjacency List) + DFS/BFS.

**The Logic:**
Represent variables as nodes and divisions as weighted directed edges.
*   Equation $A / B = k$ becomes:
    *   Edge $A \to B$ with weight $k$.
    *   Edge $B \to A$ with weight $1/k$.
*   Query $X / Y$ becomes:
    *   Find a path from $X$ to $Y$.
    *   The result is the *product* of all edge weights along the path.

**Example:**
$a/b = 2.0$, $b/c = 3.0$. Query $a/c$.
Path: $a \xrightarrow{2.0} b \xrightarrow{3.0} c$.
Result: $2.0 \times 3.0 = 6.0$.

---

## 4. Base Template & Modification

**Standard DFS Template:**
```python
def dfs(curr, target, visited):
    if curr == target: return 1.0
    visited.add(curr)
    for neighbor, weight in graph[curr]:
        if neighbor not in visited:
            res = dfs(neighbor, target, visited)
            if res != -1: return res * weight
    return -1
```

**Modified Logic:**
1.  Build the graph first from `equations` and `values`.
2.  Handle the case where start/end nodes don't exist in the graph immediately.
3.  Run DFS for each query (resetting `visited` set each time).

---

## 5. Optimal Solution

```python
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the Graph
        # graph[A][B] = weight means A / B = weight
        graph = defaultdict(dict)
        
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1.0 / value
            
        def dfs(start, end, visited):
            # Base Case 1: Unknown node
            if start not in graph or end not in graph:
                return -1.0
            
            # Base Case 2: Found target
            if start == end:
                return 1.0
            
            visited.add(start)
            
            # Explore neighbors
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    
                    if result != -1.0:
                        # Path found! Multiply weights
                        return weight * result
                        
            return -1.0

        # Step 2: Answer Queries
        results = []
        for c, d in queries:
            results.append(dfs(c, d, set()))
            
        return results
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(Q \times (V + E))$
    *   $V$ is the number of unique variables, $E$ is the number of equations.
    *   For each of the $Q$ queries, we might traverse the entire graph in the worst case (DFS).
    *   *Note:* Can be optimized to $O((V+E) + Q)$ using **Union-Find with Path Compression**, effectively making queries $O(1)$ amortized. However, DFS is usually sufficient and easier to implement in an interview unless $Q$ is massive.
*   **Space Complexity:** $O(V + E)$
    *   To store the graph.

---

## 7. Follow-up & Extensions

**Q: Optimize for massive number of queries?**
**A:** Use **Union-Find (Disjoint Set Union)** with weight tracking.
*   `parent[x] = (root, weight_to_root)`.
*   When finding `x` and `y`, if they share the same root, answer is `(weight_x_to_root / weight_y_to_root)` (or similar derivation).
*   This precomputes the components, making queries nearly $O(1)$.

**Q: What if graph is dynamic (rates update)?**
**A:** Union-Find is harder to update. A BFS/DFS approach is better for dynamic graphs, or Floyd-Warshall if $V$ is small (for all-pairs precomputation).

```