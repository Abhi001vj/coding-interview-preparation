# 907. Sum of Subarray Minimums

**Difficulty:** Hard
**Pattern:** Monotonic Stack

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an array of integers `arr`, find the sum of `min(b)` for every (contiguous) subarray `b` of `arr`. Since the answer may be large, return the answer modulo $10^9 + 7$.

**Interview Scenario (The "Financial Volatility" Prompt):**
"You are analyzing stock price data. For every possible continuous trading window (subarray of prices), you want to find the lowest price reached during that window. Then, you need to sum up all these lowest prices across *all* possible trading windows. This helps quantify market volatility or identify aggregate minimum price impacts. Due to the large number of subarrays, an efficient approach is critical."

**Why this transformation?**
*   It provides a real-world context for summing minimums across subarrays.
*   It emphasizes the need for efficiency due to the $O(N^2)$ subarrays, requiring an $O(N)$ solution.

---

## 2. Clarifying Questions (Phase 1)

1.  **Contiguous:** "Confirming subarrays must be contiguous?" (Yes).
2.  **Modulo:** "Return modulo $10^9 + 7$?" (Yes, indicates large sums).
3.  **Empty Array:** "What if `arr` is empty?" (Return 0).
4.  **Duplicates:** "What if there are duplicate values? How do they impact minimums?" (Handle with care, usually using strict inequality for one side and non-strict for the other to count uniquely if values are equal).

-----n

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Monotonic Stack.

**Why not Brute Force?**
$O(N^2)$ subarrays. For each, finding minimum is $O(N)$. Total $O(N^3)$. Even finding min for each is $O(1)$ with `min` tracking, total $O(N^2)$. For $N=30,000$, $O(N^2)$ is too slow.

**The Key Insight (Monotonic Stack):**
Instead of iterating through subarrays and finding their minimums, iterate through each number `arr[i]` and figure out how many subarrays have `arr[i]` as their minimum.

For each `arr[i]`, we need to find:
*   `left[i]`: The number of elements to its left that are *strictly greater* than `arr[i]`. (Or, index of first element `j < i` where `arr[j] <= arr[i]`).
*   `right[i]`: The number of elements to its right that are *greater than or equal to* `arr[i]`. (Or, index of first element `j > i` where `arr[j] < arr[i]`).

Then, `arr[i]` will be the minimum in `(left[i] + 1) * (right[i] + 1)` subarrays. The `+1` is for `arr[i]` itself.

**Monotonic Stack for `left[i]` (Previous Less Element):**
*   Maintain a stack of indices in increasing order of `arr[index]` values.
*   When processing `arr[i]`: Pop elements from stack that are `arr[stack.top()] >= arr[i]`. The top of the stack (after popping) is the `Previous Less Element` or PLE. `left[i]` is `i - PLE_index`.
*   Push `i`.

**Monotonic Stack for `right[i]` (Next Less Element):**
*   Similar, but process from right to left, or use a second pass.
*   To handle duplicates and ensure unique counting, for PLE use `arr[j] < arr[i]` and for NLE use `arr[j] <= arr[i]` (or vice versa).

---

## 4. Base Template & Modification

**Standard Monotonic Stack (Next Greater/Smaller):**
```python
stack = []
result_arr = [0] * n
for i in range(n):
    while stack and condition(arr[stack[-1]], arr[i]):
        # Process stack.pop()
    # Push i
```

**Modified Logic:**
Apply twice (or once with careful handling) to calculate `left` and `right` counts for each element.

---

## 5. Optimal Solution

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # `left[i]` stores the count of elements to the left of arr[i] (inclusive)
        # that are greater than arr[i], plus arr[i] itself.
        # This means `arr[i]` is the minimum for `left[i]` subarrays ending at `i`.
        left = [0] * n
        stack = [] # Stores (value, index)
        
        for i in range(n):
            count = 1 # arr[i] itself is 1 subarray
            while stack and stack[-1][0] > arr[i]:
                prev_val, prev_idx = stack.pop()
                count += left[prev_idx] # Add subarrays where prev_val was min and extended
            
            left[i] = count
            stack.append((arr[i], i))
            
        # `right[i]` stores the count of elements to the right of arr[i] (inclusive)
        # that are greater than or equal to arr[i], plus arr[i] itself.
        # This means `arr[i]` is the minimum for `right[i]` subarrays starting at `i`.
        # We need to be careful with duplicates. For example, if arr = [3,1,2,1,3]
        # To avoid double counting when arr[i] == arr[j], ensure `>` for one and `>=` for other
        # Here, `>` for left (PGE/PLE) and `>=` for right (NGE/NLE) for standard approach.
        
        right = [0] * n
        stack = [] # Stores (value, index)
        
        # Process from right to left for `right` counts
        for i in range(n - 1, -1, -1):
            count = 1
            # Use `>=` for right pass to handle duplicates correctly
            # (ensures `arr[i]` takes precedence for minimum if values are equal)
            while stack and stack[-1][0] >= arr[i]: 
                prev_val, prev_idx = stack.pop()
                count += right[prev_idx]
            
            right[i] = count
            stack.append((arr[i], i))
            
        total_sum_of_mins = 0
        for i in range(n):
            # For each element arr[i], it is the minimum in `left[i] * right[i]` subarrays.
            # `left[i]` is the number of subarrays ending at `i` where arr[i] is min.
            # `right[i]` is the number of subarrays starting at `i` where arr[i] is min.
            # The total count is the product.
            total_sum_of_mins = (total_sum_of_mins + arr[i] * left[i] * right[i]) % MOD
            
        return total_sum_of_mins
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   Two passes through the array using a monotonic stack. Each element is pushed and popped from the stack at most once.
*   **Space Complexity:** $O(N)$
    *   For `left`, `right` arrays and the stack.

---

## 7. Follow-up & Extensions

**Q: What if we needed `sum(max(b))`?**
**A:** Similar monotonic stack approach, but instead of Previous/Next Smaller Element, we'd use Previous/Next *Greater* Element (PGE/NGE).

**Q: Could this be done with Divide and Conquer?**
**A:** Yes, a segment tree with range minimum queries could work, but it would likely be $O(N \log N)$ and much more complex to implement than the monotonic stack approach.
