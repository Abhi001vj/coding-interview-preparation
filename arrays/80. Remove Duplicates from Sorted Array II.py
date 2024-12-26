# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
# 80. Remove Duplicates from Sorted Array II
# Medium
# Topics
# Companies
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

"""
Remove Duplicates from Sorted Array II - Solution Evolution
========================================================

Problem Summary:
--------------
Given a sorted array, modify it in-place so each element appears at most twice.
Keep relative order and return the length of the modified array.

Visual Examples:
-------------
Input: [1,1,1,2,2,3]
Steps:     v
[1,1,1,2,2,3]  Initial array
[1,1,_,2,2,3]  Remove extra 1
[1,1,2,2,3,_]  Shift elements left
Output: 5 (length of [1,1,2,2,3])

Input: [0,0,1,1,1,1,2,3,3]
Steps:       v v
[0,0,1,1,1,1,2,3,3]  Initial array
[0,0,1,1,_,_,2,3,3]  Remove extra 1s
[0,0,1,1,2,3,3,_,_]  Shift elements left
Output: 7 (length of [0,0,1,1,2,3,3])
"""

class DuplicateRemovalSolutions:
    def approach1_brute_force(self, nums: List[int]) -> int:
        """
        Brute Force Approach
        ------------------
        Strategy: Count frequencies and rebuild array
        
        Time Complexity: O(n²) - shifting elements for each removal
        Space Complexity: O(1) - in-place modification
        """
        if not nums:
            return 0
            
        i = 0
        while i < len(nums) - 2:
            # If found more than 2 same elements
            if nums[i] == nums[i+1] == nums[i+2]:
                # Shift all elements to the left
                for j in range(i+2, len(nums)-1):
                    nums[j] = nums[j+1]
                # Stay at same index to check new element
            else:
                i += 1
                
        return i + 2

    def approach2_two_pointers(self, nums: List[int]) -> int:
        """
        Two Pointers Approach
        -------------------
        Strategy: Use read/write pointers to overwrite duplicates
        
        Time Complexity: O(n) - single pass
        Space Complexity: O(1) - in-place modification
        
        Visual:
        write
         v
        [1,1,1,2,2,3]
           read
            v
        """
        if len(nums) <= 2:
            return len(nums)
            
        # Write pointer starts at index 2
        write = 2
        
        # Read pointer scans through array
        for read in range(2, len(nums)):
            # If current number is different from two positions back
            # it's safe to write (allows at most two duplicates)
            if nums[read] != nums[write-2]:
                nums[write] = nums[read]
                write += 1
                
        return write

    def approach3_general_k_duplicates(self, nums: List[int], k: int = 2) -> int:
        """
        General Solution for K Duplicates
        ------------------------------
        Strategy: Track last k elements to allow k duplicates
        Can handle any number of allowed duplicates
        
        Time Complexity: O(n) - single pass
        Space Complexity: O(1) - in-place modification
        """
        if len(nums) <= k:
            return len(nums)
            
        # Write pointer
        write = k
        
        # Scan through array starting after k elements
        for read in range(k, len(nums)):
            # If current number is different from k positions back,
            # it's safe to write
            if nums[read] != nums[write-k]:
                nums[write] = nums[read]
                write += 1
                
        return write

    def demonstrate_solutions(self):
        """Test all approaches with example cases."""
        test_cases = [
            ([1,1,1,2,2,3], "Example 1: Basic case"),
            ([0,0,1,1,1,1,2,3,3], "Example 2: Multiple duplicates"),
            ([1,1,1,1], "Example 3: All same numbers"),
            ([1,2,3,4], "Example 4: No duplicates"),
            ([], "Example 5: Empty array")
        ]
        
        approaches = [
            (self.approach1_brute_force, "Brute Force"),
            (self.approach2_two_pointers, "Two Pointers"),
            (self.approach3_general_k_duplicates, "General K-duplicates")
        ]
        
        print("Testing Solutions:")
        print("=================")
        
        for nums, case_name in test_cases:
            print(f"\n{case_name}:")
            print(f"Input: {nums}")
            
            for approach, name in approaches:
                # Create copy of array for each approach
                test_nums = nums.copy()
                k = approach(test_nums)
                print(f"{name}: k={k}, array={test_nums[:k]}")

def visualize_array_modification(nums: List[int]) -> None:
    """
    Helper function to visualize array modification steps
    """
    write = 2
    print("Initial array:", nums)
    
    for read in range(2, len(nums)):
        print(f"\nStep {read-1}:")
        print("Read pointer at index", read, "value =", nums[read])
        print("Write pointer at index", write)
        
        if nums[read] != nums[write-2]:
            nums[write] = nums[read]
            write += 1
            print("After modification:", nums[:write], end="")
            if write < len(nums):
                print("", nums[write:])
        else:
            print("Skip duplicate:", nums[:write], end="")
            if write < len(nums):
                print("", nums[write:])

def main():
    """
    Main function to demonstrate and explain solutions
    """
    solver = DuplicateRemovalSolutions()
    
    print("Understanding the Two Pointers Solution:")
    print("====================================")
    example = [1,1,1,2,2,3]
    print("\nExample array:", example)
    visualize_array_modification(example.copy())
    
    print("\nTesting All Solutions:")
    solver.demonstrate_solutions()
    
    print("\nKey Insights:")
    print("============")
    print("1. Sorted Array Properties:")
    print("   - Duplicates are adjacent")
    print("   - Can compare with previous elements")
    
    print("\n2. Two Pointers Pattern:")
    print("   - Read pointer scans array")
    print("   - Write pointer maintains result")
    print("   - Compare with k positions back")
    
    print("\n3. In-place Modification:")
    print("   - Overwrite duplicates")
    print("   - No extra space needed")
    print("   - Keep relative order")

if __name__ == "__main__":
    main()

"""
Key Learning Points:
-----------------
1. Array Manipulation:
   - In-place modification techniques
   - Two-pointer pattern variations
   - Handling duplicates in sorted arrays

2. Solution Evolution:
   - Brute force to optimal
   - Space-time trade-offs
   - Generalization patterns

3. Edge Cases:
   - Empty array
   - All duplicates
   - No duplicates
   - Array smaller than k
"""