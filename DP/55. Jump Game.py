# https://leetcode.com/problems/jump-game/description/
# 55. Jump Game
# Medium
# Topics
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105
```python
"""
Jump Game - Comprehensive Analysis

The problem asks us to determine if we can reach the last index by jumping,
where each number represents the maximum jump length from that position.
Let's explore different ways to solve this, starting from simple to optimized
approaches.
"""

class JumpGameSolutions:
    def approach1_recursive(self, nums: List[int]) -> bool:
        """
        Recursive approach that tries all possible jumps from each position.
        
        Let's visualize with nums = [2,3,1,1,4]:
        
                    0(2)
                   /   \
                1(3)   2(1)
               / | \     \
            2(1) 3(1) 4   3(1)
              |    |        |
            3(1)  4(4)     4(4)
              |
            4(4)
            
        Time: O(2^n) - can try all possibilities
        Space: O(n) - recursion depth
        """
        def can_reach_end(position: int, visited: set) -> bool:
            # Base cases
            if position >= len(nums) - 1:  # Reached or passed end
                return True
            if position in visited:  # Already tried this position
                return False
                
            visited.add(position)
            max_jump = nums[position]
            
            # Try each possible jump length
            for jump in range(1, max_jump + 1):
                if can_reach_end(position + jump, visited):
                    return True
                    
            return False
            
        return can_reach_end(0, set())

    def approach2_dynamic_programming(self, nums: List[int]) -> bool:
        """
        Dynamic programming approach working backwards.
        For each position, determine if we can reach the end from here.
        
        Example: nums = [2,3,1,1,4]
        dp[i] = can reach end from position i
        
        Work backwards:
        dp[4] = True (already at end)
        dp[3] = True (can reach 4)
        dp[2] = True (can reach 3,4)
        dp[1] = True (can reach 2,3,4)
        dp[0] = True (can reach 1,2)
        
        Time: O(n²)
        Space: O(n)
        """
        n = len(nums)
        dp = [False] * n
        dp[-1] = True  # Can reach end from end
        
        # Work backwards from second-to-last position
        for i in range(n-2, -1, -1):
            max_jump = min(nums[i], n-1 - i)  # Don't jump past end
            # Check if we can reach any position that can reach end
            for jump in range(1, max_jump + 1):
                if dp[i + jump]:
                    dp[i] = True
                    break
                    
        return dp[0]

    def approach3_greedy(self, nums: List[int]) -> bool:
        """
        Greedy approach tracking the furthest reachable position.
        
        Example visualization for nums = [2,3,1,1,4]:
        Position:     0   1   2   3   4
        Value:        2   3   1   1   4
        Max reach:    2   4   4   4   8
        
        At each position:
        - Update furthest we can reach
        - If current position > max reach, we're stuck
        
        Time: O(n)
        Space: O(1)
        """
        max_reach = 0  # Furthest index we can reach
        
        # Check each position we can reach
        for i in range(len(nums)):
            # If we can't reach current position
            if i > max_reach:
                return False
            # Update furthest we can reach from here
            max_reach = max(max_reach, i + nums[i])
            # If we can reach end, we're done
            if max_reach >= len(nums) - 1:
                return True
                
        return True

    def visualize_process(self, nums: List[int]) -> None:
        """
        Helper function to visualize how we determine if we can reach the end.
        """
        print(f"\nAnalyzing array: {nums}")
        print("Position:", end=" ")
        for i in range(len(nums)):
            print(f"{i:2}", end=" ")
        print("\nValue:   ", end=" ")
        for num in nums:
            print(f"{num:2}", end=" ")
        print()
        
        # Show max reach at each position
        max_reach = 0
        print("\nStep-by-step analysis:")
        for i in range(len(nums)):
            if i > max_reach:
                print(f"Position {i}: Cannot reach this position!")
                break
            old_reach = max_reach
            max_reach = max(max_reach, i + nums[i])
            print(f"Position {i}: Can jump {nums[i]} steps")
            print(f"Max reach updated from {old_reach} to {max_reach}")
            if max_reach >= len(nums) - 1:
                print("Can reach the end!")
                break

def demonstrate_solutions():
    """
    Test all approaches with various examples.
    """
    test_cases = [
        [2,3,1,1,4],  # True
        [3,2,1,0,4],  # False
        [1,1,1,1],    # True
        [0]           # True
    ]
    
    solution = JumpGameSolutions()
    
    for nums in test_cases:
        print("\n" + "="*50)
        solution.visualize_process(nums)
        
        # Test all approaches
        result1 = solution.approach1_recursive(nums)
        result2 = solution.approach2_dynamic_programming(nums)
        result3 = solution.approach3_greedy(nums)
        
        print(f"\nResults for nums = {nums}:")
        print(f"Recursive: {result1}")
        print(f"DP: {result2}")
        print(f"Greedy: {result3}")

if __name__ == "__main__":
    demonstrate_solutions()
```

Each approach demonstrates different problem-solving strategies:

1. **Recursive (Backtracking)**:
   - Most intuitive but least efficient
   - Tries all possible paths
   - Good for understanding the problem
   - Shows why optimization is needed

2. **Dynamic Programming**:
   - More efficient than recursion
   - Works backward from the goal
   - Shows optimal substructure
   - Still has room for optimization

3. **Greedy**:
   - Most efficient solution
   - Takes advantage of problem properties
   - Shows how local optimal choices lead to global solution
   - Best for actual implementation

Key Insights:
1. We don't need to find the path, just whether it exists
2. We can work forward (greedy) or backward (DP)
3. At each point, we only need to know if we can reach it

The greedy solution is particularly elegant because:
1. If we can reach position i, we can reach any position up to i
2. We only need to track the furthest position we can reach
3. If we can't reach position i, we can't reach the end

Would you like me to:
1. Explain any specific approach in more detail?
2. Add more examples or test cases?
3. Show how to handle different variations?