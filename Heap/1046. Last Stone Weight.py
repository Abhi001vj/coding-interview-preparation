# https://leetcode.com/problems/last-stone-weight/description/
# Code
# Testcase
# Test Result
# Test Result
# 1046. Last Stone Weight
# Easy
# Topics
# Companies
# Hint
# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

 

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1
 

# Constraints:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000


"""
LAST STONE WEIGHT SOLUTION
========================

Core Concept:
- Use a max heap to always get the two heaviest stones
- Simulate the smashing process
- Continue until 0 or 1 stone remains

DETAILED SOLUTION WITH VISUALIZATIONS
==================================

Example walkthrough with stones = [2,7,4,1,8,1]:

Initial state:
[2,7,4,1,8,1] -> Max Heap: [8,7,4,2,1,1]
                     8
                   /   \
                  7     4
                /  \   /
               2    1 1

Step-by-step process:
1. Start: [8,7,4,2,1,1]
2. Take 8 and 7: |8-7| = 1
3. Now: [4,2,1,1,1]
4. Take 4 and 2: |4-2| = 2
5. Now: [2,1,1,1]
6. Take 2 and 1: |2-1| = 1
7. Now: [1,1,1]
8. Take 1 and 1: |1-1| = 0
9. Now: [1]
Result: 1
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        Approach using max heap (implemented as negative min heap in Python)
        Time: O(nlogn) - n heap operations of logn each
        Space: O(n) - for the heap
        
        Example walkthrough:
        stones = [2,7,4,1,8,1]
        1. Convert to max heap by negating: [-8,-7,-4,-2,-1,-1]
        2. Process heaviest stones until 1 or 0 remain
        """
        # Convert to max heap by negating all values
        # Python only has min heap, so we negate to simulate max heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)  # O(n)
        
        """
        Visualization of initial heap:
             -8
           /    \
         -7     -4
        /  \    /
      -2   -1  -1
        """
        
        # Process stones until 1 or 0 remain
        while len(stones) > 1:
            # Get two heaviest stones (most negative)
            stone1 = -heapq.heappop(stones)  # Negate back to positive
            stone2 = -heapq.heappop(stones)
            
            """
            Example first iteration:
            stone1 = 8 (from -8)
            stone2 = 7 (from -7)
            Remaining heap:
                 -4
               /    \
             -2     -1
            /
          -1
            """
            
            # If stones are different, add back the difference
            if stone1 != stone2:
                heapq.heappush(stones, -(stone1 - stone2))
                
            """
            After first smash:
            8-7 = 1, add -1 to heap
            New heap:
                 -4
               /    \
             -2     -1
            /  \
          -1   -1
            """
        
        # Return remaining stone or 0 if none left
        return -stones[0] if stones else 0

"""
ALTERNATIVE SOLUTION USING SORTING
===============================
"""
class SortingSolution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        Alternative approach using sorting
        Time: O(n²logn) - n iterations with sorting each time
        Space: O(1) - modifies input array
        """
        stones.sort()  # Start with sorted array
        
        while len(stones) > 1:
            # Take two largest stones (end of sorted array)
            stone1 = stones.pop()  # Largest
            stone2 = stones.pop()  # Second largest
            
            # If different, add back the difference
            if stone1 != stone2:
                # Find insertion point to maintain sorted order
                diff = stone1 - stone2
                left, right = 0, len(stones)
                while left < right:
                    mid = (left + right) // 2
                    if stones[mid] < diff:
                        left = mid + 1
                    else:
                        right = mid
                stones.insert(left, diff)
        
        return stones[0] if stones else 0

"""
COMPARISON OF APPROACHES:

1. Heap Solution:
Pros:
- O(nlogn) time complexity
- Efficient for dynamic updates
- Clean implementation
Cons:
- O(n) extra space
- Needs understanding of heap operations

2. Sorting Solution:
Pros:
- Simpler to understand
- No extra space (in-place)
- Good for small arrays
Cons:
- O(n²logn) time complexity
- Less efficient for larger arrays

Memory Usage Visualization:
Heap approach:
- Initial heap creation: O(n)
- Each operation: O(logn)
- Total operations: O(n)
- Peak memory: O(n)

Sorting approach:
- In-place sorting: O(1) extra
- Each operation: O(nlogn)
- Total operations: O(n)
- Peak memory: O(1)

Example Memory States for [2,7,4,1,8,1]:

Initial:       [2,7,4,1,8,1]
After sort:    [1,1,2,4,7,8]
First smash:   [1,1,2,4,1]  (8-7=1)
Second smash:  [1,1,1,2]    (4-2=2)
Third smash:   [1,1,1]      (2-1=1)
Fourth smash:  [1]          (1-1=0, 1 remains)
"""

def test_solutions():
    # Test cases
    test_cases = [
        [2,7,4,1,8,1],
        [1],
        [2,2],
        [10,5,3,8,2]
    ]
    
    # Create instances
    heap_sol = Solution()
    sort_sol = SortingSolution()
    
    # Test and compare
    for stones in test_cases:
        print(f"\nTest case: {stones}")
        print(f"Heap solution: {heap_sol.lastStoneWeight(stones.copy())}")
        print(f"Sort solution: {sort_sol.lastStoneWeight(stones.copy())}")

if __name__ == "__main__":
    test_solutions()