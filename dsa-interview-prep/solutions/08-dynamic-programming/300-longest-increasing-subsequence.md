# 300. Longest Increasing Subsequence

**Difficulty:** Medium
**Pattern:** Dynamic Programming / Patience Sorting (Binary Search)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**Interview Scenario (The "Signal Filtering" Prompt):**
"You have a stream of timestamps or signal strengths arriving over time. Due to network noise, the data is jittery. You need to identify the longest chain of data points that maintains a strictly increasing trend, effectively filtering out the noise to see the underlying growth signal. How can you find the length of this trend efficiently?"

**Why this transformation?**
*   It contextualizes "subsequence" (can skip elements) vs "substring" (contiguous).
*   It sets the stage for discussing efficiency ($O(N^2)$ vs $O(N \log N)$).

---

## 2. Clarifying Questions (Phase 1)

1.  **Strictly Increasing:** "Does `[1, 2, 2]` count as increasing?" (Problem says *strictly*, so no. 2 cannot follow 2).
2.  **Output:** "Do you need the actual subsequence or just the length?" (Just the length).
3.  **Constraints:** "How large is N?" (If $N=2500$, $O(N^2)$ is okay. If $N=10^5$, we need $O(N \log N)$).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Dynamic Programming or Patience Sorting.

**Approach 1: DP ($O(N^2)$)**
`dp[i]` = length of LIS ending at index `i`.
`dp[i] = 1 + max(dp[j])` for all `j < i` where `nums[j] < nums[i]`.
This is intuitive but slow.

**Approach 2: Build a Subsequence with Binary Search ($O(N \log N)$)**
We maintain a list `tails`, where `tails[i]` is the *smallest tail of all increasing subsequences of length i+1*.
Why? To extend a subsequence, we want the *smallest* ending value possible, to make it easier for future numbers to be added.

**Logic:**
Iterate through `x` in `nums`:
1.  If `x` is larger than all tails, append it (we found a longer subsequence).
2.  If `x` is smaller, replace the smallest tail that is $\ge x$ with `x`.
    *   This effectively says: "I found a subsequence of length `k` that ends with a smaller value `x`. This is better than the previous one ending with `tails[k]`, so I'll update it."
    *   This replacement doesn't change the *length* of the LIS found so far, but it lowers the "barrier to entry" for future elements.

---

## 4. Base Template & Modification

**Standard Bisect Template:**
```python
sub = []
for x in nums:
    if len(sub) == 0 or sub[-1] < x:
        sub.append(x)
    else:
        idx = bisect_left(sub, x)
        sub[idx] = x
return len(sub)
```

**Modified Logic:**
None, this is the standard patience sorting implementation.

---

## 5. Optimal Solution

```python
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # 'tails' list will store the smallest tail of all increasing subsequences 
        # of length i+1 at tails[i].
        # Note: 'tails' is NOT the LIS itself, but it effectively tracks lengths.
        tails = []
        
        for num in nums:
            # Case 1: num is greater than the largest tail.
            # We can extend the longest subsequence found so far.
            if not tails or num > tails[-1]:
                tails.append(num)
                
            # Case 2: num can replace an existing tail to make it smaller.
            # Find the first element in tails >= num and replace it.
            # This maintains the sorted order of 'tails' (essential for binary search).
            else:
                idx = bisect.bisect_left(tails, num)
                tails[idx] = num
                
        return len(tails)
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N \log N)$
    *   We iterate through `nums` once ($N$).
    *   Inside the loop, `bisect_left` takes $O(\log K)$ where $K$ is the current length of `tails` ($\le N$).
*   **Space Complexity:** $O(N)$
    *   The `tails` list can grow up to size $N$.

---

## 7. Follow-up & Extensions

**Q: Return the actual LIS (not just length).**
**A:** The `tails` array does NOT contain the LIS. To reconstruct it, we need to store predecessors.
*   Let `P[i]` be the index of the predecessor of `nums[i]` in the LIS ending at `nums[i]`.
*   Maintain an array `M` where `M[j]` is the index `k` such that `nums[k]` is the tail of the LIS of length `j`.
*   When updating `tails` (conceptually `M`), record `P[i] = M[j-1]`.

**Q: Longest Non-Decreasing Subsequence?**
**A:** Change `bisect_left` to `bisect_right` and condition `num >= tails[-1]`.
