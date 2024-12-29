# https://leetcode.com/problems/sliding-window-median/

# Code


# Testcase
# Testcase
# Test Result
# 480. Sliding Window Median
# Hard
# Topics
# Companies
# Hint
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation: 
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7        3
#  1  3  -1  -3 [5  3  6] 7        5
#  1  3  -1  -3  5 [3  6  7]       6
# Example 2:

# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 166.6K
# Submissions
# 430.2K
# Acceptance Rate
# 38.7%
# Topics
# Companies
# Hint 1
# The simplest of solutions comes from the basic idea of finding the median given a set of numbers. We know that by definition, a median is the center element (or an average of the two center elements). Given an unsorted list of numbers, how do we find the median element? If you know the answer to this question, can we extend this idea to every sliding window that we come across in the array?
# Hint 2
# Is there a better way to do what we are doing in the above hint? Don't you think there is duplication of calculation being done there? Is there some sort of optimization that we can do to achieve the same result? This approach is merely a modification of the basic approach except that it simply reduces duplication of calculations once done.
# Hint 3
# The third line of thought is also based on this same idea but achieving the result in a different way. We obviously need the window to be sorted for us to be able to find the median. Is there a data-structure out there that we can use (in one or more quantities) to obtain the median element extremely fast, say O(1) time while having the ability to perform the other operations fairly efficiently as well?


"""
Sliding Window Median (LeetCode 480)

Core Challenge:
- Find median for each window of size k as it slides through array
- Handle both odd and even window sizes
- Process efficiently for large arrays
- Maintain sorted order efficiently for each window

Key Patterns Identified:
1. Sliding Window
2. Heap Usage (Two Heaps)
3. Balanced Data Structures
4. Running Median Maintenance

Let's analyze multiple approaches:

Approach 1: Brute Force with Sorting
Time: O(n * k log k) - sort each window
Space: O(k) for the window array

Visual Example:
nums = [1,3,-1,-3,5,3,6,7], k = 3

Window visualization:
[1,3,-1] → sort → [-1,1,3] → median = 1
[3,-1,-3] → sort → [-3,-1,3] → median = -1
[-1,-3,5] → sort → [-3,-1,5] → median = -1
...

Process:
1. Extract k elements
2. Sort them
3. Find median
4. Slide window
"""

