"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
947. Most Stones Removed with Same Row or Column
Medium
Topics
Companies
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.
LEETCODE 947: Most Stones Removed with Same Row or Column
Comprehensive Solution with Pattern Analysis, Visualizations, and Multiple Approaches

PATTERN ANALYSIS:
---------------
1. Problem Pattern Recognition: Graph/Connected Components
   Why? Consider this visualization of test case 1:
   
   0 1 2  <- columns
0  O O ·     O = stone
1  O · O     · = empty
2  · O O
↑
rows

   Connected Components Visual:
   [0,0] --row--> [0,1]
         --col--> [1,0]
   [0,1] --col--> [2,1]
   [2,1] --row--> [2,2]
   [2,2] --col--> [1,2]
   [1,2] --row--> [1,0]

   Key Insights:
   * Stones in same row/col form implicit edges
   * Can remove stone if connected to another
   * Forms connected components
   * Must leave 1 stone per component
   * Can remove: total_stones - num_components

DATA STRUCTURE ANALYSIS:
----------------------
1. Approach Options:

   a) Grid Matrix:
      Pros: - Visual representation
            - Direct access O(1)
      Cons: - Sparse matrix wastes space
            - Size limited by max coordinates
      
      Visual of sparse matrix issue:
      For input [[0,0], [10000,10000]]:
      O · · · · · · (10000 spaces) · · · ·
      · · · · · · · (10000 spaces) · · · ·
      · · · · · · · (10000 spaces) · · · O

   b) Graph Adjacency List:
      Pros: - Space efficient
            - Natural for connectivity
      Cons: - Need to build connections
            - Extra structures needed
      
      Visual:
      [0,0] -> {[0,1], [1,0]}
      [0,1] -> {[0,0], [2,1]}
      [1,0] -> {[0,0]}
      etc.

   c) Union-Find (Disjoint Set):
      Pros: - O(1) amortized operations
            - Perfect for components
            - Space efficient
      Cons: - Can't track removal order
            - Needs coordinate mapping

      Visual:
      parent = {
          0: 0,     # row 0
          1: 1,     # row 1
          10001: 0, # col 0 (offset)
          10002: 1, # col 1 (offset)
      }

SOLUTION APPROACHES:
------------------
1. Exhaustive Search Solution:
"""

def exhaustive_search_removal(stones):
    """
    Approach 1: Exhaustive Search (NOT backtracking)
    Time: O(n!)
    Space: O(n)
    
    Process visualization on first test case:
    Initial:    Final:
    O O ·       · · ·
    O · O  -->  · · ·
    · O O       O · ·
    
    Removal sequences possible:
    Seq1: [2,2] -> [2,1] -> [1,2] -> [1,0] -> [0,1] -> [0,0]
    Seq2: [0,1] -> [2,1] -> [2,2] -> [1,2] -> [1,0] -> [0,0]
    etc.
    """
    def can_remove(stone, remaining):
        x, y = stone
        return any(rx == x or ry == y for rx, ry in remaining)
    
    def search(stones_left, removed_count):
        nonlocal max_removed
        # Try each remaining stone
        for i in range(len(stones_left)):
            stone = stones_left[i]
            remaining = stones_left[:i] + stones_left[i+1:]
            if can_remove(stone, remaining):
                search(remaining, removed_count + 1)
        max_removed = max(max_removed, removed_count)
    
    max_removed = 0
    search(stones.copy(), 0)
    return max_removed

"""
2. Optimized Union-Find Solution:

Key Optimization Insights:
------------------------
1. Don't need actual removal order
2. Just need count of removable stones
3. Stones in same component can all be removed except one
4. Total removable = total_stones - num_components

