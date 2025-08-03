🧩 Union-Find (Disjoint Set Union or DSU) Master Reference
Union-Find efficiently supports two operations:

find(x): Locate the root (representative) of x’s set.

union(x, y): Merge the sets containing x and y.

Used to track connected components, group merges, and connectivity in graphs or sets.

⚙️ Optimizations: With vs Without Rank
Optimization	With Rank (Balanced)	Without Rank (Simple)
Path Compression	✅ Always used. Flattens the tree during find()	✅ Always used. Essential for efficiency
Union Strategy	Attach shallower (or smaller) tree under deeper one	Always attach one root to another without checks
Tree Balance	✅ Ensured with rank or size	❌ May lead to unbalanced trees
Performance	Near constant O(α(N)) per op	Can degrade to O(N) in unlucky merge orders
Memory	Slightly more (extra rank or size array/dict)	Minimal memory; just parent
Use Case	✅ For large, performance-sensitive graphs	✅ For small inputs or dynamic keys (like emails)

✅ Side-by-Side Template Comparison
📦 Without Rank (Dynamic, Simple)
python
Copy
Edit
class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)  # No balancing
⚖️ With Rank (Balanced, Optimal)
python
Copy
Edit
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
🧠 Use-Case Based Decision Matrix
Scenario	Use Rank?	Why?
Small inputs (n ≤ 100)	❌	Overhead not worth it
Dynamic data like email IDs or strings	❌ (use dict)	Rank adds complexity
Competitive programming or large datasets	✅	Performance matters
Many union operations	✅	Prevents deep trees
Offline merges (e.g., Kruskal’s MST)	❌	Merge once, no repeated unions
Grid region merging	✅	Usually N is large

🧪 Rank vs Size
Metric	Rank	Size
Meaning	Depth of tree	Number of elements in set
Use	Attach shallower under deeper	Attach smaller set under larger
Result	Balanced trees	Balanced trees

Both are used to avoid deep chains like:

Copy
Edit
1 - 2 - 3 - 4 - 5 ...
🔍 Problem-Wise DSU Usage Table
Leetcode Problem	DSU?	Path Compression	Rank?	Why?
128. Longest Consecutive Sequence	✅	✅	❌	Link num → num+1 clusters
200. Number of Islands	✅	✅	✅	Merge adjacent land using flat index
130. Surrounded Regions	✅	✅	✅	Dummy border node for escape detection
721. Accounts Merge	✅	✅	✅/❌	Emails as nodes; dynamic DSU (dict)
1631. Path With Minimum Effort	✅	✅	✅	Kruskal-like DSU to connect cells
1254. Number of Closed Islands	✅	✅	✅	Mark border-connected islands via dummy
778. Swim in Rising Water	✅	✅	✅	Sort edges, connect until start/end connected
785. Is Graph Bipartite?	❌	❌	❌	BFS/DFS coloring more appropriate
695. Max Area of Island	❌	❌	❌	Only flood-fill; no merging needed

🧩 DSU Pattern Variants Summary
Pattern	Notes
Naive DSU	No compression, no rank — slow
Path Compression Only	Your email merge example
Rank + Compression	Standard in heavy-use scenarios
Dynamic DSU	Keys can be strings or tuples; use dict
Grid DSU	Convert (i, j) to i * n + j
Offline DSU	E.g., Kruskal’s MST — sorted queries
Rollback DSU	For undoable merges in segment tree/DP

📌 Quick Cheatsheet: Should You Use Union-Find?
Problem Clue	Use Union-Find?
"Merge accounts"	✅
"Merge groups"	✅
"How many connected components?"	✅
"Are x and y connected?"	✅
"Flood fill", "Size of region"	❌ (Use DFS/BFS)
"Coloring", "Bipartite check"	❌ (Use DFS/BFS)
"Minimum edges to connect"	✅ (Kruskal style)

🧠 When NOT to Use Rank
Very few union operations

Problem size is trivially small

All unions are one-time merges (offline DSU)

You use DSU just for structure, not speed

