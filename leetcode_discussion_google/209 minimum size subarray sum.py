# https://leetcode.com/problems/minimum-size-subarray-sum/
# 209. Minimum Size Subarray Sum
# Solved
# Medium
# Topics
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

"""
SLIDING WINDOW SOLUTION EXPLAINED

Core Idea:
- Use two pointers (l, r) to form a window
- Expand window by moving r until sum >= target
- Shrink window by moving l until sum < target
- Track minimum window size that satisfies condition

Detailed Example Visualization:
nums = [2,3,1,2,4,3], target = 7

Step-by-step process:
1. Initialize: l=0, r=0
   [2],3,1,2,4,3     sum=2 < 7
    l
    r

2. Expand window:
   [2,3],1,2,4,3     sum=5 < 7
    l  r

3. Keep expanding:
   [2,3,1],2,4,3     sum=6 < 7
    l    r

4. Keep expanding:
   [2,3,1,2],4,3     sum=8 >= 7
    l      r
   Current length = 4

5. Shrink window:
   2,[3,1,2],4,3     sum=6 < 7
      l    r

6. Expand window:
   2,[3,1,2,4],3     sum=10 >= 7
      l      r
   Current length = 4

7. Shrink window:
   2,3,[1,2,4],3     sum=7 >= 7
        l    r
   Current length = 3

8. Continue process...
   Final result: [4,3] with length 2
"""

def minSubArrayLen(target: int, nums: List[int]) -> int:
    min_length = float('inf')  # Initialize to infinity
    l = 0                      # Left pointer of window
    summ = 0                   # Current sum of window
    
    """
    Sliding Window Invariant:
    - At any point, summ = sum of elements from index l to r
    - If summ >= target, try to shrink window
    - Track minimum window length that satisfies summ >= target
    """
    
    for r in range(len(nums)):
        # Expand window by adding right element
        summ += nums[r]
        
        # While window sum is valid, try to minimize it
        while summ >= target:
            # Current window size is r-l+1
            min_length = min(min_length, r-l+1)
            # Remove leftmost element
            summ -= nums[l]
            # Shrink window from left
            l += 1
            
        """
        Example State:
        nums = [2,3,1,2,4,3], target = 7
        
        When r = 3:
        - Window: [2,3,1,2], sum = 8
        - Since 8 >= 7, shrink from left:
          > Remove 2, window: [3,1,2]
          > Still valid? No, sum = 6
          > Stop shrinking
        
        When r = 4:
        - Window: [3,1,2,4], sum = 10
        - Since 10 >= 7, shrink from left:
          > Remove 3, window: [1,2,4]
          > Still valid? Yes, sum = 7
          > Can shrink more? No, sum would be < 7
        """
    
    # Return 0 if no valid window found
    return min_length if min_length < float('inf') else 0

"""
Time Complexity: O(n)
- Each element is:
  * Added to window once (r pointer)
  * Removed from window at most once (l pointer)
- Total operations is O(2n) = O(n)

Space Complexity: O(1)
- Only storing pointers and sum

Why This Works:
1. Never miss a potential answer:
   - We try every possible end point (r)
   - For each end point, we find smallest valid start point (l)

2. Optimal solution properties:
   - If a window sum >= target
   - No need to consider larger windows ending at same point
   - Can safely shrink from left

3. Early stopping:
   - Once window becomes invalid (sum < target)
   - Must expand right side to find next valid window
"""