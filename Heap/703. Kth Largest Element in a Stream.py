# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
# 703. Kth Largest Element in a Stream
# Easy
# Topics
# Companies
# You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

# Example 1:

# Input:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# Output: [null, 4, 5, 5, 8, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4
# kthLargest.add(5); // return 5
# kthLargest.add(10); // return 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8

# Example 2:

# Input:
# ["KthLargest", "add", "add", "add", "add"]
# [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

# Output: [null, 7, 7, 7, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
# kthLargest.add(2); // return 7
# kthLargest.add(10); // return 7
# kthLargest.add(9); // return 7
# kthLargest.add(9); // return 8
 

# Constraints:

# 0 <= nums.length <= 104
# 1 <= k <= nums.length + 1
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# At most 104 calls will be made to add.


"""
KTH LARGEST ELEMENT IN STREAM SOLUTIONS
=====================================

Three main approaches:
1. Sorted Array (Simple but inefficient)
2. Min Heap (Optimal)
3. Binary Search Tree (Alternative)

1. SORTED ARRAY APPROACH
=====================
"""
class KthLargestSortedArray:
    def __init__(self, k: int, nums: list[int]):
        """
        Time: O(nlogn) for sorting
        Space: O(n) for array
        
        Example: k=3, nums=[4,5,8,2]
        self.k = 3
        self.nums = [2,4,5,8] (sorted)
        """
        self.k = k
        self.nums = sorted(nums)
    
    def add(self, val: int) -> int:
        """
        Time: O(n) for insertion
        Space: O(1)
        
        Example:
        Initial: nums=[2,4,5,8], add(3)
        1. Binary search finds insert position
        2. Insert 3: [2,3,4,5,8]
        3. Return nums[-3] = 4 (3rd largest)
        """
        # Binary search for insertion position
        left, right = 0, len(self.nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.nums[mid] < val:
                left = mid + 1
            else:
                right = mid
        
        # Insert at correct position
        self.nums.insert(left, val)
        
        # Return kth largest
        return self.nums[-self.k]

"""
2. MIN HEAP APPROACH (OPTIMAL)
===========================
Uses min heap of size k to maintain k largest elements
Heap top is always kth largest
"""
import heapq

class KthLargestHeap:
    def __init__(self, k: int, nums: list[int]):
        """
        Time: O(nlogk) for heapification
        Space: O(k) for heap
        
        Example: k=3, nums=[4,5,8,2]
        1. self.k = 3
        2. Create min heap: [4,5,8]
        3. For each num:
           - If heap size < k: add num
           - If num > heap top: pop top, add num
        """
        self.k = k
        self.heap = []
        
        # Add initial numbers
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        """
        Time: O(logk) for heap operations
        Space: O(1)
        
        Example:
        heap=[4,5,8], add(3)
        1. heap size = 3 = k
        2. 3 < heap top (4), so ignore
        3. Return 4 (heap top)
        
        heap=[4,5,8], add(10)
        1. heap size = 3 = k
        2. 10 > heap top (4)
        3. Pop 4, add 10
        4. New heap: [5,8,10]
        5. Return 5 (heap top)
        """
        # If heap is too small, add value
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # If new value is larger than kth largest
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        # Return kth largest (heap top)
        return self.heap[0] if len(self.heap) == self.k else None

"""
3. BINARY SEARCH TREE APPROACH
===========================
Uses self-balancing BST (like AVL or Red-Black)
Maintains count of nodes and finds kth largest
"""
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1  # Count of nodes in subtree

class KthLargestBST:
    def __init__(self, k: int, nums: list[int]):
        """
        Time: O(nlogn) for tree construction
        Space: O(n) for tree
        
        Example: k=3, nums=[4,5,8,2]
        Creates balanced BST with count at each node
        """
        self.k = k
        self.root = None
        for num in nums:
            self.root = self._insert(self.root, num)
    
    def _insert(self, node: TreeNode, val: int) -> TreeNode:
        """
        BST insertion with count maintenance
        Time: O(logn)
        """
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        
        node.count += 1
        return node
    
    def add(self, val: int) -> int:
        """
        Time: O(logn)
        Space: O(1)
        """
        self.root = self._insert(self.root, val)
        return self._find_kth_largest(self.root, self.k)
    
    def _find_kth_largest(self, node: TreeNode, k: int) -> int:
        """
        Finds kth largest in BST using counts
        Time: O(logn)
        """
        if not node:
            return None
            
        right_count = node.right.count if node.right else 0
        
        if k == right_count + 1:
            return node.val
        elif k <= right_count:
            return self._find_kth_largest(node.right, k)
        else:
            return self._find_kth_largest(node.left, k - right_count - 1)

"""
COMPARISON OF APPROACHES
=====================

1. Sorted Array:
Pros:
- Simple to implement
- Good for small datasets
- Easy to understand

Cons:
- O(n) insertion time
- Not scalable for large streams
- Extra space for full array

2. Min Heap (Best):
Pros:
- O(logk) operations
- Only stores k elements
- Perfect for streaming data

Cons:
- Heap operations more complex
- Not as intuitive as array

3. BST:
Pros:
- O(logn) operations
- Maintains sorted order
- Good for other operations

Cons:
- Complex implementation
- More space than heap
- Balancing overhead

VISUALIZATIONS OF OPERATIONS:
==========================

For k=3, nums=[4,5,8,2]:

Initial Array: [2,4,5,8]
Add 3:
2 [3] 4 5 8  → Insert at position 1
Return: 4 (3rd largest)

Initial Heap: [4,5,8]  (min heap of size k)
Add 3:
     4
   /   \
  5     8
3 < 4, ignore
Return: 4 (top)

Initial BST:
     5
   /   \
  4     8
 /
2

Add 3:
     5
   /   \
  4     8
 /
2
 \
  3
"""