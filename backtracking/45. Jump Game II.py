# https://leetcode.com/problems/jump-game-ii/description/
# 45. Jump Game II
# Medium
# Topics
# Companies
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
```python
"""
Jump Game II - Comprehensive Solution Analysis
=========================================

The problem asks us to find the minimum number of jumps needed to reach
the last index, where each number represents the maximum jump length from
that position.

Let's explore multiple approaches to solve this:
1. Dynamic Programming
2. Greedy with BFS-like approach
3. Optimized Greedy
"""

class JumpGameSolutions:
    def approach1_dynamic_programming(self, nums: List[int]) -> int:
        """
        Dynamic Programming Solution
        --------------------------
        For each position, calculate minimum jumps needed to reach end.
        
        Visual Example for [2,3,1,1,4]:
        dp[i] = minimum jumps needed from position i
        
        Process:
        index:  0  1  2  3  4
        nums:   2  3  1  1  4
        dp:     2  1  2  1  0
        
        At index 0:
        Can jump to index 1,2 -> min(dp[1], dp[2]) + 1 = 2
        
        Time: O(n²) in worst case
        Space: O(n) for dp array
        """
        n = len(nums)
        dp = [float('inf')] * n
        dp[-1] = 0  # Base case: already at end
        
        # Work backwards from end
        for i in range(n-2, -1, -1):
            # Try all possible jumps from current position
            for jump in range(1, nums[i] + 1):
                if i + jump >= n:
                    break
                dp[i] = min(dp[i], 1 + dp[i + jump])
                
        return dp[0]

    def approach2_greedy_bfs(self, nums: List[int]) -> int:
        """
        Greedy BFS-like Approach
        ----------------------
        Think of it like BFS levels, where each level represents positions
        reachable in the same number of jumps.
        
        Visual Example for [2,3,1,1,4]:
        Level 0: [2]         -> can reach indices 1,2
        Level 1: [3,1]       -> can reach indices 2,3,4
        Level 2: [1,1,4]     -> reached end!
        
        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        if n <= 1:
            return 0
            
        current_max_reach = nums[0]  # Furthest we can go in current jump
        next_max_reach = nums[0]     # Furthest we can go in next jump
        jumps = 1
        
        for i in range(n):
            if i > current_max_reach:
                # Need another jump to continue
                jumps += 1
                current_max_reach = next_max_reach
            
            # Update furthest possible reach
            if i < n-1:  # Don't need to check from last position
                next_max_reach = max(next_max_reach, i + nums[i])
                
        return jumps

    def approach3_optimized_greedy(self, nums: List[int]) -> int:
        """
        Optimized Greedy Approach
        -----------------------
        Keep track of current range and next range to minimize jumps.
        
        Visual Example for [2,3,1,1,4]:
        Start: range [0,0], can reach [1,2]
        Jump 1: range [1,2], can reach [2,4]
        Jump 2: range [2,4], reached end!
        
        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        if n <= 1:
            return 0
            
        jumps = 0
        current_end = 0
        current_max_reach = 0
        
        for i in range(n-1):  # Don't need to jump from last index
            current_max_reach = max(current_max_reach, i + nums[i])
            
            if i == current_end:
                # Reached end of current range, must jump
                jumps += 1
                current_end = current_max_reach
                
        return jumps

    def visualize_jumps(self, nums: List[int]) -> None:
        """
        Helper function to visualize the jumping process.
        """
        print(f"\nJumping through array: {nums}")
        print("Position:", end=" ")
        for i in range(len(nums)):
            print(f"{i:2}", end=" ")
        print("\nValue:   ", end=" ")
        for num in nums:
            print(f"{num:2}", end=" ")
        print()
        
        # Show jump process
        position = 0
        jumps = 0
        while position < len(nums) - 1:
            print(f"\nAt position {position}, can jump to:", end=" ")
            max_reach = float('-inf')
            best_next = position
            
            # Show possible jumps
            for j in range(1, nums[position] + 1):
                if position + j >= len(nums):
                    break
                print(f"{position + j}", end=" ")
                # Track best next position
                if position + j + nums[position + j] > max_reach:
                    max_reach = position + j + nums[position + j]
                    best_next = position + j
                    
            jumps += 1
            position = best_next
            print(f"\nBest jump to: {position}")
            
        print(f"\nReached end in {jumps} jumps")

def demonstrate_solutions():
    """
    Test and compare all approaches with visualization.
    """
    test_cases = [
        [2,3,1,1,4],
        [2,3,0,1,4],
        [1,2,3]
    ]
    
    solution = JumpGameSolutions()
    
    for nums in test_cases:
        print("\n" + "="*50)
        solution.visualize_jumps(nums)
        
        # Compare results from all approaches
        result1 = solution.approach1_dynamic_programming(nums)
        result2 = solution.approach2_greedy_bfs(nums)
        result3 = solution.approach3_optimized_greedy(nums)
        
        print(f"\nResults for nums = {nums}:")
        print(f"Dynamic Programming: {result1}")
        print(f"Greedy BFS: {result2}")
        print(f"Optimized Greedy: {result3}")

if __name__ == "__main__":
    demonstrate_solutions()

"""
Key Insights and Patterns:

1. Dynamic Programming vs Greedy:
   - DP considers all possibilities
   - Greedy makes locally optimal choices
   - Trade-off between completeness and efficiency

2. BFS-like Thinking:
   - Each jump is like a level in BFS
   - Track maximum reachable positions
   - Minimize number of levels/jumps

3. Optimization Techniques:
   - Track ranges instead of individual positions
   - Look ahead to make better choices
   - Early termination when possible

4. Important Considerations:
   - No need to jump from last position
   - Can always reach end (given)
   - Maximum jump vs optimal jump
   - Handle edge cases (single element)
"""
```

