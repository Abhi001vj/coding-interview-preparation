# https://leetcode.com/problems/clone-graph/description/
# 133. Clone Graph
# Medium
# Topics
# Companies
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

# Example 1:


# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# Example 2:


# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
# Example 3:

# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
 

# Constraints:

# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Dictionary to store visited nodes and their clones
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            # Create clone of current node
            clone = Node(node.val)
            # Add to visited before processing neighbors
            visited[node] = clone
            
            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
        
        return dfs(node)

# Helper functions to convert between adjacency list and Node format
def buildGraph(adjList):
    if not adjList:
        return None
    
    # Create all nodes first
    nodes = [Node(i+1) for i in range(len(adjList))]
    
    # Add neighbors
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]  # j-1 because values are 1-indexed
    
    return nodes[0] if nodes else None

def graphToAdjList(node):
    if not node:
        return []
        
    visited = set()
    adj_list = []
    
    def dfs(node):
        if node in visited:
            return
        
        # Ensure the list has enough spots
        while len(adj_list) < node.val:
            adj_list.append([])
            
        visited.add(node)
        neighbors = [neighbor.val for neighbor in node.neighbors]
        adj_list[node.val - 1] = neighbors
        
        for neighbor in node.neighbors:
            dfs(neighbor)
    
    dfs(node)
    return adj_list

# Test
def test():
    # Test case 1
    adj_list = [[2,4],[1,3],[2,4],[1,3]]
    
    # Convert adjacency list to Node format
    test_node = buildGraph(adj_list)
    
    # Clone the graph
    solution = Solution()
    cloned = solution.cloneGraph(test_node)
    
    # Convert back to adjacency list for verification
    result = graphToAdjList(cloned)
    print(f"Input: {adj_list}")
    print(f"Output: {result}")
    print(f"Are equal? {adj_list == result}")

# Run test
test()


from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = [node]
        visited = {node: Node(node.val)}  # Map original node to its clone
        count = 0
        while queue:
            current = queue.pop(0)
            # Process all neighbors of current node
            for neighbor in current.neighbors:
                # If neighbor hasn't been cloned yet
                if neighbor not in visited:
                    # Create clone of neighbor
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Add cloned neighbor to current node's clone's neighbors list
                visited[current].neighbors.append(visited[neighbor])
        
        return visited[node]  # Return clone of the starting node