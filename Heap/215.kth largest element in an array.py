# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# 215. Kth Largest Element in an Array
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

"""
KTH LARGEST ELEMENT - DETAILED SOLUTIONS
=====================================

Three main approaches:
1. Sorting Solution (Simple)
2. Min Heap Solution (Memory Efficient)
3. Quick Select Solution (Most Efficient)

Example Input: nums = [3,2,1,5,6,4], k = 2
Expected Output: 5

1. SORTING APPROACH
=================
"""
class SortingSolution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Approach: Sort and index from end
        Time: O(nlogn) for sorting
        Space: O(1) - sorts in place
        
        Visual process for [3,2,1,5,6,4], k=2:
        1. Original: [3,2,1,5,6,4]
        2. Sorted:   [1,2,3,4,5,6]
        3. Answer:   nums[n-k] = nums[6-2] = nums[4] = 5
        """
        nums.sort()  # Sort in ascending order
        return nums[len(nums) - k]  # Return kth element from end

"""
2. MIN HEAP APPROACH
=================
"""
import heapq

class HeapSolution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Approach: Maintain k smallest elements in min heap
        Time: O(nlogk)
        Space: O(k)
        
        Visual process for [3,2,1,5,6,4], k=2:
        
        Heap Evolution:
        1. [3]           # First element
        2. [2,3]         # k=2 elements stored
        3. [2,3]         # 1 is smaller, ignore
        4. [3,5]         # 5 enters, 2 leaves
        5. [5,6]         # 6 enters, 3 leaves
        6. [5,6]         # 4 is smaller, ignore
        
        Return: heap[0] = 5
        """
        # Create min heap of k largest elements
        heap = []
        
        for num in nums:
            if len(heap) < k:
                # If heap not full, add element
                heapq.heappush(heap, num)
            elif num > heap[0]:
                # If current number larger than smallest in heap
                heapq.heapreplace(heap, num)
                
        # Top of heap is kth largest
        return heap[0]

"""
3. QUICK SELECT SOLUTION
=====================
"""
class QuickSelectSolution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Approach: Use quick select algorithm
        Time: O(n) average, O(n²) worst case
        Space: O(1)
        
        Visual process for [3,2,1,5,6,4], k=2:
        
        Target: len(nums) - k = 4 (5th position)
        
        Quick Select Steps:
        1. Choose pivot (say 4)
           [3,2,1,5,6,4]
           
        2. Partition around 4:
           [3,2,1,4,6,5]
           Position of 4 is too low
           
        3. Recurse on right portion:
           [6,5]
           Found position!
        """
        k = len(nums) - k  # Convert to kth smallest problem
        
        def quickSelect(left: int, right: int) -> int:
            """
            Quick select helper function
            Partitions array and recursively searches correct half
            """
            if left == right:
                return nums[left]
                
            pivot_idx = partition(left, right)
            
            if k == pivot_idx:
                return nums[k]
            elif k < pivot_idx:
                return quickSelect(left, pivot_idx - 1)
            else:
                return quickSelect(pivot_idx + 1, right)
        
        def partition(left: int, right: int) -> int:
            """
            Partitions array around pivot
            Returns final position of pivot
            
            Example partition for [3,2,1,5,6,4]:
            1. Choose pivot 4 (last element)
            2. Partition process:
               [3,2,1,5,6,4] initial
               [3,2,1,5,6,4] i=0: 3<4, swap with itself
               [3,2,1,5,6,4] i=1: 2<4, swap with itself
               [3,2,1,5,6,4] i=2: 1<4, swap with itself
               [3,2,1,4,6,5] final: swap pivot to correct position
            """
            # Choose rightmost element as pivot
            pivot = nums[right]
            # Partition index
            store_idx = left
            
            # Move elements smaller than pivot to left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1
                    
            # Place pivot in final position
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            return store_idx
            
        return quickSelect(0, len(nums) - 1)

"""
DETAILED STATE TRACKING
====================

Example for [3,2,1,5,6,4], k=2:

Heap Approach States:
Initial heap: []
After 3: [3]
After 2: [2,3]
After 1: [2,3]    # 1 ignored
After 5: [3,5]    # 2 removed
After 6: [5,6]    # 3 removed
After 4: [5,6]    # 4 ignored
Result: 5

Quick Select States:
k = 6-2 = 4 (convert to 0-based index)
Initial: [3,2,1,5,6,4]
Partition around 4:
    [3,2,1,4,6,5]
    4 at position 3 (need position 4)
Recurse right: [6,5]
    Partition around 5:
    [5,6]
    5 at position 4 (found!)
Result: 5

COMPARISON OF APPROACHES:
=====================

1. Sorting:
   Pros: Simple, stable
   Cons: O(nlogn) always
   Best when: Small arrays or need sorted result

2. Heap:
   Pros: O(nlogk) time, O(k) space
   Cons: Heap maintenance overhead
   Best when: Large arrays, small k

3. Quick Select:
   Pros: O(n) average time, O(1) space
   Cons: O(n²) worst case, complex implementation
   Best when: Large arrays, any k

