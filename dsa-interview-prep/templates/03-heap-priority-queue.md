# Heap / Priority Queue

## Introduction

A Heap (Priority Queue) is a tree-based data structure that efficiently maintains the minimum or maximum element. Python's `heapq` module provides a **min heap** by default. The key insight is that heaps provide O(log n) insertion and O(log n) extraction of the min/max element.

## Pattern Recognition

Use this pattern when you see:
- "K-th largest/smallest element"
- "Top K elements"
- "Merge K sorted lists/arrays"
- "Find median from data stream"
- "Task scheduling with priorities"
- "Dijkstra's shortest path"
- "Continuous stream" + need to track min/max

---

## Python Heap Basics

```python
import heapq

# MIN HEAP (default) - smallest on top
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8)
smallest = heapq.heappop(min_heap)  # Returns 2

# MAX HEAP (negate values)
max_heap = []
heapq.heappush(max_heap, -5)   # Negate when pushing
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)
largest = -heapq.heappop(max_heap)  # Returns 8

# HEAPIFY - convert list to heap in O(n)
nums = [5, 2, 8, 1, 9]
heapq.heapify(nums)  # nums is now a min heap

# PEEK without removing
top = min_heap[0]  # O(1)

# Push and pop in one operation
result = heapq.heappushpop(heap, val)  # Push then pop
result = heapq.heapreplace(heap, val)  # Pop then push
```

### Complexity

| Operation | Time |
|-----------|------|
| heappush | O(log n) |
| heappop | O(log n) |
| heap[0] (peek) | O(1) |
| heapify | O(n) |

---

## Base Templates

### Template 1: K-th Largest Element (Min Heap of size K)

```python
import heapq

def kth_largest(nums, k):
    """
    Find k-th largest using min heap of size k.

    Key insight: Maintain k largest elements.
    The SMALLEST of k largest = k-th largest!
    """
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest

    return heap[0]  # k-th largest
```

### Template 2: K-th Smallest Element (Max Heap of size K)

```python
def kth_smallest(nums, k):
    """
    Find k-th smallest using max heap of size k.
    Negate values to simulate max heap.
    """
    heap = []

    for num in nums:
        heapq.heappush(heap, -num)  # Negate for max heap
        if len(heap) > k:
            heapq.heappop(heap)

    return -heap[0]  # k-th smallest
```

### Template 3: Merge K Sorted Lists

```python
def merge_k_sorted(lists):
    """
    Merge k sorted lists using min heap.
    Heap stores: (value, list_index, element_index)
    """
    heap = []
    result = []

    # Initialize with first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Push next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
```

### Template 4: Two Heaps (Find Median)

```python
class MedianFinder:
    """
    Two heaps: max_heap (left half), min_heap (right half)
    max_heap uses negated values.

    Invariant: len(left) == len(right) or len(left) == len(right) + 1
    """
    def __init__(self):
        self.left = []   # Max heap (negated)
        self.right = []  # Min heap

    def addNum(self, num):
        # Add to left (max heap)
        heapq.heappush(self.left, -num)

        # Balance: move largest from left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Keep left same size or 1 larger
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2
```

---

## Key Insights

### The "Opposite Gatekeeper" Rule

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   Think of it as a "BOUNCER AT A VIP CLUB"                         │
│                                                                     │
│   K-th LARGEST → MIN heap of size K                                │
│   ─────────────────────────────────────────                        │
│   • VIP club holds K people (largest ones)                         │
│   • Bouncer (heap top) = SMALLEST person in VIP                    │
│   • New person BIGGER than bouncer? → Kick bouncer, enter          │
│   • New person SMALLER than bouncer? → Rejected                    │
│   • Result: MIN of K largest = K-th largest!                       │
│                                                                     │
│   K-th SMALLEST → MAX heap of size K                               │
│   ─────────────────────────────────────────                        │
│   • VIP club holds K people (smallest ones)                        │
│   • Bouncer (heap top) = LARGEST person in VIP                     │
│   • New person SMALLER than bouncer? → Kick bouncer, enter         │
│   • New person BIGGER than bouncer? → Rejected                     │
│   • Result: MAX of K smallest = K-th smallest!                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Visual Example: Find 3rd Largest

