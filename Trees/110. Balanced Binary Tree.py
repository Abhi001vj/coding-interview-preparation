# https://leetcode.com/problems/balanced-binary-tree/description/
# 110. Balanced Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
Key Patterns and Concepts:

Tree Traversal Patterns:

Post-order traversal (process children before parent)
Bottom-up information gathering
Height calculation pattern


State Management Patterns:

Global state tracking (iterative)
Return tuple pattern (recursive DFS)
Memoization pattern (depths dictionary)


Optimization Techniques:

Combining calculations (height + balance)
Early termination
State caching


Interview Tips:

Discuss trade-offs between approaches
Handle edge cases (empty tree, single node)
Consider space complexity for deep trees
Think about real-world applications




class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced using brute force approach.
        A height-balanced tree is one where the heights of left and right subtrees 
        of every node differ by at most 1.
        
        Time Complexity: O(n²) - We calculate height for each node
        Space Complexity: O(n) - Recursion stack in worst case
        """
        # Base case: empty tree is balanced
        if not root:
            return True
        
        # Get heights of left and right subtrees
        left = self.height(root.left)   # O(n) operation
        right = self.height(root.right) # O(n) operation
        
        # Check three conditions:
        # 1. Current node's subtrees height difference ≤ 1
        # 2. Left subtree is balanced
        # 3. Right subtree is balanced
        return (abs(left - right) <= 1 and 
                self.isBalanced(root.left) and  # Recursive check
                self.isBalanced(root.right))    # Recursive check

    def height(self, root: Optional[TreeNode]) -> int:
        """Calculate height of tree starting from given node."""
        if not root:
            return 0
        # Height = 1 + max(left subtree height, right subtree height)
        return 1 + max(self.height(root.left), 
                      self.height(root.right))

"""
Pattern Recognition:
1. Tree Recursion Pattern
2. Height Calculation Pattern
3. Multiple Recursive Traversals

Example Execution Flow:
     3
    / \
   9  20
      / \
     15  7

Step 1: Check node 3
- Calculate left height (9): 1
- Calculate right height (20->15,7): 2
- |1-2| ≤ 1 ✓
- Recursively check left and right

Step 2: Check node 9
- Left height: 0
- Right height: 0
- |0-0| ≤ 1 ✓

Step 3: Check node 20
- Left height: 1
- Right height: 1
- |1-1| ≤ 1 ✓

Final: All conditions met -> True
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if tree is balanced using optimized DFS approach.
        Returns [is_balanced, height] for each subtree to avoid 
        repeated calculations.
        
        Time Complexity: O(n) - Single traversal
        Space Complexity: O(n) - Recursion stack
        """
        def dfs(root):
            """
            Helper function performing DFS traversal.
            Returns: [is_balanced, height]
            """
            # Base case: empty tree is balanced with height 0
            if not root:
                return [True, 0]
            
            # Post-order traversal: process left and right first
            left = dfs(root.left)   # Get [balanced, height] for left
            right = dfs(root.right) # Get [balanced, height] for right
            
            # Check if current subtree is balanced:
            # 1. Left subtree is balanced (left[0])
            # 2. Right subtree is balanced (right[0])
            # 3. Height difference ≤ 1
            balanced = (left[0] and right[0] and 
                       abs(left[1] - right[1]) <= 1)
            
            # Return current state: [is_balanced, height]
            return [balanced, 1 + max(left[1], right[1])]
        
        # Return only the balanced status
        return dfs(root)[0]

"""
Pattern Recognition:
1. Bottom-up DFS Pattern
2. State Combination Pattern
3. Early Termination Pattern

Example Execution Flow:
     3
    / \
   9  20
      / \
     15  7

DFS Traversal:
1. Node 9: [True, 1]
2. Node 15: [True, 1]
3. Node 7: [True, 1]
4. Node 20: [True, 2]
5. Node 3: [True, 3]

