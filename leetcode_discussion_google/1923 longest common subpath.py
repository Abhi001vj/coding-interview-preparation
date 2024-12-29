# https://leetcode.com/problems/longest-common-subpath/description/
# 1923. Longest Common Subpath
# Hard
# Topics
# Companies
# Hint
# There is a country of n cities numbered from 0 to n - 1. In this country, there is a road connecting every pair of cities.

# There are m friends numbered from 0 to m - 1 who are traveling through the country. Each one of them will take a path consisting of some cities. Each path is represented by an integer array that contains the visited cities in order. The path may contain a city more than once, but the same city will not be listed consecutively.

# Given an integer n and a 2D integer array paths where paths[i] is an integer array representing the path of the ith friend, return the length of the longest common subpath that is shared by every friend's path, or 0 if there is no common subpath at all.

# A subpath of a path is a contiguous sequence of cities within that path.

 

# Example 1:

# Input: n = 5, paths = [[0,1,2,3,4],
#                        [2,3,4],
#                        [4,0,1,2,3]]
# Output: 2
# Explanation: The longest common subpath is [2,3].
# Example 2:

# Input: n = 3, paths = [[0],[1],[2]]
# Output: 0
# Explanation: There is no common subpath shared by the three paths.
# Example 3:

# Input: n = 5, paths = [[0,1,2,3,4],
#                        [4,3,2,1,0]]
# Output: 1
# Explanation: The possible longest common subpaths are [0], [1], [2], [3], and [4]. All have a length of 1.
 

# Constraints:

# 1 <= n <= 105
# m == paths.length
# 2 <= m <= 105
# sum(paths[i].length) <= 105
# 0 <= paths[i][j] < n
# The same city is not listed multiple times consecutively in paths[i].
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 8.2K
# Submissions
# 28.6K
# Acceptance Rate
# 28.7%
# Topics
# Companies
# 0 - 6 months
# Amazon
# 3
# Hint 1
# If there is a common path with length x, there is for sure a common path of length y where y < x.
# Hint 2
# We can use binary search over the answer with the range [0, min(path[i].length)].
# Hint 3
# Using binary search, we want to verify if we have a common path of length m. We can achieve this using hashing.


"""
Simpler Solution using Sliding Window

Key Idea:
1. For each possible window length
2. Get all subpaths of that length from first path
3. Check if any of these subpaths exists in all other paths

Example:
paths = [[0,1,2,3,4], [2,3,4], [4,0,1,2,3]]
length = 2

First path windows:
[0,1], [1,2], [2,3], [3,4]

Check each window in other paths:
[2,3] exists in all paths -> This is an answer!
"""

def findLongestCommonSubpath(n: int, paths: List[List[int]]) -> int:
    # Helper function to get all subpaths of given length
    def get_subpaths(path, length):
        subpaths = []
        for i in range(len(path) - length + 1):
            # Convert subpath to tuple for hashability
            subpath = tuple(path[i:i + length])
            subpaths.append(subpath)
        return set(subpaths)
    
    # Helper function to check if subpath exists in path
    def has_subpath(path, subpath):
        subpath_len = len(subpath)
        for i in range(len(path) - subpath_len + 1):
            if tuple(path[i:i + subpath_len]) == subpath:
                return True
        return False

    # Binary search to find longest common length
    left = 0
    right = min(len(path) for path in paths)
    
    while left <= right:
        mid = (left + right) // 2
        
        # Get all possible subpaths from first path
        first_path_subpaths = get_subpaths(paths[0], mid)
        found = False
        
        # Check each subpath if it exists in all other paths
        for subpath in first_path_subpaths:
            exists_in_all = True
            
            # Check in each other path
            for path in paths[1:]:
                if not has_subpath(path, subpath):
                    exists_in_all = False
                    break
            
            if exists_in_all:
                found = True
                break
        
        if found:
            left = mid + 1  # Try longer length
        else:
            right = mid - 1  # Try shorter length
            
    return right

