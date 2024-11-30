# https://leetcode.com/problems/palindrome-partitioning-ii/description/
# Code


# Testcase
# Testcase
# Test Result
# 132. Palindrome Partitioning II
# Solved
# Hard
# Topics
# Companies
# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# .

# Return the minimum cuts needed for a palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
# Example 2:

# Input: s = "a"
# Output: 0
# Example 3:

# Input: s = "ab"
# Output: 1
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase English letters only.
"""
COMPREHENSIVE PALINDROME PARTITIONING SOLUTIONS
=============================================

Problem Set:
1. Palindrome Partitioning I: Find all possible palindrome partitions
2. Palindrome Partitioning II: Find minimum cuts needed for palindrome partition

Example string: "aab"
Visual representation:
"aab" can be partitioned as:
1. ["a", "a", "b"]   - 2 cuts
2. ["aa", "b"]       - 1 cut (minimum)

Decision Tree Visualization:
                      "aab"
                    /      \
             "a|ab"        "aab"
            /      \      /     \
       "a|a|b"   "a|ab" "aa|b"  "aab"
         ✓         ✗       ✓      ✗
"""

class PalindromePartitioningSolutions:
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        """
        Helper function to check if substring is palindrome
        Used by all solutions
        Time: O(n), Space: O(1)
        """
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True

    """
    SOLUTION 1: PALINDROME PARTITIONING I
    ===================================
    Task: Find all possible palindrome partitions
    Approach: DFS with backtracking
    Example: 
    Input: "aab"
    Output: [["a","a","b"], ["aa","b"]]
    """
    def partition_I(self, s: str) -> list[list[str]]:
        res, part = [], []
        
        def dfs(start: int, end: int) -> None:
            """
            DFS helper for finding all partitions
            start: starting index for current partition
            end: ending index being considered
            """
            # Base case: reached end of string
            if end >= len(s):
                if start == end:  # Valid partition found
                    res.append(part.copy())
                return
            
            # Case 1: If current substring is palindrome, try including it
            if self.isPalindrome(s, start, end):
                part.append(s[start:end + 1])
                dfs(end + 1, end + 1)
                part.pop()  # Backtrack
            
            # Case 2: Try extending current substring
            dfs(start, end + 1)
        
        dfs(0, 0)
        return res

    """
    SOLUTION 2: PALINDROME PARTITIONING II (DFS + Memo)
    ===============================================
    Task: Find minimum cuts needed for palindrome partition
    Approach: DFS with memoization
    Example:
    Input: "aab"
    Output: 1
    """
    def minCut_dfs(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n  # Memoization array
        
        def dfs(start: int) -> int:
            """
            Returns minimum cuts needed for s[start:]
            Example trace for "aab":
            1. start=0: min(1 + dfs(1), 1 + dfs(2))
            2. start=1: min(1 + dfs(2))
            3. start=2: 0
            """
            if start >= n:
                return -1
            
            if dp[start] != -1:
                return dp[start]
            
            min_cuts = n - start - 1  # Worst case
            
            for end in range(start, n):
                if self.isPalindrome(s, start, end):
                    cuts = 1 + dfs(end + 1)
                    min_cuts = min(min_cuts, cuts)
            
            dp[start] = min_cuts
            return min_cuts
        
        return dfs(0)

    """
    SOLUTION 3: PALINDROME PARTITIONING II (DP)
    =======================================
    Task: Find minimum cuts needed (optimized)
    Approach: Dynamic Programming with palindrome expansion
    Example:
    Input: "aab"
    Output: 1
    """
    def minCut_dp(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n)]  # dp[i] = min cuts for s[0:i+1]
        
        def expand_palindrome(left: int, right: int) -> None:
            """
            Expands around center and updates dp array
            Example for "aab":
            1. Expand around 'a': dp[0] = 0
            2. Expand around "aa": dp[1] = 0
            3. Consider 'b': dp[2] = min(dp[2], dp[1] + 1) = 1
            """
            while left >= 0 and right < n and s[left] == s[right]:
                # If palindrome starts from beginning, no cuts needed
                if left == 0:
                    dp[right] = 0
                else:
                    # Minimum between current value and cuts needed for s[0:left-1] + 1
                    dp[right] = min(dp[right], dp[left-1] + 1)
                left -= 1
                right += 1
        
        # Try all possible centers
        for i in range(n):
            expand_palindrome(i, i)  # Odd length palindromes
            expand_palindrome(i, i+1)  # Even length palindromes
        
        return dp[n-1]

"""
COMPLEXITY ANALYSIS
==================

Palindrome Partitioning I:
- Time: O(N * 2^N) - for each position, we have two choices
- Space: O(N) - recursion depth

Palindrome Partitioning II (DFS):
- Time: O(N^2) with memoization
- Space: O(N) for memoization array and recursion

Palindrome Partitioning II (DP):
- Time: O(N^2) - expanding around each center
- Space: O(N) for dp array

OPTIMIZATION TECHNIQUES
=====================

1. Character Count Pruning:
   - Check if required characters exist before processing

2. Palindrome Precomputation:
   - Can precompute palindrome information for substrings

3. Early Termination:
   - Stop when impossible to improve current minimum

4. Two-End Processing:
   - Can process string from both ends in some cases
"""

# Test cases
def test_solutions():
    solver = PalindromePartitioningSolutions()
    test_cases = [
        "aab",
        "a",
        "ab",
        "aaaa"
    ]
    
    for s in test_cases:
        print(f"\nTest case: {s}")
        print(f"All partitions: {solver.partition_I(s)}")
        print(f"Minimum cuts (DFS): {solver.minCut_dfs(s)}")
        print(f"Minimum cuts (DP): {solver.minCut_dp(s)}")

if __name__ == "__main__":
    test_solutions()