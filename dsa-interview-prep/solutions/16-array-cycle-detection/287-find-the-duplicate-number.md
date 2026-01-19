# 287. Find the Duplicate Number

**Difficulty:** Medium
**Pattern:** Array Cycle Detection (Floyd's Tortoise and Hare) / Binary Search on Answer

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive. There is only **one repeated number** in `nums`, return this repeated number. You must solve the problem **without modifying the array** `nums` and uses only constant extra space.

**Interview Scenario (The "Read-Only Memory" Prompt):**
"You are analyzing a data dump from a read-only hardware register or a constrained memory segment. The data consists of `N+1` pointers (or indices), where each points to a location within the range `1` to `N`. We know there is a loop or a collision (duplicate pointer) in this structure. Due to hardware limitations, you cannot write to the memory (so no sorting or marking visited) and you have extremely limited stack space (no recursion or hash sets). How do you identify the value causing the collision?"

**Why this transformation?**
*   It enforces the **Read-Only** and **Constant Space** constraints, which are the hardest parts of this problem.
*   It hints at the "Linked List Cycle" analogy by mentioning "pointers" and "loops".

---

## 2. Clarifying Questions (Phase 1)

1.  **Multiple Duplicates:** "Can the duplicate number appear more than twice?" (Yes, "one repeated number" means one *value* is repeated, but it could appear 2, 3, or more times).
2.  **Input Range:** "Are all numbers strictly between 1 and n?" (Yes, this is critical because it ensures every value is a valid index).
3.  **Complexity:** "Is $O(N^2)$ acceptable?" (Usually no, target is $O(N)$).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Floyd's Cycle Detection (Tortoise and Hare).

**The Logic:**
Since values are in `[1, n]` and indices are `[0, n]`, we can treat the array as a linked list where `next_node = nums[current_node]`.
*   Index `0` is the starting node (head).
*   Because values are $\ge 1$, index `0` is never pointed to by any element (it's outside the value range). This means we have a specific entry point into the cycle.
*   Because there are `n+1` numbers and values are in `[1, n]`, by Pigeonhole Principle, at least one number points to a previously visited "node". This creates a cycle.
*   The duplicate number is the *entry point* of the cycle.

**Why not Sorting or Hash Set?**
*   Sorting modifies the array ($O(N \log N)$).
*   Hash Set uses $O(N)$ space.
*   The constraints specifically forbid these.

---

## 4. Base Template & Modification

**Standard Cycle Detection Template:**
```python
slow, fast = head, head
while True:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: break # Cycle detected

# Find entry point
slow = head
while slow != fast:
    slow = slow.next
    fast = fast.next
return slow
```

**Modified Logic (Array as Linked List):**
*   `slow.next` becomes `nums[slow]`.
*   `fast.next.next` becomes `nums[nums[fast]]`.
*   Start at index `0` (`nums[0]`).

---

## 5. Optimal Solution

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect Cycle (Tortoise and Hare)
        # We start at index 0. Since values are [1, n], index 0 is never part of the cycle itself,
        # but leads into it.
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]           # Move 1 step
            fast = nums[nums[fast]]     # Move 2 steps
            
        # Phase 2: Find Cycle Entry Point
        # The intersection point is not necessarily the duplicate.
        # Reset slow to start. Keep fast at intersection. Move both 1 step at a time.
        slow = 0 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   Phase 1 (Cycle detection) takes linear time (at most $2N$ steps).
    *   Phase 2 (Entry finding) takes linear time.
*   **Space Complexity:** $O(1)$
    *   Only two pointers (integers) used.

---

## 7. Follow-up & Extensions

**Q: Binary Search approach (Trade-off: $O(N \log N)$ time, $O(1)$ space, Read-Only).**
**A:** We can binary search on the *value range* `[1, n]`.
*   Mid = `n // 2`.
*   Count how many numbers in the array are $\le$ Mid.
*   If `count > Mid`, then by Pigeonhole Principle, the duplicate must be in `[1, Mid]`.
*   Else, duplicate is in `[Mid + 1, n]`.
*   This does NOT modify the array and uses $O(1)$ space. It is slower ($O(N \log N)$) but arguably more intuitive than the cycle finding trick.

**Q: What if we could modify the array?**
**A:** We could swap numbers to their correct positions (index `i` should have value `i+1` or `i`). Or negate values at indices to mark them visited.