Union-Find Process Visual:
Initial stones: [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

Step 1: Map coordinates
rows = {0,1,2}
cols = {10001,10002,10003} (offset for uniqueness)

Step 2: Union process:
[0,0]: union(0, 10001)    [0,1]: union(0, 10002)
O O ·     -->      O O ·
· · ·              · · ·
· · ·              · · ·

[1,0]: union(1, 10001)    [1,2]: union(1, 10003)
O O ·     -->      O O ·
O · O              O · O
· · ·              · · ·

And so on...
"""

def union_find_removal(stones):
    """
    PATTERN VISUALIZATION AND ANALYSIS:
    ---------------------------------
    Example stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    
    Grid Visualization:
    0 1 2  <- columns
    0 O O ·     O = stone
    1 O · O     · = empty
    2 · O O
    ↑
    rows
    
    Connected Components Formation:
    [0,0]---row---[0,1]
      |            |
      col          col
      |            |
    [1,0]  [1,2]--row--[2,2]
               |
               col
               |
              [2,1]

    TIME COMPLEXITY: O(N * α(N))
    ---------------------------
    * N = number of stones
    * α = inverse Ackermann function
        - Grows extremely slowly
        - For all practical values of n, α(n) ≤ 4
        - Makes our operations effectively constant time
        Example: α(2^65536) = 4
                α(A(A(100))) = 4  where A is Ackermann function
    
    SPACE COMPLEXITY: O(R + C)
    -------------------------
    * R = maximum row coordinate
    * C = maximum column coordinate
    * We need arrays of size (R + C + 2) for parent and rank
    
    UNION-FIND TERMS:
    ---------------
    1. Path Compression:
       Before:          After find(4):
       1                1
       ↓                ↓
       2         →      2,3,4
       ↓                (all point to 1)
       3
       ↓
       4

    2. Union by Rank:
       Rank = approximate tree height
       Always attach smaller tree to larger:
       rank=2   rank=3     rank=3
       1        4          4
       ↓ ↓      ↓ ↓  →    ↓ ↓ ↓
       2,3      5,6        5,6,1→(2,3)

    3. Components:
       Each disjoint set = one component
       Number of removable stones = total stones - components
    """
    # Get max coordinates for parent/rank array sizing
    max_row = max(i for i, _ in stones)
    max_col = max(j for _, j in stones)
    
    """
    ARRAY INITIALIZATION:
    -------------------
    For stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    max_row = 2, max_col = 2
    array size = 2 + 2 + 2 = 6 (max_row + max_col + 2)
    
    Indexing scheme:
    [0,1,2] = row indices
    [3,4,5] = column indices (after offset)
    """
    parent = [i for i in range(max_row + max_col + 2)]
    rank = [1] * (max_row + max_col + 2)
    
    def find(n):
        """
        Path Compression Example:
        Initial parent array: [0,1,2,3,1,1]
        After find(3):       [0,1,2,1,1,1]
        """
        p = parent[n]
        while p != parent[p]:
            parent[p] = parent[parent[p]]  # Compress path
            p = parent[p]
        return p
    
    def union(n1, n2):
        """
        Union by Rank Example:
        Initial ranks:     [2,1,1,1]
        After union(1,2):  [2,2,1,1]
        After union(1,3):  [3,2,1,1]
        """
        p1, p2 = find(n1), find(n2)
        if p1 == p2:  # Already in same component
            return 0
        if rank[p1] > rank[p2]:  # Attach smaller to larger
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        return 1  # New connection made
    
    # Column indices start after row indices
    col_offset = max_row + 1
    
    """
    COMPONENT TRACKING:
    -----------------
    Example Process:
    Initial:    components = 0, seen = {}
    Add [0,0]:  components = 2, seen = {0, 3}  (row 0, col 0+offset)
    Add [0,1]:  components = 3, seen = {0, 3, 4}
    Union(0,3): components = 2  (connected row 0 to col 0)
    """
    components = 0
    seen = set()
    
    # Count initial components (unique rows and columns)
    for r, c in stones:
        if r not in seen:
            seen.add(r)
            components += 1
        if (c + col_offset) not in seen:
            seen.add(c + col_offset)
            components += 1
    
    # Connect stones through their row/column relationships
    for r, c in stones:
        components -= union(r, c + col_offset)
    
    return len(stones) - components
def union_find_removal(stones):
    """
    Approach 2: Union-Find (Optimal)
    Time: O(N * α(N)) where α is inverse Ackermann
    Space: O(N)
    
    Example run:
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    
    Process:
    1. Initial sets: {0,1,2} (rows) and {10001,10002,10003} (cols)
    2. Unions reduce to single component
    3. Result: 6 stones - 1 component = 5 removable
    """
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return 1  # New connection
        return 0  # Already connected
    
    # Map coordinates to unique values
    # Add 10001 to cols to avoid collision
    points = set()
    for x, y in stones:
        points.add(x)
        points.add(y + 10001)
    
    # Initialize disjoint sets
    parent = {x: x for x in points}
    components = len(points)
    
    # Connect rows and columns
    for x, y in stones:
        components -= union(x, y + 10001)
    
    return len(stones) - components

"""
TESTING AND VERIFICATION:
-----------------------
Test Case Analysis:

1. Example 1: [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
   Visual:
   O O ·
   O · O
   · O O
   
   Result: 5 (all but one can be removed)

2. Example 2: [[0,0],[0,2],[1,1],[2,0],[2,2]]
   Visual:
   O · O
   · O ·
   O · O
   
   Result: 3 (forms multiple components)

3. Edge Case: [[0,0]]
   Visual:
   O
   
   Result: 0 (single stone, no removals possible)
"""

# Test execution
if __name__ == "__main__":
    test_cases = [
        [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]],  # Example 1
        [[0,0],[0,2],[1,1],[2,0],[2,2]],        # Example 2
        [[0,0]]                                  # Edge case
    ]
    
    for i, stones in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Stones: {stones}")
        print(f"Exhaustive Search Result: {exhaustive_search_removal(stones)}")
        print(f"Union-Find Result: {union_find_removal(stones)}")