Key Optimization:
- Combines balance check and height calculation
- Avoids repeated traversals
- Uses tuple to carry multiple pieces of information
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if tree is balanced using iterative post-order traversal.
        Uses explicit stack and dictionary for tracking heights.
        
        Time Complexity: O(n) - Visit each node once
        Space Complexity: O(n) - Stack and dictionary storage
        """
        if not root:
            return True
            
        stack = []          # For iterative traversal
        node = root         # Current node
        last = None        # Last processed node
        depths = {}        # Store heights: node -> height
        
        while stack or node:
            # Phase 1: Go left as far as possible
            if node:
                stack.append(node)
                node = node.left
            else:
                # Phase 2: Process node if right subtree done
                node = stack[-1]
                if not node.right or last == node.right:
                    # Post-order processing
                    stack.pop()
                    # Get heights of children (0 if None)
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)
                    
                    # Check balance condition
                    if abs(left - right) > 1:
                        return False
                        
                    # Store current node's height
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    # Phase 3: Process right subtree
                    node = node.right
        
        return True

"""
Pattern Recognition:
1. Iterative Post-order Traversal Pattern
2. Stack-based Tree Processing
3. Height Memoization Pattern

Stack Evolution Example:
     3
    / \
   9  20
      / \
     15  7

Step 1: stack=[3], node=9
Step 2: stack=[3,9], node=None
Step 3: stack=[3], depths={9:1}
Step 4: stack=[3,20], node=15
...

Key Advantages:
1. No recursion overhead
2. Explicit control over traversal
3. Memory efficient for deep trees
"""

"""
Balanced Binary Tree - Comprehensive Analysis and Solutions
========================================================

Problem Definition:
-----------------
Given a binary tree, determine if it is height-balanced.
A binary tree is height-balanced if for each node:
1. The heights of its left and right subtrees differ by at most 1
2. Both left and right subtrees are also balanced

Visual Examples:
--------------
Balanced Tree:
       3
      / \
     9  20
        /  \
       15   7
Height difference at each node ≤ 1

