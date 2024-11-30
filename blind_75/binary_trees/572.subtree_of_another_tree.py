# https://leetcode.com/problems/subtree-of-another-tree/description/
# 572. Subtree of Another Tree
# Easy
# Topics
# Companies
# Hint
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Solution 1: Recursive Tree Traversal with isEqual Check
    Time: O(m*n) where m is number of nodes in root, n in subRoot
    Space: O(h) where h is height of tree (recursion stack)
    """
    def isSubtree1(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        if self.isEqual(root, subRoot):
            return True
        return self.isSubtree1(root.left, subRoot) or self.isSubtree1(root.right, subRoot)
    
    def isEqual(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (root1.val == root2.val and 
                self.isEqual(root1.left, root2.left) and 
                self.isEqual(root1.right, root2.right))

    """
    Solution 2: Tree Serialization with String Matching
    Time: O(m + n) for serialization
    Space: O(m + n) for storing serialized strings
    """
    def isSubtree2(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def serialize(node):
            if not node:
                return "#"
            return f",{node.val}{serialize(node.left)}{serialize(node.right)}"
        
        str_root = serialize(root)
        str_subroot = serialize(subRoot)
        return str_subroot in str_root

    """
    Solution 3: DFS with Preorder Traversal and Merkle Hashing
    Time: O(m + n)
    Space: O(h) where h is height of tree
    """
    def isSubtree3(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def hash_node(node):
            if not node:
                return '#'
            node_hash = f"{node.val},{hash_node(node.left)},{hash_node(node.right)}"
            return str(hash(node_hash))
        
        def dfs(node):
            if not node:
                return False
            if hash_node(node) == sub_hash:
                return self.isEqual(node, subRoot)
            return dfs(node.left) or dfs(node.right)
        
        sub_hash = hash_node(subRoot)
        return dfs(root)