# https://leetcode.com/problems/generate-parentheses/description/
# 22. Generate Parentheses
# Medium
# Topics
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

"""
TIME AND SPACE COMPLEXITY ANALYSIS
---------------------------------

For input n = 3, let's analyze number of states and operations:

Time Complexity: O(4^n / √n)
-----------------------------
1. Number of Valid Strings:
   - This is determined by nth Catalan number: Cn = (1/(n+1)) * (2n choose n)
   - For n=3: C3 = 5 (the 5 valid combinations)
   - General formula: Cn ≈ 4^n / (n^(3/2) * π^(1/2))

2. Operations Per State:
   - Each state requires:
     * Length check: O(1)
     * Two condition checks: O(1)
     * String concatenation: O(1) [amortized]
     * Stack operations: O(1)

3. Total States Generated:
   - Each state can branch into 2 states (add '(' or ')')
   - Depth of tree is 2n (total length of final string)
   - But many branches are pruned by validity conditions
   - Actual number of states is bounded by O(4^n / √n)

Space Complexity: O(n)
---------------------
1. Stack Space:
   - At any time, stack contains partial solutions
   - Maximum stack depth: O(n)
   - Each stack element contains:
     * Current string: O(n)
     * Two integers (open_count, close_count): O(1)

2. Memory Usage Breakdown:
   - Stack storage: O(n) elements
   - Each element has string of max length 2n: O(n)
   - Result list: O(4^n / √n) strings of length O(n)

Example for n=3:
---------------
Stack element size:
- String: up to 6 chars (2*n)
- Two integers: 8 bytes
- Total per element: O(n) bytes

Maximum stack state: [
    ("(", 1, 0),
    ("((", 2, 0),
    ("(((", 3, 0),
    ... etc
] → O(n) elements

Comparison with Other Approaches:
-------------------------------
1. Recursive (without memoization):
   Time: O(2^(2n))
   Space: O(n)

2. Dynamic Programming:
   Time: O(4^n / √n)
   Space: O(n * 4^n / √n)

3. This Iterative Approach:
   Time: O(4^n / √n)
   Space: O(n)

The iterative approach achieves optimal time complexity while maintaining 
linear space complexity, making it more space-efficient than DP.
"""


"""
COMPLETE ITERATION BREAKDOWN WITH CONDITIONS for n=3
-------------------------------------------------

Initial State: 
stack = [("(", 1, 0)]  # (current_str, open_count, close_count)

Step 1: Pop ("(", 1, 0)
Condition Checks:
1. Length check: len("(") = 1 == 2*3? No, continue
2. Can add '('? (open_count < n)
   - open_count = 1 < n = 3? YES
   - Action: Add ("((", 2, 0)
3. Can add ')'? (close_count < open_count)
   - close_count = 0 < open_count = 1? YES
   - Action: Add ("()", 1, 1)
New stack = [("()", 1, 1), ("((", 2, 0)]

Step 2: Pop ("((", 2, 0)  # Right end of stack
Condition Checks:
1. Length check: len("((") = 2 == 2*3? No, continue
2. Can add '('? (open_count < n)
   - open_count = 2 < n = 3? YES
   - Action: Add ("(((", 3, 0)
3. Can add ')'? (close_count < open_count)
   - close_count = 0 < open_count = 2? YES
   - Action: Add ("(()", 2, 1)
New stack = [("(()", 2, 1), ("(((", 3, 0), ("()", 1, 1)]

Step 3: Pop ("(()", 2, 1)
Condition Checks:
1. Length check: len("(()") = 3 == 2*3? No, continue
2. Can add '('? (open_count < n)
   - open_count = 2 < n = 3? YES
   - Action: Add ("(()(", 3, 1)
3. Can add ')'? (close_count < open_count)
   - close_count = 1 < open_count = 2? YES
   - Action: Add ("(())", 2, 2)
New stack = [("(())", 2, 2), ("(()(", 3, 1), ("(((", 3, 0), ("()", 1, 1)]

Step 4: Pop ("(())", 2, 2)
Condition Checks:
1. Length check: len("(())") = 4 == 2*3? No, continue
2. Can add '('? (open_count < n)
   - open_count = 2 < n = 3? YES
   - Action: Add ("(())(", 3, 2)
3. Can add ')'? (close_count < open_count)
   - close_count = 2 < open_count = 2? NO
   - Action: None
New stack = [("(())(", 3, 2), ("(()(", 3, 1), ("(((", 3, 0), ("()", 1, 1)]

Example Complete Condition Check for Final String:
String: "((()))"
1. Length check: len("((()))") = 6 == 2*3? YES
   - Action: Add to result list
2. Balance check throughout building:
   - "(" : open=1, close=0 ✓
   - "((" : open=2, close=0 ✓
   - "(((" : open=3, close=0 ✓
   - "((()" : open=3, close=1 ✓
   - "((())" : open=3, close=2 ✓
   - "((()))" : open=3, close=3 ✓

Invalid Cases Examples (Why they're not generated):
1. "())"
   - After "()" state (1,1)
   - Cannot add ')' because close_count(1) = open_count(1)
   
2. "((("
   - After "(((" state (3,0)
   - Cannot add '(' because open_count(3) = n(3)
   - Must add ')'

3. ")("
   - Never generated because we start with "("
   - All strings must start with "("
"""
"""
GENERATE PARENTHESES: Comprehensive Solution Analysis
=================================================

Core Insight:
At each step, we can either add '(' if we have remaining open brackets,
or add ')' if we have more open than closed brackets.

Example Visualization for n=2:
                      ""
                      |
                     "("      [open=1,closed=0]
                   /     \
            "(("         "()"   [open=2,closed=0] | [open=1,closed=1]
           /    \           \
      "(()"    "(()"      "()("  [open=2,closed=1] | [open=2,closed=1] | [open=2,closed=1]
        |         |         |
    "(())"     "(())"    "()()"  [open=2,closed=2] | [open=2,closed=2] | [open=2,closed=2]
"""

