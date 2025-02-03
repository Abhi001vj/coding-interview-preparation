# Minimum Swaps to Sort Array

## Problem Statement
Given an array of integers, find the minimum number of swaps needed to sort the array in ascending order.

### Examples
```
Input:  [2, 8, 5, 4]
Output: 1
Explanation: Swap 8 with 4 to get [2, 4, 5, 8]

Input:  [10, 19, 6, 3, 5]
Output: 2
Explanation: Swap 10 with 3, then 19 with 5
```

## Solution Approaches

### 1. Greedy Approach (Selection Sort Based)
```python
def min_swaps_greedy(arr):
    """
    Time: O(n²)
    Space: O(1)
    """
    n = len(arr)
    swaps = 0
    
    # For each position
    for i in range(n):
        # Find minimum element in remaining array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # If minimum isn't current position, swap
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            
    return swaps

"""
Visual Example: [2, 8, 5, 4]

Step 1: i = 0
- Find min in [2,8,5,4]: 2 is min
- Already in position 0
- Array: [2,8,5,4]

Step 2: i = 1
- Find min in [8,5,4]: 4 is min
- Swap 8 and 4
- Array: [2,4,5,8]
- swaps = 1

Step 3: i = 2
- Find min in [5,8]: 5 is min
- Already in position
- Array: [2,4,5,8]

Step 4: i = 3
- Only 8 remains
- Done

Total swaps: 1
"""
```

### 2. Cycle Detection Method
```python
def min_swaps_cycles(arr):
    """
    Time: O(n)
    Space: O(n)
    """
    # Create position mapping
    pos = {val: i for i, val in enumerate(sorted(arr))}
    visited = set()
    swaps = 0
    
    for i in range(len(arr)):
        if i in visited or pos[arr[i]] == i:
            continue
            
        cycle_size = 0
        j = i
        while j not in visited:
            visited.add(j)
            j = pos[arr[j]]
            cycle_size += 1
            
        swaps += cycle_size - 1
        
    return swaps

"""
Visual Example: [2, 8, 5, 4]

1. Create position mapping:
   Sorted array: [2,4,5,8]
   pos = {2:0, 4:1, 5:2, 8:3}

2. Start at index 0 (value 2):
   2 should be at pos[2] = 0
   Already there! No cycle.

3. Start at index 1 (value 8):
   8 should be at pos[8] = 3
   3 has value 4, should be at pos[4] = 1
   Back to where we started!
   Cycle: 8 → 4 → 8
   Length = 2, needs 1 swap

4. Start at index 2 (value 5):
   Already visited as part of previous cycle

Total swaps = 1
"""
```

## Visualizations

### Example 1: [2, 8, 5, 4]
```
Initial:  [2, 8, 5, 4]
          ↓  ↓
Step 1:   [2, 4, 5, 8]  (1 swap)
Final:    [2, 4, 5, 8]

Cycle found: 8 ↔ 4 (one cycle of length 2)
```

### Example 2: [10, 19, 6, 3, 5]
```
Initial:  [10, 19, 6, 3, 5]
           ↓       ↓
Step 1:   [3, 19, 6, 10, 5]  (1 swap)
              ↓        ↓
Step 2:   [3, 5, 6, 10, 19]  (1 swap)
Final:    [3, 5, 6, 10, 19]

Cycles found:
1. 10 → 3 → 10 (length 2)
2. 19 → 5 → 19 (length 2)
```

## Time Complexity Analysis

### Greedy Approach:
- Finding minimum for each position: O(n)
- Doing this n times: O(n²)
- Space: O(1)

### Cycle Detection:
- Sorting for position mapping: O(n log n)
- Finding cycles: O(n) as each element visited once
- Space: O(n) for position mapping and visited set

## Edge Cases
```python
# Test cases
def test_min_swaps():
    cases = [
        # Already sorted
        ([1,2,3,4], 0),
        
        # Reverse sorted
        ([4,3,2,1], 2),
        
        # Single element
        ([1], 0),
        
        # Two elements
        ([2,1], 1),
        
        # All same value
        ([5,5,5,5], 0),
        
        # Multiple cycles
        ([6,4,2,8,3,1,5,7], 4)
    ]
    
    for arr, expected in cases:
        assert min_swaps_cycles(arr) == expected
```

## Follow-up Questions

1. Q: How would you handle duplicate elements?
   A: The current solution assumes unique elements. For duplicates, we'd need to modify the position mapping to handle multiple positions for same value.

2. Q: Can we optimize space usage?
   A: Yes, we can use the array itself as position mapping by marking visited elements, but it would modify the input array.

3. Q: How would you extend this to sort by custom criteria?
   A: Modify the position mapping creation to use the custom sorting criteria.

4. Q: What if we can only swap adjacent elements?
   A: This becomes a different problem (bubble sort) with potentially more swaps needed.