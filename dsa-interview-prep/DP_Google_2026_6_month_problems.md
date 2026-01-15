# Dynamic Programming Master Guide for Google/FAANG Interviews

A comprehensive guide mapping 60+ DP problems to 5 fundamental forms, showing how base templates are modified for each problem.

---

## Table of Contents

1. [The 5 DP Forms Overview](#the-5-dp-forms-overview)
2. [Form 1: Object/Level-based (Knapsack)](#form-1-objectlevel-based-knapsack)
3. [Form 2: Ending Form (LIS, Path Finding)](#form-2-ending-form-lis-path-finding)
4. [Form 3: Multi-Sequence DP (LCS, Edit Distance)](#form-3-multi-sequence-dp-lcs-edit-distance)
5. [Form 4: Interval DP](#form-4-interval-dp)
6. [Form 5: Game DP](#form-5-game-dp)
7. [Special/Hybrid Problems](#specialhybrid-problems)
8. [Problem Index](#problem-index)

---

## The 5 DP Forms Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        THE 5 FUNDAMENTAL DP FORMS                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FORM 1: Object/Level-based (Knapsack)                                     │
│  ──────────────────────────────────────                                    │
│  • Iterate through objects, decide: TAKE or SKIP                           │
│  • State: dp[i][capacity] or dp[capacity]                                  │
│  • Template: dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])        │
│  • Problems: House Robber, Coin Change, Subset Sum, Target Sum             │
│                                                                             │
│  FORM 2: Ending Form (LIS, Path Finding)                                   │
│  ───────────────────────────────────────                                   │
│  • Find best answer ENDING at index i                                      │
│  • State: dp[i] = best value ending at position i                          │
│  • Template: dp[i] = best(dp[j] + contribution) for valid j < i           │
│  • Problems: LIS, Maximum Subarray, Grid Paths, Jump Game                  │
│                                                                             │
│  FORM 3: Multi-Sequence DP (LCS, Edit Distance)                            │
│  ──────────────────────────────────────────────                            │
│  • Two or more sequences interacting                                       │
│  • State: dp[i][j] = answer for s1[0:i] and s2[0:j]                       │
│  • Template: Match/Mismatch transitions between sequences                  │
│  • Problems: LCS, Edit Distance, Regex Matching, Palindrome                │
│                                                                             │
│  FORM 4: Interval DP                                                        │
│  ───────────────────                                                       │
│  • Solve for range [L, R] by splitting into subranges                      │
│  • State: dp[l][r] = answer for interval [l, r]                           │
│  • Template: dp[l][r] = best(dp[l][k] + dp[k][r] + cost) for l<k<r        │
│  • Problems: Matrix Chain, Palindrome Partition, Burst Balloons            │
│                                                                             │
│  FORM 5: Game DP                                                            │
│  ───────────────                                                           │
│  • Predict winner with optimal play from both players                      │
│  • State: dp[state] = WIN if can reach any LOSE state                     │
│  • Template: Win if any move leads to opponent losing                      │
│  • Problems: Predict Winner, Stone Game variants, Nim                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Form Selection Flowchart

```
                         What's the DP about?
                                │
        ┌───────────────────────┼───────────────────────┐
        ↓                       ↓                       ↓
  Select items?          Two sequences?         Range [L,R]?
        │                       │                       │
        ↓                       ↓                       ↓
    FORM 1                   FORM 3                 FORM 4
  (Knapsack)                 (LCS)               (Interval)
        │                       │                       │
        │                       │                       │
        ↓                       ↓                       ↓
  Take/Skip?              Match chars?           Split point?
  Budget limit?           Transform?             Merge cost?


        ┌───────────────────────┼───────────────────────┐
        ↓                       ↓                       ↓
  Best ending at i?       Two players?          Special case?
        │                       │                       │
        ↓                       ↓                       ↓
    FORM 2                   FORM 5               HYBRID
   (Ending)                 (Game)              (Multiple)
```

---

## Form 1: Object/Level-based (Knapsack)

### Base Template

```python
def knapsack_template(items, capacity):
    """
    Form 1: Object/Level-based DP

    For each item, decide: TAKE or SKIP
    State: dp[capacity] = best value achievable with given capacity
    """
    dp = [0] * (capacity + 1)

    for item in items:
        weight, value = item
        # Iterate backwards to avoid using same item twice (0/1 knapsack)
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[capacity]
```

---

### LC 198 - House Robber ⭐

**Form:** 1 (Object/Level-based)

**Problem:** Rob houses without robbing adjacent ones. Maximize money.

**Template Modification:**
- Objects = houses with money
- "Take" = rob this house (skip previous)
- "Skip" = don't rob (can continue from previous)
- Capacity constraint → Adjacent constraint

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Form 1 Modification:
        - dp[i] = max money robbing houses 0..i
        - Take house i: dp[i-2] + nums[i]
        - Skip house i: dp[i-1]

        Space optimized: only need prev two values
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Space optimization: prev2 = dp[i-2], prev1 = dp[i-1]
        prev2, prev1 = 0, 0

        for num in nums:
            # Take current: prev2 + num
            # Skip current: prev1
            curr = max(prev1, prev2 + num)
            prev2, prev1 = prev1, curr

        return prev1

# Time: O(n), Space: O(1)
```

**Why Form 1?** Each house is an "object" we decide to take/skip with adjacency constraint.

---

### LC 213 - House Robber II ⭐

**Form:** 1 (Object/Level-based) with circular constraint

**Problem:** Houses in a circle. Can't rob first and last together.

**Template Modification:**
- Same as House Robber but handle circular array
- Run twice: exclude first house OR exclude last house

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Form 1 Modification for circular array:
        - Can't rob both first and last
        - Solution: max(rob[0:n-1], rob[1:n])
        """
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for money in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            return prev1

        # Exclude last house OR exclude first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Time: O(n), Space: O(1)
```

---

### LC 337 - House Robber III ⭐

**Form:** 1 adapted to Tree structure

**Problem:** Houses form a binary tree. Can't rob parent and child together.

**Template Modification:**
- Objects = tree nodes
- State per node: (rob_this_node, skip_this_node)
- Combine children's states

```python
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        Form 1 on Tree:
        - For each node, return (rob_it, skip_it)
        - If rob current: can't rob children → skip_left + skip_right + val
        - If skip current: max of each child's options
        """
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, skip)

            left = dfs(node.left)
            right = dfs(node.right)

            # Rob this node: must skip both children
            rob = node.val + left[1] + right[1]

            # Skip this node: take best of each child
            skip = max(left) + max(right)

            return (rob, skip)

        return max(dfs(root))

# Time: O(n), Space: O(h) for recursion stack
```

---

### LC 322 - Coin Change ⭐

**Form:** 1 (Unbounded Knapsack variant)

**Problem:** Minimum coins to make amount.

**Template Modification:**
- Objects = coin denominations (unlimited use)
- Capacity = target amount
- Minimize instead of maximize

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Form 1 (Unbounded Knapsack):
        - dp[a] = min coins to make amount a
        - For each coin, iterate forward (can use coin multiple times)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            # Forward iteration = unbounded (can reuse coins)
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

# Time: O(amount * len(coins)), Space: O(amount)
```

---

### LC 518 - Coin Change II ⭐

**Form:** 1 (Count combinations, not permutations)

**Problem:** Count ways to make amount (combinations, order doesn't matter).

**Template Modification:**
- Iterate coins in outer loop (ensures combinations, not permutations)
- Count ways instead of min/max

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Form 1 (Counting Combinations):
        - dp[a] = number of ways to make amount a
        - Outer loop on coins ensures we count combinations not permutations

        Key: coins outer, amount inner = combinations
             amount outer, coins inner = permutations
        """
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make 0: use nothing

        for coin in coins:  # Iterate coins first!
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]

# Time: O(amount * len(coins)), Space: O(amount)
```

---

### LC 416 - Partition Equal Subset Sum ⭐

**Form:** 1 (0/1 Knapsack - Boolean variant)

**Problem:** Can array be partitioned into two equal-sum subsets?

**Template Modification:**
- Target = total_sum / 2
- Boolean DP: can we achieve this sum?

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Form 1 (Boolean Knapsack):
        - If total sum is odd, impossible
        - Find if subset with sum = total/2 exists
        - dp[s] = True if sum s is achievable
        """
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Backwards for 0/1 knapsack (use each num once)
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]

# Time: O(n * sum), Space: O(sum)
```

---

### LC 494 - Target Sum ⭐

**Form:** 1 (Knapsack with +/- choices)

**Problem:** Assign + or - to each number to reach target sum.

**Template Modification:**
- Two choices per item: add or subtract
- Transform: if P = sum of positives, N = sum of negatives
- P - N = target, P + N = total → P = (target + total) / 2

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Form 1 (Transformed Knapsack):
        - Let P = sum of nums with +, N = sum with -
        - P - N = target, P + N = total
        - So P = (target + total) / 2
        - Problem becomes: count subsets with sum P
        """
        total = sum(nums)

        # Check feasibility
        if (target + total) % 2 == 1 or abs(target) > total:
            return 0

        new_target = (target + total) // 2

        # Count subsets with sum = new_target
        dp = [0] * (new_target + 1)
        dp[0] = 1

        for num in nums:
            for s in range(new_target, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[new_target]

# Time: O(n * target), Space: O(target)
```

---

### LC 279 - Perfect Squares ⭐

**Form:** 1 (Unbounded Knapsack)

**Problem:** Minimum perfect squares that sum to n.

**Template Modification:**
- "Coins" = perfect squares (1, 4, 9, 16, ...)
- Minimize count

```python
class Solution:
    def numSquares(self, n: int) -> int:
        """
        Form 1 (Unbounded Knapsack):
        - Items = perfect squares up to n
        - dp[i] = min squares to sum to i
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Generate all perfect squares <= n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        for sq in squares:
            for i in range(sq, n + 1):
                dp[i] = min(dp[i], dp[i - sq] + 1)

        return dp[n]

# Time: O(n * sqrt(n)), Space: O(n)
```

---

### LC 343 - Integer Break ⭐

**Form:** 1 (Unbounded selection of parts)

**Problem:** Break n into sum of integers, maximize product.

**Template Modification:**
- "Items" = integers 1 to n-1
- Can use each integer multiple times
- Maximize product

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Form 1 (Unbounded with product):
        - dp[i] = max product for integer i
        - For each j < i, try breaking as j * (i-j) or j * dp[i-j]

        Mathematical insight: Use as many 3s as possible
        """
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(1, i):
                # Either use (i-j) as is, or use dp[i-j] (break further)
                dp[i] = max(dp[i], j * max(i - j, dp[i - j]))

        return dp[n]

# Time: O(n²), Space: O(n)
# Optimal O(1): use 3s greedily
```

---

### LC 91 - Decode Ways ⭐

**Form:** 1 (Sequential decisions)

**Problem:** Count ways to decode digit string to letters.

**Template Modification:**
- At each position, decide: take 1 digit or 2 digits
- Constraint: valid codes are 1-26

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Form 1 (Sequential with constraints):
        - dp[i] = ways to decode s[0:i]
        - Choice: decode 1 digit or 2 digits
        - Constraints: no leading zeros, 2-digit ≤ 26
        """
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # dp[i] = ways to decode first i characters
        prev2, prev1 = 1, 1  # dp[0]=1, dp[1]=1 (if valid)

        for i in range(2, n + 1):
            curr = 0

            # Single digit decode (s[i-1])
            if s[i-1] != '0':
                curr += prev1

            # Two digit decode (s[i-2:i])
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1

# Time: O(n), Space: O(1)
```

---

### LC 368 - Largest Divisible Subset ⭐

**Form:** 1 + Form 2 hybrid (LIS variant with divisibility)

**Problem:** Find largest subset where every pair is divisible.

**Template Modification:**
- Sort array first
- LIS-style: dp[i] = largest subset ending at i
- Condition: nums[j] divides nums[i]

```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Form 1+2 Hybrid (LIS with divisibility):
        - Sort nums so if a divides b, a comes before b
        - dp[i] = size of largest divisible subset ending at i
        - Track parent to reconstruct
        """
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n

        max_size, max_idx = 1, 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            if dp[i] > max_size:
                max_size = dp[i]
                max_idx = i

        # Reconstruct
        result = []
        idx = max_idx
        while idx != -1:
            result.append(nums[idx])
            idx = parent[idx]

        return result[::-1]

# Time: O(n²), Space: O(n)
```

---

### LC 1626 - Best Team With No Conflicts ⭐

**Form:** 1 + Form 2 hybrid (LIS variant)

**Problem:** Select players where younger player can't have higher score.

**Template Modification:**
- Sort by (age, score)
- LIS on scores

```python
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        Form 1+2 (LIS variant):
        - Sort players by (age, score)
        - After sorting, if we pick subset in order, older always comes after
        - LIS-style: pick increasing scores
        """
        players = sorted(zip(ages, scores))
        n = len(players)

        # dp[i] = max score of team ending with player i
        dp = [0] * n

        for i in range(n):
            dp[i] = players[i][1]  # At minimum, team of just player i
            for j in range(i):
                # Can add player j before player i if score[j] <= score[i]
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        return max(dp)

# Time: O(n²), Space: O(n)
```

---

### LC 3186 - Maximum Total Damage With Spell Casting ⭐

**Form:** 1 (House Robber variant)

**Problem:** Can't use spells with damage d-2, d-1, d+1, d+2 together.

**Template Modification:**
- Group spells by damage value
- Similar to House Robber but skip ±2 instead of ±1

```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        """
        Form 1 (Extended House Robber):
        - Group by damage value, sum counts
        - Can't use damage d if using d-1, d-2, d+1, d+2
        - Sort unique damages, apply House Robber with skip-2 logic
        """
        from collections import Counter

        count = Counter(power)
        damages = sorted(count.keys())
        n = len(damages)

        if n == 0:
            return 0

        # dp[i] = max damage using damages[0..i]
        dp = [0] * n

        for i in range(n):
            # Option 1: Don't use this damage
            take_prev = dp[i-1] if i > 0 else 0

            # Option 2: Use this damage
            curr_damage = damages[i] * count[damages[i]]

            # Find latest damage we can use (< damages[i] - 2)
            j = i - 1
            while j >= 0 and damages[j] > damages[i] - 3:
                j -= 1

            use_curr = curr_damage + (dp[j] if j >= 0 else 0)

            dp[i] = max(take_prev, use_curr)

        return dp[-1]

# Time: O(n log n) with binary search optimization, Space: O(n)
```

---

## Form 2: Ending Form (LIS, Path Finding)

### Base Template

```python
def ending_form_template(arr):
    """
    Form 2: Ending Form DP

    dp[i] = best answer for subproblem ENDING at index i
    Transition: look at all valid j < i
    """
    n = len(arr)
    dp = [initial_value] * n

    for i in range(n):
        dp[i] = base_case(arr[i])
        for j in range(i):
            if valid_transition(j, i):
                dp[i] = best(dp[i], dp[j] + contribution(j, i))

    return best(dp)  # or dp[n-1] for path problems
```

---

### LC 300 - Longest Increasing Subsequence ⭐

**Form:** 2 (Classic Ending Form)

**Problem:** Find length of longest strictly increasing subsequence.

**Template Modification:**
- dp[i] = LIS length ending at index i
- Transition: find all j < i where nums[j] < nums[i]

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Form 2 (Ending Form):
        - dp[i] = length of LIS ending at index i
        - Transition: dp[i] = max(dp[j] + 1) for all j where nums[j] < nums[i]

        O(n²) solution shown; O(n log n) uses binary search
        """
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# Time: O(n²), Space: O(n)

    def lengthOfLIS_optimal(self, nums: List[int]) -> int:
        """O(n log n) using binary search on tails array"""
        from bisect import bisect_left

        tails = []
        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)
```

---

### LC 53 - Maximum Subarray ⭐

**Form:** 2 (Kadane's Algorithm)

**Problem:** Find contiguous subarray with maximum sum.

**Template Modification:**
- dp[i] = max sum subarray ending at i
- Transition: extend previous or start fresh

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Form 2 (Kadane's - Special Ending Form):
        - dp[i] = max sum of subarray ending at i
        - Transition: dp[i] = max(nums[i], dp[i-1] + nums[i])
        - Either start fresh at i, or extend from i-1

        Space optimized since we only need previous value
        """
        max_ending_here = nums[0]
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

# Time: O(n), Space: O(1)
```

---

### LC 152 - Maximum Product Subarray ⭐

**Form:** 2 (Modified Kadane's)

**Problem:** Find contiguous subarray with maximum product.

**Template Modification:**
- Track both max AND min ending at each position
- Negative × negative can become max

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Form 2 (Extended Kadane's for product):
        - Track max_prod and min_prod ending at each position
        - Why min? A negative min * negative current = large positive
        - Transition: consider current, max*current, min*current
        """
        max_prod = min_prod = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Current candidates: num alone, extend max, extend min
            candidates = (num, max_prod * num, min_prod * num)

            max_prod = max(candidates)
            min_prod = min(candidates)

            result = max(result, max_prod)

        return result

# Time: O(n), Space: O(1)
```

---

### LC 62 - Unique Paths ⭐

**Form:** 2 (Grid Path Counting)

**Problem:** Count paths from top-left to bottom-right (only right/down moves).

**Template Modification:**
- dp[i][j] = paths to reach cell (i, j)
- Transition: come from top or left

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Form 2 (Grid Ending Form):
        - dp[i][j] = number of paths to reach (i, j)
        - Transition: dp[i][j] = dp[i-1][j] + dp[i][j-1]

        Space optimized to O(n)
        """
        dp = [1] * n  # First row all 1s

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]  # top + left

        return dp[n-1]

# Time: O(m*n), Space: O(n)
```

---

### LC 120 - Triangle ⭐

**Form:** 2 (Path Sum)

**Problem:** Find minimum path sum from top to bottom of triangle.

**Template Modification:**
- dp[j] = min sum to reach position j in current row
- Process bottom-up for simpler logic

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Form 2 (Bottom-up path):
        - Start from bottom row
        - dp[j] = min path sum starting from position j
        - Transition: dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        """
        dp = triangle[-1][:]  # Start with bottom row

        # Process from second-to-last row upward
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]

# Time: O(n²), Space: O(n)
```

---

### LC 931 - Minimum Falling Path Sum ⭐

**Form:** 2 (Grid Path)

**Problem:** Minimum sum path from top to bottom, can move diagonally.

**Template Modification:**
- From (i, j) can go to (i+1, j-1), (i+1, j), (i+1, j+1)

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Form 2 (Grid path with diagonal):
        - dp[j] = min sum to reach column j in current row
        - Transition from row above: consider j-1, j, j+1
        """
        n = len(matrix)
        dp = matrix[0][:]

        for i in range(1, n):
            new_dp = [0] * n
            for j in range(n):
                # Min from above-left, above, above-right
                options = [dp[j]]
                if j > 0:
                    options.append(dp[j-1])
                if j < n - 1:
                    options.append(dp[j+1])
                new_dp[j] = matrix[i][j] + min(options)
            dp = new_dp

        return min(dp)

# Time: O(n²), Space: O(n)
```

---

### LC 55 - Jump Game ⭐

**Form:** 2 (Reachability)

**Problem:** Can you reach the last index?

**Template Modification:**
- Track farthest reachable position
- Greedy is optimal

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Form 2 (Greedy reachability):
        - Track max_reach = farthest index reachable
        - If current index > max_reach, impossible
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True

        return True

# Time: O(n), Space: O(1)
```

---

### LC 45 - Jump Game II ⭐

**Form:** 2 (BFS-style greedy)

**Problem:** Minimum jumps to reach end.

**Template Modification:**
- BFS on reachable positions
- Track jumps, current end, farthest reachable

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Form 2 (BFS-style):
        - Each "level" = all positions reachable with same number of jumps
        - Track current_end, farthest, jumps
        """
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0  # End of current jump range
        farthest = 0     # Farthest we can reach

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:  # Must jump now
                jumps += 1
                current_end = farthest

                if current_end >= len(nums) - 1:
                    break

        return jumps

# Time: O(n), Space: O(1)
```

---

### LC 329 - Longest Increasing Path in a Matrix ⭐

**Form:** 2 (DFS + Memoization)

**Problem:** Find longest increasing path in matrix.

**Template Modification:**
- dp[i][j] = longest path starting at (i, j)
- DFS with memoization

```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Form 2 (DFS + Memoization):
        - dp[i][j] = longest increasing path starting at (i, j)
        - DFS to all neighbors with larger values
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            dp[i][j] = 1
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dfs(ni, nj))

            return dp[i][j]

        return max(dfs(i, j) for i in range(m) for j in range(n))

# Time: O(m*n), Space: O(m*n)
```

---

### LC 354 - Russian Doll Envelopes ⭐

**Form:** 2 (2D LIS)

**Problem:** Max envelopes that can nest (both width and height smaller).

**Template Modification:**
- Sort by width ascending, height descending (for same width)
- LIS on heights

```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Form 2 (2D LIS):
        - Sort by width ascending, height DESCENDING (same width)
        - Why descending height? Prevents using same width twice
        - Then LIS on heights
        """
        from bisect import bisect_left

        # Sort by width asc, height desc
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # LIS on heights
        heights = [e[1] for e in envelopes]
        tails = []

        for h in heights:
            pos = bisect_left(tails, h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h

        return len(tails)

# Time: O(n log n), Space: O(n)
```

---

### LC 122 - Best Time to Buy and Sell Stock II ⭐

**Form:** 2 (State Machine)

**Problem:** Max profit with unlimited transactions.

**Template Modification:**
- State: holding stock or not
- Greedy: capture all upward movements

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Form 2 (Greedy/State Machine):
        - With unlimited transactions, capture every price increase
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

# Time: O(n), Space: O(1)
```

---

### LC 123 - Best Time to Buy and Sell Stock III ⭐

**Form:** 2 (State Machine with transaction count)

**Problem:** Max profit with at most 2 transactions.

**Template Modification:**
- Track 4 states: after 1st buy, 1st sell, 2nd buy, 2nd sell

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Form 2 (State Machine with k=2):
        - buy1 = max profit after 1st buy
        - sell1 = max profit after 1st sell
        - buy2 = max profit after 2nd buy
        - sell2 = max profit after 2nd sell
        """
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)           # Buy 1st
            sell1 = max(sell1, buy1 + price)   # Sell 1st
            buy2 = max(buy2, sell1 - price)    # Buy 2nd
            sell2 = max(sell2, buy2 + price)   # Sell 2nd

        return sell2

# Time: O(n), Space: O(1)
```

---

### LC 542 - 01 Matrix ⭐

**Form:** 2 (Multi-source BFS / DP)

**Problem:** Distance of each cell to nearest 0.

**Template Modification:**
- BFS from all 0s simultaneously
- Or DP: two passes (top-left, bottom-right)

```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Form 2 (Two-pass DP):
        - Pass 1: top-left to bottom-right
        - Pass 2: bottom-right to top-left
        """
        m, n = len(mat), len(mat[0])
        INF = float('inf')

        # Initialize: 0s stay 0, 1s become INF
        dp = [[0 if mat[i][j] == 0 else INF for j in range(n)] for i in range(m)]

        # Pass 1: top-left to bottom-right
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)

        # Pass 2: bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 1:
                    if i < m - 1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                    if j < n - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)

        return dp

# Time: O(m*n), Space: O(m*n)
```

---

### LC 787 - Cheapest Flights Within K Stops ⭐

**Form:** 2 (Bellman-Ford variant)

**Problem:** Cheapest path with at most k stops.

**Template Modification:**
- dp[k][node] = min cost to reach node with exactly k edges
- Bellman-Ford with k iterations

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Form 2 (Bellman-Ford with k iterations):
        - dp[i] = min cost to reach node i
        - Run k+1 relaxation rounds
        """
        INF = float('inf')
        dp = [INF] * n
        dp[src] = 0

        for _ in range(k + 1):
            new_dp = dp[:]
            for u, v, cost in flights:
                if dp[u] != INF:
                    new_dp[v] = min(new_dp[v], dp[u] + cost)
            dp = new_dp

        return dp[dst] if dp[dst] != INF else -1

# Time: O(k * E), Space: O(n)
```

---

### LC 975 - Odd Even Jump ⭐

**Form:** 2 (DP with monotonic stack)

**Problem:** Count indices from which you can reach end via odd/even jumps.

**Template Modification:**
- Precompute next valid jump positions using monotonic stack
- DP backwards

```python
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        """
        Form 2 (DP with precomputed jumps):
        - odd_jump[i] = can reach end starting with odd jump from i
        - even_jump[i] = can reach end starting with even jump from i
        - Precompute next positions using sorted order + stack
        """
        n = len(arr)

        def make_jump_indices(sorted_indices):
            result = [None] * n
            stack = []
            for i in sorted_indices:
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)
            return result

        # Indices sorted by value (odd jump: smallest >= current)
        sorted_inc = sorted(range(n), key=lambda i: (arr[i], i))
        # Indices sorted by -value (even jump: largest <= current)
        sorted_dec = sorted(range(n), key=lambda i: (-arr[i], i))

        next_odd = make_jump_indices(sorted_inc)
        next_even = make_jump_indices(sorted_dec)

        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True

        for i in range(n - 2, -1, -1):
            if next_odd[i] is not None:
                odd[i] = even[next_odd[i]]
            if next_even[i] is not None:
                even[i] = odd[next_even[i]]

        return sum(odd)

# Time: O(n log n), Space: O(n)
```

---

### LC 1537 - Get the Maximum Score ⭐

**Form:** 2 (Two-pointer DP)

**Problem:** Max score traversing two sorted arrays with shared values as bridges.

**Template Modification:**
- Process both arrays with two pointers
- At shared values, take max of both paths

```python
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Form 2 (Two-pointer):
        - Two sorted arrays, can switch at common values
        - Track sum on each path, switch at common points
        """
        MOD = 10**9 + 7
        i, j = 0, 0
        sum1, sum2 = 0, 0

        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and (j >= len(nums2) or nums1[i] < nums2[j]):
                sum1 += nums1[i]
                i += 1
            elif j < len(nums2) and (i >= len(nums1) or nums2[j] < nums1[i]):
                sum2 += nums2[j]
                j += 1
            else:  # nums1[i] == nums2[j]
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1

        return max(sum1, sum2) % MOD

# Time: O(n + m), Space: O(1)
```

---

## Form 3: Multi-Sequence DP (LCS, Edit Distance)

### Base Template

```python
def multi_sequence_template(s1, s2):
    """
    Form 3: Multi-Sequence DP

    dp[i][j] = answer for s1[0:i] and s2[0:j]
    Transitions based on matching/mismatching characters
    """
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases (often dp[0][j] and dp[i][0])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + match_value
            else:
                dp[i][j] = best(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + mismatch_cost)

    return dp[n][m]
```

---

### LC 1143 - Longest Common Subsequence ⭐

**Form:** 3 (Classic)

**Problem:** Length of LCS of two strings.

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Form 3 (Classic LCS):
        - dp[i][j] = LCS length for text1[0:i] and text2[0:j]
        - Match: dp[i-1][j-1] + 1
        - Mismatch: max(dp[i-1][j], dp[i][j-1])
        """
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]

# Time: O(n*m), Space: O(n*m) or O(min(n,m)) optimized
```

---

### LC 72 - Edit Distance ⭐

**Form:** 3 (with 3 operations)

**Problem:** Minimum operations (insert, delete, replace) to transform word1 to word2.

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Form 3 (Edit Distance):
        - dp[i][j] = min edits for word1[0:i] → word2[0:j]
        - Match: dp[i-1][j-1]
        - Insert: dp[i][j-1] + 1
        - Delete: dp[i-1][j] + 1
        - Replace: dp[i-1][j-1] + 1
        """
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base cases
        for i in range(n + 1):
            dp[i][0] = i  # Delete all
        for j in range(m + 1):
            dp[0][j] = j  # Insert all

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],      # Delete
                        dp[i][j-1],      # Insert
                        dp[i-1][j-1]     # Replace
                    )

        return dp[n][m]

# Time: O(n*m), Space: O(n*m)
```

---

### LC 712 - Minimum ASCII Delete Sum for Two Strings ⭐

**Form:** 3 (Edit Distance variant)

**Problem:** Min ASCII sum of deleted characters to make strings equal.

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Form 3 (Weighted Edit Distance):
        - dp[i][j] = min ASCII delete sum for s1[0:i] and s2[0:j]
        - Match: dp[i-1][j-1] (no deletion)
        - Delete from s1: dp[i-1][j] + ord(s1[i-1])
        - Delete from s2: dp[i][j-1] + ord(s2[j-1])
        """
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base cases
        for i in range(1, n + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]),
                        dp[i][j-1] + ord(s2[j-1])
                    )

        return dp[n][m]

# Time: O(n*m), Space: O(n*m)
```

---

### LC 10 - Regular Expression Matching ⭐⭐

**Form:** 3 (with special transitions for . and *)

**Problem:** Match string against regex with . and *.

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Form 3 (Regex Matching):
        - dp[i][j] = True if s[0:i] matches p[0:j]
        - '.': matches any single character
        - '*': matches zero or more of preceding character
        """
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # Base: empty string can match patterns like a*, a*b*, etc.
        for j in range(2, m + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j-1] == '*':
                    # Zero occurrences of preceding char
                    dp[i][j] = dp[i][j-2]
                    # One or more occurrences (if preceding matches)
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[n][m]

# Time: O(n*m), Space: O(n*m)
```

---

### LC 44 - Wildcard Matching ⭐⭐

**Form:** 3 (with * matching any sequence)

**Problem:** Match string against pattern with ? (single) and * (any sequence).

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Form 3 (Wildcard Matching):
        - '?': matches any single character
        - '*': matches any sequence (including empty)
        - Different from regex: * is independent, not tied to previous char
        """
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # Base: * can match empty string
        for j in range(1, m + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j-1] == '*':
                    # Match empty (dp[i][j-1]) or match one+ chars (dp[i-1][j])
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[n][m]

# Time: O(n*m), Space: O(n*m)
```

---

### LC 5 - Longest Palindromic Substring ⭐

**Form:** 3 adapted (string matched against its reverse)

**Problem:** Find longest palindromic substring.

**Template Modification:**
- dp[i][j] = True if s[i:j+1] is palindrome
- Alternative: Expand around center

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Form 3 Adapted (Substring as Interval):
        - dp[i][j] = True if s[i:j+1] is palindrome
        - Palindrome if s[i]==s[j] and inner is palindrome

        More efficient: Expand around center O(n²) or Manacher O(n)
        """
        n = len(s)
        if n < 2:
            return s

        start, max_len = 0, 1

        # Expand around center
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(n):
            # Odd length palindrome
            len1 = expand(i, i)
            # Even length palindrome
            len2 = expand(i, i + 1)

            curr_max = max(len1, len2)
            if curr_max > max_len:
                max_len = curr_max
                start = i - (curr_max - 1) // 2

        return s[start:start + max_len]

# Time: O(n²), Space: O(1)
```

---

### LC 647 - Palindromic Substrings ⭐

**Form:** 3 adapted (count all)

**Problem:** Count all palindromic substrings.

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Form 3 Adapted (Count):
        - Expand around each center
        - Count both odd and even length palindromes
        """
        n = len(s)
        count = 0

        def expand(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)      # Odd length
            expand(i, i + 1)  # Even length

        return count

# Time: O(n²), Space: O(1)
```

---

### LC 516 - Longest Palindromic Subsequence ⭐

**Form:** 3 (LCS with reverse)

**Problem:** Length of longest palindromic subsequence.

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Form 3 (LCS approach):
        - LPS(s) = LCS(s, reverse(s))
        - Or Interval DP approach
        """
        # Method 1: LCS with reverse
        n = len(s)
        rev = s[::-1]

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == rev[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][n]

# Time: O(n²), Space: O(n²)
```

---

## Form 4: Interval DP

### Base Template

```python
def interval_dp_template(arr):
    """
    Form 4: Interval DP

    dp[l][r] = answer for interval [l, r]
    Transition: try all split points k between l and r
    """
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    # Base case: single elements or length-2 intervals

    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            dp[l][r] = initial_value
            for k in range(l, r):
                dp[l][r] = best(dp[l][r], dp[l][k] + dp[k+1][r] + merge_cost(l, k, r))

    return dp[0][n-1]
```

---

### LC 131 - Palindrome Partitioning ⭐

**Form:** 4 (with backtracking for enumeration)

**Problem:** All ways to partition string into palindromes.

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Form 4 (Backtracking with DP preprocessing):
        - Precompute which substrings are palindromes
        - Backtrack to enumerate all valid partitions
        """
        n = len(s)

        # Precompute palindrome status
        is_palin = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_palin[i+1][j-1]):
                    is_palin[i][j] = True

        result = []

        def backtrack(start, path):
            if start == n:
                result.append(path[:])
                return

            for end in range(start, n):
                if is_palin[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return result

# Time: O(n * 2^n), Space: O(n²)
```

---

### LC 410 - Split Array Largest Sum ⭐⭐

**Form:** 4 / Binary Search on Answer

**Problem:** Split array into m subarrays minimizing largest sum.

**Note:** Can be solved with Form 4 DP O(n²m) or Binary Search O(n log sum)

```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Binary Search on Answer (more efficient):
        - Search for minimum largest sum
        - Check if we can split into k parts with max sum ≤ mid
        """
        def can_split(max_sum):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > max_sum:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return count <= k

        lo, hi = max(nums), sum(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

# Time: O(n log sum), Space: O(1)
```

---

### LC 241 - Different Ways to Add Parentheses ⭐

**Form:** 4 (Classic Interval with operators)

**Problem:** All possible results from different groupings of expression.

```python
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        Form 4 (Interval DP with memoization):
        - For each operator, split into left and right subexpressions
        - Combine results with operator
        """
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]

            # Base case: pure number
            if expr.isdigit() or (expr[0] == '-' and expr[1:].isdigit()):
                return [int(expr)]

            results = []
            for i, c in enumerate(expr):
                if c in '+-*':
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])

                    for l in left_results:
                        for r in right_results:
                            if c == '+':
                                results.append(l + r)
                            elif c == '-':
                                results.append(l - r)
                            else:
                                results.append(l * r)

            memo[expr] = results
            return results

        return compute(expression)

# Time: O(n * 2^n), Space: O(2^n) for results
```

---

### LC 85 - Maximal Rectangle ⭐⭐

**Form:** Special (Histogram DP using stack)

**Problem:** Largest rectangle in binary matrix.

**Note:** NOT classic interval DP. Uses histogram + monotonic stack.

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        NOT Form 4 - Uses histogram approach:
        - For each row, compute histogram heights
        - Apply "Largest Rectangle in Histogram" (LC 84)
        """
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        def largest_rectangle_histogram(heights):
            stack = []
            max_area = 0
            heights = heights + [0]

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

            return max_area

        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, largest_rectangle_histogram(heights))

        return max_area

# Time: O(m*n), Space: O(n)
```

---

### LC 221 - Maximal Square ⭐

**Form:** 2 adapted (DP on grid)

**Problem:** Largest square containing only 1s.

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Form 2 (Grid DP):
        - dp[i][j] = side length of largest square with bottom-right at (i,j)
        - Transition: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side

# Time: O(m*n), Space: O(m*n)
```

---

### LC 1277 - Count Square Submatrices with All Ones ⭐

**Form:** Same as LC 221

**Problem:** Count all square submatrices with all 1s.

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Same as Maximal Square but COUNT all squares.
        dp[i][j] = number of squares with bottom-right at (i,j)
        Answer = sum of all dp values
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    count += dp[i][j]

        return count

# Time: O(m*n), Space: O(m*n)
```

---

### LC 1326 - Minimum Number of Taps ⭐

**Form:** Greedy/Interval Coverage (not classic Form 4)

**Problem:** Minimum taps to water entire garden.

```python
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        NOT Form 4 - Interval coverage greedy:
        - Transform to intervals
        - Greedy coverage (like Jump Game II)
        """
        # Create intervals [start, end]
        max_reach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            max_reach[left] = max(max_reach[left], right)

        # Greedy interval coverage (Jump Game II style)
        taps = 0
        current_end = 0
        farthest = 0

        for i in range(n + 1):
            if i > farthest:
                return -1

            farthest = max(farthest, max_reach[i])

            if i == current_end and i < n:
                taps += 1
                current_end = farthest

        return taps

# Time: O(n), Space: O(n)
```

---

## Form 5: Game DP

### Base Template

```python
def game_dp_template(initial_state):
    """
    Form 5: Game DP

    dp[state] = True if current player can WIN from this state
    Win condition: can reach at least one losing state for opponent
    """
    memo = {}

    def can_win(state):
        if state in memo:
            return memo[state]

        if is_terminal(state):
            return terminal_result(state)

        for move in valid_moves(state):
            next_state = apply_move(state, move)
            if not can_win(next_state):  # Opponent loses
                memo[state] = True
                return True

        memo[state] = False  # All moves lead to opponent winning
        return False

    return can_win(initial_state)
```

---

### LC 486 - Predict the Winner ⭐

**Form:** 5 (Minimax)

**Problem:** Can player 1 win or tie picking from array ends?

```python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        """
        Form 5 (Minimax):
        - dp[i][j] = score difference (current player - opponent) for [i,j]
        - Pick left: nums[i] - dp[i+1][j]
        - Pick right: nums[j] - dp[i][j-1]
        - Player 1 wins if dp[0][n-1] >= 0
        """
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    nums[i] - dp[i+1][j],
                    nums[j] - dp[i][j-1]
                )

        return dp[0][n-1] >= 0

# Time: O(n²), Space: O(n²)
```

---

### LC 837 - New 21 Game ⭐

**Form:** 5 adapted (Probability DP)

**Problem:** Probability Alice has ≤ n points.

```python
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        Probability DP (not classic game):
        - dp[i] = probability of getting exactly i points
        - Use sliding window for efficiency
        """
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts

            if i < k:
                window_sum += dp[i]
            if i >= maxPts:
                window_sum -= dp[i - maxPts]

        return sum(dp[k:n+1])

# Time: O(n), Space: O(n)
```

---

## Special/Hybrid Problems

These problems don't fit neatly into the 5 forms or require combining multiple techniques.

---

### LC 42 - Trapping Rain Water ⭐⭐

**Form:** NOT DP - Two Pointers or Monotonic Stack

**Problem:** Calculate trapped water between bars.

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two Pointers approach (not DP):
        - Track left_max and right_max
        - Water at position = min(left_max, right_max) - height
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water

# Time: O(n), Space: O(1)
```

---

### LC 907 - Sum of Subarray Minimums ⭐

**Form:** Hybrid (DP + Monotonic Stack)

**Problem:** Sum of minimums of all subarrays.

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Monotonic Stack + Contribution counting:
        - For each element, count subarrays where it's the minimum
        - Use previous smaller and next smaller elements
        """
        MOD = 10**9 + 7
        n = len(arr)

        # Previous smaller (or equal) element
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # Next smaller element
        next_smaller = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate contribution of each element
        result = 0
        for i in range(n):
            left_count = i - prev_smaller[i]
            right_count = next_smaller[i] - i
            result = (result + arr[i] * left_count * right_count) % MOD

        return result

# Time: O(n), Space: O(n)
```

---

### LC 22 - Generate Parentheses ⭐

**Form:** Backtracking (not DP)

**Problem:** Generate all valid parentheses combinations.

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Backtracking (not typical DP):
        - Track open and close count
        - Add '(' if open < n
        - Add ')' if close < open
        """
        result = []

        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:
                result.append(s)
                return

            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return result

# Time: O(4^n / sqrt(n)), Space: O(n)
```

---

### LC 96 - Unique Binary Search Trees ⭐

**Form:** Catalan Numbers / Form 4 style

**Problem:** Count structurally unique BSTs with n nodes.

```python
class Solution:
    def numTrees(self, n: int) -> int:
        """
        Catalan Numbers (Form 4 style):
        - G(n) = sum(G(i-1) * G(n-i)) for i=1..n
        - G(i-1) = left subtrees, G(n-i) = right subtrees
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]