def generateParenthesis(n: int) -> List[str]:
    """
    Complete solution with backtracking.
    
    Detailed tracking for n=2:
    1. Start: "", open=0, closed=0
    2. Add '(': "(", open=1, closed=0
       └── Add '(': "((", open=2, closed=0
           └── Add ')': "(()", open=2, closed=1
               └── Add ')': "(())", open=2, closed=2 ✓
       └── Add ')': "()", open=1, closed=1
           └── Add '(': "()(", open=2, closed=1
               └── Add ')': "()()", open=2, closed=2 ✓
    """
    def backtrack(open_count: int, closed_count: int, current: str, result: List[str]) -> None:
        """
        open_count: number of '(' used
        closed_count: number of ')' used
        current: current combination being built
        result: list to store valid combinations
        
        Valid State Conditions:
        1. open_count <= n (can't use more than n open brackets)
        2. closed_count <= open_count (can't close more than we've opened)
        """
        # Base case: valid combination found
        if len(current) == 2 * n:
            result.append(current)
            return
            
        # Can add '(' if we haven't used all n
        if open_count < n:
            backtrack(open_count + 1, closed_count, current + "(", result)
            
        # Can add ')' if we have unclosed brackets
        if closed_count < open_count:
            backtrack(open_count, closed_count + 1, current + ")", result)
    
    result = []
    backtrack(0, 0, "", result)
    return result

"""
Complete Example for n=3:
------------------------

State Space Tree:
                       ""
                       |
                      "("
                    /     \
               "(("        "()"
              /    \       /  \
         "((("   "(()"  "()(" "()"
           |      /  \     |
        "((())" "(()(" "(())"
           |      |
        "((()))" "(()())"  ... and so on

Step by step for "((()))":
1. "" → "(" [open=1,closed=0]
2. "(" → "((" [open=2,closed=0]
3. "((" → "(((" [open=3,closed=0]
4. "(((" → "((())" [open=3,closed=1]
5. "((())" → "((()))" [open=3,closed=2]
Final: "((()))" [open=3,closed=3] ✓

Step by step for "(()())":
1. "" → "(" [open=1,closed=0]
2. "(" → "((" [open=2,closed=0]
3. "((" → "(()" [open=2,closed=1]
4. "(()" → "(()(" [open=3,closed=1]
5. "(()(" → "(()())" [open=3,closed=2]
Final: "(()())" [open=3,closed=3] ✓

Key Properties:
1. At any point: closed_count ≤ open_count
2. Final string length = 2 * n
3. Each valid combination has n open and n closed brackets
"""

