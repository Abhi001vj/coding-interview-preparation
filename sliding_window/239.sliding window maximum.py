# https://leetcode.com/problems/sliding-window-maximum/description/
# 239. Sliding Window Maximum
# Hard
# Topics
# Companies
# Hint
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

```python
"""
SLIDING WINDOW MAXIMUM: Complete Analysis
=====================================

Pattern Recognition:
1. Sliding Window
2. Monotonic Queue
3. Heap/Priority Queue
4. Two Pointers
"""

def brute_force_solution(nums: List[int], k: int) -> List[int]:
    """
    Approach 1: Brute Force
    Pattern: Check each window's max
    
    Example: nums = [1,3,-1,-3,5,3,6,7], k = 3
    
    Window Evolution:
    [1, 3,-1] -> max = 3
     [3,-1,-3] -> max = 3
      [-1,-3,5] -> max = 5
         [-3,5,3] -> max = 5
            [5,3,6] -> max = 6
               [3,6,7] -> max = 7
               
    Time: O(n*k) - check k elements for each window
    Space: O(1) - output array not counted
    """
    result = []
    for i in range(len(nums) - k + 1):
        max_val = max(nums[i:i+k])
        result.append(max_val)
    return result

def heap_solution(nums: List[int], k: int) -> List[int]:
    """
    Approach 2: Heap/Priority Queue
    Pattern: Max Heap with indexes
    
    Example: nums = [1,3,-1,-3,5,3,6,7], k = 3
    
    Heap state: (value, index)
    Window [1,3,-1]:   heap = [(3,1), (1,0), (-1,2)]
    Window [3,-1,-3]:  heap = [(3,1), (-1,2), (-3,3)]
    Window [-1,-3,5]:  heap = [(5,4), (-1,2), (-3,3)]
    ...
    
    Time: O(n log k) - heap operations
    Space: O(k) - heap size
    """
    from heapq import heappush, heappop
    
    result = []
    heap = []  # (negative value for max heap, index)
    
    # Initialize first window
    for i in range(k):
        heappush(heap, (-nums[i], i))
    result.append(-heap[0][0])
    
    # Process rest of the windows
    for i in range(k, len(nums)):
        # Add current element
        heappush(heap, (-nums[i], i))
        
        # Remove elements outside window
        while heap and heap[0][1] <= i - k:
            heappop(heap)
            
        result.append(-heap[0][0])
        
    return result

def deque_solution(nums: List[int], k: int) -> List[int]:
    """
    Approach 3: Monotonic Deque (Optimal)
    Pattern: Decreasing Monotonic Queue
    
    Example: nums = [1,3,-1,-3,5,3,6,7], k = 3
    
    Deque Evolution (stores indices):
    Initial window [1,3,-1]:
    1: deque = [0]
    3: deque = [1]     # 3 > 1, remove 1
    -1: deque = [1,2]  # -1 < 3, keep both
    Result: 3 (nums[deque[0]])
    
    Next window [3,-1,-3]:
    Remove 1 (outside window)
    Add -3: deque = [1,2,3]
    Result: 3
    
    Next window [-1,-3,5]:
    Add 5: deque = [4]  # 5 is largest
    Result: 5
    
    Time: O(n) - each element pushed/popped once
    Space: O(k) - deque size
    """
    from collections import deque
    
    result = []
    dq = deque()  # store indices
    
    for i in range(len(nums)):
        # Remove indices outside current window
        if dq and dq[0] <= i - k:
            dq.popleft()
            
        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
            
        # Add current element
        dq.append(i)
        
        # Add to result if window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
            
    return result

def optimized_solution(nums: List[int], k: int) -> List[int]:
    """
    Approach 4: Optimized Deque with Block Processing
    Pattern: Block Processing + Monotonic Queue
    
    Split array into blocks of size k:
    [1,3,-1] [-3,5,3] [6,7]
    
    Process each block's local max and combine
    
    Time: O(n)
    Space: O(k)
    """
    from collections import deque
    
    def clean_deque(i: int, dq: deque, nums: List[int]) -> None:
        """Helper to maintain monotonic deque"""
        # Remove old indices
        if dq and dq[0] <= i - k:
            dq.popleft()
            
        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
            
    def process_block(start: int, end: int, nums: List[int]) -> List[int]:
        """Process a block of k elements"""
        block_max = []
        dq = deque()
        
        for i in range(start, end):
            clean_deque(i, dq, nums)
            dq.append(i)
            if i - start >= k - 1:
                block_max.append(nums[dq[0]])
                
        return block_max
    
    if not nums or k == 0:
        return []
    if k == 1:
        return nums
        
    # Process main blocks
    result = []
    n = len(nums)
    for i in range(0, n - k + 1, k):
        end = min(i + k, n)
        result.extend(process_block(i, end, nums))
        
    return result

"""
COMPLEXITY ANALYSIS
-----------------
1. Brute Force:
   Time: O(n*k)
   Space: O(1)

2. Heap Solution:
   Time: O(n log k)
   Space: O(k)

3. Monotonic Deque:
   Time: O(n)
   Space: O(k)

4. Optimized Block:
   Time: O(n)
   Space: O(k)

EDGE CASES
---------
1. Empty array
2. k = 1
3. k = array length
4. All same elements
5. Strictly increasing/decreasing
6. Single element

VISUALIZATION OF MONOTONIC QUEUE
-----------------------------
Example: [1,3,-1,-3,5,3,6,7], k=3

Step-by-step deque state:
1. [1] -> deque=[0]
2. [1,3] -> deque=[1]  # 3 > 1
3. [1,3,-1] -> deque=[1,2]  # -1 < 3
4. [3,-1,-3] -> deque=[1,2,3]
5. [-1,-3,5] -> deque=[4]  # 5 > all
6. [-3,5,3] -> deque=[4]
7. [5,3,6] -> deque=[6]  # 6 > all
8. [3,6,7] -> deque=[7]  # 7 > all

OPTIMIZATION TECHNIQUES
--------------------
1. Early return for k=1
2. Block processing for cache efficiency
3. Minimize deque operations
4. Reuse arrays where possible
"""

```python
"""
SLIDING WINDOW MAXIMUM: Solution by Solution Analysis
================================================

Example Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
"""