# Time: O(n²), Space: O(n)
```

---

### LC 124 - Binary Tree Maximum Path Sum ⭐⭐

**Form:** Tree DP (post-order)

**Problem:** Maximum path sum in binary tree.

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Tree DP:
        - For each node, calculate max path ending here (going down)
        - Update global max with path through this node
        """
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            # Max path sum from left/right (ignore negative)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Path through this node
            path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, path_sum)

            # Return max path ending here (can only go one direction)
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum

# Time: O(n), Space: O(h)
```

---

### LC 834 - Sum of Distances in Tree ⭐⭐

**Form:** Tree DP (Re-rooting)

**Problem:** Sum of distances from each node to all other nodes.

```python
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Re-rooting DP (two passes):
        1. DFS to compute count and distance sum for root
        2. DFS to propagate to all other roots
        """
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n  # Nodes in subtree
        result = [0] * n

        # Pass 1: Compute for root 0
        def dfs1(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    result[node] += result[child] + count[child]

        # Pass 2: Re-root to all nodes
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    # Moving root from node to child:
                    # - count[child] nodes get closer by 1
                    # - (n - count[child]) nodes get farther by 1
                    result[child] = result[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs1(0, -1)
        dfs2(0, -1)
        return result

# Time: O(n), Space: O(n)
```

