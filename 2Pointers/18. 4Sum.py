
# https://leetcode.com/problems/4sum/description/
# 18. 4Sum
# Medium
# Topics
# Companies
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

```python
"""
4Sum Problem - Comprehensive Solution Analysis
===========================================

The 4Sum problem extends the concepts of 2Sum and 3Sum to find quadruplets
that sum to a target value. Let's understand this through multiple approaches,
starting with easier solutions and progressing to optimized ones.

Core Concept:
We need to find all unique combinations of four numbers that sum to target.
Key challenge: Avoiding duplicate quadruplets while maintaining efficiency.
"""

from typing import List
from collections import defaultdict

class FourSumSolutions:
    def approach1_naive_sorting(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Basic sorting and nested loops approach.
        
        Time Complexity: O(n³) - Three nested loops with sorted array
        Space Complexity: O(1) - Not counting output space
        
        Visual example for nums = [1,0,-1,0,-2,2], target = 0:
        
        After sorting: [-2,-1,0,0,1,2]
        
        Iteration process:
        Fix first: -2
            Fix second: -1
                Use two pointers for remaining: [0,0,1,2]
                Found: [-2,-1,1,2]
        
        Fix first: -2
            Fix second: 0
                Use two pointers for remaining: [0,1,2]
                Found: [-2,0,0,2]
        
        And so on...
        """
        nums.sort()
        n = len(nums)
        results = []
        
        for i in range(n - 3):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Use two pointers for remaining two numbers
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return results

    def approach2_hash_based(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Hash map based approach using 2Sum concept.
        
        Time Complexity: O(n³) - Still three nested loops
        Space Complexity: O(n) - Hash map storage
        
        The idea is to use a hash map to store pair sums:
        1. Calculate all possible pair sums
        2. For each pair, look for complementary pair
        3. Combine pairs ensuring no duplicates
        """
        n = len(nums)
        nums.sort()  # Sort to handle duplicates easily
        pair_sums = defaultdict(list)
        results = set()  # Use set to avoid duplicates
        
        # Calculate all possible pair sums
        for i in range(n - 1):
            for j in range(i + 1, n):
                # Store indices for each sum
                current_sum = nums[i] + nums[j]
                pair_sums[current_sum].append((i, j))
                
        # Check each pair against complementary pairs
        for sum1, pairs1 in pair_sums.items():
            complement = target - sum1
            
            if complement in pair_sums:
                # Try combining pairs
                for i1, j1 in pairs1:
                    for i2, j2 in pair_sums[complement]:
                        # Ensure no index overlap
                        if i1 != i2 and i1 != j2 and j1 != i2 and j1 != j2:
                            # Create sorted quadruplet to avoid duplicates
                            quad = sorted([nums[i1], nums[j1], nums[i2], nums[j2]])
                            results.add(tuple(quad))
                            
        return [list(quad) for quad in results]

    def approach3_k_sum_recursive(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Generalized k-sum solution using recursion.
        This approach can be extended to solve for any k-sum problem.
        
        Time Complexity: O(n³) for 4Sum
        Space Complexity: O(k) for recursion stack
        
        The recursive approach breaks down k-sum into smaller subproblems:
        4Sum → 3Sum → 2Sum
        """
        def kSum(start: int, k: int, target: int) -> List[List[int]]:
            results = []
            
            # Base case: 2Sum problem
            if k == 2:
                left, right = start, len(nums) - 1
                
                while left < right:
                    current_sum = nums[left] + nums[right]
                    
                    if current_sum == target:
                        results.append([nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
            else:
                # Recursive case: reduce to (k-1)Sum
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                        
                    # Recursively solve for k-1 numbers
                    sub_results = kSum(i + 1, k - 1, target - nums[i])
                    
                    # Add current number to all sub-results
                    for sub_result in sub_results:
                        results.append([nums[i]] + sub_result)
                        
            return results
        
        nums.sort()
        return kSum(0, 4, target)

    def visualize_solution(self, nums: List[int], target: int) -> None:
        """
        Helper function to visualize the solution process step by step.
        """
        print(f"\nFinding 4Sum quadruplets for target {target}")
        print(f"Input array: {nums}")
        
        nums.sort()
        print(f"Sorted array: {nums}")
        
        print("\nProcessing quadruplets:")
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            print(f"\nFirst number fixed: {nums[i]}")
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                print(f"  Second number fixed: {nums[j]}")
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    print(f"    Testing: {nums[i]} + {nums[j]} + {nums[left]} + "
                          f"{nums[right]} = {current_sum}")
                    
                    if current_sum == target:
                        print(f"    Found quadruplet: [{nums[i]},{nums[j]},"
                              f"{nums[left]},{nums[right]}]")
                    
                    if current_sum < target:
                        left += 1
                    else:
                        right -= 1

def demonstrate_solutions():
    """
    Test and compare all approaches with various test cases.
    """
    test_cases = [
        ([1,0,-1,0,-2,2], 0),
        ([2,2,2,2,2], 8),
        ([-3,-2,-1,0,0,1,2,3], 0),
        ([0,0,0,0], 0)
    ]
    
    solver = FourSumSolutions()
    
    for nums, target in test_cases:
        print("\n" + "="*50)
        print(f"Test Case: nums = {nums}, target = {target}")
        
        # Visualize process
        solver.visualize_solution(nums.copy(), target)
        
        # Compare results from different approaches
        result1 = solver.approach1_naive_sorting(nums.copy(), target)
        result2 = solver.approach2_hash_based(nums.copy(), target)
        result3 = solver.approach3_k_sum_recursive(nums.copy(), target)
        
        print("\nResults:")
        print(f"Naive Sorting: {result1}")
        print(f"Hash Based: {result2}")
        print(f"Recursive k-Sum: {result3}")

if __name__ == "__main__":
    demonstrate_solutions()

```

