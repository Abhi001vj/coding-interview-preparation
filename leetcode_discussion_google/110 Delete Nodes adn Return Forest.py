# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
# 1110. Delete Nodes And Return Forest
# Medium
# Topics
# Companies
# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# Example 2:

# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
 

# Constraints:

# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.


```python
"""
DELETING NODES AND CREATING FOREST
---------------------------------

Key Idea:
- Use DFS to traverse tree
- When we find a node to delete:
  1. Add its children to result if they're not to be deleted
  2. Return None to remove it from parent
- Keep track of nodes that should be in result

Example Visualization:
Initial Tree:
     1
   /   \
  2     3*
 / \   / \
4   5* 6   7

to_delete = [3,5]
* marks nodes to delete

Process:
1. Start at root (1)
   - Not in to_delete, will be in result
   - Process children

2. Process left child (2)
   - Not in to_delete
   - Process its children
   
3. Process node 4
   - Not in to_delete
   - No children
   
4. Process node 5
   - In to_delete
   - No children
   - Return None to parent 2
   
5. Process node 3
   - In to_delete
   - Children 6,7 become roots
   - Add 6,7 to result
   - Return None to parent 1

Final Forest:
  1        6    7
 /
2
 \
  4

Result: [[1,2,4], [6], [7]]
"""

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)  # Convert to set for O(1) lookup
        forest = []  # Store roots of resulting trees
        
        def dfs(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            """
            DFS helper function
            Args:
                node: current node being processed
                is_root: whether current node could be a root
            Returns:
                Node or None (if node should be deleted)
            """
            if not node:
                return None
                
            # Process current node
            is_deleted = node.val in to_delete_set
            
            # If this could be a root and it's not being deleted,
            # add it to our forest
            if is_root and not is_deleted:
                forest.append(node)
            
            # Process children
            # Children become roots if current node is deleted
            node.left = dfs(node.left, is_deleted)
            node.right = dfs(node.right, is_deleted)
            
            # If current node should be deleted,
            # return None to remove it from parent
            return None if is_deleted else node
        
        # Start DFS from root
        # Root is always a potential root node
        dfs(root, True)
        return forest
    
"""
Time Complexity: O(N) 
- Visit each node exactly once
- Set lookup is O(1)

Space Complexity: O(H + D) where:
- H is height of tree (recursion stack)
- D is size of to_delete set

Example Detailed Trace:
root = [1,2,3,4,5,6,7], to_delete = [3,5]

1. dfs(1, True)
   - not in to_delete
   - add to forest
   - process children
   
2. dfs(2, False)
   - not in to_delete
   - process children
   
3. dfs(4, False)
   - not in to_delete
   - return node 4
   
4. dfs(5, False)
   - in to_delete
   - return None
   
5. dfs(3, False)
   - in to_delete
   - process children as roots
   
6. dfs(6, True)
   - not in to_delete
   - add to forest
   
7. dfs(7, True)
   - not in to_delete
   - add to forest

Forest builds up:
[1] -> [1, 6] -> [1, 6, 7]
"""
```

Why it works:

Stack Nature:

pythonCopy# Each recursive call pushes node onto stack:
dfs(1) -> dfs(2) -> dfs(4) -> dfs(null)
# Then unwinds, handling each node:
null <- 4 <- 2 <- 1

Assignment + Return:

pythonCopynode.left = dfs(node.left, is_deleted)
# This both:
# 1. Processes the entire left subtree
# 2. Updates the left pointer with result

Complete Coverage:

pythonCopy# DFS naturally visits every node because:
# 1. Base case catches nulls
# 2. Recursive calls handle both children
# 3. Stack ensures we return to each parent
Visual of Stack:
CopyInitial:    [dfs(1)]
Push left:  [dfs(1), dfs(2)]
Push left:  [dfs(1), dfs(2), dfs(4)]
Pop null:   [dfs(1), dfs(2), dfs(4)]
Pop 4:      [dfs(1), dfs(2)]
Push right: [dfs(1), dfs(2), dfs(5)]
Pop 5:      [dfs(1), dfs(2)]
Pop 2:      [dfs(1)]
Push right: [dfs(1), dfs(3)]
Pop null:   [dfs(1)]
Pop 1:      []
We don't need explicit iteration because the recursion stack maintains our place in the tree and ensures we visit every node exactly once. Each dfs call handles its subtree completely before returning.


what will change if the values of the nodes ar enot unique? will we need to dlete mul;tiple nodes ? whatbahppens if this is not a bianry tree but a regular graph?EditGreat questions! Let's analyze each scenario:

Non-Unique Values in Tree:

pythonCopyExample:
     1
   /   \
  2     2*  (* means to delete value 2)
 / \   / \
2   3 4   2
We'd need to modify our code to handle this:
pythonCopydef delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    forest = []
    
    def dfs(node, is_root):
        if not node:
            return None
            
        # Now multiple nodes might have this value
        is_deleted = node.val in to_delete
        if is_root and not is_deleted:
            forest.append(node)
            
        # Need to process ALL nodes with this value
        node.left = dfs(node.left, is_deleted)
        node.right = dfs(node.right, is_deleted)
        
        # Still works same way but will delete all nodes with this value
        return None if is_deleted else node

For a General Graph:
We need significant changes because:


Can have cycles
Can have multiple paths to same node
No clear parent-child relationship

pythonCopydef deleteNodes(self, graph: Dict[int, List[int]], to_delete: List[int]) -> List[List[int]]:
    forests = []
    visited = set()
    
    def dfs(node, parent):
        if node in visited:
            return
            
        visited.add(node)
        is_deleted = node in to_delete
        
        # Create new component if not deleted
        if not is_deleted:
            current_forest = [node]
            forests.append(current_forest)
            
        # Process all neighbors
        for neighbor in graph[node]:
            if neighbor != parent:  # Avoid going back
                if not is_deleted:
                    # Add to current forest
                    current_forest.append(neighbor)
                dfs(neighbor, node)
                
    # Need to start DFS from each unvisited node
    for node in graph:
        if node not in visited:
            dfs(node, None)
Key Differences with Graph:

Need visited set to handle cycles:

pythonCopyvisited = set()
if node in visited:
    return

Multiple paths possible:

pythonCopy# Can't just use parent-child links
for neighbor in graph[node]:
    if neighbor != parent:  # Need to track parent

Forest creation is different:

pythonCopy# Can't rely on tree structure
if not is_deleted:
    current_forest = [node]
    forests.append(current_forest)

Connectivity handling:

pythonCopy# Need to check all components
for node in graph:
    if node not in visited:
        dfs(node, None)
Example with Graph:
pythonCopyGraph:
1 --- 2 --- 3
|     |     |
4 --- 5 --- 6

to_delete = [2, 5]

After deletion:
1   3
|   |
4   6

Need to:
1. Handle cycles
2. Track visited nodes
3. Create new forests properly
4. Maintain connectivity information
