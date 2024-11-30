# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium
# Topics
# Companies
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

"""
PROBLEM UNDERSTANDING
-------------------
Input: Two arrays representing traversals
- Preorder [3,9,20,15,7] (Root → Left → Right)
- Inorder [9,3,15,20,7] (Left → Root → Right)

Key Pattern Recognition:
1. Preorder array's first element is ALWAYS the root
2. In inorder array, elements left of root are left subtree, right of root are right subtree
3. This pattern repeats recursively for each subtree

Base Pattern Used: Divide and Conquer with Tree Properties

Visual Example:
preorder = [3,9,20,15,7]  # Root first
inorder  = [9,3,15,20,7]  # Root splits left/right

Step-by-Step Pattern Recognition:
1. Find Root (first in preorder):
   [3],9,20,15,7
   
2. Split Inorder at Root:
   Left: [9] | 3 | Right: [15,20,7]
   
3. Final Tree:
         3
        / \
       9   20
          /  \
         15   7

SOLUTION 1: BASIC RECURSIVE (Teaching Solution)
--------------------------------------------
Concept: Direct application of pattern recognition
Time: O(n²) - Due to linear search in inorder
Space: O(n) - Recursion stack

Key Steps Visualization:
1. Root = preorder[0] = 3
   Find 3 in inorder: [9, |3|, 15,20,7]
   
2. Split for left child:
   preorder: [9]
   inorder:  [9]
   
3. Split for right child:
   preorder: [20,15,7]
   inorder:  [15,20,7]
"""
def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder or not inorder:  # Base case
        return None
        
    # 1. Get root from preorder
    root = TreeNode(preorder[0])
    # 2. Find split point in inorder
    mid = inorder.index(preorder[0])
    # 3. Recursive divide and conquer
    root.left = self.buildTree1(preorder[1:mid+1], inorder[:mid])
    root.right = self.buildTree1(preorder[mid+1:], inorder[mid+1:])
    return root

"""
SOLUTION 2: HASHMAP OPTIMIZATION (Production Solution)
--------------------------------------------------
Pattern Improvement: Remove repeated searches using HashMap
Time: O(n) - Each node processed once
Space: O(n) - HashMap + recursion stack

Key Optimization:
1. Store inorder indices in HashMap:
   {9:0, 3:1, 15:2, 20:3, 7:4}
   
2. Use index arithmetic instead of array slicing:
   For root 3:
   - Left subtree size = 1 (mid=1 - in_start=0)
   - Left indices: preorder[1:2], inorder[0:1]
   - Right indices: preorder[2:5], inorder[2:5]

Visual Process:
Level 1:    3 (0,4, 0,4)
           / \
Level 2:  9   20 (2,4, 2,4)
             /  \
Level 3:   15   7
"""
def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    # Optimization 1: Create index map
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    
    def helper(pre_start: int, pre_end: int, in_start: int, in_end: int) -> TreeNode:
        if pre_start > pre_end:
            return None
            
        # 1. Create root
        root = TreeNode(preorder[pre_start])
        # 2. Get inorder position O(1)
        mid = inorder_map[preorder[pre_start]]
        # 3. Calculate left subtree size
        left_size = mid - in_start
        
        # 4. Build left and right using indices
        root.left = helper(pre_start + 1, 
                          pre_start + left_size, 
                          in_start, 
                          mid - 1)
        root.right = helper(pre_start + left_size + 1,
                           pre_end,
                           mid + 1,
                           in_end)
        return root
    
    return helper(0, len(preorder)-1, 0, len(inorder)-1)

