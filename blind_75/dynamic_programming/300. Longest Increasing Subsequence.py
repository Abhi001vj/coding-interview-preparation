# https://leetcode.com/problems/longest-increasing-subsequence/description/
# 300. Longest Increasing Subsequence
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

1. Recursion
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(i, j):
            if i == len(nums):
                return 0
            
            LIS = dfs(i + 1, j) # not include

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # include
            
            return LIS

        return dfs(0, -1)
Time & Space Complexity
Time complexity: 
O
(
2
n
)
O(2 
n
 )
Space complexity: 
O
(
n
)
O(n)
2. Dynamic Programming (Top-Down)
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]  

        def dfs(i, j):
            if i == n:
                return 0
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            LIS = dfs(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            memo[i][j + 1] = LIS
            return LIS

        return dfs(0, -1)
Time & Space Complexity
Time complexity: 
O
(
n
2
)
O(n 
2
 )
Space complexity: 
O
(
n
2
)
O(n 
2
 )
3. Dynamic Programming (Bottom-Up)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
Time & Space Complexity
Time complexity: 
O
(
n
2
)
O(n 
2
 )
Space complexity: 
O
(
n
)
O(n)
4. Segment Tree
from bisect import bisect_left
class SegmentTree:
    def __init__(self, N):
        self.n = N
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        self.tree = [0] * (2 * self.n)

    def update(self, i, val):
        self.tree[self.n + i] = val
        j = (self.n + i) >> 1
        while j >= 1:
            self.tree[j] = max(self.tree[j << 1], self.tree[j << 1 | 1])
            j >>= 1

    def query(self, l, r):
        if l > r:
            return 0
        res = float('-inf')
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def compress(arr):
            sortedArr = sorted(set(arr))
            order = []
            for num in arr:
                order.append(bisect_left(sortedArr, num))
            return order
        
        nums = compress(nums)
        n = len(nums)
        segTree = SegmentTree(n)

        LIS = 0
        for num in nums:
            curLIS = segTree.query(0, num - 1) + 1
            segTree.update(num, curLIS)
            LIS = max(LIS, curLIS)
        return LIS
Time & Space Complexity
Time complexity: 
O
(
n
log
⁡
n
)
O(nlogn)
Space complexity: 
O
(
n
)
O(n)
5. Binary Search
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]: 
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i] 

        return LIS
Time & Space Complexity
Time complexity: 
O
(
n
log
⁡
n
)
O(nlogn)
Space complexity: 
O
(
n
)
O(n)