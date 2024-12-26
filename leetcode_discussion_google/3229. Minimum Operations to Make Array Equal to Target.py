
# Code


# Testcase
# Testcase
# Test Result
# 3229. Minimum Operations to Make Array Equal to Target
# Hard
# Topics
# Companies
# Hint
# You are given two positive integer arrays nums and target, of the same length.

# In a single operation, you can select any subarray of nums and increment each element within that subarray by 1 or decrement each element within that subarray by 1.

# Return the minimum number of operations required to make nums equal to the array target.

 

# Example 1:

# Input: nums = [3,5,1,2], target = [4,6,2,4]

# Output: 2

# Explanation:

# We will perform the following operations to make nums equal to target:
# - Increment nums[0..3] by 1, nums = [4,6,2,3].
# - Increment nums[3..3] by 1, nums = [4,6,2,4].

# Example 2:

# Input: nums = [1,3,2], target = [2,1,4]

# Output: 5

# Explanation:

# We will perform the following operations to make nums equal to target:
# - Increment nums[0..0] by 1, nums = [2,3,2].
# - Decrement nums[1..1] by 1, nums = [2,2,2].
# - Decrement nums[1..1] by 1, nums = [2,1,2].
# - Increment nums[2..2] by 1, nums = [2,1,3].
# - Increment nums[2..2] by 1, nums = [2,1,4].

 

# Constraints:

# 1 <= nums.length == target.length <= 105
# 1 <= nums[i], target[i] <= 108
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 15.9K
# Submissions
# 41.7K
# Acceptance Rate
# 38.2%
# Topics
# Companies
# Hint 1
# Change nums'[i] = nums[i] - target[i], so our goal is to make nums' into all 0s.
# Hint 2
# Divide and conquer.
# Problem Analysis:
# ----------------
# Given two arrays nums and target of same length, we need to find minimum operations
# where in each operation we can select any subarray and increment/decrement all elements by 1
# to make nums equal to target.
#
# Key Insights:
# 1. We can transform this into a difference array problem
# 2. For any subarray operation, we're essentially adding/subtracting 1 from a range
# 3. The goal is to make all elements equal using minimum operations
#
# Example 1 Visualization:
# nums   = [3, 5, 1, 2]
# target = [4, 6, 2, 4]
# diff   = [-1,-1,-1,-2]  (nums[i] - target[i])
#
# Operation 1: Increment [0,3] by 1
# Before: [3, 5, 1, 2]
# After:  [4, 6, 2, 3]
#         ↑  ↑  ↑  ↑
#         +1 +1 +1 +1
#
# Operation 2: Increment [3,3] by 1
# Before: [4, 6, 2, 3]
# After:  [4, 6, 2, 4]
#                   ↑
#                   +1
#
# Solution Approaches:
# ------------------
# 1. Brute Force Solution:
#    - Try all possible subarrays and both increment/decrement
#    - Time: O(n³) - three nested loops for all possible subarrays
#    - Space: O(n) - to store current state
#
# 2. Greedy with Difference Array:
#    - Convert to difference array problem
#    - Use prefix sum concept
#    - Time: O(n)
#    - Space: O(1)

def minOperations(nums, target):
    """
    According to the hints:
      1) Let diff[i] = nums[i] - target[i]. We want diff to become all zeros.
      2) We can treat this as adjusting "boundaries" in the diff array.
         Each subarray increment/decrement effectively changes two boundaries.
    
    The minimal operations can be found by summing boundary changes and dividing by 2.
    """
    n = len(nums)
    if n == 0:
        return 0  # No elements, no operations needed (edge case, though not in constraints)

    # 1) Build the difference array
    diff = [nums[i] - target[i] for i in range(n)]
    
    # 2) Count boundary changes
    #    - First boundary: absolute value of diff[0]
    #    - Middle boundaries: absolute value of difference between consecutive elements
    #    - Last boundary: absolute value of diff[n-1]
    boundary_changes = abs(diff[0])
    for i in range(1, n):
        boundary_changes += abs(diff[i] - diff[i - 1])
    boundary_changes += abs(diff[n - 1])
    
    # 3) Each subarray operation fixes 2 boundaries, so divide by 2
    return boundary_changes // 2

# -----------------
# TESTCASES
# -----------------

# Example 1
nums1 = [3, 5, 1, 2]
target1 = [4, 6, 2, 4]
# Expected output: 2
print(minOperations(nums1, target1))

# Example 2
nums2 = [1, 3, 2]
target2 = [2, 1, 4]
# Expected output: 5
print(minOperations(nums2, target2))