Memory Usage:
------------
Sorting: O(1) extra
Heap: O(k)
Quick Select: O(1) recursion stack
"""

"""
KTH LARGEST ELEMENT - DETAILED SOLUTIONS
=====================================

Three main approaches:
1. Sorting Solution (Simple)
2. Min Heap Solution (Memory Efficient)
3. Quick Select Solution (Most Efficient)

Example Input: nums = [3,2,1,5,6,4], k = 2
Expected Output: 5

1. SORTING APPROACH
=================
"""
class SortingSolution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Approach: Sort and index from end
        Time: O(nlogn) for sorting
        Space: O(1) - sorts in place
        
        Visual process for [3,2,1,5,6,4], k=2:
        1. Original: [3,2,1,5,6,4]
        2. Sorted:   [1,2,3,4,5,6]
        3. Answer:   nums[n-k] = nums[6-2] = nums[4] = 5
        """
        nums.sort()  # Sort in ascending order
        return nums[len(nums) - k]  # Return kth element from end

"""
2. MIN HEAP APPROACH
=================
"""
import heapq

class HeapSolution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Approach: Maintain k smallest elements in min heap
        Time: O(nlogk)
        Space: O(k)
        
        Visual process for [3,2,1,5,6,4], k=2:
        
        Heap Evolution:
        1. [3]           # First element
        2. [2,3]         # k=2 elements stored
        3. [2,3]         # 1 is smaller, ignore
        4. [3,5]         # 5 enters, 2 leaves
        5. [5,6]         # 6 enters, 3 leaves
        6. [5,6]         # 4 is smaller, ignore
        
        Return: heap[0] = 5
        """
        # Create min heap of k largest elements
        heap = []
        
        for num in nums:
            if len(heap) < k:
                # If heap not full, add element
                heapq.heappush(heap, num)
            elif num > heap[0]:
                # If current number larger than smallest in heap
                heapq.heapreplace(heap, num)
                
        # Top of heap is kth largest
        return heap[0]

"""
3. QUICK SELECT SOLUTION
=====================
"""
class QuickSelectSolution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Approach: Use quick select algorithm
        Time: O(n) average, O(n²) worst case
        Space: O(1)
        
        Visual process for [3,2,1,5,6,4], k=2:
        
        Target: len(nums) - k = 4 (5th position)
        
        Quick Select Steps:
        1. Choose pivot (say 4)
           [3,2,1,5,6,4]
           
        2. Partition around 4:
           [3,2,1,4,6,5]
           Position of 4 is too low
           
        3. Recurse on right portion:
           [6,5]
           Found position!
        """
        k = len(nums) - k  # Convert to kth smallest problem
        
        def quickSelect(left: int, right: int) -> int:
            """
            Quick select helper function
            Partitions array and recursively searches correct half
            """
            if left == right:
                return nums[left]
                
            pivot_idx = partition(left, right)
            
            if k == pivot_idx:
                return nums[k]
            elif k < pivot_idx:
                return quickSelect(left, pivot_idx - 1)
            else:
                return quickSelect(pivot_idx + 1, right)
        
        def partition(left: int, right: int) -> int:
            """
            Partitions array around pivot
            Returns final position of pivot
            
            Example partition for [3,2,1,5,6,4]:
            1. Choose pivot 4 (last element)
            2. Partition process:
               [3,2,1,5,6,4] initial
               [3,2,1,5,6,4] i=0: 3<4, swap with itself
               [3,2,1,5,6,4] i=1: 2<4, swap with itself
               [3,2,1,5,6,4] i=2: 1<4, swap with itself
               [3,2,1,4,6,5] final: swap pivot to correct position
            """
            # Choose rightmost element as pivot
            pivot = nums[right]
            # Partition index
            store_idx = left
            
            # Move elements smaller than pivot to left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1
                    
            # Place pivot in final position
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            return store_idx
            
        return quickSelect(0, len(nums) - 1)

"""
DETAILED STATE TRACKING
====================

Example for [3,2,1,5,6,4], k=2:

Heap Approach States:
Initial heap: []
After 3: [3]
After 2: [2,3]
After 1: [2,3]    # 1 ignored
After 5: [3,5]    # 2 removed
After 6: [5,6]    # 3 removed
After 4: [5,6]    # 4 ignored
Result: 5

Quick Select States:
k = 6-2 = 4 (convert to 0-based index)
Initial: [3,2,1,5,6,4]
Partition around 4:
    [3,2,1,4,6,5]
    4 at position 3 (need position 4)
Recurse right: [6,5]
    Partition around 5:
    [5,6]
    5 at position 4 (found!)
Result: 5

COMPARISON OF APPROACHES:
=====================

1. Sorting:
   Pros: Simple, stable
   Cons: O(nlogn) always
   Best when: Small arrays or need sorted result

2. Heap:
   Pros: O(nlogk) time, O(k) space
   Cons: Heap maintenance overhead
   Best when: Large arrays, small k

3. Quick Select:
   Pros: O(n) average time, O(1) space
   Cons: O(n²) worst case, complex implementation
   Best when: Large arrays, any k

Memory Usage:
------------
Sorting: O(1) extra
Heap: O(k)
Quick Select: O(1) recursion stack
"""