Unbalanced Tree:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Left subtree height differs by more than 1
"""

from typing import Optional, List, Dict, Tuple

# Definition of tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BalancedTreeSolutions:
    """
    Collection of different approaches to solve the balanced binary tree problem.
    Each solution demonstrates different algorithmic patterns and trade-offs.
    """

    def __init__(self):
        """Initialize solution class with example trees for testing."""
        # Create example balanced tree
        self.balanced_tree = TreeNode(3)
        self.balanced_tree.left = TreeNode(9)
        self.balanced_tree.right = TreeNode(20)
        self.balanced_tree.right.left = TreeNode(15)
        self.balanced_tree.right.right = TreeNode(7)

        # Create example unbalanced tree
        self.unbalanced_tree = TreeNode(1)
        self.unbalanced_tree.left = TreeNode(2)
        self.unbalanced_tree.right = TreeNode(2)
        self.unbalanced_tree.left.left = TreeNode(3)
        self.unbalanced_tree.left.right = TreeNode(3)
        self.unbalanced_tree.left.left.left = TreeNode(4)
        self.unbalanced_tree.left.left.right = TreeNode(4)

    def approach1_brute_force(self, root: Optional[TreeNode]) -> bool:
        """
        Brute Force Approach
        -------------------
        Strategy:
        1. For each node, calculate height of left and right subtrees
        2. Check if difference ≤ 1
        3. Recursively check both subtrees

        Time Complexity: O(n²) - height calculation for each node
        Space Complexity: O(n) - recursion stack
        """
        if not root:
            return True
        
        # Calculate heights - O(n) operation for each node
        left_height = self._calculate_height(root.left)
        right_height = self._calculate_height(root.right)
        
        # Check balance conditions
        is_current_balanced = abs(left_height - right_height) <= 1
        is_left_balanced = self.approach1_brute_force(root.left)
        is_right_balanced = self.approach1_brute_force(root.right)
        
        return is_current_balanced and is_left_balanced and is_right_balanced

    def _calculate_height(self, root: Optional[TreeNode]) -> int:
        """Helper function to calculate height of a tree."""
        if not root:
            return 0
        return 1 + max(self._calculate_height(root.left),
                      self._calculate_height(root.right))

    def approach2_optimized_dfs(self, root: Optional[TreeNode]) -> bool:
        """
        Optimized DFS Approach
        ---------------------
        Strategy:
        1. Combine height calculation with balance checking
        2. Use bottom-up approach to avoid repeated calculations
        3. Return tuple of [is_balanced, height]

        Time Complexity: O(n) - single traversal
        Space Complexity: O(n) - recursion stack
        """
        def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return True, 0
            
            # Process left and right subtrees
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)
            
            # Check all balance conditions
            is_balanced = (left_balanced and 
                         right_balanced and 
                         abs(left_height - right_height) <= 1)
            
            # Return current state
            current_height = 1 + max(left_height, right_height)
            return is_balanced, current_height
        
        return dfs(root)[0]

    def approach3_iterative_dfs(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative DFS Approach
        ---------------------
        Strategy:
        1. Use explicit stack for traversal
        2. Process nodes in post-order
        3. Store heights in dictionary
        4. Check balance while processing

        Time Complexity: O(n) - single traversal
        Space Complexity: O(n) - stack and dictionary
        """
        if not root:
            return True

        stack = []
        node = root
        last_visited = None
        heights = {None: 0}  # Store heights, None nodes have height 0

        while stack or node:
            # Phase 1: Go left as deep as possible
            if node:
                stack.append(node)
                node = node.left
            else:
                # Peek at top node
                peek = stack[-1]
                
                # If right child exists and not processed
                if peek.right and peek.right != last_visited:
                    node = peek.right
                else:
                    # Process current node
                    node = stack.pop()
                    
                    # Get heights of children
                    left_height = heights.get(node.left, 0)
                    right_height = heights.get(node.right, 0)
                    
                    # Check balance condition
                    if abs(left_height - right_height) > 1:
                        return False
                    
                    # Store current node's height
                    heights[node] = 1 + max(left_height, right_height)
                    
                    # Update last visited
                    last_visited = node
                    node = None

        return True

    def demonstrate_solutions(self):
        """
        Demonstrate all solutions with example trees and analysis.
        """
        solutions = [
            (self.approach1_brute_force, "Brute Force"),
            (self.approach2_optimized_dfs, "Optimized DFS"),
            (self.approach3_iterative_dfs, "Iterative DFS")
        ]

        test_cases = [
            (self.balanced_tree, "Balanced Tree"),
            (self.unbalanced_tree, "Unbalanced Tree"),
            (None, "Empty Tree")
        ]

        print("Testing all solutions:")
        print("=====================")

        for solution_func, solution_name in solutions:
            print(f"\n{solution_name} Approach:")
            print("-" * (len(solution_name) + 9))
            
            for tree, case_name in test_cases:
                result = solution_func(tree)
                print(f"{case_name}: {'✓' if result else '✗'}")

def main():
    """
    Main function to demonstrate the balanced tree solutions.
    """
    solver = BalancedTreeSolutions()
    solver.demonstrate_solutions()

    print("\nKey Insights and Patterns:")
    print("=========================")
    print("1. Tree Traversal Patterns:")
    print("   - Post-order traversal is crucial")
    print("   - Bottom-up information gathering")
    print("   - Height calculation pattern")
    
    print("\n2. Optimization Patterns:")
    print("   - Combine calculations (height + balance)")
    print("   - Memoization of heights")
    print("   - Early termination")
    
    print("\n3. Space-Time Trade-offs:")
    print("   - Brute Force: Clear but inefficient")
    print("   - DFS: Optimal time, uses recursion")
    print("   - Iterative: No recursion, extra space for tracking")

if __name__ == "__main__":
    main()

"""
Additional Notes:
---------------
1. DSA Patterns:
   - Tree traversal (DFS)
   - Post-order processing
   - State tracking
   - Memoization

2. Interview Tips:
   - Start with brute force
   - Optimize step by step
   - Consider edge cases
   - Discuss trade-offs

3. Common Pitfalls:
   - Forgetting to check subtree balance
   - Incorrect height calculation
   - Missing edge cases
   - Stack overflow in recursion
"""