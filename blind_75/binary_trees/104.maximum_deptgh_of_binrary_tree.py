# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Test Result
# 104. Maximum Depth of Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level_count = 0
        queue = [root]
        while queue:
            level_size = len(queue)
            level_count += 1

            for _ in range(level_size):
                node = queue.pop(0)
                if node:

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

            

        return level_count
    
# Definition for binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Recursive DFS (Most intuitive)
def maxDepth_recursive(root: TreeNode) -> int:
    """
    Time: O(n), Space: O(h) where h is tree height
    
    Visualization for tree [3,9,20,null,null,15,7]:
               3                  Level 1
              / \
             9   20              Level 2
                /  \
               15   7            Level 3
               
    Call stack visualization:
    maxDepth(3)
    ├── maxDepth(9) = 1
    └── maxDepth(20)
        ├── maxDepth(15) = 1
        └── maxDepth(7) = 1
    Returns max(1, 2) + 1 = 3
    """
    if not root:
        return 0
    return 1 + max(maxDepth_recursive(root.left), maxDepth_recursive(root.right))

# Solution 2: Iterative BFS with Queue (Level Order)
from collections import deque
def maxDepth_bfs(root: TreeNode) -> int:
    """
    Time: O(n), Space: O(w) where w is max width
    
    Visualization for same tree:
    Queue processing:
    Level 1: [3]          depth = 1
    Level 2: [9,20]       depth = 2
    Level 3: [15,7]       depth = 3
    Level 4: []           return 3
    
    Visual process:
    Level 1:    3         Count: 1
                ↓ 
    Level 2:   9 20       Count: 2
                ↓
    Level 3:   15 7       Count: 3
    """
    if not root:
        return 0
        
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return depth

# Solution 3: Iterative DFS with Stack
def maxDepth_dfs_iterative(root: TreeNode) -> int:
    """
    Time: O(n), Space: O(h)
    
    Visualization:
    Stack processing [(node, depth)]:
    Initial:    [(3,1)]
    Step 1:     [(20,2), (9,2)]
    Step 2:     [(20,2)]             max_depth = 2
    Step 3:     [(7,3), (15,3)]      max_depth = 3
    Step 4:     [(7,3)]              max_depth = 3
    Step 5:     []                   return 3
    """
    if not root:
        return 0
        
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))
            
    return max_depth

# Solution 4: Bottom-up DFS (Alternative recursive)
def maxDepth_bottom_up(root: TreeNode) -> int:
    """
    Time: O(n), Space: O(h)
    
    Visualization of bottom-up process:
    For tree [3,9,20,null,null,15,7]:
    
           3
          / \
         9   20
            /  \
           15   7
           
    Bottom-up calculation:
    15 → 1                7 → 1
    20 → max(1,1) + 1     9 → 1
    3  → max(1,2) + 1 = 3
    """
    def dfs(node: TreeNode) -> int:
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        return max(left, right) + 1
        
    return dfs(root)

def visualize_tree_processing(root: TreeNode):
    """
    Helper function to visualize tree processing
    """
    def print_tree(node: TreeNode, level: int = 0, prefix: str = "Root"):
        if not node:
            return
        print("  " * level + f"{prefix}[{node.val}]")
        if node.left or node.right:
            print_tree(node.left, level + 1, "L")
            print_tree(node.right, level + 1, "R")
    
    print("\nTree Structure:")
    print_tree(root)
    
    # Show BFS processing
    print("\nBFS Level-order processing:")
    if not root:
        return
        
    queue = deque([(root, 1)])
    level_nodes = []
    current_level = 1
    
    while queue:
        node, level = queue.popleft()
        
        if level > current_level:
            print(f"Level {current_level}: {level_nodes}")
            level_nodes = []
            current_level = level
            
        level_nodes.append(node.val)
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
            
    print(f"Level {current_level}: {level_nodes}")

# Test cases
def test_max_depth():
    # Test case 1: [3,9,20,null,null,15,7]
    tree1 = TreeNode(3)
    tree1.left = TreeNode(9)
    tree1.right = TreeNode(20)
    tree1.right.left = TreeNode(15)
    tree1.right.right = TreeNode(7)
    
    # Test case 2: [1,null,2]
    tree2 = TreeNode(1)
    tree2.right = TreeNode(2)
    
    test_cases = [
        (tree1, "Complete tree"),
        (tree2, "Unbalanced tree"),
        (None, "Empty tree"),
        (TreeNode(1), "Single node")
    ]
    
    for tree, description in test_cases:
        print(f"\nTesting {description}")
        print("=" * 50)
        
        if tree:
            visualize_tree_processing(tree)
            
        results = {
            "Recursive": maxDepth_recursive(tree),
            "BFS": maxDepth_bfs(tree),
            "DFS Iterative": maxDepth_dfs_iterative(tree),
            "Bottom-up": maxDepth_bottom_up(tree)
        }
        
        print("\nResults:")
        for method, depth in results.items():
            print(f"{method}: {depth}")

# Run tests
test_max_depth()