---

### LC 818 - Race Car ⭐⭐

**Form:** BFS or DP with pruning

**Problem:** Minimum instructions to reach target position.

```python
class Solution:
    def racecar(self, target: int) -> int:
        """
        BFS approach (DP is also possible):
        - State: (position, speed)
        - Actions: A (accelerate), R (reverse)
        """
        from collections import deque

        queue = deque([(0, 1, 0)])  # position, speed, steps
        visited = {(0, 1)}

        while queue:
            pos, speed, steps = queue.popleft()

            # Accelerate
            new_pos = pos + speed
            new_speed = speed * 2

            if new_pos == target:
                return steps + 1

            # Prune: don't go too far past target
            if 0 < new_pos < 2 * target and (new_pos, new_speed) not in visited:
                visited.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, steps + 1))

            # Reverse
            new_speed = -1 if speed > 0 else 1
            if (pos, new_speed) not in visited:
                visited.add((pos, new_speed))
                queue.append((pos, new_speed, steps + 1))

        return -1

# Time: O(target * log(target)), Space: O(target * log(target))
```

---

### LC 898 - Bitwise ORs of Subarrays ⭐

**Form:** Special DP with set compression

**Problem:** Count distinct bitwise ORs of all subarrays.

```python
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        """
        Special DP:
        - Track all possible OR values ending at each position
        - Set size is bounded by number of bits (≤30)
        """
        result = set()
        prev = set()  # OR values ending at previous position

        for num in arr:
            # All ORs ending at current position
            curr = {num}
            for val in prev:
                curr.add(val | num)

            result.update(curr)
            prev = curr

        return len(result)

# Time: O(n * 30), Space: O(n * 30)
```

