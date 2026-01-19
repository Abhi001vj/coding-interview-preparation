# 33. Search in Rotated Sorted Array
**Difficulty:** Medium | **Pattern:** Binary Search (Modified) | **Companies:** Google, Meta, Amazon, Microsoft

---

## 1. Google/Meta Style Question Transformation

### Original LeetCode Problem:
Given a rotated sorted array `nums` (originally sorted in ascending order, then rotated at some pivot), search for `target`. Return its index or -1 if not found. You must write an algorithm with O(log n) runtime complexity.

### Google Scenario Wrapper:
> "At Google Cloud, we store server IDs in a circular buffer that was originally sorted. Due to a system restart, the buffer rotated at an unknown position. Given a server ID to find, locate it efficiently. The buffer has millions of entries, so linear search is too slow."

### Meta Constraint Twist:
> Same problem but: "Return the number of rotations (pivot index) in addition to finding the target. If target not found, still return the rotation count."

---

## 2. Clarifying Questions (Ask in Interview!)

1. **Input Constraints:**
   - Are all elements unique? → Yes (for this version)
   - Can array be not rotated (rotation = 0)? → Yes
   - What's the size? → 1 ≤ n ≤ 5000
   - Range of values? → -10⁴ ≤ nums[i] ≤ 10⁴

2. **Edge Cases:**
   - Single element array
   - Array not rotated (fully sorted)
   - Target at rotation point
   - Target not in array

3. **Output Requirements:**
   - Return index of target
   - Return -1 if not found

---

## 3. Pattern Recognition

### Why Binary Search?
- **Key Signal 1:** "O(log n) runtime" → Must be binary search
- **Key Signal 2:** Array is sorted (with modification)
- **Key Signal 3:** Searching for specific element

### Pattern Match:
| Problem Feature | Pattern Indicator |
|-----------------|-------------------|
| "O(log n)" explicitly required | Binary search |
| Rotated sorted array | Modified binary search |
| One half is always sorted | Can determine which half to search |

### Key Insight:
**At any point in a rotated sorted array, at least ONE half is always fully sorted!**

```
Example: [4, 5, 6, 7, 0, 1, 2]
                    ^
                 rotation point

If we pick mid = 7:
- Left half [4,5,6,7] is sorted ✓
- Right half [0,1,2] is sorted ✓

If we pick mid = 6:
- Left half [4,5,6] is sorted ✓
- Right half [7,0,1,2] is NOT sorted
```

---

## 4. Approach Discussion

### Approach 1: Find Pivot + Two Binary Searches - O(log n)
**Intuition:** First find rotation point, then binary search correct half.

**Steps:**
1. Binary search to find minimum (rotation point)
2. Determine which half target is in
3. Binary search that half

**Cons:** Two passes, more complex

### Approach 2: Modified Single Binary Search - O(log n) (Optimal)
**Intuition:** In one pass, determine which half is sorted and if target is there.

**Steps:**
1. Find mid point
2. Determine which half is sorted (compare with left/right)
3. Check if target is in sorted half
4. Narrow search to appropriate half

---

## 5. Base Template

```python
# Base Template: Binary Search in Rotated Array
def search_rotated(nums, target):
    """
    Key insight: One half is ALWAYS sorted.

    Steps at each iteration:
    1. Find mid
    2. Identify which half is sorted
    3. Check if target is in sorted half
    4. Narrow search accordingly
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target in left half
            else:
                left = mid + 1   # Target in right half
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target in right half
            else:
                right = mid - 1  # Target in left half

    return -1
```

---

## 6. Solution - How We Modify the Template

### Template Modification Needed:
- **What changes:** Add sorted half detection before deciding search direction
- **Key insight:** Use `nums[left] <= nums[mid]` to determine if left half is sorted

### Solution (Optimal)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Modified binary search for rotated sorted array.

        Key insight: At least one half is always sorted.
        Use the sorted half to determine where target could be.

        Time: O(log n)
        Space: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Found target
            if nums[mid] == target:
                return mid

            # Check which half is sorted
            if nums[left] <= nums[mid]:
                # LEFT half is sorted [left...mid]
                # Check if target is in sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Search right
            else:
                # RIGHT half is sorted [mid...right]
                # Check if target is in sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right
                else:
                    right = mid - 1  # Search left

        return -1
```

### Visual Walkthrough for nums=[4,5,6,7,0,1,2], target=0:

```
Initial: left=0, right=6
         [4, 5, 6, 7, 0, 1, 2]
          ^        ^        ^
         left     mid     right

Step 1: mid=3, nums[mid]=7
        nums[left]=4 <= nums[mid]=7 → LEFT half sorted
        Is target=0 in [4,7)? NO (0 < 4)
        → Search RIGHT: left=4

         [4, 5, 6, 7, 0, 1, 2]
                      ^     ^
                     left  right

