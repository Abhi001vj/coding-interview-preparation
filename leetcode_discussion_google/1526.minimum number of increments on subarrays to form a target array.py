# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
# Solved
# Hard
# Topics
# Companies
# Hint
# You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.

# In one operation you can choose any subarray from initial and increment each value by one.

# Return the minimum number of operations to form a target array from initial.

# The test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: target = [1,2,3,2,1]
# Output: 3
# Explanation: We need at least 3 operations to form the target array from the initial array.
# [0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
# [1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
# [1,2,2,2,1] increment 1 at index 2.
# [1,2,3,2,1] target array is formed.
# Example 2:

# Input: target = [3,1,1,2]
# Output: 4
# Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
# Example 3:

# Input: target = [3,1,5,4,2]
# Output: 7
# Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2].
 

# Constraints:

# 1 <= target.length <= 105
# 1 <= target[i] <= 105
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 54.9K
# Submissions
# 76.2K
# Acceptance Rate
# 72.0%
# Topics
# Companies
# Hint 1
# For a given range of values in target, an optimal strategy is to increment the entire range by the minimum value. The minimum in a range could be obtained with Range minimum query or Segment trees algorithm.

# Problem Analysis:
# ----------------
# Given: target array, start with all zeros
# Operation: increment any subarray by 1
# Goal: minimum operations to form target
#
# Key Insights:
# 1. We can only increment (no decrements)
# 2. Starting from all zeros means we need at least max(target) operations
# 3. For adjacent elements:
#    - If next element is higher, we need extra operations
#    - If next element is lower, we can reuse previous operations
#
# Example 1 Visualization:
# target = [1,2,3,2,1]
#
# Step 1: [0,0,0,0,0] -> [1,1,1,1,1]
#          ↑ ↑ ↑ ↑ ↑
#          +1+1+1+1+1
#
# Step 2: [1,1,1,1,1] -> [1,2,2,2,1]
#            ↑ ↑ ↑
#            +1+1+1
#
# Step 3: [1,2,2,2,1] -> [1,2,3,2,1]
#              ↑
#              +1
#
# Solution Approaches:
# ------------------
# 1. Brute Force (not recommended):
#    - Try all possible subarrays
#    - Time: O(n³)
#    - Space: O(n)
#
# 2. Greedy with Differences (optimal):
#    - Focus on differences between adjacent elements
#    - Time: O(n)
#    - Space: O(1)

from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Optimal Solution using Greedy approach
        Time Complexity: O(n) where n is length of array
        Space Complexity: O(1) 
        
        The key insight is:
        1. We need at least target[0] operations to reach first element
        2. For each position i:
           - If target[i] > target[i-1]: need (target[i] - target[i-1]) more operations
           - If target[i] <= target[i-1]: no extra operations needed
        """
        operations = target[0]  # Need these many to reach first element
        
        # For each subsequent element
        for i in range(1, len(target)):
            # If current element is larger than previous
            # We need extra operations to cover the difference
            if target[i] > target[i-1]:
                operations += target[i] - target[i-1]
        
        return operations

    def minNumberOperationsBruteForce(self, target: List[int]) -> int:
        """
        Brute Force solution - NOT RECOMMENDED for interview
        Time Complexity: O(n³)
        Space Complexity: O(n)
        """
        def try_all_operations(curr):
            if curr == target:
                return 0
            min_ops = float('inf')
            n = len(curr)
            
            # Try all possible subarrays
            for i in range(n):
                for j in range(i, n):
                    # Increment subarray by 1
                    next_state = curr.copy()
                    for k in range(i, j+1):
                        next_state[k] += 1
                    min_ops = min(min_ops, 1 + try_all_operations(next_state))
            
            return min_ops
        
        return try_all_operations([0] * len(target))

# Test cases
def test():
    solution = Solution()
    
    # Test Case 1
    assert solution.minNumberOperations([1,2,3,2,1]) == 3
    
    # Test Case 2
    assert solution.minNumberOperations([3,1,1,2]) == 4
    
    # Test Case 3
    assert solution.minNumberOperations([3,1,5,4,2]) == 7
    
    print("All test cases passed!")

# Run tests
if __name__ == "__main__":
    test()

"""
Detailed Analysis:

Why Greedy Works:
----------------
1. First element needs target[0] operations
2. For each subsequent element i:
   - If target[i] > target[i-1]: we must add operations
   - If target[i] <= target[i-1]: we can reuse operations

Example Step by Step:
--------------------
target = [3,1,5,4,2]

1. First element (3):
   - Need 3 operations
   operations = 3

2. Second element (1):
   - Lower than previous (3)
   - Can reuse operations
   operations = 3

3. Third element (5):
   - Higher than previous (1)
   - Need 4 more operations
   operations = 7

4. Fourth element (4):
   - Lower than previous (5)
   - Can reuse operations
   operations = 7

5. Fifth element (2):
   - Lower than previous (4)
   - Can reuse operations
   operations = 7

Final result = 7 operations

Edge Cases Handled:
------------------
1. Single element array
2. All elements same
3. Strictly increasing array
4. Strictly decreasing array
5. Array with alternating values
"""