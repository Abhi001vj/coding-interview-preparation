# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
# 1448. Count Good Nodes in Binary Tree
# Medium
# Topics
# Companies
# Hint
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

 

# Example 1:



# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# Example 2:



# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# Example 3:

# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
 

# Constraints:

# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].
"""
Count Good Nodes in Binary Tree - Comprehensive Solution
====================================================

Problem Definition:
-----------------
A node X is considered "good" if in the path from root to X there are no nodes 
with values greater than X's value. Count all good nodes in the binary tree.

Visual Examples:
--------------
Example 1:
       3                Good nodes: [3,4,5,3]
     /   \              - 3 (root) is always good
    1     4             - 4 is good (path: 3->4)
   /     / \            - 5 is good (path: 3->4->5)
  3     1   5           - 3 is good (path: 3->1->3)

Example 2:
       3                Good nodes: [3,3,4]
      /                 - 3 (root) is good
     3                  - 3 is good (path: 3->3)
    / \                 - 4 is good (path: 3->3->4)
   4   2                - 2 is not good (3 > 2 in path)
"""

from typing import Optional, List, Tuple
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class GoodNodesCounter:
    """
    Class containing different approaches to count good nodes in a binary tree.
    """
    
    def approach1_recursive_dfs(self, root: TreeNode) -> int:
        """
        DFS Approach with Path Maximum Tracking
        -------------------------------------
        Strategy:
        1. Track maximum value seen in path from root
        2. Node is good if its value >= path maximum
        3. Update path maximum while traversing down
        
        Time: O(n) - visit each node once
        Space: O(h) - recursion stack, h is height
        """
        def dfs(node: TreeNode, path_max: int) -> int:
            if not node:
                return 0
            
            # Current node is good if it's >= path maximum
            is_good = 1 if node.val >= path_max else 0
            
            # Update maximum for children
            current_max = max(path_max, node.val)
            
            # Recursively count good nodes in subtrees
            left_count = dfs(node.left, current_max)
            right_count = dfs(node.right, current_max)
            
            return is_good + left_count + right_count
        
        return dfs(root, root.val)

    def approach2_iterative_bfs(self, root: TreeNode) -> int:
        """
        BFS Approach with Queue-based Traversal
        ------------------------------------
        Strategy:
        1. Use queue to store (node, path_max) pairs
        2. Process level by level, tracking path maximum
        3. Count nodes where value >= path maximum
        
        Time: O(n) - visit each node once
        Space: O(w) - queue size, w is max width
        """
        if not root:
            return 0
            
        good_count = 0
        queue = deque([(root, float('-inf'))])
        
        while queue:
            node, path_max = queue.popleft()
            
            # Check if current node is good
            if node.val >= path_max:
                good_count += 1
            
            # Update maximum for children
            current_max = max(path_max, node.val)
            
            # Add children with updated path maximum
            if node.left:
                queue.append((node.left, current_max))
            if node.right:
                queue.append((node.right, current_max))
                
        return good_count

    def approach3_iterative_dfs(self, root: TreeNode) -> int:
        """
        Iterative DFS with Stack
        ----------------------
        Strategy:
        1. Use stack to track nodes and path maximums
        2. Process depth-first, maintaining path information
        3. Count good nodes during traversal
        
        Time: O(n) - visit each node once
        Space: O(h) - stack space, h is height
        """
        if not root:
            return 0
            
        good_count = 0
        stack = [(root, float('-inf'))]
        
        while stack:
            node, path_max = stack.pop()
            
            if node.val >= path_max:
                good_count += 1
            
            current_max = max(path_max, node.val)
            
            # Add children to stack (right first for left-to-right processing)
            if node.right:
                stack.append((node.right, current_max))
            if node.left:
                stack.append((node.left, current_max))
                
        return good_count

    def create_test_cases(self):
        """Create example trees for testing."""
        # Test case 1: [3,1,4,3,null,1,5]
        tree1 = TreeNode(3)
        tree1.left = TreeNode(1)
        tree1.right = TreeNode(4)
        tree1.left.left = TreeNode(3)
        tree1.right.left = TreeNode(1)
        tree1.right.right = TreeNode(5)

        # Test case 2: [3,3,null,4,2]
        tree2 = TreeNode(3)
        tree2.left = TreeNode(3)
        tree2.left.left = TreeNode(4)
        tree2.left.right = TreeNode(2)

        return [
            (tree1, "Example 1: Multiple good nodes"),
            (tree2, "Example 2: Node with higher ancestor"),
            (TreeNode(1), "Example 3: Single node")
        ]

    def demonstrate_solutions(self):
        """Test and compare all approaches."""
        test_cases = self.create_test_cases()
        approaches = [
            (self.approach1_recursive_dfs, "Recursive DFS"),
            (self.approach2_iterative_bfs, "Iterative BFS"),
            (self.approach3_iterative_dfs, "Iterative DFS")
        ]

        print("Good Nodes Count Results:")
        print("========================")
        
        for tree, case_name in test_cases:
            print(f"\n{case_name}:")
            for approach, name in approaches:
                result = approach(tree)
                print(f"{name}: {result} good nodes")

def main():
    """
    Main function to demonstrate solutions and provide insights.
    """
    solver = GoodNodesCounter()
    solver.demonstrate_solutions()

    print("\nKey Patterns and Insights:")
    print("=========================")
    print("1. Path Maximum Pattern:")
    print("   - Track maximum value along current path")
    print("   - Compare current node with path maximum")
    print("   - Update maximum for children")
    
    print("\n2. Implementation Patterns:")
    print("   - DFS with state (path maximum)")
    print("   - Level-order with paired information")
    print("   - Stack/Queue-based state tracking")
    
    print("\n3. Edge Cases:")
    print("   - Single node (always good)")
    print("   - Decreasing path values")
    print("   - Equal values in path")
    print("   - Deep unbalanced trees")

if __name__ == "__main__":
    main()

"""
Additional Notes:
---------------
1. DSA Patterns Used:
   - Tree traversal with state
   - Path information tracking
   - Dynamic maximum maintenance
   - Stack/Queue based iteration

2. Interview Tips:
   - Start with recursive solution (most intuitive)
   - Discuss trade-offs between approaches
   - Consider space efficiency for different tree shapes
   - Handle edge cases explicitly

3. Common Pitfalls:
   - Incorrect path maximum tracking
   - Not handling equal values correctly
   - Forgetting to update maximum for children
   - Stack overflow in deep trees
   - Missing null checks
"""