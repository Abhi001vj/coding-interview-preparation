# 4. Median of Two Sorted Arrays

**Difficulty:** Hard
**Pattern:** Binary Search (on Answer / Partition)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be $O(\log(m+n))$ (or $O(\log(\min(m,n)))$).

**Interview Scenario (The "Data Stream Merging" Prompt):**
"You are working with two independent, real-time data streams, each producing sorted numerical data. You need to provide a live `median` value across the *combined* dataset from both streams. To save memory and processing time, you cannot fully merge and sort the entire combined stream. How would you determine the median efficiently, especially given that the streams are very large but we only need to query the median?"

**Why this transformation?**
*   It emphasizes the **efficiency constraint** ($O(\log(m+n))$), ruling out simpler $O(m+n)$ merge approaches.
*   It frames the problem as needing a statistical measure from *conceptual* combined data, not actual merged data.

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty Arrays:** "Can one or both arrays be empty?" (Yes, handle edge cases where one is empty).
2.  **Odd/Even Total Length:** "How do I calculate the median for an even total number of elements?" (Average of the two middle elements).
3.  **Constraints:** "What are the maximum sizes of `m` and `n`?" ($0 \le m, n \le 1000$, total $m+n$ up to $2000$). Logarithmic complexity for this is key.

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Binary Search on Answer / Partition.

**The Logic:**
Instead of finding the median *value*, we are looking for the *correct partition* point in the two arrays. If we can correctly partition `nums1` and `nums2` such that:
1.  The left halves of both arrays combined contain `(m+n+1)//2` elements.
2.  The right halves of both arrays combined contain `(m+n) - (m+n+1)//2` elements.
3.  `max(left_half)` is less than or equal to `min(right_half)`.
Then the median can be found from the `max(left_half)` and `min(right_half)` values.

**Binary Search Idea:**
Focus on partitioning the *smaller* array (say `nums1`). This ensures the binary search range is $O(\min(m,n))$, leading to $O(\log(\min(m,n)))$ overall complexity.

Let `partitionX` be the split point in `nums1` and `partitionY` be the split point in `nums2`.
`partitionX + partitionY = (m+n+1)//2` (for total left elements).

We need to satisfy:
`maxLeftX <= minRightY`
`maxLeftY <= minRightX`

If `maxLeftX > minRightY`, we moved `partitionX` too far right in `nums1` (or `partitionY` too far left in `nums2`). So, move `partitionX` left (search in `[0, partitionX-1]`).
If `maxLeftY > minRightX`, we moved `partitionX` too far left (or `partitionY` too far right). So, move `partitionX` right (search in `[partitionX+1, m]`).

---

## 4. Base Template & Modification

**Standard Binary Search Template (on indices):**
```python
low, high = 0, len(array)
while low <= high:
    mid = (low + high) // 2
    # Check condition involving mid
    if condition_met: return result
    elif too_high: high = mid - 1
    else: low = mid + 1
```

**Modified Logic:**
We apply binary search on the `partitionX` index in the *smaller* array. The `partitionY` index is derived. Then we check the four critical values around the partitions.

---

## 5. Optimal Solution

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        
        # Binary search range for partition in nums1
        # partitionX represents the number of elements taken from nums1 into the left half
        low, high = 0, m
        
        # Calculate the total number of elements required in the left half
        # (m + n + 1) // 2 ensures we get the correct size for both odd and even total lengths
        # For odd total length, it gives the single middle element index
        # For even total length, it gives the index of the first of the two middle elements
        total_left_half_size = (m + n + 1) // 2
        
        while low <= high:
            # Try a partition in nums1
            partitionX = (low + high) // 2
            # Calculate corresponding partition in nums2
            partitionY = total_left_half_size - partitionX
            
            # Determine the four values crucial for checking the partition
            # If a partition is at 0, maxLeft is -infinity. If at length, minRight is +infinity.
            maxLeftX = nums1[partitionX - 1] if partitionX != 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX != m else float('inf')
            
            maxLeftY = nums2[partitionY - 1] if partitionY != 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY != n else float('inf')
            
            # Check if partitions are correct
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Correct partition found!
                
                # If total length is odd, median is the maximum of the left halves
                if (m + n) % 2 == 1:
                    return float(max(maxLeftX, maxLeftY))
                # If total length is even, median is average of maxLeft and minRight
                else:
                    return float(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            
            # Adjust binary search range
            elif maxLeftX > minRightY:
                # partitionX is too far right, need to move it left
                high = partitionX - 1
            else: # maxLeftY > minRightX
                # partitionX is too far left, need to move it right
                low = partitionX + 1
                
        # This part should ideally not be reached if inputs are valid
        return -1.0 
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(\log(\min(m, n)))$
    *   The binary search is performed on the length of the smaller array.
*   **Space Complexity:** $O(1)$
    *   Only scalar variables used.

---

## 7. Follow-up & Extensions

**Q: What if the arrays are not sorted?**
**A:** If not sorted, the $O(\log(m+n))$ approach is impossible. You would need to merge them first ($O(m+n) \log(m+n)$) or use a selection algorithm like Quickselect ($O(m+n)$ average).

**Q: What if there are duplicates and they need special handling (e.g., distinct medians)?**
**A:** The current approach handles duplicates correctly as it relies on relative ordering, not distinct values. However, if the definition of median changed based on distinct values, the problem becomes much harder.