---

### LC 808 - Soup Servings ⭐

**Form:** Probability DP with pruning

**Problem:** Probability that soup A empties first.

```python
class Solution:
    def soupServings(self, n: int) -> float:
        """
        Probability DP with memoization:
        - For large n, probability approaches 1
        - Scale down by 25 to reduce state space
        """
        # For large n, P(A first) + 0.5*P(same) ≈ 1
        if n >= 5000:
            return 1.0

        n = (n + 24) // 25  # Scale down
        memo = {}

        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            if (a, b) in memo:
                return memo[(a, b)]

            # Four equally likely operations
            result = 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

            memo[(a, b)] = result
            return result

        return dp(n, n)

# Time: O(n²), Space: O(n²)
```

---

### LC 1483 - Kth Ancestor of a Tree Node ⭐⭐

**Form:** Binary Lifting (not typical DP)

**Problem:** Find kth ancestor in tree efficiently.

```python
class TreeAncestor:
    """
    Binary Lifting:
    - Precompute 2^j ancestors for all nodes
    - Answer query by decomposing k into powers of 2
    """

    def __init__(self, n: int, parent: List[int]):
        self.LOG = 20
        self.up = [[-1] * self.LOG for _ in range(n)]

        # Base case: 2^0 = 1st ancestor = parent
        for i in range(n):
            self.up[i][0] = parent[i]

        # Build: 2^j ancestor = 2^(j-1) ancestor's 2^(j-1) ancestor
        for j in range(1, self.LOG):
            for i in range(n):
                if self.up[i][j-1] != -1:
                    self.up[i][j] = self.up[self.up[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG):
            if k & (1 << j):
                node = self.up[node][j]
                if node == -1:
                    return -1
        return node

# Preprocessing: O(n log n)
# Query: O(log k)
```

