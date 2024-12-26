# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# 138. Copy List with Random Pointer
# Medium
# Topics
# Companies
# Hint
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

 

# Example 1:


# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:


# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:



# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
 

# Constraints:

# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.

```python
"""
COPY LIST WITH RANDOM POINTER: Complete Analysis
=============================================

Pattern Recognition:
1. Hash Map for Node Mapping
2. Interweaving Nodes
3. Graph Cloning
4. Two-Pass Solutions
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def hashmap_solution(head: 'Node') -> 'Node':
    """
    Approach 1: Hash Map
    Pattern: Node Mapping using Dictionary
    
    Example: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    
    Visual Process:
    1. First Pass (Create Nodes):
    Original:  7 -> 13 -> 11 -> 10 -> 1
    Hashmap: {
        7: Node(7),
        13: Node(13),
        11: Node(11),
        10: Node(10),
        1: Node(1)
    }
    
    2. Second Pass (Connect Pointers):
    For each node:
        new_node.next = hashmap[old_node.next]
        new_node.random = hashmap[old_node.random]
        
    Time: O(n)
    Space: O(n)
    """
    if not head:
        return None
        
    # First pass: create nodes
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next
        
    # Second pass: connect pointers
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next
        
    return old_to_new[head]

def interweaving_solution(head: 'Node') -> 'Node':
    """
    Approach 2: Interweaving Nodes
    Pattern: In-place Node Creation and Connection
    
    Example Visual Process:
    1. Original List:
    7 -> 13 -> 11 -> 10 -> 1
    
    2. Interweave copied nodes:
    7 -> 7' -> 13 -> 13' -> 11 -> 11' -> 10 -> 10' -> 1 -> 1'
    
    3. Connect random pointers:
    For each original node:
        node.next.random = node.random.next
        
    4. Separate lists:
    Original: 7 -> 13 -> 11 -> 10 -> 1
    Copy:     7' -> 13' -> 11' -> 10' -> 1'
    
    Time: O(n)
    Space: O(1) extra space
    """
    if not head:
        return None
        
    # Step 1: Interweave nodes
    curr = head
    while curr:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next
        
    # Step 2: Connect random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
        
    # Step 3: Separate lists
    dummy = Node(0)
    curr_new = dummy
    curr = head
    while curr:
        # Extract copy node
        curr_new.next = curr.next
        curr_new = curr_new.next
        
        # Restore original list
        curr.next = curr.next.next
        curr = curr.next
        
    return dummy.next

def recursive_solution(head: 'Node') -> 'Node':
    """
    Approach 3: Recursive DFS
    Pattern: Graph Clone using DFS
    
    Visual Process:
    Original: 7 -> 13 -> 11 -> 10 -> 1
    
    Recursive Stack:
    1. visit(7):
       - create Node(7)
       - visit(13)
       
    2. visit(13):
       - create Node(13)
       - visit(11)
       ...
       
    Time: O(n)
    Space: O(n) - recursion stack
    """
    visited = {}
    
    def copy_node(node: 'Node') -> 'Node':
        if not node:
            return None
            
        # Return if already copied
        if node in visited:
            return visited[node]
            
        # Create new node
        copy = Node(node.val)
        visited[node] = copy
        
        # Recursively copy next and random
        copy.next = copy_node(node.next)
        copy.random = copy_node(node.random)
        
        return copy
        
    return copy_node(head)

"""
EDGE CASES AND SPECIAL CONDITIONS
-------------------------------
1. Empty list
2. Single node
3. Circular random pointers
4. Self-referential random pointers
5. All random pointers null
6. All nodes pointing to same random node

VISUALIZATION OF SPACE-TIME TRADEOFFS
----------------------------------
Approach     Time    Space   Advantages
-----------------------------------------------------------------------------
HashMap      O(n)    O(n)    Simple implementation, clear node mapping
Interweaving O(n)    O(1)    Space optimal, but complex pointer manipulation
Recursive    O(n)    O(n)    Natural for graph-like structures, clear logic

OPTIMIZATION TECHNIQUES
--------------------
1. Early termination for empty/single node
2. In-place modification where possible
3. Pointer arithmetic to avoid extra space
4. Single pass when possible

EXAMPLE WALKTHROUGHS
------------------
For input: [[7,null],[13,0],[11,4],[10,2],[1,0]]

HashMap Approach:
1. Create nodes: {7:7', 13:13', 11:11', 10:10', 1:1'}
2. Connect pointers:
   7'.next = 13'
   13'.next = 11'
   11'.next = 10'
   10'.next = 1'
   13'.random = 7'
   ...

Interweaving Approach:
1. Original:    7 -> 13 -> 11 -> 10 -> 1
2. Interweave: 7 -> 7' -> 13 -> 13' -> 11 -> 11' -> 10 -> 10' -> 1 -> 1'
3. Connect random pointers
4. Separate lists

Recursive Approach:
1. Copy 7, mark visited
2. Recurse on next (13)
3. Recurse on random (null)
4. Continue pattern
"""

```python
"""
DEEP COPY WITH RANDOM POINTER: Detailed Solution Analysis
====================================================

Example Input Visualization:
Original List: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Visual Representation:
7 -> 13 -> 11 -> 10 -> 1
↓     ↓     ↓     ↓    ↓
null  7    null   11   7
"""