def brute_force_solution(nums: List[int], k: int) -> List[int]:
    """
    APPROACH 1: BRUTE FORCE
    ----------------------
    Step by step visualization:
    
    Window 1: [1,3,-1]
    Iteration: max(1) -> max(3) -> max(-1) = 3
    
    Window 2: [3,-1,-3]
    Iteration: max(3) -> max(-1) -> max(-3) = 3
    
    Window 3: [-1,-3,5]
    Iteration: max(-1) -> max(-3) -> max(5) = 5
    
    Complete process:
    [1,3,-1]    →  3   Compare each element
    [3,-1,-3]   →  3   Linear scan in window
    [-1,-3,5]   →  5   Find maximum
    [-3,5,3]    →  5   Move window right
    [5,3,6]     →  6   Repeat process
    [3,6,7]     →  7   Until end
    """
    output = []
    for i in range(len(nums) - k + 1):
        maxi = nums[i]
        for j in range(i, i + k):
            maxi = max(maxi, nums[j])
        output.append(maxi)
    return output

def segment_tree_solution(nums: List[int], k: int) -> List[int]:
    """
    APPROACH 2: SEGMENT TREE
    ----------------------
    Tree visualization for [1,3,-1,-3,5,3,6,7]:
    
                 [max value]
           /                  \
       [max 0:4]           [max 4:8]
      /         \         /         \
   [max 0:2] [max 2:4] [max 4:6] [max 6:8]
    /    \     /    \    /    \    /    \
   [1]   [3] [-1]  [-3] [5]   [3] [6]   [7]
   
    Query Process:
    1. Window [0:3]: Query tree for max(0,2)
    2. Window [1:4]: Query tree for max(1,3)
    3. Window [2:5]: Query tree for max(2,4)
    """
    class SegmentTree:
        def __init__(self, N, a):
            """Initialize tree with power of 2 size"""
            self.n = N
            self.A = a[:]
            # Pad to power of 2
            while (self.n & (self.n - 1)) != 0:
                self.A.append(float('-inf'))
                self.n += 1
            self.tree = [0] * (2 * self.n)
            self.build()

        def build(self):
            """
            Build tree bottom-up:
            1. Copy leaf values
            2. Compute internal nodes
            """
            # Copy array to leaves
            for i in range(self.n):
                self.tree[self.n + i] = self.A[i]
            # Build internal nodes
            for i in range(self.n - 1, 0, -1):
                self.tree[i] = max(
                    self.tree[i << 1],      # Left child
                    self.tree[i << 1 | 1]   # Right child
                )

