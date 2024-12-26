# https://leetcode.com/problems/find-the-duplicate-number/description/
# 287. Find the Duplicate Number
# Medium
# Topics
# Companies
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity

```python
"""
FIND DUPLICATE NUMBER: Comprehensive Analysis
=========================================

Key Patterns:
1. Floyd's Cycle Detection (Tortoise and Hare)
2. Binary Search
3. Bit Manipulation
4. Index as Hash Key

Critical Insights:
1. Numbers are in range [1, n]
2. Array length is n + 1
3. Only one duplicate number
4. Can't modify array
5. Need constant space
"""

def binary_search_solution(nums: List[int]) -> int:
    """
    APPROACH 1: BINARY SEARCH
    Pattern: Count numbers <= mid
    
    Example: nums = [1,3,4,2,2]
    
    Visual Process:
    1. Range [1,4], mid = 2
       Count ≤ 2: [1,2,2] = 3 numbers
       2 < 3, duplicate in [1,2]
    
    2. Range [1,2], mid = 1
       Count ≤ 1: [1] = 1 number
       1 = 1, duplicate in [2,2]
    
    3. Range [2,2]
       Answer = 2
    
    Time: O(n log n)
    Space: O(1)
    """
    left, right = 1, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        count = sum(num <= mid for num in nums)
        
        # If count > mid, duplicate in left half
        if count > mid:
            right = mid
        else:
            left = mid + 1
            
    return left

def cycle_detection_solution(nums: List[int]) -> int:
    """
    APPROACH 2: FLOYD'S CYCLE DETECTION
    Pattern: Linked List Cycle Detection
    
    Example: nums = [1,3,4,2,2]
    Index:    0 1 2 3 4
    
    Treating array as linked list:
    index 0 → nums[0] = 1 → nums[1] = 3 → nums[3] = 2 → nums[2] = 4 → nums[4] = 2
                                                        ↑________________________|
    
    Phase 1: Find intersection
    Tortoise: 0→1→3→2→4→2→4→2
    Hare:     0→1→3→4→4→4→4→4
    Meet at index 4
    
    Phase 2: Find cycle start
    Move pointer from start and intersection
    Until they meet at duplicate
    
    Time: O(n)
    Space: O(1)
    """
    # Phase 1: Find intersection
    tortoise = hare = nums[0]
    
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
            
    # Phase 2: Find cycle start
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
        
    return hare

def bit_manipulation_solution(nums: List[int]) -> int:
    """
    APPROACH 3: BIT MANIPULATION
    Pattern: XOR properties
    
    Example: nums = [1,3,4,2,2]
    
    Visual Process:
    1. For each bit position:
       Count 1s in nums vs 1s in [1,n]
       
    2. If count in nums > count in [1,n]
       Bit is set in duplicate number
    
    Time: O(n log n)
    Space: O(1)
    """
    duplicate = 0
    n = len(nums) - 1
    
    # Check each bit
    for bit in range(32):
        mask = 1 << bit
        count_nums = sum(bool(num & mask) for num in nums)
        count_range = sum(bool(i & mask) for i in range(1, n + 1))
        
        if count_nums > count_range:
            duplicate |= mask
            
    return duplicate

def index_marking_solution(nums: List[int]) -> int:
    """
    APPROACH 4: NEGATIVE MARKING (modifies array)
    Pattern: Use index as hash key
    Note: This violates "don't modify array" constraint
    
    Example: nums = [1,3,4,2,2]
    
    Process:
    1. [1,3,4,2,2] → mark nums[1] negative
    2. [1,-3,4,2,2] → mark nums[3] negative
    3. [1,-3,4,-2,2] → mark nums[4] negative
    4. [1,-3,4,-2,-2] → try mark nums[2], already negative!
    
    Time: O(n)
    Space: O(1)
    """
    for num in nums:
        index = abs(num)
        if nums[index] > 0:
            nums[index] *= -1
        else:
            return index
    return 0

"""
COMPLEXITY ANALYSIS
-----------------
1. Binary Search:
   Time: O(n log n)
   Space: O(1)
   
2. Floyd's Cycle:
   Time: O(n)
   Space: O(1)
   
3. Bit Manipulation:
   Time: O(n log n)
   Space: O(1)

MATHEMATICAL PROOF OF DUPLICATE
----------------------------
1. Array has n+1 numbers
2. Each number in range [1,n]
3. By Pigeonhole Principle:
   n numbers can fill n slots
   n+1 numbers must have duplicate

EDGE CASES
---------
1. Minimum array: [1,1]
2. All same number: [3,3,3,3]
3. Duplicate at start: [2,2,3,4,1]
4. Duplicate at end: [1,2,3,4,4]

VISUALIZATION OF CYCLE DETECTION
-----------------------------
nums = [1,3,4,2,2]

Array as Graph:
index → value
0 → 1
1 → 3
2 → 4
3 → 2
4 → 2

Makes cycle:
0 → 1 → 3 → 2 → 4 ⟲

Movement:
Tortoise: 1 step
0→1→3→2→4→2
Hare: 2 steps
0→1→3→2→4→2

Meet at 2 (duplicate number)
"""
```

