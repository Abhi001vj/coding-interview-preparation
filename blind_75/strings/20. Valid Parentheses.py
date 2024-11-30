# https://leetcode.com/problems/valid-parentheses/description/
# 20. Valid Parentheses
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Solution 1: Simple Stack (Most straightforward)
def isValid_simple(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    Basic approach using stack and direct matching
    """
    stack = []
    
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == '}' and stack[-1] != '{':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            stack.pop()
    
    return len(stack) == 0

# Solution 2: Hash Map Mapping (More elegant)
def isValid_hashmap(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    Using hashmap for cleaner matching logic
    """
    stack = []
    matches = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        if char not in matches:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Solution 3: Stack with Early Exit
def isValid_optimized(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    With early exit conditions and optimizations
    """
    # Early exit conditions
    if len(s) % 2:  # Odd length can't be valid
        return False
    
    if not s:
        return True
        
    if s[0] in ')}]':  # Starts with closing
        return False
        
    stack = []
    matches = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for i, char in enumerate(s):
        if char not in matches:
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1] != matches[char]:
                return False
            stack.pop()
            
        # Early exit: more closing than opening
        if len(stack) > len(s) - i - 1:
            return False
    
    return len(stack) == 0

# Solution 4: String Replacement (For discussion)
def isValid_replacement(s: str) -> bool:
    """
    Time: O(n^2)
    Space: O(n)
    Using string replacement - not efficient but interesting approach
    """
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return s == ''

# Test and Visualization Helper
def visualize_parentheses_matching(s: str):
    """
    Visualizes how the stack changes for each character
    """
    print(f"\nAnalyzing string: {s}")
    print("=" * 50)
    
    stack = []
    matches = {')': '(', '}': '{', ']': '['}
    
    print("Stack changes:")
    print("Initial stack: []")
    
    for i, char in enumerate(s):
        current_string = list(s)
        current_string[i] = f"[{char}]"  # Highlight current char
        print(f"\nProcessing: {''.join(current_string)}")
        
        if char not in matches:
            stack.append(char)
            print(f"Open bracket: Added {char}")
        else:
            if not stack:
                print(f"Error: Found closing {char} with empty stack")
                return False
            if stack[-1] != matches[char]:
                print(f"Error: Mismatch - Expected {matches[char]}, found {stack[-1]}")
                return False
            last = stack.pop()
            print(f"Matched {last} with {char}")
            
        print(f"Current stack: {stack}")
    
    is_valid = len(stack) == 0
    print(f"\nFinal stack: {stack}")
    print(f"Valid: {is_valid}")
    return is_valid

# Test cases
test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "((()))",
    "){",
    "(((("
]

for test in test_cases:
    visualize_parentheses_matching(test)