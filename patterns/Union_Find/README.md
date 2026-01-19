# Union-Find (Disjoint Set Union - DSU)

Union-Find is a data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It provides near-constant time operations to add new sets, merge existing sets, and determine whether elements are in the same set.

## Core Concepts
- **Parent Array:** `parent[i]` points to the parent of node `i`. If `parent[i] == i`, `i` is a root.
- **Find(x):** Follows parent pointers to find the root of `x`. Uses **Path Compression** (point nodes directly to root) for $O(1)$ amortized time.
- **Union(x, y):** Connects the roots of `x` and `y`. Uses **Union by Rank/Size** to keep trees flat.

## Pattern Variations & Examples

| Problem | Difficulty | Key Concept | Modification to Base Pattern |
|:---|:---|:---|:---|
| **[323. Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)** | Medium | **Base Pattern** | Standard implementation. Count starts at `N`, decrement every time `Union` returns `True`. |
| **[684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)** | Medium | **Cycle Detection** | Return the edge `[u, v]` if `Find(u) == Find(v)` (they are already connected). |
| **[547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)** | Medium | **Matrix -> Graph** | Input is an adjacency matrix. Iterate `grid[i][j] == 1` to perform unions. |
| **[721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)** | Medium | **String Mapping** | Map string emails to integer IDs. Union emails belonging to the same name. |
| **[990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)** | Medium | **Logic Check** | First process all `==` equations to build sets. Then process `!=` to check for contradictions (`Find(a) == Find(b)` is a conflict). |

## Complexity
- **Time:** $O(\alpha(N))$ per operation, where $\alpha$ is the Inverse Ackermann function (nearly constant, $\le 4$ for all practical $N$).
- **Space:** $O(N)$ for parent and rank arrays.

## Visualization
Run the included python script to see the "Redundant Connection" problem visualized, demonstrating how sets merge and how cycles are detected.
