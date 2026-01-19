# 237. Delete Node in a Linked List

**Difficulty:** Medium
**Pattern:** Linked List Manipulation

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Write a function to delete a node (except the tail) in a singly linked list, given only access to that node. You are given `node` (the node to be deleted) and you **will not be given access to the head** of the list.

**Interview Scenario (The "Embedded System Cleanup" Prompt):**
"Imagine you're developing firmware for an embedded device that manages a sequence of tasks in a linked list. Due to strict memory constraints and a design decision, a task scheduler function needs to remove a completed task from the list, but it only receives a pointer to the task itself, not the head of the entire task queue. How would you implement this 'self-deletion' function, assuming the task is never the last one in the queue?"

**Why this transformation?**
*   It explicitly states the unusual constraint: **no access to the head**. This is the core trick of the problem.
*   It provides a practical context for such a constraint (embedded systems, limited scope).
*   It highlights the `not tail` assumption.

---

## 2. Clarifying Questions (Phase 1)

1.  **Tail Node:** "Confirming that the given `node` will *never* be the tail of the list?" (Yes, this is critical, as we can't delete the tail without its predecessor).
2.  **Singly Linked List:** "Is it a singly or doubly linked list?" (Singly, implies no `prev` pointer).
3.  **Memory:** "Do I need to deallocate memory (in C++/Java)?" (In Python, garbage collection handles this, but conceptually yes, if applicable).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Linked List (Tricky Manipulation).

**The Trap:**
Normally, to delete a node, you need its *predecessor* to bypass it (`predecessor.next = node.next`). But here, we *only* have `node`.

**The Key Insight:**
If we can't delete `node` directly, we can *overwrite* `node` with the values of its `next` node, and then delete the `next` node. This effectively removes `node`'s data and shifts `next`'s data to `node`'s position. Since `node` is not the tail, `node.next` always exists.

**Steps:**
1.  Copy the value of `node.next` to `node.val`.
2.  Copy the `next` pointer of `node.next` to `node.next`.
    *   Essentially, `node.val = node.next.val` and `node.next = node.next.next`.

This looks like we deleted `node`, but technically we deleted `node.next` and replaced `node`'s content with `node.next`'s content.

---

## 4. Base Template & Modification

**Standard Linked List Deletion (requires predecessor):**
```python
# Assume prev is the node before target_node
prev.next = target_node.next
```

**Modified Logic (Self-deletion):**
```python
# Given `node` to delete
node.val = node.next.val
node.next = node.next.next
```

---

## 5. Optimal Solution

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode):
        """
        Deletes a node from a singly linked list, given only access to that node.
        The node is guaranteed not to be the tail.
        """
        
        # Step 1: Overwrite the current node's value with the value of its next node.
        # This effectively "moves" the data of the next node to the current node's position.
        node.val = node.next.val
        
        # Step 2: Bypass the next node by linking the current node to the node after its next.
        # This effectively "deletes" the next node, as it's no longer reachable.
        node.next = node.next.next
        
        # The original 'node.next' is now garbage collected in Python.
        # In languages like C++, you would explicitly `delete temp_node;` if you stored node.next in temp_node.
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(1)$
    *   Performs a constant number of operations (two assignments).
*   **Space Complexity:** $O(1)$
    *   Uses a constant amount of extra space.

---

## 7. Follow-up & Extensions

**Q: What if the node *can* be the tail?**
**A:** This problem becomes impossible if you only have access to the tail node and not its predecessor in a singly linked list. You cannot modify the `next` pointer of the predecessor if you don't know what it is. If you could traverse from the head, you would find the predecessor and then delete the tail.

**Q: What if it's a doubly linked list?**
**A:** If `node` has access to `prev` and `next`, then it's straightforward:
`node.prev.next = node.next`
`node.next.prev = node.prev`
(And handle `null` checks for `prev`/`next` appropriately).
