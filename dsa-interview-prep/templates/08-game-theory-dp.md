# Game Theory DP (Minimax)

## Introduction

Game Theory DP handles two-player games where both players play optimally. The key insight is that when it's your turn, you maximize your advantage; when it's opponent's turn, they minimize your advantage. This leads to the "minimax" principle.

## Pattern Recognition

Use this pattern when you see:
- "Two players take turns"
- "Both play optimally"
- "Can player 1 win?"
- "Predict the winner"
- Players pick from ends of array
- Stone game variants
- Turn-based decision making

---

## Base Templates

### Template 1: Pick from Ends (Score Difference DP)

```python
def minimax_ends(nums):
    """
    Two players pick from either end, both play optimally.
    Returns True if player 1 can win or tie.

    dp[i][j] = score_diff (P1 - P2) for subarray [i,j]
               when it's CURRENT player's turn

    Key insight: Opponent's gain is my loss, so we SUBTRACT.
    """
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # Base case: single element
    for i in range(n):
        dp[i][i] = nums[i]

    # Fill for increasing lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Current player picks left or right
            pick_left = nums[i] - dp[i + 1][j]
            pick_right = nums[j] - dp[i][j - 1]
            dp[i][j] = max(pick_left, pick_right)

    return dp[0][n - 1] >= 0
```

### Template 2: Stone Game (Optimal Total Score)

```python
def stone_game_score(piles):
    """
    Two players pick piles from ends.
    Returns (alice_score, bob_score).
    """
    n = len(piles)
    # dp[i][j] = (alice_score, bob_score) for piles[i:j+1]
    dp = {}

    def solve(i, j, is_alice):
        if i > j:
            return (0, 0)

        if (i, j, is_alice) in dp:
            return dp[(i, j, is_alice)]

        left_a, left_b = solve(i + 1, j, not is_alice)
        right_a, right_b = solve(i, j - 1, not is_alice)

        if is_alice:
            # Alice picks, add to her score
            pick_left = (left_a + piles[i], left_b)
            pick_right = (right_a + piles[j], right_b)
            # Alice maximizes her score
            result = max(pick_left, pick_right, key=lambda x: x[0])
        else:
            # Bob picks, add to his score
            pick_left = (left_a, left_b + piles[i])
            pick_right = (right_a, right_b + piles[j])
            # Bob maximizes his score
            result = max(pick_left, pick_right, key=lambda x: x[1])

        dp[(i, j, is_alice)] = result
        return result

    return solve(0, n - 1, True)
```

### Template 3: Can I Win (Bitmask DP)

```python
def can_i_win(max_num, target):
    """
    Players pick from 1..max_num (no reuse), first to reach target wins.
    Use bitmask to represent used numbers.
    """
    if target <= 0:
        return True
    if (1 + max_num) * max_num // 2 < target:
        return False

    memo = {}

    def can_win(used_mask, total):
        if used_mask in memo:
            return memo[used_mask]

        for num in range(1, max_num + 1):
            bit = 1 << num
            if used_mask & bit:
                continue  # Already used

            # If this move wins, or opponent loses after this move
            if total + num >= target or not can_win(used_mask | bit, total + num):
                memo[used_mask] = True
                return True

        memo[used_mask] = False
        return False

    return can_win(0, 0)
```

---

## Key Insights

