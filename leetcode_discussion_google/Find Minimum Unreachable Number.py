"""
Problem: Find Minimum Unreachable Number
Level: Hard

Example Visualization:
Input: [1, 2]

Possible expressions and their values:
1. Single numbers:
   1, 2

2. Two numbers with operations:
   1 + 2 = 3
   2 + 1 = 3
   1 * 2 = 2
   2 * 1 = 2
   2 - 1 = 1
   2 / 1 = 2
   
Therefore: Can make 1, 2, 3
First unreachable positive number: 4

DSA Pattern:
1. Backtracking - Generate all possible expressions
2. Set - Track reachable numbers
3. Expression evaluation with stack
"""
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-10
        
        def solve(nums):
            # Base case
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON
                
            # Try every pair of numbers
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    # Get the pair of numbers
                    a, b = nums[i], nums[j]
                    
                    # Get remaining numbers
                    remaining = nums[:i] + nums[i+1:j] + nums[j+1:]
                    
                    # Try all operations
                    for op in ['+', '-', '*', '/']:
                        # Skip division by zero
                        if op == '/' and abs(b) < EPSILON:
                            continue
                            
                        # Compute result based on operation
                        if op == '+':
                            result = a + b
                        elif op == '-':
                            result = a - b
                        elif op == '*':
                            result = a * b
                        else:  # Division
                            result = a / b
                            
                        # Add result to remaining numbers and recurse
                        if solve(remaining + [result]):
                            return True
                            
                        # Try reverse order for non-commutative operations
                        if op in ['-', '/']:
                            if op == '/' and abs(a) < EPSILON:
                                continue
                            result = b - a if op == '-' else b / a
                            if solve(remaining + [result]):
                                return True
                                
            return False
        
        # Convert to float and start solving
        return solve([float(x) for x in cards])

from itertools import permutations
import math
from typing import List

class Solution:
    def find_min_unreachable(self, nums: List[int]) -> int:
        """
        Find minimum positive number that cannot be formed
        Time: O(n! * 4^(n-1)) - n! permutations, 4 operators for n-1 positions
        Space: O(n! * 4^(n-1)) for storing all possible results
        """
        def evaluate(expr: str) -> float:
            """
            Evaluate mathematical expression using stack
            Time: O(n) where n is length of expression
            Space: O(n) for stack
            """
            def apply_op(ops, vals):
                op = ops.pop()
                b = vals.pop()
                a = vals.pop()
                if op == '+': vals.append(a + b)
                elif op == '-': vals.append(a - b)
                elif op == '*': vals.append(a * b)
                elif op == '/': 
                    if b == 0: vals.append(float('inf'))
                    else: vals.append(a / b)

            precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
            vals = []
            ops = []
            
            i = 0
            while i < len(expr):
                if expr[i].isdigit():
                    num = 0
                    while i < len(expr) and expr[i].isdigit():
                        num = num * 10 + int(expr[i])
                        i += 1
                    vals.append(num)
                    continue
                    
                if expr[i] == '(':
                    ops.append(expr[i])
                elif expr[i] == ')':
                    while ops and ops[-1] != '(':
                        apply_op(ops, vals)
                    ops.pop()  # Remove '('
                else:
                    while (ops and ops[-1] != '(' and 
                           precedence.get(ops[-1], 0) >= precedence.get(expr[i], 0)):
                        apply_op(ops, vals)
                    ops.append(expr[i])
                i += 1
                
            while ops:
                apply_op(ops, vals)
                
            return vals[0]

        def generate_expressions(nums):
            """
            Generate all possible expressions
            Time: O(n! * 4^(n-1))
            Space: O(n) for recursion depth
            """
            possible_values = set()
            operators = ['+', '-', '*', '/']
            
            # Try all permutations of numbers
            for perm in permutations(nums):
                n = len(perm)
                
                # For each permutation, try all operator combinations
                def backtrack(pos, curr_expr):
                    if pos == n:
                        try:
                            result = evaluate(curr_expr)
                            # Only add if result is positive integer
                            if result > 0 and result.is_integer():
                                possible_values.add(int(result))
                        except:
                            pass
                        return
                        
                    # Add current number
                    curr_expr += str(perm[pos])
                    
                    # If not last number, try all operators
                    if pos < n - 1:
                        for op in operators:
                            backtrack(pos + 1, curr_expr + op)
                    else:
                        backtrack(pos + 1, curr_expr)
                
                backtrack(0, "")
            
            return possible_values

        # Generate all possible values
        possible_values = generate_expressions(nums)
        
        # Find first missing positive number
        i = 1
        while i in possible_values:
            i += 1
        return i

# Test cases
def test_solution():
    """
    Test with various scenarios
    """
    sol = Solution()
    
    test_cases = [
        # Base cases
        ([1, 2], 4),
        ([1, 2, 3], 10),
        
        # Single element
        ([5], 1),
        
        # Multiple elements
        ([1, 2, 4], 13),
        
        # Larger numbers
        ([10, 20], 1),
    ]
    
    for nums, expected in test_cases:
        result = sol.find_min_unreachable(nums)
        assert result == expected, f"Failed for {nums}. Got {result}, expected {expected}"

