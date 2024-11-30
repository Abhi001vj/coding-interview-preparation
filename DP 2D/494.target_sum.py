# https://leetcode.com/problems/target-sum/description/
# 494. Target Sum
# Medium
# Topics
# Companies
# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
```python
"""
TARGET SUM ANALYSIS
Input: nums = [1,1,1,1,1], target = 3
Output: 5 (number of ways)

1. RECURSIVE SOLUTION VISUALIZATION
---------------------------------
First three levels of the decision tree:

                                (i=0, sum=0)
                        /                        \
               +1 (1,1)                         -1 (1,-1)
            /           \                     /            \
    +1 (2,2)           -1 (2,0)      +1 (2,0)           -1 (2,-2)
    /      \           /      \       /      \           /       \
+1(3,3)  -1(3,1) +1(3,1)  -1(3,-1) +1(3,1) -1(3,-1) +1(3,-1) -1(3,-3)
...        ...     ...      ...      ...     ...      ...       ...

The 5 paths that reach target=3:
1. [+1, +1, +1, +1, -1] = 3
2. [+1, +1, +1, -1, +1] = 3
3. [+1, +1, -1, +1, +1] = 3
4. [+1, -1, +1, +1, +1] = 3
5. [-1, +1, +1, +1, +1] = 3
"""

def recursive_solution(nums: list[int], target: int) -> int:
    def backtrack(i: int, total: int, path: list = None) -> int:
        if path is None:
            path = []
            
        # Base case: reached end of array
        if i == len(nums):
            if total == target:
                print(f"Found valid path: {path} = {total}")
                return 1
            return 0
            
        # Try adding current number
        ways = backtrack(i + 1, total + nums[i], path + [f"+{nums[i]}"])
        # Try subtracting current number
        ways += backtrack(i + 1, total - nums[i], path + [f"-{nums[i]}"])
        
        return ways
        
    return backtrack(0, 0)

"""
2. MEMOIZATION (TOP-DOWN DP)
---------------------------
Memo table evolution for key states:

Initial: {}

After first level:
(0,0) -> 5    # Start state leads to 5 ways
(1,1) -> 4    # After adding first 1
(1,-1) -> 1   # After subtracting first 1

Middle states:
(2,2) -> 3    # Two +1s
(2,0) -> 2    # +1,-1 or -1,+1
(2,-2) -> 0   # Two -1s

Final level states:
(4,3) -> 1    # One way to reach target
(4,1) -> 0    # Can't reach target
(4,-1) -> 0   # Can't reach target
"""

def memoized_solution(nums: list[int], target: int) -> int:
    dp = {}  # (index, total) -> number of ways
    
    def print_memo_state(i: int, total: int):
        print(f"\nState at (i={i}, total={total}):")
        for (idx, sum_val), ways in sorted(dp.items()):
            print(f"dp[{idx},{sum_val}] = {ways}")
    
    def backtrack(i: int, total: int) -> int:
        if i == len(nums):
            return 1 if total == target else 0
            
        if (i, total) in dp:
            return dp[(i, total)]
            
        dp[(i, total)] = (backtrack(i + 1, total + nums[i]) + 
                         backtrack(i + 1, total - nums[i]))
        print_memo_state(i, total)
        return dp[(i, total)]
    
    return backtrack(0, 0)

"""
3. BOTTOM-UP DP
--------------
State evolution by level:

Level 0: {0: 1}
Initial state, only one way to make sum 0

Level 1: {1: 1, -1: 1}
After processing first 1

Level 2: {2: 1, 0: 2, -2: 1}
After processing second 1

Level 3: {3: 1, 1: 3, -1: 3, -3: 1}
After processing third 1

Level 4: {4: 1, 2: 4, 0: 6, -2: 4, -4: 1}
After processing fourth 1

Level 5: {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1}
Final state, answer is dp[5][3] = 5
"""

def bottom_up_solution(nums: list[int], target: int) -> int:
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n + 1)]
    dp[0][0] = 1
    
    def print_level(i: int):
        print(f"\nLevel {i}:")
        for sum_val, count in sorted(dp[i].items()):
            print(f"Sum {sum_val}: {count} ways")
    
    for i in range(n):
        for curr_sum, count in dp[i].items():
            dp[i + 1][curr_sum + nums[i]] += count
            dp[i + 1][curr_sum - nums[i]] += count
        print_level(i + 1)
    
    return dp[n][target]

"""
4. SPACE-OPTIMIZED SOLUTION
-------------------------
State evolution processing each number:

Initial: {0: 1}

After 1st 1:
{-1: 1, 1: 1}

After 2nd 1:
{-2: 1, 0: 2, 2: 1}

After 3rd 1:
{-3: 1, -1: 3, 1: 3, 3: 1}

After 4th 1:
{-4: 1, -2: 4, 0: 6, 2: 4, 4: 1}

After 5th 1:
{-5: 1, -3: 5, -1: 10, 1: 10, 3: 5, 5: 1}
                           ^
                        Target value = 3
                        Answer = 5 ways
"""

def optimized_solution(nums: list[int], target: int) -> int:
    dp = defaultdict(int)
    dp[0] = 1
    
    def print_state(num: int):
        print(f"\nAfter processing {num}:")
        for sum_val, count in sorted(dp.items()):
            print(f"Sum {sum_val}: {count} ways")
    
    for num in nums:
        next_dp = defaultdict(int)
        for curr_sum, count in dp.items():
            next_dp[curr_sum + num] += count
            next_dp[curr_sum - num] += count
        dp = next_dp
        print_state(num)
    
    return dp[target]

# Test all solutions
def test_solutions():
    nums = [1,1,1,1,1]
    target = 3
    
    print(f"Testing with nums={nums}, target={target}")
    print("\n1. Recursive solution with all paths:")
    print("Ways:", recursive_solution(nums, target))
    
    print("\n2. Memoized solution with state evolution:")
    print("Ways:", memoized_solution(nums, target))
    
    print("\n3. Bottom-up solution with level-by-level build:")
    print("Ways:", bottom_up_solution(nums, target))
    
    print("\n4. Space-optimized solution with state tracking:")
    print("Ways:", optimized_solution(nums, target))

if __name__ == "__main__":
    test_solutions()
```
```python
"""
BOTTOM-UP DP COMPLETE STRUCTURE ANALYSIS
For nums = [1,1,1,1,1], target = 3

Outer DP Array Structure: dp[i] where i is the level/index
Inner Dictionary Structure: dp[i][sum] where sum is the running total

Complete Structure Visualization:

dp = [
    {                   # Level 0 (Initial)
        0: 1           # Only one way to make 0 with no numbers
    },
    {                   # Level 1 (After first 1)
        1: 1,          # Using +1
        -1: 1          # Using -1
    },
    {                   # Level 2 (After second 1)
        2: 1,          # +1 +1
        0: 2,          # +1 -1 and -1 +1
        -2: 1          # -1 -1
    },
    {                   # Level 3 (After third 1)
        3: 1,          # +1 +1 +1
        1: 3,          # +1 +1 -1, +1 -1 +1, -1 +1 +1
        -1: 3,         # +1 -1 -1, -1 +1 -1, -1 -1 +1
        -3: 1          # -1 -1 -1
    },
    {                   # Level 4 (After fourth 1)
        4: 1,          # All +1s
        2: 4,          # Three +1s, one -1
        0: 6,          # Two +1s, two -1s
        -2: 4,         # One +1, three -1s
        -4: 1          # All -1s
    },
    {                   # Level 5 (Final)
        5: 1,          # All +1s
        3: 5,          # Four +1s, one -1 (TARGET)
        1: 10,         # Three +1s, two -1s
        -1: 10,        # Two +1s, three -1s
        -3: 5,         # One +1, four -1s
        -5: 1          # All -1s
    }
]
"""

def bottom_up_detailed(nums: list[int], target: int) -> int:
    n = len(nums)
    # Initialize array of dictionaries
    dp = [defaultdict(int) for _ in range(n + 1)]
    
    # Base case explanation:
    # dp[0][0] = 1 because:
    # 1. With 0 numbers, we can only make sum of 0
    # 2. There's exactly one way to do this (empty selection)
    # 3. All other sums at level 0 are impossible (default to 0)
    dp[0][0] = 1
    
    def print_detailed_state(i: int):
        print(f"\nLevel {i} complete state:")
        print(f"dp[{i}] = {{")
        for sum_val, count in sorted(dp[i].items()):
            paths = get_paths_for_sum(i, sum_val)
            print(f"    {sum_val}: {count} ways {paths}")
        print("}")
    
    def get_paths_for_sum(level: int, target_sum: int) -> str:
        """Helper function to show paths that lead to each sum"""
        if level == 0:
            return "[]"
        paths = []
        # This is a simplified version - in practice, would need recursion
        # to find all actual paths
        return f"(paths omitted for clarity)"
    
    # Fill the dp array
    for i in range(n):
        for curr_sum, count in dp[i].items():
            # Add current number
            dp[i + 1][curr_sum + nums[i]] += count
            # Subtract current number
            dp[i + 1][curr_sum - nums[i]] += count
        print_detailed_state(i + 1)
    
    return dp[n][target]
```python
"""
SPACE-OPTIMIZED COMPLETE STRUCTURE ANALYSIS
For nums = [1,1,1,1,1], target = 3

Complete State Transitions with All Steps:

Initial State:
dp: {0: 1}            # Only one way to make 0 with no numbers

First Number (1):
Current dp: {0: 1}
Computing next_dp:
- From sum 0: Add 1  → next_dp[1] += 1
- From sum 0: Sub 1  → next_dp[-1] += 1
next_dp: {1: 1, -1: 1}
After swap: dp = {1: 1, -1: 1}

Second Number (1):
Current dp: {1: 1, -1: 1}
Computing next_dp:
- From sum 1:  Add 1 → next_dp[2] += 1
- From sum 1:  Sub 1 → next_dp[0] += 1
- From sum -1: Add 1 → next_dp[0] += 1
- From sum -1: Sub 1 → next_dp[-2] += 1
next_dp: {2: 1, 0: 2, -2: 1}
After swap: dp = {2: 1, 0: 2, -2: 1}

Third Number (1):
Current dp: {2: 1, 0: 2, -2: 1}
Computing next_dp:
- From sum 2:  Add 1 → next_dp[3] += 1
- From sum 2:  Sub 1 → next_dp[1] += 1
- From sum 0:  Add 1 → next_dp[1] += 2
- From sum 0:  Sub 1 → next_dp[-1] += 2
- From sum -2: Add 1 → next_dp[-1] += 1
- From sum -2: Sub 1 → next_dp[-3] += 1
next_dp: {3: 1, 1: 3, -1: 3, -3: 1}
After swap: dp = {3: 1, 1: 3, -1: 3, -3: 1}

Fourth Number (1):
Current dp: {3: 1, 1: 3, -1: 3, -3: 1}
Computing next_dp:
- From sum 3:  Add 1 → next_dp[4] += 1
- From sum 3:  Sub 1 → next_dp[2] += 1
- From sum 1:  Add 1 → next_dp[2] += 3
- From sum 1:  Sub 1 → next_dp[0] += 3
- From sum -1: Add 1 → next_dp[0] += 3
- From sum -1: Sub 1 → next_dp[-2] += 3
- From sum -3: Add 1 → next_dp[-2] += 1
- From sum -3: Sub 1 → next_dp[-4] += 1
next_dp: {4: 1, 2: 4, 0: 6, -2: 4, -4: 1}
After swap: dp = {4: 1, 2: 4, 0: 6, -2: 4, -4: 1}

Fifth Number (1):
Current dp: {4: 1, 2: 4, 0: 6, -2: 4, -4: 1}
Computing next_dp:
- From sum 4:  Add 1 → next_dp[5] += 1
- From sum 4:  Sub 1 → next_dp[3] += 1
- From sum 2:  Add 1 → next_dp[3] += 4
- From sum 2:  Sub 1 → next_dp[1] += 4
- From sum 0:  Add 1 → next_dp[1] += 6
- From sum 0:  Sub 1 → next_dp[-1] += 6
- From sum -2: Add 1 → next_dp[-1] += 4
- From sum -2: Sub 1 → next_dp[-3] += 4
- From sum -4: Add 1 → next_dp[-3] += 1
- From sum -4: Sub 1 → next_dp[-5] += 1
next_dp: {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1}
After swap: dp = {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1}

Final Result:
dp[target] = dp[3] = 5 ways
"""

