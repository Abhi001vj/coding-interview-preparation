# https://leetcode.com/problems/merge-k-sorted-lists/description/
# 23. Merge k Sorted Lists
# Solved
# Hard
# Topics
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Early exit
        if not lists:
            return None
            
        # Initialize head and heap
        head = tail = ListNode(0)
        heap = []
        
        # Add first nodes to heap
        for i, node in enumerate(lists):
            if node:
                # Use node.val as primary key, i as tiebreaker
                heappush(heap, (node.val, i, node))
        
        # Process nodes until heap is empty
        while heap:
            val, i, node = heappop(heap)
            
            # Add next node from same list if exists
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
                
            # Build result list
            tail.next = node
            tail = tail.next
        
        return head.next