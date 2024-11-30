# https://leetcode.com/problems/trapping-rain-water/description/
# 42. Trapping Rain Water
# Hard
# Topics
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

"""
TRAPPING RAIN WATER: Comprehensive Solution Analysis
=================================================

The problem presents an elevation map where we need to calculate trapped water.
Let's analyze each approach with detailed visualizations and explanations.

Given example: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Visual representation:
                     __
         __         |  |
    __   |  |__    |  |__    __
   |  |  |     |   |     |__|  |
___|  |__|     |___|           |___

Water trapped (marked with .):
                     __
         __    .    |  |
    __   |  |__    |  |__    __
   |  |  |     |   |     |__|  |
___|  |__|     |___|           |___

Key insight: For any position i, water trapped = min(maxLeft, maxRight) - height[i]
"""

def trap_brute_force(height: List[int]) -> int:
    """
    Brute Force Approach:
    For each position, find the highest bars on left and right.
    
    Visual example for position i=5 (height[5]=0):
    [0,1,0,2,1,0,1,3,2,1,2,1]
         leftMax=2 →  ← rightMax=3
                |0|
    Water at i=5 = min(2,3) - 0 = 2 units
    
    Time: O(n²), Space: O(1)
    """
    if not height:
        return 0
    n = len(height)
    res = 0
    
    # For each position, calculate water trapped
    for i in range(n):
        leftMax = rightMax = height[i]
        
        # Find highest bar on left
        for j in range(i):
            leftMax = max(leftMax, height[j])
            
        # Find highest bar on right    
        for j in range(i + 1, n):
            rightMax = max(rightMax, height[j])
            
        # Add trapped water at current position    
        res += min(leftMax, rightMax) - height[i]
    return res

def trap_prefix_arrays(height: List[int]) -> int:
    """
    Prefix & Suffix Arrays Approach:
    Precompute max heights from left and right.
    
    Visual array evolution:
    Original:  [0,1,0,2,1,0,1,3,2,1,2,1]
    leftMax:   [0,1,1,2,2,2,2,3,3,3,3,3]
    rightMax:  [3,3,3,3,3,3,3,3,2,2,2,1]
    
    For each i:
    water[i] = min(leftMax[i], rightMax[i]) - height[i]
    
    Time: O(n), Space: O(n)
    """
    n = len(height)
    if n == 0:
        return 0
        
    # Initialize arrays
    leftMax = [0] * n
    rightMax = [0] * n
    
    # Fill leftMax array
    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], height[i])
    
    # Fill rightMax array    
    rightMax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], height[i])
    
    # Calculate trapped water
    res = 0
    for i in range(n):
        res += min(leftMax[i], rightMax[i]) - height[i]
    return res

def trap_stack(height: List[int]) -> int:
    """
    Stack-based Approach:
    Maintain a stack of decreasing heights.
    
    Visual stack evolution for [0,1,0,2]:
    1. Push 0: stack=[0]
    2. Push 1: Calculate water for 0
              stack=[1]
    3. Push 0: stack=[1,0]
    4. Push 2: Calculate water between 1 and 2
              stack=[2]
    
    Time: O(n), Space: O(n)
    """
    if not height:
        return 0
    stack = []
    res = 0
    
    for i in range(len(height)):
        # While current height creates a container
        while stack and height[i] >= height[stack[-1]]:
            mid = height[stack.pop()]
            if stack:
                # Calculate water trapped in container
                h = min(height[i], height[stack[-1]]) - mid
                w = i - stack[-1] - 1
                res += h * w
        stack.append(i)
    return res

def trap_two_pointers(height: List[int]) -> int:
    """
    Two Pointers Approach:
    Move inward from both ends, tracking max heights.
    
    Visual example:
    [0,1,0,2,1,0,1,3,2,1,2,1]
     L                     R
    leftMax=0          rightMax=1
    
    Move pointers based on which side has smaller max height.
    This ensures we can calculate trapped water at current position.
    
    Time: O(n), Space: O(1)
    """
    if not height:
        return 0
        
    l, r = 0, len(height) - 1
    leftMax = height[l]
    rightMax = height[r]
    res = 0
    
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
            
    return res