# 198. House Robber

**Difficulty:** Medium
**Pattern:** Dynamic Programming (1D Array)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. If two adjacent houses were broken into on the same night, it would alert the police. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob without alerting the police. (The problem statement for LeetCode 198 actually says they are *linearly* arranged, but the typical FAANG follow-up for this problem is the circular arrangement, so I'm setting up for that context, but providing linear solution first.)

**Interview Scenario (The "Resource Allocation with Constraints" Prompt):**
"You're optimizing a resource allocation strategy. You have a linear sequence of projects, each offering a certain profit. However, due to resource contention, you cannot undertake any two immediately adjacent projects. Design an algorithm to select a subset of non-adjacent projects that maximizes your total profit. What if these projects were arranged in a circle instead of a line?"

**Why this transformation?**
*   It generalizes the "robber" context to a more abstract resource allocation problem.
*   It explicitly mentions the **circular arrangement** as a key follow-up, which is crucial for this problem's understanding.

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty Array:** "What if `nums` is empty?" (Return 0).
2.  **Single/Two Houses:** "What if there's only one or two houses?" (Max of those available).
3.  **Values:** "Can house values be zero or negative?" (Assume non-negative for this problem, often given positive in problem statement).
4.  **Arrangement:** "Are houses in a line or a circle?" (Initially linear, but acknowledge the circular follow-up).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Dynamic Programming.

**The Overlapping Subproblems / Optimal Substructure:**
To decide if we rob house `i`, we look at two choices:
1.  **Rob house `i`:** In this case, we cannot rob house `i-1`. So, the total money is `nums[i]` + money from robbing houses up to `i-2`.
2.  **Don't rob house `i`:** In this case, we can potentially rob house `i-1`. So, the total money is money from robbing houses up to `i-1`.

We take the maximum of these two choices.

**State Definition:**
`dp[i]` = maximum money that can be robbed from houses `0` to `i`.

**Recurrence Relation:**
`dp[i] = max(dp[i-1], nums[i] + dp[i-2])`

**Base Cases:**
*   `dp[0] = nums[0]`
*   `dp[1] = max(nums[0], nums[1])` (if `nums` has at least 2 elements)

---

## 4. Base Template & Modification

**Standard 1D DP Template:**
```python
dp = [0] * (n)
dp[0] = ...
dp[1] = ...
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
return dp[n-1]
```

**Modified Logic (Space Optimization):**
Notice `dp[i]` only depends on `dp[i-1]` and `dp[i-2]`. We can optimize space to $O(1)$ by only keeping track of the previous two maximums.
*   `prev2 = dp[i-2]`
*   `prev1 = dp[i-1]`
*   `current = max(prev1, prev2 + nums[i])`

---

## 5. Optimal Solution (Space Optimized)

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Initialize dp states for the first two houses
        # dp[i] represents max money robbed up to house i
        
        # If only one house, rob it.
        # If two houses, rob the one with more money.
        
        # prev2_max_money: Max money robbed up to (i-2)th house
        # prev1_max_money: Max money robbed up to (i-1)th house
        prev2_max_money = nums[0]
        prev1_max_money = max(nums[0], nums[1])
        
        # Iterate from the third house onwards (index 2)
        for i in range(2, len(nums)):
            # current_max_money: Max money robbed up to ith house
            # Option 1: Don't rob current house (i), so max is prev1_max_money
            # Option 2: Rob current house (i), so max is nums[i] + prev2_max_money
            current_max_money = max(prev1_max_money, nums[i] + prev2_max_money)
            
            # Update previous states for the next iteration
            prev2_max_money = prev1_max_money
            prev1_max_money = current_max_money
            
        return prev1_max_money # After loop, prev1_max_money holds the result for the last house
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   One pass through the array.
*   **Space Complexity:** $O(1)$
    *   Only constant number of variables used.

---

## 7. Follow-up & Extensions

**Q: House Robber II (Circular Arrangement).**
**A:** If houses are in a circle, house 0 and house `n-1` are adjacent. This means you cannot rob both.
*   **Strategy:** Break it into two subproblems:
    1.  Max money robbing `houses[0]` to `houses[n-2]` (i.e., exclude the last house).
    2.  Max money robbing `houses[1]` to `houses[n-1]` (i.e., exclude the first house).
*   The answer is the maximum of these two results. Both subproblems can be solved with the linear `House Robber I` logic.
