"""
Palindromic Partitioning Problem

Example Visualization:
Input: "aab"
Possible partitions:
a|a|b   -> 2 cuts
aa|b    -> 1 cut

Find minimum cuts needed.

Three Approaches:
1. Recursive (TLE)
2. Memoization
3. Tabulation
"""

class Solution:
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        """
        Check if substring s[i:j+1] is palindrome
        Example:
        s="aab", i=0, j=1 ("aa") -> True
        s="aab", i=0, j=2 ("aab") -> False
        """
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def minCutRecursive(self, s: str) -> int:
        """
        Approach 1: Pure Recursion (TLE)
        Time: O(2^n) - tries all possible cuts
        Space: O(n) recursive stack
        
        Visualization for "aab":
        solve(0)
                       aab
              /        |         \
            a|ab      aa|b      aab
           /   \        |        
         a|b    ab     b
          |
          b
        """
        def solve(index: int) -> int:
            # Base case: end of string
            if index >= len(s):
                return 0
                
            min_cuts = float('inf')
            # Try all possible cuts from index
            for j in range(index, len(s)):
                """
                Example for index=0:
                j=0: check "a" -> palindrome
                j=1: check "aa" -> palindrome
                j=2: check "aab" -> not palindrome
                """
                if self.isPalindrome(s, index, j):
                    cost = 1 + solve(j + 1)
                    min_cuts = min(min_cuts, cost)
                    
            return min_cuts
            
        return solve(0) - 1
    
    def minCutMemo(self, s: str) -> int:
        """
        Approach 2: Memoization
        Time: O(n²) - each position computed once
        Space: O(n) for dp array + recursion stack
        
        Visualization for "aab":
        dp[0] = min cuts needed starting at index 0
        dp[1] = min cuts needed starting at index 1
        dp[2] = min cuts needed starting at index 2
        """
        n = len(s)
        dp = [-1] * n
        
        def solve(index: int) -> int:
            if index >= n:
                return 0
                
            # Return cached result if available
            if dp[index] != -1:
                return dp[index]
                
            min_cuts = float('inf')
            for j in range(index, n):
                if self.isPalindrome(s, index, j):
                    cost = 1 + solve(j + 1)
                    min_cuts = min(min_cuts, cost)
                    
            dp[index] = min_cuts
            return min_cuts
            
        return solve(0) - 1
    
    def minCutTab(self, s: str) -> int:
        """
        Approach 3: Tabulation
        Time: O(n²)
        Space: O(n)
        
        Example: "aab"
        dp[3] = 0  (base case)
        dp[2] = 1  (b|)
        dp[1] = 1  (aa|b)
        dp[0] = 1  (aa|b)
        """
        n = len(s)
        dp = [0] * (n + 1)
        
        # Fill dp array from right to left
        for i in range(n-1, -1, -1):
            min_cuts = float('inf')
            """
            For each position i:
            Try all possible substrings from i to j
            If palindrome, take 1 + dp[j+1]
            """
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    cost = 1 + dp[j + 1]
                    min_cuts = min(min_cuts, cost)
            dp[i] = min_cuts
            
        return dp[0] - 1

# Test cases
def test_palindrome_partition():
    """
    Test cases:
    1. Single cut needed
    2. Multiple cuts needed
    3. No cuts needed (already palindrome)
    4. All different characters
    """
    test_cases = [
        ("aab", 1),     # aa|b
        ("ababc", 3),   # a|b|a|b|c
        ("aaaa", 0),    # Already palindrome
        ("abcd", 3)     # a|b|c|d
    ]
    
    solution = Solution()
    for s, expected in test_cases:
        assert solution.minCutTab(s) == expected
        print(f"String: {s}, Minimum cuts: {expected}")

"""
Time Complexity Analysis:
1. Recursive: O(2^n)
   - Each position can be cut or not cut
   - Creates binary recursion tree

2. Memoization: O(n²)
   - n positions
   - Each position tries up to n cuts
   - Each position computed once

3. Tabulation: O(n²)
   - Same as memoization
   - Eliminates recursion stack

Space Complexity:
1. Recursive: O(n) stack space
2. Memoization: O(n) dp array + O(n) stack
3. Tabulation: O(n) dp array

Edge Cases:
1. Empty string -> 0
2. Single character -> 0
3. All same characters -> 0
4. No palindromes except single chars
5. Already palindrome
"""