def space_optimized_complete(nums: list[int], target: int) -> int:
    dp = defaultdict(int)
    dp[0] = 1
    
    def print_state_transition(step: int, num: int, curr_dp: dict, next_dp: dict):
        print(f"\nStep {step}: Processing number {num}")
        print("Current dp state:")
        for sum_val, count in sorted(curr_dp.items()):
            print(f"  Sum {sum_val}: {count} ways")
        print("Next dp state computations:")
        for curr_sum, count in sorted(curr_dp.items()):
            print(f"  From sum {curr_sum}:")
            print(f"    Add {num} → next_dp[{curr_sum + num}] += {count}")
            print(f"    Sub {num} → next_dp[{curr_sum - num}] += {count}")
        print("Resulting next_dp:")
        for sum_val, count in sorted(next_dp.items()):
            print(f"  Sum {sum_val}: {count} ways")
    
    for i, num in enumerate(nums, 1):
        next_dp = defaultdict(int)
        for curr_sum, count in dp.items():
            next_dp[curr_sum + num] += count
            next_dp[curr_sum - num] += count
        print_state_transition(i, num, dp, next_dp)
        dp = next_dp
    
    return dp[target]

# Test with example
if __name__ == "__main__":
    nums = [1,1,1,1,1]
    target = 3
    print(f"Finding number of ways to reach target {target} with nums {nums}")
    result = space_optimized_complete(nums, target)
    print(f"\nFinal result: {result} ways")
