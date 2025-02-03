"""
Median of Two Sorted Arrays
Time: O(log(min(m,n)))
Space: O(1)

Visual Example:
nums1 = [1, 3, 8, 9]
nums2 = [2, 4, 7]

Partition Visualization:
nums1: [1, 3 | 8, 9]
nums2: [2 | 4, 7]
Combined: [1, 2, 3 | 4, 7, 8, 9]
        left half | right half

Key Insight: Find correct partition point where:
1. left1 <= right2
2. left2 <= right1
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find median using binary search on smaller array
        
        Example walkthrough:
        nums1 = [1,3], nums2 = [2]
        
        Step 1: Ensure nums1 is smaller
        If not, swap arrays
        
        Step 2: Binary search for partition
        partition1: split nums1
        partition2: split nums2 accordingly
        """
        # Make sure nums1 is the smaller array
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
            
        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1
        
        while low <= high:
            """
            Visual for each iteration:
            nums1: [....cut1....]
            nums2: [....cut2....]
            
            left1 | right1
            left2 | right2
            
            Check if this partition is valid
            """
            # Get partition points
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1
            
            # Get values around partitions
            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            right1 = float('inf') if cut1 == n1 else nums1[cut1]
            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right2 = float('inf') if cut2 == n2 else nums2[cut2]
            
            """
            Example state:
            nums1 = [1,3], cut1 = 1
            nums1: [1 | 3]
            left1 = 1, right1 = 3
            
            nums2 = [2], cut2 = 1
            nums2: [2 | ]
            left2 = 2, right2 = inf
            """
            
            # Check if partition is valid
            if left1 <= right2 and left2 <= right1:
                # Found correct partition
                if (n1 + n2) % 2 == 0:
                    # Even length - average of two middle values
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    # Odd length - maximum of left values
                    return max(left1, left2)
            
            elif left1 > right2:
                # Too many elements on left in nums1
                high = cut1 - 1
            else:
                # Too few elements on left in nums1
                low = cut1 + 1
                
        return 0.0

def test_median():
    """
    Test cases for median finding
    """
    test_cases = [
        {
            'nums1': [1,3],
            'nums2': [2],
            'expected': 2.0
        },
        {
            'nums1': [1,2],
            'nums2': [3,4],
            'expected': 2.5
        },
        {
            'nums1': [],
            'nums2': [1],
            'expected': 1.0
        },
        {
            'nums1': [2],
            'nums2': [],
            'expected': 2.0
        }
    ]
    
    solution = Solution()
    for tc in test_cases:
        result = solution.findMedianSortedArrays(tc['nums1'], tc['nums2'])
        assert abs(result - tc['expected']) < 1e-5

"""
Detailed Analysis:

1. Why Binary Search Works:
   - We only need to find the correct partition point
   - Each step eliminates half of possibilities
   - Guaranteed to find partition if exists
   
2. Time Complexity: O(log(min(m,n)))
   - Binary search on smaller array
   - Each step divides search space by 2
   
3. Space Complexity: O(1)
   - Only using constant extra space
   - No recursion or additional data structures

Edge Cases:
1. Empty arrays
2. Single element arrays
3. Even vs odd total length
4. Arrays of very different sizes
5. Duplicate elements
6. Negative numbers

Optimization Notes:
1. Always search on smaller array
2. Use infinity for boundary conditions
3. Handle even/odd length separately
4. Early exit conditions

Example Walkthrough:
nums1 = [1,3], nums2 = [2]

Initial partition:
[1 | 3]
[2 | ]

Check condition:
left1 (1) <= right2 (inf) ✓
left2 (2) <= right1 (3) ✓

Odd total length:
Return max(left1, left2) = 2
"""