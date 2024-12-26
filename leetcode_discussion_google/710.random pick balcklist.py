# 710. Random Pick with Blacklist
# Solved
# Hard
# Topics
# Companies
# You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

# Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.

# Implement the Solution class:

# Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
# int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.
 

# Example 1:

# Input
# ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
# [[7, [2, 3, 5]], [], [], [], [], [], [], []]
# Output
# [null, 0, 4, 1, 6, 1, 0, 4]

# Explanation
# Solution solution = new Solution(7, [2, 3, 5]);
# solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that for every call of pick,
#                  // 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
# solution.pick(); // return 4
# solution.pick(); // return 1
# solution.pick(); // return 6
# solution.pick(); // return 1
# solution.pick(); // return 0
# solution.pick(); // return 4
 

# Constraints:

# 1 <= n <= 109
# 0 <= blacklist.length <= min(105, n - 1)
# 0 <= blacklist[i] < n
# All the values of blacklist are unique.
# At most 2 * 104 calls will be made to pick.
"""
PROBLEM SIMPLIFIED:
-----------------
Given: n=7, blacklist=[2,3,5]
Valid numbers: [0,1,4,6]
Goal: Return any valid number with equal probability (1/4 for each)

Key Requirements:
1. Minimize random() calls
2. Equal probability for all valid numbers
3. Efficient space usage

Let's implement all approaches with clear visualizations:

1. BRUTE FORCE (Inefficient but Simple)
-------------------------------------
Visualization:
n=7, blacklist=[2,3,5]

Numbers: [0][1][2][3][4][5][6]
              x  x     x
              blacklisted

Process: Keep generating random numbers until we get non-blacklisted one
"""

class BruteForceSolution:
    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.blackset = set(blacklist)  # For O(1) lookup
    
    def pick(self) -> int:
        num = random.randint(0, self.n-1)
        while num in self.blackset:  # Keep trying until valid
            num = random.randint(0, self.n-1)
        return num

"""
2. OPTIMAL MAPPING SOLUTION
-------------------------
Key Insight: Instead of rejecting numbers, remap blacklisted numbers

Visualization:
n=7, blacklist=[2,3,5]

Step 1: Identify valid range
[0][1][2][3][4][5][6]  <- Original array
      x  x     x        <- x marks blacklisted
<-valid->                <- valid range = 4 (n - len(blacklist))

Step 2: Create mapping
- Map 2 -> 6 (first blacklisted to last valid)
- Map 3 -> 4 (second blacklisted to second-last valid)
- 5 is outside valid range, ignore it

Final Mapping: {2:6, 3:4}

When picking:
- Generate random in [0,3]
- If number is in mapping (2,3), return mapped value
- If number is not in mapping (0,1), return as is
"""

class OptimalSolution:
    def __init__(self, n: int, blacklist: List[int]):
        self.mapping = {}
        self.valid_range = n - len(blacklist)
        
        # Create set of blacklisted numbers
        black_set = set(blacklist)
        
        # Find last valid number to map to
        last = n - 1
        
        # Create mappings for blacklisted numbers in valid range
        for b in blacklist:
            if b < self.valid_range:  # Only map numbers in valid range
                # Find next valid number to map to
                while last in black_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1
    
    def pick(self) -> int:
        # Generate random number in valid range
        p = random.randint(0, self.valid_range - 1)
        # Return mapped value if exists, otherwise return original
        return self.mapping.get(p, p)

"""
Example Usage:
------------
solution = OptimalSolution(7, [2,3,5])

Pick() examples:
1. random(0,3) returns 2:
   - 2 is in mapping -> returns 6
2. random(0,3) returns 1:
   - 1 not in mapping -> returns 1
3. random(0,3) returns 3:
   - 3 is in mapping -> returns 4
4. random(0,3) returns 0:
   - 0 not in mapping -> returns 0

Time Complexity: O(1) per pick
Space Complexity: O(B) where B is blacklist length
"""
"""
BINARY SEARCH SOLUTION FOR RANDOM PICK WITH BLACKLIST
--------------------------------------------------

Problem Understanding:
n = 7, blacklist = [2,3,5]
Valid numbers: [0,1,4,6]
Need: Pick any valid number with equal probability (1/4 each)

Key Insight for Binary Search Approach:
------------------------------------
Instead of storing all valid numbers, we can use binary search to find 
the kth valid number in the range [0,n-1]

Detailed Algorithm:
-----------------
1. Generate random k in range [0, valid_count-1]
2. Use binary search to find kth valid number
3. Count valid numbers up to mid point to navigate search

Visual Example:
-------------
n=7, blacklist=[2,3,5]
valid_count = 4 (total valid numbers)

If k=2 (wanting 3rd valid number):

Numbers:    [0][1][2][3][4][5][6]
Blacklist:        x  x     x
Valid idx:  [0][1]    [2][3]
            ^--want 2nd valid number
"""

class BinarySearchSolution:
    def __init__(self, n: int, blacklist: List[int]):
        """
        Initialize with range n and blacklist
        Time: O(1)
        Space: O(B) for blacklist set
        """
        self.n = n
        self.blackset = set(blacklist)  # For O(1) lookup
        self.valid_count = n - len(blacklist)
    
    def count_valid_numbers_until(self, x: int) -> int:
        """
        Count valid numbers in range [0,x]
        Time: O(1)
        
        Example:
        x=3, blacklist=[2,3]
        Returns 2 (numbers 0,1 are valid)
        """
        total = x + 1  # All numbers up to x
        blacklisted = len([num for num in self.blackset if num <= x])
        return total - blacklisted
    
    def pick(self) -> int:
        """
        Returns random valid number
        Time: O(log n)
        
        Example walkthrough:
        n=7, blacklist=[2,3,5]
        k=1 (want 2nd valid number)
        
        Step 1: left=0, right=6, mid=3
               [0,1,2,3,4,5,6]
                L   M     R
               valid_count(3) = 2 (too many)
        
        Step 2: left=0, right=3, mid=1
               [0,1,2,3]
                L M
               valid_count(1) = 2 (found!)
        """
        # Generate random k (which valid number we want)
        k = random.randint(0, self.valid_count - 1)
        
        left, right = 0, self.n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Count valid numbers up to mid
            valid_count = self.count_valid_numbers_until(mid)
            
            if valid_count > k:
                # Too many valid numbers, search left half
                right = mid
            else:
                # Too few valid numbers, search right half
                left = mid + 1
                
        # Skip blacklisted numbers
        while left in self.blackset:
            left += 1
            
        return left

"""
Complete Example:
---------------
n=7, blacklist=[2,3,5]

Valid numbers mapping:
Original: [0][1][2][3][4][5][6]
Valid:    [0][1]    [4]  [6]
Index:     0  1      2    3

When k=1:
1. Binary search for number with exactly 2 valid numbers before it
2. Search process:
   - mid=3: valid_count=2 (0,1 are valid) → move right
   - mid=5: valid_count=3 (0,1,4 are valid) → move left
   - mid=4: valid_count=3 (0,1,4 are valid) → found!
3. Return 4 (the 2nd valid number)

Time Complexity: O(log n) per pick
Space Complexity: O(B) for blacklist storage
"""