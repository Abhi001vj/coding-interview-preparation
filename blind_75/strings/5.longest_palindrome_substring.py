# https://leetcode.com/problems/longest-palindromic-substring/description/
# 5. Longest Palindromic Substring
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letter

# Solution 1: Brute Force (For discussion)
def longestPalindrome_bruteforce(s: str) -> str:
    """
    Time: O(n³)
    Space: O(1)
    Check all possible substrings
    """
    max_len = 0
    max_palindrome = ""
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and len(substr) > max_len:
                max_len = len(substr)
                max_palindrome = substr
                
    return max_palindrome

# Solution 2: Expand Around Center
def longestPalindrome_expand(s: str) -> str:
    """
    Time: O(n²)
    Space: O(1)
    Expand around potential centers
    """
    if not s:
        return ""
        
    start = end = 0
    
    def expand_around_center(left: int, right: int) -> tuple:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    for i in range(len(s)):
        # Odd length palindromes
        l1, r1 = expand_around_center(i, i)
        # Even length palindromes
        l2, r2 = expand_around_center(i, i + 1)
        
        # Update if longer palindrome found
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
            
    return s[start:end + 1]

# Solution 3: Dynamic Programming
def longestPalindrome_dp(s: str) -> str:
    """
    Time: O(n²)
    Space: O(n²)
    Using DP table to store palindrome status
    """
    n = len(s)
    # dp[i][j] means s[i:j+1] is palindrome
    dp = [[False] * n for _ in range(n)]
    max_start = 0
    max_length = 1
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for palindromes of length 2+
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            
            # Check if substring can be palindrome
            if length == 2:
                dp[start][end] = s[start] == s[end]
            else:
                dp[start][end] = (s[start] == s[end] and 
                                 dp[start + 1][end - 1])
            
            # Update max if we found longer palindrome
            if dp[start][end] and length > max_length:
                max_start = start
                max_length = length
                
    return s[max_start:max_start + max_length]

# Solution 4: Manacher's Algorithm (Advanced)
def longestPalindrome_manacher(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    Using Manacher's algorithm
    """
    # Transform string to handle even length
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # p[i] represents palindrome radius at i
    center = right = 0
    max_center = max_len = 0
    
    for i in range(n):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
            
        # Attempt to expand palindrome centered at i
        left = i - (p[i] + 1)
        right_ptr = i + (p[i] + 1)
        
        while left >= 0 and right_ptr < n and t[left] == t[right_ptr]:
            p[i] += 1
            left -= 1
            right_ptr += 1
            
        # If palindrome expands past right boundary
        if i + p[i] > right:
            center = i
            right = i + p[i]
            
        # Update max palindrome if necessary
        if p[i] > max_len:
            max_len = p[i]
            max_center = i
            
    # Extract longest palindrome
    start = (max_center - max_len) // 2
    return s[start:start + max_len]

# Visualization helper
def visualize_palindrome_finding(s: str, method='expand'):
    """
    Visualizes how palindromes are found
    """
    print(f"\nFinding palindromes in: {s}")
    print("=" * 50)
    
    if method == 'expand':
        # Show expansion process
        def show_expansion(center, is_odd=True):
            left = right = center if is_odd else (center, center + 1)
            if not is_odd:
                left, right = left
            print(f"\nExpanding around {'center' if is_odd else 'between'} {center}")
            
            while True:
                current = list(s)
                if left >= 0 and right < len(s):
                    current[left] = f"[{current[left]}]"
                    current[right] = f"[{current[right]}]"
                    print(f"Current window: {''.join(current)}")
                    print(f"Checking: {s[left]} vs {s[right]}")
                    
                    if left >= 0 and right < len(s) and s[left] == s[right]:
                        print("Match! Expanding...")
                        left -= 1
                        right += 1
                    else:
                        print("Mismatch or boundary reached")
                        break
                else:
                    break
            
            return s[left + 1:right]
        
        # Show expansions around each center
        for i in range(len(s)):
            # Odd length
            palindrome1 = show_expansion(i)
            # Even length
            palindrome2 = show_expansion(i, False)
            print(f"Palindromes found: {palindrome1}, {palindrome2}")
    
    elif method == 'dp':
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # Show DP table evolution
        print("\nDP Table Evolution:")
        for length in range(1, n + 1):
            print(f"\nChecking length {length}:")
            for start in range(n - length + 1):
                end = start + length - 1
                
                if length == 1:
                    dp[start][end] = True
                elif length == 2:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = (s[start] == s[end] and 
                                     dp[start + 1][end - 1])
                
                if dp[start][end]:
                    current = list(s)
                    current.insert(start, '[')
                    current.insert(end + 2, ']')
                    print(f"Found palindrome: {''.join(current)}")

# Test cases
test_cases = [
    "babad",
    "cbbd",
    "a",
    "ac",
    "racecar"
]

for test in test_cases:
    print(f"\nTesting string: {test}")
    print("=" * 50)
    results = {
        "Brute Force": longestPalindrome_bruteforce(test),
        "Expand": longestPalindrome_expand(test),
        "DP": longestPalindrome_dp(test),
        "Manacher": longestPalindrome_manacher(test)
    }
    
    print("Results from all methods:")
    for method, result in results.items():
        print(f"{method}: {result}")
    
    # Show detailed visualization for first test case
    if test == test_cases[0]:
        visualize_palindrome_finding(test)