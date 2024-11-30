# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# 297. Serialize and Deserialize Binary Tree
# Hard
# Topics
# Companies
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
from collections import deque

class Codec:
    """
    Approach: Level-order (BFS) serialization with null pointer representation
    Time Complexity: O(n) for both serialize and deserialize where n is number of nodes
    Space Complexity: O(w) where w is the maximum width of the tree
    
    Visual representation of serialization:
         1
       /   \
      2     3     =>  "1,2,3,null,null,4,5"
           / \
          4   5
    
    The BFS approach:
    1. Maintains the structural information without need for special delimiters
    2. Makes it easy to reconstruct the tree level by level
    3. Efficient for both complete and skewed trees
    """
    
    def serialize(self, root):
        """
        Encodes a tree to a single string using level-order traversal.
        
        Algorithm visualization:
        1. Use a queue to process nodes level by level
        2. For each node:
           - Add its value to result
           - Add both children to queue (even if null)
        3. Trim trailing nulls for efficiency
        """
        if not root:
            return "[]"
            
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                # Add both children to maintain structure
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
                
        # Optimize space by removing trailing nulls
        while result[-1] == "null":
            result.pop()
            
        return "[" + ",".join(result) + "]"

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        Algorithm visualization:
        1. Split string into values
        2. Create root from first value
        3. Use queue to track parent nodes
        4. For each parent:
           - Get next two values for left/right children
           - Create nodes and link to parent
           - Add new nodes to queue
        """
        if data == "[]":
            return None
            
        # Remove brackets and split into values
        values = data[1:-1].split(",")
        if not values[0]:
            return None
            
        # Create root and add to queue
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1  # Index to track current value
        
        while queue and i < len(values):
            node = queue.popleft()
            
            # Process left child
            if i < len(values) and values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            # Process right child
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
            
        return root