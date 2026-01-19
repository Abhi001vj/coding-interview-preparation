# 23. Merge k Sorted Lists

**Difficulty:** Hard
**Pattern:** Heap (Priority Queue) / Divide & Conquer

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** You are given an array of `k` linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

**Interview Scenario (The "Log Merge" Prompt):**
"You have `k` servers, and each server produces a log file where log entries are sorted by timestamp. You want to merge these `k` log files into a single master log file, also sorted by timestamp. The total number of log entries is huge ($N$), but `k` (number of servers) is relatively small. How do you do this efficiently?"

**Why this transformation?**
*   It moves context from "Linked Lists" (memory structure) to "Streams" (Iterators), which is more realistic for systems design.
*   It highlights that you can only see the "head" (current timestamp) of each stream at any moment.

---

## 2. Clarifying Questions (Phase 1)

1.  **Input Format:** "Are the lists valid? Can any be empty?" (Yes, handle empty lists).
2.  **Constraints:** "What is the relationship between $N$ (total nodes) and $K$ (number of lists)?" (Usually $K \ll N$).
3.  **Space:** "Can I allocate new nodes or should I reuse existing ones?" (Reuse is better/standard for Linked List problems).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Min-Heap (Priority Queue).

**Why not simple concatenation + sort?**
Collecting all $N$ nodes and sorting takes $O(N \log N)$. We can do better because the sub-lists are *already sorted*.

**The Logic:**
At any point, the next smallest element in the final result MUST be one of the `k` heads of the current lists.
1.  Put the head of every non-empty list into a Min-Heap.
2.  Extract the minimum element (smallest head) -> add to result.
3.  If the extracted node has a `next`, push that `next` node into the Heap.
4.  Repeat until Heap is empty.

**Complexity Intuition:**
*   Heap size is at most $K$.
*   Insertion/Deletion takes $O(\log K)$.
*   We do this for every node ($N$ times).
*   Total: $O(N \log K)$. Since $K \le N$, this is faster than $O(N \log N)$.

---

## 4. Base Template & Modification

**Standard Heap Template:**
```python
heap = []
heapq.heappush(heap, val)
while heap:
    val = heapq.heappop(heap)
    # process val
```

**Modified Logic (Handling Linked List Nodes):**
Python's `heapq` compares elements directly. If we push `ListNode` objects, Python will try to compare them. If two nodes have the same value, it will try to compare the `next` attribute, which might fail or be invalid.
*   **Fix:** Store tuples `(val, i, node)` in the heap. `val` is primary key. `i` (unique index) breaks ties so `node` is never compared.

---

## 5. Optimal Solution

```python
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # 1. Initialize Heap with the head of each list
        # We store (val, unique_id, node) to avoid comparison issues
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
                
        dummy = ListNode(0)
        current = dummy
        
        # 2. Process the Heap
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Append to result
            current.next = node
            current = current.next
            
            # If there is a next node in this list, push it
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N \log K)$
    *   $N$ is total number of nodes. $K$ is number of linked lists.
    *   Heap operations take $O(\log K)$.
*   **Space Complexity:** $O(K)$
    *   The heap stores at most $K$ elements.

---

## 7. Follow-up & Extensions

**Q: Can you do this with Divide and Conquer (Merge Sort)?**
**A:** Yes. Pair up lists and merge them (like a tournament bracket).
*   Round 1: Merge pairs $(0,1), (2,3), \dots$ -> $K/2$ lists.
*   Round 2: Merge new pairs -> $K/4$ lists.
*   Complexity is also $O(N \log K)$. It avoids the heap overhead but uses stack space for recursion (or can be iterative).
*   Ideally, mention both. Heap is often preferred for "Streaming" data where all data isn't available upfront. D&C is great for fixed lists.
