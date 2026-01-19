# Union-Find (DSU) Study Guide

**Pattern:** Disjoint Set Union (DSU)  
**Common Applications:** Connectivity, Cycle Detection, Merging Sets, Kruskal's MST  

---

## 1. The Core Intuition

Imagine you are at a party where everyone is a stranger.
- Initially, everyone is in their own "group" of size 1.
- You see Person A shake hands with Person B. **UNION!** Now {A, B} are a group.
- Person B shakes hands with Person C. **UNION!** Now {A, B, C} are a group.
- Person A wants to introduce Person D to Person C.
- **FIND:** You ask "Who is A's leader?" (let's say A). You ask "Who is D's leader?" (let's say D).
- Since Leader(A) != Leader(D), they are different groups. You merge them.

**The "Redundant Connection" Twist:**
- What if Person A shakes hands with Person C?
- You check: Leader(A) is A. Leader(C) is A (because they are already in the group).
- **Leader(A) == Leader(C)**.
- This handshake is useless! They are already connected. **This is a cycle.**

---

## 2. The Algorithm (Path Compression + Union by Rank)

The naive approach (following parent pointers) can be $O(N)$ (a long line). We optimize it to $O(1)$ amortized.

### Optimization 1: Path Compression
When we call `find(x)`, we don't just return the root. We make `x` (and all ancestors we visit) point **directly** to the root.
```python
def find(self, x):
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x]) # Direct link to grandpa!
    return self.parent[x]
```

### Optimization 2: Union by Rank
Always attach the **shorter** tree to the **taller** tree. This keeps the tree height logarithmic.

---

## 3. Template Code (Memorize This)

```python
class DSU:
    def __init__(self, n):
        # Nodes are 1-indexed usually, so size n+1
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1) # Or size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Attach smaller rank to larger rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True # Merged
        return False # Cycle detected
```

## 4. Key Problem: Redundant Connection (LC 684)

**Problem:** You have a graph that is a tree + 1 extra edge. Find that edge.
**Solution:** Iterate through edges. The first edge `(u, v)` where `find(u) == find(v)` is the answer.

**Why DSU?**
- BFS/DFS: $O(N)$ per edge check -> $O(N^2)$ total.
- DSU: $O(1)$ per edge check -> $O(N)$ total.

---

## 5. Variations

1.  **Count Connected Components:**
    - Initialize `count = N`.
    - Every successful `union(u, v)` (where roots were different), do `count -= 1`.
    - Final answer is `count`.

2.  **String Inputs (Accounts Merge):**
    - Map strings to integers `0..N-1` using a hash map `email_to_id`.
    - Run standard integer DSU.

3.  **2D Grid (Number of Islands):**
    - Flatten 2D `(r, c)` to 1D index `r * cols + c`.
    - Union adjacent `1`s.
