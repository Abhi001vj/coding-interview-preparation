# 53. Maximum Subarray

**Difficulty:** Medium
**Pattern:** Dynamic Programming / Kadane's Algorithm

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

**Interview Scenario (The "Stock Profit" Prompt):**
"I have a list of daily P&L (Profit and Loss) numbers for a trading strategy over time. Some days we made money (positive), some days we lost (negative). I want to find the single continuous period where we made the maximum total profit. Note: The period must be continuous."

**Why this transformation?**
*   It distinguishes between "Subarray" (continuous) and "Subsequence" (any elements).
*   It sets up the "reset" intuition: if your cumulative profit drops below zero, you're better off starting a new period from the next day.

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty Array:** "Can the array be empty? If so, is the max sum 0 or -infinity?" (Usually at least 1 element).
2.  **All Negatives:** "What if all numbers are negative?" (Return the largest single negative number, e.g., `[-5, -2, -9]` -> `-2`. Do NOT return 0 unless an empty subarray is allowed).
3.  **Result:** "Return just the sum or the indices?" (Just the sum).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Kadane's Algorithm ($O(N)$).

**Why not Brute Force?**
Trying all subarrays is $O(N^2)$. We need linear time.

**The Logic (Kadane's):**
Iterate through the array adding numbers to a `current_sum`.
*   Decision at each step: Should I extend the previous subarray, or start a new one here?
*   **Rule:** If `current_sum + x < x`, it means `current_sum` was negative (dragging us down). We should discard the history and start fresh at `x`.
*   Formally: `current_sum = max(x, current_sum + x)`.

---

## 4. Base Template & Modification

**Kadane's Template:**
```python
max_so_far = -inf
current_max = 0
for x in nums:
    current_max = max(x, current_max + x)
    max_so_far = max(max_so_far, current_max)
```

**Modified Logic:**
None needed, this is the canonical problem for this pattern.

---

## 5. Optimal Solution

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Initialize with the first element to handle the "all negative" case correctly
        max_so_far = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            x = nums[i]
            
            # Decision: Start new subarray at x, or extend existing one?
            # equivalent to: current_sum = max(x, current_sum + x)
            if current_sum < 0:
                current_sum = x  # Reset: previous sum was negative, ditch it
            else:
                current_sum += x # Extend
                
            max_so_far = max(max_so_far, current_sum)
            
        return max_so_far
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   One pass through the array.
*   **Space Complexity:** $O(1)$
    *   Only scalar variables used.

---

## 7. Follow-up & Extensions

**Q: Return the subarray indices?**
**A:** We need to track `start`, `end`, and `temp_start`.
*   When `current_sum` resets (i.e., `current_sum = x`), set `temp_start = i`.
*   When `max_so_far` updates, set `start = temp_start`, `end = i`.

**Q: Maximum Circular Subarray Sum?**
**A:** A circular subarray is either the standard max subarray OR (Total Sum - Minimum Subarray Sum). We compute both and take the max.
