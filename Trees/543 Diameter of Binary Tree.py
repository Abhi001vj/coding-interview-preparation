# https://leetcode.com/problems/diameter-of-binary-tree/description/
# 543. Diameter of Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the diameter of binary tree using brute force approach.
        For each node:
        1. Calculate left subtree height
        2. Calculate right subtree height
        3. Compare with max diameter through children
        """
        # Base case: empty tree has diameter 0
        if not root:
            return 0
        
        # Calculate heights of left and right subtrees
        # Each calculation is O(n) operation
        leftHeight = self.maxHeight(root.left)    # First traversal
        rightHeight = self.maxHeight(root.right)  # Second traversal
        
        # Current potential diameter through this node
        diameter = leftHeight + rightHeight 
        
        # Recursively find max diameter in subtrees
        # This creates multiple redundant calculations
        sub = max(self.diameterOfBinaryTree(root.left),   # Third traversal
                 self.diameterOfBinaryTree(root.right))   # Fourth traversal
        
        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        """Calculate maximum height of the tree."""
        if not root:
            return 0
        # Height = 1 + max(left height, right height)
        return 1 + max(self.maxHeight(root.left), 
                      self.maxHeight(root.right))

"""
Execution Flow for Example Tree:
            1
           / \
          2   3
         / \
        4   5

Step 1: Calculate diameter through root(1)
- Get left height (2->4,5) = 2
- Get right height (3) = 1
- Local diameter = 3

Step 2: Calculate diameter through left child(2)
- Get left height (4) = 1
- Get right height (5) = 1
- Local diameter = 2

Step 3: Calculate diameter through right child(3)
- Get left height = 0
- Get right height = 0
- Local diameter = 0

Final diameter = max(3, 2, 0) = 3
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate diameter using optimized DFS approach.
        Key optimization: Combine height calculation with diameter update
        Uses closure to maintain global state.
        """
        # Global variable to track maximum diameter
        res = 0
        
        def dfs(root):
            """
            Inner function performing DFS traversal.
            Returns: Height of current subtree
            Updates: Global maximum diameter (res)
            """
            nonlocal res  # Access outer function's variable
            
            if not root:
                return 0
                
            # Post-order traversal pattern
            left = dfs(root.left)    # Get left subtree height
            right = dfs(root.right)  # Get right subtree height
            
            # Update maximum diameter if current path is longer
            # Current diameter = left height + right height
            res = max(res, left + right)
            
            # Return height of current subtree
            return 1 + max(left, right)
        
        # Start DFS traversal
        dfs(root)
        return res

"""
Execution Flow Visualization:
            1
           / \
          2   3
         / \
        4   5

DFS Traversal Order:
1. Visit 4: height=1, res=0
2. Visit 5: height=1, res=2 (path: 4->2->5)
3. Visit 2: height=2, res=2
4. Visit 3: height=1, res=3 (path: 4->2->1->3)
5. Visit 1: height=3, final res=3
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate diameter using iterative post-order traversal.
        Uses stack for traversal and hashmap for storing results.
        Each node stores (height, diameter) tuple in hashmap.
        """
        if not root:
            return 0
            
        # Stack for iterative traversal
        stack = [root]
        
        # HashMap: node -> (height, diameter)
        # None nodes have height=0, diameter=0
        mp = {None: (0, 0)}
        
        while stack:
            node = stack[-1]  # Current node (peek)
            
            # Post-order traversal: process children first
            if node.left and node.left not in mp:
                stack.append(node.left)
                continue
                
            if node.right and node.right not in mp:
                stack.append(node.right)
                continue
            
            # Process current node (both children are processed)
            node = stack.pop()
            
            # Get children's information
            leftHeight, leftDiameter = mp[node.left]
            rightHeight, rightDiameter = mp[node.right]
            
            # Calculate and store current node's information
            # height = 1 + max child height
            # diameter = max(path through node, max child diameter)
            mp[node] = (1 + max(leftHeight, rightHeight),
                       max(leftHeight + rightHeight,
                           leftDiameter, rightDiameter))
        
        # Return diameter stored for root
        return mp[root][1]

"""
Stack and HashMap State Evolution:
            1
           / \
          2   3
         / \
        4   5

Initial: 
- Stack: [1]
- Map: {None: (0,0)}

Processing 4:
- Stack: [1,2,4]
- Map: {None: (0,0), 4: (1,0)}

Processing 5:
- Stack: [1,2]
- Map: {None: (0,0), 4: (1,0), 5: (1,0)}

Processing 2:
- Stack: [1]
- Map: {..., 2: (2,2)}

Final:
- Map: {..., 1: (3,3)}
"""