# https://leetcode.com/problems/add-two-numbers/description/
# 2. Add Two Numbers
# Solved
# Medium
# Topics
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

```python
"""
ADD TWO NUMBERS IN LINKED LIST: Complete Analysis
=============================================

Core Patterns:
1. Linked List Traversal
2. Carry Propagation
3. Dummy Head Pattern
4. Two Pointers

Key Insight: Numbers are already in reverse order, simplifying addition
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def iterative_solution(l1: ListNode, l2: ListNode) -> ListNode:
    """
    APPROACH 1: ITERATIVE WITH CARRY
    
    Example: l1 = [2,4,3], l2 = [5,6,4]
    Represents: 342 + 465 = 807
    
    Step-by-step Process:
    1. First digits: 2 + 5 = 7
       Result: [7]
       Carry: 0
    
    2. Second digits: 4 + 6 = 10
       Result: [7,0]
       Carry: 1
    
    3. Third digits: 3 + 4 + 1(carry) = 8
       Result: [7,0,8]
       Carry: 0
    
    Visual Process:
    Step    l1    l2    Sum    Carry    Result
    ----    --    --    ---    -----    ------
    1       2     5     7      0        [7]
    2       4     6     10     1        [7,0]
    3       3     4+1   8      0        [7,0,8]
    """
    dummy = ListNode(0)  # Dummy head for easier insertion
    current = dummy
    carry = 0
    
    # Process while either list has digits or carry exists
    while l1 or l2 or carry:
        # Get values, using 0 if list exhausted
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        # Calculate sum and new carry
        total = x + y + carry
        carry = total // 10
        digit = total % 10
        
        # Create new node with digit
        current.next = ListNode(digit)
        current = current.next
        
        # Move to next digits if available
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy.next

def recursive_solution(l1: ListNode, l2: ListNode) -> ListNode:
    """
    APPROACH 2: RECURSIVE
    
    Example walkthrough: l1 = [9,9,9], l2 = [9,9]
    
    Recursive Call Stack:
    1. add(9,9)   → 8, carry=1
       add(9,9)   → 9, carry=1
       add(9,-)   → 0, carry=1
       add(-,-)   → 1, carry=0
       
    Result building:
    8 → 9 → 0 → 1
    
    Visual Stack:
    Level    l1    l2    Sum    Result Node
    -----    --    --    ---    -----------
    1        9     9     18     8->...
    2        9     9     19     8->9->...
    3        9     -     10     8->9->0->...
    4        -     -     1      8->9->0->1
    """
    def addWithCarry(l1: ListNode, l2: ListNode, carry: int) -> ListNode:
        # Base case
        if not l1 and not l2 and not carry:
            return None
            
        # Get values
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        # Create current node
        node = ListNode(digit)
        
        # Recursively process next digits
        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None
        node.next = addWithCarry(next1, next2, carry)
        
        return node
        
    return addWithCarry(l1, l2, 0)

def optimized_solution(l1: ListNode, l2: ListNode) -> ListNode:
    """
    APPROACH 3: IN-PLACE MODIFICATION
    Reuses nodes from longer list to save space
    
    Example: l1 = [2,4,3], l2 = [5,6,4]
    
    Visual Process:
    1. Compare lengths: len(l1) = len(l2) = 3
    2. Modify l1 in-place:
       [2,4,3] → [7,0,8]
       
    Time: O(max(N,M))
    Space: O(1) excluding output
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        # Calculate sum
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        
        # Update carry and digit
        carry = total // 10
        digit = total % 10
        
        # Reuse node if possible
        if l1:
            l1.val = digit
            current.next = l1
        else:
            current.next = ListNode(digit)
            
        # Move pointers
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy.next

"""
EDGE CASES AND SPECIAL CONDITIONS
------------------