"""
Array Doubling and Shuffling Problem

Part 1: Double and Shuffle
Input: Original array
Output: Doubled values array shuffled

Part 2: Recover Original
Input: Doubled shuffled array
Output: Original array
"""

import random
from typing import List

def double_and_shuffle(nums: List[int]) -> List[int]:
    """
    Part 1: Create doubled array and shuffle
    Time: O(n) for creation + O(n) for shuffle = O(n)
    Space: O(n) for new array
    
    Example Visualization:
    Input: [1,2,4]
    Step 1 - Double values:
    Original: [1   ,2   ,4   ]
    Doubled:  [1,1 ,2,2 ,4,4 ] 
    
    Step 2 - Shuffle:
    [1,1,2,2,4,4] -> [4,8,4,2,1,2]
    """
    # Create array with original and doubled values
    result = []
    for num in nums:
        result.extend([num, num * 2])
        
    # Shuffle the array
    random.shuffle(result)
    return result

def recover_original(doubled: List[int]) -> List[int]:
    """
    Part 2: Recover original array from doubled shuffled array
    Time: O(n log n) for sorting
    Space: O(n) for result array
    
    Example Visualization:
    Input: [4,8,4,2,1,2]
    
    Step 1 - Group by value/2:
    4: [4,8]  (original 4)
    2: [2,4]  (original 2)
    1: [1,2]  (original 1)
    
    Step 2 - Extract originals:
    4 -> min(4,8/2) = 4
    2 -> min(2,4/2) = 2
    1 -> min(1,2/2) = 1
    """
    # Dictionary to store value counts
    counts = {}
    for num in doubled:
        counts[num] = counts.get(num, 0) + 1
        
    # Find original values
    result = []
    used = set()
    
    for num in sorted(doubled):
        if num in used:
            continue
            
        # Check if there's a doubled value
        if num % 2 == 0 and num // 2 in counts:
            small = num // 2
            large = num
        else:
            small = num
            large = num * 2
            
        if counts.get(small, 0) > 0 and counts.get(large, 0) > 0:
            result.append(small)
            counts[small] -= 1
            counts[large] -= 1
            used.add(small)
            used.add(large)
            
    return result

# Test cases
def test_array_operations():
    """
    Test both parts with various inputs
    """
    test_cases = [
        [1, 2, 4],
        [1],
        [5, 10],
        [3, 6, 9, 12]
    ]
    
    for nums in test_cases:
        # Test Part 1
        doubled = double_and_shuffle(nums[:])
        assert len(doubled) == 2 * len(nums)
        assert sorted(doubled) == sorted(nums + [x*2 for x in nums])
        
        # Test Part 2
        recovered = recover_original(doubled)
        assert sorted(recovered) == sorted(nums)
        
        print(f"Original: {nums}")
        print(f"Doubled and shuffled: {doubled}")
        print(f"Recovered: {recovered}")
        print()

"""
Edge Cases:
1. Empty array
2. Single element
3. Array with zeros
4. Array with negative numbers
5. Array with duplicates (not in original problem)

Time Complexity Analysis:
Part 1:
- Creating doubled array: O(n)
- Shuffling: O(n)
- Total: O(n)

Part 2:
- Counting values: O(n)
- Sorting: O(n log n)
- Processing values: O(n)
- Total: O(n log n)

Space Complexity:
Part 1: O(n) for result array
Part 2: O(n) for counts dictionary and result array

Alternative Approaches for Part 2:
1. Sort and pair approach:
   - Sort array
   - Match consecutive pairs
   - Time: O(n log n)
   - Space: O(n)

2. Hash table approach (current):
   - Count frequencies
   - Match values with doubles
   - Time: O(n log n)
   - Space: O(n)
"""