def recursiveHashMap_solution(head: 'Node') -> 'Node':
    """
    APPROACH 1: RECURSIVE HASH MAP
    ----------------------------
    State Evolution for [[7,null],[13,0],[11,4],[10,2],[1,0]]:
    
    Recursive Call Stack:
    1. copy(7):
       map = {7: 7'}
       -> copy(13)
       
    2. copy(13):
       map = {7: 7', 13: 13'}
       -> copy(11)
       -> set 13'.random = map[7]
       
    3. copy(11):
       map = {7: 7', 13: 13', 11: 11'}
       -> copy(10)
       
    Visual Process:
    Original →  Copy
    7       →   7'   map[7] = 7'
    13      →   13'  map[13] = 13', 13'.random = map[7]
    11      →   11'  map[11] = 11'
    10      →   10'  map[10] = 10'
    1       →   1'   map[1] = 1'
    """
    def copyNode(node, visited={}):
        if not node:
            return None
        if node in visited:
            return visited[node]
        
        # Create new node and cache it
        copy = Node(node.val)
        visited[node] = copy
        
        # Recursively build next and random
        copy.next = copyNode(node.next, visited)
        copy.random = copyNode(node.random, visited)
        return copy
    
    return copyNode(head)

def twoPassHashMap_solution(head: 'Node') -> 'Node':
    """
    APPROACH 2: TWO PASS HASH MAP
    ---------------------------
    Pass 1: Create all nodes
    Pass 2: Connect all pointers
    
    Visual Process:
    
    Pass 1 (Node Creation):
    Original: 7 -> 13 -> 11 -> 10 -> 1
    
    Map Building:
    {
        7  → Node(7)
        13 → Node(13)
        11 → Node(11)
        10 → Node(10)
        1  → Node(1)
    }
    
    Pass 2 (Connect Pointers):
    Step 1: 7' → 13'  (next)
           7' → null  (random)
           
    Step 2: 13' → 11' (next)
           13' → 7'   (random)
           ...
    """
    if not head:
        return None
        
    # First pass: create nodes
    oldToCopy = {None: None}
    curr = head
    while curr:
        oldToCopy[curr] = Node(curr.val)
        curr = curr.next
        
    # Second pass: connect pointers
    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next
        
    return oldToCopy[head]

def spaceOptimized_solution(head: 'Node') -> 'Node':
    """
    APPROACH 3: SPACE OPTIMIZED (INTERWEAVING)
    --------------------------------------
    Three-phase approach using interleaved nodes
    
    Phase 1: Create Interleaved List
    Original: 7 -> 13 -> 11
    Becomes:  7 -> 7' -> 13 -> 13' -> 11 -> 11'
    
    Phase 2: Set Random Pointers
    For each node:
        node.next.random = node.random.next
    
    Visual:
    7  -> 7'  -> 13 -> 13' -> 11 -> 11'
    ↓     ↓      ↓     ↓      ↓     ↓
    null  null   7    7'     null  null
    
    Phase 3: Separate Lists
    Original: 7  -> 13 -> 11
    Copy:    7' -> 13'-> 11'
    
    Complete Process Visual:
    Step 1:
    7 -> 13 -> 11
    ↓
    7 -> 7' -> 13 -> 13' -> 11 -> 11'
    
    Step 2: Connect randoms
    7 -> 7' -> 13 -> 13' -> 11 -> 11'
         ↓          ↓           ↓
        null       7'         null
        
    Step 3: Separate
    7 -> 13 -> 11
    7' -> 13'-> 11'
    """
    if not head:
        return None
    
    # Phase 1: Create interleaved list
    curr = head
    while curr:
        copy = Node(curr.val)
        copy.next = curr.next
        curr.next = copy
        curr = copy.next
    
    # Phase 2: Connect random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    
    # Phase 3: Separate lists
    dummy = Node(0)
    copy_curr = dummy
    curr = head
    
    while curr:
        # Extract nodes
        copy_curr.next = curr.next
        curr.next = curr.next.next
        
        copy_curr = copy_curr.next
        curr = curr.next
    
    return dummy.next

"""
COMPLEXITY ANALYSIS FOR ALL APPROACHES
-----------------------------------
1. Hash Map (Recursive):
   Time: O(n) - Visit each node once
   Space: O(n) - Stack + HashMap
   
2. Two Pass Hash Map:
   Time: O(n) - Two passes
   Space: O(n) - HashMap

3. Space Optimized:
   Time: O(n) - Three passes
   Space: O(1) - No extra storage

TRADE-OFFS:
----------
1. Hash Map Approaches:
   + Simple to implement
   + Easy to understand
   - Extra space for hash map

2. Space Optimized:
   + Constant extra space
   - Complex pointer manipulation
   - Multiple passes required
   - More prone to errors

EDGE CASES VISUALIZATION:
----------------------
1. Empty List:
   Input: null
   Output: null

2. Single Node with Self Loop:
   Input: [1,0]
   Visual: 1 ↔ 1

3. Circular Random Pointers:
   Input: [[1,1],[2,0]]
   Visual: 1 → 2
          ↑   ↓
          └───┘
"""