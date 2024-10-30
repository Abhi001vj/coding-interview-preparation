# https://leetcode.com/problems/3sum/description/
# 15. 3Sum
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4M
# Submissions
# 11.3M
# Acceptance Rate
# 35.6%
# Topics
# Companies
# Hint 1
# So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!
# Hint 2
# For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y, which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
# Hint 3
# The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Early return for invalid inputs
        if len(nums) < 3:
            return []
        
        # Sort once at the beginning
        nums.sort()
        res = []
        n = len(nums)
        
        # Early termination checks
        if nums[0] > 0 or nums[-1] < 0:  # If all positive or all negative
            return []
        
        for i in range(n-2):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Early termination: if smallest possible sum > 0, no more solutions
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
                
            # Early termination: if largest possible sum < 0, try next i
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
                
            # Two pointers
            left, right = i + 1, n - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates but optimize by moving both pointers simultaneously
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                        
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res


                