# https://leetcode.com/problems/sort-colors/description/
# 75. Sort Colors
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

"""
Sort Colors (Dutch National Flag Problem) - Solution Analysis
=========================================================

Problem Essence:
--------------
Sort an array containing only 0s, 1s, and 2s in-place.
This is a variation of Dutch National Flag problem invented by Edsger Dijkstra.

Visual Representation:
-------------------
Initial array:  [2, 0, 2, 1, 1, 0]
We want to partition into three regions:
[0s (red) | 1s (white) | 2s (blue)]

Key Insight: Use three pointers to maintain regions
low    mid    high
 ↓      ↓      ↓
[0, 0 | 1, 1 | 2, 2]
  red  white   blue
"""

from typing import List

class DutchFlagSolutions:
    def approach1_counting_sort(self, nums: List[int]) -> None:
        """
        Counting Sort Approach
        --------------------
        Strategy:
        1. Count frequencies of 0s, 1s, and 2s
        2. Overwrite array with correct counts
        
        Time Complexity: O(n) - two passes through array
        Space Complexity: O(1) - only three counters needed
        
        Interview Note: Good starting point to demonstrate problem understanding
        """
        # Count frequencies
        counts = [0, 0, 0]  # counts[i] represents count of number i
        for num in nums:
            counts[num] += 1
            
        # Overwrite array with sorted values
        index = 0
        for i in range(3):
            for _ in range(counts[i]):
                nums[index] = i
                index += 1

    def approach2_two_passes(self, nums: List[int]) -> None:
        """
        Two-Pass Partitioning
        -------------------
        Strategy:
        1. First pass: Move all 0s to start
        2. Second pass: Move all 2s to end
        
        Time Complexity: O(n) - two passes
        Space Complexity: O(1) - in-place swaps
        
        Interview Note: Shows understanding of partitioning concept
        """
        # First pass: Move all 0s to the left
        write_idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[write_idx], nums[i] = nums[i], nums[write_idx]
                write_idx += 1
        
        # Second pass: Move all 2s to the right
        write_idx = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2 and i < write_idx:
                nums[write_idx], nums[i] = nums[i], nums[write_idx]
                write_idx -= 1

    def approach3_three_pointers(self, nums: List[int]) -> None:
        """
        Three-Pointer (Dutch National Flag) Algorithm
        -----------------------------------------
        Strategy:
        Maintain three pointers to partition array into four regions:
        [0s | 1s | unprocessed | 2s]
        
        Time Complexity: O(n) - single pass
        Space Complexity: O(1) - in-place swaps
        
        Interview Note: Optimal solution showing advanced algorithm knowledge
        """
        # Initialize pointers
        low = 0          # boundary for 0s (red)
        mid = 0          # current element (scanning pointer)
        high = len(nums) - 1  # boundary for 2s (blue)
        
        while mid <= high:
            if nums[mid] == 0:
                # Extend 0s region
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Extend 1s region
                mid += 1
            else:  # nums[mid] == 2
                # Extend 2s region
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Don't increment mid as new element needs checking

    def demonstrate_approaches(self):
        """
        Demonstrate and compare all approaches with visualization
        """
        test_cases = [
            ([2,0,2,1,1,0], "Standard case"),
            ([2,0,1], "Minimal case"),
            ([1,1,1,1], "All same values"),
            ([0,2,0,2,0], "No ones"),
            ([1,0,2,1,0,2], "Equal distribution")
        ]
        
        approaches = [
            (self.approach1_counting_sort, "Counting Sort"),
            (self.approach2_two_passes, "Two-Pass Partitioning"),
            (self.approach3_three_pointers, "Dutch National Flag")
        ]
        
        for nums, case_desc in test_cases:
            print(f"\nTest Case: {case_desc}")
            print(f"Input: {nums}")
            
            for approach, name in approaches:
                test_array = nums.copy()
                approach(test_array)
                print(f"{name}: {test_array}")

    def visualize_three_pointers(self, nums: List[int]) -> None:
        """
        Visualize the three-pointer algorithm step by step
        """
        def print_state(nums, low, mid, high):
            print("\nArray state:")
            for i in range(len(nums)):
                if i == low:
                    print("l", end="")
                if i == mid:
                    print("m", end="")
                if i == high:
                    print("h", end="")
                print(f" {nums[i]} ", end="")
            print("\nRegions: [0s: 0->low-1][1s: low->mid-1][unknown: mid->high][2s: high+1->end]")
        
        low = mid = 0
        high = len(nums) - 1
        
        print("Initial state:")
        print_state(nums, low, mid, high)
        
        while mid <= high:
            print(f"\nProcessing nums[{mid}] = {nums[mid]}")
            
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
            print_state(nums, low, mid, high)

def main():
    """
    Main function demonstrating comprehensive understanding of the problem
    """
    solver = DutchFlagSolutions()
    
    print("Dutch National Flag Problem Analysis")
    print("==================================")
    
    # Demonstrate progression of approaches
    solver.demonstrate_approaches()
    
    # Detailed visualization of optimal solution
    print("\nDetailed Three-Pointer Algorithm Visualization:")
    example = [2,0,2,1,1,0]
    solver.visualize_three_pointers(example.copy())
    
    print("\nTime-Space Complexity Analysis:")
    print("------------------------------")
    print("1. Counting Sort: O(n) time, O(1) space, two passes")
    print("2. Two-Pass: O(n) time, O(1) space, two passes")
    print("3. Three-Pointer: O(n) time, O(1) space, one pass")
    
    print("\nInterview Discussion Points:")
    print("-------------------------")
    print("1. Problem variants:")
    print("   - Sorting k distinct values")
    print("   - Stable sorting requirement")
    print("   - Parallel processing version")
    
    print("\n2. Follow-up questions:")
    print("   - Handling invalid inputs")
    print("   - Optimizing for different data distributions")
    print("   - Adapting for larger color spaces")

if __name__ == "__main__":
    main()

"""
Interview Meta-Analysis:
---------------------
1. Solution Evolution:
   - Start with simple counting approach
   - Progress to partitioning concept
   - Arrive at optimal three-pointer solution

2. Key Algorithm Patterns:
   - Multiple pointer technique
   - Partition-based sorting
   - State machine concepts

3. Code Quality Aspects:
   - Clear variable names
   - Comprehensive comments
   - Modular structure
   - Error handling consideration

4. System Design Connections:
   - Partitioning in distributed systems
   - In-place algorithms in memory-constrained environments
   - Stability considerations in real systems
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for color in nums:
            counts[color] += 1

        R, W, B = counts
        nums[:R] = [0] * R
        nums[R:R+W] = [1] * W
        nums[R+W:] = [2] * B
    
        return nums
