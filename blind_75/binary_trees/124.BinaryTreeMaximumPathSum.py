# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# 124. Binary Tree Maximum Path Sum
# Hard
# Topics
# Companies
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Recursive DFS with Global Variable
def maxPathSum_global(root: TreeNode) -> int:
    """
    Time: O(n), Space: O(h) for recursion stack
    Strategy: Use global variable to track maximum
    
    Visual example:
         -10
        /   \
       9     20
            /  \
           15   7
           
    Process at node 20:
    left_gain = max(15, 0) = 15
    right_gain = max(7, 0) = 7
    current_path = 15 + 20 + 7 = 42
    return up: 20 + max(15,7) = 35
    """
    max_sum = float('-inf')
    
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
            
        # Get max path sums from children (use 0 if negative)
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Current path value including both children
        current_path = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path)
        
        # Return value for parent's path
        return node.val + max(left_gain, right_gain)
        
    max_gain(root)
    return max_sum

# Solution 2: Recursive DFS returning tuple
def maxPathSum_tuple(root: TreeNode) -> int:
    """
    Time: O(n), Space: O(h)
    Strategy: Return (max_path_through_node, max_path_ending_at_node)
    
    Visual example:
          1
         / \
        2   3
        
    Returns tuple at each node:
    At 2: (2, 2)     # (path through, path ending)
    At 3: (3, 3)
    At 1: (6, 4)     # through=2+1+3=6, ending=1+max(2,3)=4
    """
    def max_gain(node):
        if not node:
            return float('-inf'), 0
            
        left_through, left_end = max_gain(node.left)
        right_through, right_end = max_gain(node.right)
        
        # Max path ending at current node
        end_at_node = node.val + max(0, max(left_end, right_end))
        
        # Max path going through current node
        through_node = node.val + max(0, left_end) + max(0, right_end)
        
        # Max path possible in this subtree
        max_path = max(through_node, left_through, right_through)
        
        return max_path, end_at_node
        
    return max_gain(root)[0]

# Solution 3: Iterative Post-order with Stack
def maxPathSum_iterative(root: TreeNode) -> int:
    """
    Time: O(n), Space: O(h)
    Strategy: Post-order traversal with value caching
    
    Visual process for [-10,9,20,15,7]:
    Stack visualization:
    1. [-10, 9, 20, 15, 7]    # Push all
    2. [-10, 9, 20, 15]       # Process 7
    3. [-10, 9, 20]           # Process 15
    4. [-10, 9]               # Process 20
    5. [-10]                  # Process 9
    6. []                     # Process -10
    """
    if not root:
        return 0
        
    max_sum = float('-inf')
    stack = [(root, False)]
    gains = {}  # Cache for node gains
    
    while stack:
        node, visited = stack[-1]
        
        # Post-order traversal logic
        if not node:
            stack.pop()
            continue
            
        if visited:
            stack.pop()
            
            # Calculate gains similar to recursive approach
            left_gain = max(gains.get(node.left, 0), 0)
            right_gain = max(gains.get(node.right, 0), 0)
            
            # Update max_sum and cache current node's gain
            current_path = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path)
            gains[node] = node.val + max(left_gain, right_gain)
        else:
            stack[-1] = (node, True)
            stack.append((node.right, False))
            stack.append((node.left, False))
            
    return max_sum

# Solution 4: Level-order BFS approach (less efficient but interesting)
def maxPathSum_bfs(root: TreeNode) -> int:
    """
    Time: O(n²), Space: O(w) where w is max width
    Strategy: Process each node as potential highest point
    
    Visual process:
    Level by level:
    1. Process root as highest point
    2. Process level 2 nodes as highest points
    3. Process level 3 nodes as highest points
    
    Less efficient but demonstrates different thinking
    """
    if not root:
        return 0
        
    max_sum = float('-inf')
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Try paths through current node
        def get_max_single_path(node, exclude=None):
            if not node or node == exclude:
                return 0
            left = max(get_max_single_path(node.left, exclude), 0)
            right = max(get_max_single_path(node.right, exclude), 0)
            return node.val + max(left, right)
        
        # Current node as highest point
        left_path = max(get_max_single_path(node.left), 0)
        right_path = max(get_max_single_path(node.right), 0)
        max_sum = max(max_sum, node.val + left_path + right_path)
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return max_sum