Each approach offers different insights:

1. **Dynamic Programming**:
   - Most intuitive approach
   - Shows optimal substructure
   - Good for understanding problem structure
   - Less efficient than greedy approaches

2. **Greedy BFS**:
   - Views problem as level traversal
   - More efficient than DP
   - Natural way to minimize jumps
   - Shows connection to graph algorithms

3. **Optimized Greedy**:
   - Most efficient solution
   - Maintains minimal state
   - Shows power of range tracking
   - Best for actual implementation

Would you like me to:
1. Explain any specific approach in detail?
2. Add more examples or visualizations?
3. Discuss specific optimizations?
4. Show how to handle different variations of the problem?


```python
"""
Let's understand how backtracking works for Jump Game II with a detailed example
and step-by-step visualization. The key idea is to try all possible jumps
at each position, but working backwards from the largest possible jump first.
"""

def jump(self, nums: List[int]) -> int:
    """
    Example: nums = [2,3,1,1,4]
    
    The backtracking process works like a decision tree where at each position,
    we try all possible jumps we can make from largest to smallest.
    
    Visual Process:
    Starting at index 0, nums[0] = 2
    Can jump 1 or 2 positions
    
            0(2)
           /    \
        1(3)    2(1)
       /  |  \    |
    2(1) 3(1) 4  3(1)
      |    |       |
    3(1)  4(4)    4(4)
      |
    4(4)
    
    When we reach index 4 (target), we update smallest[0] with minimum jumps needed
    """
    n = len(nums)
    smallest = [float('inf')]  # Using list to modify in recursive calls

    def backtrack(i=0, jumps=0):
        """
        i: current position
        jumps: number of jumps taken so far
        
        Example state changes for nums = [2,3,1,1,4]:
        
        Call 1: i=0, jumps=0
        - Can jump to positions 1,2
        - Try position 2 first (larger jump)
        
        Call 2: i=2, jumps=1
        - Can jump to position 3
        
        Call 3: i=3, jumps=2
        - Can jump to position 4
        
        Call 4: i=4, jumps=3
        - Reached end, update smallest[0]
        """
        # Base case: reached target
        if i == n-1:
            smallest[0] = min(smallest[0], jumps)
            return
        
        # Calculate maximum possible jump from current position
        max_jumps = nums[i]
        max_reachable_index = min(i+max_jumps, n-1)

        # Try all possible jumps from largest to smallest
        for new_index in range(max_reachable_index, i, -1):
            # Only proceed if this path could lead to a better solution
            if jumps + 1 < smallest[0]:  # Optimization
                backtrack(new_index, jumps+1)
    
    backtrack()  # Start backtracking from index 0
    return smallest[0]

def visualize_backtracking(nums: List[int]):
    """
    Helper function to visualize the backtracking process
    """
    print(f"\nBacktracking through array: {nums}")
    
    def print_state(i: int, jumps: int, indent: int):
        print(" " * indent + f"At index {i} (value={nums[i]}) after {jumps} jumps")
        print(" " * indent + "Can jump to:", end=" ")
        max_jumps = nums[i]
        max_reachable = min(i + max_jumps, len(nums)-1)
        for pos in range(i+1, max_reachable+1):
            print(pos, end=" ")
        print()
    
    def trace_backtrack(i=0, jumps=0, indent=0):
        print_state(i, jumps, indent)
        
        if i == len(nums)-1:
            print(" " * indent + "Reached target!")
            return
        
        max_jumps = nums[i]
        max_reachable = min(i + max_jumps, len(nums)-1)
        
        for new_index in range(max_reachable, i, -1):
            print(" " * indent + f"Trying jump to {new_index}")
            trace_backtrack(new_index, jumps+1, indent+2)
    
    trace_backtrack()

# Example usage
nums = [2,3,1,1,4]
visualize_backtracking(nums)
```

