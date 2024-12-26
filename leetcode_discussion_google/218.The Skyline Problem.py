# https://leetcode.com/problems/the-skyline-problem/description/
# 218. The Skyline Problem
# Solved
# Hard
# Topics
# Companies
# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

# The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

# lefti is the x coordinate of the left edge of the ith building.
# righti is the x coordinate of the right edge of the ith building.
# heighti is the height of the ith building.
# You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

# The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

# Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

 

# Example 1:


# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
# Example 2:

# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]
 

# Constraints:

# 1 <= buildings.length <= 104
# 0 <= lefti < righti <= 231 - 1
# 1 <= heighti <= 231 - 1
# buildings is sorted by lefti in non-decreasing order.
# Skyline Problem Analysis
#
# Input: Array of buildings [left, right, height]
# Output: Key points forming skyline [[x1,y1], [x2,y2],...]
#
# Example Visualization:
# Input: [[2,9,10],[3,7,15],[5,12,12]]
#
#     15        
#     **        
#     **        
# 10  **10 12    
# **  ****__**    
# **  ****__**    
# **  ****__**    
# 0 2 3 7 9 12
#
# Output: [[2,10],[3,15],[7,12],[12,0]]

from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Priority Queue Solution
        Time: O(n log n)
        Space: O(n)
        """
        # Convert buildings to events: [x, -h] for start, [x, h] for end
        events = []
        for left, right, height in buildings:
            events.append([left, -height])  # Negative for start
            events.append([right, height])  # Positive for end
        
        # Sort events by x and process higher buildings first
        events.sort(key=lambda x: (x[0], x[1]))
        
        result = []  # Skyline points
        heap = [0]   # Height heap with ground level
        prev_height = 0
        
        for x, h in events:
            if h < 0:  # Building starts
                heapq.heappush(heap, h)
            else:      # Building ends
                heap.remove(-h)
                heapq.heapify(heap)
            
            # Current highest building
            curr_height = -heap[0]
            
            # If height changes, add point to skyline
            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height
        
        return result

def test():
    solution = Solution()
    
    # Test case 1
    buildings1 = [[2,9,10],[3,7,15],[5,12,12]]
    assert solution.getSkyline(buildings1) == [[2,10],[3,15],[7,12],[12,0]]
    
    # Test case 2
    buildings2 = [[0,2,3],[2,5,3]]
    assert solution.getSkyline(buildings2) == [[0,3],[5,0]]
    
    print("All tests passed!")

"""
Solution Process:
---------------
1. Convert buildings to events:
   For building [2,9,10]:
   - Start event: [2,-10]
   - End event: [9,10]

2. Sort events by x-coordinate:
   - For same x, process starts before ends
   - Higher buildings before lower

3. Process events with max heap:
   - Start: push -height (for max heap)
   - End: remove height
   - If max height changes, add point

Example Step-by-Step:
-------------------
Input: [[2,9,10],[3,7,15],[5,12,12]]

Events: [2,-10], [3,-15], [5,-12], [7,15], [9,10], [12,12]

1. x=2: push -10
   heap=[-10]
   height=10 ≠ 0 → add [2,10]

2. x=3: push -15
   heap=[-15,-10]
   height=15 ≠ 10 → add [3,15]

3. x=5: push -12
   heap=[-15,-12,-10]
   height=15 (no change)

4. x=7: remove -15
   heap=[-12,-10]
   height=12 ≠ 15 → add [7,12]

5. x=9: remove -10
   heap=[-12]
   height=12 (no change)

6. x=12: remove -12
   heap=[0]
   height=0 ≠ 12 → add [12,0]

Key Points:
----------
1. Use events to handle overlapping buildings
2. Max heap tracks active building heights
3. Only add points when height changes
4. Process same x-coordinate events in correct order

Edge Cases:
----------
1. Single building
2. Multiple buildings same height
3. Buildings sharing edges
4. No gaps between buildings
5. All buildings same height
"""