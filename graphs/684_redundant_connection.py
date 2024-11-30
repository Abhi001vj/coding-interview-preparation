# https://leetcode.com/problems/redundant-connection/description/
#  684. Redundant Connection
# Solved
# Medium
# Topics
# Companies
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
 

# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
# 1. Cycle Detection (DFS)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):
            if visit[node]:
                return True
            
            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n + 1)
            
            if dfs(u, -1):
                return [u, v]
        return []
Time & Space Complexity
Time complexity: 
O
(
E
∗
(
V
+
E
)
)
O(E∗(V+E))
Space complexity: 
O
(
V
+
E
)
O(V+E)
Where 
V
V is the number of vertices and 
E
E is the number of edges in the graph.
2. Depth First Search (Optimal)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1
        
        def dfs(node, par):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True  
            
            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1, -1)
        
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []
Time & Space Complexity
Time complexity: 
O
(
V
+
E
)
O(V+E)
Space complexity: 
O
(
V
+
E
)
O(V+E)
Where 
V
V is the number of vertices and 
E
E is the number of edges in the graph.
3. Kanh's Algorithm (BFS)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        for u, v in edges[::-1]:
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []
Time & Space Complexity
Time complexity: 
O
(
V
+
E
)
O(V+E)
Space complexity: 
O
(
V
+
E
)
O(V+E)
Where 
V
V is the number of vertices and 
E
E is the number of edges in the graph.
4. Disjoint Set Union
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
Time & Space Complexity
Time complexity: 
O
(
V
+
(
E
∗
α
(
V
)
)
)
O(V+(E∗α(V)))
Space complexity: 
O
(
V
)
O(V)
Where 
V
V is the number of vertices and 
E
E is the number of edges in the graph. 
α
(
)
α() is used for amortized complexity.