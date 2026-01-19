# 494. Target Sum

**Difficulty:** Medium
**Pattern:** Dynamic Programming (Subset Sum / Knapsack Variation) / Recursion with Memoization

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** You are given an integer array `nums` and an integer `target`. You want to build an expression by adding one of the symbols `'+'` or `'-'` before each integer in `nums` and then concatenate all the integers. Return the number of different expressions that you can build, which evaluate to `target`.

**Interview Scenario (The "Boolean Expression Counting" Prompt):
"You have a sequence of values, and for each value, you can either add it to a running total or subtract it from the total. Your goal is to find out how many distinct sequences of additions/subtractions will result in a specific target sum. This is relevant for configuration space exploration or signal processing where phases can be inverted."

**Why this transformation?**
*   It generalizes the "+" / "-" choice to a binary decision for each element.
*   It emphasizes counting distinct ways, which is a hallmark of DP.

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty Array:** "What if `nums` is empty?" (Return 1 if target is 0, else 0).
2.  **Zeroes:** "How do zeroes affect the count?" (A `+0` or `-0` doesn't change the sum, but it counts as a distinct operation for `nums`, so it will double the count if we have zeroes).
3.  **Constraints:** "Length of `nums`?" (Up to 20 elements. This small N suggests $2^N$ or $N \times Sum$ complexity is acceptable).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Dynamic Programming (Subset Sum / Knapsack). Recursion with Memoization is also a strong choice due to the small `N`.

**The Logic (Recursion with Memoization):**
For each number `nums[i]`, we have two choices:
1.  Add `nums[i]` to the current sum.
2.  Subtract `nums[i]` from the current sum.

This forms a decision tree. Memoization prevents redundant calculations.

**State:** `(index, current_sum)`.
`memo[index][current_sum]` = number of ways to reach `current_sum` from `nums[index:]`.

**Optimization (Sum Transformation):**
Let `P` be the sum of numbers with `+` signs, and `N` be the sum of numbers with `-` signs.
`Sum(nums)` total = `P + N`.
`Target = P - N`.
We also know `P + N = Sum(all numbers)`.
Adding the two equations: `2P = Target + Sum(all numbers)`.
So, `P = (Target + Sum(all numbers)) / 2`.

This transforms the problem into: "Find the number of ways to pick a subset of `nums` that sums to `P`". This is a classic **Subset Sum** problem, solvable with DP.

*   **Condition:** `(Target + Sum(all numbers))` must be non-negative and even.

---

## 4. Base Template & Modification

**Standard Memoized DFS Template:**
```python
memo = {}
def dfs(index, current_sum):
    if (index, current_sum) in memo: return memo[(index, current_sum)]
    if index == len(nums):
        return 1 if current_sum == target else 0

    # choice 1: add
    ways1 = dfs(index + 1, current_sum + nums[index])
    # choice 2: subtract
    ways2 = dfs(index + 1, current_sum - nums[index])
    
    memo[(index, current_sum)] = ways1 + ways2
    return ways1 + ways2
```

**Modified Logic (DP / Subset Sum):**
Use the transformed target `P` and a 1D DP array (or 2D for explicit `index, sum`).
`dp[s]` = number of ways to get sum `s` using a subset of elements processed so far.

---

## 5. Optimal Solution (DP / Subset Sum Transformation)

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Edge case: If target is outside possible range
        if target > total_sum or target < -total_sum:
            return 0
        
        # Transformation: P - N = target and P + N = total_sum
        # Adding gives: 2P = target + total_sum
        # So, P = (target + total_sum) / 2
        # We need to find a subset that sums to P.
        # If (target + total_sum) is odd or negative, it's impossible to form P.
        if (target + total_sum) % 2 != 0 or (target + total_sum) < 0:
            return 0
            
        target_subset_sum = (target + total_sum) // 2
        
        # Now, this is a classic Subset Sum DP problem:
        # dp[s] = number of ways to get sum `s` using a subset of elements.
        # Initialize dp array. dp[0] = 1 (one way to get sum 0: choose nothing).
        dp = [0] * (target_subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            # Iterate from right to left to avoid using the same num multiple times 
            # in the current iteration's calculations.
            for s in range(target_subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
                
        return dp[target_subset_sum]
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N \times S)$ where $S$ is `sum(nums)` (or `target_subset_sum`).
    *   `N` iterations for `num`.
    *   Inner loop iterates up to `S` times.
*   **Space Complexity:** $O(S)$ where $S$ is `sum(nums)` (for the `dp` array).

---

## 7. Follow-up & Extensions

**Q: What if we needed to return *one* such expression?**
**A:** The recursive approach (DFS) could be modified to return the path (list of operations) instead of just counting.

**Q: What if the numbers were very large, but `N` was small?**
**A:** Meet-in-the-Middle technique. Split `nums` into two halves, generate all possible sums for each half, then find pairs of sums that add up to `target` (or `P`). This brings complexity down from $2^N$ to $2^{N/2}$.

```
