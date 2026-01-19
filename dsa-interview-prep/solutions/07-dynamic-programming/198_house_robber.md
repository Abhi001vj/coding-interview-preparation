# 198. House Robber
**Difficulty:** Medium | **Pattern:** Dynamic Programming (Linear) | **Companies:** Google, Meta, Amazon, Microsoft

---

## 1. Google/Meta Style Question Transformation

### Original LeetCode Problem:
Given an array `nums` representing money in each house along a street, return the maximum amount you can rob without robbing two adjacent houses.

### Google Scenario Wrapper:
> "At Google Ads, we're optimizing ad placement. Given a sequence of ad slots with different revenue values, select non-adjacent slots to maximize total revenue. Adjacent slots can't both show premium ads due to user experience guidelines."

### Meta Constraint Twist:
> Same problem but: "Return the indices of houses you'd rob, not just the total amount. If multiple solutions give the same max, return the one with fewer houses robbed."

---

## 2. Clarifying Questions (Ask in Interview!)

1. **Input Constraints:**
   - Can values be negative? → No, 0 ≤ nums[i] ≤ 400
   - Can array be empty? → Yes, return 0
   - Size limit? → 1 ≤ n ≤ 100

2. **Edge Cases:**
   - Empty array → return 0
   - Single house → return that value
   - Two houses → return max of both
   - All same values

3. **Output Requirements:**
   - Return maximum sum (integer)
   - Don't need to return which houses

---

## 3. Pattern Recognition

### Why Dynamic Programming?
- **Key Signal 1:** "Maximum" → Optimization problem
- **Key Signal 2:** "Cannot choose adjacent" → Constraint-based decision at each step
- **Key Signal 3:** Optimal substructure: best solution at house i depends on best solutions before i

### Pattern Match:
| Problem Feature | Pattern Indicator |
|-----------------|-------------------|
| "Maximum/minimum" | DP or Greedy |
| Decision at each step | DP with state |
| Cannot take adjacent | State depends on whether we took previous |
| Linear array | 1D DP |

### Key Insight:
At each house, we have two choices:
1. **Rob it:** Add current value + best from 2 houses ago
2. **Skip it:** Take best from previous house

`dp[i] = max(nums[i] + dp[i-2], dp[i-1])`

---

## 4. Approach Discussion

### Approach 1: Recursion with Memoization - O(n) time, O(n) space
**Intuition:** At each house, choose max of robbing or skipping.

**Steps:**
1. Define `rob(i)` = max money robbing from house i onwards
2. rob(i) = max(nums[i] + rob(i+2), rob(i+1))
3. Use memoization to avoid recomputation

### Approach 2: Bottom-up DP Array - O(n) time, O(n) space
**Intuition:** Build solution from small subproblems.

**Steps:**
1. dp[i] = max money robbing up to house i
2. dp[i] = max(nums[i] + dp[i-2], dp[i-1])
3. Return dp[n-1]

### Approach 3: Space-Optimized DP - O(n) time, O(1) space (Optimal)
**Intuition:** Only need last two values, not entire array.

**Steps:**
1. Track prev2 (best 2 houses ago) and prev1 (best at previous house)
2. Update at each step
3. Return final value

---

## 5. Base Template

```python
# Base Template: Linear DP with "take or skip" decision
def linear_dp_take_skip(nums):
    """
    Template for DP where at each step we either
    take current element (can't take adjacent) or skip it.

    State: dp[i] = max value considering elements 0..i
    Transition: dp[i] = max(take, skip)
      - take = nums[i] + dp[i-2]
      - skip = dp[i-1]
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # Space-optimized: only need last two values
    prev2 = 0           # dp[i-2]
    prev1 = nums[0]     # dp[i-1]

    for i in range(1, len(nums)):
        current = max(
            nums[i] + prev2,  # Take current
            prev1             # Skip current
        )
        prev2 = prev1
        prev1 = current

    return prev1
```

---

## 6. Solution - How We Modify the Template

