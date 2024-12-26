# 209. Minimum Size Subarray Sum
# Medium
# Topics
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = float('inf')
        l  = 0
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                min_length = min(min_length, r-l+1)
                summ -= nums[l]
                l += 1

        return min_length if min_length < float('inf') else 0
    

```python
"""
Minimum Size Subarray Sum - Comprehensive Solution Analysis
======================================================

Problem: Find the shortest subarray with sum ≥ target.

Let's explore multiple solutions:
1. Brute Force - Check all possible subarrays
2. Sliding Window - Optimal O(n) solution
3. Binary Search with Cumulative Sums - O(n log n) solution
"""

from typing import List
import sys

class MinSubarraySolutions:
    def approach1_brute_force(self, target: int, nums: List[int]) -> int:
        """
        Brute Force Solution: Check all possible subarrays
        
        Visual Example for target = 7, nums = [2,3,1,2,4,3]:
        Start at each index and try all lengths:
        
        Start at index 0:
        [2] = 2
        [2,3] = 5
        [2,3,1] = 6
        [2,3,1,2] = 8 ✓ (length 4)
        
        Start at index 1:
        [3] = 3
        [3,1] = 4
        [3,1,2] = 6
        [3,1,2,4] = 10 ✓ (length 4)
        
        And so on...
        
        Time: O(n²)
        Space: O(1)
        """
        n = len(nums)
        min_length = float('inf')
        
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                if current_sum >= target:
                    min_length = min(min_length, end - start + 1)
                    break
        
        return min_length if min_length != float('inf') else 0

    def approach2_sliding_window(self, target: int, nums: List[int]) -> int:
        """
        Sliding Window Solution: Maintain a window with sum ≥ target
        
        Visual Example for target = 7, nums = [2,3,1,2,4,3]:
        
        Window states:
        [2] = 2 < 7
        [2,3] = 5 < 7
        [2,3,1] = 6 < 7
        [2,3,1,2] = 8 ≥ 7, try shrinking
        [3,1,2] = 6 < 7
        [3,1,2,4] = 10 ≥ 7, try shrinking
        [1,2,4] = 7 ≥ 7, try shrinking
        [2,4] = 6 < 7
        [2,4,3] = 9 ≥ 7, try shrinking
        [4,3] = 7 ≥ 7 ✓ Best so far (length 2)
        
        Time: O(n)
        Space: O(1)
        """
        left = current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0

    def approach3_binary_search(self, target: int, nums: List[int]) -> int:
        """
        Binary Search Solution: Use prefix sums and binary search
        
        Visual Example for target = 7, nums = [2,3,1,2,4,3]:
        
        1. Create prefix sums:
        nums:    [2, 3, 1, 2, 4, 3]
        prefix:  [0, 2, 5, 6, 8, 12, 15]
        
        2. For each index i, binary search for smallest j where:
        prefix[j] - prefix[i] ≥ target
        
        Time: O(n log n)
        Space: O(n)
        """
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # Build prefix sum array
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            
        min_length = float('inf')
        
        # For each starting point
        for i in range(n):
            # Binary search for end point
            left, right = i + 1, n
            
            while left <= right:
                mid = (left + right) // 2
                current_sum = prefix_sum[mid] - prefix_sum[i]
                
                if current_sum >= target:
                    min_length = min(min_length, mid - i)
                    right = mid - 1
                else:
                    left = mid + 1
        
        return min_length if min_length != float('inf') else 0

    def visualize_process(self, target: int, nums: List[int]) -> None:
        """
        Helper function to visualize how each solution works.
        """
        print(f"\nInput: target = {target}, nums = {nums}")
        
        # Visualize sliding window approach
        print("\nSliding Window Process:")
        left = current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            print(f"Add nums[{right}] = {nums[right]}, Window sum = {current_sum}")
            
            while current_sum >= target:
                print(f"Window [{left}:{right+1}] = {nums[left:right+1]}, "
                      f"length = {right-left+1}")
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        # Visualize binary search approach
        print("\nBinary Search Process:")
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        print(f"Prefix sums: {prefix_sum}")

def demonstrate_solutions():
    """
    Test and compare all approaches with visualization.
    """
    test_cases = [
        (7, [2,3,1,2,4,3]),
        (4, [1,4,4]),
        (11, [1,1,1,1,1,1,1,1])
    ]
    
    solutions = MinSubarraySolutions()
    
    for target, nums in test_cases:
        print("\n" + "="*50)
        solutions.visualize_process(target, nums)
        
        # Compare results
        result1 = solutions.approach1_brute_force(target, nums)
        result2 = solutions.approach2_sliding_window(target, nums)
        result3 = solutions.approach3_binary_search(target, nums)
        
        print(f"\nResults:")
        print(f"Brute Force: {result1}")
        print(f"Sliding Window: {result2}")
        print(f"Binary Search: {result3}")

if __name__ == "__main__":
    demonstrate_solutions()

"""
Key Insights:

1. Solution Evolution:
   - Start with brute force to understand problem
   - Optimize with sliding window technique
   - Consider alternative with binary search

2. Sliding Window Pattern:
   - Grow window until condition met
   - Shrink window while maintaining condition
   - Track minimum window size

3. Binary Search Pattern:
   - Use prefix sums for range queries
   - Binary search for optimal endpoints
   - Trade space for time complexity

4. Important Edge Cases:
   - No valid subarray
   - Single element >= target
   - All elements too small
   - Target = sum of array
"""
```

Let me break down the key aspects of each solution:

1. **Brute Force Solution**:
   - Most straightforward approach
   - Check all possible subarrays
   - Good for understanding the problem
   - Inefficient for large inputs

2. **Sliding Window Solution** (Most Optimal):
   - Maintains a dynamic window
   - Grows when sum is too small
   - Shrinks when sum is large enough
   - Very efficient O(n) time complexity

3. **Binary Search Solution**:
   - Uses prefix sums for quick range sums
   - Binary searches for optimal endpoints
   - O(n log n) time complexity
   - Good when prefix sums already exist

Each approach teaches different problem-solving concepts:
1. How to optimize from brute force
2. When to use sliding window technique
3. How to apply binary search to optimization problems

Would you like me to:
1. Explain any specific approach in more detail?
2. Add more visualizations or examples?
3. Discuss specific optimization techniques?