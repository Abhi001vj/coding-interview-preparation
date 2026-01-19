# Monotonic Stack

## Introduction

A Monotonic Stack maintains elements in sorted order (either increasing or decreasing). It efficiently solves problems where you need to find the **next/previous greater/smaller element** for each position. The key insight is that elements "wait" on the stack until they find their answer.

## Pattern Recognition

Use this pattern when you see:
- "Next greater element" / "Next smaller element"
- "Previous greater element" / "Previous smaller element"
- "Days until warmer temperature"
- "Largest rectangle in histogram"
- "Stock span" problems
- "Remove K digits" to minimize number
- Finding optimal pairs with index constraints (i < j)
- Problems involving "span" or "width" calculations

---

## Base Templates

### Template 1: Next Greater Element (Decreasing Stack)

```python
def next_greater(nums):
    """
    For each element, find the next greater element to its right.
    Returns: List where result[i] = index of next greater, or -1 if none.

    Stack is DECREASING (largest at bottom, smallest at top).
    Smallest elements are "most desperate" to find something greater.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Stores INDICES (not values!)

    for i in range(n):
        # Pop all smaller elements - current is their "next greater"
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = i  # or nums[i] for value instead of index

        stack.append(i)

    return result
```

### Template 2: Next Smaller Element (Increasing Stack)

```python
def next_smaller(nums):
    """
    For each element, find the next smaller element to its right.
    Returns: List where result[i] = index of next smaller, or -1 if none.

    Stack is INCREASING (smallest at bottom, largest at top).
    Largest elements are "most desperate" to find something smaller.
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        # Pop all larger elements - current is their "next smaller"
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = i

        stack.append(i)

    return result
```

### Template 3: Previous Greater Element (Decreasing Stack)

```python
def previous_greater(nums):
    """
    For each element, find the previous greater element to its left.
    Stack elements are CANDIDATES for my answer.
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        # Pop elements that can't be previous greater for future elements
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()

        # Stack top (if exists) is my previous greater
        if stack:
            result[i] = stack[-1]

        stack.append(i)

    return result
```

### Template 4: Previous Smaller Element (Increasing Stack)

```python
def previous_smaller(nums):
    """
    For each element, find the previous smaller element to its left.
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(i)

    return result
```

---

## Key Insights

### The "Opposite" Rule

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   WHAT YOU WANT    →    USE THE OPPOSITE STACK                     │
│                                                                     │
│   Find GREATER  →  DECREASING stack (small waits on top)           │
│   Find SMALLER  →  INCREASING stack (large waits on top)           │
│                                                                     │
│   WHY? The "opposite" puts the most "needy" element on top!        │
│                                                                     │
│   Decreasing: smallest on top → first to find its greater          │
│   Increasing: largest on top → first to find its smaller           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### NEXT vs PREVIOUS

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   NEXT (answer is to the RIGHT):                                   │
│   • Stack elements are WAITING for their answer                    │
│   • Pop condition: found their answer                              │
│   • result[popped_idx] = current                                   │
│                                                                     │
│   PREVIOUS (answer is to the LEFT):                                │
│   • Stack elements are CANDIDATES for my answer                    │
│   • Pop condition: remove invalid candidates                       │
│   • result[current_idx] = stack top                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Quick Reference Table

| Want to Find | Stack Type | Pop Condition | When to Set Result |
|--------------|------------|---------------|-------------------|
| Next Greater | Decreasing | `stack[-1] < curr` | When popping |
| Next Smaller | Increasing | `stack[-1] > curr` | When popping |
| Prev Greater | Decreasing | `stack[-1] <= curr` | After popping, check top |
| Prev Smaller | Increasing | `stack[-1] >= curr` | After popping, check top |

---

## LeetCode Problems

### Problem 1: LC 739 - Daily Temperatures