def test_parentheses():
    """
    Test cases with visualizations
    """
    test_cases = [
        1,  # Expected: ["()"]
        2,  # Expected: ["(())", "()()"]
        3   # Expected: ["((()))", "(()())", "(())()", "()(())", "()()()"]
    ]
    
    for n in test_cases:
        result = generateParenthesis(n)
        print(f"\nInput n = {n}")
        print(f"Output: {result}")
        print(f"Count: {len(result)}")

if __name__ == "__main__":
    test_parentheses()

"""
Time & Space Complexity:
----------------------
Time: O(4ⁿ/√n) - Catalan number sequence
Space: O(n) for recursion stack

Why this works:
1. Backtracking ensures all valid combinations
2. State tracking prevents invalid combinations
3. Base case ensures correct length
4. Conditions maintain valid parentheses rules
"""


"""
ALTERNATIVE APPROACHES FOR GENERATE PARENTHESES
============================================

1. ITERATIVE STACK APPROACH (More intuitive)
------------------------------------------
Uses a stack to build combinations iteratively.
"""

def generateParenthesesIterative(n: int) -> List[str]:
    """
    Stack-based approach.
    For n=2:
    
    Stack evolution:
    [("(", 1, 0)]  # (string, open, close)
    [("((", 2, 0), ("()", 1, 1)]
    [("(())", 2, 2), ("()(", 2, 1)]
    [("(())", 2, 2), ("()()", 2, 2)]
    """
    if n == 0:
        return []
        
    result = []
    stack = [("(", 1, 0)]  # (current_string, open_count, close_count)
    
    while stack:
        curr, open_count, close_count = stack.pop()
        
        if len(curr) == 2 * n:
            result.append(curr)
            continue
            
        if open_count < n:
            stack.append((curr + "(", open_count + 1, close_count))
        if close_count < open_count:
            stack.append((curr + ")", open_count, close_count + 1))
            
    return result

"""
2. BUILD FROM SMALLER SOLUTIONS (Dynamic Programming)
------------------------------------------------
Builds solutions by combining smaller valid patterns.
"""

def generateParenthesesDP(n: int) -> List[str]:
    """
    DP approach building from smaller solutions.
    
    For n=3, builds from combinations of:
    - () + [n=2 solutions inside]
    - (n=1 solutions) + (n=1 solutions)
    - (n=2 solutions) + ()
    
    Example:
    n=1: ["()"]
    n=2: ["(())", "()()"]
    n=3: combines patterns from n=1 and n=2
    """
    dp = [[] for _ in range(n + 1)]
    dp[0] = [""]  # Base case
    
    for i in range(1, n + 1):
        for j in range(i):
            # Combine inner and outer patterns
            for inside in dp[j]:
                for outside in dp[i - 1 - j]:
                    dp[i].append("(" + inside + ")" + outside)
    
    return dp[n]

"""
3. BINARY STRING APPROACH (Mathematical)
------------------------------------
Generates valid combinations using binary representation.
"""

def generateParenthesesBinary(n: int) -> List[str]:
    """
    Uses binary numbers to generate combinations.
    For n=2:
    Valid pattern must have:
    - Equal number of 1s and 0s
    - Running sum of 1s >= 0s at each point
    
    Example mapping:
    1 -> '('
    0 -> ')'
    """
    def isValid(number: int, n: int) -> bool:
        count = 0
        for i in range(2 * n):
            if number & (1 << i):
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0
    
    def toParentheses(number: int, n: int) -> str:
        return ''.join('(' if number & (1 << i) else ')' 
                      for i in range(2 * n - 1, -1, -1))
    
    result = []
    for i in range(1 << (2 * n)):
        if isValid(i, n):
            result.append(toParentheses(i, n))
    return result

"""
4. COMBINATORIAL APPROACH (Using Catalan Numbers)
---------------------------------------------
Uses mathematical properties of Catalan numbers.
"""

