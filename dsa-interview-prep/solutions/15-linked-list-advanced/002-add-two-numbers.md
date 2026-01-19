# 2. Add Two Numbers

**Difficulty:** Medium
**Pattern:** Linked List (Digit by Digit Addition)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

**Interview Scenario (The "Big Number Arithmetic" Prompt):**
"You are implementing a calculator for arbitrary-precision integers, where numbers can be extremely large and don't fit into standard integer types. These numbers are represented as linked lists, with the least significant digit at the head. Implement the addition operation for two such numbers. You should also consider how to handle potential carries and create a new linked list for the result."

**Why this transformation?**
*   It provides a clear motivation for using linked lists for arbitrary-precision arithmetic.
*   It highlights the core concepts of digit-by-digit addition and carry propagation.

-----n

## 2. Clarifying Questions (Phase 1)

1.  **Empty Lists:** "Are the lists guaranteed non-empty?" (Problem states non-empty).
2.  **Leading Zeroes:** "Can the numbers have leading zeros (except for the number 0 itself)?" (Usually no, but good to confirm. Output should not have leading zeros either, unless the result is 0).
3.  **Output:** "Return a new linked list, or modify one of the inputs?" (Return a new one).
4.  **Number Sign:** "Are they non-negative?" (Yes, simplifies handling signs).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Linked List (Traversal / Arithmetic Simulation).

**The Logic:**
Since digits are in reverse order (LSD first), we can iterate through both lists simultaneously, just like how we perform addition by hand.

1.  Initialize a `dummy_head` for the result list and a `current` pointer.
2.  Initialize `carry = 0`.
3.  Loop while `l1` or `l2` or `carry` is not empty/zero:
    *   Get `val1 = l1.val` (or 0 if `l1` is `None`). Advance `l1`.
    *   Get `val2 = l2.val` (or 0 if `l2` is `None`). Advance `l2`.
    *   `current_sum = val1 + val2 + carry`.
    *   `carry = current_sum // 10`.
    *   `digit = current_sum % 10`.
    *   Create a new node `ListNode(digit)` and append it to `current.next`.
    *   Advance `current`.
4.  Return `dummy_head.next`.

---

## 4. Base Template & Modification

**Standard Linked List Traversal (simultaneous):**
```python
dummy = ListNode(0)
curr = dummy
carry = 0
while l1 or l2 or carry:
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    
    # Calculation logic
    
    curr.next = ListNode(new_digit)
    curr = curr.next
    
    if l1: l1 = l1.next
    if l2: l2 = l2.next
return dummy.next
```

**Modified Logic:** None, this is the canonical template for linked list addition.

---

## 5. Optimal Solution

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head for the result linked list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop continues as long as there are digits in either list or a carry exists
        while l1 or l2 or carry:
            # Get the value of the current digit from l1 (or 0 if l1 is exhausted)
            val1 = l1.val if l1 else 0
            
            # Get the value of the current digit from l2 (or 0 if l2 is exhausted)
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of current digits and the carry from the previous step
            current_sum = val1 + val2 + carry
            
            # Calculate the new carry for the next step
            carry = current_sum // 10
            
            # Get the digit to be placed in the current result node
            digit = current_sum % 10
            
            # Create a new node with the calculated digit and append it to the result list
            current.next = ListNode(digit)
            
            # Move the current pointer to the newly added node
            current = current.next
            
            # Advance l1 and l2 pointers if they are not None
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # The result list starts from dummy_head.next (dummy_head was just a placeholder)
        return dummy_head.next
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(\max(M, N))$
    *   Where $M$ and $N$ are the lengths of `l1` and `l2` respectively. We iterate through both lists once.
*   **Space Complexity:** $O(\max(M, N))$
    *   To store the new linked list (the sum), which can have at most $\max(M, N) + 1$ nodes.

---

## 7. Follow-up & Extensions

**Q: What if digits are stored in forward order (MSD first)?**
**A:** This is much harder. You would need to:
1.  Reverse both lists.
2.  Add them (as above).
3.  Reverse the result.
OR:
1.  Use two stacks to store digits from both lists.
2.  Pop from stacks, add, handle carry.
3.  Build result list by pre-pending nodes.
