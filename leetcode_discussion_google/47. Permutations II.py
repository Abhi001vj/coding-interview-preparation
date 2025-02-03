# https://leetcode.com/problems/permutations-ii/description/
# 47. Permutations II
# Medium
# Topics
# Companies
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

Initial State:
nums = [1,1,2] (sorted)
used = [F,F,F]
curr = []
result = []

Stack Trace Level 1 (Start):
backtrack(nums=[1,1,2], used=[F,F,F], curr=[])
    Try i=0 (first 1):
        used = [T,F,F]
        curr = [1]
        |
        ├── Stack Level 2:
        |   backtrack(nums=[1,1,2], used=[T,F,F], curr=[1])
        |   Try i=1 (second 1):
        |       used = [T,T,F]
        |       curr = [1,1]
        |       |
        |       ├── Stack Level 3:
        |       |   backtrack(nums=[1,1,2], used=[T,T,F], curr=[1,1])
        |       |   Try i=2 (2):
        |       |       used = [T,T,T]
        |       |       curr = [1,1,2]
        |       |       Found complete permutation: [1,1,2]
        |       |       Backtrack: remove 2
        |       |       curr = [1,1]
        |       |       used = [T,T,F]
        |       |
        |       Backtrack: remove second 1
        |       curr = [1]
        |       used = [T,F,F]
        |   
        |   Try i=2 (2):
        |       used = [T,F,T]
        |       curr = [1,2]
        |       |
        |       ├── Stack Level 3:
        |       |   backtrack(nums=[1,1,2], used=[T,F,T], curr=[1,2])
        |       |   Try i=1 (second 1):
        |       |       used = [T,T,T]
        |       |       curr = [1,2,1]
        |       |       Found complete permutation: [1,2,1]
        |       |       Backtrack: remove second 1
        |
        Backtrack: remove first 1
        curr = []
        used = [F,F,F]

    Try i=1 (second 1):
        SKIP! Previous 1 is unused (nums[1]=1, nums[0]=1, used[0]=F)

    Try i=2 (2):
        used = [F,F,T]
        curr = [2]
        |
        ├── Stack Level 2:
        |   backtrack(nums=[1,1,2], used=[F,F,T], curr=[2])
        |   Try i=0 (first 1):
        |       used = [T,F,T]
        |       curr = [2,1]
        |       |
        |       ├── Stack Level 3:
        |       |   backtrack(nums=[1,1,2], used=[T,F,T], curr=[2,1])
        |       |   Try i=1 (second 1):
        |       |       used = [T,T,T]
        |       |       curr = [2,1,1]
        |       |       Found complete permutation: [2,1,1]

Final Result: [[1,1,2], [1,2,1], [2,1,1]]