**Link:** [https://leetcode.com/problems/daily-temperatures/](https://leetcode.com/problems/daily-temperatures/)

**Problem:** Given daily temperatures, find how many days until a warmer day.

**Pattern:** Next Greater Element (Decreasing Stack)

**Template Modification:**
- Store indices in stack
- Result = difference in indices (days to wait)

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Decreasing stack of indices

        for i in range(n):
            # Pop all colder days - they found their warmer day
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                result[idx] = i - idx  # Days to wait

            stack.append(i)

        return result
```

**Complexity:** O(n) time, O(n) space

---

### Problem 2: LC 496 - Next Greater Element I

**Link:** [https://leetcode.com/problems/next-greater-element-i/](https://leetcode.com/problems/next-greater-element-i/)

**Problem:** Given nums1 (subset of nums2), find next greater element in nums2 for each element in nums1.

**Pattern:** Next Greater + HashMap

**Template Modification:**
- Build next greater map for nums2
- Look up each element in nums1

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Build map: element -> its next greater in nums2
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Remaining elements have no next greater
        for num in stack:
            next_greater[num] = -1

        return [next_greater[num] for num in nums1]
```

**Complexity:** O(n + m) time, O(n) space

---

### Problem 3: LC 503 - Next Greater Element II (Circular)

**Link:** [https://leetcode.com/problems/next-greater-element-ii/](https://leetcode.com/problems/next-greater-element-ii/)

**Problem:** Same as above but array is circular (can wrap around).

**Pattern:** Next Greater + Double Pass

**Template Modification:**
- Iterate through array twice (simulate circular)
- Use modulo for index

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        # Two passes to handle circular nature
        for i in range(2 * n):
            idx = i % n

            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]

            # Only push indices in first pass
            if i < n:
                stack.append(i)

        return result
```

**Complexity:** O(n) time, O(n) space

---

### Problem 4: LC 84 - Largest Rectangle in Histogram

**Link:** [https://leetcode.com/problems/largest-rectangle-in-histogram/](https://leetcode.com/problems/largest-rectangle-in-histogram/)

**Problem:** Find largest rectangular area in histogram.

**Pattern:** Previous Smaller + Next Smaller (Increasing Stack)

**Key Insight:** For each bar, find how far it can extend left and right (until hitting a smaller bar).

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n + 1):
            # Use 0 as sentinel for final cleanup
            h = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # Width = distance between previous smaller and current
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
```

**Alternative: Precompute boundaries**

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Find previous smaller
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # Find next smaller
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate max area
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area
```

**Complexity:** O(n) time, O(n) space

---

### Problem 5: LC 85 - Maximal Rectangle

**Link:** [https://leetcode.com/problems/maximal-rectangle/](https://leetcode.com/problems/maximal-rectangle/)

**Problem:** Find largest rectangle containing only 1s in binary matrix.

**Pattern:** Largest Rectangle in Histogram (row by row)

**Template Modification:**
- Build histogram heights for each row
- Apply LC 84 solution to each row

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            # Update heights
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            # Apply largest rectangle in histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights = heights + [0]  # Sentinel

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
```

**Complexity:** O(rows * cols) time, O(cols) space

---

### Problem 6: LC 42 - Trapping Rain Water

**Link:** [https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)

**Problem:** Calculate how much rain water can be trapped.

**Pattern:** Monotonic Stack (Decreasing)

**Key Insight:** Water is trapped between bars. When we find a taller bar, calculate water trapped with previous bars.

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # Decreasing stack
        water = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = height[stack.pop()]

                if not stack:
                    break

                left = stack[-1]
                width = i - left - 1
                bounded_height = min(height[left], h) - bottom
                water += width * bounded_height

            stack.append(i)

        return water
```

**Alternative: Two Pointers (O(1) space)**

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water
```

**Complexity:** O(n) time, O(n) or O(1) space

---

### Problem 7: LC 901 - Online Stock Span

**Link:** [https://leetcode.com/problems/online-stock-span/](https://leetcode.com/problems/online-stock-span/)

**Problem:** For each day's price, return count of consecutive days (including today) where price was <= today's price.

**Pattern:** Previous Greater Element (Decreasing Stack with counts)

```python
class StockSpanner:
    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price: int) -> int:
        span = 1

        # Pop all smaller/equal prices, accumulate their spans
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span
```

**Complexity:** O(1) amortized per call

---

### Problem 8: LC 962 - Maximum Width Ramp

**Link:** [https://leetcode.com/problems/maximum-width-ramp/](https://leetcode.com/problems/maximum-width-ramp/)

**Problem:** Find maximum j - i where i < j and nums[i] <= nums[j].

**Pattern:** Decreasing Stack + Reverse Scan

**Key Insight:** Only decreasing elements can be optimal starting points.

```python
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        # Step 1: Build decreasing stack of potential starting points
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # Step 2: Scan from right, match with stack
        max_width = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)

        return max_width
```

**Complexity:** O(n) time, O(n) space

---

### Problem 9: LC 402 - Remove K Digits

**Link:** [https://leetcode.com/problems/remove-k-digits/](https://leetcode.com/problems/remove-k-digits/)

**Problem:** Remove k digits to make the smallest number.

**Pattern:** Increasing Stack (greedy)

**Key Insight:** Remove larger digits that come before smaller digits.

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            # Remove larger digits before smaller ones
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # Remove remaining from end if k > 0
        stack = stack[:-k] if k else stack

        # Remove leading zeros and handle empty case
        return ''.join(stack).lstrip('0') or '0'
```

**Complexity:** O(n) time, O(n) space

---

### Problem 10: LC 907 - Sum of Subarray Minimums

**Link:** [https://leetcode.com/problems/sum-of-subarray-minimums/](https://leetcode.com/problems/sum-of-subarray-minimums/)

**Problem:** Sum of min(subarray) for all subarrays.

**Pattern:** Previous Smaller + Next Smaller

**Key Insight:** For each element, count how many subarrays it's the minimum of.

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # Previous less element (strictly less)
        prev_less = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)

        # Next less element (less or equal to handle duplicates)
        next_less = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate contribution of each element
        total = 0
        for i in range(n):
            left_count = i - prev_less[i]
            right_count = next_less[i] - i
            total = (total + arr[i] * left_count * right_count) % MOD

        return total
```

**Complexity:** O(n) time, O(n) space

---

## Common Mistakes

1. **Storing values instead of indices**
   - Usually need indices to calculate distances/widths
   - Store indices, access values via `nums[stack[-1]]`

2. **Wrong comparison operator**
   - `<` vs `<=` matters for handling duplicates
   - `<` for strictly greater/smaller
   - `<=` when equal elements should also trigger pop

3. **Forgetting to handle remaining stack elements**
   - After iteration, stack may have elements without answers
   - Set their result to -1 or use sentinel value

4. **Off-by-one in width calculations**
   - Width = `right - left - 1` (exclusive of boundaries)
   - Be careful with empty stack case

5. **Confusing NEXT vs PREVIOUS logic**
   - NEXT: set result when popping
   - PREVIOUS: set result after checking stack top

---

## Practice Checklist

- [ ] LC 739 - Daily Temperatures (Easy warm-up)
- [ ] LC 496 - Next Greater Element I (Basic)
- [ ] LC 503 - Next Greater Element II (Circular)
- [ ] LC 84 - Largest Rectangle in Histogram (Classic Hard)
- [ ] LC 85 - Maximal Rectangle (Apply LC 84)
- [ ] LC 42 - Trapping Rain Water (Classic)
- [ ] LC 901 - Online Stock Span (Span counting)
- [ ] LC 962 - Maximum Width Ramp (Two-phase)
- [ ] LC 402 - Remove K Digits (Greedy)
- [ ] LC 907 - Sum of Subarray Minimums (Contribution counting)
