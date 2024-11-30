# https://leetcode.com/problems/palindromic-substrings/description/
# 647. Palindromic Substrings
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

# Solution 1: Brute Force (For discussion)
def countSubstrings_brute(s: str) -> int:
    """
    Time: O(n³)
    Space: O(1)
    Check all possible substrings
    """
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                count += 1
    return count

# Solution 2: Expand Around Center
def countSubstrings_expand(s: str) -> int:
    """
    Time: O(n²)
    Space: O(1)
    Expand from potential palindrome centers
    """
    count = 0
    
    def expand_around_center(left: int, right: int) -> int:
        local_count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            local_count += 1
            left -= 1
            right += 1
        return local_count
    
    for i in range(len(s)):
        # Odd length palindromes
        count += expand_around_center(i, i)
        # Even length palindromes
        count += expand_around_center(i, i + 1)
    
    return count

# Solution 3: Dynamic Programming
def countSubstrings_dp(s: str) -> int:
    """
    Time: O(n²)
    Space: O(n²)
    Using DP table to store palindrome status
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    
    # Single characters
    for i in range(n):
        dp[i][i] = True
        count += 1
    
    # Check lengths 2 and above
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            
            if length == 2:
                dp[start][end] = s[start] == s[end]
            else:
                dp[start][end] = (s[start] == s[end] and 
                                 dp[start + 1][end - 1])
            
            if dp[start][end]:
                count += 1
    
    return count

# Solution 4: Manacher's Algorithm (Advanced)
def countSubstrings_manacher(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    Using Manacher's algorithm
    """
    # Transform string
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # p[i] = radius of palindrome centered at i
    center = right = 0
    count = 0
    
    for i in range(n):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
        
        # Expand palindrome centered at i
        left = i - (p[i] + 1)
        right_ptr = i + (p[i] + 1)
        
        while left >= 0 and right_ptr < n and t[left] == t[right_ptr]:
            p[i] += 1
            left -= 1
            right_ptr += 1
        
        # Update center and right boundary
        if i + p[i] > right:
            center = i
            right = i + p[i]
        
        # Count palindromes
        # Each radius increase means new palindrome in original string
        count += (p[i] + 1) // 2
    
    return count

# Visualization helper
def visualize_palindrome_counting(s: str):
    """
    Visualizes how palindromes are found and counted
    """
    print(f"\nAnalyzing string: {s}")
    print("=" * 50)
    
    # Track all palindromes found
    palindromes = []
    
    def expand_and_show(center: int, is_odd: bool = True):
        """Shows expansion process and collects palindromes"""
        left = right = center
        if not is_odd:
            right = center + 1
            
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # Visualize current palindrome
            palindrome = s[left:right+1]
            palindromes.append(palindrome)
            
            # Show the expansion
            current = list(s)
            current.insert(left, '[')
            current.insert(right + 2, ']')
            print(f"Found palindrome: {''.join(current)} -> {palindrome}")
            
            left -= 1
            right += 1
    
    print("\nExpanding around centers:")
    for i in range(len(s)):
        print(f"\nPosition {i}:")
        # Odd length
        print(f"Checking odd length from {s[i]}")
        expand_and_show(i)
        
        # Even length
        if i < len(s) - 1:
            print(f"Checking even length from {s[i:i+2]}")
            expand_and_show(i, False)
    
    print("\nAll palindromes found:")
    for i, p in enumerate(palindromes, 1):
        print(f"{i}. '{p}'")
    
    return len(palindromes)

# Test cases
test_cases = [
    "abc",
    "aaa",
    "racecar",
    "bb"
]

for test in test_cases:
    print(f"\nTesting string: {test}")
    print("=" * 50)
    
    results = {
        "Brute Force": countSubstrings_brute(test),
        "Expand": countSubstrings_expand(test),
        "DP": countSubstrings_dp(test),
        "Manacher": countSubstrings_manacher(test)
    }
    
    print("Results from all methods:")
    for method, result in results.items():
        print(f"{method}: {result}")
    
    # Detailed visualization for first test case
    if test == test_cases[0]:
        count = visualize_palindrome_counting(test)
        print(f"\nTotal palindromes found: {count}")