def generateParenthesesCatalan(n: int) -> List[str]:
    """
    Based on Catalan number properties:
    - nth Catalan number = number of valid combinations
    - Uses combinatorial properties to generate patterns
    
    Example for n=2:
    Catalan(2) = 2
    Patterns follow Catalan number properties
    """
    def nextPattern(pattern: str, n: int) -> str:
        # Find rightmost '(' that can be moved
        count = 0
        i = len(pattern) - 1
        while i >= 0:
            if pattern[i] == ')':
                count += 1
            else:
                count -= 1
                if count > 0:
                    break
            i -= 1
            
        if i < 0:
            return ""
            
        # Move '(' and rearrange the rest
        return (pattern[:i] + ")" + "(" * (n - (i + 1)//2) + 
                ")" * (n - (i + count + 2)//2))
    
    if n == 0:
        return []
        
    first = "(" * n + ")" * n
    result = [first]
    pattern = first
    
    while True:
        pattern = nextPattern(pattern, n)
        if not pattern:
            break
        result.append(pattern)
        
    return result

# Test all approaches
def test_all_approaches():
    n = 3
    results = {
        "Iterative": generateParenthesesIterative(n),
        "DP": generateParenthesesDP(n),
        "Binary": generateParenthesesBinary(n),
        "Catalan": generateParenthesesCatalan(n)
    }
    
    for name, result in results.items():
        print(f"\n{name} Approach:")
        print(f"Result: {result}")
        print(f"Count: {len(result)}")


"""
GENERATE PARENTHESES (n=3)
Three distinct approaches with complete visualization
"""

def generateParenthesis_brute_force(n: int) -> List[str]:
    """
    Brute Force Approach: Generate all possible combinations and validate
    
    For n=3 (partial tree showing key branches):
                        ""
            /                       \
          "("                       ")"
      /         \               /         \
    "(("        "()"          ")("        "))"
    /   \      /   \         /   \        /  \
   "(((" "(()" "()(""())"  ")((" ")(*"  "))(" "))*"
   
    * indicates invalid paths (not fully shown)
    
    Complete path for "((()))":
    1. "" -> "(" -> "((" -> "(((" -> "((()"->"((())"->"((()))"
    
    Valid string check process for "((()))":
    c  | open | valid?
    ( ->  1   | yes (open >= 0)
    ( ->  2   | yes (open >= 0)
    ( ->  3   | yes (open >= 0)
    ) ->  2   | yes (open >= 0)
    ) ->  1   | yes (open >= 0)
    ) ->  0   | yes (open = 0)
    """
    res = []
    
    def valid(s: str):
        """
        Validates string by tracking open parentheses count
        Examples for n=3:
        "((()))" -> valid (count goes 1,2,3,2,1,0)
        "())()" -> invalid (count goes 1,0,-1...)
        ")(" -> invalid (count goes -1...)
        """
        open = 0
        for c in s:
            open += 1 if c == '(' else -1
            if open < 0:  # More closing than opening
                return False
        return not open  # Must have equal opening and closing

    def dfs(s: str):
        """
        Generates all possible combinations recursively
        Tree example for first few levels:
        Level 1: ""
        Level 2: "(", ")"
        Level 3: "((", "()", ")(", "))"
        And so on until length 2*n
        """
        if n * 2 == len(s):
            if valid(s):
                res.append(s)
            return
        
        dfs(s + '(')
        dfs(s + ')')
    
    dfs("")
    return res


def generateParenthesis_backtrack(n: int) -> List[str]:
    """
    Backtracking Approach: Build only valid combinations
    
    For n=3, state space tree (openN, closedN):
                       (0,0)""
                         |
                      (1,0)"("
                    /          \
            (2,0)"(("        (1,1)"()"
           /        \           \
    (3,0)"((("   (2,1)"(()"   (2,1)"()("
         |          |            |
    (3,1)"((()"  (2,2)"(())"  (2,2)"()()"
         |                       |
    (3,2)"((()))"         (3,2)"()(())"
    
    Stack evolution for "((()))":
    1. stack=["("]        openN=1, closedN=0
    2. stack=["(", "("]   openN=2, closedN=0
    3. stack=["(", "(", "("] openN=3, closedN=0
    4. stack=["(", "(", "(", ")"] openN=3, closedN=1
    5. stack=["(", "(", "(", ")", ")"] openN=3, closedN=2
    6. stack=["(", "(", "(", ")", ")", ")"] openN=3, closedN=3
    """
    stack = []
    res = []
    
    def backtrack(openN: int, closedN: int):
        """
        openN: count of opening brackets used
        closedN: count of closing brackets used
        
        Valid states maintained by conditions:
        1. openN < n: can add more opening brackets
        2. closedN < openN: can add closing bracket
        
        For n=3, valid sequence example:
        (openN,closedN): (0,0)->(1,0)->(2,0)->(3,0)->
                        (3,1)->(3,2)->(3,3)
        """
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res


def generateParenthesis_dp(n: int) -> List[str]:
    """
    Dynamic Programming Approach: Build from smaller solutions
    
    For n=3, builds solutions using:
    res[0] = [""]
    res[1] = ["()"]
    res[2] = ["(())", "()()"]
    res[3] = combinations of res[0,1,2]
    
    Building process for n=3:
    1. i=0, k-i-1=2: "(" + "" + ")" + ["(())", "()()"]
    2. i=1, k-i-1=1: "(" + "()" + ")" + ["()"]
    3. i=2, k-i-1=0: "(" + ["(())", "()()"] + ")" + ""
    
    Final res[3] combinations formed:
    "((()))"  from "(" + "" + ")" + "(())"
    "(()())"  from "(" + "()" + ")" + "()"
    "(())()"  from "(" + "()" + ")" + "()"
    "()(())"  from "()" + "(" + "" + ")" + "()"
    "()()()"  from "()" + "()" + "()"
    """
    res = [[] for _ in range(n+1)]
    res[0] = [""]
    
    for k in range(n + 1):
        for i in range(k):
            for left in res[i]:
                for right in res[k-i-1]:
                    res[k].append("(" + left + ")" + right)
    
    return res[-1]


```python
"""
1. BRUTE FORCE APPROACH
----------------------
Initial State: res = [], s = ""

Step-by-Step State Evolution:
1. Call dfs("")
   Condition Checks:
   - len("") = 0 == 2*3? NO → Continue
   - Branch 1: dfs("(")
   - Branch 2: dfs(")")

Example for s = "(()"
Valid Check Process:
1. c='(' → open=1 → valid (open >= 0)
2. c='(' → open=2 → valid (open >= 0)
3. c=')' → open=1 → valid (open >= 0)
Final: open=1 → invalid (open ≠ 0)

Complete State Tree for n=2:
                    ""
           /                  \
         "("                  ")"
     /         \          /         \
  "(("         "()"     ")("       "))"
  /   \       /   \     /   \     /   \
"(()" "(())" "()(" "())" ")()" ")((" "))(" ")))"

Condition Tracking at Each Node:
"" →    open=0, valid=true
"(" →   open=1, valid=true
"((" →  open=2, valid=true
"(()" → open=1, valid=true
"(())" → open=0, valid=true, ADD TO RESULT
...

2. BACKTRACKING APPROACH
-----------------------
Initial State:
stack = []
res = []
openN = 0
closedN = 0

Complete State Evolution for n=2:
(openN, closedN, stack)
(0,0,[]) → Initial
(1,0,["("]) → Add "("
(2,0,["(","("]) → Add "("
(2,1,["(","(",")"]) → Add ")"
(2,2,["(","(",")",")"] → Complete "(())"

Condition Checks at Each State:
1. Base Case Check:
   - openN == closedN == n?
   
2. Open Bracket Check:
   - Can add if openN < n
   
3. Close Bracket Check:
   - Can add if closedN < openN

Example Path for "(())":
Step   Action       OpenN   ClosedN   Stack
1.     Start       0       0         []
2.     Add "("     1       0         ["("]
3.     Add "("     2       0         ["(", "("]
4.     Add ")"     2       1         ["(", "(", ")"]
5.     Add ")"     2       2         ["(", "(", ")", ")"]
6.     Complete    2       2         → Add to result

3. DYNAMIC PROGRAMMING APPROACH
-----------------------------
Initial State: res = [[] for _ in range(n+1)]

DP Table Evolution for n=2:
res[0] = [""]
res[1] = ["()"]
res[2] = building...

Building Process for res[2]:
1. i=0, k-i-1=1:
   left="" from res[0]
   right="()" from res[1]
   Add: "(" + "" + ")" + "()" = "()()"

2. i=1, k-i-1=0:
   left="()" from res[1]
   right="" from res[0]
   Add: "(" + "()" + ")" + "" = "(())"

Complete DP Table:
k=0: [""]
k=1: ["()"]
k=2: ["(())", "()()"]
k=3: ["((()))", "(()())", "(())()", "()(())", "()()()"]

State Transition Logic:
For each k:
1. Try all splits (i) from 0 to k
2. Combine lefts and rights with "(left)right"
3. Add all combinations to res[k]
"""

# Implementation details with condition tracking...
```
"""
4. BINARY STRING APPROACH
------------------------
Initial State: result = []

Binary Number to Parentheses Mapping:
1 → '('
0 → ')'

Example for n=2 (complete process):
Binary    Number   Valid?  String   Reason
0000      0       No      "))"     Starts with ')', count < 0
0001      1       No      ")("     Starts with ')', count < 0
0010      2       No      ")()"    Starts with ')', count < 0
0011      3       No      ")("     Starts with ')', count < 0
...
1100      12      Yes     "(())"   Valid balance
1010      10      Yes     "()()"   Valid balance

Validity Check Process Example:
For binary 1100 → "(())"
Pos | Bit | Char | Count | Valid?
0   | 1   | (   | +1    | Yes
1   | 1   | (   | +2    | Yes
2   | 0   | )   | +1    | Yes
3   | 0   | )   | 0     | Yes → Add to result

5. CATALAN NUMBER APPROACH
-------------------------
Initial State:
first = "(" * n + ")" * n
result = [first]

For n=3:
Start: "((()))"

Pattern Evolution:
1. "((()))" → Initial
2. "(()())" → Move first '(' right
3. "(())()" → Move second '(' right
4. "()(())" → Move '(' pair
5. "()()()" → Final pattern

State Tracking for n=2:
Step  Pattern  Action
1    "(())"   Start
2    "()()"   Move first '('
3    Done     No more valid moves

Complete Movement Rules:
1. Find rightmost movable '('
2. Move it right maintaining validity
3. Reset all following brackets
4. Add new pattern to result

6. ITERATIVE STACK (Detailed Flow)
--------------------------------
Initial: stack = [("(", 1, 0)]

Complete Stack Evolution for n=2:
Stack Status                 | Action
[("(", 1, 0)]              | Initial
[("((", 2, 0), ("()", 1, 1)] | After processing "("
[("()", 1, 1), ("(()", 2, 1)] | After "(("
[("(()", 2, 1), ("()(", 2, 1)] | After "()"
[("()(", 2, 1), ("(())", 2, 2)] | After "(()"
[("(())", 2, 2), ("()()", 2, 2)] | Final valid patterns

Detailed Condition Checks:
For state ("((", 2, 0):
1. Length Check:
   - len("((") = 2
   - 2*n = 4
   - Continue building

2. Open Bracket Check:
   - open_count = 2
   - n = 2
   - Cannot add more '('

3. Close Bracket Check:
   - close_count = 0
   - open_count = 2
   - Can add ')'

Example Complete Path: "(())"
Step | Stack Entry | Open | Close | Action
1    | ("(", 1, 0)  | 1    | 0     | Add "("
2    | ("((", 2, 0) | 2    | 0     | Add ")"
3    | ("(()", 2, 1)| 2    | 1     | Add ")"
4    | ("(())", 2, 2)| 2    | 2    | Complete

Memory Usage at Each Step:
1. Stack: O(n) elements
2. Each element: (string [2n], open_count [1], close_count [1])
3. Result list: Growing with valid combinations
"""

def complete_generate_parentheses(n: int) -> List[str]:
    """
    Combining best features of each approach:
    1. Stack-based iteration for space efficiency
    2. State tracking for validity
    3. Early pruning of invalid paths
    4. Optimized string building
    
    State Tracking Example (n=2):
    ("(", 1, 0) → Root state
    ├── ("((", 2, 0) → Add open
    │   └── ("(()", 2, 1) → Add close
    │       └── ("(())", 2, 2) ✓ Complete
    └── ("()", 1, 1) → Add close
        └── ("()(", 2, 1) → Add open
            └── ("()()", 2, 2) ✓ Complete
    """
    if n == 0:
        return []
        
    result = []
    stack = [("(", 1, 0)]  # (str, open, close)
    
    while stack:
        curr, open_count, close_count = stack.pop()
        curr_len = len(curr)
        
        # Complete string check
        if curr_len == 2 * n:
            result.append(curr)
            continue
            
        # Try all valid next moves
        remaining_space = 2 * n - curr_len
        
        # Add close bracket if valid
        if close_count < open_count:
            stack.append((curr + ")", open_count, close_count + 1))
            
        # Add open bracket if space allows
        if open_count < n:
            stack.append((curr + "(", open_count + 1, close_count))
    
    return result

"""
Edge Cases and Special Conditions:
--------------------------------
1. n = 0: Return empty list
2. n = 1: Only "()"
3. n = 2: "(())" and "()()"

Performance Optimizations:
------------------------
1. Stack operations: O(1)
2. String concatenation: O(1) amortized
3. State tracking: Constant space per entry
4. Early pruning: Avoid invalid paths

Complete Time Analysis:
---------------------
T(n) = Number of valid states * Cost per state
     = O(4^n/√n) * O(1)
     = O(4^n/√n)
"""
```
DETAILED COMPLEXITY ANALYSIS FOR EACH APPROACH
============================================

1. BRUTE FORCE APPROACH
----------------------
Time Complexity: O(2^(2n) * n)
- Why 2^(2n)?
  * At each position, we have 2 choices ('(' or ')')
  * Total length is 2n
  * So total combinations = 2^(2n)
- Why * n?
  * For each combination, we need O(n) to validate
  * Validation requires scanning string once

Space Complexity: O(n)
- Recursion stack depth is 2n
- Each recursive call stores a string of max length 2n

2. BACKTRACKING APPROACH
----------------------
Time Complexity: O(4^n/√n)
- This comes from nth Catalan number (Cn)
- Formula: Cn = (1/(n+1)) * (2n choose n)
- Approximation: Cn ≈ 4^n/(n^(3/2) * π^(1/2))

Proof:
1. Catalan number formula:
   Cn = (1/(n+1)) * (2n choose n)
   
2. Using Stirling's approximation:
   n! ≈ √(2πn) * (n/e)^n
   
3. Plugging into binomial:
   (2n choose n) ≈ 4^n/√(πn)
   
4. Therefore:
   Cn ≈ 4^n/(n^(3/2) * π^(1/2))

Space Complexity: O(n)
- Stack depth is n
- Each stack frame uses O(1) space

3. DYNAMIC PROGRAMMING APPROACH
-----------------------------
Time Complexity: O(4^n/√n)
- For each k from 1 to n:
  * We try all splits i from 0 to k
  * For each split, generate all combinations
- Total number of combinations = nth Catalan number

Space Complexity: O(4^n/√n)
- Need to store all combinations
- Each combination has length 2n
- Number of combinations = nth Catalan number

4. BINARY STRING APPROACH
-----------------------
Time Complexity: O(2^(2n) * n)
- Check all binary numbers of length 2n: 2^(2n)
- Each check requires O(n) validation

Space Complexity: O(n)
- Only store current state and result

5. CATALAN NUMBER APPROACH
------------------------
Time Complexity: O(4^n/√n)
- Number of valid patterns = nth Catalan number
- Each pattern requires O(n) to generate

Space Complexity: O(n)
- Store current pattern and result strings

UNDERSTANDING 4^n/√n
------------------
This comes from:
1. Total possible patterns = nth Catalan number
2. Catalan number formula simplification:
   * Cn = (1/(n+1)) * (2n choose n)
   * ≈ 4^n/(n^(3/2) * π^(1/2))
   * ≈ O(4^n/√n) after removing constants

WHY 4^n?
--------
- Consider valid combinations:
  * Length is 2n
  * Each position must be balanced
  * Pattern follows Catalan number
  * 4^n represents upper bound on possibilities

WHY /√n?
--------
- Comes from Stirling's approximation of factorials
- Represents the "reduction factor" from total possibilities
- Not all 4^n patterns are valid
```