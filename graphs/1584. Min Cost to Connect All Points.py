# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
# 1584. Min Cost to Connect All Points
# Medium
# Topics
# Companies
# Hint
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:


# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
 

# Constraints:

# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.

```python
"""
Minimum Cost to Connect All Points - Comprehensive Solution Analysis
===============================================================

This is a Minimum Spanning Tree (MST) problem where:
1. Vertices are the points
2. Edges are the Manhattan distances between points
3. Goal is to find MST with minimum total cost

We'll implement multiple approaches:
1. Kruskal's Algorithm with Union-Find
2. Prim's Algorithm with Priority Queue
3. Optimized Prim's with Arrays
"""

from typing import List
import heapq
from collections import defaultdict

class UnionFind:
    """
    Union-Find data structure for Kruskal's algorithm.
    Implements path compression and union by rank.
    """
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class MinCostConnection:
    def approach1_kruskals(self, points: List[List[int]]) -> int:
        """
        Kruskal's Algorithm Implementation
        
        Visual Process for points = [[0,0],[2,2],[3,10],[5,2],[7,0]]:
        
        1. Sort all edges by weight:
        (0,1): 4  - between [0,0] and [2,2]
        (1,3): 3  - between [2,2] and [5,2]
        (3,4): 4  - between [5,2] and [7,0]
        ...and so on
        
        2. Add edges if they don't create cycle:
        Step 1: Add (1,3) cost=3
        [0,0]   [2,2]---[5,2]   [7,0]
                   |
                [3,10]
                
        Step 2: Add (0,1) cost=4
        [0,0]---[2,2]---[5,2]   [7,0]
                   |
                [3,10]
        
        And continue...
        """
        if not points:
            return 0
            
        n = len(points)
        edges = []  # Store all edges with weights
        
        # Create all edges with their weights
        for i in range(n):
            for j in range(i + 1, n):
                weight = abs(points[i][0] - points[j][0]) + \
                        abs(points[i][1] - points[j][1])
                edges.append((weight, i, j))
        
        # Sort edges by weight
        edges.sort()
        
        # Initialize Union-Find
        uf = UnionFind(n)
        total_cost = 0
        edges_used = 0
        
        # Process edges in order of increasing weight
        for weight, u, v in edges:
            if not uf.connected(u, v):
                uf.union(u, v)
                total_cost += weight
                edges_used += 1
                if edges_used == n - 1:
                    break
        
        return total_cost

    def approach2_prims(self, points: List[List[int]]) -> int:
        """
        Prim's Algorithm with Priority Queue
        
        Visual Process:
        Start from first point, gradually grow MST
        
        1. Initial state (starting from [0,0]):
        [0,0]   [2,2]   [3,10]   [5,2]   [7,0]
         *
        
        2. Add closest point ([2,2]):
        [0,0]---[2,2]   [3,10]   [5,2]   [7,0]
         *       *
        
        Continue until all points connected...
        """
        n = len(points)
        if n <= 1:
            return 0
            
        # Initialize data structures
        pq = [(0, 0)]  # (cost, vertex)
        visited = set()
        total_cost = 0
        
        while pq and len(visited) < n:
            cost, curr = heapq.heappop(pq)
            
            if curr in visited:
                continue
                
            visited.add(curr)
            total_cost += cost
            
            # Add edges to unvisited neighbors
            for next_vertex in range(n):
                if next_vertex not in visited:
                    distance = abs(points[curr][0] - points[next_vertex][0]) + \
                             abs(points[curr][1] - points[next_vertex][1])
                    heapq.heappush(pq, (distance, next_vertex))
        
        return total_cost

    def approach3_optimized_prims(self, points: List[List[int]]) -> int:
        """
        Optimized Prim's Algorithm using Arrays
        
        Instead of PQ, use array to track minimum distances.
        More efficient for dense graphs.
        
        Visual State Tracking:
        distances[i] = minimum distance from MST to point i
        
        Initial:  [∞, ∞, ∞, ∞, ∞]
        Step 1:   [0, 4, 13, 7, 7]
        Step 2:   [0, 0, 10, 3, 7]
        ...and so on
        """
        n = len(points)
        
        # Initialize tracking arrays
        distances = [float('inf')] * n  # Distance to MST
        distances[0] = 0
        visited = [False] * n
        total_cost = 0
        
        # Process all points
        for _ in range(n):
            # Find unvisited vertex with minimum distance
            curr_vertex = -1
            curr_distance = float('inf')
            for vertex in range(n):
                if not visited[vertex] and distances[vertex] < curr_distance:
                    curr_vertex = vertex
                    curr_distance = distances[vertex]
            
            # Mark current vertex as visited and add its cost
            visited[curr_vertex] = True
            total_cost += curr_distance
            
            # Update distances for unvisited neighbors
            for next_vertex in range(n):
                if not visited[next_vertex]:
                    distance = abs(points[curr_vertex][0] - points[next_vertex][0]) + \
                             abs(points[curr_vertex][1] - points[next_vertex][1])
                    distances[next_vertex] = min(distances[next_vertex], distance)
        
        return total_cost

    def visualize_mst_construction(self, points):
        """
        Visualize the MST construction process step by step.
        """
        n = len(points)
        print("\nMST Construction Visualization:")
        print("Points:", points)
        
        # Show initial state
        print("\nInitial state:")
        self._print_points_state(points, set())
        
        # Show growth of MST
        visited = set()
        visited.add(0)
        edges = []
        
        for step in range(n-1):
            min_cost = float('inf')
            min_edge = None
            
            # Find next edge to add
            for i in visited:
                for j in range(n):
                    if j not in visited:
                        cost = abs(points[i][0] - points[j][0]) + \
                               abs(points[i][1] - points[j][1])
                        if cost < min_cost:
                            min_cost = cost
                            min_edge = (i, j)
            
            if min_edge:
                visited.add(min_edge[1])
                edges.append(min_edge)
                print(f"\nStep {step+1}:")
                self._print_points_state(points, visited, edges)

    def _print_points_state(self, points, visited, edges=[]):
        """Helper function to print current state of MST construction."""
        # Create ASCII art representation
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)
        
        scale = 2  # Scale factor for better visualization
        grid = [[' ' for _ in range((max_x-min_x+1)*scale)] 
                for _ in range((max_y-min_y+1)*scale)]
        
        # Plot points
        for i, point in enumerate(points):
            x = (point[0] - min_x) * scale
            y = (point[1] - min_y) * scale
            grid[y][x] = '*' if i in visited else 'o'
        
        # Plot edges
        for u, v in edges:
            x1 = (points[u][0] - min_x) * scale
            y1 = (points[u][1] - min_y) * scale
            x2 = (points[v][0] - min_x) * scale
            y2 = (points[v][1] - min_y) * scale
            
            # Draw simple line
            if x1 == x2:  # Vertical line
                for y in range(min(y1, y2), max(y1, y2)+1):
                    if grid[y][x1] not in {'*', 'o'}:
                        grid[y][x1] = '|'
            elif y1 == y2:  # Horizontal line
                for x in range(min(x1, x2), max(x1, x2)+1):
                    if grid[y1][x] not in {'*', 'o'}:
                        grid[y1][x] = '-'
        
        # Print grid
        for row in grid:
            print(''.join(row))

def main():
    """
    Demonstrate and test all approaches with visualization.
    """
    test_cases = [
        [[0,0],[2,2],[3,10],[5,2],[7,0]],
        [[3,12],[-2,5],[-4,1]]
    ]
    
    solution = MinCostConnection()
    
    for points in test_cases:
        print("\n" + "="*50)
        print(f"Testing with points: {points}")
        
        # Visualize MST construction
        solution.visualize_mst_construction(points)
        
        # Compare results from all approaches
        result1 = solution.approach1_kruskals(points)
        result2 = solution.approach2_prims(points)
        result3 = solution.approach3_optimized_prims(points)
        
        print(f"\nResults:")
        print(f"Kruskal's: {result1}")
        print(f"Prim's: {result2}")
        print(f"Optimized Prim's: {result3}")

if __name__ == "__main__":
    main()

"""
Interview Tips:

1. Algorithm Selection:
   - Kruskal's: Better for sparse graphs
   - Prim's: Better for dense graphs
   - Optimized Prim's: Best for this specific problem

2. Time Complexity Analysis:
   - Kruskal's: O(E log E) for sorting edges
   - Prim's with PQ: O(E log V)
   - Optimized Prim's: O(V²)

3. Space Complexity:
   - Kruskal's: O(V) for Union-Find
   - Prim's: O(V) for visited set and PQ
   - Optimized Prim's: O(V) for distance array

4. Follow-up Questions:
   - How to handle dynamic point additions?
   - What if points are in 3D space?
   - How to parallelize for large datasets?
   - How to handle floating-point coordinates?
"""
```

This solution provides:
1. Multiple implementation approaches
2. Detailed visualizations
3. Step-by-step construction process
4. Performance analysis
5. Interview tips and follow-ups

The visualization helps understand how each algorithm:
1. Builds the MST incrementally
2. Makes decisions about which edges to include
3. Avoids cycles
4. Minimizes total cost

Would you like me to:
1. Explain any specific approach in more detail?
2. Add more visualization features?
3. Discuss specific optimizations?
4. Cover additional variations of the problem?