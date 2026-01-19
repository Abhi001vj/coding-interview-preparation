# 138. Copy List with Random Pointer

**Difficulty:** Medium
**Pattern:** Linked List / Hash Map (or Interweaving Nodes)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or to `null`. Construct a deep copy of the list. The deep copy should consist of exactly `n` new nodes, where each new node has its `val` and `next` pointer set to the same values as the original node. The `random` pointer of the new nodes should point to new nodes in the copied list, corresponding to the `random` pointers of the original list.

**Interview Scenario (The "Object Graph Duplication" Prompt):**
"You are working on a system that manages complex object graphs, where objects (represented as nodes) have references to other objects (`next`) and potentially arbitrary cross-references (`random`). You need to implement a deep clone operation for such a graph, ensuring that all references within the cloned graph point to newly created, corresponding cloned objects, not to the original objects. Consider memory efficiency and potential cycles in the graph."

**Why this transformation?**
*   It generalizes the problem from a "linked list" to an "object graph," which is a common pattern.
*   It explicitly mentions "deep clone" and "arbitrary cross-references," highlighting the challenge of replicating relationships correctly.
*   "Memory efficiency and potential cycles" hint at the two main solutions: Hash Map (for cycles and arbitrary random) and Interweaving (for memory efficiency).

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty List:** "What if the input list is empty or `null`?" (Return `null`).
2.  **Random to Self/Null:** "Can `random` pointers point to the node itself or to `null`?" (Yes, handle these cases).
3.  **Cycles:** "Are cycles possible through `next` or `random` pointers?" (Yes, for both. This makes a simple recursive deep copy tricky without visited tracking).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Hash Map (Mapping Old Nodes to New Nodes) or Interweaving Nodes.

**Solution 1: Hash Map (Intuitive, but uses $O(N)$ space)**
1.  **First Pass (Create Nodes):** Iterate through the original list. For each original node, create a new node with the same `val`. Store this mapping in a hash map: `original_node -> new_node`.
2.  **Second Pass (Assign Pointers):** Iterate through the original list again. For each original node, retrieve its corresponding new node from the hash map. Then, set the `next` pointer of the new node to `map[original_node.next]` and the `random` pointer to `map[original_node.random]`.

**Solution 2: Interweaving Nodes (More Complex, but $O(1)$ space)**
1.  **First Pass (Create and Interweave):** Iterate through the original list. For each node `curr`, create a new copy `new_node` with `new_node.val = curr.val`. Then, set `new_node.next = curr.next` and `curr.next = new_node`. This creates an interleaved list: `A -> A' -> B -> B' -> C -> C' -> ...`
2.  **Second Pass (Assign Random Pointers):** Iterate through the interleaved list using `curr` (original) and `curr.next` (new_copy). If `curr.random` exists, then `curr.next.random = curr.random.next`.
3.  **Third Pass (Separate Lists):** Separate the original and new lists. This involves carefully re-linking `original.next` and `new_copy.next`.

---

## 4. Base Template & Modification

**Hash Map Template:**
```python
old_to_new = {None: None} # Handle nulls
curr = head
while curr:
    old_to_new[curr] = Node(curr.val)
    curr = curr.next

curr = head
while curr:
    new_node = old_to_new[curr]
    new_node.next = old_to_new[curr.next]
    new_node.random = old_to_new[curr.random]
    curr = curr.next

return old_to_new[head]
```

**Interweaving Template (Conceptual):**
```python
# 1. Interweave
curr = head
while curr:
    new_node = Node(curr.val, curr.next)
    curr.next = new_node
    curr = new_node.next

# 2. Assign Randoms
curr = head
while curr:
    if curr.random:
        curr.next.random = curr.random.next
    curr = curr.next.next # Move to next original node

# 3. Separate
# Requires careful re-linking
```

---

## 5. Optimal Solution (Hash Map Approach - Generally Preferred for Readability/Maintainability)

```python
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Use a hash map to store the mapping from original nodes to new nodes
        # This is crucial for handling random pointers and cycles.
        # Initialize with None -> None to easily handle null next/random pointers.
        old_to_new = {None: None}
        
        # First Pass: Create new nodes and populate the hash map
        # We only copy values and create nodes, not assign pointers yet.
        current_old = head
        while current_old:
            old_to_new[current_old] = Node(current_old.val)
            current_old = current_old.next
            
        # Second Pass: Assign next and random pointers for the new nodes
        current_old = head
        while current_old:
            new_node = old_to_new[current_old]
            
            # Assign next pointer of the new node
            # If current_old.next is None, old_to_new[None] correctly gives None.
            new_node.next = old_to_new[current_old.next]
            
            # Assign random pointer of the new node
            # If current_old.random is None, old_to_new[None] correctly gives None.
            new_node.random = old_to_new[current_old.random]
            
            current_old = current_old.next
            
        # The head of the deep copy is the new node corresponding to the original head
        return old_to_new[head]
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   Two passes through the linked list, each taking $O(N)$ time.
    *   Hash map operations (insertion and lookup) take $O(1)$ on average.
*   **Space Complexity:** $O(N)$
    *   The hash map stores $N$ entries in the worst case (one for each node).

---

## 7. Follow-up & Extensions

**Q: Implement the $O(1)$ space solution (Interweaving Nodes).**
**A:** This is more complex but is often asked as a follow-up to optimize space.
*   **Pass 1:** For each original node `curr`, create `new_node = Node(curr.val)`, set `new_node.next = curr.next`, and `curr.next = new_node`. This interleaves `A -> A' -> B -> B' -> ...`
*   **Pass 2:** For each original node `curr`, if `curr.random` exists, then `curr.next.random = curr.random.next` (the new random pointer points to the new version of the random target).
*   **Pass 3:** Separate the two lists. Restore `original_node.next` and correctly link `new_node.next`.

**Q: What if nodes can have multiple arbitrary pointers (e.g., `prev`, `child1`, `child2`)?**
**A:** The Hash Map approach is more easily extendable. For each pointer type, you'd just map `new_node.pointer_type = old_to_new[old_node.pointer_type]`.