def median_sliding_window_brute(nums: List[int], k: int) -> List[float]:
    """
    Brute force solution using sorting
    Time: O(n * k log k)
    Space: O(k)
    """
    def get_median(sorted_window):
        if len(sorted_window) % 2 == 0:
            return (sorted_window[k//2-1] + sorted_window[k//2]) / 2
        return float(sorted_window[k//2])
    
    result = []
    for i in range(len(nums) - k + 1):
        # Extract and sort current window
        window = sorted(nums[i:i+k])
        result.append(get_median(window))
    return result

"""
Approach 2: Insertion Sort Optimization
Time: O(n * k) - maintain sorted window using insertion
Space: O(k) for the window array

Key Insight: Each window differs by only one element from previous
Therefore, we can maintain sortedness more efficiently

Visual Example:
nums = [1,3,-1,-3,5], k = 3

Window transitions:
[1,3,-1] sorted: [-1,1,3]
Remove 1, Add -3:
[-1,3,-3] → insertion sort → [-3,-1,3]

Process:
1. Initially sort first window
2. For each slide:
   - Remove old element (binary search)
   - Insert new element (binary search)
   - Find median
"""

from bisect import insort, bisect_left

def median_sliding_window_insertion(nums: List[int], k: int) -> List[float]:
    """
    Optimized solution using insertion sort
    Time: O(n * k)
    Space: O(k)
    """
    def get_median(window):
        if k % 2 == 0:
            return (window[k//2-1] + window[k//2]) / 2
        return float(window[k//2])
    
    # Initialize first window
    window = sorted(nums[:k])
    result = [get_median(window)]
    
    for i in range(k, len(nums)):
        # Remove old element
        window.pop(bisect_left(window, nums[i-k]))
        # Insert new element
        insort(window, nums[i])
        result.append(get_median(window))
    
    return result

"""
Approach 3: Two Heaps (Optimal Solution)
Time: O(n * log k)
Space: O(k)

Key Insight: Use two heaps to maintain median position
- Max heap for smaller half
- Min heap for larger half

Visual Example:
nums = [1,3,-1], k = 3

Heap States:
1. Add 1:
small: []     large: [1]

2. Add 3:
small: [-1]   large: [3]
       ↑
    median boundary

3. Add -1:
small: [-1,-1]   large: [3]
         ↑
     median boundary

Process Visualization:
           small heap │ large heap
Initial:        []    │    [1]
Add 3:         [1]    │    [3]
Add -1:     [-1,1]    │    [3]

Memory Layout:
┌─────────┐ ┌─────────┐
│ MaxHeap │ │ MinHeap │
│ smaller │ │ larger  │
│ half    │ │ half    │
└─────────┘ └─────────┘
"""

from heapq import heappush, heappop
from collections import defaultdict

def median_sliding_window_optimal(nums: List[int], k: int) -> List[float]:
    """
    Optimal solution using two heaps
    Time: O(n * log k)
    Space: O(k)
    
    Why O(n * log k)?
    - For each element (n iterations):
        - Heap push/pop operations: O(log k)
        - Getting median: O(1)
        - Cleanup operations: amortized O(log k)
    """
    def get_median(s, l, k):
        return float(l[0]) if k % 2 else (l[0] - s[0]) / 2
    
    # Initialize heaps and removal tracking
    small = []  # max heap (-ve numbers)
    large = []  # min heap
    removed = defaultdict(int)  # track elements to be removed
    
    # Helper to remove elements marked for deletion
    def clean_top():
        while small and removed[-small[0]] > 0:
            removed[-heappop(small)] -= 1
        while large and removed[large[0]] > 0:
            removed[heappop(large)] -= 1
    
    # Helper to rebalance heaps
    def rebalance():
        while len(small) > len(large):
            heappush(large, -heappop(small))
        while len(large) > len(small) + 1:
            heappush(small, -heappop(large))
    
    # Process first window
    for i in range(k):
        heappush(small, -nums[i])
        heappush(large, -heappop(small))
        if len(large) > len(small) + 1:
            heappush(small, -heappop(large))
    
    result = [get_median(small, large, k)]
    
    # Process remaining windows
    for i in range(k, len(nums)):
        # Mark outgoing element for removal
        removed[nums[i-k]] += 1
        
        # Add new element
        if nums[i] >= large[0]:
            heappush(large, nums[i])
        else:
            heappush(small, -nums[i])
        
        # Clean and rebalance
        clean_top()
        rebalance()
        
        # Calculate median
        result.append(get_median(small, large, k))
    
    return result

"""
Why Two Heaps is Optimal:

1. Efficient Median Access: O(1)
   - Median always at heap boundaries
   - No need to sort entire window

2. Efficient Updates: O(log k)
   - Heap operations logarithmic
   - Only affected elements need movement

3. Space Efficient: O(k)
   - Only store window elements
   - Constant overhead for tracking removals

Trade-offs Analysis:

Brute Force:
+ Simple to implement
+ Good for small k
- Poor for large windows
- Redundant sorting work

Insertion Sort:
+ Better than brute force
+ Maintains sortedness
- Still linear window operations
- Complex removal process

Two Heaps:
+ Optimal time complexity
+ Constant time median access
- More complex implementation
- Memory overhead for removal tracking

Example Test Cases:

1. Basic odd-length window:
nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]

2. Even-length window:
nums = [1,2,3,4], k = 2
Output: [1.50000,2.50000,3.50000]

3. Single element window:
nums = [1,2,3], k = 1
Output: [1.00000,2.00000,3.00000]
"""

# Test function to verify all implementations
def test_solutions():
    test_cases = [
        {
            "nums": [1,3,-1,-3,5,3,6,7],
            "k": 3,
            "expected": [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
        },
        {
            "nums": [1,2,3,4,2,3,1,4,2],
            "k": 3,
            "expected": [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
        }
    ]
    
    for i, test in enumerate(test_cases):
        brute = median_sliding_window_brute(test["nums"], test["k"])
        insertion = median_sliding_window_insertion(test["nums"], test["k"])
        optimal = median_sliding_window_optimal(test["nums"], test["k"])
        
        # Check if results match within epsilon
        epsilon = 1e-5
        assert all(abs(b - e) < epsilon for b, e in zip(brute, test["expected"]))
        assert all(abs(i - e) < epsilon for i, e in zip(insertion, test["expected"]))
        assert all(abs(o - e) < epsilon for o, e in zip(optimal, test["expected"]))
        
    print("All test cases passed!")