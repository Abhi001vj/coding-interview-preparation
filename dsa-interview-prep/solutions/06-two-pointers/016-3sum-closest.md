# 16. 3Sum Closest

**Difficulty:** Medium
**Pattern:** Two Pointers (with Sorting)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers.

**Interview Scenario (The "Approximate Match" Prompt):
"You are building a recommendation engine for a shopping bundle. You have a list of item prices and a target bundle price (e.g., $100). You need to pick exactly three distinct items such that their total price is as close as possible to the target (either slightly above or slightly below is fine, just minimize the absolute difference). How would you do this efficiently?"

**Why this transformation?**
* It frames the problem as an optimization/approximation task.
* It emphasizes "exactly three items" which hints at the $N^3 \to N^2$ optimization.

---

## 2. Clarifying Questions (Phase 1)

1.  **Uniqueness:** "Can I use the same element index multiple times?" (No, distinct indices).
2.  **Multiple Answers:** "What if there are two sums equally close (e.g., target 5, sums 4 and 6)?" (Return either? The problem asks for the *sum*, usually guaranteed unique or any valid one. LeetCode usually guarantees a single answer or just asks for the sum value).
3.  **Input Size:** "What is the range of N?" ($3 \le N \le 1000$). "This suggests $O(N^2)$ is acceptable."

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Sorting + Two Pointers.

**Why not Brute Force?**
Trying all triplets is $O(N^3)$. For $N=1000$, $10^9$ operations is too slow. We need $O(N^2)$.

**The Logic:**
1.  **Sort** the array. This allows us to make directed decisions.
2.  Fix the first number (`nums[i]`).
3.  Now we need to find two other numbers (`nums[left]`, `nums[right]`) such that their sum is closest to `target - nums[i]`.
4.  This reduces the sub-problem to **2Sum Closest**, which can be solved in $O(N)$ using Two Pointers on a sorted array.
    *   If sum < target, we need a larger sum -> `left += 1`
    *   If sum > target, we need a smaller sum -> `right -= 1`
    *   If sum == target, difference is 0, return immediately.

---

## 4. Base Template & Modification

**Standard 3Sum Template:**
```python
nums.sort()
for i in range(n):
    l, r = i + 1, n - 1
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s == target: ...
        elif s < target: l += 1
        else: r -= 1
```

**Modified Logic:**
Instead of looking for exact equality, we track the `closest_sum` found so far by comparing absolute differences: `abs(target - current_sum) < abs(target - closest_sum)`.

---

## 5. Optimal Solution

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            # Optimization: Skip duplicates for i (optional for correctness, good for speed)
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Check if this is the closest we've seen so far
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                # Two Pointers Logic
                if current_sum == target:
                    return current_sum  # Exact match, distance is 0
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N^2)$
    *   Sorting takes $O(N \log N)$.
    *   The outer loop runs $N$ times. The inner `while` loop runs $O(N)$ times. Total $O(N^2)$.
*   **Space Complexity:** $O(1)$ or $O(\log N)$
    *   Depends on the sorting implementation (Python's Timsort is $O(N)$ space, typically $O(\log N)$ or $O(1)$ for C++). We assume $O(1)$ ignoring sort space.

---

## 7. Follow-up & Extensions

**Q: What if we needed 4Sum Closest?**
**A:** Wrap the 3Sum logic in another loop ($O(N^3)$).

**Q: What if the array is immutable and we cannot sort?**
**A:** We would likely need to use a Hash Map approach (like 2Sum) but adapted for "closest", which is hard with Hash Maps (Hash Maps are good for exact matches). Without sorting, $O(N^2)$ is very difficult. We might be forced into $O(N^3)$ or using a balanced BST / Heap to find closest elements, which adds overhead.

```