"""
How it works (with example):
paths = [[0,1,2,3,4], [2,3,4], [4,0,1,2,3]]

1. Try length = 2:
   - Get subpaths from first path: [0,1], [1,2], [2,3], [3,4]
   - Check each in other paths:
     [2,3] exists in all -> Success!

2. Try length = 3:
   - Get subpaths from first path: [0,1,2], [1,2,3], [2,3,4]
   - Check each in other paths:
     None exist in all -> Fail!

3. Return length 2 as answer

Advantages of this approach:
1. More intuitive and easier to understand
2. Code is simpler and more maintainable
3. Easier to debug and modify
4. No complex hash calculations

Trade-offs:
1. Slower than rolling hash solution
2. More memory usage for storing subpaths
3. Works well for smaller inputs
"""

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def check_length(length):
            # Get first subpath from first path
            seen = set()
            # Process first path's windows and store only unique ones
            for i in range(len(paths[0]) - length + 1):
                subpath = tuple(paths[0][i:i+length])
                seen.add(subpath)
            
            # Check each other path
            for path in paths[1:]:
                # Current path's valid subpaths
                current_seen = set()
                for i in range(len(path) - length + 1):
                    subpath = tuple(path[i:i+length])
                    if subpath in seen:  # Only add if it existed in previous path
                        current_seen.add(subpath)
                
                seen = current_seen  # Update seen to only keep common subpaths
                if not seen:  # If no common subpaths found, return False early
                    return False
            
            return bool(seen)  # True if any common subpaths remain
        
        # Binary search for the length
        left = 0
        right = min(len(path) for path in paths)
        
        while left <= right:
            mid = (left + right) // 2
            
            if check_length(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
    
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        # Constants for double hashing
        MOD1, MOD2 = 1_000_000_007, 1_000_000_009
        BASE1, BASE2 = 100003, 100019
        
        def check_length(length):
            # Special case
            if length == 0:
                return True
                
            # Hash sets for current path
            hash_set = set()
            first = True
            
            # Process each path
            for path in paths:
                if len(path) < length:
                    return False
                    
                # Current path's hashes
                curr_hashes = set()
                
                # Calculate initial hash for first window
                h1 = h2 = 0
                power1 = pow(BASE1, length - 1, MOD1)
                power2 = pow(BASE2, length - 1, MOD2)
                
                # Compute hash for first window
                for i in range(length):
                    h1 = (h1 * BASE1 + path[i]) % MOD1
                    h2 = (h2 * BASE2 + path[i]) % MOD2
                curr_hashes.add((h1, h2))
                
                # Sliding window for remaining windows
                for i in range(length, len(path)):
                    # Remove first element
                    h1 = (h1 - path[i - length] * power1) % MOD1
                    h2 = (h2 - path[i - length] * power2) % MOD2
                    
                    # Add new element
                    h1 = (h1 * BASE1 + path[i]) % MOD1
                    h2 = (h2 * BASE2 + path[i]) % MOD2
                    
                    curr_hashes.add((h1, h2))
                
                # For first path, initialize hash_set
                if first:
                    hash_set = curr_hashes
                    first = False
                else:
                    # Keep only hashes that exist in both sets
                    hash_set &= curr_hashes
                    
                    # Early termination if no common hashes
                    if not hash_set:
                        return False
            
            return True
            
        # Binary search for the length
        left, right = 0, min(len(p) for p in paths)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if check_length(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result
    

    """
ROLLING HASH EXPLAINED WITH VISUALIZATIONS

What is Hashing?
---------------
Hashing is like creating a unique "fingerprint" for data.
Example: Instead of storing "hello", we store a number like 532 that represents it.

Why Rolling Hash?
---------------
It's a way to quickly compute hashes for sliding windows without recalculating everything.
Like having a window that slides over data, updating the hash efficiently.

Example:
Array: [2, 3, 4, 5]
Window size: 2

Regular way (slow):
Window [2,3] -> Calculate hash from scratch
Window [3,4] -> Calculate hash from scratch
Window [4,5] -> Calculate hash from scratch

Rolling hash way (fast):
Window [2,3] -> Calculate initial hash
Window [3,4] -> Remove 2's contribution, add 4's contribution
Window [4,5] -> Remove 3's contribution, add 5's contribution
"""

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        """
        STEP 1: CONSTANTS EXPLAINED
        --------------------------
        MOD1, MOD2: Large prime numbers to keep hash values in reasonable range
                   Like having two different size buckets to put things in
        BASE1, BASE2: Prime numbers used as base for polynomial hash
                     Like using different counting systems (base-10, base-16)
        """
        MOD1, MOD2 = 1_000_000_007, 1_000_000_009
        BASE1, BASE2 = 100003, 100019
        
        def check_length(length):
            """
            STEP 2: ROLLING HASH VISUALIZATION
            ---------------------------------
            Example: path = [1, 2, 3, 4], length = 2
            
            First window [1,2]:
            hash = 1*BASE^1 + 2*BASE^0
            
            Second window [2,3]:
            Remove 1: subtract (1*BASE^1)
            Multiply by BASE (shift left)
            Add 3
            
            Visual:
            [1, 2], 3, 4  -> hash_1
               [2, 3], 4  -> update hash_1 to hash_2
                  [3, 4]  -> update hash_2 to hash_3
            """
            if length == 0:
                return True
            
            """
            STEP 3: HASH SET EXPLANATION
            ---------------------------
            hash_set: Stores unique hashes we've seen
            first: Marks if we're processing first path
            
            Example:
            paths = [[1,2,3], [2,3,4], [3,4,5]]
            length = 2
            
            Path1 hashes: {hash([1,2]), hash([2,3])}
            Path2 hashes: {hash([2,3]), hash([3,4])}
            Common: {hash([2,3])}
            """
            hash_set = set()
            first = True
            
            for path in paths:
                if len(path) < length:
                    return False
                
                """
                STEP 4: DOUBLE HASHING EXPLAINED
                -------------------------------
                Why two hashes? Reduces chance of collisions!
                
                Example:
                [1,2] and [3,4] might have same hash1
                But very unlikely to have same hash1 AND hash2
                
                Like checking both fingerprint and face recognition
                """
                curr_hashes = set()
                h1 = h2 = 0
                
                """
                STEP 5: POWER CALCULATION
                ------------------------
                power1 = BASE1^(length-1)
                Used to remove first element of window
                
                Example for length=3:
                Number = 1*BASE^2 + 2*BASE^1 + 3*BASE^0
                To remove 1: subtract 1*BASE^2
                """
                power1 = pow(BASE1, length - 1, MOD1)
                power2 = pow(BASE2, length - 1, MOD2)
                
                """
                STEP 6: INITIAL WINDOW HASH
                --------------------------
                Example: [1,2,3], length=2
                First window [1,2]:
                h1 = (1*BASE1 + 2) % MOD1
                
                Visual:
                [1, 2], 3  <- initial window
                """
                for i in range(length):
                    h1 = (h1 * BASE1 + path[i]) % MOD1
                    h2 = (h2 * BASE2 + path[i]) % MOD2
                curr_hashes.add((h1, h2))
                
                """
                STEP 7: SLIDING WINDOW UPDATE
                ----------------------------
                Example: Moving from [1,2] to [2,3]
                1. Remove 1: subtract (1*power1)
                2. Multiply by BASE (shift left)
                3. Add new number 3
                
                Visual:
                [1, 2], 3  -> hash1
                    [2, 3]  -> update to hash2
                """
                for i in range(length, len(path)):
                    # Remove first element of previous window
                    h1 = (h1 - path[i - length] * power1) % MOD1
                    h2 = (h2 - path[i - length] * power2) % MOD2
                    
                    # Add new element
                    h1 = (h1 * BASE1 + path[i]) % MOD1
                    h2 = (h2 * BASE2 + path[i]) % MOD2
                    
                    curr_hashes.add((h1, h2))
                
                """
                STEP 8: HASH SET INTERSECTION
                ----------------------------
                For first path: just store all hashes
                For other paths: keep only hashes that exist in both
                
                Example:
                Path1 hashes: {(1,1), (2,2), (3,3)}
                Path2 hashes: {(2,2), (3,3), (4,4)}
                After intersection: {(2,2), (3,3)}
                """
                if first:
                    hash_set = curr_hashes
                    first = False
                else:
                    hash_set &= curr_hashes
                    if not hash_set:
                        return False
            
            return True
        
        """
        STEP 9: BINARY SEARCH
        --------------------
        Example: paths with lengths [5,6,7]
        Try length 3 -> Success
        Try length 4 -> Success
        Try length 5 -> Fail
        Answer is 4
        
        Visual:
        1 2 3 4 5 6 7 8
            ^     ^
            left  right
        """
        left, right = 0, min(len(p) for p in paths)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check_length(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result