# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# Code
# Testcase
# Test Result
# Test Result
# 150. Evaluate Reverse Polish Notation
# Medium
# Topics
# Companies
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 

# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

1. Brute Force
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == '+':
                        result = a + b
                    elif tokens[i] == '-':
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        result = int(a / b)
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    break
        return int(tokens[0])
Time & Space Complexity
Time complexity: 
O
(
n
2
)
O(n 
2
 )
Space complexity: 
O
(
n
)
O(n)
2. Doubly Linked List
class DoublyLinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLinkedList(tokens[0])
        curr = head

        for i in range(1, len(tokens)):
            curr.next = DoublyLinkedList(tokens[i], prev=curr)
            curr = curr.next

        while head is not None:
            if head.val in "+-*/":
                l = int(head.prev.prev.val)
                r = int(head.prev.val)
                if head.val == '+':
                    res = l + r
                elif head.val == '-':
                    res = l - r
                elif head.val == '*':
                    res = l * r
                else:
                    res = int(l / r)

                head.val = str(res)
                head.prev = head.prev.prev.prev
                if head.prev is not None:
                    head.prev.next = head

            ans = int(head.val)
            head = head.next

        return ans
Time & Space Complexity
Time complexity: 
O
(
n
)
O(n)
Space complexity: 
O
(
n
)
O(n)
3. Recursion
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            
            right = dfs()
            left = dfs()
            
            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)
        
        return dfs()
Time & Space Complexity
Time complexity: 
O
(
n
)
O(n)
Space complexity: 
O
(
n
)
O(n)
4. Stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
Time & Space Complexity
Time complexity: 
O
(
n
)
O(n)
Space complexity: 
O
(
n
)
O(n)

"""
REVERSE POLISH NOTATION EVALUATOR: Comprehensive Analysis
=====================================================

Basic Concept:
RPN (Postfix) eliminates need for parentheses by putting operators after operands.
Example: "3 + 4" in RPN is "3 4 +"

Let's analyze each approach with detailed visualizations:

1. BRUTE FORCE APPROACH
----------------------
Scans array for operators and replaces operations with results.

Example 1: ["2","1","+","3","*"]
Visual Evolution:
Step 1: ["2","1","+","3","*"]
        ^^^^^ Find first operator
Step 2: ["3","3","*"]        # Replace "2","1","+" with result "3"
Step 3: ["9"]                # Replace "3","3","*" with result "9"

Example 2: ["4","13","5","/","+"]
Visual Evolution:
Step 1: ["4","13","5","/","+"]
            ^^^^^^^ First division
Step 2: ["4","2","+"]       # 13/5 = 2 (integer division)
Step 3: ["6"]               # 4+2 = 6
"""

class BruteForceRPN:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Example walkthrough for ["2","1","+","3","*"]:
        
        1. Initial: tokens = ["2","1","+","3","*"]
        2. Find '+': 
           - a = 2, b = 1
           - result = 3
           - tokens = ["3","3","*"]
        3. Find '*':
           - a = 3, b = 3
           - result = 9
           - tokens = ["9"]
        """
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == '+':
                        result = a + b
                    elif tokens[i] == '-':
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        result = int(a / b)
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    break
        return int(tokens[0])

"""
2. STACK APPROACH (Most Efficient)
--------------------------------
Uses stack to track operands, applies operators when found.

Example 3 Detailed Evolution: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

Stack Evolution:
[10]                    # Push 10
[10,6]                  # Push 6
[10,6,9]               # Push 9
[10,6,9,3]             # Push 3
[10,6,12]              # '+': 9+3=12
[10,6,12,-11]          # Push -11
[10,6,-132]            # '*': 12*-11=-132
[10,0]                 # '/': 6/-132=0
[0]                    # '*': 10*0=0
[0,17]                 # Push 17
[17]                   # '+': 0+17=17
[17,5]                 # Push 5
[22]                   # '+': 17+5=22
"""

def stack_evalRPN(tokens: List[str]) -> int:
    """
    Stack-based solution with visualizations.
    
    Example walkthrough for ["4","13","5","/","+"]:
    
    1. Push 4:   stack = [4]
    2. Push 13:  stack = [4,13]
    3. Push 5:   stack = [4,13,5]
    4. '/':      stack = [4,2]     # 13/5=2
    5. '+':      stack = [6]       # 4+2=6
    """
    stack = []
    for token in tokens:
        if token == "+":
            a, b = stack.pop(), stack.pop()
            stack.append(b + a)
        elif token == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == "*":
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        elif token == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))  # Integer division
        else:
            stack.append(int(token))
    return stack[0]

"""
3. RECURSIVE APPROACH
-------------------
Works backwards from end of expression.

Example Visualization for ["2","1","+","3","*"]:

Call Stack Evolution:
evalRPN(["2","1","+","3","*"])
└── dfs()  # token="*"
    ├── dfs()  # token="3" returns 3
    └── dfs()  # token="+"
        ├── dfs()  # token="1" returns 1
        └── dfs()  # token="2" returns 2
        Returns 2+1=3
    Returns 3*3=9
"""

def recursive_evalRPN(tokens: List[str]) -> int:
    """
    Recursive solution processing tokens from right to left.
    
    For ["4","13","5","/","+"]:
    1. Pop '+': need left and right
       ├── Pop '/': need left and right
       │   ├── Pop '5' returns 5
       │   └── Pop '13' returns 13
       │   Returns 13/5=2
       └── Pop '4' returns 4
       Returns 4+2=6
    """
    def dfs():
        token = tokens.pop()
        if token not in "+-*/":
            return int(token)
            
        right = dfs()  # Get right operand first
        left = dfs()   # Then left operand
        
        if token == '+': return left + right
        if token == '-': return left - right
        if token == '*': return left * right
        return int(left / right)  # token == '/'
    
    return dfs()