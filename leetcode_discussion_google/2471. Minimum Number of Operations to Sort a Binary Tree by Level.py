# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
# 2471. Minimum Number of Operations to Sort a Binary Tree by Level
# Medium
# Topics
# Companies
# Hint
# You are given the root of a binary tree with unique values.

# In one operation, you can choose any two nodes at the same level and swap their values.

# Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

# The level of a node is the number of edges along the path between it and the root node.

 

# Example 1:


# Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
# Output: 3
# Explanation:
# - Swap 4 and 3. The 2nd level becomes [3,4].
# - Swap 7 and 5. The 3rd level becomes [5,6,8,7].
# - Swap 8 and 7. The 3rd level becomes [5,6,7,8].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# Example 2:


# Input: root = [1,3,2,7,6,5,4]
# Output: 3
# Explanation:
# - Swap 3 and 2. The 2nd level becomes [2,3].
# - Swap 7 and 4. The 3rd level becomes [4,6,5,7].
# - Swap 6 and 5. The 3rd level becomes [4,5,6,7].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# Example 3:


# Input: root = [1,2,3,4,5,6]
# Output: 0
# Explanation: Each level is already sorted in increasing order so return 0.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 105
# All the values of the tree are unique.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 103.6K
# Submissions
# 139.1K
# Acceptance Rate
# 74.5%
# Topics
# Companies
# Hint 1
# We can group the values level by level and solve each group independently.
# Hint 2
# Do BFS to group the value level by level.
# Hint 3
# Find the minimum number of swaps to sort the array of each level.
# Hint 4
# While iterating over the array, check the current element, and if not in the correct index, replace that element with the index of the element which should have come.

# Minimum Operations to Sort Binary Tree by Level - Detailed Solution

## Problem Understanding
We need to:
1. Process a binary tree level by level
2. For each level, find minimum swaps to sort values
3. Sum up all minimum swaps across levels

## Pattern Recognition
1. Tree Traversal Pattern - Level Order (BFS)
2. Array Sorting Pattern - Minimum Swaps to Sort
3. Graph Cycle Detection (for optimal swap counting)

## Visualization
```python
"""
Example Tree Visualization:
Level 0:     1
           /   \
Level 1:   4     3
         /  \   /  \
Level 2: 7    6 8    5

Level-wise arrays before sorting:
Level 0: [1]           -> Already sorted
Level 1: [4, 3]        -> Needs 1 swap
Level 2: [7, 6, 8, 5]  -> Needs 2 swaps

Swap Process for Level 2 [7,6,8,5]:
1. Create position mapping: {5:0, 6:1, 7:2, 8:3}
2. Current: [7,6,8,5] -> Should be: [5,6,7,8]
3. Follow cycles:
   Cycle 1: 7 -> 2, 5 -> 0, 7  (2 swaps)
   Cycle 2: 8 -> 3, 8  (no additional swaps needed)
Total swaps = 2
"""
```

## Solutions

### 1. BFS with Array Sort Comparison (Initial Solution)
```python
from collections import deque
from typing import Optional

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(N * log N) where N is number of nodes
        Space Complexity: O(W) where W is max width of tree
        
        Approach: Use BFS to get levels, then count different positions
        between sorted and unsorted arrays
        """
        if not root:
            return 0
        
        total_swaps = 0
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_vals = []
            
            # Get values at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Count swaps needed for this level
            sorted_vals = sorted(level_vals)
            if sorted_vals != level_vals:
                total_swaps += self.count_swaps_naive(level_vals[:])
                
        return total_swaps
    
    def count_swaps_naive(self, arr: List[int]) -> int:
        """
        Counts minimum swaps using direct comparison with sorted array
        Time: O(n log n) due to sorting
        Space: O(n) for sorted copy
        """
        swaps = 0
        sorted_arr = sorted(arr)
        val_to_pos = {val: i for i, val in enumerate(arr)}
        
        for i, val in enumerate(arr):
            if val != sorted_arr[i]:
                swaps += 1
                # Update positions after swap
                j = val_to_pos[sorted_arr[i]]
                arr[i], arr[j] = arr[j], arr[i]
                val_to_pos[val] = j
                val_to_pos[sorted_arr[i]] = i
                
        return swaps
```

### 2. Optimized Solution using Cycle Detection
```python
from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(N) where N is number of nodes
        Space Complexity: O(W) where W is max width of tree
        
        Optimization: Use cycle detection to count minimum swaps
        """
        if not root:
            return 0
            
        total_swaps = 0
        queue = deque([root])
        
        def count_swaps_cycles(arr: List[int]) -> int:
            """
            Counts minimum swaps using cycle detection
            Time: O(n) as each element is visited once
            Space: O(n) for position mapping
            """
            # Create position mapping for sorted array
            pos = {val: i for i, val in enumerate(sorted(arr))}
            visited = set()
            swaps = 0
            
            for i in range(len(arr)):
                if i in visited or pos[arr[i]] == i:
                    continue
                    
                # Count elements in this cycle
                cycle_size = 0
                j = i
                while j not in visited:
                    visited.add(j)
                    j = pos[arr[j]]
                    cycle_size += 1
                    
                # Minimum swaps for a cycle is (cycle_size - 1)
                swaps += cycle_size - 1
                
            return swaps
        
        while queue:
            level_size = len(queue)
            level = []
            
            # Build level array
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add swaps needed for this level
            total_swaps += count_swaps_cycles(level)
            
        return total_swaps
```

## Complexity Analysis

### Time Complexity
1. Initial Solution: O(N * log N)
   - BFS traversal: O(N)
   - For each level:
     - Sorting: O(k * log k) where k is level size
     - Swap counting: O(k)
   - Total: O(N * log N) dominated by sorting

2. Optimized Solution: O(N)
   - BFS traversal: O(N)
   - For each level:
     - Cycle detection: O(k) where k is level size
   - Total: O(N) as each node is processed once

### Space Complexity
Both solutions: O(W) where W is maximum width of the tree
- Queue storage: O(W)
- Level array: O(W)
- Position mapping: O(W)

## Edge Cases
1. Empty tree: return 0
2. Single node: return 0
3. Already sorted levels: return 0
4. All nodes need swapping
5. Maximum tree size (10^5 nodes)
6. Skewed tree (max height)
7. Perfect binary tree (max width)

## Testing
```python
def test_minimum_operations():
    test_cases = [
        # Empty tree
        (None, 0),
        
        # Single node
        (TreeNode(1), 0),
        
        # Example from problem
        (create_tree([1,4,3,7,6,8,5]), 3),
        
        # Already sorted
        (create_tree([1,2,3,4,5,6]), 0),
        
        # All nodes need swaps
        (create_tree([1,5,2,6,3,4]), 2)
    ]
    
    solution = Solution()
    for tree, expected in test_cases:
        assert solution.minimumOperations(tree) == expected
```

## Follow-up Questions
1. How would you modify the solution for a k-ary tree?
2. Can we optimize memory usage for very wide trees?
3. How would you handle duplicate values if allowed?
4. Can we parallelize the level processing for very large trees?

## Key Insights
1. Breaking down into level-wise arrays simplifies the problem
2. Cycle detection is more efficient than naive swapping
3. BFS is perfect for level-wise processing
4. The solution is optimal as we need to check each node at least once