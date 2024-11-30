# https://leetcode.com/problems/min-stack/description/
# 155. Min Stack
# Solved
# Medium
# Topics
# Companies
# Hint
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

1. Brute Force
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())
        
        while len(tmp):
            self.stack.append(tmp.pop())
        
        return mini
Time & Space Complexity
Time complexity: 
O
(
n
)
O(n) for 
g
e
t
M
i
n
(
)
getMin() and 
O
(
1
)
O(1) for other operations.
Space complexity: 
O
(
n
)
O(n) for 
g
e
t
M
i
n
(
)
getMin() and 
O
(
1
)
O(1) for other operations.
2. Two Stacks
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
Time & Space Complexity
Time complexity: 
O
(
1
)
O(1) for all operations.
Space complexity: 
O
(
n
)
O(n)
3. One Stack
class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()
        
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
Time & Space Complexity
Time complexity: 
O
(
1
)
O(1) for all operations.
Space complexity: 
O
(
n
)
O(n)
"""
MINSTACK: One Stack Solution Analysis
===================================

Key Insight:
Instead of storing actual values, we store the difference between current value
and current minimum. This encoding allows us to track both values and minimums
in a single stack.

Visual Example Flow:
------------------
Let's track operations: push(-2), push(0), push(-3)

1. Initial State:
   stack: []
   min: inf

2. Push(-2):
   * First element
   * stack: [0]     # Store 0 as difference
   * min: -2        # Update minimum

3. Push(0):
   * diff = 0 - (-2) = 2
   * stack: [0, 2]  # Store the difference
   * min: -2        # Min doesn't change

4. Push(-3):
   * diff = -3 - (-2) = -1
   * stack: [0, 2, -1]  # Negative diff indicates new minimum
   * min: -3            # Update minimum
"""

class MinStack:
    """
    Implementation storing differences from current minimum.
    """
    def __init__(self):
        """
        Initialize empty stack and minimum value.
        """
        self.min = float('inf')  # Current minimum
        self.stack = []          # Stack storing differences

    def push(self, x: int) -> None:
        """
        Push value onto stack.
        
        Examples:
        1. Push(-2) to empty stack:
           stack: [0], min: -2
        
        2. Push(0) with min=-2:
           diff = 0-(-2) = 2
           stack: [0,2], min: -2
        
        3. Push(-3) with min=-2:
           diff = -3-(-2) = -1
           stack: [0,2,-1], min: -3
        """
        if not self.stack:
            # First element case
            self.stack.append(0)  # Store 0 as difference
            self.min = x         # Set as minimum
        else:
            # Store difference from current minimum
            diff = x - self.min
            self.stack.append(diff)
            if x < self.min:
                # Update minimum if new value is smaller
                self.min = x

    def pop(self) -> None:
        """
        Pop value from stack.
        
        Example:
        Starting state: stack=[0,2,-1], min=-3
        Pop():
        1. Get diff = -1
        2. Since diff < 0, restore previous min:
           min = -3 - (-1) = -2
        Result: stack=[0,2], min=-2
        """
        if not self.stack:
            return
        
        pop = self.stack.pop()
        
        if pop < 0:
            # If popped difference is negative,
            # restore previous minimum
            self.min = self.min - pop

    def top(self) -> int:
        """
        Get top value.
        
        Examples:
        1. stack=[0,2,-1], min=-3, top=-1:
           Since -1 < 0, return min (-3)
        
        2. stack=[0,2], min=-2, top=2:
           Since 2 > 0, return 2 + (-2) = 0
        """
        top = self.stack[-1]
        if top > 0:
            # If difference is positive, add to minimum
            return top + self.min
        else:
            # If difference is negative or zero, current value is minimum
            return self.min

    def getMin(self) -> int:
        """
        Get minimum value.
        
        Example:
        stack=[0,2,-1], min=-3
        Return: -3
        """
        return self.min

"""
Why This Works:
--------------

1. Value Encoding:
   * If x >= min: store (x - min)
   * If x < min: store (x - old_min) and update min
   
2. Value Decoding:
   * If diff >= 0: actual value = diff + min
   * If diff < 0: actual value = min

3. Minimum Tracking:
   * Negative difference indicates we updated minimum
   * When popping negative difference, restore previous minimum

Example Complete Sequence:
------------------------
Operation  | Stack     | Min  | Actual Values
-----------|-----------|------|---------------
push(-2)   | [0]      | -2   | [-2]
push(0)    | [0,2]    | -2   | [-2,0]
push(-3)   | [0,2,-1] | -3   | [-2,0,-3]
pop()      | [0,2]    | -2   | [-2,0]
"""
\
"""
MINSTACK: Complete Solutions Analysis
===================================

Example sequence for all solutions:
Operations: push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()

1. BRUTE FORCE APPROACH
----------------------
Uses single stack but recalculates minimum each time.

Visual State Evolution:
Initial:    stack = []
push(-2):   stack = [-2]
push(0):    stack = [-2, 0]
push(-3):   stack = [-2, 0, -3]
getMin():   stack = []  temp = [-3, 0, -2]  min = -3  restore = [-2, 0, -3]
pop():      stack = [-2, 0]
top():      stack = [-2, 0]      return 0
getMin():   stack = []  temp = [0, -2]      min = -2  restore = [-2, 0]
"""

