# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# 230. Kth Smallest Element in a BST
# Medium
# Topics
# Companies
# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

"""
COMPREHENSIVE SOLUTION ANALYSIS: KTH SMALLEST IN BST
=================================================

1. PROBLEM UNDERSTANDING
-----------------------
Goal: Find kth smallest value in BST (1-indexed)

Key Insights:
1. BST property: Left < Node < Right
2. Inorder traversal gives sorted sequence
3. Need to track position during traversal
4. Must handle 1-based indexing

Visual Examples:
Example 1:
     3
    / \      Inorder: [1,2,3,4]
   1   4     k=1 → return 1
    \
     2

Example 2:
     5
    / \
   3   6     Inorder: [1,2,3,4,5,6]
  / \        k=3 → return 3
 2   4
/
1

Constraints Analysis:
- Nodes: 1 to 10^4
- k: 1 to n (valid k guaranteed)
- Node values: 0 to 10^4
- Must handle frequent modifications (follow-up)

Edge Cases:
1. k = 1 (leftmost node)
2. k = n (rightmost node)
3. Single node tree
4. Skewed tree (left/right)

2. SOLUTION PROGRESSION
----------------------

SOLUTION 1: RECURSIVE INORDER WITH ARRAY
--------------------------------------
Pattern: Full inorder traversal + array storage
Time: O(n)
Space: O(n)

Visual Process:
     3
    / \
   1   4    Steps:
    \        1. Store inorder: [1,2,3,4]
     2       2. Return arr[k-1]
"""
def kthSmallest1(self, root: TreeNode, k: int) -> int:
    def inorder(node: TreeNode) -> None:
        if not node:
            return
        # Build sorted array
        inorder(node.left)
        self.sorted.append(node.val)
        inorder(node.right)
    
    self.sorted = []
    inorder(root)
    return self.sorted[k-1]  # Convert 1-based to 0-based

"""
SOLUTION 2: RECURSIVE WITH COUNTER (OPTIMIZED)
-------------------------------------------
Pattern: Early stopping inorder traversal
Time: O(H + k) where H is height
Space: O(H) for recursion stack

Visual Process:
     3
    / \     count = 0
   1   4    When count = k, stop
    \       Only traverse needed nodes
     2

Step-by-step for k=2:
1. Start at 3, go left
2. At 1, count=1
3. At 2, count=2 (found!)
"""
def kthSmallest2(self, root: TreeNode, k: int) -> int:
    def inorder(node: TreeNode) -> None:
        if not node or self.count > k:
            return
        
        # Process left subtree
        inorder(node.left)
        
        # Process current node
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
            
        # Process right subtree
        inorder(node.right)
    
    self.count = 0
    self.result = None
    inorder(root)
    return self.result

"""
SOLUTION 3: ITERATIVE WITH STACK (MEMORY EFFICIENT)
-----------------------------------------------
Pattern: Iterative inorder with early stopping
Time: O(H + k)
Space: O(H)

Visual Process:
Stack states for k=2:
1. [3,1]
2. [3] + process 1
3. [3,2]
4. Found!
"""
def kthSmallest3(self, root: TreeNode, k: int) -> int:
    stack = []
    curr = root
    count = 0
    
    while stack or curr:
        # Push all left nodes
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        count += 1
        
        if count == k:
            return curr.val
        
        curr = curr.right
    
    return -1  # Should never reach here if k is valid

"""
SOLUTION 4: AUGMENTED BST NODE (FOLLOW-UP SOLUTION)
-----------------------------------------------
Pattern: Store size of left subtree
Time: O(H) for query, O(H) for update
Space: O(N) for additional count field

Visual Process:
     3 [3]
    / \        [x] = size of left subtree
   1   4 [0]   For k=2:
    \          1. 3 has left_count=1
     2 [0]     2. k>left_count+1, go right
"""
class AugmentedNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.left_count = 0  # Size of left subtree

def kthSmallest4(self, root: AugmentedNode, k: int) -> int:
    curr = root
    
    while curr:
        left_count = curr.left_count
        
        if k == left_count + 1:  # Current node is kth
            return curr.val
        elif k <= left_count:  # kth is in left subtree
            curr = curr.left
        else:  # kth is in right subtree
            k = k - left_count - 1  # Adjust k
            curr = curr.right
    
    return -1

"""
SOLUTION COMPARISON
-----------------
1. Array Solution (Solution 1)
   Pros: Simple, intuitive
   Cons: O(n) space, processes all nodes
   Best for: Interviews, explaining concept

2. Counter Solution (Solution 2)
   Pros: Early stopping, O(H) space
   Cons: Uses global variables
   Best for: Single queries, clean code

3. Iterative Solution (Solution 3)
   Pros: No recursion, O(H) space
   Cons: More complex code
   Best for: Memory-constrained systems

4. Augmented BST (Solution 4)
   Pros: O(H) query time, efficient for frequent queries
   Cons: Extra space per node, complex updates
   Best for: Frequent queries with updates

IMPLEMENTATION NOTES
------------------
1. Handling Updates:
   - Solution 1-3: No special handling needed
   - Solution 4: Must update left_count on insertions/deletions

2. Space-Time Trade-offs:
   - More space → Faster queries
   - Less space → Slower queries

TESTING APPROACH
--------------
"""
def test_kth_smallest():
    # Test case 1: Simple tree
    #     3
    #    / \
    #   1   4
    #    \
    #     2
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    
    assert kthSmallest2(root1, 1) == 1  # Smallest
    assert kthSmallest2(root1, 2) == 2  # Second smallest
    assert kthSmallest2(root1, 4) == 4  # Largest

    # Add more test cases for edge cases...

"""
LEARNING POINTS
-------------
1. Inorder traversal properties in BST
2. Early stopping optimization
3. Space-time trade-offs
4. Augmented data structures

FOLLOW-UP INSIGHTS
----------------
1. For frequent updates:
   - Use augmented BST
   - Consider Red-Black tree
   - Balance trade-offs based on operation frequency
"""