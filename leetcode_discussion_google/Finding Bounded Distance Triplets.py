"""
Problem: Find Triplets with Bounded Differences
Given: 
- Three sorted arrays a[], b[], c[] of size n
- Distance bound d
- Need triplets (i,j,k) where |a[i]-b[j]|≤d, |b[j]-c[k]|≤d, |c[k]-a[i]|≤d

Example:
a = [1, 3, 5]
b = [2, 3, 4]
c = [2, 3, 4]
d = 1

Valid triplets visualization:
For a[i]=3:
  b[j]=2,3,4 are all within d=1
  For b[j]=3:
    c[k]=2,3,4 are all within d=1
    And all these c[k] are within d=1 of a[i]=3

Approaches:
1. Brute Force: O(n³)
2. Binary Search: O(n²logn)
3. Three Pointers: O(n²)
"""

def find_triplets_brute_force(a: list, b: list, c: list, d: int) -> list:
    """
    Brute force approach - check all possible triplets
    Time: O(n³)
    Space: O(1) excluding output storage
    """
    n = len(a)
    result = []
    
    for i in range(n):
        for j in range(n):
            if abs(a[i] - b[j]) > d:
                continue
            for k in range(n):
                if (abs(b[j] - c[k]) <= d and 
                    abs(c[k] - a[i]) <= d):
                    result.append((a[i], b[j], c[k]))
    
    return result

def find_triplets_binary_search(a: list, b: list, c: list, d: int) -> list:
    """
    Binary search approach - for each a[i], b[j], binary search valid c[k]
    Time: O(n²logn)
    Space: O(1) excluding output storage
    """
    def binary_search_range(arr: list, target: int, d: int) -> tuple:
        """Find range of values within d of target using binary search"""
        n = len(arr)
        
        # Find leftmost valid value
        left, right = 0, n-1
        left_bound = n
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target - d:
                left_bound = mid
                right = mid - 1
            else:
                left = mid + 1
                
        # Find rightmost valid value
        left, right = 0, n-1
        right_bound = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= target + d:
                right_bound = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return left_bound, right_bound
    
    n = len(a)
    result = []
    
    for i in range(n):
        for j in range(n):
            if abs(a[i] - b[j]) > d:
                continue
                
            # Binary search for valid c[k]
            left, right = binary_search_range(c, b[j], d)
            if left <= right:
                for k in range(left, right + 1):
                    if abs(c[k] - a[i]) <= d:
                        result.append((a[i], b[j], c[k]))
    
    return result

def find_triplets_three_pointers(a: list, b: list, c: list, d: int) -> list:
    """
    Three pointers approach - maintain three pointers and move them optimally
    Time: O(n²)
    Space: O(1) excluding output storage
    
    Key insight: Since arrays are sorted, we can maintain windows of valid values
    and slide them efficiently
    """
    n = len(a)
    result = []
    
    for i in range(n):
        # Initialize pointers for b and c arrays
        j_start = 0
        while j_start < n and b[j_start] < a[i] - d:
            j_start += 1
            
        k_start = 0
        while k_start < n and c[k_start] < min(a[i]