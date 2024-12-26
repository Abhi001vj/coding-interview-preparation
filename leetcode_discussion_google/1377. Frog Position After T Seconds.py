# https://leetcode.com/problems/frog-position-after-t-seconds/description/

# Code


# Testcase
# Testcase
# Test Result
# 1377. Frog Position After T Seconds
# Solved
# Hard
# Topics
# Companies
# Hint
# Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.

# Return the probability that after t seconds the frog is on the vertex target. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:


# Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
# Output: 0.16666666666666666 
# Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
# Example 2:


# Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
# Output: 0.3333333333333333
# Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 
 

# Constraints:

# 1 <= n <= 100
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ai, bi <= n
# 1 <= t <= 50
# 1 <= target <= n
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 33.1K
# Submissions
# 92.9K
# Acceptance Rate
# 35.6%
# Topics
# Companies
# Hint 1
# Use a variation of DFS with parameters 'curent_vertex' and 'current_time'.
# Hint 2
# Update the probability considering to jump to one of the children vertices.

from collections import defaultdict, deque
from typing import List

class Solution:
    """
    Problem Breakdown:
    -----------------
    1. We have an undirected tree with n vertices (1 to n)
    2. Frog starts at vertex 1
    3. Each second:
       - Frog jumps to an unvisited neighbor
       - Equal probability for all possible unvisited neighbors
       - If no unvisited neighbors, stays on current vertex
    4. Need to find probability of being on target vertex after exactly t seconds

    Pattern Recognition:
    ------------------
    1. Graph Traversal Problem
    2. Probability calculation
    3. Tree structure (no cycles)
    4. BFS/DFS with state tracking

    Example Visualization:
    --------------------
    For n=7, edges=[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t=2, target=4

          1
       /  |  \
      2   3   7
     / \   \
    4   6   5

    Path to target=4:
    1 -> 2 -> 4

    Time 0: Start at 1
    Time 1: Can jump to 2(1/3), 3(1/3), or 7(1/3)
    Time 2: If at 2, can jump to 4(1/2) or 6(1/2)
    
    Probability = 1/3 * 1/2 = 1/6

    Approaches:
    ----------
    1. BFS (Optimal) - O(n) time, O(n) space
    2. DFS (Alternative) - O(n) time, O(n) space
    """
    
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        """
        Optimal Solution using BFS
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(n) - for adjacency list and queue
        
        Key Ideas:
        1. Build adjacency list to represent tree
        2. Use BFS to track possible positions and probabilities
        3. Handle special cases (t too small/large)
        4. Track visited nodes to handle "unvisited" constraint
        """
        if n == 1:
            return 1.0 if target == 1 else 0.0
        
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Queue entries: (node, probability, time, visited_nodes)
        queue = deque([(1, 1.0, 0, {1})])
        
        while queue and t >= 0:
            node, prob, time, visited = queue.popleft()
            
            # Find unvisited neighbors
            unvisited = [next_node for next_node in graph[node] 
                        if next_node not in visited]
            
            # If we're at target
            if node == target:
                # Return probability if:
                # 1. We've used exactly t seconds, or
                # 2. We have no more moves and haven't exceeded t
                if time == t or (not unvisited and time <= t):
                    return prob
                # If we have more moves or haven't reached t, continue
                if not unvisited or time >= t:
                    return 0.0
            
            # If we have unvisited neighbors, distribute probability
            if unvisited:
                next_prob = prob / len(unvisited)
                for next_node in unvisited:
                    new_visited = visited | {next_node}
                    queue.append((next_node, next_prob, time + 1, new_visited))
        
        return 0.0

    """
    Alternative DFS Solution (for comparison):
    
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0
            
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node, prob, time, visited):
            if time > t:
                return 0.0
                
            unvisited = [next_node for next_node in graph[node] 
                        if next_node not in visited]
                
            if node == target:
                if time == t or (not unvisited and time <= t):
                    return prob
                return 0.0
                
            if not unvisited or time >= t:
                return 0.0
                
            total_prob = 0.0
            next_prob = prob / len(unvisited)
            
            for next_node in unvisited:
                total_prob += dfs(next_node, next_prob, time + 1, 
                                visited | {next_node})
                
            return total_prob
            
        return dfs(1, 1.0, 0, {1})
    """