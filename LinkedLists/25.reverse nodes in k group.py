# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# 25. Reverse Nodes in k-Group
# Hard
# Topics
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

```python
"""
REVERSE NODES IN K-GROUP: Complete Analysis
========================================

Key Patterns:
1. Linked List Manipulation
2. Group Processing
3. Two Pointers Technique
4. Sublist Reversal

Visual Process Example:
Input: 1->2->3->4->5, k=2

Step-by-Step Process:
1. Find k groups
2. Reverse each group
3. Connect groups
4. Handle remaining nodes
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group_iterative(head: ListNode, k: int) -> ListNode:
    """
    APPROACH 1: ITERATIVE SOLUTION
    ---------------------------
    Example: [1,2,3,4,5], k=2
    
    Visual Process:
    Initial:     1->2->3->4->5
    
    Step 1: Process first group
    Before:      1->2->3->4->5
    After:       2->1->3->4->5
                 ^  ^
                 group1
    
    Step 2: Process second group
    Before:      2->1->3->4->5
    After:       2->1->4->3->5
                      ^  ^
                      group2
    
    Step 3: Not enough nodes for third group
    Final:       2->1->4->3->5
    
    Time: O(n)
    Space: O(1)
    """
    if not head or k == 1:
        return head
        
    # Count length for group validation
    def getLength(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length
        
    length = getLength(head)
    
    # Dummy node for easier handling of head
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    
    # Process each group
    while length >= k:
        curr = prev_group.next  # First node of current group
        next_group = curr.next  # Second node of current group
        
        # Reverse k nodes
        for i in range(k-1):
            curr.next = next_group.next
            next_group.next = prev_group.next
            prev_group.next = next_group
            next_group = curr.next
            
        prev_group = curr
        length -= k
        
    return dummy.next

def reverse_k_group_recursive(head: ListNode, k: int) -> ListNode:
    """
    APPROACH 2: RECURSIVE SOLUTION
    ---------------------------
    Example: [1,2,3,4,5], k=3
    
    Visual Process:
    Level 1: Check first group (1,2,3)
            Reverse: 3->2->1->recursive(4)
            
    Level 2: Check second group (4,5)
            Not enough nodes, return as is
            
    Reverse Process:
    1->2->3->4->5 (original)
    3->2->1->4->5 (after reversal)
    
    Time: O(n)
    Space: O(n/k) for recursion stack
    """
    # Check if we have k nodes left
    curr = head
    count = 0
    while curr and count < k:
        curr = curr.next
        count += 1
    
    if count < k:
        return head
        
    # Reverse current group
    curr = head
    prev = None
    next_node = None
    count = 0
    
    while count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1
        
    # Connect with rest of the list
    if next_node:
        head.next = reverse_k_group_recursive(next_node, k)
        
    return prev

def reverse_k_group_optimized(head: ListNode, k: int) -> ListNode:
    """
    APPROACH 3: OPTIMIZED ITERATIVE
    ----------------------------
    Example: [1,2,3,4,5,6], k=3
    
    Visual State Tracking:
    Initial: 1->2->3->4->5->6
    
    Group 1:
    Step 1: Mark boundaries
            prev=dummy, start=1, end=3
    Step 2: Reverse
            3->2->1->4->5->6
    Step 3: Update pointers
            dummy->3->2->1->4->5->6
            
    Group 2:
    Step 1: Mark boundaries
            prev=1, start=4, end=6
    Step 2: Reverse
            3->2->1->6->5->4
    
    Time: O(n)
    Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    
    while True:
        # Check for k nodes
        kth = get_kth(prev_group, k)
        if not kth:
            break
            
        # Save pointers
        next_group = kth.next
        curr = prev_group.next
        prev = kth.next
        
        # Reverse group
        while curr != next_group:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # Update connections
        temp = prev_group.next
        prev_group.next = kth
        prev_group = temp
        
    return dummy.next

def get_kth(curr: ListNode, k: int) -> ListNode:
    """
    Helper to find kth node
    Returns None if less than k nodes remain
    """
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

"""
COMPLEXITY ANALYSIS
-----------------
1. Iterative:
   Time: O(n)
   Space: O(1)
   - Single pass through list
   - Constant extra space
   
2. Recursive:
   Time: O(n)
   Space: O(n/k)
   - Single pass through list
   - Recursion stack space
   
3. Optimized:
   Time: O(n)
   Space: O(1)
   - Single pass through list
   - Constant extra space

EDGE CASES
---------
1. Empty list
2. Single node
3. k = 1
4. k = length
5. k > length
6. Non-multiple of k
7. k = 2 vs k > 2

VISUALIZATION OF EDGE CASES
------------------------
1. k=1: Return as is
   1->2->3 = 1->2->3
   
2. k=n: Reverse all
   1->2->3 = 3->2->1
   
3. Non-multiple:
   1->2->3->4->5, k=2
   2->1->4->3->5
"""
```python
"""
DETAILED K-GROUP REVERSE: Solution Analysis
=======================================
Example: head = [1,2,3,4,5], k = 2
"""

