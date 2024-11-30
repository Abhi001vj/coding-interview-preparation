# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

"""
APPROACH:
Two Pointer Technique with a dummy node.

WHY DUMMY NODE?
- Handles edge cases (removing first node)
- Simplifies pointer manipulation
- Avoids special case handling

VISUALIZATION:
For input: [1,2,3,4,5], n = 2

Initial:
dummy -> 1 -> 2 -> 3 -> 4 -> 5
fast^
slow^

After moving fast n+1 steps:
dummy -> 1 -> 2 -> 3 -> 4 -> 5
slow^              fast^

Final position:
dummy -> 1 -> 2 -> 3 -> 4 -> 5
             slow^         fast^
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize both pointers at dummy
        fast = slow = dummy
        
        # Move fast pointer n+1 steps ahead
        # +1 because we want slow to be before the node to remove
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next
            
        # Remove nth node
        slow.next = slow.next.next
        
        return dummy.next

"""
STEP BY STEP EXAMPLE:
head = [1,2,3,4,5], n = 2

1. Initial Setup:
   dummy -> 1 -> 2 -> 3 -> 4 -> 5
   f,s^

2. Move fast n+1 (3) steps:
   dummy -> 1 -> 2 -> 3 -> 4 -> 5
   s^               f^

3. Move both until fast hits null:
   dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null
                s^               f^

4. Remove node:
   dummy -> 1 -> 2 -> 3 -> 5

TIME/SPACE COMPLEXITY:
Time: O(N) - single pass
Space: O(1) - constant extra space

EDGE CASES:
1. Single node: [1], n = 1
   - Dummy node handles this
2. Remove first node: [1,2], n = 2
   - Dummy node handles this
3. Remove last node: [1,2], n = 1
   - Works normally
"""

# Alternative Implementation with Length Calculation
class AlternativeSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        # Calculate length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        # Move to node before the one to be deleted
        curr = dummy
        for _ in range(length - n):
            curr = curr.next
            
        # Remove nth node
        curr.next = curr.next.next
        
        return dummy.next

"""
WHY TWO POINTER IS BETTER:

1. Single Pass vs Two Passes:
   Length calculation: O(N)
   + Node removal: O(N)
   = Two passes

   Two Pointer:
   Single pass: O(N)

2. Memory Access Pattern:
   Two Pointer:
   - Sequential access
   - Better cache utilization
   - Fewer pointer updates

3. Code Simplicity:
   - No length calculation
   - No arithmetic
   - More intuitive

COMMON MISTAKES TO AVOID:
1. Forgetting dummy node
2. Wrong number of steps for fast pointer
3. Not handling edge cases
4. Off-by-one errors in pointer movement
"""

"""
APPROACH 1: Stack-based Solution
- Push all nodes to stack
- Pop n times to find target
- Intuitive but uses extra space

VISUALIZATION:
Input: [1,2,3,4,5], n = 2
"""
class StackSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        stack = []
        
        # Push all nodes to stack
        curr = dummy
        while curr:
            stack.append(curr)
            curr = curr.next
            
        # Pop n times
        for _ in range(n):
            stack.pop()
            
        # Top of stack is node before target
        prev = stack[-1]
        prev.next = prev.next.next
        
        return dummy.next

"""
Stack Visualization:
Initial Stack:
[dummy,1,2,3,4,5]
Pop n=2 times:
[dummy,1,2,3]
Remove node:
dummy->1->2->3->5

APPROACH 2: Length Calculation with Forward Skip
- Calculate length first
- Skip to (length-n)th node
- More intuitive but two passes
"""
class LengthSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Visual Process:
        1. Count Length:
        1->2->3->4->5 (length = 5)
        
        2. Calculate target position:
        position = length - n = 3
        
        3. Move to previous node:
        1->2->3->4->5
           ^target-1
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        
        # Calculate length
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        # Move to node before target
        position = length - n
        curr = dummy
        for _ in range(position):
            curr = curr.next
            
        # Remove target node
        curr.next = curr.next.next
        return dummy.next

"""
APPROACH 3: Recursive Solution
- Use recursion to reach end
- Count backwards
- Elegant but uses stack space
"""
class RecursiveSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def recurse(node: Optional[ListNode], n: int) -> tuple[Optional[ListNode], int]:
            """
            Returns: (node, position from end)
            
            Visualization:
            1->2->3->4->5->None
            Recursive calls:
            5: returns (5, 1)
            4: returns (4, 2) <- target
            3: returns (3, 3)
            2: returns (2, 4)
            1: returns (1, 5)
            """
            if not node:
                return None, 0
                
            next_node, position = recurse(node.next, n)
            position += 1
            
            if position == n + 1:
                node.next = node.next.next
            
            return node, position
            
        dummy = ListNode(0)
        dummy.next = head
        recurse(dummy, n)
        return dummy.next

"""
APPROACH 4: Window/Sliding Approach
- Maintain n+1 sized window
- Slide until end
- Single pass, no extra space
"""
class WindowSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Visual Process:
        Input: [1,2,3,4,5], n = 2
        
        Window Movement:
        Step 1: [1,2,3]->4->5
               ^   ^
              prev end
        
        Step 2: [2,3,4]->5
                ^   ^
               prev end
        
        Step 3: [3,4,5]->None
                ^   ^
               prev end
        """
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize window
        window = []
        curr = dummy
        
        # Build initial window
        while len(window) <= n and curr:
            window.append(curr)
            curr = curr.next
            
        # Slide window
        while curr:
            window.pop(0)
            window.append(curr)
            curr = curr.next
            
        # Remove target node
        window[0].next = window[0].next.next
        return dummy.next

