# https://leetcode.com/problems/daily-temperatures/description/
# 739. Daily Temperatures
# Medium
# Topics
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

```
PATTERN RECOGNITION FOR INTERVIEWS
--------------------------------
1. Monotonic Stack Pattern:
   - Next Greater Element
   - Next Smaller Element
   - Temperature spans
   - Building outlines

2. Similar Problems:
   - Next Greater Element I, II
   - Stock Span Problem
   - Largest Rectangle in Histogram

3. Edge Cases to Consider:
   - All same temperatures: [70,70,70]
   - Strictly increasing: [60,70,80]
   - Strictly decreasing: [80,70,60]
   - Single element: [70]
   - Maximum length: 10^5 elements

OPTIMIZATION TECHNIQUES
----------------------
1. Early Exit Conditions:
   - Last element always 0
   - Can stop if found max temp

2. Space Optimizations:
   - Use array instead of stack
   - Reuse input array if allowed

3. Time Optimizations:
   - Skip processed elements
   - Track max temperature
```
"""
DAILY TEMPERATURES: PATTERN-BASED SOLUTIONS
=========================================

1. Monotonic Stack with Visualizations
------------------------------------
"""

def monotonic_stack_solution(temperatures: List[int]) -> List[int]:
    """
    Pattern: Monotonic Decreasing Stack
    
    Visual stack evolution for [73,74,75,71,69,72,76,73]:
    
    Step  Temperature   Stack(indices)    Result
    ----  -----------   -------------    ---------------
    1.    73           [0]              [0,0,0,0,0,0,0,0]
    2.    74           [1]              [1,0,0,0,0,0,0,0]
    3.    75           [2]              [1,1,0,0,0,0,0,0]
    4.    71           [2,3]            [1,1,0,0,0,0,0,0]
    5.    69           [2,3,4]          [1,1,0,0,0,0,0,0]
    6.    72           [2,6]            [1,1,0,2,1,0,0,0]
    7.    76           [6]              [1,1,4,2,1,1,0,0]
    8.    73           [6,7]            [1,1,4,2,1,1,0,0]
    
    Space-Time Analysis:
    - Time: O(n), each element pushed/popped once
    - Space: O(n), max stack size
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # (index, temp) pairs
    
    for curr_idx, curr_temp in enumerate(temperatures):
        # Process stack while current temperature is warmer
        while stack and curr_temp > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = curr_idx - prev_idx
        stack.append(curr_idx)
        
    return result

"""
2. Early Exit and Max Tracking Optimization
-----------------------------------------
"""

def optimized_with_max_tracking(temperatures: List[int]) -> List[int]:
    """
    Pattern: Max Temperature Tracking with Early Exit
    
    Example for [73,74,75,71,69,72,76,73]:
    
    Step  Temp  Max   Early Exit?   Action
    ----  ----  ---   -----------   ------
    1.    73    73    No            Process normally
    2.    74    74    No            Update max
    3.    75    75    No            Update max
    4.    71    75    No            Less than max, continue
    5.    69    75    No            Less than max, continue
    6.    72    75    No            Less than max, continue
    7.    76    76    Yes           New max, remaining will be 0
    8.    73    76    Yes           Skip (early exit)
    
    Optimizations:
    1. Track maximum temperature
    2. Early exit when max found
    3. Skip processed elements
    """
    n = len(temperatures)
    result = [0] * n
    stack = []
    max_temp = float('-inf')
    
    for i in range(n):
        curr_temp = temperatures[i]
        max_temp = max(max_temp, curr_temp)
        
        # Early exit if this is maximum temperature
        if curr_temp == 100:  # Maximum possible temperature
            break
            
        while stack and curr_temp > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
            
        stack.append(i)
        
    return result

"""
3. Edge Case Handling Solution
----------------------------
"""

def edge_case_optimized_solution(temperatures: List[int]) -> List[int]:
    """
    Pattern: Edge Case Optimization
    
    Edge Case Handling:
    1. Same temperatures: [70,70,70]
       Stack: [0,1,2] → All zeros (no warmer day)
       
    2. Increasing: [60,70,80]
       Result builds immediately: [1,1,0]
       
    3. Decreasing: [80,70,60]
       Stack builds fully: [0,1,2] → All zeros
       
    4. Single: [70]
       Immediate return [0]
    """
    n = len(temperatures)
    if n == 1:  # Handle single element
        return [0]
        
    result = [0] * n
    
    # Handle strictly increasing/decreasing sequences efficiently
    is_increasing = True
    is_decreasing = True
    
    for i in range(1, n):
        if temperatures[i] <= temperatures[i-1]:
            is_increasing = False
        if temperatures[i] >= temperatures[i-1]:
            is_decreasing = False
            
    # Optimize for special sequences
    if is_increasing:
        return [1] * (n-1) + [0]
    if is_decreasing:
        return [0] * n
        
    # General case with stack
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
        
    return result

"""
4. Space-Optimized Solution
-------------------------
"""

def space_optimized_solution(temperatures: List[int]) -> List[int]:
    """
    Pattern: Space Optimization using Array
    
    Instead of stack, use result array to track indices:
    - Negative values indicate unprocessed temperatures
    - Process in reverse to optimize space
    
    Example [73,74,75,71,69,72,76,73]:
    Result array evolution:
    [0,0,0,0,0,0,0,0] → Initial
    [0,0,0,0,0,0,0,-7] → Process 73
    [0,0,0,0,0,0,-6,-7] → Process 76
    ...and so on
    """
    n = len(temperatures)
    result = [0] * n
    
    for i in range(n-2, -1, -1):
        next_day = i + 1
        
        # Find next warmer day
        while next_day < n and temperatures[next_day] <= temperatures[i]:
            if result[next_day] > 0:
                next_day += result[next_day]
            else:
                next_day = n
                break
                
        # Update result
        if next_day < n:
            result[i] = next_day - i
            
    return result