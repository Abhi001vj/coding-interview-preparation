# https://leetcode.com/problems/maximum-product-subarray/description/
# 152. Maximum Product Subarray
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curmin, curmax = 1,1

        for n in nums:
            tmp = curmax*n
            curmax = max(tmp, curmin*n, n)
            curmin = min(tmp, curmin*n, n)

            res =  max(res, curmax)

        return res