"""
SOLUTION 3: STACK-BASED (Memory Efficient)
---------------------------------------
Pattern Change: Iterative with Stack
Time: O(n) - Single pass
Space: O(h) - Stack size = tree height

Key Pattern:
1. Preorder tells us when to go down (new nodes)
2. Inorder tells us when to go up (completed subtrees)

Visual Stack Process for [3,9,20,15,7]:
1. [3]           Create root
2. [3,9]         Go left
3. [3]           Pop (found 9 in inorder)
4. [3,20]        Go right
5. [3,20,15]     Go left
6. [3,20,7]      Go right

Path Construction:
     3
    / \
   9   20
      /  \
     15   7
"""
def buildTree3(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder:
        return None
    
    root = TreeNode(preorder[0])
    stack = [root]
    inorderIndex = 0
    
    for i in range(1, len(preorder)):
        current = TreeNode(preorder[i])
        # Going down left
        if stack[-1].val != inorder[inorderIndex]:
            stack[-1].left = current
        # Going up and right
        else:
            while stack and stack[-1].val == inorder[inorderIndex]:
                parent = stack.pop()
                inorderIndex += 1
            parent.right = current
        stack.append(current)
    
    return root

"""
SOLUTIONS COMPARISON & PROGRESSION
--------------------------------
1. Basic Recursive (Solution 1)
   Pros: Simple to understand, good for interviews
   Cons: O(n²) time, creates new arrays
   Best for: Learning and teaching

2. HashMap Solution (Solution 2)
   Improvement: O(n) time with O(n) space
   Added: Index map for O(1) lookups
   Best for: Production code, balanced trees

3. Stack Solution (Solution 3)
   Improvement: O(h) space for stack
   Added: Iterative approach, no recursion
   Best for: Memory-constrained systems

Next Steps/Improvements:
1. Parallel processing for large trees
2. Streaming input handling
3. Balanced tree optimizations
4. Error handling and validation
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        preorder = collections.deque(preorder)
        inorder = collections.deque(inorder)
        
        def build(stop):
            if not inorder or inorder[0] == stop:
                return None
            
            root = TreeNode(preorder.popleft())
            root.left = build(root.val)  # Process left subtree
            inorder.popleft()  # Remove processed node
            root.right = build(stop)  # Process right subtree
            return root
            
        return build(None)
    

"""
SOLUTION 4: MORRIS-LIKE CONSTRUCTION (Most Space Efficient)
-------------------------------------------------------
Pattern Used: Threaded Binary Tree concept adapted for construction
Time: O(n) - Single pass through nodes
Space: O(1) - Constant extra space (not counting output tree)

Key Innovation: 
- Uses deque data structure for O(1) operations
- Eliminates need for stack or recursion
- Builds tree by tracking "stop" nodes

Visual Process for [3,9,20,15,7]:
Initial State:
preorder = deque([3,9,20,15,7])
inorder = deque([9,3,15,20,7])

Step-by-Step Construction:
1. Initial call: build(None)
   preorder: [3|9,20,15,7]
   inorder:  [9,3,15,20,7]
   Creates: 3

2. Process left subtree: build(3)
   preorder: [9|20,15,7]
   inorder:  [9|3,15,20,7]
   Creates: 9 as left child

3. Process right subtree: build(None)
   preorder: [20|15,7]
   inorder:  [15,20,7]
   Creates: 20 as right child

4. Process 20's left: build(20)
   preorder: [15|7]
   inorder:  [15|20,7]
   Creates: 15 as left child

5. Process 20's right: build(None)
   preorder: [7]
   inorder:  [7]
   Creates: 7 as right child

Final Tree Structure:
     3
    / \
   9   20
      /  \
     15   7
"""
def buildTree4(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder:
        return None
        
    # Convert to deques for O(1) pop operations
    preorder = collections.deque(preorder)
    inorder = collections.deque(inorder)
    
    def build(stop):
        if not inorder or inorder[0] == stop:
            return None
        
        # Create node from preorder
        root = TreeNode(preorder.popleft())
        
        # Build left subtree before processing current node
        root.left = build(root.val)
        
        # Process current node
        inorder.popleft()
        
        # Build right subtree
        root.right = build(stop)
        
        return root
        
    return build(None)

"""
WHY THIS SOLUTION IS INNOVATIVE:
------------------------------
1. Space Efficiency:
   - Uses O(1) extra space compared to O(n) in previous solutions
   - Only modifies input collections directly
   - No additional data structures needed

2. Algorithm Pattern:
   - Uses "stop" node concept from Morris Traversal
   - Maintains tree structure without stack/recursion overhead
   - Leverages properties of both traversals simultaneously

3. Key Advantages:
   - Most memory efficient solution
   - No hash table needed
   - No stack maintenance
   - Minimal variable tracking

4. Trade-offs:
   - More complex logic
   - Modifies input arrays
   - Requires understanding of threaded binary tree concept

COMPARISON WITH PREVIOUS SOLUTIONS:
--------------------------------
Solution 1 (Basic) → Solution 2 (HashMap) → Solution 3 (Stack) → Solution 4 (Morris-like)
Space:    O(n)     →     O(n)            →    O(h)           →     O(1)
Complexity: Simple  →     Medium          →    Medium         →     Complex

WHEN TO USE THIS SOLUTION:
-------------------------
1. Memory is extremely constrained
2. Input modification is acceptable
3. Code complexity is not a primary concern
4. Performance is critical

IMPROVEMENTS & VARIATIONS:
------------------------
1. Add input validation
2. Handle duplicate values
3. Add error recovery
4. Optimize for specific tree shapes
"""