# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# 235. Lowest Common Ancestor of a Binary Search Tree
# Medium
# Topics
# Companies
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

"""
COMPREHENSIVE SOLUTION ANALYSIS: LCA IN BST
=========================================

1. PROBLEM UNDERSTANDING
-----------------------
Goal: Find lowest common ancestor (LCA) of two nodes in BST

Key Concepts:
1. Lowest Common Ancestor (LCA):
   - Lowest/deepest node that is ancestor to both p and q
   - Node can be ancestor of itself
   - In BST, first node between p and q values is LCA

BST Properties Used:
1. Left subtree values < Node value
2. Right subtree values > Node value
3. All values unique
4. Both nodes guaranteed to exist

Visual Examples:
Example 1:
         6
        / \
       2   8
      / \ / \
     0  4 7  9
        / \
       3   5

For p=2, q=8:
- LCA is 6 (split point)
- 2 < 6 < 8 (key insight!)

Example 2:
For p=2, q=4:
- LCA is 2 (ancestor of itself)
- 2 <= 4 (in right subtree)

2. PATTERN RECOGNITION
--------------------
Core Patterns:
1. Binary Search Pattern
   - Use BST property for efficient traversal
   - No need to explore all paths

2. Divide & Conquer
   - Problem space reduces at each step
   - Decision based on node values

3. Ancestor Pattern
   - Track path to nodes
   - Find first common node

3. SOLUTION PROGRESSION
---------------------

SOLUTION 1: RECURSIVE PATH FINDING (GENERIC TREE SOLUTION)
------------------------------------------------------
Pattern: Store paths to nodes and find first common
Time: O(n)
Space: O(h)
"""
def lowestCommonAncestor1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def find_path(node: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
        if not node:
            return False
            
        path.append(node)
        if node == target:
            return True
            
        if (find_path(node.left, target, path) or 
            find_path(node.right, target, path)):
            return True
            
        path.pop()
        return False
    
    path_p = []
    path_q = []
    find_path(root, p, path_p)
    find_path(root, q, path_q)
    
    # Find last common node
    i = 0
    while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
        i += 1
    return path_p[i-1]

"""
SOLUTION 2: BST PROPERTY RECURSIVE (OPTIMAL)
----------------------------------------
Pattern: Use BST property for direction
Time: O(h) where h is height
Space: O(h) for recursion

Visual Process:
     6
    / \
   2   8    Current=6
  / \       p=2, q=8
 0   4      2<6<8 → LCA found!
"""
def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # If both values less than current, go left
    if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor2(root.left, p, q)
    
    # If both values greater than current, go right
    if p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor2(root.right, p, q)
    
    # Found split point or one of the nodes
    return root

"""
SOLUTION 3: ITERATIVE BST PROPERTY (MEMORY EFFICIENT)
------------------------------------------------
Pattern: Iterative binary search
Time: O(h)
Space: O(1)

Visual Process:
     6      curr=6
    / \     p=2, q=8
   2   8    2<6<8 → Found!
  / \
 0   4
"""
def lowestCommonAncestor3(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    
    while curr:
        # If both values less than current, go left
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        # If both values greater than current, go right
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        # Found split point or one of the nodes
        else:
            return curr
    
    return None

"""
4. KEY DSA CONCEPTS USED
-----------------------
1. Tree Traversal:
   - Path finding
   - Ancestor tracking
   - Level by level movement

2. Binary Search:
   - Efficient path finding in BST
   - O(h) vs O(n) improvement
   - Direction based on value comparison

3. Divide & Conquer:
   - Problem space reduction
   - Decision making at each node
   - Subproblem delegation

4. Space-Time Trade-offs:
   - Path storage vs direct traverse
   - Recursion vs iteration
   - Memory usage considerations

5. PATTERN MATCHING GUIDE
------------------------
When to use similar approach:
1. Problems involving common ancestors
2. Path finding in BST
3. Node relationship questions
4. Tree property utilization

Common Pattern Variations:
1. Lowest Common Ancestor
2. Path to Node
3. Node Distance
4. Range Queries

6. TESTING STRATEGY
-----------------
"""
def test_lca():
    # Test case 1: Split point LCA
    #      6
    #     / \
    #    2   8
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    assert lowestCommonAncestor2(root1, root1.left, root1.right).val == 6

    # Test case 2: Node is its own ancestor
    assert lowestCommonAncestor2(root1, root1.left, root1.left).val == 2

"""
7. OPTIMIZATION INSIGHTS
----------------------
1. BST Property Usage:
   - Reduces time from O(n) to O(h)
   - Eliminates need for path storage
   - Enables efficient navigation

2. Memory Optimization:
   - Iterative vs recursive
   - Path storage elimination
   - Constant space solution

8. PRACTICAL APPLICATIONS
-----------------------
1. File system ancestor finding
2. Organization hierarchy
3. Network routing
4. Taxonomic classification

9. FOLLOW-UP QUESTIONS
--------------------
1. What if nodes might not exist?
2. How to handle duplicates?
3. Distance between nodes?
4. Multiple node LCA?
"""