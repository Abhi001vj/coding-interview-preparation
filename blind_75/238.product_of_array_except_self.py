# # https://leetcode.com/problems/product-of-array-except-self/description/
# 238. Product of Array Except Self
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3.1M
# Submissions
# 4.6M
# Acceptance Rate
# 66.9%
# Topics
# Companies
# Hint 1
# Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?
# Hint 2
# Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        suffix_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix_product 
            suffix_product *= nums[i]

        return answer