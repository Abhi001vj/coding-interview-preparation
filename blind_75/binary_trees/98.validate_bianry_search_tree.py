# https://leetcode.com/problems/validate-binary-search-tree/description/
# 98. Validate Binary Search Tree
# Medium
# Topics
# Companies
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

"""
COMPREHENSIVE SOLUTION ANALYSIS: VALIDATE BST
===========================================

1. PROBLEM UNDERSTANDING
-----------------------
Problem Statement:
Given a binary tree, determine if it's a valid Binary Search Tree (BST)

Key BST Properties:
1. Left subtree nodes < Current node value
2. Right subtree nodes > Current node value
3. ALL left subtree values < node value < ALL right subtree values

Visual Examples:
Valid BST:
     2
    / \    All valid because:
   1   3   1 < 2 < 3

Invalid BST:
     5
    / \    Invalid because:
   1   4   3 < 4 < 6 violates 4 < 5
      / \
     3   6

Constraints Analysis:
- Node range: 1 to 10^4 nodes
- Value range: -2^31 to 2^31-1
- Must handle null nodes
- Must validate entire subtrees, not just direct children

Edge Cases:
1. Single node tree
2. Complete binary tree
3. Skewed tree
4. Values at INT_MIN/INT_MAX
5. Duplicate values (not allowed)

2. BASE PATTERNS RECOGNITION
---------------------------
Applicable Patterns:
1. Tree Traversal (DFS/recursion)
2. Range Validation
3. State tracking through recursion
4. Divide and Conquer

3. SOLUTION PROGRESSION
----------------------

SOLUTION 1: RECURSIVE INORDER TRAVERSAL (INTUITIVE APPROACH)
---------------------------------------------------------
Pattern: Inorder traversal with previous value tracking
Time: O(n) - visit each node once
Space: O(h) - recursion stack, h = height

Visual Process:
Inorder traversal (Left → Root → Right) of valid BST must be strictly increasing
     2
    / \    Inorder: [1,2,3] ✓
   1   3   Strictly increasing

Code and Visualization:
"""
def isValidBST1(self, root: TreeNode) -> bool:
    def inorder(node):
        if not node:
            return True
        
        # Process left subtree
        if not inorder(node.left):
            return False
            
        # Process current node
        if node.val <= self.prev:  # Invalid if not strictly increasing
            return False
        self.prev = node.val
        
        # Process right subtree
        return inorder(node.right)
    
    self.prev = float('-inf')  # Initialize previous value
    return inorder(root)

"""
SOLUTION 2: RECURSIVE WITH RANGE VALIDATION (INTUITIVE & CORRECT)
-------------------------------------------------------------
Pattern: DFS with range propagation
Time: O(n) - visit each node once
Space: O(h) - recursion stack

Visual Process:
Each node gets a valid range from its parent
     5
    / \    Range for 1: (-∞, 5)
   1   7   Range for 7: (5, ∞)
      / \   Range for 4: (5, 7) ✗
     4   8  Range for 8: (7, ∞)
"""
def isValidBST2(self, root: TreeNode) -> bool:
    def validate(node: TreeNode, min_val: float, max_val: float) -> bool:
        if not node:
            return True
            
        # Check current node's value against its valid range
        if not (min_val < node.val < max_val):
            return False
            
        # Validate left subtree with updated max range
        # Validate right subtree with updated min range
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

"""
SOLUTION 3: ITERATIVE WITH STACK (SPACE OPTIMIZED)
-----------------------------------------------
Pattern: Iterative inorder traversal
Time: O(n)
Space: O(h) - explicit stack instead of recursion

Visual Process:
Stack-based traversal:
1. Push all left nodes
2. Process current
3. Go right
"""
def isValidBST3(self, root: TreeNode) -> bool:
    if not root:
        return True
        
    stack = []
    prev = float('-inf')
    curr = root
    
    while stack or curr:
        # Push all left nodes
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        
        # Validate current node
        if curr.val <= prev:
            return False
        prev = curr.val
        
        # Move to right subtree
        curr = curr.right
    
    return True

