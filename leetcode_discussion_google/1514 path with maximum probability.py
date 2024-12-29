# https://leetcode.com/problems/path-with-maximum-probability/description/
# 1514. Path with Maximum Probability
# Medium
# Topics
# Companies
# Hint
# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

# Example 1:



# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
# Example 2:



# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
# Output: 0.30000
# Example 3:



# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.
 

# Constraints:

# 2 <= n <= 10^4
# 0 <= start, end < n
# start != end
# 0 <= a, b < n
# a != b
# 0 <= succProb.length == edges.length <= 2*10^4
# 0 <= succProb[i] <= 1
# There is at most one edge between every two nodes.
# Hint 1
# Multiplying probabilities will result in precision errors.
# Hint 2
# Take log probabilities to sum up numbers instead of multiplying them.
# Hint 3
# Use Dijkstra's algorithm to find the minimum path between the two nodes after negating all costs.


"""
Path with Maximum Probability - Comprehensive Solution
Time Complexity Analysis:
1. Brute Force (DFS): O(n!) - exploring all possible paths
2. Dijkstra's Algorithm: O((V + E)logV) where V is vertices and E is edges
3. Space Complexity: O(V + E) for adjacency list and priority queue

Problem Understanding:
- We have an undirected weighted graph where weights are probabilities
- Need to find path from start to end with maximum probability
- Probability of a path is the product of probabilities of its edges
- Return 0 if no path exists

Key Insights:
1. Since we multiply probabilities, taking -log transforms the problem into finding shortest path
2. Dijkstra's algorithm can be modified to handle maximum probability
3. Using priority queue gives us optimal performance

Example Visualization for n=3, edges=[[0,1],[1,2],[0,2]], succProb=[0.5,0.5,0.2]:

Graph Structure:
    0.5
0 -------- 1
|\         |
| \        | 0.5
|  \       |
|   \      |
|    \     |
|     \    |
|      \   |
|       \  |
|        \ |
|         \|
2 ----------
     0.2

Possible Paths:
1. 0 -> 2 (direct)
   Probability: 0.2

2. 0 -> 1 -> 2
   Probability: 0.5 * 0.5 = 0.25 (This is the maximum)
"""

from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], 
                      start: int, end: int) -> float:
        # Build adjacency list with probabilities
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))  # undirected graph
        
        # Initialize max heap (using negative for max heap in Python)
        # Format: (-probability_so_far, node)
        max_heap = [(-1.0, start)]
        
        # Track best probabilities seen so far
        best_prob = [0.0] * n
        best_prob[start] = 1.0
        
        while max_heap:
            prob_so_far, curr = heapq.heappop(max_heap)
            prob_so_far = -prob_so_far  # Convert back to positive
            
            # If we've found better path already, skip
            if prob_so_far < best_prob[curr]:
                continue
            
            # Check all neighbors
            for next_node, edge_prob in graph[curr]:
                new_prob = prob_so_far * edge_prob
                
                # Only proceed if we found better probability
                if new_prob > best_prob[next_node]:
                    best_prob[next_node] = new_prob
                    heapq.heappush(max_heap, (-new_prob, next_node))
        
        return best_prob[end]

    """
    Alternative Solutions:

    1. Brute Force DFS (not implemented due to exponential complexity):
    - Try all possible paths using DFS
    - Keep track of maximum probability seen so far
    - Time complexity: O(n!)
    - Space complexity: O(n) for recursion stack

    def maxProbabilityBruteForce(self, n, edges, succProb, start, end):
        def dfs(node, visited, prob_so_far):
            if node == end:
                return prob_so_far
            max_prob = 0
            visited.add(node)
            for next_node, edge_prob in graph[node]:
                if next_node not in visited:
                    max_prob = max(max_prob, 
                                 dfs(next_node, visited, prob_so_far * edge_prob))
            visited.remove(node)
            return max_prob

    2. Dynamic Programming (not optimal for this case):
    - Would work for DAGs but this is an undirected graph
    - Could have cycles which makes DP complicated
    - Would need additional state to handle cycles

    Why Dijkstra's is Optimal:
    1. Handles cycles naturally
    2. Always processes highest probability paths first
    3. Can terminate early when we find the target
    4. Works with undirected graphs
    5. Efficient O((V + E)logV) time complexity
    """