def heap_solution(nums: List[int], k: int) -> List[int]:
    """
    APPROACH 3: HEAP (PRIORITY QUEUE)
    ------------------------------
    Heap State Evolution:
    
    Initial Window [1,3,-1]:
    heap = [(-3,2), (-1,1), (1,0)]
    
    After sliding:
    Pop outdated elements
    Add new elements
    
    Visualization:
    Window      Heap State (val,idx)     Max
    [1,3,-1]    [(-3,1), (-1,2), (1,0)]  3
    [3,-1,-3]   [(-3,2), (-1,1), (3,0)]  3
    [-1,-3,5]   [(-5,4), (-3,2), (-1,1)] 5
    """
    heap = []
    output = []
    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        if i >= k - 1:
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            output.append(-heap[0][0])
    return output

def dp_solution(nums: List[int], k: int) -> List[int]:
    """
    APPROACH 4: DYNAMIC PROGRAMMING
    ----------------------------
    Using two arrays: leftMax and rightMax
    
    Visualization for [1,3,-1,-3,5,3,6,7], k=3:
    
    Blocks:    [1,3,-1] [-3,5,3] [6,7]
    leftMax:   [1,3,3]  [-3,5,5] [6,7]
    rightMax:  [3,3,-1] [5,5,3]  [7,7]
    
    For each window:
    max = max(rightMax[start], leftMax[end])
    
    Processing:
    Window          RightMax    LeftMax     Result
    [1,3,-1]        3           3           3
    [3,-1,-3]       3           5           3
    [-1,-3,5]       5           5           5
    """
    n = len(nums)
    leftMax = [0] * n
    rightMax = [0] * n
    
    # Build left max array
    leftMax[0] = nums[0]
    for i in range(1, n):
        if i % k == 0:
            leftMax[i] = nums[i]
        else:
            leftMax[i] = max(leftMax[i-1], nums[i])
            
    # Build right max array
    rightMax[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
        if (i + 1) % k == 0:
            rightMax[i] = nums[i]
        else:
            rightMax[i] = max(rightMax[i+1], nums[i])
            
    return [max(rightMax[i], leftMax[i+k-1]) 
            for i in range(n-k+1)]

def deque_solution(nums: List[int], k: int) -> List[int]:
    """
    APPROACH 5: DEQUE (MOST EFFICIENT)
    -------------------------------
    Monotonic Deque Evolution:
    
    Window [1,3,-1]:
    1: deque=[0]
    3: deque=[1]     # 3 > 1, pop 1
    -1: deque=[1,2]  # -1 < 3, keep both
    
    Window [3,-1,-3]:
    pop 1 (outside window)
    -3: deque=[1,2,3]
    
    Complete process:
    Window    Deque(indices)    Maximum
    [1,3,-1]  [1,2]            3
    [3,-1,-3] [1,2,3]          3
    [-1,-3,5] [4]              5
    [-3,5,3]  [4]              5
    [5,3,6]   [6]              6
    [3,6,7]   [7]              7
    """
    output = []
    q = deque()  # store indices
    l = r = 0
    
    while r < len(nums):
        # Remove smaller elements
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        
        # Remove elements outside window
        if l > q[0]:
            q.popleft()
            
        # Add to result if window is complete
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    
    return output
```