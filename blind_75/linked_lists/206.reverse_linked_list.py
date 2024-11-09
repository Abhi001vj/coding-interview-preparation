# https://leetcode.com/problems/reverse-linked-list/description/
# 206. Reverse Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
PROBLEM IN THE ORIGINAL CODE:

Original Code Issue:
current_node = head
previous_node = None
next_node = head.next  # First issue: head could be None
while current_node:
    current_node.next = previous_node
    previous_node = current_node 
    current_node = current_node.next  # Second issue: Lost reference to next node

The main problems:
1. No check for empty list (head could be None)
2. next_node variable declared but never used
3. Losing the reference to next node before moving to it

Visual example of what's happening:
Initial List: 1 -> 2 -> 3

Step 1:
current = 1
previous = None
Lost reference to 2 when we set current.next = previous

CORRECTED VERSION:
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list
        if not head:
            return None
            
        current_node = head
        previous_node = None
        
        while current_node:
            # Store next node before we change the pointer
            next_node = current_node.next
            
            # Reverse the pointer
            current_node.next = previous_node
            
            # Move previous and current one step forward
            previous_node = current_node
            current_node = next_node
            
        return previous_node

"""
STEP BY STEP VISUALIZATION:
List: 1 -> 2 -> 3 -> None

Initial state:
current = 1
previous = None
next = 2

Step 1:
Save next = 2
1.next = None
previous = 1
current = 2

Visual: None <- 1  2 -> 3 -> None

Step 2:
Save next = 3
2.next = 1
previous = 2
current = 3

Visual: None <- 1 <- 2  3 -> None

Step 3:
Save next = None
3.next = 2
previous = 3
current = None

Final: None <- 1 <- 2 <- 3

ALTERNATIVE RECURSIVE SOLUTION:
"""
class RecursiveSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not head or not head.next:
            return head
            
        # Recursive call
        rest = self.reverseList(head.next)
        
        # Reverse the links
        head.next.next = head
        head.next = None
        
        return rest

"""
WHY THE ORIGINAL CODE FAILED:

1. Missing Edge Cases:
   - Didn't handle empty list
   - Didn't handle single node list

2. Pointer Problem:
   - Lost track of next node
   - Can't traverse forward after reversing pointer

3. Variable Usage:
   - Declared but never used next_node
   - Incorrect update sequence

CORRECT POINTER UPDATE SEQUENCE:
1. Save next node reference
2. Reverse current pointer
3. Move previous pointer
4. Move current pointer

TEST CASES TO VERIFY:
1. Empty list: None -> None
2. Single node: 1 -> 1
3. Two nodes: 1->2 -> 2->1
4. Multiple nodes: 1->2->3 -> 3->2->1
"""