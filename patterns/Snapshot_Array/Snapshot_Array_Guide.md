# Snapshot Array Study Guide

**Pattern:** Versioned Data / Binary Search on History  
**Common Applications:** Version Control, Time-Travel Debugging, Persistent Data Structures  

---

## 1. The Core Intuition

Standard arrays are **mutable and forgetful**. If you change `A[0] = 5` to `A[0] = 10`, the `5` is lost forever.
Snapshot Arrays are **accountants**. They verify "What was the balance on January 1st?"

**The Data Structure:**
Instead of a single integer, every "cell" in the array is a **list of records**.
```python
# Standard Array
arr[0] = 10

# Snapshot Array (History)
arr[0] = [
    (snap_id=0, val=0),   # Initial
    (snap_id=2, val=5),   # Changed at snap 2
    (snap_id=5, val=10)   # Changed at snap 5
]
```

**The Query:**
`get(index=0, snap_id=3)`
- We go to `arr[0]`.
- We see records for snaps `0, 2, 5`.
- `3` is not there!
- **Rule:** If `3` is missing, the value is whatever it was at the *most recent previous snapshot*.
- We look for the largest ID $\le 3$. That is `2`. Value is `5`.

---

## 2. The Algorithm (Binary Search)

Since the `snap_id`s in the list are always sorted (we only add to the end as time moves forward), we can use **Binary Search**.

### Why Binary Search?
- Linear scan: $O(S)$ where S is number of updates. Too slow if many updates.
- Binary search: $O(\log S)$.

### Bisect Right vs Left?
We want the value **associated with** the largest ID $\le$ Query ID.
Python's `bisect_right` finds the insertion point *after* the target.
`bisect_right(list, target_snap)` gives us the index where a *newer* snapshot would go.
The index *before* that (`index - 1`) is the answer.

---

## 3. Template Code (Memorize This)

```python
import bisect

class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        # List of lists. Each entry is [snap_id, value]
        # Initialize all indices with (snap=0, val=0)
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        # Optimization: If we update same index multiple times 
        # inside the SAME snapshot, just overwrite the last entry.
        if self.history[index][-1][0] == self.snap_id:
            self.history[index][-1] = (self.snap_id, val)
        else:
            self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        hist = self.history[index]
        # Find rightmost insertion point for (snap_id, INF)
        # This gives us the index of the first element strictly GREATER than snap_id
        i = bisect.bisect_right(hist, (snap_id, float('inf')))
        
        # The element at i-1 is the largest one <= snap_id
        return hist[i - 1][1]
```

---

## 4. Key Variations

### 1. Time-Based Key-Value Store (LC 981)
- **Difference:** Instead of integer `index`, use a `HashMap<String, List>`.
- **Timestamps:** Instead of auto-incrementing `snap_id`, the user provides `timestamp`.
- **Logic:** Identical. `Map[key]` gives the history list. Binary search the list.

### 2. Random Access vs Sparse Updates
- If the array is huge ($10^9$) but updates are sparse, use a `Map<Integer, List>` instead of `List<List>`.

---

## 5. Complexity Analysis
- **Space:** $O(U)$ where U is total number of `set` calls (updates). We only store changes.
- **Time (Set):** $O(1)$.
- **Time (Snap):** $O(1)$.
- **Time (Get):** $O(\log U_{idx})$ where $U_{idx}$ is number of updates to that specific index.
