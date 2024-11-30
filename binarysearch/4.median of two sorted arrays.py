# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# 4. Median of Two Sorted Arrays
# Hard
# Topics
# Companies
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

```python
"""
MEDIAN OF TWO SORTED ARRAYS: Complete Analysis
===========================================

Pattern Recognition:
1. Merge Sort Merge step
2. Binary Search
3. Partition
4. Two Pointers
5. Divide & Conquer

Key Insights:
1. Arrays are already sorted
2. Median splits array into equal halves
3. Need O(log(m+n)) complexity
4. Can skip merging entire arrays
"""

def brute_force_solution(nums1: List[int], nums2: List[int]) -> float:
    """
    Approach 1: Merge and Find Median
    Pattern: Merge Sort's Merge Step
    
    Visual Example: nums1 = [1,3], nums2 = [2]
    
    Merge Process:
    Step 1: [1] | [3]  and  [2]
            ↓
    Step 2: [1,2] | [3]
            ↓
    Step 3: [1,2,3]
    
    Median: Index (3-1)/2 = 1 → value = 2
    
    Time: O(m + n)
    Space: O(m + n)
    """
    merged = []
    i = j = 0
    
    # Merge arrays
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
            
    # Add remaining elements
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    
    # Find median
    total = len(merged)
    if total % 2:
        return float(merged[total//2])
    return (merged[total//2 - 1] + merged[total//2]) / 2

def two_pointer_solution(nums1: List[int], nums2: List[int]) -> float:
    """
    Approach 2: Two Pointers without Merging
    Pattern: Two Pointers + Counter
    
    Example: nums1 = [1,2], nums2 = [3,4]
    
    Visualization:
    Step 1: [1,2] [3,4]  count=0 target=(4/2)=2
           ↓   ↓
    Step 2: [1,2] [3,4]  count=1 prev=1
              ↓   ↓
    Step 3: [1,2] [3,4]  count=2 prev=2, curr=2
              ↓   ↓
    
    Time: O(m + n)
    Space: O(1)
    """
    m, n = len(nums1), len(nums2)
    total = m + n
    target = total // 2
    i = j = count = 0
    prev = curr = 0
    
    # Move pointers until median position
    while count <= target:
        prev = curr
        
        if i == m:
            curr = nums2[j]
            j += 1
        elif j == n:
            curr = nums1[i]
            i += 1
        elif nums1[i] <= nums2[j]:
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1
            
        count += 1
        
    if total % 2:
        return float(curr)
    return (prev + curr) / 2

def binary_search_optimal(nums1: List[int], nums2: List[int]) -> float:
    """
    Approach 3: Binary Search (Optimal)
    Pattern: Binary Search on Partition
    
    Example: nums1 = [1,3], nums2 = [2]
    
    Partition Visualization:
    Step 1: nums1 = [1|3], nums2 = [2|]
           left1=1, right1=3, left2=2, right2=∞
           
    Valid partition because:
    1. left1 <= right2 (1 <= ∞)
    2. left2 <= right1 (2 <= 3)
    3. Count of elements on left = (m+n+1)/2
    
    Time: O(log(min(m,n)))
    Space: O(1)
    """
    # Ensure nums1 is smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        # Partition positions
        partitionX = (left + right) // 2
        partitionY = (m + n + 1) // 2 - partitionX
        
        # Find elements around partition
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        # Check if partition is correct
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # Found correct partition
            if (m + n) % 2:
                return float(max(maxLeftX, maxLeftY))
            return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            
        elif maxLeftX > minRightY:
            # Move partition left
            right = partitionX - 1
        else:
            # Move partition right
            left = partitionX + 1
    
    raise ValueError("Input arrays are not sorted")

"""
COMPLEXITY ANALYSIS
-----------------
1. Brute Force:
   Time: O(m + n) - One pass merge
   Space: O(m + n) - Store merged array

2. Two Pointers:
   Time: O(m + n) - One pass through arrays
   Space: O(1) - Constant extra space

3. Binary Search:
   Time: O(log(min(m,n))) - Binary search on smaller array
   Space: O(1) - Constant extra space

EDGE CASES
---------
1. Empty arrays
2. Single element arrays
3. Arrays of different lengths
4. Negative numbers
5. Duplicate elements
6. All elements same in one array

VISUALIZATION OF BINARY SEARCH APPROACH
-----------------------------------
Example: nums1 = [1,3,8,9], nums2 = [7,11,18,19]

Step 1: Initial partition
nums1: [1,3|8,9]
nums2: [7,11|18,19]
maxLeft = max(3,11) = 11
minRight = min(8,18) = 8
Invalid: 11 > 8

Step 2: Move partition right
nums1: [1,3,8|9]
nums2: [7|11,18,19]
maxLeft = max(8,7) = 8
minRight = min(9,11) = 9
Valid partition found!

Median = (8 + 9)/2 = 8.5

KEY IMPLEMENTATION DETAILS
-----------------------
1. Binary Search:
   - Search on smaller array
   - Handle partition bounds
   - Infinity for empty partitions

2. Two Pointers:
   - Track previous and current
   - Handle array exhaustion
   - Count up to median position

3. Edge Case Handling:
   - Array length checks
   - Odd/even total length
   - Boundary elements
"""