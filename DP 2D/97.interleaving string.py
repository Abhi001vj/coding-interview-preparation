# https://leetcode.com/problems/interleaving-string/description/
# ```python
# """
# SPACE-OPTIMIZED COMPLETE STRUCTURE ANALYSIS
# For nums = [1,1,1,1,1], target = 3

# Complete State Transitions with All Steps:

# Initial State:
# dp: {0: 1}            # Only one way to make 0 with no numbers

# First Number (1):
# Current dp: {0: 1}
# Computing next_dp:
# - From sum 0: Add 1  → next_dp[1] += 1
# - From sum 0: Sub 1  → next_dp[-1] += 1
# next_dp: {1: 1, -1: 1}
# After swap: dp = {1: 1, -1: 1}

# Second Number (1):
# Current dp: {1: 1, -1: 1}
# Computing next_dp:
# - From sum 1:  Add 1 → next_dp[2] += 1
# - From sum 1:  Sub 1 → next_dp[0] += 1
# - From sum -1: Add 1 → next_dp[0] += 1
# - From sum -1: Sub 1 → next_dp[-2] += 1
# next_dp: {2: 1, 0: 2, -2: 1}
# After swap: dp = {2: 1, 0: 2, -2: 1}

# Third Number (1):
# Current dp: {2: 1, 0: 2, -2: 1}
# Computing next_dp:
# - From sum 2:  Add 1 → next_dp[3] += 1
# - From sum 2:  Sub 1 → next_dp[1] += 1
# - From sum 0:  Add 1 → next_dp[1] += 2
# - From sum 0:  Sub 1 → next_dp[-1] += 2
# - From sum -2: Add 1 → next_dp[-1] += 1
# - From sum -2: Sub 1 → next_dp[-3] += 1
# next_dp: {3: 1, 1: 3, -1: 3, -3: 1}
# After swap: dp = {3: 1, 1: 3, -1: 3, -3: 1}

# Fourth Number (1):
# Current dp: {3: 1, 1: 3, -1: 3, -3: 1}
# Computing next_dp:
# - From sum 3:  Add 1 → next_dp[4] += 1
# - From sum 3:  Sub 1 → next_dp[2] += 1
# - From sum 1:  Add 1 → next_dp[2] += 3
# - From sum 1:  Sub 1 → next_dp[0] += 3
# - From sum -1: Add 1 → next_dp[0] += 3
# - From sum -1: Sub 1 → next_dp[-2] += 3
# - From sum -3: Add 1 → next_dp[-2] += 1
# - From sum -3: Sub 1 → next_dp[-4] += 1
# next_dp: {4: 1, 2: 4, 0: 6, -2: 4, -4: 1}
# After swap: dp = {4: 1, 2: 4, 0: 6, -2: 4, -4: 1}

# Fifth Number (1):
# Current dp: {4: 1, 2: 4, 0: 6, -2: 4, -4: 1}
# Computing next_dp:
# - From sum 4:  Add 1 → next_dp[5] += 1
# - From sum 4:  Sub 1 → next_dp[3] += 1
# - From sum 2:  Add 1 → next_dp[3] += 4
# - From sum 2:  Sub 1 → next_dp[1] += 4
# - From sum 0:  Add 1 → next_dp[1] += 6
# - From sum 0:  Sub 1 → next_dp[-1] += 6
# - From sum -2: Add 1 → next_dp[-1] += 4
# - From sum -2: Sub 1 → next_dp[-3] += 4
# - From sum -4: Add 1 → next_dp[-3] += 1
# - From sum -4: Sub 1 → next_dp[-5] += 1
# next_dp: {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1}
# After swap: dp = {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1}

# Final Result:
# dp[target] = dp[3] = 5 ways
# """

# def space_optimized_complete(nums: list[int], target: int) -> int:
#     dp = defaultdict(int)
#     dp[0] = 1
    