```python
"""
FIND DUPLICATE NUMBER: All Approaches Analysis
==========================================
Example Array: nums = [1,3,4,2,2]
"""

def sorting_solution(nums: List[int]) -> int:
    """
    APPROACH 1: SORTING
    ------------------
    Visual Process:
    Original: [1,3,4,2,2]
    
    Sorting Steps:
    1. [1,3,4,2,2] → [1,2,2,3,4]
              ^  ^    Compare adjacent
    2. [1,2,2,3,4]
         ^ ^      Found duplicate!
    
    Time: O(n log n)
    Space: O(1) or O(n) depending on sort
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
    return -1

def hashset_solution(nums: List[int]) -> int:
    """
    APPROACH 2: HASH SET
    ------------------
    Visual Process:
    Array: [1,3,4,2,2]
    
    Step    Number    Set         Result
    1       1         {1}         continue
    2       3         {1,3}       continue
    3       4         {1,3,4}     continue
    4       2         {1,3,4,2}   continue
    5       2         {1,3,4,2}   Found! (2 in set)
    
    Time: O(n)
    Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

def array_marking_solution(nums: List[int]) -> int:
    """
    APPROACH 3: ARRAY MARKING
    -----------------------
    Visual Process for [1,3,4,2,2]:
    
    Index:  0  1  2  3  4
    Array:  [1,3,4,2,2]
    
    Step   Number   Seen Array      Action
    1      1        [1,0,0,0,0]    Mark 1
    2      3        [1,0,0,1,0]    Mark 3
    3      4        [1,0,0,1,1]    Mark 4
    4      2        [1,1,0,1,1]    Mark 2
    5      2        [1,1,1,1,1]    Found! (already marked)
    
    Time: O(n)
    Space: O(n)
    """
    seen = [0] * len(nums)
    for num in nums:
        if seen[num - 1]:
            return num
        seen[num - 1] = 1
    return -1

def negative_marking_solution(nums: List[int]) -> int:
    """
    APPROACH 4: NEGATIVE MARKING
    --------------------------
    Visual Process for [1,3,4,2,2]:
    
    Step   Number   Array State        Action
    1      1        [-1,3,4,2,2]      Mark index 1
    2      3        [-1,-3,4,2,2]     Mark index 3
    3      4        [-1,-3,4,-2,2]    Mark index 4
    4      2        [-1,-3,4,-2,-2]   Mark index 2
    5      2        Found! (already negative)
    
    Time: O(n)
    Space: O(1)
    """
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            return abs(num)
        nums[idx] *= -1
    return -1

def binary_search_solution(nums: List[int]) -> int:
    """
    APPROACH 5: BINARY SEARCH
    -----------------------
    Example: [1,3,4,2,2]
    Range: [1,4]
    
    Visual Search Process:
    Step   Range    Mid   Count≤Mid   Action
    1      [1,4]    2     3           high=2 (3>2)
    2      [1,2]    1     1           low=2 (1=1)
    3      [2,2]    2     Found!      count=3>2
    
    Time: O(n log n)
    Space: O(1)
    """
    low, high = 1, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        count = sum(1 for num in nums if num <= mid)
        if count <= mid:
            low = mid + 1
        else:
            high = mid
    return low

def bit_manipulation_solution(nums: List[int]) -> int:
    """
    APPROACH 6: BIT MANIPULATION
    --------------------------
    Example: [1,3,4,2,2]
    
    Visual Bit Analysis:
    Position   Nums Count   Range Count   Result
    0-bit      3           2             1
    1-bit      2           2             0
    2-bit      1           1             0
    
    Result: 2 (binary 10)
    
    Time: O(32*n)
    Space: O(1)
    """
    n = len(nums)
    res = 0
    for b in range(32):
        nums_count = sum(1 for num in nums if num & (1 << b))
        range_count = sum(1 for i in range(1, n) if i & (1 << b))
        if nums_count > range_count:
            res |= (1 << b)
    return res

def floyd_cycle_solution(nums: List[int]) -> int:
    """
    APPROACH 7: FLOYD'S CYCLE (OPTIMAL)
    --------------------------------
    Example: [1,3,4,2,2]
    
    Visual Path:
    Index:  0→1→3→2→4
           Values: 1→3→2→4→2 (cycle!)
    
    Movement Table:
    Step   Slow   Fast   Status
    1      1      3      Continue
    2      3      4      Continue
    3      2      2      Meet!
    
    After Meet:
    Step   Slow2  Slow   Status
    1      1      4      Continue
    2      3      2      Continue
    3      2      2      Found!
    
    Time: O(n)
    Space: O(1)
    """
    slow = fast = nums[0]
    # Find meeting point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find cycle start
    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow

"""
COMPARISON OF APPROACHES
----------------------
1. Sorting:
   + Simple to implement
   - Modifies array
   - O(n log n) time

2. Hash Set:
   + Simple and intuitive
   + O(n) time
   - O(n) space

3. Array Marking:
   + O(n) time
   - O(n) space
   - Extra array needed

4. Negative Marking:
   + O(1) space
   - Modifies input array

5. Binary Search:
   + Doesn't modify array
   + O(1) space
   - O(n log n) time

6. Bit Manipulation:
   + Clever approach
   + O(1) space
   - Complex implementation

7. Floyd's Cycle:
   + Optimal (time and space)
   + Doesn't modify array
   - Complex concept
"""