---

### LC 2054 - Two Best Non-Overlapping Events ⭐

**Form:** Form 1 variant with binary search

**Problem:** Maximum value from at most 2 non-overlapping events.

```python
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
        Sort + Binary Search + Suffix Max:
        - Sort by start time
        - For each event, binary search for next non-overlapping
        - Track suffix max values
        """
        from bisect import bisect_left

        events.sort()
        n = len(events)

        # Suffix max: max value from events[i:]
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        starts = [e[0] for e in events]
        result = 0

        for start, end, val in events:
            # Just this event
            result = max(result, val)

            # This event + one non-overlapping event
            next_idx = bisect_left(starts, end + 1)
            if next_idx < n:
                result = max(result, val + suffix_max[next_idx])

        return result

# Time: O(n log n), Space: O(n)
```

---

### LC 2035 - Partition Array Into Two Arrays to Minimize Sum Difference ⭐⭐

**Form:** Meet in the Middle (not standard DP)

**Problem:** Split array into two equal-size parts, minimize sum difference.

```python
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        Meet in the Middle:
        - Split array into two halves
        - Enumerate all subsets of each half
        - Group by subset size, binary search for best match
        """
        from bisect import bisect_left

        n = len(nums) // 2
        total = sum(nums)

        # Left half subsets grouped by size
        left = [[] for _ in range(n + 1)]
        for mask in range(1 << n):
            size = bin(mask).count('1')
            subset_sum = sum(nums[i] for i in range(n) if mask & (1 << i))
            left[size].append(subset_sum)

        # Sort for binary search
        for i in range(n + 1):
            left[i].sort()

        # Right half: for each subset, find best match from left
        result = float('inf')

        for mask in range(1 << n):
            size = bin(mask).count('1')
            right_sum = sum(nums[n + i] for i in range(n) if mask & (1 << i))

            # Need left subset of size (n - size)
            left_size = n - size
            left_sums = left[left_size]

            # Want: left_sum + right_sum = total / 2
            # i.e., left_sum = total/2 - right_sum
            target = total // 2 - right_sum

            # Binary search for closest
            idx = bisect_left(left_sums, target)

            for i in [idx - 1, idx]:
                if 0 <= i < len(left_sums):
                    left_sum = left_sums[i]
                    part1 = left_sum + right_sum
                    part2 = total - part1
                    result = min(result, abs(part1 - part2))

        return result

# Time: O(2^(n/2) * n), Space: O(2^(n/2))
```

