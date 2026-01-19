# Backtracking

## Introduction

Backtracking is a systematic way to explore all possible solutions by building candidates incrementally and abandoning a candidate ("backtracking") as soon as it's determined that it cannot lead to a valid solution. Think of it as DFS on a decision tree where each node represents a partial solution.

## Pattern Recognition

Use this pattern when you see:
- "Generate all permutations/combinations/subsets"
- "Find all valid configurations"
- "N-Queens, Sudoku solver"
- "Word search in grid"
- "All paths from source to target"
- "Partition into valid groups"
- Keywords: "all", "every", "generate", "enumerate"

---

## Base Templates

### Template 1: Subsets / Combinations

```python
def subsets(nums):
    """
    Generate all subsets.
    At each position, choose to include or not include.
    """
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Add current subset

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)  # Move to next index
            path.pop()  # Backtrack

    backtrack(0, [])
    return result
```

### Template 2: Permutations

```python
def permutations(nums):
    """
    Generate all permutations.
    At each position, try all unused elements.
    """
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result
```

### Template 3: Combination Sum (With Reuse)

```python
def combination_sum(candidates, target):
    """
    Find all combinations that sum to target.
    Same element can be used multiple times.
    """
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # Same i, can reuse
            path.pop()

    backtrack(0, [], target)
    return result
```

### Template 4: Grid Path Finding

```python
def find_paths(grid, start, end):
    """
    Find all paths in grid from start to end.
    """
    result = []
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def backtrack(r, c, path):
        if (r, c) == end:
            result.append(path[:])
            return

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                if (nr, nc) not in path:  # Avoid cycles
                    path.append((nr, nc))
                    backtrack(nr, nc, path)
                    path.pop()

    path = [start]
    backtrack(start[0], start[1], path)
    return result
```

---

## Key Insights

### The Backtracking Template

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   def backtrack(state):                                            │
│       if is_solution(state):                                       │
│           record_solution(state)                                   │
│           return                                                   │
│                                                                     │
│       for choice in get_choices(state):                           │
│           if is_valid(choice):                                    │
│               make_choice(choice)      # Modify state             │
│               backtrack(state)         # Recurse                  │
│               undo_choice(choice)      # Backtrack (restore)      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Subsets vs Permutations vs Combinations

| Type | Order Matters? | Start Index | Example |
|------|---------------|-------------|---------|
| Subsets | No | i + 1 | [1,2], [2,1] same |
| Permutations | Yes | 0 (use `used[]`) | [1,2] ≠ [2,1] |
| Combinations (k) | No | i + 1 | [1,2] = [2,1] |

### Handling Duplicates

```python
# Sort first, then skip duplicates at same level
nums.sort()
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i-1]:
        continue  # Skip duplicate at same level
```

---

## LeetCode Problems

### Problem 1: LC 78 - Subsets

