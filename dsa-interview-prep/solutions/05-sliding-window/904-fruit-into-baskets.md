# 904. Fruit Into Baskets

**Difficulty:** Medium
**Pattern:** Sliding Window (Fixed Distinct Elements)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** You are visiting a farm that has a single row of fruit trees arranged from left to right. You are given an integer array `fruits` where `fruits[i]` is the type of fruit the `i-th` tree produces. You want to collect as much fruit as possible. You start at any tree of your choice, then repeatedly perform the following actions:
1.  Add one piece of fruit from the current tree to your baskets.
2.  If you cannot, stop. You have only two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Return the maximum number of fruits you can collect.

**Interview Scenario (The "Data Type Consolidation" Prompt):**
"You are analyzing a long sequence of data packets, where each packet has a specific 'type'. You need to find the longest contiguous sub-sequence of packets that contains at most two distinct types. This is relevant for optimizing network buffering or merging data streams where diversity needs to be limited."

**Why this transformation?**
*   It generalizes "fruit types" to "data types" to make it more abstract.
*   It highlights the core constraint: **at most two distinct types** within the window.

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty Array:** "What if `fruits` is empty?" (Return 0).
2.  **Single Type:** "What if all fruits are the same type?" (Return `len(fruits)`).
3.  **Indices:** "Do I return the count of fruits or the start/end indices?" (Just the count).
4.  **Constraints:** "Length of `fruits`?" ($N \le 10^5$. Implies $O(N)$ solution).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Sliding Window (Variable Size, based on count of distinct elements).

**The Logic:**
We want to find the longest subarray (window) that contains at most two distinct fruit types.

1.  Use a `left` and `right` pointer to define the current window `[left, right]`.
2.  Use a `frequency map` (or `defaultdict`) to keep track of the count of each fruit type within the current window.
3.  Expand the window with `right`:
    *   Add `fruits[right]` to the frequency map.
4.  Shrink the window with `left`:
    *   If `len(freq_map)` (number of distinct fruit types) exceeds 2, we need to shrink.
    *   Decrement count of `fruits[left]` in `freq_map`.
    *   If count of `fruits[left]` becomes 0, remove it from `freq_map` (distinct count decreases).
    *   Increment `left`.
5.  At each valid window (distinct types $\le 2$), update `max_fruits = max(max_fruits, right - left + 1)`.

---

## 4. Base Template & Modification

**Standard Sliding Window Template (Variable Size):**
```python
left = 0
max_len = 0
window_map = {}
for right in range(len(array)):
    add_to_window(array[right], window_map)
    while condition_invalid(window_map):
        remove_from_window(array[left], window_map)
        left += 1
    max_len = max(max_len, right - left + 1)
```

**Modified Logic:**
`condition_invalid` is `len(window_map) > 2`.

---

## 5. Optimal Solution

```python
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
            
        # `fruit_counts` stores the frequency of each fruit type in the current window
        fruit_counts = defaultdict(int)
        max_fruits = 0
        left = 0 # Left pointer of the sliding window
        
        # Iterate with the right pointer to expand the window
        for right in range(len(fruits)):
            # Add the current fruit to the window
            fruit_counts[fruits[right]] += 1
            
            # If the number of distinct fruit types in the window exceeds 2,
            # shrink the window from the left until the condition is met again.
            while len(fruit_counts) > 2:
                # Remove the fruit at the left pointer from the window
                fruit_counts[fruits[left]] -= 1
                
                # If its count becomes 0, remove the type from the map
                if fruit_counts[fruits[left]] == 0:
                    del fruit_counts[fruits[left]]
                    
                left += 1 # Shrink window from the left
            
            # At this point, the window [left, right] is valid (at most 2 distinct fruit types).
            # Calculate the current window size and update max_fruits.
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   Both `left` and `right` pointers traverse the array at most once.
    *   Hash map operations (get, put, delete) take $O(1)$ on average.
*   **Space Complexity:** $O(1)$ (effectively $O(K)$ where $K$ is max distinct fruit types allowed)
    *   The hash map stores at most 3 entries (two fruit types, and temporarily one more if shrinking).

---

## 7. Follow-up & Extensions

**Q: What if you had `k` baskets instead of 2?**
**A:** Change the condition `len(fruit_counts) > 2` to `len(fruit_counts) > k`.

**Q: What if the order of collected fruits mattered? (Not applicable for this problem).**
**A:** This usually implies permutation problems, not relevant here.