def reverseKGroup_recursive(head: ListNode, k: int) -> ListNode:
    """
    APPROACH 1: RECURSIVE SOLUTION
    ---------------------------
    
    Input: 1->2->3->4->5, k=2
    
    Recursion Tree and State Evolution:
    Level 1: First Group [1,2]
            1. Check k nodes exist: Yes
            2. Make recursive call for 3->4->5
            
            Level 2: Second Group [3,4]
                    1. Check k nodes exist: Yes
                    2. Make recursive call for 5
                    
                    Level 3: Last Node [5]
                            1. Check k nodes exist: No
                            2. Return 5 as is
                    
                    3. Reverse [3,4]: 4->3->5
                    
            3. Reverse [1,2]: 2->1->4->3->5
    
    Step by Step for First Group:
    1. Initial:    1->2->rest
    2. Store next: tmp = 2
    3. Point fwd:  1->rest
    4. Move head:  2->1->rest
    
    Visual Process:
    Step 0: 1->2->3->4->5
    Step 1: 2->1->4->3->5 (after all recursion)
    """
    cur = head
    group = 0
    
    # Count k nodes
    while cur and group < k:
        cur = cur.next
        group += 1
        
    if group == k:  # If we have k nodes
        # Recurse on remaining list
        cur = reverseKGroup_recursive(cur, k)
        
        # Reverse current group
        while group > 0:
            tmp = head.next    # Save next
            head.next = cur    # Point to result of recursion
            cur = head        # Move current
            head = tmp        # Move head
            group -= 1
            
        head = cur
    return head

def reverseKGroup_iterative(head: ListNode, k: int) -> ListNode:
    """
    APPROACH 2: ITERATIVE SOLUTION
    ---------------------------
    
    Input: 1->2->3->4->5, k=2
    
    Visual State Evolution:
    
    Initial Setup:
    dummy -> 1->2->3->4->5
    groupPrev = dummy
    
    First Group [1,2]:
    1. Find kth: kth = 2
    2. Save next: groupNext = 3
    3. Reverse:
       Before: dummy->1->2->3->...
       After:  dummy->2->1->3->...
       
    Second Group [3,4]:
    1. Find kth: kth = 4
    2. Save next: groupNext = 5
    3. Reverse:
       Before: dummy->2->1->3->4->5
       After:  dummy->2->1->4->3->5
       
    Final State: 2->1->4->3->5
    
    Detailed Reversal Process:
    Step 1: Initial state
    dummy -> 1->2->3
    prev = 3, curr = 1
    
    Step 2: First iteration
    tmp = 2
    1->3
    prev = 1
    curr = 2
    
    Step 3: Second iteration
    2->1->3
    prev = 2
    curr = 3
    """
    dummy = ListNode(0, head)
    groupPrev = dummy
    
    while True:
        # Find kth node
        kth = getKth(groupPrev, k)
        if not kth:
            break
            
        groupNext = kth.next
        
        # Reverse group
        prev, curr = kth.next, groupPrev.next
        
        # Reversal process
        while curr != groupNext:
            tmp = curr.next    # Save next
            curr.next = prev   # Reverse pointer
            prev = curr       # Move prev
            curr = tmp        # Move curr
            
        # Connect with rest of list
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
        
    return dummy.next

def getKth(curr: ListNode, k: int) -> ListNode:
    """
    Helper function to find kth node
    
    Example: curr->1->2->3->4, k=2
    Step 1: curr = 1, k = 1
    Step 2: curr = 2, k = 0
    Return: node 2
    """
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

"""
COMPLEXITY ANALYSIS
-----------------

Recursive:
1. Time: O(n)
   - Visit each node once
   - Reverse each group once
2. Space: O(n/k)
   - Recursion depth = number of groups
   - Each recursion stores constant space

Iterative:
1. Time: O(n)
   - Visit each node once
   - Reverse each group once
2. Space: O(1)
   - Only use constant extra space
   - No recursion stack

EDGE CASES
---------
1. head = null
2. k = 1
3. single node
4. k = length
5. k > length

DEBUGGING TIPS
------------
1. Track group boundaries carefully
2. Maintain proper connections between groups
3. Handle last group correctly
4. Check k nodes exist before reversing
"""