```
nums = [5, 2, 9, 1, 7, 6], k = 3

MIN heap (size 3) - "Club for 3 largest"

Process 5:  heap = [5]
Process 2:  heap = [2, 5]
Process 9:  heap = [2, 5, 9]     ← Full! Bouncer = 2
Process 1:  1 < 2? REJECTED
Process 7:  7 > 2? KICK 2, ADD 7 → heap = [5, 7, 9], Bouncer = 5
Process 6:  6 > 5? KICK 5, ADD 6 → heap = [6, 7, 9], Bouncer = 6

Answer: heap[0] = 6 (3rd largest!) ✓

Sorted: [1, 2, 5, 6, 7, 9]
                   ↑
              3rd largest
```

### Quick Reference

| Goal | Heap Type | Size | Answer |
|------|-----------|------|--------|
| K-th largest | Min heap | K | heap[0] |
| K-th smallest | Max heap (negated) | K | -heap[0] |
| Top K largest | Min heap | K | All elements |
| Top K smallest | Max heap | K | All elements (negated) |

---

## LeetCode Problems

### Problem 1: LC 215 - Kth Largest Element in an Array

**Link:** [https://leetcode.com/problems/kth-largest-element-in-an-array/](https://leetcode.com/problems/kth-largest-element-in-an-array/)

**Problem:** Find the k-th largest element in an unsorted array.

**Pattern:** Min heap of size K

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
```

**Alternative: Quickselect O(n) average**

```python
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k  # k-th largest = (n-k)-th smallest

        def quickselect(left, right):
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            # Move pivot to end
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            # Partition
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1

            nums[store_idx], nums[right] = nums[right], nums[store_idx]

            if store_idx == target:
                return nums[store_idx]
            elif store_idx < target:
                return quickselect(store_idx + 1, right)
            else:
                return quickselect(left, store_idx - 1)

        return quickselect(0, len(nums) - 1)
```

**Complexity:** Heap: O(n log k), Quickselect: O(n) average

---

### Problem 2: LC 347 - Top K Frequent Elements

**Link:** [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

**Problem:** Return the k most frequent elements.

**Pattern:** Min heap of size K (by frequency)

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []  # (frequency, element)

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
```

**Alternative: Bucket Sort O(n)**

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # Bucket by frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # Collect top k from highest frequency
        result = []
        for freq in range(len(buckets) - 1, -1, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
```

**Complexity:** Heap: O(n log k), Bucket: O(n)

---

### Problem 3: LC 23 - Merge K Sorted Lists

**Link:** [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-k-sorted-lists/)

**Problem:** Merge k sorted linked lists into one sorted list.

**Pattern:** Min heap with (value, index, node)

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Initialize with head of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
```

**Complexity:** O(n log k) where n = total nodes

---

### Problem 4: LC 295 - Find Median from Data Stream

**Link:** [https://leetcode.com/problems/find-median-from-data-stream/](https://leetcode.com/problems/find-median-from-data-stream/)

**Problem:** Design a data structure that supports adding integers and finding median.

**Pattern:** Two Heaps (max left, min right)

```python
class MedianFinder:
    def __init__(self):
        self.left = []   # Max heap (negated) - smaller half
        self.right = []  # Min heap - larger half

    def addNum(self, num: int) -> None:
        # Always add to left first
        heapq.heappush(self.left, -num)

        # Move largest from left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Balance: left should be >= right in size
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2
```

**Complexity:** addNum: O(log n), findMedian: O(1)

---

### Problem 5: LC 373 - Find K Pairs with Smallest Sums

**Link:** [https://leetcode.com/problems/find-k-pairs-with-smallest-sums/](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

**Problem:** Given two sorted arrays, find k pairs with smallest sums.

**Pattern:** Min heap with lazy expansion

**Key Insight:** Don't generate all pairs. Start with (0,0), expand neighbors.

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = [(nums1[0] + nums2[0], 0, 0)]  # (sum, i, j)
        seen = {(0, 0)}
        result = []

        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            # Add neighbors
            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                seen.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                seen.add((i, j + 1))

        return result
```

**Complexity:** O(k log k)

---

### Problem 6: LC 621 - Task Scheduler

**Link:** [https://leetcode.com/problems/task-scheduler/](https://leetcode.com/problems/task-scheduler/)

**Problem:** Schedule tasks with cooling period n. Find minimum time.

**Pattern:** Max heap + greedy

**Key Insight:** Always process the most frequent task first to minimize idle time.

```python
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = []  # (available_time, count)

        while max_heap or cooldown:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # Execute one task
                if cnt < 0:
                    cooldown.append((time + n, cnt))

            # Check if any task is ready
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(max_heap, cooldown.pop(0)[1])

        return time
```

**Alternative: Math formula**

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_freq = max(count.values())
        max_count = sum(1 for freq in count.values() if freq == max_freq)

        # (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
```

**Complexity:** O(n) for math, O(n log 26) for heap

---

### Problem 7: LC 743 - Network Delay Time (Dijkstra)

**Link:** [https://leetcode.com/problems/network-delay-time/](https://leetcode.com/problems/network-delay-time/)

**Problem:** Find time for signal to reach all nodes from source.

**Pattern:** Dijkstra's algorithm with min heap

```python
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Dijkstra's algorithm
        dist = {k: 0}
        heap = [(0, k)]  # (distance, node)

        while heap:
            d, node = heapq.heappop(heap)

            if d > dist.get(node, float('inf')):
                continue

            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist.get(neighbor, float('inf')):
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        if len(dist) < n:
            return -1

        return max(dist.values())
```

**Complexity:** O(E log V)

---

### Problem 8: LC 1046 - Last Stone Weight

**Link:** [https://leetcode.com/problems/last-stone-weight/](https://leetcode.com/problems/last-stone-weight/)

**Problem:** Smash two heaviest stones. Return weight of last stone.

**Pattern:** Max heap (simulation)

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max heap (negate values)
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0
```

**Complexity:** O(n log n)

---

### Problem 9: LC 703 - Kth Largest Element in a Stream

**Link:** [https://leetcode.com/problems/kth-largest-element-in-a-stream/](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

**Problem:** Design a class to find k-th largest in a stream.

**Pattern:** Min heap of size K (maintained across adds)

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
```

**Complexity:** add: O(log k)

---

## Common Mistakes

1. **Forgetting to negate for max heap**
   - Python only has min heap
   - Must negate when pushing AND when reading

2. **Wrong heap size for K-th problems**
   - K-th largest → heap size K
   - If heap grows beyond K, pop

3. **Not handling empty heap**
   - Check `if heap:` before `heap[0]`

4. **Heapify is O(n), not O(n log n)**
   - Use heapify when starting with a list
   - Don't push elements one by one

5. **Comparing incomparable objects**
   - If using tuples, ensure first element breaks ties
   - Use (priority, index, object) pattern

---

## Practice Checklist

- [ ] LC 215 - Kth Largest Element (Basic)
- [ ] LC 347 - Top K Frequent Elements (Frequency counting)
- [ ] LC 23 - Merge K Sorted Lists (Classic)
- [ ] LC 295 - Find Median from Data Stream (Two heaps)
- [ ] LC 373 - K Pairs with Smallest Sums (Lazy expansion)
- [ ] LC 621 - Task Scheduler (Greedy + cooldown)
- [ ] LC 743 - Network Delay Time (Dijkstra)
- [ ] LC 1046 - Last Stone Weight (Simulation)
- [ ] LC 703 - Kth Largest in Stream (Streaming)
- [ ] LC 378 - Kth Smallest Element in Sorted Matrix