### Solution 1: Top-Down with Memoization

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Top-down DP with memoization.

        Time: O(n)
        Space: O(n) for memoization + recursion stack
        """
        memo = {}

        def dp(i):
            # Base cases
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            # Choice: rob current house + skip next, OR skip current
            rob_current = nums[i] + dp(i + 2)
            skip_current = dp(i + 1)

            memo[i] = max(rob_current, skip_current)
            return memo[i]

        return dp(0)
```

### Solution 2: Bottom-Up DP Array

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Bottom-up DP with array.

        dp[i] = max money robbing houses 0 to i

        Time: O(n)
        Space: O(n)
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(
                nums[i] + dp[i-2],  # Rob house i
                dp[i-1]              # Skip house i
            )

        return dp[n-1]
```

### Solution 3: Space-Optimized (Optimal)

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Space-optimized DP.

        Only need previous two values at each step.

        Time: O(n)
        Space: O(1)
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # prev2 = max money at i-2
        # prev1 = max money at i-1
        prev2 = 0
        prev1 = nums[0]

        for i in range(1, len(nums)):
            # Current = max(rob this house, skip this house)
            current = max(nums[i] + prev2, prev1)

            # Slide window forward
            prev2 = prev1
            prev1 = current

        return prev1
```

### Visual Walkthrough for nums=[2,7,9,3,1]:

```
House values: [2, 7, 9, 3, 1]
               0  1  2  3  4

Building dp array (bottom-up):

dp[0] = 2                    (only option: rob house 0)
dp[1] = max(2, 7) = 7        (rob house 0 OR house 1)
dp[2] = max(9+2, 7) = 11     (rob houses 0,2 OR best up to 1)
dp[3] = max(3+7, 11) = 11    (rob houses 1,3 OR best up to 2)
dp[4] = max(1+11, 11) = 12   (rob houses 0,2,4 OR best up to 3)

Final: [2, 7, 11, 11, 12]
Answer: 12 (houses 0, 2, 4 → 2+9+1=12)

Space-optimized trace:
i=0: prev2=0, prev1=2
i=1: curr=max(7+0, 2)=7, prev2=2, prev1=7
i=2: curr=max(9+2, 7)=11, prev2=7, prev1=11
i=3: curr=max(3+7, 11)=11, prev2=11, prev1=11
i=4: curr=max(1+11, 11)=12, prev2=11, prev1=12

Answer: 12
```

---

## 7. Complexity Analysis

### Time Complexity: O(n)
- Visit each house exactly once
- O(1) work at each house

### Space Complexity:
- **Memoization:** O(n) for memo + O(n) recursion stack
- **Bottom-up Array:** O(n) for dp array
- **Space-optimized:** O(1) - only two variables

---

## 8. Test Cases & Edge Cases

```python
# Test Case 1: Basic example
Input: nums = [1,2,3,1]
Expected: 4
Trace: Rob houses 0 and 2 (1+3=4)

# Test Case 2: Given example
Input: nums = [2,7,9,3,1]
Expected: 12
Trace: Rob houses 0, 2, 4 (2+9+1=12)

# Test Case 3: Single house
Input: nums = [5]
Expected: 5

# Test Case 4: Two houses
Input: nums = [2,1]
Expected: 2

# Test Case 5: All same values
Input: nums = [5,5,5,5,5]
Expected: 15
Trace: Rob houses 0, 2, 4 (5+5+5=15)

# Test Case 6: Increasing values
Input: nums = [1,2,3,4,5]
Expected: 9
Trace: Rob houses 1, 3 or 0, 2, 4 = max(2+4, 1+3+5) = 9

# Test Case 7: Empty array
Input: nums = []
Expected: 0
```

---

## 9. Common Mistakes to Avoid

1. **Wrong base case initialization:**
   ```python
   # WRONG
   dp[1] = nums[1]  # Should compare with dp[0]

   # CORRECT
   dp[1] = max(nums[0], nums[1])
   ```

2. **Off-by-one in space optimization:**
   ```python
   # WRONG - starting from wrong index
   for i in range(len(nums)):

   # CORRECT - start from 1 since we handle 0 separately
   for i in range(1, len(nums)):
   ```

3. **Forgetting edge cases:**
   ```python
   # Must handle:
   if not nums: return 0
   if len(nums) == 1: return nums[0]
   ```

4. **Wrong update order in space optimization:**
   ```python
   # WRONG
   prev1 = current
   prev2 = prev1  # Now prev2 == current!

   # CORRECT
   prev2 = prev1
   prev1 = current
   ```

---

## 10. Follow-up Questions

### Follow-up 1: "Houses arranged in a circle" (LC 213 House Robber II)
**Answer:** First and last houses are adjacent. Run twice:
1. Rob houses 0 to n-2 (exclude last)
2. Rob houses 1 to n-1 (exclude first)
Return max of both.

### Follow-up 2: "Houses arranged in a binary tree" (LC 337 House Robber III)
**Answer:** Use tree DP. At each node, return pair (rob_this, skip_this).
```python
def dfs(node):
    if not node:
        return (0, 0)
    left = dfs(node.left)
    right = dfs(node.right)
    rob = node.val + left[1] + right[1]
    skip = max(left) + max(right)
    return (rob, skip)
```

### Follow-up 3: "Return which houses to rob"
**Answer:** Backtrack through dp array or track decisions.
```python
# After computing dp, backtrack:
result = []
i = n - 1
while i >= 0:
    if i == 0 or dp[i] != dp[i-1]:
        result.append(i)
        i -= 2
    else:
        i -= 1
return result[::-1]
```

### Follow-up 4: "Minimum robbery to get at least target amount"
**Answer:** Different DP state - track minimum count to achieve each amount.

### Related Problems:
- LC 213 - House Robber II (Circular)
- LC 337 - House Robber III (Binary Tree)
- LC 740 - Delete and Earn (Similar DP concept)
- LC 256 - Paint House (Similar "can't use adjacent same")

---

## 11. Interview Tips

- **Time Target:** 10-15 minutes for this medium problem
- **Communication Points:**
  - "This is a classic DP problem - at each house I have two choices"
  - "My state is the max money up to house i"
  - "Since I only need the last two values, I can optimize to O(1) space"
  - "Let me trace through a small example..."
- **Red Flags to Avoid:**
  - Trying greedy (doesn't work - picking max doesn't guarantee optimal)
  - Not recognizing this is a "take or skip" DP pattern
  - Forgetting circular variant is a common follow-up