The solution demonstrates several key concepts for technical interviews:

1. **Solution Evolution**:
   - Starting with basic sorting approach
   - Moving to hash-based optimization
   - Generalizing to k-sum problem
   - Each approach teaches different algorithmic concepts

2. **Pattern Recognition**:
   - Two pointer technique
   - Hash map usage
   - Recursive problem decomposition
   - Duplicate handling

3. **Optimization Techniques**:
   - Early termination
   - Skip duplicates
   - Space-time tradeoffs
   - Problem generalization

4. **Interview Tips**:
   - Start with the simplest solution
   - Explain tradeoffs between approaches
   - Discuss scalability concerns
   - Handle edge cases carefully
   - Show understanding of time/space complexity

Would you like me to explain any particular aspect in more detail?


```python
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique quadruplets that sum to target using a two-pointer approach.
    Let's understand this with a detailed example.
    
    Example visualization using nums = [1,0,-1,0,-2,2], target = 0
    
    Step 1: Sort the array
    [-2,-1,0,0,1,2]  # This enables us to use two pointers
    
    Step 2: Use two fixed pointers (i,j) and two moving pointers (lo,hi)
    i  j lo      hi
    -2 -1 0...2   # Fixed points + sliding window
    
    Visual Process:
    1) First iteration:
    i  j  lo hi
    -2 -1  0  2  → sum = -1 (too small, move lo)
    -2 -1  1  2  → sum = 0 (found! [-2,-1,1,2])
    
    2) Next j iteration:
    i  j   lo hi
    -2  0   0  2  → sum = 0 (found! [-2,0,0,2])
    
    And so on...
    """
    n = len(nums)
    answer = []
    nums.sort()  # Sort to handle duplicates and enable two pointers

    # First fixed pointer i
    for i in range(n):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Second fixed pointer j
        for j in range(i+1, n):
            # Skip duplicates for j
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            
            # Two moving pointers: lo and hi
            lo, hi = j+1, n-1
            
            # Two-pointer technique
            while lo < hi:
                summ = nums[i] + nums[j] + nums[lo] + nums[hi]
                
                if summ == target:
                    # Found a valid quadruplet
                    answer.append([nums[i], nums[j], nums[lo], nums[hi]])
                    
                    # Move both pointers
                    lo += 1
                    hi -= 1
                    
                    # Skip duplicates for lo
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    # Skip duplicates for hi
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                        
                elif summ < target:
                    # Sum too small, increase lo
                    lo += 1
                else:
                    # Sum too large, decrease hi
                    hi -= 1

    return answer

"""
Let's break down a complete example:
nums = [1,0,-1,0,-2,2], target = 0

1. After sorting: [-2,-1,0,0,1,2]

2. First iteration (i = 0, nums[i] = -2):
   [-2, -1, 0, 0, 1, 2]
    i   j  lo    hi
   
   Check combinations:
   - [-2,-1,0,2] = -1 (too small)
   - [-2,-1,1,2] = 0 ✓ (add to answer)

3. Second iteration (i = 0, j = 2):
   [-2, -1, 0, 0, 1, 2]
    i      j  lo hi
   
   Check combinations:
   - [-2,0,0,2] = 0 ✓ (add to answer)

4. Next iterations:
   Similar process for remaining combinations
   Eventually finds [-1,0,0,1]

Key Points to Remember:
1. Sorting enables two-pointer technique
2. Skip duplicates at all levels (i, j, lo, hi)
3. Four nested levels of iteration but optimized by two pointers
4. Move pointers based on sum comparison with target
"""
```

This solution is elegant because:

1. **Efficient Duplicate Handling**: 
   - Uses sorting to make duplicates adjacent
   - Skips duplicates at each level to avoid redundant work
   - Ensures unique quadruplets without using extra space

2. **Two-Pointer Optimization**: 
   - Reduces time complexity from O(n⁴) to O(n³)
   - Enables linear scanning of remaining elements
   - Provides directional guidance based on sum comparison

3. **Clean Implementation**: 
   - Logical structure with fixed and moving pointers
   - Clear duplicate handling at each level
   - Straightforward sum comparison and pointer movement

4. **Space Efficiency**: 
   - O(1) extra space (not counting the output array)
   - In-place sorting
   - No additional data structures needed

Would you like me to elaborate on any particular aspect of the solution?