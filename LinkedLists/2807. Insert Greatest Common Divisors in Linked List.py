
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
# 2807. Insert Greatest Common Divisors in Linked List
# Medium
# Topics
# Companies
# Given the head of a linked list head, in which each node contains an integer value.

# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

# Return the linked list after insertion.

# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

# Example 1:


# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
# There are no more adjacent nodes, so we return the linked list.
# Example 2:


# Input: head = [7]
# Output: [7]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
# There are no pairs of adjacent nodes, so we return the initial linked list.
 

# Constraints:

# The number of nodes in the list is in the range [1, 5000].
# 1 <= Node.val <= 1000

```python
"""
Linked List GCD Insertion Problem - Detailed Solution
=================================================

Problem Breakdown:
---------------
1. Given: A linked list with integer values
2. Task: Insert GCD between every adjacent pair of nodes
3. Return: Modified linked list

Key Concepts:
-----------
- Finding GCD using Euclidean algorithm
- Linked list node insertion
- Traversing and modifying a linked list

Visual Example:
Original List:    18 -> 6 -> 10 -> 3
After Insertion:  18 -> 6 -> 6 -> 2 -> 10 -> 1 -> 3
                      ↑      ↑       ↑      ↑
                    GCD     GCD     GCD    GCD
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Insert GCD nodes between adjacent nodes in a linked list.
        
        Visual process for input [18,6,10,3]:
        
        Step 1: Initial state
        18 -> 6 -> 10 -> 3
        ^
        curr
        
        Step 2: After first iteration
        18 -> 6 -> 6 -> 10 -> 3
             ^
             curr
        
        Step 3: After second iteration
        18 -> 6 -> 6 -> 10 -> 2 -> 3
                  ^
                  curr
        
        Step 4: After final iteration
        18 -> 6 -> 6 -> 10 -> 2 -> 3 -> 1
                       ^
                       curr
        """
        def gcd(a: int, b: int) -> int:
            """
            Calculate GCD using Euclidean algorithm.
            Example: gcd(18, 6)
            18 = 6 * 3 + 0
            Return: 6
            """
            while b:
                a, b = b, a % b
            return a

        # Handle empty list or single node
        if not head or not head.next:
            return head
            
        # Start with first node
        curr = head
        
        # Traverse until second-to-last node
        while curr.next:
            # Get GCD of current and next values
            gcd_value = gcd(curr.val, curr.next.val)
            
            # Create new node with GCD value
            new_node = ListNode(gcd_value)
            
            # Insert new node between current and next
            new_node.next = curr.next
            curr.next = new_node
            
            # Move to next original node (skip the inserted node)
            curr = new_node.next
            
        return head

    def visualize_insertion(self, values: List[int]) -> None:
        """
        Helper function to visualize the insertion process.
        """
        def create_list(nums):
            dummy = ListNode(0)
            curr = dummy
            for num in nums:
                curr.next = ListNode(num)
                curr = curr.next
            return dummy.next
            
        def print_list(node):
            values = []
            while node:
                values.append(str(node.val))
                node = node.next
            print(" -> ".join(values))

        head = create_list(values)
        print("\nOriginal list:")
        print_list(head)
        
        # Process each insertion
        curr = head
        step = 1
        
        while curr and curr.next:
            gcd_val = self.gcd(curr.val, curr.next.val)
            print(f"\nStep {step}: Insert GCD({curr.val}, {curr.next.val}) = {gcd_val}")
            curr = curr.next
            step += 1
        
        print("\nFinal result:")
        print_list(self.insertGreatestCommonDivisors(create_list(values)))

def demonstrate_solution():
    """
    Demonstrate the solution with example cases.
    """
    test_cases = [
        [18, 6, 10, 3],
        [7],
        [12, 8, 4, 2],
        [25, 15, 10, 5]
    ]
    
    solver = Solution()
    
    for values in test_cases:
        print("\n" + "="*50)
        print(f"Testing with values: {values}")
        solver.visualize_insertion(values)

if __name__ == "__main__":
    demonstrate_solution()

"""
Time & Space Complexity Analysis:
------------------------------
Time Complexity: O(n*k)
- n: length of linked list
- k: maximum number of iterations in GCD calculation
- Traverse list once: O(n)
- GCD calculation for each pair: O(k)

Space Complexity: O(n)
- Additional nodes created: n-1 new nodes
- No recursion or additional data structures

Key Implementation Points:
1. GCD Calculation
   - Use Euclidean algorithm for efficiency
   - Handle edge cases (zero, negative numbers)

2. Linked List Manipulation
   - Careful pointer manipulation
   - Maintain original list structure
   - Skip inserted nodes during traversal

3. Edge Cases
   - Empty list
   - Single node
   - Equal adjacent values
"""
```

Let's analyze the key points:

1. **GCD Calculation**:
   - Uses Euclidean algorithm: repeatedly divide larger number by smaller
   - Example: GCD(18,6)
     ```
     18 = 6 * 3 + 0
     GCD = 6
     ```

2. **Node Insertion Process**:
   - For each pair of nodes:
     1. Calculate GCD
     2. Create new node
     3. Update pointers
     4. Skip to next original node

3. **Edge Cases**:
   - Empty list → return null
   - Single node → return unchanged
   - Equal values → GCD is the value itself

Would you like me to:
1. Explain any specific part in more detail?
2. Add more test cases and visualizations?
3. Show alternative approaches?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            gcd = math.gcd(cur.val, prev.val)
            g = ListNode(gcd)
            prev.next = g
            g.next = cur
            prev = cur
            cur = cur.next

        return head

