"""
Google Phone Screen: Distinct Combinations Problem

Problem Understanding:
1. Given two arrays of length 3 with values in range [0...n-1]
2. For each position, we can use values within t distance (wrapping around)
3. Need to find total distinct combinations possible

Visual Example:
n = 3, t = 1
arr1 = [0, 1, 2]
arr2 = [2, 0, 1]

For position 0 in arr1[0]=0:
Wrapping Around Visualization:
  2       0       1
  ↑       ↑       ↑
[0,1,2] wraps to [0,1,2]
Valid values for 0: [2,0,1] (t=1 means ±1 wrapping)
"""

def solve(n: int, t: int, arr1: List[int], arr2: List[int]) -> int:
    """
    Find number of distinct combinations possible
    Time: O(t * n)
    Space: O(n)
    
    Example walkthrough for n=3, t=1:
    arr1[0,1,2], arr2[2,0,1]
    
    For first position (0 in arr1):
    - Can use: [2,0,1] (wrapping with t=1)
    For second position (1 in arr1):
    - Can use: [0,1,2] (wrapping with t=1)
    And so on...
    """
    def get_possible_values(val: int, t: int, n: int) -> Set[int]:
        """
        Get all possible values within t distance of val
        Handles wrapping around
        
        Example: val=0, t=1, n=3
        Upper bound: (0+1)%3 = 1
        Lower bound: (0-1+3)%3 = 2
        Returns: {0,1,2}
        """
        possible = set()
        for i in range(-t, t+1):
            possible.add((val + i + n) % n)
        return possible
    
    def get_overlaps(d1: int, d2: int, t: int, n: int) -> int:
        """
        Count how many values overlap between possible values
        of d1 and d2 considering wrapping
        
        Example: d1=0, d2=2, t=1, n=3
        d1 possible: {2,0,1}
        d2 possible: {1,2,0}
        Overlap: 3 values
        """
        if d1 == d2:
            return 2 * t + 1
            
        set1 = get_possible_values(d1, t, n)
        set2 = get_possible_values(d2, t, n)
        return len(set1.intersection(set2))

    # Calculate maximum possible combinations
    # Each position has (2t + 1) choices due to wrapping
    single_pos_choices = 2 * t + 1
    max_combinations = 2 * (single_pos_choices ** 3)
    
    """
    Example calculation for t=1:
    single_pos_choices = 3 (can use current, +1, -1)
    For each array: 3 * 3 * 3 = 27 combinations
    Total max (2 arrays): 2 * 27 = 54 combinations
    """
    
    # Calculate overlaps for each position
    total_overlaps = 1
    for i in range(3):
        position_overlaps = get_overlaps(arr1[i], arr2[i], t, n)
        total_overlaps *= position_overlaps
        
    """
    Overlap calculation example:
    Position 0: arr1[0]=0, arr2[0]=2
    - Overlapping values: 3
    Position 1: arr1[1]=1, arr2[1]=0
    - Overlapping values: 3
    Position 2: arr1[2]=2, arr2[2]=1
    - Overlapping values: 3
    Total overlaps: 3 * 3 * 3 = 27
    """
    
    return max_combinations - total_overlaps

# Test cases with visualizations
def test_combinations():
    """
    Test Case 1:
    n=3, t=1
    arr1=[0,1,2], arr2=[2,0,1]
    
    Maximum combinations:
    - Each position has 3 choices (t=1)
    - Each array can make 27 combinations
    - Total max: 54 combinations
    
    Overlaps:
    - Each position has 3 overlapping values
    - Total overlaps: 27
    
    Result: 54 - 27 = 27 distinct combinations
    """
    test_cases = [
        {
            'n': 3,
            't': 1,
            'arr1': [0,1,2],
            'arr2': [2,0,1],
            'expected': 27
        },
        # Add more test cases
    ]
    
    for tc in test_cases:
        result = solve(tc['n'], tc['t'], tc['arr1'], tc['arr2'])
        assert result == tc['expected'], f"Expected {tc['expected']}, got {result}"

"""
Edge Cases to Consider:
1. t = 0 (only exact values)
2. t = n (all values possible)
3. arr1 = arr2 (complete overlap)
4. Maximum wrap-around (t > n)
5. n = 1 (single value possible)

Time Complexity Analysis:
- get_possible_values: O(t)
- get_overlaps: O(t)
- Main function: O(t) for each position
Total: O(t)

Space Complexity:
- Sets for possible values: O(t)
- No recursion or additional structures
Total: O(t)
"""