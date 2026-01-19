# 12 Essential Algorithm Patterns

## Quick Reference

| Pattern | When to Use | Key Data Structure | Time |
|---------|-------------|-------------------|------|
| Sliding Window | Contiguous subarray/substring | Two pointers + HashMap | O(n) |
| Two Pointers | Sorted array, pairs | Two indices | O(n) |
| Fast & Slow Pointers | Cycle detection, middle | Two pointers | O(n) |
| Merge Intervals | Overlapping intervals | Sorting | O(n log n) |
| Cyclic Sort | Numbers in range [1,n] | In-place swaps | O(n) |
| In-place Linked List Reversal | Reverse portions | Prev/Curr/Next | O(n) |
| Tree BFS | Level-order operations | Queue | O(n) |
| Tree DFS | Path problems, traversals | Recursion/Stack | O(n) |
| Two Heaps | Median, scheduling | Min + Max Heap | O(log n) |
| Subsets/Backtracking | All combinations | Recursion | O(2^n) |
| Binary Search | Sorted data, answer search | Left/Right pointers | O(log n) |
| Union-Find (DSU) | Connected components | Parent array | O(α(n)) |

---

## Pattern 1: Sliding Window

### When to Use
- Find longest/shortest substring with condition
- Find subarray with specific sum/property
- "Contiguous" is mentioned
- Window of size k

### Template
```python
def sliding_window(arr, k):
    window_start = 0
    window_sum = 0  # or use dict for frequency
    result = 0

    for window_end in range(len(arr)):
        # Expand: add element at window_end
        window_sum += arr[window_end]

        # Shrink: when window is too large or invalid
        while window_end - window_start + 1 > k:  # or condition violated
            window_sum -= arr[window_start]
            window_start += 1

        # Update result
        result = max(result, window_sum)

    return result
```

### Variable Window Template
```python
def variable_sliding_window(s):
    char_count = {}
    window_start = 0
    max_length = 0

    for window_end in range(len(s)):
        # Add right character
        right_char = s[window_end]
        char_count[right_char] = char_count.get(right_char, 0) + 1

        # Shrink window while condition violated
        while len(char_count) > k:  # example condition
            left_char = s[window_start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
```

### Key Problems
- LC3: Longest Substring Without Repeating Characters
- LC76: Minimum Window Substring
- LC424: Longest Repeating Character Replacement
- LC1004: Max Consecutive Ones III

---

## Pattern 2: Two Pointers

### When to Use
- Sorted array
- Find pairs with target sum
- Remove duplicates
- Reverse array/string