The key points to understand about this solution:

1. **Why Backtracking?**
   - It explores all possible paths to find the minimum jumps
   - It can prune paths that won't lead to a better solution
   - It works backwards from larger jumps to smaller ones

2. **How it Works:**
   - At each position, it tries all possible jumps
   - It starts with the largest possible jump first
   - When it reaches the end, it updates the minimum jumps needed
   - It backtracks to try other paths

3. **State Management:**
   - `i` tracks current position
   - `jumps` tracks number of jumps taken
   - `smallest[0]` stores the minimum jumps found so far
   - Using list for `smallest` to modify it in recursive calls

4. **Optimization:**
   - Only explores paths that could lead to better solutions
   - Tries larger jumps first (might reach target faster)
   - Uses early pruning when current path is already worse

Would you like me to:
1. Add more detailed state transitions?
2. Show how it handles different test cases?
3. Explain any specific part in more detail?
4. Compare this with other approaches?


def jump(nums: List[int]) -> int:
    """
    Let's visualize with example: nums = [2,3,1,1,4]
    
    We track three things:
    1. jumps: number of jumps taken
    2. current_end: farthest we can go with current jumps
    3. current_max_reach: farthest we can reach exploring current range
    
    Let's watch how values change at each position:
    
    Initial state:
    [2, 3, 1, 1, 4]
     ^
     i=0
    jumps = 0
    current_end = 0
    current_max_reach = 0
    
    Step 1 (i=0):
    [2, 3, 1, 1, 4]
     ^
    - From index 0, we can reach index 2 (0 + nums[0])
    - current_max_reach = max(0, 0 + 2) = 2
    - i equals current_end (0), so make a jump
    - jumps = 1
    - current_end = current_max_reach = 2
    
    Step 2 (i=1):
    [2, 3, 1, 1, 4]
        ^
    - From index 1, we can reach index 4 (1 + nums[1])
    - current_max_reach = max(2, 1 + 3) = 4
    - i not equal to current_end yet, continue
    
    Step 3 (i=2):
    [2, 3, 1, 1, 4]
           ^
    - From index 2, we can reach index 3 (2 + nums[2])
    - current_max_reach = max(4, 2 + 1) = 4
    - i equals current_end (2), so make a jump
    - jumps = 2
    - current_end = current_max_reach = 4
    
    Step 4 (i=3):
    [2, 3, 1, 1, 4]
              ^
    - From index 3, we can reach index 4 (3 + nums[3])
    - current_max_reach = max(4, 3 + 1) = 4
    - i not equal to current_end yet, continue
    
    Final jumps = 2
    """
    n = len(nums)
    if n <= 1:
        return 0
        
    jumps = 0              # Track number of jumps
    current_end = 0        # Farthest we can go with current jumps
    current_max_reach = 0  # Farthest we can potentially reach
    
    # Don't need to check last position as we're already there
    for i in range(n-1):
        # Update the farthest we can reach from current position
        current_max_reach = max(current_max_reach, i + nums[i])
        
        # If we've reached the end of current jump's range
        if i == current_end:
            # Must make another jump
            jumps += 1
            # Update how far we can go with this new jump
            current_end = current_max_reach
            
    return jumps