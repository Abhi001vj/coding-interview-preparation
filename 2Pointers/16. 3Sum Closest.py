# https://leetcode.com/problems/3sum-closest/description/
# 16. 3Sum Closest
# Medium
# Topics
# Companies
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

```python
"""
3Sum Closest Problem - Comprehensive Solution Analysis
=================================================

Core Concept:
-----------
Find three numbers in an array whose sum is closest to a given target.
Key observation: We can use sorting + two pointers to avoid checking all triplets.

Visualization of the approach:
[-4, -1, 1, 2], target = 1

After sorting:
     L  R
[-4, -1, 1, 2]
 ^
fixed

We fix one number and use two pointers for the remaining array.
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Find three integers in nums that sum closest to target.
        
        Time Complexity: O(n²) - One number fixed, two pointers for rest
        Space Complexity: O(1) - Only using pointers and variables
        
        Approach Visualization:
        nums = [-4, -1, 1, 2], target = 1
        
        Step 1: Sort the array
        [-4, -1, 1, 2]
        
        Step 2: For each number, use two pointers for rest:
        Fixed: -4
        [-4, -1, 1, 2]
             L     R    Sum = -4 + (-1) + 2 = -3
             L  R       Sum = -4 + (-1) + 1 = -4
        
        Fixed: -1
        [-4, -1, 1, 2]
              ^  L  R   Sum = -1 + 1 + 2 = 2 (closest!)
        
        And so on...
        """
        # Sort array to enable two-pointer technique
        nums.sort()
        n = len(nums)
        
        # Initialize closest sum with first three numbers
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Fix first number and use two pointers for remaining array
        for i in range(n - 2):
            # Skip duplicates for fixed number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize two pointers
            left = i + 1
            right = n - 1
            
            while left < right:
                # Calculate current sum
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If exact match found, return immediately
                if current_sum == target:
                    return target
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return closest_sum

    def visualize_process(self, nums: List[int], target: int) -> None:
        """
        Helper function to visualize the solution process step by step.
        """
        print(f"\nFinding closest sum to target {target} in array {nums}")
        
        # Sort array
        nums.sort()
        print(f"Sorted array: {nums}")
        
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            print(f"\nFixed number: {nums[i]}")
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                print(f"  Checking triplet: {nums[i]} + {nums[left]} + {nums[right]}"
                      f" = {current_sum} (diff from target: {abs(current_sum - target)})")
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    print(f"  New closest sum found: {closest_sum}")
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

def demonstrate_solution():
    """
    Demonstrate the solution with various test cases and explain the process.
    """
    test_cases = [
        ([-1, 2, 1, -4], 1),
        ([0, 0, 0], 1),
        ([1, 1, 1, 0], 100),
        ([-1, 2, 1, -4, 3, -3], 5)
    ]
    
    solution = Solution()
    
    for nums, target in test_cases:
        print("\n" + "="*50)
        print(f"Test Case: nums = {nums}, target = {target}")
        
        # Show step-by-step process
        solution.visualize_process(nums.copy(), target)
        
        # Get final result
        result = solution.threeSumClosest(nums.copy(), target)
        print(f"\nFinal Result: {result}")

if __name__ == "__main__":
    demonstrate_solution()

"""
Interview Tips and Key Insights:
-----------------------------
1. Problem-Solving Strategy:
   - Sort first to enable two-pointer technique
   - Fix one element and use two pointers for rest
   - Track closest sum using absolute difference
   - Handle duplicates for optimization

2. Optimization Techniques:
   - Skip duplicate values to avoid redundant calculations
   - Early termination on exact match
   - Sort array to enable efficient searching
   - Two-pointer technique reduces time complexity

3. Edge Cases to Consider:
   - All numbers same
   - Negative numbers
   - Target far from possible sums
   - Minimum array length (3)
   - Duplicates in array

4. Common Mistakes to Avoid:
   - Not handling duplicates
   - Incorrect pointer movements
   - Not updating closest sum properly
   - Missing edge cases
   - Wrong comparisons for updating result

5. Follow-up Questions to Prepare:
   - How to handle larger arrays?
   - What if we need k numbers instead of 3?
   - How to find all such triplets?
   - Can we optimize for special cases?
   - How to handle overflow?

6. Time/Space Complexity Analysis:
   Time: O(n²)
   - Sorting: O(n log n)
   - Two nested loops: O(n²)
   
   Space: O(1)
   - Only using constant extra space
   - Sorting might use O(log n) stack space
"""
```

Key points to emphasize in an interview:

1. **Initial Approach**:
   - Start with explaining why sorting helps
   - Mention the brute force approach first (O(n³))
   - Explain how two pointers optimize the solution

2. **Optimization Discussion**:
   - Handling duplicates
   - Early termination
   - Direction of pointer movement
   - Closest sum tracking

3. **Code Organization**:
   - Clear variable names
   - Helpful comments
   - Modular structure
   - Good error handling

4. **Testing Strategy**:
   - Start with simple cases
   - Edge cases
   - Invalid inputs
   - Performance testing

Would you like me to elaborate on any specific aspect or provide additional examples?