#     def print_state_transition(step: int, num: int, curr_dp: dict, next_dp: dict):
#         print(f"\nStep {step}: Processing number {num}")
#         print("Current dp state:")
#         for sum_val, count in sorted(curr_dp.items()):
#             print(f"  Sum {sum_val}: {count} ways")
#         print("Next dp state computations:")
#         for curr_sum, count in sorted(curr_dp.items()):
#             print(f"  From sum {curr_sum}:")
#             print(f"    Add {num} → next_dp[{curr_sum + num}] += {count}")
#             print(f"    Sub {num} → next_dp[{curr_sum - num}] += {count}")
#         print("Resulting next_dp:")
#         for sum_val, count in sorted(next_dp.items()):
#             print(f"  Sum {sum_val}: {count} ways")
    
#     for i, num in enumerate(nums, 1):
#         next_dp = defaultdict(int)
#         for curr_sum, count in dp.items():
#             next_dp[curr_sum + num] += count
#             next_dp[curr_sum - num] += count
#         print_state_transition(i, num, dp, next_dp)
#         dp = next_dp
    
#     return dp[target]

# # Test with example
# if __name__ == "__main__":
#     nums = [1,1,1,1,1]
#     target = 3
#     print(f"Finding number of ways to reach target {target} with nums {nums}")
#     result = space_optimized_complete(nums, target)
#     print(f"\nFinal result: {result} ways")
# ```

