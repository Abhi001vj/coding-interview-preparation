# https://leetcode.com/problems/house-robber/description/
# 198. House Robber
# Medium
# Topics
# Companies
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

"""
APPROACH ANALYSIS:

1. Basic Understanding:
   - Can't rob adjacent houses
   - Need to find max sum of non-adjacent elements
   - Example: [2,7,9,3,1]
   Possible combinations:
   2 + 9 + 1 = 12
   7 + 3 = 10
   2 + 3 = 5
   etc.

2. Approaches Available:
   A. Recursive (with memoization)
   B. Dynamic Programming with array
   C. DP with constant space
   D. Even/Odd approach (not optimal)

Let's implement all approaches:
"""

# Solution 1: Recursive with Memoization
class RecursiveSolution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def rob_from(i: int) -> int:
            # Base cases
            if i >= len(nums):
                return 0
            
            # Check memo
            if i in memo:
                return memo[i]
            
            # Decision tree:
            # Either rob current house and skip next
            # Or skip current and try next
            memo[i] = max(
                nums[i] + rob_from(i + 2),  # Rob current
                rob_from(i + 1)             # Skip current
            )
            
            return memo[i]
        
        return rob_from(0)

# Solution 2: Dynamic Programming with Array
class DPArraySolution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        # dp[i] represents max money at house i
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(
                dp[i-1],           # Skip current house
                dp[i-2] + nums[i]  # Rob current house
            )
            
        return dp[-1]

# Solution 3: DP with Constant Space
class OptimizedDPSolution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        # Only need two previous values
        prev_two = nums[0]  # Max money if we end at i-2
        prev_one = max(nums[0], nums[1])  # Max money if we end at i-1
        
        for i in range(2, len(nums)):
            current = max(
                prev_one,                # Skip current house
                prev_two + nums[i]       # Rob current house
            )
            prev_two = prev_one
            prev_one = current
            
        return prev_one

"""
DETAILED WALKTHROUGH for nums = [2,7,9,3,1]

1. Recursive Approach:
   Call Tree:
                rob(0)
              /        \
         rob(2)        rob(1)
        /     \       /     \
    rob(4)  rob(3)  rob(3)  rob(2)
   
   With memoization:
   rob(0) = max(2 + rob(2), rob(1))
   rob(2) = max(9 + rob(4), rob(3))
   ...

2. DP Array Approach:
   dp[0] = 2
   dp[1] = max(2, 7) = 7
   dp[2] = max(7, 2 + 9) = 11
   dp[3] = max(11, 7 + 3) = 11
   dp[4] = max(11, 11 + 1) = 12

3. Optimized DP:
   prev_two = 2
   prev_one = 7
   i=2: current = max(7, 2+9) = 11
   i=3: current = max(11, 7+3) = 11
   i=4: current = max(11, 11+1) = 12

Time/Space Complexity:
1. Recursive: O(n) time, O(n) space
2. DP Array: O(n) time, O(n) space
3. Optimized: O(n) time, O(1) space

Visual State Transitions:
[2,7,9,3,1]

State at each house:
House 0: 2     (Take 2)
House 1: 7     (Take 7)
House 2: 11    (Take 2+9)
House 3: 11    (Keep previous)
House 4: 12    (Take 11+1)
"""

# Solution 4: Even/Odd Approach (Alternative but not optimal)
class EvenOddSolution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        even_sum = 0
        odd_sum = 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum = max(even_sum + nums[i], odd_sum)
            else:
                odd_sum = max(odd_sum + nums[i], even_sum)
                
        return max(even_sum, odd_sum)

"""
DECISION POINTS:

1. Why DP is Best:
   - Optimal substructure
   - Overlapping subproblems
   - No need to try all combinations

2. Space Optimization:
   - Only need last two values
   - Can reduce from O(n) to O(1)

3. Edge Cases:
   - Empty array
   - Single house
   - All same values
   - Alternating high/low values

4. Follow-up Questions:
   - What if houses are in a circle?
   - What if some houses have alarms?
   - What if adjacent houses have different penalties?
   """