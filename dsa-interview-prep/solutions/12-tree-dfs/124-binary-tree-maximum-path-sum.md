# 124. Binary Tree Maximum Path Sum

**Difficulty:** Hard
**Pattern:** Tree DFS / Recursion (Post-Order Traversal)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** A path in a binary tree is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to pass through the root. The path sum is the sum of the node's values in the path. Given the `root` of a binary tree, return the maximum path sum.

**Interview Scenario (The "Network Latency" Prompt):**
"You are analyzing data flow in a distributed system, modeled as a tree structure where nodes represent servers and edges represent connections. Each server has an associated 'processing cost' (can be positive or negative, representing gain or loss). You want to find the maximum possible cumulative cost achievable by traversing *any* continuous path through the network, regardless of start or end point. How would you calculate this?"

**Why this transformation?**
*   It emphasizes that the path can start and end anywhere (not necessarily root-to-leaf or root-to-any-node).
*   It introduces negative values, making the "maximum" non-trivial (you might want to skip negative branches).

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty Tree:** "What if the tree is empty?" (Return 0 or handle error, problem typically guarantees non-empty or defines behavior).
2.  **Single Node:** "What if the tree has a single node?" (Return its value).
3.  **Path Definition:** "Confirming, a path must include at least one node?" (Yes, at least one node).
4.  **Values:** "Can node values be negative?" (Yes, this is key for the problem's complexity).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Tree DFS (Post-Order Traversal) with Global Maximum Tracking.

**The Logic:**
This problem is tricky because a path can fork and then merge (forming a "V" shape) if it doesn't need to pass through the root. It also means a path might look like `Left-Child -> Parent -> Right-Child`.

**Key Insight:**
For any given node, there are two types of maximum path sums it can contribute to:
1.  **Path that *starts or ends* at this node and goes upwards:** This path would be `node.val + max(max_path_from_left_child_going_up, max_path_from_right_child_going_up)`. We *cannot* take both left and right children if we are going to continue upwards.
2.  **Path that *passes through* this node and does not go upwards:** This path would be `node.val + max_path_from_left_child_going_up + max_path_from_right_child_going_up`. This forms a "V" shape at the current node.

We need to return type 1 to the parent for its calculation, but we need to update a *global maximum* with type 2.

---

## 4. Base Template & Modification

**Standard DFS Template for Trees (Post-order):**
```python
max_val = -float('inf') # global variable
def dfs(node):
    if not node: return 0
    left_val = dfs(node.left)
    right_val = dfs(node.right)
    
    # Process node.val, left_val, right_val
    # Update global max_val
    # Return value for parent
```

**Modified Logic:**
1.  Initialize `self.max_path_sum = -float('inf')` (or `root.val` if tree is guaranteed non-empty).
2.  In `dfs(node)`:
    *   Recursively call `dfs` on left and right children.
    *   Crucially, `max(0, ...)` for child paths: if a child path sum is negative, it's better to not include it.
    *   Calculate `path_through_node = node.val + left_gain + right_gain` (Type 2).
    *   Update `self.max_path_sum = max(self.max_path_sum, path_through_node)`.
    *   Return `node.val + max(left_gain, right_gain)` (Type 1) to the parent.

---

## 5. Optimal Solution

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a global variable to store the maximum path sum found so far
        # Use negative infinity because node values can be negative
        self.max_path_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively get the maximum path sum from left and right children
            # If a child's path sum is negative, it's better to not include it
            # in a path going upwards, so we take max(0, ...)
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            
            # Calculate the path sum that *passes through* the current node
            # This path *does not* extend upwards to the parent (it forks here).
            # This is one of the candidates for the overall maximum path sum.
            path_through_current_node = node.val + left_gain + right_gain
            
            # Update the global maximum path sum found so far
            self.max_path_sum = max(self.max_path_sum, path_through_current_node)
            
            # Return the maximum path sum that *can extend upwards* from the current node.
            # We can only choose one branch (left or right) to continue the path upwards.
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_path_sum

```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   Each node is visited exactly once during the DFS traversal.
*   **Space Complexity:** $O(H)$ where H is the height of the tree.
    *   This is due to the recursion stack. In the worst case (skewed tree), $H = N$, so $O(N)$. In the best case (balanced tree), $H = \log N$, so $O(\log N)$.

---

## 7. Follow-up & Extensions

**Q: What if the path must start at the root?**
**A:** The problem becomes simpler: `max(dfs(root.left), dfs(root.right))` + `root.val`. You only need to track one max path from the root downwards.

**Q: Find the maximum path sum from root to any leaf?**
**A:** Similar to the above, but you'd need to ensure the path terminates at a leaf and handle negative values carefully.