```python
"""
INTERLEAVING STRING PROBLEM ANALYSIS
----------------------------------
Example 1: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"

PATTERN IDENTIFICATION:
1. This is a string matching problem with DP characteristics
2. At each step, we can choose from either s1 or s2
3. Choices must maintain order within each string
4. Can be solved using either recursion + memoization or bottom-up DP

VISUALIZATION OF MATCHING PROCESS:
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

Matching visualization:
s1: a a b c c
s2: d b b c a
s3: a a d b b c b c a c
    1 1 2 2 2 1 2 1 2 1
    ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
Numbers indicate which string character came from (1=s1, 2=s2)

1. RECURSIVE SOLUTION WITH VISUALIZATION
--------------------------------------
Decision tree shows possible choices at each step:
"""

def recursive_solution(s1: str, s2: str, s3: str) -> bool:
    """
    Recursive solution showing all possible matching paths
    Time: O(2^(m+n)), Space: O(m+n) without memoization
    where m = len(s1), n = len(s2)
    """
    if len(s1) + len(s2) != len(s3):
        return False
        
    def backtrack(i1: int, i2: int, path: list = None) -> bool:
        if path is None:
            path = []
            
        i3 = i1 + i2  # Current position in s3
        
        # Base case: reached end of both strings
        if i3 == len(s3):
            print(f"Found valid interleaving: {path}")
            return True
            
        # Try taking from s1
        if i1 < len(s1) and s1[i1] == s3[i3]:
            if backtrack(i1 + 1, i2, path + [(s1[i1], 1)]):
                return True
                
        # Try taking from s2
        if i2 < len(s2) and s2[i2] == s3[i3]:
            if backtrack(i1, i2 + 1, path + [(s2[i2], 2)]):
                return True
                
        return False
        
    return backtrack(0, 0)

"""
2. MEMOIZED SOLUTION WITH STATE TRACKING
--------------------------------------
Key States:
(i1, i2) -> can we form s3[i1+i2:] using s1[i1:] and s2[i2:]

Complete state space for example:
"""

def memoized_solution(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
        
    dp = {}  # (i1, i2) -> bool
    
    def print_state(i1: int, i2: int, result: bool):
        i3 = i1 + i2
        print(f"State (i1={i1}, i2={i2}, i3={i3}):")
        print(f"  s1[i1:] = {s1[i1:] if i1 < len(s1) else ''}")
        print(f"  s2[i2:] = {s2[i2:] if i2 < len(s2) else ''}")
        print(f"  s3[i3:] = {s3[i3:]}")
        print(f"  Result: {result}")
    
    def dfs(i1: int, i2: int) -> bool:
        i3 = i1 + i2
        
        # Base case
        if i3 == len(s3):
            return True
            
        if (i1, i2) in dp:
            return dp[(i1, i2)]
            
        result = False
        # Try s1
        if i1 < len(s1) and s1[i1] == s3[i3]:
            result |= dfs(i1 + 1, i2)
        # Try s2
        if i2 < len(s2) and s2[i2] == s3[i3]:
            result |= dfs(i1, i2 + 1)
            
        dp[(i1, i2)] = result
        print_state(i1, i2, result)
        return result
        
    return dfs(0, 0)

"""
3. BOTTOM-UP DP SOLUTION WITH TABLE VISUALIZATION
---------------------------------------------
DP Table[i1][i2] represents: can we form s3[0:i1+i2] using s1[0:i1] and s2[0:i2]

For s1 = "aab", s2 = "abc", s3 = "aaabbc":
"""

def bottom_up_solution(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
        
    m, n = len(s1), len(s2)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    def print_dp_table():
        print("\nDP Table:")
        print("   ", end="")
        print("  ".join(["-"] + list(s2)))
        for i in range(m + 1):
            print(f"{s1[i-1] if i > 0 else '-'} ", end="")
            for j in range(n + 1):
                print("T " if dp[i][j] else "F ", end="")
            print()
    
    # Fill first row (using only s2)
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    
    # Fill first column (using only s1)
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    
    # Fill rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s3[i+j-1]:
                dp[i][j] |= dp[i-1][j]
            if s2[j-1] == s3[i+j-1]:
                dp[i][j] |= dp[i][j-1]
        print_dp_table()
    
    return dp[m][n]

"""
4. SPACE-OPTIMIZED SOLUTION
-------------------------
Observation: We only need previous row to compute current row
"""

def space_optimized_solution(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
        
    m, n = len(s1), len(s2)
    dp = [False] * (n + 1)
    dp[0] = True
    
    def print_current_state(i: int):
        print(f"\nAfter processing s1[{i-1}] = {s1[i-1]}:")
        print("Current dp state:", ["T" if x else "F" for x in dp])
    
    # Initialize first row
    for j in range(1, n + 1):
        dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
    
    # Process row by row
    for i in range(1, m + 1):
        dp[0] = dp[0] and s1[i-1] == s3[i-1]
        for j in range(1, n + 1):
            above = dp[j]
            left = dp[j-1]
            dp[j] = (above and s1[i-1] == s3[i+j-1]) or \
                    (left and s2[j-1] == s3[i+j-1])
        print_current_state(i)
    
    return dp[n]

def test_all_solutions():
    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac"),  # True
        ("aabcc", "dbbca", "aadbbbaccc"),  # False
        ("", "", ""),                       # True
        ("a", "b", "ab")                    # True
    ]
    
    for s1, s2, s3 in test_cases:
        print(f"\nTesting s1={s1}, s2={s2}, s3={s3}")
        print("1. Recursive:", recursive_solution(s1, s2, s3))
        print("2. Memoized:", memoized_solution(s1, s2, s3))
        print("3. Bottom-up:", bottom_up_solution(s1, s2, s3))
        print("4. Space-optimized:", space_optimized_solution(s1, s2, s3))

if __name__ == "__main__":
    test_all_solutions()
```
```python
"""
INTERLEAVING STRING COMPLETE VISUALIZATION
----------------------------------------
Example: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"

1. CHARACTER MATCHING VISUALIZATION:
   s1: a  a  b  c  c
       ↓  ↓  ↓  ↓  ↓
   s3: a  a  d  b  b  c  b  c  a  c
       ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑
   s2: d  b  b  c  a

2. COMPLETE DP TABLE EVOLUTION:
   Rows: characters from s1 (+ empty)
   Cols: characters from s2 (+ empty)
   
   Initial State:
      -  d  b  b  c  a
   -  T  F  F  F  F  F
   a  F  F  F  F  F  F
   a  F  F  F  F  F  F
   b  F  F  F  F  F  F
   c  F  F  F  F  F  F
   c  F  F  F  F  F  F

   After processing first row (empty from s1):
      -  d  b  b  c  a
   -  T  F  F  F  F  F
   a  T  F  F  F  F  F
   a  F  F  F  F  F  F
   b  F  F  F  F  F  F
   c  F  F  F  F  F  F
   c  F  F  F  F  F  F

   After processing 'a' from s1:
      -  d  b  b  c  a
   -  T  F  F  F  F  F
   a  T  T  F  F  F  F
   a  F  T  T  F  F  F
   b  F  F  T  T  F  F
   c  F  F  F  T  T  F
   c  F  F  F  F  T  T

3. STEP-BY-STEP DECISION TREE:
                                (0,0,-)
                    /                       \
            (1,0,a)                        (0,1,d)
          /         \                    /         \
    (2,0,aa)      (1,1,ad)         (1,1,da)    (0,2,db)
    /     \       /      \         /     \      /     \
   ...    ...   ...     ...     ...     ...   ...    ...

4. STATE TRANSITION VISUALIZATION:
   Each cell (i,j) represents attempt to match s3[i+j] using:
   - s1[i] from above cell
   - s2[j] from left cell
"""
```python
"""
COMPLETE INTERLEAVING STRING SOLUTIONS ANALYSIS
Example: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"

1. RECURSIVE SOLUTION BREAKDOWN
-----------------------------
Decision Tree Visualization:
                    (0,0,0)
                /            \
     (1,0,1)  a             d  (0,1,1)
        /    \               /        \
(2,0,2)a    (1,1,2)d   (1,1,2)a    (0,2,2)b
    /  \       /   \       /   \       /   \
   ...  ...   ...  ...   ...  ...    ...  ...

Each node format: (i, j, k) where:
- i: position in s1
- j: position in s2
- k: position in s3
"""

