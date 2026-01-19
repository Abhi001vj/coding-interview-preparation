# 560. Subarray Sum Equals K

**Difficulty:** Medium
**Pattern:** Prefix Sum + Hash Map

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

**Interview Scenario (The "Financial Transactions" Prompt):**
"You are analyzing a sequence of financial transactions (gains and losses). You want to identify how many distinct, contiguous periods of transactions result in a net profit or loss of exactly `K` dollars. These periods can overlap. How would you count them efficiently?"

**Why this transformation?**
*   It provides a real-world context for "subarray sum".
*   It emphasizes "contiguous" and "overlapping" nature of subarrays.

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty Array:** "What if `nums` is empty?" (Return 0).
2.  **Negative Numbers:** "Can `nums` contain negative numbers?" (Yes, this is important as `current_sum` can decrease, preventing simple sliding window).
3.  **Zeroes:** "How do zeroes affect the count?" (A subarray of `[0]` has sum 0. If `k=0`, this counts. `[1,0,1]` and `k=1` has `[1]` and `[0,1]` and `[1]` as valid subarrays, where `[0,1]` has sum 1).
4.  **Constraints:** "Length of `nums`?" ($N \le 20,000$. This implies $O(N)$ or $O(N \log N)$ solution, $O(N^2)$ is too slow).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Prefix Sum + Hash Map.

**Why not Sliding Window?**
Standard sliding window works for positive numbers where `current_sum` is always non-decreasing. With negative numbers, `current_sum` can fluctuate, making it hard to shrink/expand the window predictably.

**The Logic (Prefix Sum + Hash Map):**
Let `P[i]` be the sum of `nums[0...i-1]` (prefix sum). Then the sum of any subarray `nums[j...i]` is `P[i+1] - P[j]`.
We want `P[i+1] - P[j] = k`. Rearranging, we need to find `P[j] = P[i+1] - k`.

**Algorithm:**
1.  Initialize `current_sum = 0`, `count = 0`.
2.  Use a hash map `freq_map` to store `(prefix_sum: frequency)`. Initialize `freq_map[0] = 1` to handle cases where the subarray starts from index 0 itself (i.e., `current_sum - k == 0`).
3.  Iterate through `num` in `nums`:
    *   `current_sum += num`.
    *   Check if `current_sum - k` exists in `freq_map`. If it does, add `freq_map[current_sum - k]` to `count`. This means for every previous prefix sum that equals `current_sum - k`, we found a subarray ending at the current position that sums to `k`.
    *   Increment `freq_map[current_sum]`.

---

## 4. Base Template & Modification

**Standard Prefix Sum + Hash Map Template:**
```python
prefix_sum_counts = {0: 1} # Base case for subarrays starting at index 0
current_sum = 0
count = 0
for x in nums:
    current_sum += x
    if current_sum - k in prefix_sum_counts:
        count += prefix_sum_counts[current_sum - k]
    prefix_sum_counts[current_sum] = prefix_sum_counts.get(current_sum, 0) + 1
return count
```

**Modified Logic:** None, this is the canonical template.

---

## 5. Optimal Solution

```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # `freq_map` stores (prefix_sum: frequency_of_that_prefix_sum)
        # Initialize with {0: 1} to handle cases where a subarray itself sums to k
        # (e.g., if current_sum becomes k, then current_sum - k = 0, and we need count for 0)
        freq_map = defaultdict(int)
        freq_map[0] = 1
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            # If `current_sum - k` exists in our frequency map,
            # it means there are `freq_map[current_sum - k]` subarrays
            # that end at the current position and sum to `k`.
            if (current_sum - k) in freq_map:
                count += freq_map[current_sum - k]
                
            # Add the current prefix sum to the frequency map
            freq_map[current_sum] += 1
            
        return count
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   One pass through the array.
    *   Hash map operations (insertion and lookup) take $O(1)$ on average.
*   **Space Complexity:** $O(N)$
    *   In the worst case, all prefix sums are unique, requiring $O(N)$ space for the hash map.

---

## 7. Follow-up & Extensions

**Q: Return the actual subarrays instead of just the count.**
**A:** This is harder. The hash map approach only gives counts. You'd likely need to store (sum, index_list) or similar, which blows up space/time. For specific problems asking for *one* subarray, you can store `(prefix_sum, index)` and retrieve indices.

**Q: What if elements can only be positive?**
**A:** A two-pointer sliding window approach would be optimal then, achieving $O(N)$ time and $O(1)$ space. (But it doesn't work with negatives).
