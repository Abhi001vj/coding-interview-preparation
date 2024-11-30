# https://leetcode.com/problems/invert-binary-tree/description/
# 226. Invert Binary Tree
# Easy
# Topics
# Companies
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Definition for binary tree node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Recursive DFS (Most intuitive)
def invertTree_recursive(root: TreeNode) -> TreeNode:
    """
    Time: O(n), Space: O(h) for recursion stack
    
    Visualization for [4,2,7,1,3,6,9]:
    Original:                 Inverted:
         4                        4
       /   \                    /   \
      2     7       →         7     2
     / \   / \              / \   / \
    1   3 6   9            9   6 3   1
    
    Process:
    1. Swap 2 and 7
    2. Recursively invert subtrees
    """
    if not root:
        return None
        
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invertTree_recursive(root.left)
    invertTree_recursive(root.right)
    
    return root

# Solution 2: Iterative BFS
from collections import deque
def invertTree_bfs(root: TreeNode) -> TreeNode:
    """
    Time: O(n), Space: O(w) where w is max width
    
    Visualization of BFS process:
    Level 1: Queue=[4]
            Swap 2↔7
    Level 2: Queue=[7,2]
            Swap 6↔9, 1↔3
    Level 3: Queue=[9,6,3,1]
    """
    if not root:
        return None
        
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        # Swap children
        node.left, node.right = node.right, node.left
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return root

# Solution 3: Iterative DFS with Stack
def invertTree_dfs_iterative(root: TreeNode) -> TreeNode:
    """
    Time: O(n), Space: O(h)
    
    Visualization of stack process:
    Initial: Stack=[4]
    Step 1:  Stack=[2,7]    Swap 2↔7
    Step 2:  Stack=[2,6,9]  Swap 6↔9
    Step 3:  Stack=[2,1,3]  Swap 1↔3
    """
    if not root:
        return None
        
    stack = [root]
    
    while stack:
        node = stack.pop()
        # Swap children
        node.left, node.right = node.right, node.left
        
        # Add children to stack
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return root

# Solution 4: Bottom-up Recursive
def invertTree_bottom_up(root: TreeNode) -> TreeNode:
    """
    Time: O(n), Space: O(h)
    
    Visualization of bottom-up process:
    For [4,2,7,1,3,6,9]:
    
    1. Invert leaf level:
       1,3 and 6,9 get ready to swap
       
    2. Invert middle level:
       2's children (1,3) are swapped
       7's children (6,9) are swapped
       
    3. Invert root level:
       4's children (2,7) are swapped
    """
    if not root:
        return None
        
    # First recursively get inverted subtrees
    left_inverted = invertTree_bottom_up(root.left)
    right_inverted = invertTree_bottom_up(root.right)
    
    # Then swap them
    root.left = right_inverted
    root.right = left_inverted
    
    return root

def visualize_inversion(root: TreeNode, method):
    """
    Helper to visualize tree inversion process
    """
    def print_tree(node: TreeNode, level: int = 0, prefix: str = "Root"):
        if not node:
            print("  " * level + f"{prefix}: None")
            return
        print("  " * level + f"{prefix}: {node.val}")
        if node.left or node.right:
            print_tree(node.left, level + 1, "L")
            print_tree(node.right, level + 1, "R")
    
    print(f"\nInverting using {method}:")
    print("=" * 50)
    print("\nBefore inversion:")
    print_tree(root)
    
    # Create a copy for visualization
    def copy_tree(node):
        if not node:
            return None
        new_node = TreeNode(node.val)
        new_node.left = copy_tree(node.left)
        new_node.right = copy_tree(node.right)
        return new_node
    
    original = copy_tree(root)
    
    # Apply inversion
    if method == "Recursive":
        result = invertTree_recursive(root)
    elif method == "BFS":
        result = invertTree_bfs(root)
    elif method == "DFS Iterative":
        result = invertTree_dfs_iterative(root)
    else:
        result = invertTree_bottom_up(root)
    
    print("\nAfter inversion:")
    print_tree(result)
    
    return result

# Test cases
def test_invert_tree():
    # Test case 1: [4,2,7,1,3,6,9]
    tree1 = TreeNode(4)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(7)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(3)
    tree1.right.left = TreeNode(6)
    tree1.right.right = TreeNode(9)
    
    # Test case 2: [2,1,3]
    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    
    test_cases = [
        (tree1, "Complete binary tree"),
        (tree2, "Simple tree"),
        (None, "Empty tree"),
        (TreeNode(1), "Single node")
    ]
    
    for tree, description in test_cases:
        print(f"\nTesting {description}")
        for method in ["Recursive", "BFS", "DFS Iterative", "Bottom-up"]:
            visualize_inversion(copy_tree(tree), method)

# Run tests
test_invert_tree()