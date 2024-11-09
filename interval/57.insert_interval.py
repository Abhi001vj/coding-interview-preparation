# https://leetcode.com/problems/insert-interval/description/
# 57. Insert Interval
# Medium
# Topics
# Companies
# Hint
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105


def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    Example walkthrough with intervals = [[1,3],[6,9]], newInterval = [2,5]
    
    Visual process:
    1. Initial state:
       [1,3] [6,9]  <- original intervals
         [2,5]      <- new interval
    
    2. Before overlap:
       [1,3]        <- start <= newInterval.start
    
    3. Overlap check:
       [1,3] overlaps [2,5] -> merge to [1,5]
    
    4. After potential overlap:
       [6,9]        <- start > newInterval.end
    
    Final result: [[1,5], [6,9]]
    """
    
    result = []
    i = 0
    n = len(intervals)
    
    # Step 1: Add all intervals that come before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Step 2: Merge overlapping intervals
    merged = newInterval
    while i < n and intervals[i][0] <= merged[1]:
        merged = [
            min(merged[0], intervals[i][0]),
            max(merged[1], intervals[i][1])
        ]
        i += 1
    result.append(merged)
    
    # Step 3: Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

"""
Let me explain the key test cases:

1. No overlap case:
   intervals = [[1,2], [5,6]], newInterval = [3,4]
   Result: [[1,2], [3,4], [5,6]]

2. Single overlap:
   intervals = [[1,3], [6,9]], newInterval = [2,5]
   Result: [[1,5], [6,9]]

3. Multiple overlaps:
   intervals = [[1,2], [3,5], [6,7], [8,10]], newInterval = [4,8]
   Result: [[1,2], [3,10]]

4. Edge cases:
   - Empty intervals: []
   - newInterval before all: [0,1] into [[2,3]]
   - newInterval after all: [4,5] into [[1,2]]
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        
        for i in range(n):
            start, end = intervals[i]
            if newInterval[1] < start:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > end:
                result.append( intervals[i])
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        result.append(newInterval)     
        return result

"""
CURRENT SOLUTION EXPLANATION
---------------------------
Let's analyze the current solution with example: 
intervals = [[1,3],[6,9]], newInterval = [2,5]

Visual process:
1) First iteration: interval [1,3]
   newInterval = [2,5]
   2 is not > 3 and 5 is not < 1
   -> Merge: newInterval becomes [1,5]
   result = []

2) Second iteration: interval [6,9]
   newInterval = [1,5]
   5 < 6 -> Add [1,5] and return result + rest
   Final result: [[1,5],[6,9]]

Key Cases:
1. newInterval end < current start:
   [1,2] trying to insert [3,4]
   -> Add newInterval and return rest

2. newInterval start > current end:
   [1,2] trying to insert [0,0]
   -> Add current interval

3. Overlap case:
   [1,3] with [2,4]
   -> Merge by taking min of starts, max of ends

Current Solution Code:
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[List[int]]) -> List[List[int]]:
        # Handle empty input
        if not intervals:
            return [newInterval]
            
        result = []
        n = len(intervals)
        
        for i in range(n):
            start, end = intervals[i]
            # Case 1: newInterval ends before current interval
            if newInterval[1] < start:
                result.append(newInterval)
                return result + intervals[i:]  # Early return optimization
            # Case 2: newInterval starts after current interval
            elif newInterval[0] > end:
                result.append(intervals[i])
            # Case 3: Overlap case - merge intervals
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        
        result.append(newInterval)
        return result

"""
OPTIMIZED SOLUTION
----------------
Key Optimizations:
1. Handle edge cases first
2. Use binary search to find insertion point
3. Minimize list operations
"""

class OptimizedSolution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Edge cases
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
            
        # Binary search to find first potential overlap
        left, right = 0, len(intervals)
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][1] < newInterval[0]:
                left = mid + 1
            else:
                right = mid
                
        # Process intervals from found position
        result = intervals[:left]
        
        # Merge overlapping intervals
        merged = newInterval
        i = left
        while i < len(intervals) and intervals[i][0] <= merged[1]:
            merged = [
                min(merged[0], intervals[i][0]),
                max(merged[1], intervals[i][1])
            ]
            i += 1
            
        result.append(merged)
        result.extend(intervals[i:])
        return result

"""
Time Complexity Comparison:
1. Original Solution: O(n)
   - Single pass through intervals
   - List concatenation in worst case

2. Optimized Solution: O(log n) + O(k)
   - Binary search: O(log n)
   - k is number of overlapping intervals
   - Best case: O(log n) if no overlaps
   - Worst case: Still O(n) if many overlaps

Space Complexity:
Both solutions: O(n) for result list

Key Improvements:
1. Edge case handling reduces unnecessary iterations
2. Binary search reduces search time for insertion point
3. Minimize list operations with extend instead of concatenation
4. Early returns for non-overlap cases

Test Cases to Verify:
1. No overlap: intervals = [[1,2],[4,5]], newInterval = [6,7]
2. Complete overlap: intervals = [[1,5]], newInterval = [2,3]
3. Multiple overlaps: intervals = [[1,3],[4,6],[8,10]], newInterval = [2,9]
4. Edge insertion: intervals = [[2,3],[4,5]], newInterval = [1,1]
"""