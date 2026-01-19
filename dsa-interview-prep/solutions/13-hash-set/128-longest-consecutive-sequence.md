# 128. Longest Consecutive Sequence

**Difficulty:** Medium
**Pattern:** Hash Set / Disjoint Set Union (DSU)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in $O(n)$ time.

**Interview Scenario (The "Data Grouping" Prompt):**
"You're processing a large stream of numerical IDs from various systems. These IDs are not necessarily unique or sorted, and they arrive out of order. You need to identify the longest contiguous block of IDs, even if some IDs are missing from the stream (i.e., we are looking for `max(k)` such that `x, x+1, ..., x+k-1` are all present). The constraint is that you need a very efficient solution, ideally linear time, as the stream is massive."

**Why this transformation?**
*   It emphasizes the **$O(n)$ time complexity** constraint, which rules out sorting-based $O(n \log n)$ solutions.
*   It frames the problem as finding a "block" or "range" within a set of numbers, which naturally leads to thinking about presence/absence (Hash Set).

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty Array:** "What if `nums` is empty?" (Return 0).
2.  **Duplicates:** "Are there duplicates in `nums`? How should they be handled?" (Duplicates don't affect the consecutive sequence logic, as we care about the *presence* of a number, not its count. A Hash Set naturally handles this).
3.  **Range of Values:** "Are numbers within a certain range?" (Typically standard integer range).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Hash Set.

**Why not Sorting?**
Sorting takes $O(n \log n)$, which violates the $O(n)$ requirement.

**The Logic (Hash Set):**
1.  Put all numbers into a `HashSet` for $O(1)$ average time lookups.
2.  Iterate through each number `num` in the original array.
3.  For each `num`, check if it's the *start* of a potential consecutive sequence.
    *   A number `num` is the start of a sequence if `num - 1` is *not* present in the `HashSet`.
    *   If `num - 1` *is* present, then `num` is part of a longer sequence starting at `num - 1`, so we can skip `num` for now (it will be processed when we find `num - 1`).
4.  If `num` is the start, then start counting: `current_num = num`, `current_length = 1`.
5.  Increment `current_num` and check if `current_num` is in the `HashSet`. Continue as long as it is, incrementing `current_length`.
6.  Update `max_length` with `current_length`.

This way, each number is checked at most a few times: once to put it into the set, and once as part of an expanding sequence (and potentially a quick `num-1` check). Crucially, the inner `while` loop only runs for elements that are *part* of an unbroken chain. Once an element is part of a sequence, it's 'consumed' for that chain. Each number is visited/checked for sequence expansion at most once.

---

## 4. Base Template & Modification

**Standard Iteration with Hash Set:**
```python
num_set = set(nums)
max_len = 0
for num in nums:
    if num - 1 not in num_set: # Check if start of sequence
        current_num = num
        current_len = 1
        while current_num + 1 in num_set:
            current_num += 1
            current_len += 1
        max_len = max(max_len, current_len)
```

**Modified Logic:** None needed, this is the canonical template for the Hash Set approach.

---

## 5. Optimal Solution

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Step 1: Put all numbers into a hash set for O(1) average time lookups
        num_set = set(nums)
        max_length = 0
        
        # Step 2: Iterate through each number in the original array
        for num in nums:
            # Check if the current number `num` is the potential start of a sequence.
            # A number `num` is a start if `num - 1` is NOT present in the set.
            # If `num - 1` is present, it means `num` is part of a longer sequence
            # starting from `num - 1`, so we don't need to process `num` as a start.
            if (num - 1) not in num_set:
                current_num = num
                current_length = 1
                
                # Extend the sequence upwards as long as consecutive numbers are found
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_length += 1
                    
                # Update the maximum length found so far
                max_length = max(max_length, current_length)
                
        return max_length
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   Adding all elements to a hash set takes $O(N)$ on average.
    *   The outer loop iterates $N$ times.
    *   The crucial part: the inner `while` loop only runs for numbers that are the *start* of a sequence. Each number in `nums` is visited by the inner `while` loop at most once across all iterations of the outer loop. For example, if we have `[1,2,3,4]`, `1` starts the chain and `2,3,4` are visited in the inner loop. When the outer loop reaches `2,3,4`, they are skipped because `num-1` is in the set. Thus, each number is involved in a constant number of operations overall.
*   **Space Complexity:** $O(N)$
    *   To store all numbers in the `num_set`.

---

## 7. Follow-up & Extensions

**Q: What if the numbers are very large, preventing direct hashing (e.g., custom objects)?**
**A:** You'd need a custom hashing function or a `Map` that can handle the custom objects and then apply the same logic.

**Q: Can Disjoint Set Union (DSU) be used?**
**A:** Yes, DSU is another valid $O(N \alpha(N))$ approach (effectively $O(N)$). You iterate through `nums`. For each `num`, if `num+1` or `num-1` exist, union their sets. The size of the largest set would be the answer. This is more complex to implement than the hash set method for this specific problem.
