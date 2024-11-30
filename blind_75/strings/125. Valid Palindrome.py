# https://leetcode.com/problems/valid-palindrome/description/
# 125. Valid Palindrome
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
# Solution 1: Clean and Reverse (Simple but not optimal)
def isPalindrome_reverse(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    Simple approach using string cleaning and reverse
    """
    # Clean string
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Solution 2: Two Pointers (Space Optimal)
def isPalindrome_two_pointers(s: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    Using two pointers to avoid extra space
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

# Solution 3: Optimized Two Pointers with Early Exit
def isPalindrome_optimized(s: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    With early exit conditions and optimizations
    """
    if not s:
        return True
        
    # Early exit for single character
    if len(s) == 1:
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        # Use ord() for faster character checks
        left_char = s[left].lower()
        while left < right and not (left_char.isalnum()):
            left += 1
            left_char = s[left].lower()
            
        right_char = s[right].lower()
        while left < right and not (right_char.isalnum()):
            right -= 1
            right_char = s[right].lower()
            
        if left_char != right_char:
            return False
            
        left += 1
        right -= 1
        
    return True

# Visualization helper
def visualize_palindrome_check(s: str):
    """
    Visualizes the palindrome checking process
    """
    print(f"\nAnalyzing string: '{s}'")
    print("=" * 50)
    
    # Show cleaning process
    print("\nCleaning process:")
    cleaned = ''
    for c in s:
        if c.isalnum():
            cleaned += c.lower()
            print(f"Adding '{c}' -> Current: '{cleaned}'")
    
    print(f"\nCleaned string: '{cleaned}'")
    
    # Show two pointer process
    print("\nTwo pointer comparison:")
    chars = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        # Visualize current state
        current = chars.copy()
        current[left] = f"[{current[left]}]"
        current[right] = f"[{current[right]}]"
        print(f"\nCurrent: {''.join(current)}")
        
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
            print(f"Skipped left to index {left}")
            
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
            print(f"Skipped right to index {right}")
            
        if left >= right:
            break
            
        print(f"Comparing: {s[left].lower()} vs {s[right].lower()}")
        
        if s[left].lower() != s[right].lower():
            print("Mismatch found!")
            return False
        
        left += 1
        right -= 1
    
    return True

# Test cases
test_cases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " ",
    ".,",
    "a.",
    "0P"
]

for test in test_cases:
    print("\nTest case:", test)
    result = visualize_palindrome_check(test)
    print(f"Final result: {result}")