def recursive_with_trace(s1: str, s2: str, s3: str) -> bool:
    def print_state(i: int, j: int, k: int, src: str = None):
        print(f"\nChecking position:")
        print(f"s1[{i}]: {s1[i] if i < len(s1) else 'END'}")
        print(f"s2[{j}]: {s2[j] if j < len(s2) else 'END'}")
        print(f"s3[{k}]: {s3[k] if k < len(s3) else 'END'}")
        if src:
            print(f"Trying match from: {src}")
            
        # Visualize current match point
        s1_vis = list('.' * len(s1))
        s2_vis = list('.' * len(s2))
        s3_vis = list('.' * len(s3))
        if i < len(s1): s1_vis[i] = s1[i]
        if j < len(s2): s2_vis[j] = s2[j]
        if k < len(s3): s3_vis[k] = s3[k]
        
        print("\nCurrent state:")
        print(f"s1: {''.join(s1_vis)}")
        print(f"s2: {''.join(s2_vis)}")
        print(f"s3: {''.join(s3_vis)}")
    
    def dfs(i: int, j: int, k: int) -> bool:
        print_state(i, j, k)
        
        # Base case: reached end of s3
        if k == len(s3):
            result = (i == len(s1)) and (j == len(s2))
            print(f"Reached end, valid: {result}")
            return result
        
        # Try matching with s1
        if i < len(s1) and s1[i] == s3[k]:
            print_state(i, j, k, "s1")
            if dfs(i + 1, j, k + 1):
                return True
        
        # Try matching with s2
        if j < len(s2) and s2[j] == s3[k]:
            print_state(i, j, k, "s2")
            if dfs(i, j + 1, k + 1):
                return True
        
        print(f"No match found at i={i}, j={j}, k={k}")
        return False
    
    return dfs(0, 0, 0)

"""
2. MEMOIZED SOLUTION VISUALIZATION
--------------------------------
State table format:
dp[(i,j)] -> can we interleave s1[i:] and s2[j:] to form s3[i+j:]

Complete state evolution for "abc", "def", "adbecf":
Initial state:
   -  d  e  f
-  ?  ?  ?  ?
a  ?  ?  ?  ?
b  ?  ?  ?  ?
c  ?  ?  ?  ?

Final state:
   -  d  e  f
-  T  F  F  F
a  T  F  F  F
b  F  T  F  F
c  F  F  T  F
"""

