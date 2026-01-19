# DSA Pattern Templates

A collection of patterns, templates, and example problems from practice sessions.

---

## Table of Contents

1. [Interactive Elimination / Guess & Filter](#1-interactive-elimination--guess--filter)
2. [Monotonic Stack](#2-monotonic-stack)
3. [Heap / Priority Queue](#3-heap--priority-queue)
4. [Stack vs Queue vs Heap - When to Use](#4-stack-vs-queue-vs-heap---when-to-use)
5. [Binary Search on Answer](#5-binary-search-on-answer)
6. [Interval Problems / Greedy](#6-interval-problems--greedy)
7. [Game Theory DP (Minimax)](#7-game-theory-dp-minimax)
8. [Greedy Math Patterns](#8-greedy-math-patterns)
9. [Consecutive Count Pattern](#9-consecutive-count-pattern)
10. [Trie for Bit Manipulation](#10-trie-for-bit-manipulation)

---

## 1. Interactive Elimination / Guess & Filter

### Pattern Recognition

Use when you see:
- Hidden answer you need to find
- Limited number of queries/guesses allowed
- Each query returns partial information (feedback)
- Need to eliminate candidates based on feedback

### Template

```python
def interactive_elimination(candidates, api):
    """
    Generic template for guess-and-eliminate problems.

    Args:
        candidates: List of possible answers
        api: Interface that gives feedback on guesses
    """

    def pick_best_guess(candidates):
        """
        Heuristic to pick the most informative guess.
        Goal: maximize elimination regardless of feedback.
        """
        # Option 1: Random (simple but not optimal)
        # return random.choice(candidates)

        # Option 2: Max overlap heuristic (O(n))
        # Pick word with most common characters
        pass

    def matches_feedback(candidate, guess, feedback):
        """Check if candidate is consistent with the feedback."""
        pass

    while candidates:
        # 1. Pick best guess using heuristic
        guess = pick_best_guess(candidates)

        # 2. Query the API
        feedback = api.query(guess)

        # 3. Check if we found the answer
        if is_answer(feedback):
            return guess

        # 4. Filter candidates based on feedback
        candidates = [c for c in candidates
                     if matches_feedback(c, guess, feedback)]

    return None  # Should not reach here if answer exists
```

### Key Insight

```
SCORE (heuristic)  →  Pick which word to guess
FEEDBACK (API)     →  Filter impossible candidates

They are DIFFERENT! Score helps us guess smartly,
feedback helps us eliminate.
```

### Complexity

| Operation | Time |
|-----------|------|
| Pick best guess | O(n) with max-overlap heuristic |
| Filter candidates | O(n) |
| Total iterations | O(k) where k = max allowed guesses |
| **Overall** | **O(k × n) = O(n)** when k is constant |

### Example Problem: LC 843 - Guess the Word

**Problem:** Find a secret 6-letter word with ≤10 guesses. API returns count of exact position matches.

**Google-Style Framing:** "Design a password recovery system that identifies a 6-character code with a rate-limited verification API (10 calls max)."

```python
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        def pair_matches(a: str, b: str) -> int:
            """Count exact position matches between two words."""
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word() -> str:
            """
            Pick word with highest overlap score.
            O(n) using character frequency counting.
            """
            # Count frequency of each char at each position
            counts = [[0] * 26 for _ in range(6)]
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord('a')] += 1

            # Score each word: sum of frequencies of its characters
            best_word = candidates[0]
            best_score = 0
            for word in candidates:
                score = sum(counts[i][ord(c) - ord('a')]
                           for i, c in enumerate(word))
                if score > best_score:
                    best_score = score
                    best_word = word

            return best_word

        candidates = wordlist[:]

        while candidates:
            # Pick smartest guess
            guess = most_overlap_word()

            # Get feedback from API
            matches = master.guess(guess)

            # Found it!
            if matches == 6:
                return

            # Filter: keep only words with same match count
            candidates = [w for w in candidates
                         if pair_matches(guess, w) == matches]
```

### Why Max-Overlap Works

```
counts = frequency of each character at each position (ONE array)
score  = sum of frequencies for a word's characters (PER word)

High score → word shares characters with many others
           → more likely to get non-zero feedback
           → better elimination power
```

### Related Problems

| Problem | Description |
|---------|-------------|
| LC 374 - Guess Number Higher/Lower | Binary search with API |
| LC 375 - Guess Number Higher/Lower II | Minimax strategy |
| LC 489 - Robot Room Cleaner | Interactive exploration |

### Common Mistakes

1. Using O(n²) minimax when O(n) heuristic works
2. Confusing "score" (picking) with "matches" (filtering)
3. Not handling edge case when candidates = 1

---

## 2. Monotonic Stack

### Pattern Recognition

Use when you see:
- "Next greater/smaller element"
- "Previous greater/smaller element"
- "Largest rectangle in histogram"
- "Days until warmer temperature"
- Finding optimal pairs with index constraints (i < j)
- Problems involving "span" or "width" calculations

### Two Types of Monotonic Stacks

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DECREASING STACK                                 │
│                                                                     │
│     Values: [large, ..., small] (top is smallest)                   │
│     PUSH: when current < stack top                                  │
│     POP:  when current >= stack top                                 │
│                                                                     │
│     Use for: Next/Previous GREATER element                          │
│              Maximum width ramp                                     │
├─────────────────────────────────────────────────────────────────────┤
│                    INCREASING STACK                                 │
│                                                                     │
│     Values: [small, ..., large] (top is largest)                    │
│     PUSH: when current > stack top                                  │
│     POP:  when current <= stack top                                 │
│                                                                     │
│     Use for: Next/Previous SMALLER element                          │
│              Largest rectangle in histogram                         │
└─────────────────────────────────────────────────────────────────────┘
```

### Template: Decreasing Stack (Next Greater)

```python
def next_greater_element(nums):
    """
    For each element, find the next greater element to its right.
    Returns: List where result[i] = next greater element, or -1 if none
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Stores indices, values are decreasing

    for i in range(n):
        # Pop all smaller elements - we found their "next greater"
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
```

### Template: Increasing Stack (Next Smaller)

```python
def next_smaller_element(nums):
    """
    For each element, find the next smaller element to its right.
    Returns: List where result[i] = next smaller element, or -1 if none
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Stores indices, values are increasing

    for i in range(n):
        # Pop all larger elements - we found their "next smaller"
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
```

### 🔑 KEY INSIGHT: Why "Opposite" Stack Type?

**WHY does finding GREATER use DECREASING stack? (Seems backwards!)**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Think: "Who is WAITING for what?"                        │
│                                                             │
│   DECREASING stack for Next GREATER:                       │
│   ──────────────────────────────────                       │
│   Stack: [9, 7, 3] (decreasing, top=3 is smallest)         │
│                 ↑                                           │
│   Smallest is on TOP = "most desperate" to find greater    │
│                                                             │
│   When 5 arrives:                                          │
│     • 5 > 3? YES → 3 found its GREATER! Pop 3.            │
│     • 5 > 7? NO → 7 still waiting. Stop.                  │
│   Stack: [9, 7, 5]                                         │
│                                                             │
│   Small elements get "answered" when something BIGGER comes│
│                                                             │
│   ─────────────────────────────────────────────────────    │
│                                                             │
│   INCREASING stack for Next SMALLER:                       │
│   ──────────────────────────────────                       │
│   Stack: [1, 3, 7] (increasing, top=7 is largest)          │
│                 ↑                                           │
│   Largest is on TOP = "most desperate" to find smaller     │
│                                                             │
│   When 5 arrives:                                          │
│     • 5 < 7? YES → 7 found its SMALLER! Pop 7.            │
│     • 5 < 3? NO → 3 still waiting. Stop.                  │
│   Stack: [1, 3, 5]                                         │
│                                                             │
│   Large elements get "answered" when something SMALLER comes│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**The Universal Rule:**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│        WHAT YOU WANT    →    USE THE OPPOSITE              │
│                                                             │
│   Find GREATER  →  DECREASING stack (small waits on top)   │
│   Find SMALLER  →  INCREASING stack (large waits on top)   │
│                                                             │
│   WHY? The "opposite" puts the most "needy" element on top!│
│                                                             │
│   Decreasing: smallest on top → first to find its greater  │
│   Increasing: largest on top → first to find its smaller   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Quick Reference

| Want to Find | Stack Type | Pop Condition | Examples |
|--------------|------------|---------------|----------|
| Next Greater | Decreasing | `stack[-1] < curr` | LC 739, 496, 503 |
| Next Smaller | Increasing | `stack[-1] > curr` | LC 84, 85, 42 |
| Prev Greater | Decreasing | `stack[-1] <= curr` | LC 901 |
| Prev Smaller | Increasing | `stack[-1] >= curr` | LC 962 |

### 🔄 Direction Guide: LEFT→RIGHT vs RIGHT→LEFT

**Two ways to iterate - both work, but think differently:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   LEFT → RIGHT: Stack holds elements BEFORE current                │
│                 "Who is WAITING for their answer?"                 │
│                 When I pop → I'm ANSWERING the popped element      │
│                 result[popped_idx] = current                       │
│                                                                     │
│   RIGHT → LEFT: Stack holds elements AFTER current                 │
│                 "Who can ANSWER my question?"                      │
│                 Stack top = my answer                              │
│                 result[i] = stack_top                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Example: Next Greater for [2, 1, 5, 6, 2, 3]**

```
LEFT → RIGHT (elements wait for answer):
──────────────────────────────────────────
i=0: push 0           stack=[0] (2 waiting)
i=1: push 1           stack=[0,1] (2,1 waiting)
i=2: 5>1? pop, ans[1]=5
     5>2? pop, ans[0]=5
     push 2           stack=[2] (5 waiting)
i=3: 6>5? pop, ans[2]=6
     push 3           stack=[3] (6 waiting)
...
Result: [5, 5, 6, -1, 3, -1]

RIGHT → LEFT (look right for answer):
──────────────────────────────────────────
i=5: push 5           stack=[5], ans[5]=-1
i=4: 3>2? ans[4]=3    stack=[5,4]
i=3: pop 3, pop 2
     push 3           stack=[3], ans[3]=-1
i=2: 6>5? ans[2]=6    stack=[3,2]
i=1: 5>1? ans[1]=5    stack=[3,2,1]
i=0: 5>2? ans[0]=5    stack=[3,2,1,0]
Result: [5, 5, 6, -1, 3, -1] ✓ Same!
```

**Which direction to use?**

| Problem Type | Recommended | Why |
|--------------|-------------|-----|
| NEXT greater/smaller | LEFT → RIGHT | Natural: wait → answer arrives |
| PREVIOUS greater/smaller | LEFT → RIGHT | Stack top = my previous |
| Need BOTH next AND prev | LEFT → RIGHT | Can compute both in one pass |

**Recommendation: Always use LEFT → RIGHT.** It works for all cases!

### Template: All 4 Variants (LEFT → RIGHT)

```python
def all_monotonic_variants(nums):
    """Compute all 4 variants in separate passes."""
    n = len(nums)
    next_greater = [-1] * n
    next_smaller = [-1] * n
    prev_greater = [-1] * n
    prev_smaller = [-1] * n

    # NEXT greater: decreasing stack, pop when curr > top
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            next_greater[stack.pop()] = nums[i]
        stack.append(i)

    # NEXT smaller: increasing stack, pop when curr < top
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            next_smaller[stack.pop()] = nums[i]
        stack.append(i)

    # PREV greater: decreasing stack, top is my answer
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            prev_greater[i] = nums[stack[-1]]
        stack.append(i)

    # PREV smaller: increasing stack, top is my answer
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            prev_smaller[i] = nums[stack[-1]]
        stack.append(i)

    return next_greater, next_smaller, prev_greater, prev_smaller

# Example: nums = [2, 1, 5, 6, 2, 3]
# next_greater: [5, 5, 6, -1, 3, -1]
# next_smaller: [1, -1, 2, 2, -1, -1]
# prev_greater: [-1, 2, -1, -1, 6, 6]
# prev_smaller: [-1, -1, 1, 5, 1, 2]
```

### Key Difference: NEXT vs PREV

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   NEXT (answer is to the RIGHT):                                   │
│   • Stack elements are WAITING                                     │
│   • Pop condition: found their answer                              │
│   • result[popped] = current                                       │
│                                                                     │
│   PREV (answer is to the LEFT):                                    │
│   • Stack elements are CANDIDATES                                  │
│   • Pop condition: remove invalid candidates                       │
│   • result[current] = stack top                                    │
│                                                                     │
│   Notice:                                                          │
│   • NEXT: we SET result when we POP                               │
│   • PREV: we SET result when we CHECK TOP                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Example Problem: LC 962 - Maximum Width Ramp

**Problem:** Find maximum `j - i` where `i < j` and `nums[i] <= nums[j]`.

**Google-Style Framing:** "Find the maximum holding period where you could buy at price X and sell at price Y where Y >= X."

**Approach 1: Monotonic Stack O(n)**

```python
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []  # Decreasing stack of candidate starting indices

        # Step 1: Build decreasing stack (potential starting points)
        # Only keep indices where value is smaller than all previous
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # Step 2: Scan from right, greedily match with stack
        max_width = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)

        return max_width
```

**Why It Works:**
```
Step 1: Decreasing stack keeps only "useful" starting points
  - If nums[k] < nums[i] for k < i, then k is always better than i
  - k gives wider ramp AND smaller starting value

Step 2: Right-to-left finds widest ramp for each start
  - Once we match i with j, any j' < j gives smaller width
  - So we pop i after matching (it's "used up")
```

**Approach 2: Sorting O(n log n)**

```python
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = list(range(n))

        # Sort indices by their values
        indices.sort(key=lambda i: (nums[i], i))

        min_index = n  # Track smallest index seen
        max_width = 0

        # After sorting: all previous indices have values <= current
        for i in indices:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)

        return max_width
```

**Approach 3: Two Pointers with Suffix Max O(n)**

```python
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)

        # suffix_max[i] = max value from index i to end
        suffix_max = [0] * n
        suffix_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])

        # Two pointers
        max_width = 0
        i, j = 0, 0

        while j < n:
            if nums[i] <= suffix_max[j]:
                max_width = max(max_width, j - i)
                j += 1
            else:
                i += 1

        return max_width
```

### Complexity Comparison

| Approach | Time | Space | Best For |
|----------|------|-------|----------|
| Monotonic Stack | O(n) | O(n) | Showing stack mastery |
| Sorting | O(n log n) | O(n) | Easiest to explain |
| Two Pointers | O(n) | O(n) | Showing two-pointer skill |

### Related Problems

| Problem | Description | Stack Type |
|---------|-------------|------------|
| LC 739 - Daily Temperatures | Days until warmer | Decreasing |
| LC 496 - Next Greater Element I | Find next greater | Decreasing |
| LC 503 - Next Greater Element II | Circular array | Decreasing |
| LC 84 - Largest Rectangle in Histogram | Max area | Increasing |
| LC 42 - Trapping Rain Water | Water between bars | Both work |
| LC 901 - Online Stock Span | Consecutive smaller days | Decreasing |

### Common Mistakes

1. Confusing increasing vs decreasing stack
2. Forgetting to store indices (not values) in stack
3. Off-by-one errors when calculating width/span
4. Not handling empty stack case

---

## 3. Heap / Priority Queue

### Pattern Recognition

Use when you see:
- "K-th largest/smallest"
- "Top K frequent elements"
- "Merge K sorted lists/arrays"
- "Find median from data stream"
- "Task scheduling with priorities"
- "Dijkstra's shortest path"

### Python Heap Basics

```python
import heapq

# MIN HEAP (default) - smallest on top
min_heap = []
heapq.heappush(min_heap, 5)    # Add element
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8)
smallest = heapq.heappop(min_heap)  # Returns 2

# MAX HEAP (negate values)
max_heap = []
heapq.heappush(max_heap, -5)   # Negate when pushing
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)
largest = -heapq.heappop(max_heap)  # Returns 8 (negate again)

# HEAPIFY - convert list to heap in O(n)
nums = [5, 2, 8, 1, 9]
heapq.heapify(nums)  # nums is now a min heap

# PEEK without removing
top = min_heap[0]  # O(1)
```

### Heap Operations Complexity

| Operation | Time | Description |
|-----------|------|-------------|
| heappush | O(log n) | Add element, bubble up |
| heappop | O(log n) | Remove top, bubble down |
| heap[0] | O(1) | Peek at top |
| heapify | O(n) | Convert list to heap |

### 🔑 KEY INSIGHT: The "Opposite Gatekeeper" Rule

**WHY does K-th LARGEST use MIN heap? (Seems backwards!)**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Think of it as a "BOUNCER AT A VIP CLUB"                 │
│                                                             │
│   K-th LARGEST → MIN heap of size K                        │
│   ─────────────────────────────────────────                │
│   • VIP club only holds K people (largest ones)            │
│   • Bouncer (heap top) = SMALLEST person in VIP            │
│   • New person BIGGER than bouncer? → Kick bouncer, enter  │
│   • New person SMALLER than bouncer? → Rejected            │
│   • Result: MIN of K largest = K-th largest!               │
│                                                             │
│   K-th SMALLEST → MAX heap of size K                       │
│   ─────────────────────────────────────────                │
│   • VIP club only holds K people (smallest ones)           │
│   • Bouncer (heap top) = LARGEST person in VIP             │
│   • New person SMALLER than bouncer? → Kick bouncer, enter │
│   • New person BIGGER than bouncer? → Rejected             │
│   • Result: MAX of K smallest = K-th smallest!             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Visual Example: Find 3rd Largest from [5, 2, 9, 1, 7, 6]**

```
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

**The Universal Rule:**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│        WHAT YOU WANT    →    USE THE OPPOSITE              │
│                                                             │
│   Keep K LARGEST   →  MIN heap (kicks out smallest)        │
│   Keep K SMALLEST  →  MAX heap (kicks out largest)         │
│                                                             │
│   WHY? The "opposite" gatekeeper PROTECTS what you want!   │
│                                                             │
│   MIN heap top = smallest of K largest = K-th largest      │
│   MAX heap top = largest of K smallest = K-th smallest     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Template: K-th Largest Element

```python
import heapq

def kth_largest(nums: List[int], k: int) -> int:
    """
    Find k-th largest element using min heap of size k.
    The top of heap = k-th largest (k-1 elements are larger).
    """
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest

    return heap[0]  # k-th largest
```

### Template: Top K Frequent Elements

```python
import heapq
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using min heap.
    """
    count = Counter(nums)

    # Min heap of (frequency, element)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]
```

### Template: Merge K Sorted Lists

```python
import heapq

def merge_k_sorted(lists: List[List[int]]) -> List[int]:
    """
    Merge k sorted lists using min heap.
    Heap stores: (value, list_index, element_index)
    """
    heap = []

    # Initialize with first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
```

### Template: Two Heaps (Find Median)

```python
import heapq

class MedianFinder:
    """
    Two heaps: max_heap (left half), min_heap (right half)
    max_heap stores negated values for max behavior
    """

    def __init__(self):
        self.left = []   # Max heap (negated)
        self.right = []  # Min heap

    def addNum(self, num: int) -> None:
        # Add to left (max heap)
        heapq.heappush(self.left, -num)

        # Balance: move largest from left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Keep left same size or 1 larger
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2
```

### Example Problem: LC 215 - Kth Largest Element

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap of size k
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
```

### Related Problems

| Problem | Description | Heap Type |
|---------|-------------|-----------|
| LC 215 - Kth Largest | Find k-th largest | Min heap size k |
| LC 347 - Top K Frequent | K most frequent | Min heap size k |
| LC 23 - Merge K Sorted Lists | Merge lists | Min heap |
| LC 295 - Find Median | Stream median | Two heaps |
| LC 373 - K Pairs Smallest Sums | K smallest pairs | Min heap |
| LC 743 - Network Delay Time | Dijkstra | Min heap |
| LC 621 - Task Scheduler | Schedule tasks | Max heap |

### Common Mistakes

1. Forgetting to negate for max heap
2. Using wrong heap size for "k-th" problems
3. Not handling empty heap edge case
4. Forgetting heapify is O(n), not O(n log n)

---

## 4. Stack vs Queue vs Heap - When to Use

### Data Structure Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA STRUCTURE COMPARISON                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   STACK (LIFO)          QUEUE (FIFO)         HEAP (Priority)       │
│   ┌─────────┐           ┌─────────┐          ┌─────────┐           │
│   │ newest  │ ←pop      │ oldest  │ ←pop     │ min/max │ ←pop      │
│   │   ...   │           │   ...   │          │   ...   │           │
│   │ oldest  │           │ newest  │          │  rest   │           │
│   └─────────┘           └─────────┘          └─────────┘           │
│       ↑                     ↑                    ↑                  │
│      push                  push                 push                │
│                                                                     │
│   Last In First Out     First In First Out   Priority Order        │
│   O(1) operations       O(1) operations      O(log n) operations   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Pattern Selection Guide

```
┌─────────────────────────────────────────────────────────────────────┐
│                    WHEN TO USE WHICH?                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  STACK - Use when:                                                  │
│  ├─ Matching pairs (parentheses, tags)                              │
│  ├─ Undo/redo operations                                            │
│  ├─ DFS traversal                                                   │
│  ├─ Backtracking                                                    │
│  ├─ Next/previous greater/smaller element                           │
│  └─ Expression evaluation                                           │
│                                                                     │
│  QUEUE - Use when:                                                  │
│  ├─ BFS traversal                                                   │
│  ├─ Level-order tree traversal                                      │
│  ├─ Process in arrival order                                        │
│  └─ Sliding window (with deque)                                     │
│                                                                     │
│  HEAP - Use when:                                                   │
│  ├─ K-th largest/smallest                                           │
│  ├─ Top K elements                                                  │
│  ├─ Merge K sorted things                                           │
│  ├─ Continuous stream + need ordering                               │
│  ├─ Dijkstra's algorithm                                            │
│  └─ Task scheduling with priorities                                 │
│                                                                     │
│  MONOTONIC STACK - Use when:                                        │
│  ├─ Next greater/smaller element                                    │
│  ├─ Largest rectangle problems                                      │
│  └─ Stock span, temperature problems                                │
│                                                                     │
│  MONOTONIC DEQUE - Use when:                                        │
│  ├─ Sliding window maximum/minimum                                  │
│  └─ Need to pop from both ends                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Keyword Triggers

| Keyword/Phrase | Data Structure | Example Problem |
|----------------|----------------|-----------------|
| "Valid parentheses" | Stack | LC 20 |
| "Next warmer day" | Monotonic Stack | LC 739 |
| "Largest rectangle" | Monotonic Stack | LC 84 |
| "Level order traversal" | Queue | LC 102 |
| "Shortest path unweighted" | Queue (BFS) | LC 994 |
| "K-th largest" | Heap (min, size k) | LC 215 |
| "Top K frequent" | Heap | LC 347 |
| "Merge K sorted" | Heap | LC 23 |
| "Median from stream" | Two Heaps | LC 295 |
| "Shortest path weighted" | Heap (Dijkstra) | LC 743 |
| "Sliding window max" | Monotonic Deque | LC 239 |
| "All permutations" | Stack (backtrack) | LC 46 |

### Decision Flowchart

```
                        What's the problem about?
                                  │
          ┌───────────────────────┼───────────────────────┐
          ↓                       ↓                       ↓
    Order of processing?    Need priority?         Matching/Nesting?
          │                       │                       │
    ┌─────┴─────┐                 ↓                       ↓
    ↓           ↓               HEAP                    STACK
  LIFO?      FIFO?                │                       │
    │           │           ┌─────┴─────┐           ┌─────┴─────┐
    ↓           ↓           ↓           ↓           ↓           ↓
  STACK      QUEUE      K-th elem?   Merge K?   Monotonic?   Simple?
    │           │           │           │           │           │
    ↓           ↓           ↓           ↓           ↓           ↓
   DFS        BFS       Min heap    Min heap    See next     Valid
Backtrack  Level-order  of size k   of heads     section    parens
```

### Monotonic Stack Decision

```
            Need next/prev greater or smaller?
                          │
              ┌───────────┴───────────┐
              ↓                       ↓
         GREATER                   SMALLER
              │                       │
              ↓                       ↓
      DECREASING STACK        INCREASING STACK
              │                       │
    ┌─────────┴─────────┐   ┌─────────┴─────────┐
    ↓                   ↓   ↓                   ↓
Pop when            Examples   Pop when      Examples
curr > top          LC 739     curr < top    LC 84
                    LC 496                   LC 42
                    LC 901                   LC 85
```

### Summary Table

| Structure | Access Pattern | Insert | Remove | Use Case |
|-----------|---------------|--------|--------|----------|
| Stack | LIFO | O(1) | O(1) | DFS, matching, undo |
| Queue | FIFO | O(1) | O(1) | BFS, level-order |
| Deque | Both ends | O(1) | O(1) | Sliding window |
| Min Heap | Smallest first | O(log n) | O(log n) | K-th, merge K |
| Max Heap | Largest first | O(log n) | O(log n) | Top K, scheduling |
| Mono Stack | Ordered | O(1)* | O(1)* | Next greater/smaller |

*Amortized - each element pushed/popped once

### 🎯 MASTER MEMORY CARD: The "Use Opposite" Rule

```
╔═════════════════════════════════════════════════════════════════════╗
║                                                                     ║
║    🧠 THE "OPPOSITE GATEKEEPER" PRINCIPLE                          ║
║                                                                     ║
║    What you WANT         →    Use the OPPOSITE                     ║
║    ─────────────────────────────────────────────                   ║
║                                                                     ║
║    HEAP:                                                            ║
║    ├─ K-th LARGEST       →    MIN heap size K                      ║
║    │                          (kicks out smallest, keeps largest)  ║
║    │                                                                ║
║    └─ K-th SMALLEST      →    MAX heap size K                      ║
║                               (kicks out largest, keeps smallest)  ║
║                                                                     ║
║    MONOTONIC STACK:                                                 ║
║    ├─ Find next GREATER  →    DECREASING stack                     ║
║    │                          (smallest on top, waiting for bigger)║
║    │                                                                ║
║    └─ Find next SMALLER  →    INCREASING stack                     ║
║                               (largest on top, waiting for smaller)║
║                                                                     ║
╠═════════════════════════════════════════════════════════════════════╣
║                                                                     ║
║    WHY DOES THIS WORK?                                             ║
║                                                                     ║
║    The "opposite" structure creates a GATEKEEPER:                  ║
║                                                                     ║
║    • MIN heap top = smallest of the largest = K-th largest         ║
║    • MAX heap top = largest of the smallest = K-th smallest        ║
║    • Decreasing top = smallest waiting = first to find greater     ║
║    • Increasing top = largest waiting = first to find smaller      ║
║                                                                     ║
╠═════════════════════════════════════════════════════════════════════╣
║                                                                     ║
║    QUICK RECALL:                                                   ║
║                                                                     ║
║    "I want LARGEST → use MIN"    (opposite!)                       ║
║    "I want GREATER → use DECREASING"    (opposite!)                ║
║                                                                     ║
║    The gatekeeper is always the OPPOSITE of what you seek.         ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝
```

---

## 5. Binary Search Templates

### The Two Main Binary Search Templates

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                     BINARY SEARCH TEMPLATE DECISION                        ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   TEMPLATE 1: left <= right (Save Result Pattern)                         ║
║   ─────────────────────────────────────────────────                       ║
║   Use when: Finding LARGEST/SMALLEST value satisfying condition           ║
║             AND you can SKIP mid after checking                           ║
║                                                                           ║
║   while left <= right:                                                    ║
║       mid = (left + right) // 2                                           ║
║       if condition(mid):                                                  ║
║           result = mid         # Save answer                              ║
║           left = mid + 1       # Try for larger (or right = mid - 1)     ║
║       else:                                                               ║
║           right = mid - 1      # (or left = mid + 1)                     ║
║   return result                                                           ║
║                                                                           ║
║   Examples: Longest duplicate substring, largest valid answer             ║
║                                                                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   TEMPLATE 2: left < right (Boundary Finding Pattern)                     ║
║   ─────────────────────────────────────────────────                       ║
║   Use when: Finding exact BOUNDARY where condition changes                ║
║             mid COULD be the answer, CAN'T skip it                        ║
║                                                                           ║
║   while left < right:                                                     ║
║       mid = (left + right) // 2                                           ║
║       if condition(mid):                                                  ║
║           right = mid          # mid could be answer, KEEP it             ║
║       else:                                                               ║
║           left = mid + 1       # mid is wrong, skip it                   ║
║   return left  # left == right, converged to boundary                    ║
║                                                                           ║
║   Examples: First bad version, smallest divisor, search insert position   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### 🔑 KEY INSIGHT: When to Use Which?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   Ask: "Can I SKIP mid after checking it?"                         │
│                                                                     │
│   YES, I can skip mid:                                              │
│   ────────────────────                                              │
│   • Use: left <= right                                             │
│   • Move: left = mid + 1 AND right = mid - 1                       │
│   • Save result when condition is true                             │
│   • Example: "Find longest duplicate" - if length 5 works,         │
│              save it and try 6 (skip 5)                            │
│                                                                     │
│   NO, mid could be the answer:                                      │
│   ─────────────────────────────                                     │
│   • Use: left < right                                              │
│   • Move: right = mid (keep mid!) or left = mid + 1               │
│   • Converge to boundary                                           │
│   • Example: "Find first bad version" - if version 5 is bad,       │
│              it MIGHT be the first bad, can't skip it              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Template 1: Save Result (Finding Maximum Valid)

```python
def find_maximum_valid(lo, hi, condition):
    """
    Find LARGEST value where condition is True.

    Condition pattern: True True True True False False
                                      ↑
                            Want this (largest True)
    """
    result = -1  # Or appropriate default

    while lo <= hi:
        mid = (lo + hi) // 2

        if condition(mid):
            result = mid       # Save! This might be answer
            lo = mid + 1       # But try for LARGER
        else:
            hi = mid - 1       # Too big, go smaller

    return result

# Example: Longest Duplicate Substring
# condition(length) = "does duplicate of this length exist?"
# True for lengths 1,2,3 | False for 4,5,6
# Want: 3 (largest True)
```

### Template 1: Save Result (Finding Minimum Valid)

```python
def find_minimum_valid(lo, hi, condition):
    """
    Find SMALLEST value where condition is True.

    Condition pattern: False False False True True True
                                         ↑
                              Want this (smallest True)
    """
    result = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if condition(mid):
            result = mid       # Save! This might be answer
            hi = mid - 1       # But try for SMALLER
        else:
            lo = mid + 1       # Too small, go larger

    return result
```

### Template 2: Boundary Finding (First True)

```python
def find_first_true(lo, hi, condition):
    """
    Find FIRST position where condition becomes True.

    Condition pattern: False False False True True True
                                         ↑
                              Want this (boundary)
    """
    while lo < hi:
        mid = (lo + hi) // 2

        if condition(mid):
            hi = mid           # mid COULD be first True, KEEP it
        else:
            lo = mid + 1       # mid is False, skip it

    return lo  # lo == hi, converged to boundary
```

### Template 2: Boundary Finding (Last True)

```python
def find_last_true(lo, hi, condition):
    """
    Find LAST position where condition is True.

    Condition pattern: True True True False False False
                                  ↑
                       Want this (last True)
    """
    while lo < hi:
        mid = (lo + hi + 1) // 2  # ⚠️ Round UP to avoid infinite loop!

        if condition(mid):
            lo = mid           # mid COULD be last True, KEEP it
        else:
            hi = mid - 1       # mid is False, skip it

    return lo  # lo == hi, converged to boundary

# ⚠️ WHY +1? Prevents infinite loop!
# If lo=4, hi=5, mid=(4+5)//2=4
# If condition(4) is True, lo=4 (stuck!)
# With +1: mid=(4+5+1)//2=5, progress guaranteed
```

### Visual Comparison

```
Finding LARGEST where condition is True:

Condition:  T    T    T    T    F    F    F
Index:      1    2    3    4    5    6    7
                      ↑
                   Answer = 4

TEMPLATE 1 (left <= right):
─────────────────────────────
lo=1, hi=7, mid=4: T → result=4, lo=5
lo=5, hi=7, mid=6: F → hi=5
lo=5, hi=5, mid=5: F → hi=4
lo=5 > hi=4 → STOP, return result=4 ✓

TEMPLATE 2 (left < right) with round-up:
─────────────────────────────────────────
lo=1, hi=7, mid=4: T → lo=4
lo=4, hi=7, mid=6: F → hi=5
lo=4, hi=5, mid=5: F → hi=4
lo=4 == hi=4 → STOP, return 4 ✓
```

### Quick Reference Table

| Goal | Template | Loop | Mid Calculation | When True | When False |
|------|----------|------|-----------------|-----------|------------|
| Largest valid | 1 | `<=` | `(lo+hi)//2` | `result=mid; lo=mid+1` | `hi=mid-1` |
| Smallest valid | 1 | `<=` | `(lo+hi)//2` | `result=mid; hi=mid-1` | `lo=mid+1` |
| First True | 2 | `<` | `(lo+hi)//2` | `hi=mid` | `lo=mid+1` |
| Last True | 2 | `<` | `(lo+hi+1)//2` | `lo=mid` | `hi=mid-1` |

### Common Mistakes

```
┌─────────────────────────────────────────────────────────────────────┐
│ MISTAKE 1: Using wrong template                                     │
│ ─────────────────────────────────                                   │
│ Template 2 with left <= right → infinite loop or skip answer        │
│ Template 1 with left < right → might not check all values           │
│                                                                     │
│ MISTAKE 2: Forgetting +1 for "last True"                           │
│ ──────────────────────────────────────────                          │
│ mid = (lo + hi) // 2 with lo = mid → infinite loop when hi = lo+1  │
│                                                                     │
│ MISTAKE 3: Wrong direction after condition                          │
│ ──────────────────────────────────────────                          │
│ Finding MAX but doing hi = mid - 1 when True → wrong!              │
│ Finding MIN but doing lo = mid + 1 when True → wrong!              │
└─────────────────────────────────────────────────────────────────────┘
```

### Practical Examples: Same Problem, Different Templates

**Problem: Longest Duplicate Substring (LC 1044)**

```python
# TEMPLATE 1: Save Result (Recommended for this problem)
def longestDupSubstring(s):
    def has_dup(length):
        seen = set()
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub in seen:
                return sub
            seen.add(sub)
        return ""

    result = ""
    left, right = 1, len(s) - 1

    while left <= right:              # Template 1
        mid = (left + right) // 2
        dup = has_dup(mid)
        if dup:
            result = dup              # Save result
            left = mid + 1            # Try longer
        else:
            right = mid - 1           # Try shorter

    return result
```

**Problem: First Bad Version (LC 278)**

```python
# TEMPLATE 2: Boundary Finding (Recommended for this problem)
def firstBadVersion(n):
    left, right = 1, n

    while left < right:               # Template 2
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid               # mid COULD be first bad, keep it
        else:
            left = mid + 1            # mid is good, skip it

    return left  # Converged to boundary
```

**Problem: Search Insert Position (LC 35)**

```python
# TEMPLATE 2: Find where target should be inserted
def searchInsert(nums, target):
    left, right = 0, len(nums)

    while left < right:               # Template 2
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid               # mid could be insert position
        else:
            left = mid + 1

    return left
```

---

### Binary Search on Answer

### Pattern Recognition

Use when you see:
- "Find minimum/maximum value that satisfies condition"
- "Smallest divisor", "Maximum distance", "Minimum capacity"
- The answer is a NUMBER in a RANGE, not an element in array
- You can CHECK if a value works in O(n) or O(n log n)
- **MONOTONIC relationship**: If condition is true for X, it's true for all values in one direction

### Template: Find MINIMUM Valid Answer

```python
def binary_search_min_answer(lo, hi, is_valid):
    """
    Find smallest x in [lo, hi] where is_valid(x) is True.
    Assumes: is_valid(x) = False for x < answer, True for x >= answer
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if is_valid(mid):
            hi = mid      # mid works, try smaller
        else:
            lo = mid + 1  # mid fails, need larger
    return lo
```

### Template: Find MAXIMUM Valid Answer

```python
def binary_search_max_answer(lo, hi, is_valid):
    """
    Find largest x in [lo, hi] where is_valid(x) is True.
    Assumes: is_valid(x) = True for x <= answer, False for x > answer
    """
    while lo < hi:
        mid = (lo + hi + 1) // 2  # +1 to avoid infinite loop!
        if is_valid(mid):
            lo = mid      # mid works, try larger
        else:
            hi = mid - 1  # mid fails, need smaller
    return lo
```

### 🔑 KEY INSIGHT: Why `lo = mid + 1` but `hi = mid`?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   When INVALID (lo = mid + 1):                                     │
│   ─────────────────────────────                                    │
│   • mid is DEFINITELY WRONG - we KNOW it's not the answer         │
│   • Safe to SKIP it entirely: lo = mid + 1                        │
│                                                                     │
│   When VALID (hi = mid):                                           │
│   ───────────────────────                                          │
│   • mid MIGHT BE the answer! (smallest valid we've seen)          │
│   • We CAN'T skip it - must KEEP it in range: hi = mid            │
│   • If we used hi = mid - 1, we might skip the actual answer!     │
│                                                                     │
│   THE GUARANTEE:                                                   │
│   ─────────────────                                                │
│   • Loop continues while lo < hi                                  │
│   • Stops when lo == hi (they converge to same point)             │
│   • hi only moves to VALID positions                              │
│   • lo keeps pushing forward, skipping invalid ones               │
│   • They MEET at the boundary = smallest valid answer!            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 🔑 Visual Example: Why This Works

```
Search space: [1, 9], looking for smallest divisor where sum <= threshold

divisor:  1    2    3    4    5    6    7    8    9
valid?    ❌   ❌   ❌   ❌   ✅   ✅   ✅   ✅   ✅
                          ^
                    SMALLEST valid = answer!

Step 1: lo=1, hi=9, mid=5
        valid(5)? YES → hi = 5   (keep 5, might be answer)
        [lo=1, hi=5]

Step 2: lo=1, hi=5, mid=3
        valid(3)? NO → lo = 4    (skip 3, definitely wrong)
        [lo=4, hi=5]

Step 3: lo=4, hi=5, mid=4
        valid(4)? NO → lo = 5    (skip 4)
        [lo=5, hi=5]

STOP! lo == hi == 5 → Answer is 5
```

### 🔑 KEY INSIGHT: MIN vs MAX Templates

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   Finding MINIMUM valid:                                            │
│   • mid = (lo + hi) // 2                                           │
│   • if valid: hi = mid         (keep mid, search LEFT)             │
│   • else: lo = mid + 1         (skip mid, go RIGHT)                │
│                                                                     │
│   Finding MAXIMUM valid:                                            │
│   • mid = (lo + hi + 1) // 2   ← +1 to round UP!                   │
│   • if valid: lo = mid         (keep mid, search RIGHT)            │
│   • else: hi = mid - 1         (skip mid, go LEFT)                 │
│                                                                     │
│   WHY +1 for MAX? Prevents infinite loop when lo + 1 == hi         │
│   Example: lo=4, hi=5 → mid=(4+5)//2=4 → if valid, lo=4 (stuck!)   │
│            With +1: mid=(4+5+1)//2=5 → if valid, lo=5 (progress!)  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### The Golden Rule Table

| Situation | Action | Why |
|-----------|--------|-----|
| `mid` is DEFINITELY wrong | `lo = mid + 1` or `hi = mid - 1` | Skip it |
| `mid` MIGHT be the answer | `hi = mid` or `lo = mid` | Keep it in range |

### Example Problem: LC 1283 - Smallest Divisor Given Threshold

**Problem:** Find smallest divisor d such that sum(ceil(nums[i]/d)) ≤ threshold

```python
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_valid(divisor):
            total = sum((num + divisor - 1) // divisor for num in nums)
            return total <= threshold

        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if is_valid(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

### Example Problem: LC 1552 - Magnetic Force Between Two Balls

**Problem:** Find MAXIMUM minimum distance to place m balls

```python
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(min_dist):
            count, last = 1, position[0]
            for p in position[1:]:
                if p - last >= min_dist:
                    count += 1
                    last = p
            return count >= m

        lo, hi = 1, position[-1] - position[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2  # +1 because finding MAX
            if can_place(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

### Related Problems

| Problem | Type | is_valid() Check |
|---------|------|------------------|
| LC 1283 - Smallest Divisor | MIN | sum of ceils ≤ threshold |
| LC 1552 - Magnetic Force | MAX | can place m balls |
| LC 875 - Koko Eating Bananas | MIN | can finish in h hours |
| LC 1011 - Ship Packages | MIN | can ship in d days |
| LC 410 - Split Array Largest Sum | MIN | can split into m parts |
| LC 475 - Heaters | MIN | all houses covered |
| LC 774 - Minimize Max Distance | MIN | max gap ≤ mid |

---

## 6. Interval Problems / Greedy

### Pattern Recognition

Use when you see:
- "Minimum arrows/points to cover intervals"
- "Maximum non-overlapping intervals"
- "Merge intervals"
- Array of [start, end] pairs

### Template: Minimum Points to Cover (Sort by END)

```python
def min_points_to_cover(intervals):
    """Minimum points to hit all intervals. Sort by END."""
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float('-inf')

    for start, finish in intervals:
        if start > end:  # Current point doesn't cover this
            count += 1
            end = finish  # Place new point at interval end

    return count
```

### Template: Maximum Non-Overlapping (Sort by END)

```python
def max_non_overlapping(intervals):
    """Maximum intervals that don't overlap. Sort by END."""
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float('-inf')

    for start, finish in intervals:
        if start >= end:  # No overlap
            count += 1
            end = finish

    return count
```

### Template: Merge Overlapping (Sort by START)

```python
def merge_intervals(intervals):
    """Merge overlapping intervals. Sort by START."""
    intervals.sort(key=lambda x: x[0])
    merged = []

    for start, finish in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], finish)
        else:
            merged.append([start, finish])

    return merged
```

### 🔑 KEY INSIGHT: When to Sort by What?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   Sort by END when:                                                 │
│   • Finding minimum points/arrows to cover all                     │
│   • Finding maximum non-overlapping intervals                      │
│   • Greedy "finish earliest first" strategy                        │
│                                                                     │
│   Sort by START when:                                               │
│   • Merging overlapping intervals                                  │
│   • Processing intervals in order                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Example Problem: LC 452 - Minimum Arrows to Burst Balloons

```python
class Solution:
    def findMinArrowPoints(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])  # Sort by END
        arrows = 0
        end = float('-inf')

        for start, finish in points:
            if start > end:
                arrows += 1
                end = finish

        return arrows
```

### Related Problems

| Problem | Pattern | Sort By |
|---------|---------|---------|
| LC 452 - Minimum Arrows | Min points to cover | END |
| LC 435 - Non-overlapping Intervals | Max non-overlapping | END |
| LC 56 - Merge Intervals | Merge overlapping | START |
| LC 57 - Insert Interval | Insert + Merge | START |
| LC 253 - Meeting Rooms II | Min rooms needed | START (+ heap) |
| LC 846 - Hand of Straights | Form consecutive groups | Value |

---

## 7. Game Theory DP (Minimax)

### Pattern Recognition

Use when you see:
- "Two players take turns"
- "Optimal play", "Both play optimally"
- "Can player 1 win?", "Predict the winner"
- Players pick from ends of array

### Template: Minimax DP

```python
def minimax_game(nums):
    """
    Two players pick from either end, both play optimally.
    Returns True if player 1 can win or tie.

    dp[i][j] = (player1 score - player2 score) for subarray [i,j]
               when it's current player's turn
    """
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # Base case: single element
    for i in range(n):
        dp[i][i] = nums[i]

    # Fill for increasing lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Current player picks left or right
            pick_left = nums[i] - dp[i+1][j]
            pick_right = nums[j] - dp[i][j-1]
            dp[i][j] = max(pick_left, pick_right)

    return dp[0][n-1] >= 0
```

### 🔑 KEY INSIGHT: Why Subtract?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   dp[i][j] = MY_SCORE - OPPONENT_SCORE for range [i,j]             │
│                                                                     │
│   If I pick nums[i]:                                                │
│   • I gain nums[i]                                                 │
│   • Opponent plays optimally on [i+1, j]                           │
│   • Opponent's "advantage" becomes MY disadvantage                 │
│   • So: nums[i] - dp[i+1][j]                                       │
│                                                                     │
│   Why subtract? Because dp[i+1][j] is from OPPONENT's view!        │
│   Their positive = my negative.                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Example Problem: LC 486 - Predict the Winner

```python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i+1][j],
                               nums[j] - dp[i][j-1])

        return dp[0][n-1] >= 0
```

### Related Problems

| Problem | Variant |
|---------|---------|
| LC 486 - Predict the Winner | Basic minimax |
| LC 877 - Stone Game | Alice always wins (math) |
| LC 1140 - Stone Game II | Variable pile picks |
| LC 1406 - Stone Game III | Pick 1, 2, or 3 |
| LC 464 - Can I Win | Bitmask DP |

---

## 8. Greedy Math Patterns

### Pattern: Broken Calculator (Work Backwards)

```python
# LC 991 - Broken Calculator
# Can multiply by 2 or subtract 1. Get from start to target.
def min_ops_broken_calc(start, target):
    ops = 0
    while target > start:
        if target % 2 == 1:
            target += 1  # Reverse of subtract
        else:
            target //= 2  # Reverse of multiply
        ops += 1
    return ops + (start - target)  # Remaining subtractions
```

### Pattern: Patching Array (Greedy Range Extension)

```python
# LC 330 - Patching Array
# Add minimum numbers to cover [1, n]
def min_patches(nums, n):
    patches = 0
    covered = 0  # Can make all sums in [0, covered]
    i = 0

    while covered < n:
        if i < len(nums) and nums[i] <= covered + 1:
            covered += nums[i]
            i += 1
        else:
            # Add covered + 1 to extend range
            covered += covered + 1
            patches += 1

    return patches
```

### Pattern: Integer Break (Use 3s)

```python
# LC 343 - Integer Break
# Split n into sum, maximize product
def integer_break(n):
    if n <= 3:
        return n - 1

    if n % 3 == 0:
        return 3 ** (n // 3)
    elif n % 3 == 1:
        return 3 ** (n // 3 - 1) * 4
    else:
        return 3 ** (n // 3) * 2
```

---

## 9. Consecutive Count Pattern

### Pattern Recognition

Use when you see:
- "Count subarrays of consecutive X"
- "Number of subarrays with property"
- The formula n*(n+1)/2 for n consecutive elements

### Template

```python
def count_consecutive_subarrays(arr, target):
    """
    Count all subarrays containing only target value.
    n consecutive targets = n + (n-1) + ... + 1 = n*(n+1)/2 subarrays
    """
    total = 0
    streak = 0

    for val in arr:
        if val == target:
            streak += 1
            total += streak  # Adds 1, then 2, then 3, ...
        else:
            streak = 0

    return total
```

### Example Problem: LC 2348 - Zero-Filled Subarrays

```python
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = streak = 0
        for num in nums:
            if num == 0:
                streak += 1
                total += streak
            else:
                streak = 0
        return total
```

### Why It Works

```
Zeros: [0, 0, 0]

Subarrays:
  [0]           - 1 subarray ending at index 0
  [0], [0,0]    - 2 subarrays ending at index 1
  [0], [0,0], [0,0,0] - 3 subarrays ending at index 2

Total = 1 + 2 + 3 = 6 = 3*4/2
```

---

## 10. Trie for Bit Manipulation

### Pattern Recognition

Use when you see:
- "Maximum XOR of two numbers"
- "Count pairs with XOR property"
- Need to optimize bit-by-bit decisions

### Template: Bit Trie

```python
class BitTrie:
    def __init__(self, max_bits=31):
        self.root = {}
        self.max_bits = max_bits

    def insert(self, num):
        node = self.root
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def find_max_xor(self, num):
        """Find number in trie that gives max XOR with num."""
        node = self.root
        result = 0
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit  # Want opposite for max XOR
            if want in node:
                result |= (1 << i)
                node = node[want]
            elif bit in node:
                node = node[bit]
            else:
                break
        return result
```

### Example Problem: LC 421 - Maximum XOR

```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}

        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        max_xor = 0
        for num in nums:
            node = root
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                want = 1 - bit
                if want in node:
                    curr_xor |= (1 << i)
                    node = node[want]
                else:
                    node = node[bit]
            max_xor = max(max_xor, curr_xor)

        return max_xor
```

---
