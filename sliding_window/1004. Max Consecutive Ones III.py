# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# 1004. Max Consecutive Ones III
# Medium
# Topics
# Companies
# Hint
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


```python
"""
Max Consecutive Ones III - Comprehensive Analysis
==============================================

Core Concept:
We want to find the longest sequence of consecutive 1s we can create by flipping
at most k zeros. This is effectively a sliding window problem where we're looking
for the longest window that contains at most k zeros.

Let's explore multiple approaches to solve this:
1. Basic Sliding Window 
2. Optimized Sliding Window with Zero Count
3. Prefix Sum with Binary Search
"""

class Solution:
    def approach1_basic_sliding_window(self, nums: List[int], k: int) -> int:
        """
        Basic Sliding Window Approach
        ---------------------------
        Maintain a window and track zeros within it.
        
        Visual Example:
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        
        Window states:
        [1] -> [1,1] -> [1,1,1] -> [1,1,1,0] -> [1,1,1,0,0] ->
        can't expand (would exceed k zeros) -> start shrinking ->
        [1,1,0,0] -> [1,0,0] -> [0,0] -> [0] -> []
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = curr_zeros = max_ones = 0
        
        for right in range(len(nums)):
            # Add new element to window
            if nums[right] == 0:
                curr_zeros += 1
            
            # Shrink window while we have too many zeros
            while curr_zeros > k:
                if nums[left] == 0:
                    curr_zeros -= 1
                left += 1
            
            # Update maximum window size
            max_ones = max(max_ones, right - left + 1)
        
        return max_ones

    def approach2_optimized_sliding_window(self, nums: List[int], k: int) -> int:
        """
        Optimized Sliding Window Approach
        ------------------------------
        Instead of explicitly tracking zeros, we use the window size and ones count.
        
        Example visualization:
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        
        Window: [1,1,1]     ones=3, size=3, zeros=0
        Window: [1,1,1,0]   ones=3, size=4, zeros=1
        Window: [1,1,1,0,0] ones=3, size=5, zeros=2
        ...and so on
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = curr_ones = max_window = 0
        
        for right in range(len(nums)):
            # Count ones in current window
            if nums[right] == 1:
                curr_ones += 1
            
            # Current window size
            window_size = right - left + 1
            
            # If number of zeros in window > k, shrink window
            if window_size - curr_ones > k:
                if nums[left] == 1:
                    curr_ones -= 1
                left += 1
            
            # Update maximum window size
            max_window = max(max_window, right - left + 1)
        
        return max_window

    def approach3_prefix_sum(self, nums: List[int], k: int) -> int:
        """
        Prefix Sum with Binary Search Approach
        ----------------------------------
        Use prefix sum to count ones and binary search for valid windows.
        
        Example:
        nums = [1,1,1,0,0,0,1,1,1,1,0]
        prefix = [0,1,2,3,3,3,3,4,5,6,7,7]
        
        For each index i, binary search for largest j where
        zeros in window (j-i) - (prefix[j]-prefix[i]) <= k
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        
        # Build prefix sum array
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        max_length = 0
        
        # For each starting point
        for i in range(n):
            left, right = i, n
            
            # Binary search for largest valid window
            while left < right:
                mid = (left + right + 1) // 2
                zeros = (mid - i) - (prefix[mid] - prefix[i])
                
                if zeros <= k:
                    left = mid
                else:
                    right = mid - 1
            
            max_length = max(max_length, left - i)
        
        return max_length

def visualize_solutions():
    """
    Helper function to visualize how each approach works.
    """
    test_cases = [
        ([1,1,1,0,0,0,1,1,1,1,0], 2),
        ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
    ]
    
    solution = Solution()
    
    for nums, k in test_cases:
        print(f"\nTest case: nums = {nums}, k = {k}")
        
        # Demonstrate window movement for first approach
        print("\nSliding Window Visualization:")
        left = zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            window = nums[left:right+1]
            print(f"Window: {window}, Zeros: {zeros}")
        
        # Compare results from all approaches
        result1 = solution.approach1_basic_sliding_window(nums, k)
        result2 = solution.approach2_optimized_sliding_window(nums, k)
        result3 = solution.approach3_prefix_sum(nums, k)
        
        print(f"\nResults:")
        print(f"Basic Sliding Window: {result1}")
        print(f"Optimized Sliding Window: {result2}")
        print(f"Prefix Sum: {result3}")

if __name__ == "__main__":
    visualize_solutions()

"""
Key Insights and Patterns:

1. Window Management:
   - Expanding window when valid (zeros ≤ k)
   - Shrinking window when invalid (zeros > k)
   - Tracking window state efficiently

2. Optimization Techniques:
   - Using window size vs explicit zero counting
   - Prefix sums for quick range queries
   - Binary search for optimal windows

3. Trade-offs:
   - Time vs Space complexity
   - Code simplicity vs Performance
   - Memory usage vs Computation speed

4. Edge Cases:
   - All zeros
   - All ones
   - k = 0
   - k = length of array
"""
```

The problem can be solved using several approaches, each with its own advantages:

1. **Basic Sliding Window**:
   - Most intuitive approach
   - Easy to understand and implement
   - Good balance of efficiency and simplicity

2. **Optimized Sliding Window**:
   - More efficient state tracking
   - Fewer operations per window adjustment
   - Better space utilization

3. **Prefix Sum**:
   - Different perspective on the problem
   - Enables binary search optimization
   - Better for certain input patterns

Key concepts to understand:
1. Window validity based on zero count
2. Efficient state tracking
3. Optimal window size determination

Would you like me to:
1. Explain any specific approach in more detail?
2. Add more examples or visualizations?
3. Discuss specific optimization techniques?


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        num_zeros = 0
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] == 0:
                num_zeros += 1
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            
            w = r - l + 1
            max_w = max(max_w, w)
        return max_w