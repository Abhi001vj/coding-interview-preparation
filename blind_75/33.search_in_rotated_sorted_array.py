# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# 33. Search in Rotated Sorted Array
# Solved
# Medium
# Topics
# Companies
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        res = -1

        l = 0
        r = len(nums) - 1

        while l<=r:
            m = (l+r) // 2
            # If the middle element is the target
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]: # left sorted
                if nums[l] <= target< nums[m]: # target is in left
                    r = m-1
                else:  # Target is in the right half
                    l = m +1
            else: # right is sorted
                if nums[m] < target<= nums[r]: # target is in right
                    l = m+1
                else:  # Target is in the left half
                    r = m -1

                
        return -1