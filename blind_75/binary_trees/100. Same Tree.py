# https://leetcode.com/problems/same-tree/description/
# 100. Same Tree
# Easy
# Topics
# Companies
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q) or (p.val != q.val):
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p, q)


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Recursive DFS (Most intuitive)
def isSameTree_recursive(p: TreeNode, q: TreeNode) -> bool:
    """
    Time: O(min(n,m)) where n,m are tree sizes
    Space: O(min(h1,h2)) for recursion stack, h=height
    """
    # Base cases
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    # Check current nodes and recurse
    return (p.val == q.val and 
            isSameTree_recursive(p.left, q.left) and 
            isSameTree_recursive(p.right, q.right))

# Solution 2: Iterative BFS with Queue
from collections import deque
def isSameTree_bfs(p: TreeNode, q: TreeNode) -> bool:
    """
    Time: O(min(n,m))
    Space: O(w) where w is max width of tree
    """
    queue = deque([(p, q)])
    
    while queue:
        node1, node2 = queue.popleft()
        
        # Check current pair
        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
            
        # Add children
        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))
    
    return True

# Solution 3: Iterative DFS with Stack
def isSameTree_iterative(p: TreeNode, q: TreeNode) -> bool:
    """
    Time: O(min(n,m))
    Space: O(h) where h is height of tree
    """
    stack = [(p, q)]
    
    while stack:
        node1, node2 = stack.pop()
        
        # Check current pair
        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
            
        # Add children
        stack.append((node1.right, node2.right))
        stack.append((node1.left, node2.left))
    
    return True

# Solution 4: Serialize and Compare (For discussion)
def isSameTree_serialize(p: TreeNode, q: TreeNode) -> bool:
    """
    Time: O(n+m)
    Space: O(n+m)
    Not efficient but interesting approach
    """
    def serialize(root: TreeNode) -> str:
        if not root:
            return "null"
        return f"{root.val},{serialize(root.left)},{serialize(root.right)}"
    
    return serialize(p) == serialize(q)

# Visualization helper
def visualize_comparison(p: TreeNode, q: TreeNode):
    """
    Visualizes the tree comparison process
    """
    def print_tree(root: TreeNode, level: int = 0, prefix: str = "Root"):
        if not root:
            print("  " * level + f"{prefix}: None")
            return
        print("  " * level + f"{prefix}: {root.val}")
        if root.left or root.right:
            print_tree(root.left, level + 1, "L")
            print_tree(root.right, level + 1, "R")
    
    print("\nComparing Trees:")
    print("=" * 50)
    print("Tree 1:")
    print_tree(p)
    print("\nTree 2:")
    print_tree(q)
    
    def compare_nodes(node1: TreeNode, node2: TreeNode, level: int = 0, path: str = "Root"):
        """Shows detailed comparison process"""
        print("\n" + "-" * 20)
        print(f"Comparing at {path}:")
        
        if not node1 and not node2:
            print(f"Both nodes are None ✓")
            return True
            
        if not node1 or not node2:
            print(f"One node is None, other is {node1.val if node1 else node2.val} ✗")
            return False
            
        print(f"Values: {node1.val} vs {node2.val}")
        if node1.val != node2.val:
            print("Values don't match ✗")
            return False
            
        print("Values match ✓")
        left_same = compare_nodes(node1.left, node2.left, level + 1, path + "->L")
        right_same = compare_nodes(node1.right, node2.right, level + 1, path + "->R")
        
        return left_same and right_same
    
    result = compare_nodes(p, q)
    print("\nFinal result:", result)
    return result

# Test function
def test_solutions():
    # Create test cases
    test_cases = [
        # Case 1: Same trees
        (
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2), TreeNode(3))
        ),
        # Case 2: Different structure
        (
            TreeNode(1, TreeNode(2)),
            TreeNode(1, None, TreeNode(2))
        ),
        # Case 3: Different values
        (
            TreeNode(1, TreeNode(2), TreeNode(1)),
            TreeNode(1, TreeNode(1), TreeNode(2))
        ),
        # Case 4: Empty trees
        (None, None),
        # Case 5: One empty, one not
        (TreeNode(1), None)
    ]
    
    for i, (p, q) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print("=" * 50)
        
        results = {
            "Recursive": isSameTree_recursive(p, q),
            "BFS": isSameTree_bfs(p, q),
            "Iterative DFS": isSameTree_iterative(p, q),
            "Serialize": isSameTree_serialize(p, q)
        }
        
        print("Results:")
        for method, result in results.items():
            print(f"{method}: {result}")
            
        # Detailed visualization for first test case
        if i == 1:
            visualize_comparison(p, q)

# Run tests
test_solutions()