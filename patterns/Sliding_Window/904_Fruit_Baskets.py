from typing import List
import collections

# FAANG Interview Stage 1: Clarify
# Q: Input? -> "Array of integers (tree types)"
# Q: Baskets? -> "2 baskets, each can hold UNLIMITED fruits of 1 TYPE"
# Translation: "Find longest subarray with at most 2 unique numbers"

# FAANG Interview Stage 2: Plan
# Approach: Sliding Window
# 1. Expand right, add fruit to count.
# 2. While len(count) > 2 (Too many types):
#    Shrink left (remove fruit).
# 3. Update max_len.

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = collections.defaultdict(int)
        left = 0
        max_picked = 0
        
        for right in range(len(fruits)):
            # Add fruit
            basket[fruits[right]] += 1
            
            # While we have more than 2 types
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            max_picked = max(max_picked, right - left + 1)
            
        return max_picked

if __name__ == "__main__":
    solver = Solution()
    print(f"Test 1 ([1,2,1]): {solver.totalFruit([1,2,1])} (Expected: 3)")
    print(f"Test 2 ([0,1,2,2]): {solver.totalFruit([0,1,2,2])} (Expected: 3)")
    print(f"Test 3 ([1,2,3,2,2]): {solver.totalFruit([1,2,3,2,2])} (Expected: 4)")