"""
Complexity Analysis:

Time Complexity Breakdown:
1. Number permutations: O(n!)
2. For each permutation:
   - Operator combinations: O(4^(n-1))
   - Expression evaluation: O(n)
Total: O(n! * 4^(n-1) * n)

Space Complexity Breakdown:
1. Result set: O(n! * 4^(n-1))
2. Recursion stack: O(n)
3. Expression evaluation stack: O(n)
Total: O(n! * 4^(n-1))

Edge Cases:
1. Single element array
2. Array with large numbers
3. Array with elements that can form many combinations
4. Division by zero possibilities
5. Floating point results
6. Negative results

Optimizations:
1. Prune expressions that would yield:
   - Negative numbers
   - Non-integer results
2. Cache intermediate results
3. Use bit manipulation for operator combinations
4. Early termination when finding unreachable numbers
"""

"""
24 Game Solution
Input: 4 cards [1-9]
Goal: Make 24 using +,-,*,/ and parentheses

Pattern Recognition:
1. Backtracking/DFS - Try all combinations
2. Mathematical Expression Evaluation
3. State Reduction (4->3->2->1 numbers)

Visual Example for [4,1,8,7]:

Step-by-Step Process:
1. Start with [4,1,8,7]
2. Pick two numbers and operation: (8-4)=4
3. Remaining: [4,7,1]
4. Pick two more: (7-1)=6
5. Final: [4,6]
6. Last operation: 4*6=24

       [4,1,8,7]
           ↓
    (8-4)=[4,7,1]
           ↓
    (7-1)=[4,6]
           ↓
      4*6=24 ✓

Time: O(4! * 4³) = O(96)
Space: O(1) due to bounded input
"""

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-10  # For float comparison
        
        def solve(nums: List[float]) -> bool:
            """
            Recursive solver trying all combinations
            nums: list of remaining numbers
            returns: True if can make 24, False otherwise
            
            Visual State Space Tree:
            Level 1: [a,b,c,d] → 4 numbers
            Level 2: [x,c,d] → 3 numbers (x = operation(a,b))
            Level 3: [y,d] → 2 numbers (y = operation(x,c))
            Level 4: [z] → 1 number (z = operation(y,d))
            """
            if len(nums) == 1:  # Base case
                return abs(nums[0] - 24) < EPSILON
            
            n = len(nums)
            # Try every pair of numbers
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = nums[i], nums[j]
                    
                    # Create remaining numbers list
                    remaining = nums[:i] + nums[i+1:j] + nums[j+1:]
                    
                    """
                    Example remaining array creation:
                    nums = [4,1,8,7], i=0, j=2
                    nums[:i] = []
                    nums[i+1:j] = [1]
                    nums[j+1:] = [7]
                    remaining = [1,7]
                    """
                    
                    # Try all operations
                    for op in ['+', '-', '*', '/']:
                        if op == '+':
                            remaining.append(a + b)
                        elif op == '-':
                            remaining.append(a - b)
                            remaining.append(b - a)  # Try reverse
                        elif op == '*':
                            remaining.append(a * b)
                        elif op == '/' and abs(b) > EPSILON:
                            remaining.append(a / b)
                        if op == '/' and abs(a) > EPSILON:
                            remaining.append(b / a)  # Try reverse
                        
                        """
                        Operation Example:
                        For 8 and 4:
                        8+4 = 12
                        8-4 = 4, 4-8 = -4
                        8*4 = 32
                        8/4 = 2, 4/8 = 0.5
                        """
                            
                        # Recursively solve
                        if solve(remaining):
                            return True
                        
                        # Backtrack by removing results
                        remaining.pop()
                        if op in '-/' and len(remaining) > 0:
                            remaining.pop()
                            
            return False
        
        # Convert to float for division
        return solve([float(x) for x in cards])

"""
Detailed Examples:

1. [4,1,8,7] -> True
   Path to solution:
   - Pick 8,4: 8-4=4
   - Pick 7,1: 7-1=6
   - Pick 4,6: 4*6=24

2. [1,2,1,2] -> False
   Can try all combinations:
   1+2+1+2 = 6
   1*2*1*2 = 4
   etc.
   No combination reaches 24

3. [3,3,8,8] -> True
   8/(3-8/3) = 24

Edge Cases:
1. Division by zero
2. Floating point precision
3. Order of operations
4. Negative intermediate results
5. Duplicate numbers

Optimizations:
1. EPSILON for float comparison
2. Early return when 24 found
3. Skip redundant operations
4. Handle division carefully
"""

# Test cases
def test_24_game():
    s = Solution()
    test_cases = [
        ([4,1,8,7], True),   # Basic case
        ([1,2,1,2], False),  # Impossible case
        ([3,3,8,8], True),   # Complex division
        ([1,1,1,1], False),  # All same numbers
        ([9,9,9,9], False),  # Large numbers
    ]
    
    for cards, expected in test_cases:
        assert s.judgePoint24(cards) == expected