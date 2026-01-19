# Two Pointers

## Introduction

The Two Pointers pattern uses two pointers to traverse a data structure, often from opposite ends or in the same direction. It reduces O(n²) brute force to O(n) by eliminating redundant comparisons. The key insight is that pointer movement decisions eliminate multiple possibilities at once.

## Pattern Recognition

Use this pattern when you see:
- **Sorted array** (huge hint!)
- "Find pair with target sum"
- "Remove duplicates in place"
- "Reverse array/string"
- "Palindrome check"
- "Container with most water"
- "Move zeros / partition array"
- "3Sum, 4Sum" (outer loop + two pointers)

---

## Base Templates

### Template 1: Opposite Direction (Sorted Array)

```python
def two_sum_sorted(arr, target):
    """
    Find pair that sums to target in sorted array.
    Move pointers based on sum comparison.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1   # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return []
```

### Template 2: Same Direction (Fast/Slow)

```python
def remove_duplicates(arr):
    """
    Remove duplicates in-place from sorted array.
    Slow pointer marks write position, fast scans.
    """
    if not arr:
        return 0

    write = 1  # Slow pointer (write position)

    for read in range(1, len(arr)):  # Fast pointer
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1

    return write
```

### Template 3: Partition (Dutch National Flag)

```python
def partition(arr, pivot):
    """
    Partition array around pivot.
    Three regions: < pivot, == pivot, > pivot
    """
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > pivot:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1

    return arr
```

### Template 4: Reverse

```python
def reverse(arr, left, right):
    """
    Reverse array in-place between indices.
    """
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

---

## Key Insights

### Why Two Pointers Works (Sorted Array)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   arr = [1, 3, 5, 7, 9], target = 8                                │
│          L           R                                              │
│                                                                     │
│   sum = 1 + 9 = 10 > 8                                             │
│   → R can't pair with ANY element to the right of L               │
│   → Move R left (eliminates ALL pairs with R)                      │
│                                                                     │
│   sum = 1 + 7 = 8 = target ✓                                       │
│                                                                     │
│   Key: Each move eliminates MULTIPLE pairs, not just one!          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Choosing Direction

| Pattern | Direction | Use When |
|---------|-----------|----------|
| Opposite | ← L ... R → | Sorted array, pair finding, palindrome |
| Same | L → ... R → | Remove in-place, fast/slow |
| Three-way | L, M, R | Partition, Dutch National Flag |

---

## LeetCode Problems

### Problem 1: LC 167 - Two Sum II (Sorted Array)

**Link:** [https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Problem:** Find two numbers that sum to target in sorted array.

**Pattern:** Opposite direction

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]  # 1-indexed
            elif total < target:
                left += 1
            else:
                right -= 1

        return []
```

**Complexity:** O(n)

---

### Problem 2: LC 15 - 3Sum

**Link:** [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/)

**Problem:** Find all unique triplets that sum to zero.

**Pattern:** Sort + Outer loop + Two pointers

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early termination
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
```

**Complexity:** O(n²)

---

### Problem 3: LC 11 - Container With Most Water

**Link:** [https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

**Problem:** Find two lines that form container with most water.

**Pattern:** Opposite direction, move shorter line

**Key Insight:** Moving the taller line can only decrease area.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_water = max(max_water, width * h)

            # Move the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
```

**Complexity:** O(n)

---

### Problem 4: LC 42 - Trapping Rain Water

**Link:** [https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)

**Problem:** Calculate trapped rain water.

**Pattern:** Two pointers with max tracking

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

**Complexity:** O(n) time, O(1) space

---

### Problem 5: LC 26 - Remove Duplicates from Sorted Array

**Link:** [https://leetcode.com/problems/remove-duplicates-from-sorted-array/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Problem:** Remove duplicates in-place, return new length.

**Pattern:** Same direction (write/read pointers)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write
```

**Complexity:** O(n)

---

### Problem 6: LC 283 - Move Zeroes

**Link:** [https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)

**Problem:** Move all zeros to end, maintaining relative order.

**Pattern:** Same direction (write position)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        # Move all non-zeros to front
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
```

**Complexity:** O(n)

---

### Problem 7: LC 125 - Valid Palindrome

**Link:** [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/)

**Problem:** Check if string is palindrome (alphanumeric only).

**Pattern:** Opposite direction

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

**Complexity:** O(n)

---

### Problem 8: LC 75 - Sort Colors (Dutch National Flag)

**Link:** [https://leetcode.com/problems/sort-colors/](https://leetcode.com/problems/sort-colors/)

**Problem:** Sort array with only 0, 1, 2 in-place.

**Pattern:** Three-way partition

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:  # nums[mid] == 1
                mid += 1
```

**Complexity:** O(n)

---

### Problem 9: LC 977 - Squares of a Sorted Array

**Link:** [https://leetcode.com/problems/squares-of-a-sorted-array/](https://leetcode.com/problems/squares-of-a-sorted-array/)

**Problem:** Return sorted squares of sorted array.

**Pattern:** Opposite direction (merge from ends)

**Key Insight:** Largest squares are at the ends (largest absolute values).

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1  # Fill from end

        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1

        return result
```

**Complexity:** O(n)

---

### Problem 10: LC 18 - 4Sum

**Link:** [https://leetcode.com/problems/4sum/](https://leetcode.com/problems/4sum/)

**Problem:** Find all unique quadruplets that sum to target.

**Pattern:** Two outer loops + Two pointers

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
```

**Complexity:** O(n³)

---

## Common Mistakes

1. **Forgetting array must be sorted**
   - Opposite-direction only works on sorted arrays
   - Sort first if needed: O(n log n)

2. **Infinite loop with `while left <= right`**
   - Use `left < right` to avoid processing same element twice

3. **Not handling duplicates in k-Sum**
   - Skip duplicates after finding a valid combination

4. **Wrong direction choice**
   - Sorted + pair finding → opposite
   - In-place modification → same direction

5. **Off-by-one in partition**
   - Test with arrays of size 0, 1, 2

---

## Practice Checklist

- [ ] LC 167 - Two Sum II (Basic sorted pair)
- [ ] LC 15 - 3Sum (Skip duplicates)
- [ ] LC 11 - Container With Most Water (Greedy)
- [ ] LC 42 - Trapping Rain Water (Two pointers + max)
- [ ] LC 26 - Remove Duplicates (Write pointer)
- [ ] LC 283 - Move Zeroes (Partition)
- [ ] LC 125 - Valid Palindrome (Classic)
- [ ] LC 75 - Sort Colors (Dutch National Flag)
- [ ] LC 977 - Squares of Sorted Array (Merge from ends)
- [ ] LC 18 - 4Sum (Extension of 3Sum)