### Template - Opposite Direction
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []
```

### Template - Same Direction
```python
def remove_duplicates(arr):
    if not arr:
        return 0

    write_idx = 1
    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[read_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1

    return write_idx
```

### Key Problems
- LC15: 3Sum
- LC11: Container With Most Water
- LC42: Trapping Rain Water
- LC26: Remove Duplicates from Sorted Array

---

## Pattern 3: Fast & Slow Pointers

### When to Use
- Detect cycle in linked list/array
- Find middle of linked list
- Find cycle start

### Template - Cycle Detection
```python
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
```

### Template - Find Cycle Start
```python
def find_cycle_start(head):
    slow = fast = head

    # Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
```

### Key Problems
- LC141: Linked List Cycle
- LC142: Linked List Cycle II
- LC287: Find the Duplicate Number
- LC876: Middle of the Linked List

---

## Pattern 4: Merge Intervals

### When to Use
- Overlapping intervals
- Meeting rooms
- Insert interval
- Merge schedules

### Template
```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # Overlapping
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
```

### Key Problems
- LC56: Merge Intervals
- LC57: Insert Interval
- LC253: Meeting Rooms II
- LC986: Interval List Intersections

---

## Pattern 5: Binary Search

### When to Use
- Sorted array
- Find target or insertion point
- "Search for answer" problems (find min/max that satisfies condition)
- Minimize maximum / Maximize minimum
- **Key signal**: MONOTONIC relationship (if true for X, true for all values in one direction)

### Template - Standard
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # or left for insertion point
```

### Template - Find First/Last
```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

### Template - Answer Binary Search (Find MINIMUM valid)
```python
def find_min_valid(lo, hi, is_valid):
    """Find smallest value where is_valid() returns True."""
    while lo < hi:
        mid = (lo + hi) // 2

        if is_valid(mid):
            hi = mid      # Valid! But maybe smaller works, keep mid, search LEFT
        else:
            lo = mid + 1  # Invalid! Skip mid entirely, search RIGHT

    return lo  # lo == hi at this point
```

### 🔑 KEY INSIGHT: Why `left = mid + 1` but `right = mid`?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   When INVALID (left = mid + 1):                                   │
│   • mid is DEFINITELY WRONG - we KNOW it's not the answer         │
│   • Safe to SKIP it: left = mid + 1                               │
│                                                                     │
│   When VALID (right = mid):                                        │
│   • mid MIGHT BE the answer! (smallest valid we've seen so far)   │
│   • We CAN'T skip it - keep it in range: right = mid              │
│   • If we used right = mid - 1, we might skip the actual answer!  │
│                                                                     │
│   THE GUARANTEE:                                                   │
│   • Loop stops when left == right (they converge)                 │
│   • right only moves to VALID positions                           │
│   • left keeps pushing forward, skipping invalid ones             │
│   • They MEET at the boundary = smallest valid answer!            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Visual Walkthrough

```
Search space: [1, 9], find smallest divisor where sum <= threshold

divisor:  1    2    3    4    5    6    7    8    9
valid?    ❌   ❌   ❌   ❌   ✅   ✅   ✅   ✅   ✅
                          ^
                    Answer = 5 (smallest valid)

Step 1: lo=1, hi=9, mid=5 → valid ✅ → hi=5  (keep 5)
Step 2: lo=1, hi=5, mid=3 → invalid ❌ → lo=4  (skip 3)
Step 3: lo=4, hi=5, mid=4 → invalid ❌ → lo=5  (skip 4)
Step 4: lo=5, hi=5 → STOP! Return 5
```

### Template - Find MAXIMUM valid
```python
def find_max_valid(lo, hi, is_valid):
    """Find largest value where is_valid() returns True."""
    while lo < hi:
        mid = (lo + hi + 1) // 2  # +1 to round UP (prevents infinite loop!)

        if is_valid(mid):
            lo = mid      # Valid! Try larger, keep mid, search RIGHT
        else:
            hi = mid - 1  # Invalid! Skip mid, search LEFT

    return lo
```

### Quick Reference Table

| Goal | mid calculation | When valid | When invalid |
|------|-----------------|------------|--------------|
| Find MIN valid | `(lo + hi) // 2` | `hi = mid` | `lo = mid + 1` |
| Find MAX valid | `(lo + hi + 1) // 2` | `lo = mid` | `hi = mid - 1` |

### Key Problems
- LC33: Search in Rotated Sorted Array
- LC153: Find Minimum in Rotated Sorted Array
- LC875: Koko Eating Bananas
- LC1011: Capacity To Ship Packages
- LC1283: Smallest Divisor Given Threshold
- LC1552: Magnetic Force Between Two Balls

---

## Pattern 6: Union-Find (DSU)

### When to Use
- Group elements by equivalence
- Connected components
- "Merge" or "union" operations
- Transitive relationships (if A~B and B~C, then A~C)

### Template
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already same group

        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### Key Problems
- LC721: Accounts Merge ⭐ (Failed in interview)
- LC547: Number of Provinces
- LC684: Redundant Connection
- LC1101: Earliest Moment When Everyone Become Friends

---

## Pattern 7: Monotonic Stack

### When to Use
- Next greater/smaller element
- Maximum rectangle in histogram
- Stock span problems
- Remove k digits

### Template - Next Greater Element
```python
def next_greater(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # Store indices

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result
```

### Template - Previous Smaller Element
```python
def previous_smaller(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)

    return result
```

### Key Problems
- LC739: Daily Temperatures
- LC84: Largest Rectangle in Histogram
- LC907: Sum of Subarray Minimums ⭐
- LC402: Remove K Digits

---

## Pattern 8: Tree BFS

### When to Use
- Level order traversal
- Minimum depth
- Connect level nodes
- Zigzag traversal

### Template
```python
from collections import deque

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

### Key Problems
- LC102: Binary Tree Level Order Traversal
- LC199: Binary Tree Right Side View
- LC111: Minimum Depth of Binary Tree
- LC103: Binary Tree Zigzag Level Order Traversal

---

## Pattern 9: Tree DFS

### When to Use
- Path sum problems
- Tree diameter
- Validate BST
- Lowest common ancestor

### Template - Recursive
```python
def dfs(root):
    if not root:
        return 0  # Base case

    left = dfs(root.left)
    right = dfs(root.right)

    # Process current node
    return 1 + max(left, right)  # Example: height
```

### Template - Iterative with Stack
```python
def dfs_iterative(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

### Key Problems
- LC124: Binary Tree Maximum Path Sum
- LC236: Lowest Common Ancestor
- LC98: Validate Binary Search Tree
- LC543: Diameter of Binary Tree

---

## Pattern 10: Backtracking

### When to Use
- Generate all combinations/permutations
- Subset problems
- Path finding in grid
- N-Queens, Sudoku

### Template
```python
def backtrack(candidates, path, result, start=0):
    # Base case: found valid solution
    if is_valid_solution(path):
        result.append(path[:])  # Make a copy!
        return

    for i in range(start, len(candidates)):
        # Skip duplicates if needed
        if i > start and candidates[i] == candidates[i-1]:
            continue

        # Make choice
        path.append(candidates[i])

        # Recurse
        backtrack(candidates, path, result, i + 1)  # or i for reuse

        # Undo choice
        path.pop()
```

### Key Problems
- LC46: Permutations
- LC78: Subsets
- LC39: Combination Sum
- LC51: N-Queens

---

## Pattern 11: Dynamic Programming

### When to Use
- Optimal substructure
- Overlapping subproblems
- "Count ways", "minimum/maximum"
- Can break into smaller problems

### Template - 1D DP
```python
def dp_1d(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case

    for i in range(1, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # Recurrence

    return dp[n]
```

### Template - 2D DP
```python
def dp_2d(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    dp[0][0] = 1

    # Fill table
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

    return dp[m][n]
```

### Key Problems
- LC198: House Robber
- LC322: Coin Change
- LC300: Longest Increasing Subsequence
- LC72: Edit Distance

---

## Pattern 12: Snapshot/Versioning

### When to Use
- Query historical state
- Time travel / version control
- Design problems with snapshots

### Template - Copy on Write (Simple)
```python
class SnapshotArray:
    def __init__(self, length):
        self.snapshots = [{} for _ in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        self.snapshots[index][self.snap_id] = val

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        # Binary search for largest snap_id <= target
        snaps = self.snapshots[index]
        keys = sorted(k for k in snaps if k <= snap_id)
        return snaps[keys[-1]] if keys else 0
```

### Template - Diff Chain (Space Efficient)
```python
class HistorySet:
    def __init__(self):
        self.history = []  # (prev_id, action, value)
        self.current = set()
        self.id = -1

    def add(self, val):
        if val in self.current:
            return self.id
        self.history.append((self.id, 'add', val))
        self.id += 1
        self.current.add(val)
        return self.id

    def remove(self, val):
        if val not in self.current:
            return self.id
        self.history.append((self.id, 'remove', val))
        self.id += 1
        self.current.remove(val)
        return self.id

    def members(self, op_id=None):
        if op_id is None or op_id == self.id:
            return set(self.current)
        # Reconstruct by replaying history
        ops = []
        curr = op_id
        while curr >= 0:
            prev, action, value = self.history[curr]
            ops.append((action, value))
            curr = prev
        s = set()
        for action, value in reversed(ops):
            if action == 'add':
                s.add(value)
            else:
                s.discard(value)
        return s
```

### Key Problems
- LC1146: Snapshot Array ⭐ (Google interview pattern)
- LC981: Time Based Key-Value Store
- Custom: HistorySet ⭐ (Failed in interview)