Step 2: mid=5, nums[mid]=1
        nums[left]=0 <= nums[mid]=1 → LEFT half sorted
        Is target=0 in [0,1)? YES!
        → Search LEFT: right=4

         [4, 5, 6, 7, 0, 1, 2]
                      ^
                   left=right

Step 3: mid=4, nums[mid]=0
        nums[mid] == target ✓
        Return 4

Answer: 4
```

### Why `nums[left] <= nums[mid]` and not `<`?

```
Edge case: [3, 1], target=1
left=0, right=1, mid=0

If we use <:
  nums[left]=3 < nums[mid]=3? NO
  → Goes to else (right half sorted)
  → Checks if 3 < 1 <= 1? NO
  → right = -1, exit loop, return -1 ❌ WRONG

If we use <=:
  nums[left]=3 <= nums[mid]=3? YES
  → Left half is "sorted" (single element)
  → Checks if 3 <= 1 < 3? NO
  → left = 1
  → Next iteration: nums[mid]=1 == target ✓
```

---

## 7. Complexity Analysis

### Time Complexity: O(log n)
- Standard binary search eliminates half of remaining elements each iteration
- Maximum iterations: log₂(n)

### Space Complexity: O(1)
- Only using constant extra variables (left, right, mid)
- No recursion, no additional data structures

---

## 8. Test Cases & Edge Cases

```python
# Test Case 1: Basic rotated array
Input: nums = [4,5,6,7,0,1,2], target = 0
Expected: 4

# Test Case 2: Target not found
Input: nums = [4,5,6,7,0,1,2], target = 3
Expected: -1

# Test Case 3: Not rotated (sorted array)
Input: nums = [1,2,3,4,5], target = 3
Expected: 2

# Test Case 4: Single element - found
Input: nums = [1], target = 1
Expected: 0

# Test Case 5: Single element - not found
Input: nums = [1], target = 0
Expected: -1

# Test Case 6: Two elements
Input: nums = [3,1], target = 1
Expected: 1

# Test Case 7: Target at rotation point
Input: nums = [4,5,6,7,0,1,2], target = 4
Expected: 0

# Test Case 8: Full rotation (same as original)
Input: nums = [1,2,3], target = 2
Expected: 1
```

---

## 9. Common Mistakes to Avoid

1. **Using `<` instead of `<=` for sorted half check:**
   ```python
   # WRONG - fails when left == mid
   if nums[left] < nums[mid]:

   # CORRECT - handles single element half
   if nums[left] <= nums[mid]:
   ```

2. **Wrong boundary conditions for target check:**
   ```python
   # WRONG - missing boundary handling
   if nums[left] < target < nums[mid]:

   # CORRECT - include left boundary
   if nums[left] <= target < nums[mid]:
   ```

3. **Off-by-one in search direction:**
   ```python
   # When target is in range, search that half
   # When target is NOT in range, search OTHER half
   ```

4. **Forgetting to handle `nums[mid] == target` first:**
   ```python
   # Must check this BEFORE determining which half is sorted
   if nums[mid] == target:
       return mid
   ```

---

## 10. Follow-up Questions

### Follow-up 1: "What if there are duplicates?" (LC 81)
**Answer:** When nums[left] == nums[mid] == nums[right], we can't determine which half is sorted. Shrink both ends: left++, right--. Worst case becomes O(n).
```python
if nums[left] == nums[mid] == nums[right]:
    left += 1
    right -= 1
    continue
```

### Follow-up 2: "Find the minimum element" (LC 153)
**Answer:** Similar approach - search for point where nums[mid] > nums[mid+1]
```python
if nums[mid] > nums[right]:
    left = mid + 1
else:
    right = mid
return nums[left]
```

### Follow-up 3: "Find the rotation count/pivot index"
**Answer:** Minimum element's index equals rotation count
```python
# Rotation count = index of minimum element
```

### Related Problems:
- LC 81 - Search in Rotated Sorted Array II (With duplicates)
- LC 153 - Find Minimum in Rotated Sorted Array
- LC 154 - Find Minimum in Rotated Sorted Array II (With duplicates)
- LC 162 - Find Peak Element (Similar binary search logic)

---

## 11. Interview Tips

- **Time Target:** 15-20 minutes for this medium problem
- **Communication Points:**
  - "I notice O(log n) is required, so this must be binary search"
  - "Even though it's rotated, at least one half is always sorted"
  - "I'll use the sorted half to determine if target could be there"
  - "Let me draw out an example to verify my logic..."
- **Red Flags to Avoid:**
  - Trying to find rotation point first (overcomplicated)
  - Forgetting edge cases with `<=` vs `<`
  - Not verifying with small examples like [3,1]