```
```python
"""
PROBLEM: Target Sum [LeetCode 494]
Input: nums = [1,1,1,1,1], target = 3
Output: 5

Lets analyze each solution with example nums=[1,2,1], target=0:

1. RECURSIVE SOLUTION
------------------
Decision Tree Visualization:
                              (i=0, total=0)
                        /                       \
                +1 (1,1)                      -1 (1,-1)
               /         \                   /          \
        +2 (2,3)    -2 (2,-1)        +2 (2,1)     -2 (2,-3)
        /     \      /     \         /     \       /      \
   +1(3,4) -1(3,2) +1(3,0) -1(3,-2) +1(3,2) -1(3,0) +1(3,-2) -1(3,-4)

"""

class Solution:
    def findTargetSumWays_recursive(self, nums: list[int], target: int) -> int:
        """
        Recursive solution breakdown for nums=[1,2,1]
        
        Call Stack Trace:
        backtrack(0, 0)
            ├── backtrack(1, 1)    # Add +1
            │   ├── backtrack(2, 3)    # Add +2
            │   │   ├── backtrack(3, 4)    # Add +1
            │   │   └── backtrack(3, 2)    # Add -1
            │   └── backtrack(2, -1)   # Add -2
            │       ├── backtrack(3, 0)    # Add +1
            │       └── backtrack(3, -2)   # Add -1
            └── backtrack(1, -1)   # Add -1
                ├── backtrack(2, 1)    # Add +2
                │   ├── backtrack(3, 2)    # Add +1
                │   └── backtrack(3, 0)    # Add -1
                └── backtrack(2, -3)   # Add -2
                    ├── backtrack(3, -2)   # Add +1
                    └── backtrack(3, -4)   # Add -1
        """
        def backtrack(i: int, total: int) -> int:
            # Base case: if we've used all numbers
            if i == len(nums):
                # Return 1 if we've reached target, 0 otherwise
                return 1 if total == target else 0
            
            # Try both adding and subtracting current number
            return (backtrack(i + 1, total + nums[i]) +  # Add nums[i]
                   backtrack(i + 1, total - nums[i]))    # Subtract nums[i]
        
        return backtrack(0, 0)

    """
    2. TOP-DOWN DP (MEMOIZATION)
    --------------------------
    Memo table evolution for nums=[1,2,1], target=0:
    
    Key format: (index, running_total) -> count
    
    Initial:                  Final state:
    {}                       {(0,0): 2,
                             (1,1): 1,
                             (1,-1): 1,
                             (2,3): 0,
                             (2,-1): 1,
                             (2,1): 1,
                             (2,-3): 0}
    """
    def findTargetSumWays_memoized(self, nums: list[int], target: int) -> int:
        dp = {}  # (index, total) -> number of ways
        
        def backtrack(i: int, total: int) -> int:
            # Base case
            if i == len(nums):
                return 1 if total == target else 0
            
            # Check if state already computed
            if (i, total) in dp:
                return dp[(i, total)]
            
            # Compute result and cache it
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) + 
                             backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]
        
        return backtrack(0, 0)

    """
    3. BOTTOM-UP DP
    -------------
    State evolution for nums=[1,2,1], target=0:
    
    Level 0: {0: 1}
    Level 1: {1: 1, -1: 1}
    Level 2: {3: 1, -1: 1, 1: 1, -3: 1}
    Level 3: {4: 1, 2: 2, 0: 2, -2: 2, -4: 1}
    
    Each level represents possible sums after processing i numbers
    Values show count of ways to achieve each sum
    """
    def findTargetSumWays_bottom_up(self, nums: list[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: one way to make sum 0 with no numbers
        
        # Process each number
        for i in range(n):
            # For each current sum and its count
            for curr_sum, count in dp[i].items():
                # Add current number
                dp[i + 1][curr_sum + nums[i]] += count
                # Subtract current number
                dp[i + 1][curr_sum - nums[i]] += count
        
        return dp[n][target]

    """
    4. SPACE-OPTIMIZED DP
    -------------------
    State evolution for nums=[1,2,1], target=0:
    
    Initial:    {0: 1}
    After 1:    {1: 1, -1: 1}
    After 2:    {3: 1, -1: 1, 1: 1, -3: 1}
    After 1:    {4: 1, 2: 2, 0: 2, -2: 2, -4: 1}
    
    Only keeps track of current possible sums
    Rolling updates reduce space complexity
    """
    def findTargetSumWays_optimized(self, nums: list[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1  # Base case
        
        for num in nums:
            next_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                # Update next state with both choices
                next_dp[curr_sum + num] += count  # Add num
                next_dp[curr_sum - num] += count  # Subtract num
            dp = next_dp  # Roll over to next state
            
        return dp[target]

def print_example():
    """
    Test function to demonstrate all solutions with detailed output
    """
    nums = [1,2,1]
    target = 0
    s = Solution()
    
    print(f"Testing with nums={nums}, target={target}")
    print("\n1. Recursive solution:", s.findTargetSumWays_recursive(nums, target))
    print("\n2. Memoized solution:", s.findTargetSumWays_memoized(nums, target))
    print("\n3. Bottom-up solution:", s.findTargetSumWays_bottom_up(nums, target))
    print("\n4. Optimized solution:", s.findTargetSumWays_optimized(nums, target))

if __name__ == "__main__":
    print_example()
```

"""
TARGET SUM PROBLEM - COMPREHENSIVE ANALYSIS
----------------------------------------
Example: nums = [1,1,1,1,1], target = 3

CORE CONCEPTS:
1. Each number must be preceded by either + or -
2. Need to find total ways to reach target
3. Classic decision tree/backtracking with optimization potential

VISUALIZATION OF STATE SPACE:
For smaller example nums=[1,1,1], target=1

Full Decision Tree:
                        (i=0, sum=0)
                   /                  \
            +1 (0,1)                -1 (0,-1)
           /         \             /          \
    +1(1,2)         -1(1,0)   +1(1,0)      -1(1,-2)
    /     \         /     \    /     \      /      \
+1(2,3) -1(2,1) +1(2,1) -1(2,-1) +1(2,1) -1(2,-1) +1(2,-1) -1(2,-3)

Each node format: (index, running_sum)
"""

class TargetSumAnalyzer:
    def __init__(self):
        self.paths = []  # Store all valid paths
        
    def recursive_solution(self, nums: list[int], target: int) -> int:
        """
        Recursive Approach (Brute Force)
        Time: O(2^n) - two choices for each number
        Space: O(n) - recursion stack depth
        
        Decision Process:
        1. At each index, branch into + and - choices
        2. Track running sum along path
        3. Count valid paths at leaf nodes
        """
        def backtrack(index: int, curr_sum: int, path: list) -> int:
            # Base case: reached end of array
            if index == len(nums):
                if curr_sum == target:
                    self.paths.append(path[:])
                    return 1
                return 0
            
            current = nums[index]
            # Try adding current number
            plus_count = backtrack(index + 1, curr_sum + current, 
                                 path + [f"+{current}"])
            # Try subtracting current number
            minus_count = backtrack(index + 1, curr_sum - current, 
                                  path + [f"-{current}"])
            
            return plus_count + minus_count
        
        return backtrack(0, 0, [])
    
    def memoized_solution(self, nums: list[int], target: int) -> int:
        """
        Top-down DP with Memoization
        Time: O(n * total), where total is sum of all numbers
        Space: O(n * total)
        
        Memo Table Structure for nums=[1,1,1], target=1:
        (index, curr_sum) -> count of ways
        
        Initial:                      Final:
        (0,0) -> ?                   (0,0) -> 2
        (1,1) -> ?                   (1,1) -> 1
        (1,-1) -> ?                  (1,-1) -> 1
        (2,*) -> 0/1                 (2,*) -> base cases
        """
        memo = {}
        total = sum(nums)
        
        def print_memo_state(index: int, curr_sum: int):
            print(f"\nState at index {index}, sum {curr_sum}")
            for k, v in sorted(memo.items()):
                print(f"({k[0]}, {k[1]}) -> {v}")
                
        def dfs(index: int, curr_sum: int) -> int:
            # Base case
            if index == len(nums):
                return 1 if curr_sum == target else 0
            
            # Check memo
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            
            # Try both choices
            current = nums[index]
            count = (dfs(index + 1, curr_sum + current) + 
                    dfs(index + 1, curr_sum - current))
            
            memo[(index, curr_sum)] = count
            print_memo_state(index, curr_sum)
            return count
        
        return dfs(0, 0)
    
    def bottom_up_dp(self, nums: list[int], target: int) -> int:
        """
        Bottom-up DP Solution
        Time: O(n * total)
        Space: O(n * total)
        
        DP Table Evolution for nums=[1,1,1], target=1:
        Level 0: {0: 1}
        Level 1: {-1: 1, 1: 1}
        Level 2: {-2: 1, 0: 2, 2: 1}
        Level 3: {-3: 1, -1: 3, 1: 3, 3: 1}
        
        Each key is possible sum, value is count of ways
        """
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case
        
        def print_dp_state(level: int):
            print(f"\nAfter level {level}:")
            for sum_val, count in sorted(dp[level].items()):
                print(f"Sum {sum_val}: {count} ways")
        
        # Build table bottom-up
        for i in range(n):
            curr = nums[i]
            for prev_sum, count in dp[i].items():
                # Add current number
                dp[i + 1][prev_sum + curr] += count
                # Subtract current number
                dp[i + 1][prev_sum - curr] += count
            print_dp_state(i + 1)
        
        return dp[n][target]
    
    def space_optimized(self, nums: list[int], target: int) -> int:
        """
        Space-Optimized Solution
        Time: O(n * total)
        Space: O(total)
        
        State Evolution for nums=[1,1], target=0:
        Start: {0: 1}
        After 1: {-1: 1, 1: 1}
        After 2: {-2: 1, 0: 2, 2: 1}
        
        Only keeps current possible sums and their counts
        """
        curr_sums = defaultdict(int)
        curr_sums[0] = 1
        
        def print_state(num: int):
            print(f"\nAfter processing {num}:")
            for sum_val, count in sorted(curr_sums.items()):
                print(f"Sum {sum_val}: {count} ways")
        
        for num in nums:
            next_sums = defaultdict(int)
            for curr_sum, count in curr_sums.items():
                next_sums[curr_sum + num] += count
                next_sums[curr_sum - num] += count
            curr_sums = next_sums
            print_state(num)
            
        return curr_sums[target]

"""
OPTIMIZATION INSIGHTS:
-------------------
1. State Compression:
   - Only need (index, curr_sum) for each state
   - Can further reduce to just curr_sum with rolling array

2. Pruning Opportunities:
   - Can skip branches if |curr_sum ± remaining_sum| < |target|
   - Early termination if impossible to reach target

3. Space Optimization:
   - Only need previous level's sums
   - Can use single dictionary with rolling updates

PATTERN RECOGNITION:
-----------------
1. Decision Tree Pattern:
   - Binary choice at each step
   - Need all possible combinations

2. DP Pattern:
   - Overlapping subproblems
   - State can be compressed
   - Bottom-up possible

3. Related Problems:
   - Subset Sum
   - 0/1 Knapsack variants
   - Expression evaluation
"""

def test_solutions():
    test_cases = [
        ([1,1,1,1,1], 3),
        ([1], 1),
        ([1,1], 0)
    ]
    
    solver = TargetSumAnalyzer()
    
    for nums, target in test_cases:
        print(f"\nTesting nums={nums}, target={target}")
        print("Recursive:", solver.recursive_solution(nums, target))
        print("Valid paths found:", solver.paths)
        solver.paths = []  # Reset paths
        
        print("\nMemoized:", solver.memoized_solution(nums, target))
        print("\nBottom-up DP:", solver.bottom_up_dp(nums, target))
        print("\nSpace Optimized:", solver.space_optimized(nums, target))

if __name__ == "__main__":
    test_solutions()