# https://leetcode.com/problems/combination-sum-ii/description/
# 40. Combination Sum II
# Solved
# Medium
# Topics
# Companies
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

"""
Visual representation of the algorithm:

For input [1,1,2,5,6,7,10] target=8

                                   []
                    1/              2|               5\
                [1]                [2]              [5]
            1/    2\    5\         5|  6\           6\
        [1,1]    [1,2]  [1,5]    [2,5] [2,6]      [5,6]
        2/  5\    5\     6\
    [1,1,2] [1,1,5] [1,2,5] [1,5,6]
    5/  6\    6\     6\
[1,1,2,5] [1,1,6] [1,2,5] 
           ✓         ✓

✓ indicates a valid solution
"""

def combinationSum2_bruteforce(candidates, target):
    """
    Brute force approach using backtracking
    Time Complexity: O(2^n)
    Space Complexity: O(n) for recursion stack
    """
    def backtrack(start, curr_sum, curr_combo):
        # Base case: if we've found a valid combination
        if curr_sum == target:
            result.append(curr_combo[:])
            return
        
        # Base case: if we've exceeded our target
        if curr_sum > target:
            return
        
        # Try each remaining candidate
        for i in range(start, len(candidates)):
            # Skip duplicates at the same level of recursion
            if i > start and candidates[i] == candidates[i-1]:
                continue
                
            # Add current number to combination
            curr_combo.append(candidates[i])
            
            # Recursively try next numbers
            backtrack(i + 1, curr_sum + candidates[i], curr_combo)
            
            # Backtrack by removing the last added number
            curr_combo.pop()
    
    # Sort candidates to handle duplicates
    candidates.sort()
    result = []
    backtrack(0, 0, [])
    return result

def combinationSum2_optimized(candidates, target):
    """
    Optimized solution using counter and pruning
    Time Complexity: O(2^n) worst case, but much better in practice
    Space Complexity: O(n) + O(unique numbers)
    """
    # Step 1: Create frequency map for optimization
    freq = {}
    for num in candidates:
        freq[num] = freq.get(num, 0) + 1
    
    # Convert to sorted unique numbers for processing
    nums = sorted(freq.keys())
    
    def backtrack(pos, remain_target, curr_combo):
        """
        pos: current position in nums array
        remain_target: remaining target to reach
        curr_combo: current combination being built
        """
        # Success case: we've found a valid combination
        if remain_target == 0:
            result.append(curr_combo[:])
            return
            
        # Base case: if we've gone through all numbers
        if pos >= len(nums):
            return
            
        # Get current number we're processing
        curr_num = nums[pos]
        
        # Early pruning: if smallest remaining number is too big
        if curr_num > remain_target:
            return
            
        # Try using current number 0 to freq[curr_num] times
        max_count = min(freq[curr_num], remain_target // curr_num)
        for count in range(max_count + 1):
            # Add 'count' copies of current number
            curr_combo.extend([curr_num] * count)
            
            # Recurse with updated target
            backtrack(pos + 1, 
                     remain_target - (curr_num * count), 
                     curr_combo)
            
            # Backtrack by removing added numbers
            for _ in range(count):
                curr_combo.pop()
    
    result = []
    backtrack(0, target, [])
    return result

# Test code with examples
if __name__ == "__main__":
    # Test Case 1
    candidates1 = [10,1,2,7,6,1,5]
    target1 = 8
    print("Brute Force Solution:")
    print(combinationSum2_bruteforce(candidates1, target1))
    print("\nOptimized Solution:")
    print(combinationSum2_optimized(candidates1, target1))
    
    # Test Case 2
    candidates2 = [2,5,2,1,2]
    target2 = 5
    print("\nTest Case 2:")
    print(combinationSum2_optimized(candidates2, target2))

"""
Key Optimizations Explained:

1. Frequency Counter:
   - Reduces duplicate processing by tracking count of each number
   - Allows us to handle each unique number once

2. Early Pruning:
   - Skip processing when current number > remaining target
   - Calculate maximum possible count for each number

3. Sorting:
   - Helps handle duplicates efficiently
   - Enables early termination when numbers get too large

4. Space-Time Tradeoff:
   - Uses extra space for frequency counter
   - Significantly reduces duplicate computation

Interview Follow-up Discussion Points:
1. How would you handle negative numbers?
2. What if the array was pre-sorted?
3. How would you parallelize this for very large inputs?
4. How would you modify for unlimited use of numbers?
"""