---

### LC 465 - Optimal Account Balancing ⭐⭐

**Form:** Bitmask DP

**Problem:** Minimum transactions to settle debts.

```python
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        Bitmask DP:
        - Compute net balance for each person
        - Find minimum subset that sums to 0
        - dp[mask] = min transactions for people in mask
        """
        from collections import defaultdict

        # Calculate net balances
        balance = defaultdict(int)
        for a, b, amount in transactions:
            balance[a] -= amount
            balance[b] += amount

        # Keep only non-zero balances
        debts = [b for b in balance.values() if b != 0]
        n = len(debts)

        if n == 0:
            return 0

        # dp[mask] = min transactions for subset mask
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        # sum[mask] = sum of debts in mask
        subset_sum = [0] * (1 << n)
        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    subset_sum[mask] += debts[i]

        # Find subsets that sum to 0
        for mask in range(1 << n):
            if subset_sum[mask] != 0:
                continue

            # Count people in mask
            count = bin(mask).count('1')
            dp[mask] = count - 1  # Can settle in count-1 transactions

            # Try all proper subsets
            sub = mask
            while sub > 0:
                if subset_sum[sub] == 0:
                    dp[mask] = min(dp[mask], dp[sub] + dp[mask ^ sub])
                sub = (sub - 1) & mask

        return dp[(1 << n) - 1]

# Time: O(3^n), Space: O(2^n)
```

