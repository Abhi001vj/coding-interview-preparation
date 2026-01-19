"""
2348. Number of Zero-Filled Subarrays (Medium)
Pattern: Array / Math (Arithmetic Progression)

--------------------------------------------------------------------------------
PROBLEM UNDERSTANDING
--------------------------------------------------------------------------------
Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements.

Input:  [1, 3, 0, 0, 2, 0, 0, 4]
Output: 6
Explanation:
- [0, 0] gives: 2 size-1 subarrays, 1 size-2 subarray -> Total 3.
- [0, 0] gives: 2 size-1 subarrays, 1 size-2 subarray -> Total 3.
- Total = 3 + 3 = 6.

--------------------------------------------------------------------------------
VISUALIZATION: THE "STREAK" CONCEPT
--------------------------------------------------------------------------------
Imagine a streak of zeros as a triangle of possibilities.

Streak: [0, 0, 0] (Length 3)
1. Single 0s:  [0], [0], [0]   (3)
2. Double 0s:  [0,0], [0,0]    (2)
3. Triple 0s:  [0,0,0]         (1)

Total = 1 + 2 + 3 = 6.
General Formula for streak of length L: Sum = L * (L + 1) / 2

--------------------------------------------------------------------------------
ALGORITHM
--------------------------------------------------------------------------------
1. Iterate through the array.
2. If we see a 0, increment current_streak_length.
3. Add current_streak_length to total_ans.
   (Why? Because adding the Nth zero adds N new subarrays ending at that zero).
   
   Example: [0, 0] -> [0, 0, 0]
   Old Subarrays: [0], [0], [0,0] (3)
   New Zero adds: [0], [0,0], [0,0,0] (3 new ones)
   Total becomes 3 + 3 = 6.

4. If we see a non-0, reset current_streak_length to 0.

Complexity: O(N) Time, O(1) Space.
--------------------------------------------------------------------------------
"""

from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        streak = 0
        
        for x in nums:
            if x == 0:
                streak += 1
                ans += streak
            else:
                streak = 0
                
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4])) # Expected: 6
