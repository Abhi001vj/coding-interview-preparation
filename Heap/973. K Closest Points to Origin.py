# https://leetcode.com/problems/k-closest-points-to-origin/description/
# 973. K Closest Points to Origin
# Medium
# Topics
# Companies
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

# Constraints:

# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104

1. Sorting
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]
Time & Space Complexity
Time complexity: 
O
(
n
log
⁡
n
)
O(nlogn)
Space complexity: 
O
(
1
)
O(1) or 
O
(
n
)
O(n) depending on the sorting algorithm.
2. Min Heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
            
        return res
Time & Space Complexity
Time complexity: 
O
(
k
∗
log
⁡
n
)
O(k∗logn)
Space complexity: 
O
(
n
)
O(n)
Where 
n
n is the length of the array 
p
o
i
n
t
s
points.
3. Max Heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res
Time & Space Complexity
Time complexity: 
O
(
n
∗
log
⁡
k
)
O(n∗logk)
Space complexity: 
O
(
k
)
O(k)
Where 
n
n is the length of the array 
p
o
i
n
t
s
points.
4. Quick Select
class Solution:
    def kClosest(self, points, k):
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]
Time & Space Complexity
Time complexity: 
O
(
n
)
O(n) in average case, 
O
(
n
2
)
O(n 
2
 ) in worst case.
Space complexity: 
O
(
1
)
O(1)

"""
K CLOSEST POINTS TO ORIGIN - DETAILED SOLUTIONS
============================================

Three main approaches:
1. Sorting Solution (Simple)
2. Max Heap Solution (Memory Efficient)
3. Quick Select Solution (Most Efficient)

1. SORTING SOLUTION
=================
"""
class SortingSolution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Approach: Sort all points by distance
        Time: O(nlogn) for sorting
        Space: O(1) - sorts in place
        
        Example: points = [[1,3],[-2,2]], k = 1
        
        1. Calculate distances:
           [1,3] → √(1² + 3²) = √10
           [-2,2] → √((-2)² + 2²) = √8
        
        2. Sort by distance:
           [-2,2], [1,3]  # √8 < √10
           
        3. Return first k points
        """
        # Sort points by distance (x² + y²)
        # No need to calculate actual sqrt as relative ordering remains same
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        return points[:k]

"""
2. MAX HEAP SOLUTION
==================
"""
import heapq

class HeapSolution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Approach: Maintain k closest points in max heap
        Time: O(nlogk)
        Space: O(k)
        
        Example: points = [[3,3],[5,-1],[-2,4]], k = 2
        
        Distances:
        [3,3] → 18
        [5,-1] → 26
        [-2,4] → 20
        
        Heap evolution:
        1. [3,3] added: [(18, [3,3])]
        2. [5,-1] added: [(26, [5,-1]), (18, [3,3])]
        3. [-2,4] processed: [(20, [-2,4]), (18, [3,3])]
        """
        # Max heap of (-distance, point)
        heap = []
        
        for x, y in points:
            # Calculate distance (squared)
            dist = -(x*x + y*y)  # Negative for max heap
            
            if len(heap) < k:
                # If heap not full, add point
                heapq.heappush(heap, (dist, [x,y]))
            elif dist > heap[0][0]:
                # If closer than furthest point in heap
                heapq.heapreplace(heap, (dist, [x,y]))
        
        # Extract points from heap
        return [point for (dist, point) in heap]

"""
3. QUICK SELECT SOLUTION (Most Efficient)
=====================================
"""
class QuickSelectSolution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Approach: Use quick select to find kth closest point
        Time: O(n) average, O(n²) worst case
        Space: O(1)
        
        Example: points = [[3,3],[5,-1],[-2,4]], k = 2
        
        1. Calculate distances:
           [3,3] → 18
           [5,-1] → 26
           [-2,4] → 20
           
        2. Quick select process:
           Partition around pivot until k closest found
        """
        def distance(point):
            return point[0]**2 + point[1]**2
        
        def partition(left, right):
            """
            Partitions array around pivot
            Returns final position of pivot
            """
            pivot = distance(points[right])
            store_idx = left
            
            for i in range(left, right):
                if distance(points[i]) <= pivot:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1
            
            points[store_idx], points[right] = points[right], points[store_idx]
            return store_idx
        
        def select(left, right):
            """
            Quick select to find kth element
            """
            if left < right:
                pivot_idx = partition(left, right)
                
                if pivot_idx == k:
                    return
                elif pivot_idx < k:
                    select(pivot_idx + 1, right)
                else:
                    select(left, pivot_idx - 1)
        
        select(0, len(points) - 1)
        return points[:k]

"""
VISUAL REPRESENTATION OF DISTANCES
==============================

For points: [[1,3],[-2,2]]

Coordinate System:
   4 |
   3 |    •(1,3)
   2 |  •(-2,2)
   1 |
   0 +------------
  -1 |
  -2 |
     -2 -1 0 1 2

Distance Calculation:
• (1,3): √(1² + 3²) = √10 ≈ 3.16
• (-2,2): √((-2)² + 2²) = √8 ≈ 2.83

COMPARISON OF APPROACHES
=====================

1. Sorting:
   Pros:
   - Simple to implement
   - Stable sorting
   Cons:
   - O(nlogn) time always
   - Processes all points

2. Max Heap:
   Pros:
   - O(nlogk) time
   - O(k) space
   Cons:
   - Heap operations overhead
   - More complex implementation

3. Quick Select:
   Pros:
   - O(n) average time
   - In-place operation
   Cons:
   - Complex implementation
   - O(n²) worst case
   - Unstable ordering

Memory Usage Patterns:
Sorting: O(1) extra space
Heap: O(k) heap space
Quick Select: O(1) extra space

When to use each:
- Sorting: Small arrays or when full sorting needed
- Heap: Large arrays with small k
- Quick Select: Large arrays when order doesn't matter
"""

def test_solutions():
    points1 = [[1,3],[-2,2]]
    k1 = 1
    points2 = [[3,3],[5,-1],[-2,4]]
    k2 = 2
    
    solutions = [
        ("Sorting", SortingSolution()),
        ("Heap", HeapSolution()),
        ("QuickSelect", QuickSelectSolution())
    ]
    
    for name, sol in solutions:
        print(f"\n{name} Solution:")
        print(f"Test 1: {sol.kClosest(points1.copy(), k1)}")
        print(f"Test 2: {sol.kClosest(points2.copy(), k2)}")

if __name__ == "__main__":
    test_solutions()