**Link:** [https://leetcode.com/problems/subsets/](https://leetcode.com/problems/subsets/)

**Problem:** Generate all subsets of distinct integers.

**Pattern:** Include/exclude each element

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
```

**Complexity:** O(n * 2^n)

---

### Problem 2: LC 90 - Subsets II (With Duplicates)

**Link:** [https://leetcode.com/problems/subsets-ii/](https://leetcode.com/problems/subsets-ii/)

**Problem:** Generate all subsets, array may have duplicates.

**Pattern:** Sort + skip duplicates at same level

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                # Skip duplicates at same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
```

**Complexity:** O(n * 2^n)

---

### Problem 3: LC 46 - Permutations

**Link:** [https://leetcode.com/problems/permutations/](https://leetcode.com/problems/permutations/)

**Problem:** Generate all permutations of distinct integers.

**Pattern:** Use all elements, track used

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result
```

**Alternative: Swap-based**

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result
```

**Complexity:** O(n * n!)

---

### Problem 4: LC 47 - Permutations II (With Duplicates)

**Link:** [https://leetcode.com/problems/permutations-ii/](https://leetcode.com/problems/permutations-ii/)

**Problem:** Generate unique permutations of array with duplicates.

**Pattern:** Sort + skip if same as previous AND previous not used

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Skip duplicates: same value AND previous not used
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result
```

**Complexity:** O(n * n!)

---

### Problem 5: LC 39 - Combination Sum

**Link:** [https://leetcode.com/problems/combination-sum/](https://leetcode.com/problems/combination-sum/)

**Problem:** Find combinations that sum to target (can reuse elements).

**Pattern:** Stay at same index to allow reuse

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])  # Same i
                path.pop()

        backtrack(0, [], target)
        return result
```

**Complexity:** O(n^(target/min))

---

### Problem 6: LC 40 - Combination Sum II

**Link:** [https://leetcode.com/problems/combination-sum-ii/](https://leetcode.com/problems/combination-sum-ii/)

**Problem:** Find combinations (no reuse), array may have duplicates.

**Pattern:** Move to i+1 (no reuse) + skip duplicates

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])  # i + 1
                path.pop()

        backtrack(0, [], target)
        return result
```

**Complexity:** O(2^n)

---

### Problem 7: LC 79 - Word Search

**Link:** [https://leetcode.com/problems/word-search/](https://leetcode.com/problems/word-search/)

**Problem:** Find if word exists in grid (adjacent cells).

**Pattern:** Grid DFS with backtracking

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, idx):
            if idx == len(word):
                return True

            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[idx]):
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore neighbors
            found = (backtrack(r + 1, c, idx + 1) or
                     backtrack(r - 1, c, idx + 1) or
                     backtrack(r, c + 1, idx + 1) or
                     backtrack(r, c - 1, idx + 1))

            # Restore
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
```

**Complexity:** O(m * n * 4^L) where L = word length

---

### Problem 8: LC 51 - N-Queens

**Link:** [https://leetcode.com/problems/n-queens/](https://leetcode.com/problems/n-queens/)

**Problem:** Place n queens on n×n board so no two attack each other.

**Pattern:** Row-by-row placement, check column/diagonals

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        def backtrack(row, queens):
            if row == n:
                board = []
                for r, c in sorted(queens):
                    board.append('.' * c + 'Q' + '.' * (n - c - 1))
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                queens.append((row, col))

                backtrack(row + 1, queens)

                queens.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0, [])
        return result
```

**Complexity:** O(n!)

---

### Problem 9: LC 131 - Palindrome Partitioning

**Link:** [https://leetcode.com/problems/palindrome-partitioning/](https://leetcode.com/problems/palindrome-partitioning/)

**Problem:** Partition string into all palindrome substrings.

**Pattern:** Try all partition points, validate palindrome

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result
```

**Complexity:** O(n * 2^n)

---

### Problem 10: LC 17 - Letter Combinations of a Phone Number

**Link:** [https://leetcode.com/problems/letter-combinations-of-a-phone-number/](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

**Problem:** Generate all letter combinations from phone digits.

**Pattern:** Cartesian product via backtracking

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def backtrack(idx, path):
            if idx == len(digits):
                result.append(''.join(path))
                return

            for char in phone[digits[idx]]:
                path.append(char)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])
        return result
```

**Complexity:** O(4^n) where n = digits length

---

## Common Mistakes

1. **Forgetting to make a copy when adding to result**
   - Use `path[:]` or `list(path)`, not just `path`

2. **Not restoring state after backtracking**
   - Every `path.append()` needs corresponding `path.pop()`

3. **Wrong duplicate handling**
   - For subsets: `i > start and nums[i] == nums[i-1]`
   - For permutations: need `used` array check too

4. **Infinite recursion**
   - Missing base case
   - Not advancing state (e.g., using `i` instead of `i+1`)

5. **Modifying input during grid search**
   - Must restore original value after backtracking

---

## Practice Checklist

- [ ] LC 78 - Subsets (Basic)
- [ ] LC 90 - Subsets II (Duplicates)
- [ ] LC 46 - Permutations (Basic)
- [ ] LC 47 - Permutations II (Duplicates)
- [ ] LC 39 - Combination Sum (Reuse allowed)
- [ ] LC 40 - Combination Sum II (No reuse + duplicates)
- [ ] LC 79 - Word Search (Grid backtracking)
- [ ] LC 51 - N-Queens (Classic constraint)
- [ ] LC 131 - Palindrome Partitioning (String partition)
- [ ] LC 17 - Letter Combinations (Cartesian product)