---

### LC 2188 - Minimum Time to Finish the Race ⭐

**Form:** DP with precomputation

**Problem:** Minimum time to complete laps with tire changes.

```python
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        """
        DP with precomputation:
        - Precompute min time for x consecutive laps on same tire
        - DP: dp[i] = min time for i laps
        """
        # Precompute: min time for x laps without changing
        MAX_LAPS = 20  # After ~20 laps, changing is always better
        min_time_same_tire = [float('inf')] * MAX_LAPS

        for f, r in tires:
            time = 0
            lap_time = f
            for x in range(1, MAX_LAPS):
                time += lap_time
                if lap_time > changeTime + f:  # Better to change
                    break
                min_time_same_tire[x] = min(min_time_same_tire[x], time)
                lap_time *= r

        # DP: dp[i] = min time for i laps
        dp = [float('inf')] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            for x in range(1, min(i + 1, MAX_LAPS)):
                # Do x laps on same tire, then change (if not last segment)
                if i == x:
                    dp[i] = min(dp[i], dp[i - x] + min_time_same_tire[x])
                else:
                    dp[i] = min(dp[i], dp[i - x] + min_time_same_tire[x] + changeTime)

        return dp[numLaps]

# Time: O(numLaps * MAX_LAPS), Space: O(numLaps)
```

---

### LC 2616 - Minimize the Maximum Difference of Pairs ⭐

**Form:** Binary Search on Answer (NOT DP)

**Problem:** Select p pairs minimizing max difference.

```python
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        Binary Search on Answer:
        - Search for minimum max difference
        - Greedy check: can we form p pairs with max diff ≤ mid?
        """
        if p == 0:
            return 0

        nums.sort()

        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # Use both
                else:
                    i += 1  # Skip this one
            return count >= p

        lo, hi = 0, nums[-1] - nums[0]

        while lo < hi:
            mid = (lo + hi) // 2
            if can_form_pairs(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

# Time: O(n log(max_diff)), Space: O(1) excluding sort
```

---

### LC 3351 - Sum of Good Subsequences ⭐

**Form:** DP with hash map

**Problem:** Sum of all subsequences where adjacent elements differ by 1.

```python
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        """
        DP with hash map:
        - count[v] = number of good subsequences ending with value v
        - total[v] = sum of all elements in those subsequences
        """
        MOD = 10**9 + 7
        count = {}  # count[v] = number of subsequences ending with v
        total = {}  # total[v] = sum of elements in those subsequences

        result = 0

        for num in nums:
            # New subsequences ending at num
            new_count = 1  # Just num itself
            new_total = num

            # Extend from num-1
            if num - 1 in count:
                new_count = (new_count + count[num - 1]) % MOD
                new_total = (new_total + total[num - 1] + num * count[num - 1]) % MOD

            # Extend from num+1
            if num + 1 in count:
                new_count = (new_count + count[num + 1]) % MOD
                new_total = (new_total + total[num + 1] + num * count[num + 1]) % MOD

            # Add to result
            result = (result + new_total) % MOD

            # Update maps
            count[num] = (count.get(num, 0) + new_count) % MOD
            total[num] = (total.get(num, 0) + new_total) % MOD

        return result

# Time: O(n), Space: O(n)
```

