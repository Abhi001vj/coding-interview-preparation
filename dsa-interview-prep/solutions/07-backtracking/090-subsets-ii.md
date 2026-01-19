# 90. Subsets II

**Difficulty:** Medium
**Pattern:** Backtracking / Recursion (with Duplicates Handling)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

**Interview Scenario (The "Configuration Permutations" Prompt):
"You are developing a feature for a software product where users can select various options or settings from a list. This list might have identical options (e.g., two different versions of 'Dark Mode', or two identical security patches). You need to generate all unique combinations of these settings. For example, if a user can choose from `[A, B, A]`, the unique combinations are `[], [A], [B], [A,A], [A,B], [A,A,B]`. How would you implement this?"

**Why this transformation?**
*   It highlights the key challenge: **handling duplicates** to ensure unique subsets.
*   It relates to a practical scenario where combinations are needed, but redundant combinations are undesirable.

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty Subset:** "Should the empty set `[]` be included?" (Yes, for power set).
2.  **Order of Elements:** "Does the order of elements within a subset matter? e.g., `[1,2]` vs `[2,1]`?" (No, usually subsets are order-agnostic, so we sort the input to help handle duplicates).
3.  **Input Range:** "What are the constraints on `nums` length and values?" ($1 

 N 

 10$, values from -10 to 10. Small `N` suggests exponential time is fine).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Backtracking.

**The Logic (Standard Subsets):**
For each element, we have two choices: either include it in the current subset or not. This naturally leads to a recursive/backtracking approach.

**The Duplicates Problem:**
If `nums = [1, 2, 2]`, and we process the first `2`, we get `[1, 2]`. If we later process the second `2`, we might get another `[1, 2]`. We need to avoid this.

**Solution to Duplicates:**
1.  **Sort** the input array `nums`. This brings identical elements together.
2.  In the backtracking step, when choosing the next element `nums[i]`, if `nums[i]` is the same as `nums[i-1]` (and we are not picking `nums[i-1]` in the current recursive call), then `nums[i]` would produce the exact same subsets as `nums[i-1]` did. So, we **skip** `nums[i]` if `i > start_index` and `nums[i] == nums[i-1]`.

---

## 4. Base Template & Modification

**Standard Backtracking Template:**
```python
def backtrack(start_index, current_subset):
    result.append(list(current_subset)) # Make a copy
    for i from start_index to len(nums) - 1:
        current_subset.add(nums[i]) # or append
        backtrack(i + 1, current_subset)
        current_subset.remove(nums[i]) # or pop
```

**Modified Template (Handling Duplicates):**
```python
def backtrack(start_index, current_subset):
    result.append(list(current_subset))
    for i in range(start_index, len(nums)):
        # Skip duplicates
        if i > start_index and nums[i] == nums[i-1]:
            continue
        
        current_subset.append(nums[i])
        backtrack(i + 1, current_subset)
        current_subset.pop()
```

---

## 5. Optimal Solution

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # Sort to handle duplicates easily
        
        def backtrack(start_index, current_subset):
            # Add the current subset to the result list
            # We append a copy because current_subset will be modified later
            res.append(list(current_subset))
            
            # Iterate from start_index to consider elements
            for i in range(start_index, len(nums)):
                # Skip duplicates:
                # If the current element is the same as the previous one,
                # and we are not considering the first occurrence of this element
                # in the current recursive level (i > start_index),
                # then skipping it avoids duplicate subsets.
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                    
                current_subset.append(nums[i])      # Include nums[i]
                backtrack(i + 1, current_subset)  # Recurse with the next index
                current_subset.pop()                # Backtrack: Remove nums[i]
                
        backtrack(0, []) # Start backtracking from index 0 with an empty subset
        return res

```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N 

 2^N)$
    *   There are $2^N$ possible subsets.
    *   For each subset, converting `current_subset` to a `list` and appending it to `res` takes $O(N)$ time (in the worst case, a subset has $N$ elements).
    *   Sorting takes $O(N 

 
log N)$, which is dominated by $O(N 

 2^N)$.
*   **Space Complexity:** $O(N)$ (for `current_subset` and recursion stack)
    *   The maximum depth of the recursion stack is $N$.
    *   The `current_subset` list can hold up to $N$ elements.
    *   The `res` list stores $2^N$ subsets, so output space is $O(N 

 2^N)$.

---

## 7. Follow-up & Extensions

**Q: What if we needed subsets of a specific size `k`?**
**A:** Add a base case in the `backtrack` function: `if len(current_subset) == k: res.append(list(current_subset)); return`. No need to explore further once `k` elements are chosen.

**Q: What if the elements in `nums` were strings instead of integers?**
**A:** The logic remains the same. Sorting would still work alphabetically. The `list(current_subset)` conversion and append would be identical.

```