class MinStackBrute:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        """
        Simply append to stack
        Time: O(1)
        """
        self.stack.append(val)

    def pop(self) -> None:
        """
        Simple pop from stack
        Time: O(1)
        """
        self.stack.pop()

    def top(self) -> int:
        """
        Return top element
        Time: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Need to scan entire stack for minimum
        Time: O(n) - Main inefficiency
        
        Example process for stack = [-2, 0, -3]:
        1. Create temp = []
        2. While scanning:
           [-2, 0, -3] → [-2, 0] → [-2] → []
           temp = [-3] → [-3, 0] → [-3, 0, -2]
        3. While restoring:
           [] → [-2] → [-2, 0] → [-2, 0, -3]
        """
        tmp = []
        mini = self.stack[-1]

        # Empty stack into temp while finding minimum
        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())
        
        # Restore stack
        while len(tmp):
            self.stack.append(tmp.pop())
        
        return mini

"""
2. TWO STACKS APPROACH
---------------------
Maintains two synchronized stacks: one for values, one for minimums.

Visual State Evolution:
Initial:    stack = []         minStack = []
push(-2):   stack = [-2]       minStack = [-2]    min = -2
push(0):    stack = [-2, 0]    minStack = [-2,-2] min = -2
push(-3):   stack = [-2,0,-3]  minStack = [-2,-2,-3] min = -3
getMin():   return -3
pop():      stack = [-2,0]     minStack = [-2,-2]
top():      return 0
getMin():   return -2

Key Insight: minStack[i] always holds minimum for stack[0:i+1]
"""

class MinStackTwo:
    def __init__(self):
        self.stack = []      # Regular stack
        self.minStack = []   # Parallel stack tracking minimums

    def push(self, val: int) -> None:
        """
        Push to both stacks
        Example: push(0) with state:
        stack = [-2], minStack = [-2]
        Result:
        stack = [-2, 0]
        minStack = [-2, -2]  # -2 still minimum
        Time: O(1)
        """
        self.stack.append(val)
        # Update minimum stack with current minimum
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        """
        Pop from both stacks
        Example state:
        stack = [-2, 0, -3]
        minStack = [-2, -2, -3]
        After pop():
        stack = [-2, 0]
        minStack = [-2, -2]
        Time: O(1)
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        """
        Return top of regular stack
        Time: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Return top of minimum stack
        Time: O(1)
        """
        return self.minStack[-1]

"""
3. SINGLE STACK WITH ENCODING (Most Optimal)
-----------------------------------------
Stores differences from minimum, encodes minimum changes in negative values.

Visual State Evolution with encoded values:
Initial:    stack = []         min = inf
push(-2):   stack = [0]        min = -2    # First element case
push(0):    stack = [0, 2]     min = -2    # diff = 0-(-2) = 2
push(-3):   stack = [0,2,-1]   min = -3    # diff = -3-(-2) = -1

Value Decoding Logic:
1. If diff > 0: actual = min + diff
2. If diff <= 0: actual = min

Example: stack = [0,2,-1], min = -3
- First 0: indicates first element
- 2: means value is min + 2 = -2 + 2 = 0
- -1: indicates minimum changed to -3
"""

# [Previous One Stack implementation remains the same]

"""
COMPARISON OF APPROACHES
----------------------

1. Brute Force:
   Pros: Simple implementation, minimal space
   Cons: O(n) for getMin()
   Space: O(n) for stack
   
2. Two Stacks:
   Pros: Simple logic, O(1) operations
   Cons: Uses 2x space
   Space: O(2n) for two stacks
   
3. One Stack with Encoding:
   Pros: Most space-efficient, O(1) operations
   Cons: Complex logic, potential overflow issues
   Space: O(n) for stack

Visual Memory Usage Comparison for n=4 elements:
Brute:    [v1|v2|v3|v4]
TwoStack: [v1|v2|v3|v4][m1|m2|m3|m4]
OneStack: [d1|d2|d3|d4]+min
"""