---

### LC 3562 - Maximum Profit from Trading Stocks with Discounts ⭐⭐

**Form:** Tree DP (similar to House Robber III)

**Problem:** Max profit trading on tree where children give discounts.

```python
# Note: This is a complex tree DP problem
# Solution depends on exact problem constraints
# General approach: DFS returning (buy_here, skip_here) tuples
```

---

### LC 3751 - Total Waviness of Numbers in Range I

**Form:** Digit DP

**Problem:** Count "waviness" property across range.

```python
# Digit DP template:
# State: (position, tight, previous_digit, ...)
# Count numbers with specific digit patterns
```

---

## Problem Index

| # | Problem | Form | Difficulty | Key Technique |
|---|---------|------|------------|---------------|
| 5 | Longest Palindromic Substring | 3 | Medium | Expand around center |
| 10 | Regular Expression Matching | 3 | Hard | 2D DP with * handling |
| 22 | Generate Parentheses | - | Medium | Backtracking |
| 42 | Trapping Rain Water | - | Hard | Two pointers |
| 44 | Wildcard Matching | 3 | Hard | 2D DP |
| 45 | Jump Game II | 2 | Medium | BFS/Greedy |
| 53 | Maximum Subarray | 2 | Medium | Kadane's |
| 55 | Jump Game | 2 | Medium | Greedy |
| 62 | Unique Paths | 2 | Medium | Grid DP |
| 72 | Edit Distance | 3 | Medium | Classic 2D |
| 85 | Maximal Rectangle | 4 | Hard | Histogram + Stack |
| 91 | Decode Ways | 1 | Medium | Sequential DP |
| 96 | Unique Binary Search Trees | 4 | Medium | Catalan |
| 120 | Triangle | 2 | Medium | Bottom-up path |
| 122 | Best Time Buy/Sell II | 2 | Medium | Greedy |
| 123 | Best Time Buy/Sell III | 2 | Hard | State machine |
| 124 | Binary Tree Max Path Sum | - | Hard | Tree DP |
| 131 | Palindrome Partitioning | 4 | Medium | Backtrack + DP |
| 152 | Maximum Product Subarray | 2 | Medium | Track min/max |
| 198 | House Robber | 1 | Medium | Classic take/skip |
| 213 | House Robber II | 1 | Medium | Circular handling |
| 221 | Maximal Square | 2 | Medium | Grid DP |
| 241 | Different Ways Add Parens | 4 | Medium | Divide & conquer |
| 279 | Perfect Squares | 1 | Medium | Unbounded knapsack |
| 300 | Longest Increasing Subseq | 2 | Medium | Classic LIS |
| 322 | Coin Change | 1 | Medium | Unbounded knapsack |
| 329 | Longest Inc Path Matrix | 2 | Hard | DFS + memo |
| 337 | House Robber III | 1 | Medium | Tree DP |
| 343 | Integer Break | 1 | Medium | Math/DP |
| 354 | Russian Doll Envelopes | 2 | Hard | 2D LIS |
| 368 | Largest Divisible Subset | 1+2 | Medium | LIS variant |
| 410 | Split Array Largest Sum | 4/BS | Hard | Binary search |
| 416 | Partition Equal Subset Sum | 1 | Medium | 0/1 Knapsack |
| 465 | Optimal Account Balancing | - | Hard | Bitmask DP |
| 486 | Predict the Winner | 5 | Medium | Minimax |
| 494 | Target Sum | 1 | Medium | Transformed knapsack |
| 516 | Longest Palindromic Subseq | 3 | Medium | LCS with reverse |
| 518 | Coin Change II | 1 | Medium | Count combinations |
| 542 | 01 Matrix | 2 | Medium | Multi-source BFS |
| 647 | Palindromic Substrings | 3 | Medium | Expand center |
| 712 | Min ASCII Delete Sum | 3 | Medium | Weighted edit dist |
| 787 | Cheapest Flights K Stops | 2 | Medium | Bellman-Ford |
| 808 | Soup Servings | 5 | Medium | Probability DP |
| 818 | Race Car | - | Hard | BFS |
| 834 | Sum of Distances in Tree | - | Hard | Re-rooting |
| 837 | New 21 Game | 5 | Medium | Probability DP |
| 898 | Bitwise ORs Subarrays | - | Medium | Set compression |
| 907 | Sum of Subarray Minimums | - | Medium | Monotonic stack |
| 931 | Minimum Falling Path Sum | 2 | Medium | Grid path |
| 975 | Odd Even Jump | 2 | Hard | DP + monotonic stack |
| 1143 | Longest Common Subseq | 3 | Medium | Classic LCS |
| 1277 | Count Square Submatrices | 2 | Medium | Grid DP |
| 1326 | Min Taps to Water Garden | - | Hard | Greedy intervals |
| 1483 | Kth Ancestor Tree Node | - | Hard | Binary lifting |
| 1537 | Get Maximum Score | 2 | Hard | Two pointers |
| 1626 | Best Team No Conflicts | 1+2 | Medium | Sort + LIS |
| 2035 | Partition Min Sum Diff | - | Hard | Meet in middle |
| 2054 | Two Best Non-Overlap Events | 1 | Medium | Sort + binary search |
| 2188 | Min Time Finish Race | - | Hard | Precompute + DP |
| 2616 | Min Max Diff of Pairs | - | Medium | Binary search |
| 3186 | Max Damage Spell Casting | 1 | Medium | House Robber variant |
| 3351 | Sum of Good Subsequences | - | Hard | DP with hash |

---

## Summary: Form Selection Guide

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        WHEN TO USE WHICH FORM                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FORM 1 (Knapsack):                                                        │
│  • "Select items with constraint"                                          │
│  • "Can't take adjacent" → House Robber                                    │
│  • "Budget/capacity limit" → 0/1 or Unbounded Knapsack                     │
│  • "Partition into subsets" → Subset Sum                                   │
│                                                                             │
│  FORM 2 (Ending):                                                          │
│  • "Best/longest ending at position i"                                     │
│  • "Path from start to end"                                                │
│  • "Kadane's for contiguous subarrays"                                     │
│  • "LIS and variants"                                                      │
│                                                                             │
│  FORM 3 (Multi-Sequence):                                                  │
│  • "Two strings/arrays interacting"                                        │
│  • "LCS, Edit Distance"                                                    │
│  • "Pattern matching (regex, wildcard)"                                    │
│  • "Palindrome (string vs reverse)"                                        │
│                                                                             │
│  FORM 4 (Interval):                                                        │
│  • "Range [l, r] problems"                                                 │
│  • "Split into subproblems"                                                │
│  • "Matrix chain multiplication style"                                     │
│  • "Burst balloons, merge stones"                                          │
│                                                                             │
│  FORM 5 (Game):                                                            │
│  • "Two players, optimal play"                                             │
│  • "Win/Lose determination"                                                │
│  • "Minimax with score difference"                                         │
│                                                                             │
│  SPECIAL CASES:                                                            │
│  • Tree DP: Post-order traversal returning tuples                          │
│  • Digit DP: Count numbers with digit constraints                          │
│  • Bitmask DP: Small n (≤20) with subset states                           │
│  • Probability DP: Expected value calculations                             │
│  • Binary Search on Answer: When DP would be too slow                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```