"""
SOLUTION COMPARISON AND ANALYSIS
------------------------------
1. Solution 1 (Inorder)
   Pros: Intuitive, clean code
   Cons: Uses global variable, subtle bugs with duplicates
   Best for: Interview explanations, simple cases

2. Solution 2 (Range)
   Pros: Most intuitive validation approach, handles all cases
   Cons: Passes extra parameters
   Best for: Production code, clear intent

3. Solution 3 (Iterative)
   Pros: No recursion, constant extra space
   Cons: More complex implementation
   Best for: Memory-constrained systems

OPTIMIZATION INSIGHTS
-------------------
1. Recursion → Iteration optimization
2. Global state → Parameter passing
3. Early termination optimizations
4. Range validation vs. sorted property

PRACTICAL APPLICATIONS
--------------------
1. Database index validation
2. File system directory structure
3. Decision trees validation
4. Expression tree validation

LEARNING POINTS
-------------
1. BST property is recursive
2. Range validation vs. local property checking
3. Importance of handling edge cases
4. Trade-offs between approaches

FOLLOW-UP QUESTIONS
-----------------
1. How to handle duplicate values?
2. How to modify for n-ary trees?
3. How to validate a BST during construction?
4. How to handle very large trees?
"""

```
# Let's trace the exact execution for tree:
#      2
#     / \
#    1   3

# Initial state: self.prev = float('-inf')

# DETAILED EXECUTION FLOW:
# -----------------------
# 1. Start at root (2):
#    Call inorder(2)
#    └── Goes to left child (1)

# 2. At node 1:
#    Call inorder(1)
#    ├── First: Check left child
#    │   inorder(None) → returns True
#    │
#    ├── Then: Process node 1
#    │   Check: if 1 <= prev (-inf)
#    │   1 > -inf ✓ (Condition FAILS, so we continue!)
#    │   Update: prev = 1
#    │
#    └── Finally: Check right child
#        inorder(None) → returns True

# 3. Back to node 2:
#    Check: if 2 <= prev (1)
#    2 > 1 ✓
#    Update: prev = 2

# KEY INSIGHT:
# -----------
# The condition: if node.val <= self.prev
#               returns False if condition is TRUE
#               continues if condition is FALSE

# For node 1:
# - node.val = 1
# - self.prev = -inf
# - 1 <= -inf is FALSE
# - So we DON'T return False
# - We continue processing!

# VISUALIZATION WITH VALUES:
# ------------------------
#      2
#     / \
#    1   3
   
# Step 1 (at 1):
# prev = -inf
# 1 <= -inf? NO! ✓ (Continue)
# Update prev = 1

# Step 2 (at 2):
# prev = 1
# 2 <= 1? NO! ✓ (Continue)
# Update prev = 2

# Step 3 (at 3):
# prev = 2
# 3 <= 2? NO! ✓ (Continue)
# Update prev = 3

# CODE BREAKDOWN:
# -------------
# ```python
# def inorder(node):
#     if not node:
#         return True
    
#     # Process left subtree
#     if not inorder(node.left):
#         return False
        
#     # Current node processing
#     if node.val <= self.prev:  # THIS LINE
#         return False  # Only if value NOT strictly increasing
#     self.prev = node.val  # Update for next comparison
    
#     # Process right subtree
#     return inorder(node.right)
# ```

# CONDITION TRUTH TABLE:
# --------------------
# node.val <= self.prev | Result
# ---------------------|--------
# True                 | Return False (Invalid BST)
# False                | Continue (Valid so far)

# Example cases:
# 1. First node (1):
#    - node.val = 1
#    - self.prev = -inf
#    - 1 <= -inf is FALSE
#    - Continue ✓

# 2. Second node (2):
#    - node.val = 2
#    - self.prev = 1
#    - 2 <= 1 is FALSE
#    - Continue ✓

# 3. Invalid case example:
#    - node.val = 1
#    - self.prev = 2
#    - 1 <= 2 is TRUE
#    - Return False ✗
# ```

# The key points to remember:
# 1. The condition `if node.val <= self.prev` checks if we're violating BST property
# 2. We want this condition to be FALSE to continue (valid BST)
# 3. When it's TRUE, we have a violation
# 4. Starting with -inf ensures first node always passes
# 5. The condition essentially checks: "Is current value NOT greater than previous?"

# Would you like me to elaborate on any part of this explanation or provide more examples?