def memoized_with_trace(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
        
    dp = {}
    
    def print_memo_state(i: int, j: int):
        print(f"\nMemo state after checking (i={i}, j={j}):")
        print("   " + " ".join(list("-" + s2)))
        for x in range(len(s1) + 1):
            row = [s1[x-1] if x > 0 else "-"]
            for y in range(len(s2) + 1):
                if (x,y) in dp:
                    row.append("T" if dp[(x,y)] else "F")
                else:
                    row.append("?")
            print(" ".join(row))
    
    def dfs(i: int, j: int, k: int) -> bool:
        # Base case
        if k == len(s3):
            return (i == len(s1)) and (j == len(s2))
            
        if (i,j) in dp:
            return dp[(i,j)]
        
        result = False
        # Try s1
        if i < len(s1) and s1[i] == s3[k]:
            result = dfs(i + 1, j, k + 1)
        # Try s2
        if not result and j < len(s2) and s2[j] == s3[k]:
            result = dfs(i, j + 1, k + 1)
            
        dp[(i,j)] = result
        print_memo_state(i, j)
        return result
        
    return dfs(0, 0, 0)

"""
3. BOTTOM-UP DP VISUALIZATION
---------------------------
DP Table Evolution:
Each cell dp[i][j] represents whether we can interleave
s1[0:i] and s2[0:j] to form s3[0:i+j]

For s1="ab", s2="cd", s3="acbd":

Initial:
     -  c  d
  -  T  F  F
  a  F  F  F
  b  F  F  F

After first row:
     -  c  d
  -  T  F  F
  a  T  F  F
  b  F  F  F

Final:
     -  c  d
  -  T  F  F
  a  T  T  F
  b  F  T  T
"""

def bottom_up_with_trace(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
        
    m, n = len(s1), len(s2)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[m][n] = True
    
    def print_dp_state(i: int, j: int, src: str = None):
        print(f"\nDP state after processing (i={i}, j={j})")
        if src:
            print(f"Matched from: {src}")
        print("   " + " ".join(list("-" + s2)))
        for x in range(m + 1):
            row = [s1[x-1] if x > 0 else "-"]
            row.extend("T" if dp[x][y] else "F" for y in range(n + 1))
            print(" ".join(row))
    
    # Fill DP table
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i < m and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True
                print_dp_state(i, j, "s1")
            if j < n and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True
                print_dp_state(i, j, "s2")
    
    return dp[0][0]

"""
4. SPACE OPTIMIZED VISUALIZATION
------------------------------
We only need to keep track of one row of the DP table.
For each position, we maintain the previous row's result
and current row's result.

Evolution for s1="ab", s2="cd", s3="acbd":

Initial dp:  [T, F, F]
Row 1 (a):   [T, T, F]
Row 2 (b):   [F, T, T]
"""

def space_optimized_with_trace(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    if n < m:
        return space_optimized_with_trace(s2, s1, s3)
    
    dp = [False] * (n + 1)
    dp[n] = True
    
    def print_current_state(i: int):
        print(f"\nProcessing row {i} (char: {s1[i] if i < m else 'END'}):")
        print("Current dp state:")
        print(" ".join("T" if x else "F" for x in dp))
    
    for i in range(m, -1, -1):
        print_current_state(i)
        nextDp = [False] * (n + 1)
        nextDp[n] = (i == m)
        
        for j in range(n - 1, -1, -1):
            match_s1 = i < m and s1[i] == s3[i + j] and dp[j]
            match_s2 = j < n and s2[j] == s3[i + j] and nextDp[j + 1]
            nextDp[j] = match_s1 or match_s2
            
            if match_s1 or match_s2:
                print(f"Match at j={j} using " + 
                      ("s1" if match_s1 else "s2"))
        
        dp = nextDp
    
    return dp[0]

def test_all_solutions():
    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac"),  # True
        ("abc", "def", "adbecf"),          # True
        ("a", "b", "ab"),                  # True
        ("", "", "")                       # True
    ]
    
    for s1, s2, s3 in test_cases:
        print(f"\nTesting s1={s1}, s2={s2}, s3={s3}")
        print("\n1. Recursive solution:")
        recursive_with_trace(s1, s2, s3)
        print("\n2. Memoized solution:")
        memoized_with_trace(s1, s2, s3)
        print("\n3. Bottom-up solution:")
        bottom_up_with_trace(s1, s2, s3)
        print("\n4. Space-optimized solution:")
        space_optimized_with_trace(s1, s2, s3)

if __name__ == "__main__":
    test_all_solutions()
```