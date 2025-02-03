"""
Problem: Find minimum characters to remove to get unique string
Input: String with repeated characters
Output: Count of minimum characters to remove

Examples visualization:
1. "abcbbde"
   a b c b b d e
   Remove "bb" (length 2) -> "abcde"

2. "aaabcdaa"
   a a a b c d a a
   Remove "aaabcda" (length 7) -> "a"

Approach 1: Sliding Window with Count Map
Time: O(n²)
Space: O(n)
"""

def min_remove_for_unique(s: str) -> int:
    """
    Find minimum characters to remove for unique string
    Uses sliding window to try all possible substrings
    
    Visual example for "abcbb":
    Window 1: a|bcbb -> can keep 'a'
    Window 2: ab|cbb -> can keep 'ab'
    Window 3: abc|bb -> can keep 'abc'
    Window 4: abcb|b -> can't keep due to 'b'
    Window 5: abcbb| -> can't keep due to 'b'
    """
    n = len(s)
    min_remove = n  # Worst case: remove all
    
    def is_unique(counts):
        """Check if character counts are all 0 or 1"""
        return all(v <= 1 for v in counts.values())
    
    # Try all possible windows
    for i in range(n):
        for j in range(i+1, n+1):
            # Get substring to potentially remove
            to_remove = s[i:j]
            
            # Check remaining string
            remaining = s[:i] + s[j:]
            counts = {}
            for c in remaining:
                counts[c] = counts.get(c, 0) + 1
                
            # Update minimum if remaining is unique
            if is_unique(counts):
                min_remove = min(min_remove, len(to_remove))
                
    return min_remove

"""
Better Approach: Dynamic Programming
Time: O(n²)
Space: O(n²)
"""
def min_remove_dp(s: str) -> int:
    """
    DP approach to find minimum removals
    dp[i][j] = min removals needed for substring s[i:j+1]
    
    Visual DP table for "abcbb":
      a  b  c  b  b
    a 0  0  0  2  2
    b    0  0  2  2
    c       0  2  2
    b          1  2
    b             1
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Process increasing lengths
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            
            # If first and last char are same
            if s[start] == s[end]:
                # Need to remove one of them if length > 2
                dp[start][end] = dp[start+1][end-1] + (length > 2)
            else:
                # Try removing either first or last
                dp[start][end] = min(
                    1 + dp[start+1][end],  # Remove first
                    1 + dp[start][end-1]   # Remove last
                )
                
    return dp[0][n-1]

# Test cases with detailed comments
def test_min_remove():
    """
    Test cases:
    1. Simple repeats: "abcbb"
    2. Multiple repeats: "aaabcdaa"
    3. All unique: "abc"
    4. All same: "aaaa"
    5. Empty string: ""
    """
    test_cases = [
        ("abcbbde", 2),   # Remove "bb"
        ("aaabcdaa", 7),  # Remove "aaabcda"
        ("abc", 0),       # Already unique
        ("aaaa", 3),      # Keep one 'a'
        ("", 0),          # Empty string
    ]
    
    for s, expected in test_cases:
        assert min_remove_for_unique(s) == expected, f"Failed for {s}"
        assert min_remove_dp(s) == expected, f"DP failed for {s}"

"""
Edge Cases to Consider:
1. Empty string
2. All characters same
3. Already unique string
4. Alternating characters
5. Maximum length string

Optimization Tips:
1. Can use bit manipulation for small alphabets
2. Can prune search space based on current minimum
3. Can cache intermediate results
4. Can use rolling hash for faster string comparison

Time Complexity Analysis:
1. Brute Force: O(n³)
   - Try all substrings: O(n²)
   - Check uniqueness: O(n)
   
2. Sliding Window: O(n²)
   - Windows: O(n²)
   - Character counting: O(1)
   
3. DP Approach: O(n²)
   - Fill DP table: O(n²)
   - Each cell calculation: O(1)
"""