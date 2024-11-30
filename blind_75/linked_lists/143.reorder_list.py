# https://leetcode.com/problems/reorder-list/description/
# 143. Reorder List
# Solved
# Medium
# Topics
# Companies
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000
"""
ISSUE:
For odd-length lists like [1,2,3,4,5], we're losing the middle node (3)
because of how we're handling the middle split.

VISUALIZATION OF ISSUE:
Input: [1,2,3,4,5]

Current split:
First half:  1->2->None
Second half: 5->4->None  (Lost 3!)

Should be:
First half:  1->2->3->None
Second half: 5->4->None

FIXED SOLUTION:
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Edge cases
        if not head or not head.next:
            return
        
        # Step 1: Find middle (FIXED for odd length)
        slow = fast = head
        
        # Move slow to middle node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split list (slow is at mid point)
        # For [1,2,3,4,5]: slow will be at 3
        second = slow.next  # start of second half
        slow.next = None   # end first half
        
        # Step 2: Reverse second half
        prev = None
        curr = second
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Step 3: Merge lists
        first = head
        second = prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

"""
DETAILED VISUALIZATION FOR [1,2,3,4,5]:

1. Finding Middle:
1->2->3->4->5
     s
         f
slow stops at 3

2. Splitting:
First half:  1->2->3->None
Second half: 4->5->None

3. Reversing Second Half:
First half:  1->2->3->None
Second half: 5->4->None

4. Merging Steps:
Initial:
first:  1->2->3->None
second: 5->4->None

Step 1:
1->5->2->3->None
4->None

Step 2:
1->5->2->4->3->None

COMPARISON OF SPLITS:

Original (Wrong):
Input: [1,2,3,4,5]
Split: [1,2] and [5,4]  (Lost 3)

Fixed:
Input: [1,2,3,4,5]
Split: [1,2,3] and [5,4]  (Keeps 3)

KEY CHANGES:
1. Modified middle finding condition
2. Proper handling of slow pointer
3. Correct split point for odd lengths
"""

# Test function to verify correctness
def test_reorder():
    """
    Test cases:
    1. Odd length: [1,2,3,4,5]
    Expected: [1,5,2,4,3]
    
    2. Even length: [1,2,3,4]
    Expected: [1,4,2,3]
    
    3. Small odd: [1,2,3]
    Expected: [1,3,2]
    """
    def create_linked_list(arr):
        if not arr: return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
    
    def list_to_array(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    
    # Test cases
    test_cases = [
        [1,2,3,4,5],
        [1,2,3,4],
        [1,2,3]
    ]
    
    solution = Solution()
    for test in test_cases:
        head = create_linked_list(test)
        solution.reorderList(head)
        print(f"Input: {test}")
        print(f"Output: {list_to_array(head)}")
        print("---")

"""
Time Complexity: O(n)
Space Complexity: O(1)

EDGE CASES HANDLED:
1. Empty list
2. Single node
3. Two nodes
4. Odd length lists
5. Even length lists
"""

"""
APPROACH 1: Using Stack
Intuitive but uses O(n) space
Great for visualization and understanding

APPROACH 2: Using Deque
Similar to stack but with O(n) space
Easier operations from both ends

APPROACH 3: Array Conversion
Simple to understand but O(n) space
Direct index manipulation
"""

# Approach 1: Stack Solution
class StackSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Visual Process:
        Input: 1->2->3->4->5
        
        Stack:
        [5]
        [4]
        [3]  <- middle (ignore for now)
        [2]
        [1]
        
        Reorder Steps:
        1->2->3->4->5 becomes:
        1->5->2->4->3
        """
        if not head or not head.next:
            return
            
        # Push all nodes to stack
        stack = []
        curr = head
        length = 0
        while curr:
            stack.append(curr)
            curr = curr.next
            length += 1
            
        # Process until middle
        curr = head
        for _ in range(length // 2):
            # Save next node
            next_temp = curr.next
            
            # Get node from stack
            last = stack.pop()
            
            # Connect nodes
            curr.next = last
            last.next = next_temp
            
            # Move to next position
            curr = next_temp
            
        # Handle the end
        if curr:
            curr.next = None
        stack[-1].next = None if stack else None

# Approach 2: Deque Solution
from collections import deque
class DequeSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Visual Process:
        Input: 1->2->3->4->5
        
        Deque:
        front [1,2,3,4,5] back
        
        Steps:
        1. Take front (1)
        2. Take back (5)
        3. Take front (2)
        4. Take back (4)
        5. Middle remains (3)
        """
        if not head or not head.next:
            return
            
        # Convert to deque
        d = deque()
        curr = head.next  # Start from second node
        while curr:
            d.append(curr)
            curr = curr.next
            
        # Reorder
        curr = head
        is_front = False
        while d:
            if is_front:
                curr.next = d.popleft()
            else:
                curr.next = d.pop()
            curr = curr.next
            is_front = not is_front
            
        curr.next = None

# Approach 3: Array Solution
class ArraySolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Visual Process:
        Input: 1->2->3->4->5
        
        Array: [1,2,3,4,5]
        Indices: 0 and n-1, 1 and n-2, etc.
        
        Reorder:
        [1] and [5] -> 1->5
        [2] and [4] -> 1->5->2->4
        [3] remains -> 1->5->2->4->3
        """
        if not head or not head.next:
            return
            
        # Convert to array
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        # Reorder using two pointers
        left, right = 0, len(nodes) - 1
        last = None
        
        while left < right:
            # Save next node for left pointer
            next_left = nodes[left].next
            
            # Connect nodes
            nodes[left].next = nodes[right]
            nodes[right].next = next_left
            
            # Update last node
            last = nodes[right]
            
            # Move pointers
            left += 1
            right -= 1
            
        # Handle middle node for odd length
        if left == right:
            last.next = nodes[left]
            nodes[left].next = None
        else:
            last.next = None

"""
VISUALIZATION OF ALL APPROACHES:

Input: [1,2,3,4,5]

Stack Approach:
Step 1: Stack = [5,4,3,2,1]
Step 2: 1->5
Step 3: 1->5->2->4
Step 4: 1->5->2->4->3

Deque Approach:
Step 1: Deque = [2,3,4,5]
Step 2: 1->5
Step 3: 1->5->2->4
Step 4: 1->5->2->4->3

Array Approach:
Step 1: Array = [1,2,3,4,5]
Step 2: Connect 0 and 4: 1->5
Step 3: Connect 1 and 3: 1->5->2->4
Step 4: Add middle: 1->5->2->4->3

COMPARISON:

Stack:
Pros: Intuitive
Cons: O(n) space
Best for: Understanding the problem

Deque:
Pros: Easy bi-directional ops
Cons: O(n) space
Best for: Cleaner implementation

Array:
Pros: Direct index access
Cons: O(n) space
Best for: Easier visualization

Original (Two Pointer):
Pros: O(1) space
Cons: More complex
Best for: Production code
"""