### Why Subtract in Minimax?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   dp[i][j] = MY_SCORE - OPPONENT_SCORE for range [i,j]             │
│                                                                     │
│   If I pick nums[i]:                                                │
│   • I gain nums[i]                                                 │
│   • Opponent plays optimally on [i+1, j]                           │
│   • Opponent's "advantage" from [i+1,j] becomes MY disadvantage    │
│   • So: nums[i] - dp[i+1][j]                                       │
│                                                                     │
│   Why subtract? Because dp[i+1][j] is from OPPONENT's perspective!│
│   Their positive = my negative.                                    │
│                                                                     │
│   Example: nums = [1, 5, 2]                                        │
│   dp[1][2] = 3 (opponent's view: pick 5, then 5-2 = 3)            │
│   If I pick nums[0]=1: my advantage = 1 - 3 = -2                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Filling Order for 2D DP

```
For length-based problems, fill by increasing length:

    j →
i   [0][1][2][3]
↓   [_][1][2][3]     Length 1 (diagonal)
    [_][_][2][3]     Length 2
    [_][_][_][3]     Length 3
                     Length 4

for length in range(1, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
```

---

## LeetCode Problems

### Problem 1: LC 486 - Predict the Winner

**Link:** [https://leetcode.com/problems/predict-the-winner/](https://leetcode.com/problems/predict-the-winner/)

**Problem:** Two players pick from ends. Can Player 1 win?

**Pattern:** Minimax with score difference

```python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # Base case: single element
        for i in range(n):
            dp[i][i] = nums[i]

        # Fill by increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j],
                               nums[j] - dp[i][j - 1])

        return dp[0][n - 1] >= 0
```

**Space Optimized (1D):**

```python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                dp[i] = max(nums[i] - dp[i + 1],
                            nums[i + length - 1] - dp[i])

        return dp[0] >= 0
```

**Complexity:** O(n²) time, O(n) space

---

### Problem 2: LC 877 - Stone Game

**Link:** [https://leetcode.com/problems/stone-game/](https://leetcode.com/problems/stone-game/)

**Problem:** Even number of piles, Alice first. Can Alice always win?

**Pattern:** Same as LC 486, but Alice always wins (math proof)!

**Math insight:** With even piles, Alice can always choose all odd-indexed or all even-indexed piles.

```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Alice always wins (can control odd/even indexed piles)
        return True
```

**DP Solution (same as 486):**

```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(piles[i] - dp[i + 1][j],
                               piles[j] - dp[i][j - 1])

        return dp[0][n - 1] > 0
```

**Complexity:** O(n²) or O(1)

---

### Problem 3: LC 1140 - Stone Game II

**Link:** [https://leetcode.com/problems/stone-game-ii/](https://leetcode.com/problems/stone-game-ii/)

**Problem:** Pick 1 to 2M piles, M updates to max(M, X). Return Alice's max stones.

**Pattern:** Minimax with suffix sum

```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # Suffix sums for quick range sum
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            """Max stones current player can get from piles[i:] with M=m"""
            if i >= n:
                return 0

            if (i, m) in memo:
                return memo[(i, m)]

            # If can take all remaining
            if i + 2 * m >= n:
                return suffix[i]

            best = 0
            for x in range(1, 2 * m + 1):
                # Take x piles, opponent gets optimal from rest
                opponent = dp(i + x, max(m, x))
                # I get: total remaining - what opponent gets
                best = max(best, suffix[i] - opponent)

            memo[(i, m)] = best
            return best

        return dp(0, 1)
```

**Complexity:** O(n³)

---

### Problem 4: LC 1406 - Stone Game III

**Link:** [https://leetcode.com/problems/stone-game-iii/](https://leetcode.com/problems/stone-game-iii/)

**Problem:** Pick 1, 2, or 3 stones from front. Return winner.

**Pattern:** Minimax with fixed choices

```python
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # Suffix sums
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + stoneValue[i]

        # dp[i] = max score difference (current - opponent) from index i
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            take = 0
            for k in range(1, 4):  # Take 1, 2, or 3
                if i + k > n:
                    break
                take += stoneValue[i + k - 1]
                dp[i] = max(dp[i], take - dp[i + k])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
```

**Complexity:** O(n)

---

### Problem 5: LC 464 - Can I Win

**Link:** [https://leetcode.com/problems/can-i-win/](https://leetcode.com/problems/can-i-win/)

**Problem:** Pick from 1..maxNum (no reuse), first to reach target wins.

**Pattern:** Bitmask DP for state

```python
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        total_sum = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if total_sum < desiredTotal:
            return False

        memo = {}

        def can_win(used, remaining):
            if used in memo:
                return memo[used]

            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << i
                if used & bit:
                    continue

                # Win if: this move reaches target, or opponent loses
                if i >= remaining or not can_win(used | bit, remaining - i):
                    memo[used] = True
                    return True

            memo[used] = False
            return False

        return can_win(0, desiredTotal)
```

**Complexity:** O(2^n * n)

---

### Problem 6: LC 294 - Flip Game II

**Link:** [https://leetcode.com/problems/flip-game-ii/](https://leetcode.com/problems/flip-game-ii/) (Premium)

**Problem:** Flip ++ to --, player who can't move loses.

**Pattern:** Minimax with string state

```python
class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = {}

        def can_win(s):
            if s in memo:
                return memo[s]

            for i in range(len(s) - 1):
                if s[i:i+2] == '++':
                    # Make move, check if opponent loses
                    new_state = s[:i] + '--' + s[i+2:]
                    if not can_win(new_state):
                        memo[s] = True
                        return True

            memo[s] = False
            return False

        return can_win(currentState)
```

**Complexity:** O(n * 2^n) worst case

---

### Problem 7: LC 1510 - Stone Game IV

**Link:** [https://leetcode.com/problems/stone-game-iv/](https://leetcode.com/problems/stone-game-iv/)

**Problem:** Remove perfect square stones. Player who can't move loses.

**Pattern:** DP on remaining stones

```python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] = True if current player wins with i stones
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            # Try all perfect square moves
            k = 1
            while k * k <= i:
                # If opponent loses after this move, I win
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1

        return dp[n]
```

**Complexity:** O(n√n)

---

### Problem 8: LC 1563 - Stone Game V

**Link:** [https://leetcode.com/problems/stone-game-v/](https://leetcode.com/problems/stone-game-v/)

**Problem:** Split stones, keep smaller half + its sum. Maximize Alice's score.

**Pattern:** Interval DP with prefix sums

```python
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def range_sum(i, j):
            return prefix[j + 1] - prefix[i]

        memo = {}

        def dp(i, j):
            if i >= j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            best = 0
            for k in range(i, j):
                left_sum = range_sum(i, k)
                right_sum = range_sum(k + 1, j)

                if left_sum < right_sum:
                    best = max(best, left_sum + dp(i, k))
                elif left_sum > right_sum:
                    best = max(best, right_sum + dp(k + 1, j))
                else:
                    best = max(best, left_sum + max(dp(i, k), dp(k + 1, j)))

            memo[(i, j)] = best
            return best

        return dp(0, n - 1)
```

**Complexity:** O(n³)

---

## Common Mistakes

1. **Forgetting whose turn it is**
   - Score difference DP handles this implicitly
   - Explicit turn tracking needs boolean parameter

2. **Wrong sign when subtracting**
   - `my_score - opponent_score` from current player's view
   - Opponent's DP value is subtracted, not added

3. **Base case errors**
   - Single element: current player takes it (dp[i][i] = nums[i])
   - Empty range: score is 0

4. **Filling order in 2D DP**
   - Must fill by increasing length
   - Can't fill row by row or column by column

5. **Bitmask overflow**
   - Use `1 << i` carefully
   - Check maxChoosableInteger <= 20 or so

---

## Practice Checklist

- [ ] LC 486 - Predict the Winner (Classic minimax)
- [ ] LC 877 - Stone Game (Math shortcut)
- [ ] LC 1140 - Stone Game II (Variable picks)
- [ ] LC 1406 - Stone Game III (Fixed picks)
- [ ] LC 464 - Can I Win (Bitmask)
- [ ] LC 294 - Flip Game II (String state)
- [ ] LC 1510 - Stone Game IV (Perfect squares)
- [ ] LC 1563 - Stone Game V (Split and keep)