"""
COMPARISON OF APPROACHES:

1. Stack Solution:
   Time: O(N)
   Space: O(N)
   Pros: Intuitive
   Cons: Extra space

2. Length Solution:
   Time: O(N)
   Space: O(1)
   Pros: Easy to understand
   Cons: Two passes

3. Recursive Solution:
   Time: O(N)
   Space: O(N) - recursion stack
   Pros: Elegant
   Cons: Stack space

4. Window Solution:
   Time: O(N)
   Space: O(n) - window size
   Pros: Single pass
   Cons: Extra space for window

Memory Access Patterns:
Stack: [..., prev, target, next]
Length: dummy -> ... -> prev -> target -> next
Recursive: Call stack builds up to N depth
Window: Fixed size sliding view
"""


"""
APPROACH:
1. Find middle of list using slow/fast pointers
2. Reverse second half of list
3. Merge two halves alternately

VISUALIZATION:
Input: [1,2,3,4,5]

Step 1: Find Middle
1 -> 2 -> 3 -> 4 -> 5
     s    
          f
(s is at middle)

Step 2: Reverse Second Half
Original: 1 -> 2 -> 3 -> 4 -> 5
After split: 
First half:  1 -> 2 -> 3
Second half: 4 -> 5
After reverse: 
First half:  1 -> 2 -> 3
Second half: 5 -> 4

Step 3: Merge Alternately
Result: 1 -> 5 -> 2 -> 4 -> 3
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find middle using slow/fast pointers
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        # Split the list
        prev.next = None
        
        # Step 2: Reverse second half
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Step 3: Merge lists
        first = head
        second = prev
        
        while second:
            # Save next pointers
            temp1 = first.next
            temp2 = second.next
            
            # Connect nodes
            first.next = second
            second.next = temp1
            
            # Move pointers
            first = temp1
            second = temp2

"""
DETAILED STEP-BY-STEP:

1. Finding Middle:
Initial: 1 -> 2 -> 3 -> 4 -> 5
Step 1: s=1, f=1
Step 2: s=2, f=3
Step 3: s=3, f=5
Result: middle at 3

2. Reversing Second Half:
Before: 3 -> 4 -> 5
Step 1: null <- 3   4 -> 5
Step 2: null <- 3 <- 4   5
Step 3: null <- 3 <- 4 <- 5
Result: 5 -> 4 -> 3

3. Merging:
First half:  1 -> 2 -> 3
Second half: 5 -> 4
Step 1: 1 -> 5 -> 2 -> 4 -> 3

MEMORY MANAGEMENT:
Original pointers:
1 -> 2 -> 3 -> 4 -> 5

During reverse:
1 -> 2 -> 3
5 -> 4

Final pointers:
1 -> 5 -> 2 -> 4 -> 3

TIME/SPACE COMPLEXITY:
Time: O(n) - Three passes through list
Space: O(1) - In-place modifications
"""

# Alternative Solution using Stack
class StackSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Stack approach for better visualization
        Not as space-efficient but easier to understand
        """
        if not head or not head.next:
            return
            
        # Push all nodes to stack
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
            
        # Reorder using stack
        curr = head
        length = len(stack)
        for i in range(length // 2):
            # Save next node
            next_temp = curr.next
            
            # Get last node from stack
            last = stack.pop()
            
            # Connect nodes
            curr.next = last
            last.next = next_temp
            
            # Move to next pair
            curr = next_temp
            
        # Handle final node
        if curr:
            curr.next = None

"""
VISUALIZATION OF STACK APPROACH:
Input: [1,2,3,4,5]

Stack: [1,2,3,4,5]
Step 1: Pop 5, connect after 1
1 -> 5 -> 2 -> 3 -> 4

Step 2: Pop 4, connect after 2
1 -> 5 -> 2 -> 4 -> 3

Step 3: Set last node's next to null
1 -> 5 -> 2 -> 4 -> 3 -> null

EDGE CASES:
1. Empty list
2. Single node
3. Even vs Odd length
4. Two nodes
"""