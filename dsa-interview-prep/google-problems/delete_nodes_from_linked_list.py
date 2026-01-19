# LeetCode 3217: Delete Nodes From Linked List Present in Array
# Google-style: Filter blocked content IDs from processing queue

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove all nodes with values in nums from linked list.

        Approach: In-place with dummy node
        1. Convert nums to set for O(1) lookup
        2. Use dummy node to handle head deletion
        3. Traverse and skip nodes to delete

        Time: O(n + m) where n = len(nums), m = list length
        Space: O(n) for the set
        """
        # Step 1: Convert to set for O(1) lookup
        to_delete = set(nums)

        # Step 2: Create dummy node pointing to head
        dummy = ListNode(0)
        dummy.next = head

        # Step 3: Traverse with prev pointer
        prev = dummy

        while prev.next:
            if prev.next.val in to_delete:
                # Skip the node (delete it)
                prev.next = prev.next.next
            else:
                # Keep the node, move prev forward
                prev = prev.next

        return dummy.next


# ============================================================
# VERIFICATION
# ============================================================

# Example 1: nums = [1,2,3], head = [1,2,3,4,5]
#
# to_delete = {1, 2, 3}
#
# dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
#   ↑
#  prev
#
# prev.next = 1, 1 in set? YES → skip
# dummy -> 2 -> 3 -> 4 -> 5 -> None
#   ↑
#  prev
#
# prev.next = 2, 2 in set? YES → skip
# dummy -> 3 -> 4 -> 5 -> None
#   ↑
#  prev
#
# prev.next = 3, 3 in set? YES → skip
# dummy -> 4 -> 5 -> None
#   ↑
#  prev
#
# prev.next = 4, 4 in set? NO → move prev
# dummy -> 4 -> 5 -> None
#          ↑
#         prev
#
# prev.next = 5, 5 in set? NO → move prev
# dummy -> 4 -> 5 -> None
#               ↑
#              prev
#
# prev.next = None → DONE
# Return dummy.next = 4 -> 5 ✓


# Example 2: nums = [1], head = [1,2,1,2,1,2]
#
# to_delete = {1}
#
# dummy -> 1 -> 2 -> 1 -> 2 -> 1 -> 2 -> None
#   ↑
#  prev
#
# 1 in set? YES → skip → dummy -> 2 -> 1 -> 2 -> 1 -> 2
# 2 in set? NO → move prev
# 1 in set? YES → skip → dummy -> 2 -> 2 -> 1 -> 2
# 2 in set? NO → move prev
# 1 in set? YES → skip → dummy -> 2 -> 2 -> 2
# 2 in set? NO → move prev
# None → DONE
# Return [2, 2, 2] ✓


# Example 3: nums = [5], head = [1,2,3,4]
# No node has value 5, all nodes kept
# Return [1, 2, 3, 4] ✓
