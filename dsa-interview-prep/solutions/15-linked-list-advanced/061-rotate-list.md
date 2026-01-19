# 61. Rotate List

**Difficulty:** Medium
**Pattern:** Linked List Manipulation

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given the `head` of a linked list, rotate the list to the right by `k` places.

**Interview Scenario (The "Circular Buffer Shift" Prompt):**
"You are managing a log buffer or a task queue in an embedded system that behaves like a circular list. Occasionally, you need to 'shift' the view of this buffer by `k` positions to the right (or left). This means the logical 'start' of the buffer moves. Implement a function to perform this cyclic shift without copying all data, by only re-pointing a few pointers. `k` can be very large."

**Why this transformation?**
*   It provides a real-world use case for linked list rotation.
*   It emphasizes the "in-place" aspect by avoiding full data copying.
*   The `k` can be very large ($k > list_length$), which is a common trick.

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty List:** "What if the list is empty or has only one node?" (Return head as is).
2.  **`k` Value:** "Can `k` be 0? Or negative?" (Assume non-negative as per problem, 0 implies no rotation).
3.  **Large `k`:** "What if `k` is larger than the length of the list?" (Equivalent to `k % length` rotations).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Linked List (Two Pointers / Connect Head to Tail).

**The Logic:**
1.  **Handle Edge Cases:** If list is empty, single node, or `k=0`, return early.
2.  **Find Length and Make Circular:** Traverse the list to find its `length` and connect the `tail` to the `head`. This makes it a circular list for easier manipulation.
3.  **Find New Tail and New Head:** To rotate right by `k` places, the new tail will be the node at `length - (k % length) - 1` position from the original head. The node *after* this new tail will be the new head.
    *   Example: `1->2->3->4->5`, `k=2`.
    *   Length = 5. `k % length = 2`.
    *   New tail at `5 - 2 - 1 = 2` (0-indexed). So `3` is the new tail.
    *   `4` is the new head.
4.  **Break Circle:** Set `new_tail.next = None`.

---

## 4. Base Template & Modification

**Standard Linked List Traversal:**
```python
curr = head
while curr:
    # Process curr
    curr = curr.next
```

**Modified Logic:**
Three passes:
1.  Count length, find tail, connect tail to head.
2.  Traverse to find new tail and new head.
3.  Break the circle.

---

## 5. Optimal Solution

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
            
        # Step 1: Find the length of the list and connect tail to head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        tail.next = head # Make it a circular list
        
        # Step 2: Calculate effective rotations
        # k could be greater than length, so take modulo
        k %= length
        
        # If k is 0 after modulo, no actual rotation is needed. The list is already circular.
        # However, we still need to break the circle at the original tail to restore it.
        # A more robust check might be: if k == 0 and length > 1, then no rotation needed
        # but to break the circle at old tail: tail.next = None and return head (original)
        # But the problem implies k rotations, so if k % length == 0, we still need to perform the operation to change head
        # For example, [1,2,3] k=3. Result is [1,2,3]. Our logic will make it [1,2,3].
        
        # Step 3: Find the new tail and new head
        # To rotate right by k, the new tail will be at (length - k - 1) position from original head.
        # (length - k - 1) because it's 0-indexed and we want the node *before* the new head.
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        
        # Step 4: Break the circle
        new_tail.next = None
        
        return new_head
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   One pass to find length and connect tail to head.
    *   One pass to find new tail/head.
*   **Space Complexity:** $O(1)$
    *   Only a few pointer variables used.

---

## 7. Follow-up & Extensions

**Q: Rotate Left by `k` places.**
**A:** To rotate left by `k` is equivalent to rotating right by `length - k` places. The same logic applies after adjusting `k`.

**Q: What if you are only allowed one pass?**
**A:** This is harder. You could use two pointers, one `k` steps ahead of the other. When the leading pointer reaches the end, the trailing pointer is at the new tail. Requires careful handling of circularity. (Similar to finding $N^{th}$ node from end).
