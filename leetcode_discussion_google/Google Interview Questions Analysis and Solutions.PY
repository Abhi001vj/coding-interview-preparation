"""
Google Interview Questions Analysis

Question 1: Largest K-digit Number
-----------------------------
Problem: Find largest K-digit number that can be formed from original number preserving order
Input: String S="3582", K=2
Output: "82"

Visualization of the process:
"3582" (K=2)
First digit options:  3,5,8 (need 1 more digit after)
If choose 3: remaining options are 5,8,2
If choose 5: remaining options are 8,2
If choose 8: remaining options are 2  <- This gives largest result

Solution using Monotonic Stack:
"""

def find_largest_k_digits(s: str, k: int) -> str:
    """
    Time: O(n)
    Space: O(k)
    Uses monotonic stack to maintain largest possible sequence
    """
    stack = []
    # n digits remaining to process after current position
    remaining = len(s) - k
    
    for digit in s:
        # While we can still remove digits and current digit is larger
        while remaining > 0 and stack and stack[-1] < digit:
            stack.pop()
            remaining -= 1
        stack.append(digit)
    
    # If we still need to remove digits, remove from end
    while remaining > 0:
        stack.pop()
        remaining -= 1
    
    return ''.join(stack[:k])

"""
Question 2: Digit Sequence Sum
--------------------------
Problem: Find all sequences using digits 1,2 that sum to target
Input: Sum = 4
Output: ["1111", "112", "121", "211", "22"]

Tree visualization for Sum=4:
                     4
            /                \
           3(1)              2(2)
        /        \         /      \
     2(1)        1(2)   0(2)     X
    /    \      /
 1(1)    0(2)  X
 /    \
0(1)   X

Solution with Recursion/Backtracking:
"""

def find_sequences(target: int, max_digit: int = 2) -> list:
    """
    Time: O(1.618^n) for digits [1,2]
    Space: O(n) for recursion stack
    Returns all sequences that sum to target using digits 1 to max_digit
    """
    def backtrack(remaining: int, path: str) -> None:
        if remaining == 0:
            result.append(path)
            return
        if remaining < 0:
            return
            
        for digit in range(1, max_digit + 1):
            backtrack(remaining - digit, path + str(digit))
    
    result = []
    backtrack(target, "")
    return result

"""
Follow-up: Counting sequences with DP
"""

def count_sequences_dp(target: int, max_digit: int = 2) -> int:
    """
    Time: O(n)
    Space: O(n)
    Returns count of sequences summing to target using digits 1 to max_digit
    """
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case
    
    for i in range(1, target + 1):
        for digit in range(1, max_digit + 1):
            if i >= digit:
                dp[i] += dp[i - digit]
    
    return dp[target]

"""
Question 3: Expression Simplification
--------------------------------
Problem: Simplify expression with variables, +/-, and parentheses
Input: "a-(a-b)-c"
Output: "b-c"

Visualization of process:
a-(a-b)-c
Step 1: Map counts: {a: 1-1, b: 1, c: -1}
Step 2: Simplify to non-zero terms: b-c

Solution for basic case:
"""

def simplify_expression(expr: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    Returns simplified expression without nested parentheses
    """
    var_count = {}  # Track coefficient of each variable
    current_sign = 1
    i = 0
    
    while i < len(expr):
        if expr[i].isalpha():
            var_count[expr[i]] = var_count.get(expr[i], 0) + current_sign
        elif expr[i] == '-':
            current_sign = -1
        elif expr[i] == '+':
            current_sign = 1
        elif expr[i] == '(':
            # Find matching parenthesis
            level = 1
            j = i + 1
            while level > 0:
                if expr[j] == '(':
                    level += 1
                elif expr[j] == ')':
                    level -= 1
                j += 1
            # Recursively process inside parentheses
            inner = simplify_expression(expr[i+1:j-1])
            if current_sign == -1:
                # Negate all terms inside
                inner = negate_expression(inner)
            # Process inner result
            var_count = merge_expressions(var_count, parse_expression(inner))
            i = j - 1
        i += 1
    
    # Build result string
    result = []
    for var in sorted(var_count.keys()):
        coef = var_count[var]
        if coef != 0:
            if coef > 0 and result:
                result.append('+')
            if coef == -1:
                result.append('-')
            elif coef != 1:
                result.append(str(coef))
            result.append(var)
    
    return ''.join(result) if result else "0"

"""
Helper functions for nested parentheses case:
"""

def negate_expression(expr: str) -> str:
    """Negate all terms in expression"""
    if not expr:
        return ""
    result = []
    i = 0
    while i < len(expr):
        if expr[i] == '+':
            result.append('-')
        elif expr[i] == '-':
            result.append('+')
        else:
            result.append(expr[i])
        i += 1
    return ''.join(result)

def parse_expression(expr: str) -> dict:
    """Parse expression into variable coefficient map"""
    var_count = {}
    current_sign = 1
    i = 0
    while i < len(expr):
        if expr[i].isalpha():
            var_count[expr[i]] = var_count.get(expr[i], 0) + current_sign
        elif expr[i] == '-':
            current_sign = -1
        elif expr[i] == '+':
            current_sign = 1
        i += 1
    return var_count

def merge_expressions(expr1: dict, expr2: dict) -> dict:
    """Merge two coefficient maps"""
    result = expr1.copy()
    for var, count in expr2.items():
        result[var] = result.get(var, 0) + count
    return result

"""
Time Complexity Analysis:
1. Largest K-digit Number: O(n) time, O(k) space
2. Digit Sequence Sum:
   - Original: O(1.618^n) time [Golden ratio]
   - DP version: O(n) time, O(n) space
3. Expression Simplification:
   - Basic: O(n) time and space
   - Nested parentheses: O(n²) time in worst case

Key Insights:
1. Monotonic stack for maintaining optimal subsequence
2. Tree pruning in sequence generation reduces complexity
3. Variable coefficient tracking for expression simplification
"""