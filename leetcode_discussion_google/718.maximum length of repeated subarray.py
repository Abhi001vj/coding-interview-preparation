# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
# 718. Maximum Length of Repeated Subarray
# Medium
# Topics
# Companies
# Hint
# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

# Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# Example 2:

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 322.8K
# Submissions
# 633.4K
# Acceptance Rate
# 51.0%
# Topics
# Companies
# Hint 1
# Use dynamic programming. dp[i][j] will be the longest common prefix of A[i:] and B[j:].
# Hint 2
# The answer is max(dp[i][j]) over all i, j.

"""
Maximum Length of Repeated Subarray - Comprehensive Solution

Problem Understanding:
- Find longest subarray (contiguous sequence) that appears in both arrays
- Subarray must maintain same order in both arrays
- Empty array is possible but won't be the answer if other matches exist

Approaches:
1. Brute Force: Try all possible subarrays - O(n²m) time, O(1) space
2. Dynamic Programming: O(n*m) time, O(n*m) space
3. Rolling Hash/Sliding Window: O(n*m) time, O(n+m) space

Example Visualization with DP table:
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

DP Table Construction:
(Values represent length of common subarray ending at i,j)

     [3  2  1  4  7] (nums2)
  [ 0  0  0  0  0  0]
1 [ 0  0  0  1  0  0]
2 [ 0  0  1  0  0  0]
3 [ 0  1  0  0  0  0]
2 [ 0  0  2  0  0  0]
1 [ 0  0  0  3  0  0]
(nums1)

Maximum value in table = 3, corresponding to subarray [3,2,1]
"""

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize DP table with one extra row and column for base cases
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Variable to track maximum length found
        max_length = 0
        
        """
        DP State Definition:
        dp[i][j] = length of longest common subarray ending at 
                   nums1[i-1] and nums2[j-1]
        
        DP Transition:
        if nums1[i-1] == nums2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 0
        """
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(max_length, dp[i][j])
                    
        return max_length

    def findLength_space_optimized(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Space optimized version using rolling array
        Time: O(m*n)
        Space: O(n)
        """
        m, n = len(nums1), len(nums2)
        prev_row = [0] * (n + 1)
        max_length = 0
        
        for i in range(1, m + 1):
            curr_row = [0] * (n + 1)
            for j in range(1, n + 1):
                if nums1[i-1] == nums2[j-1]:
                    curr_row[j] = prev_row[j-1] + 1
                    max_length = max(max_length, curr_row[j])
            prev_row = curr_row
            
        return max_length

    """
    Alternative Approaches:

    1. Brute Force Solution:
    def findLength_brute_force(self, nums1, nums2):
        def check_subarray(len_s, start1, start2):
            for i in range(len_s):
                if nums1[start1 + i] != nums2[start2 + i]:
                    return False
            return True
            
        max_len = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                k = 0
                while (i + k < len(nums1) and 
                       j + k < len(nums2) and 
                       nums1[i + k] == nums2[j + k]):
                    k += 1
                max_len = max(max_len, k)
        return max_len

    2. Binary Search + Rolling Hash:
    - Binary search on the length of the common subarray
    - Use rolling hash to quickly compare subarrays
    - Time: O(n*log(min(n,m)))
    - More complex implementation but better for very large arrays
    """