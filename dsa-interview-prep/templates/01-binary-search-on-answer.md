# Binary Search on Answer

## Introduction

Binary Search on Answer is a powerful technique where instead of searching for an element in an array, we search for the **optimal value** (minimum or maximum) that satisfies a given condition. The key insight is that the answer space is **monotonic** - if a value works, all values in one direction also work.

## Pattern Recognition

Use this pattern when you see:
- "Find **minimum/maximum** value that satisfies condition"
- "Smallest divisor", "Maximum distance", "Minimum capacity"
- The answer is a **NUMBER in a RANGE**, not an element in array
- You can **CHECK if a value works** in O(n) or O(n log n)
- **MONOTONIC relationship**: If condition is true for X, it's true for all values in one direction

### Common Keywords
- "Minimize the maximum..."
- "Maximize the minimum..."
- "Smallest X such that..."
- "At most K operations/days/hours"

---

## Base Templates

### Template 1: Find MINIMUM Valid Answer

```python
def binary_search_min(lo, hi, is_valid):
    """
    Find smallest x in [lo, hi] where is_valid(x) is True.

    Assumes: is_valid(x) = False for x < answer, True for x >= answer

    Example: Find smallest divisor where sum <= threshold
             [False, False, False, True, True, True]
                                   ^ answer
    """
    while lo < hi:
        mid = (lo + hi) // 2

        if is_valid(mid):
            hi = mid      # mid works, but maybe smaller works too - search LEFT
        else:
            lo = mid + 1  # mid doesn't work, need larger - search RIGHT

    return lo  # lo == hi at this point
```

### Template 2: Find MAXIMUM Valid Answer

```python
def binary_search_max(lo, hi, is_valid):
    """
    Find largest x in [lo, hi] where is_valid(x) is True.

    Assumes: is_valid(x) = True for x <= answer, False for x > answer

    Example: Find maximum distance to place balls
             [True, True, True, True, False, False]
                               ^ answer
    """
    while lo < hi:
        mid = (lo + hi + 1) // 2  # +1 to round UP (prevents infinite loop!)

        if is_valid(mid):
            lo = mid      # mid works, but maybe larger works too - search RIGHT
        else:
            hi = mid - 1  # mid doesn't work, need smaller - search LEFT

    return lo
```

---

## Key Insights

### Why `lo = mid + 1` but `hi = mid`?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   When INVALID (lo = mid + 1):                                     │
│   ─────────────────────────────                                    │
│   • mid is DEFINITELY WRONG - we KNOW it's not the answer         │
│   • Safe to SKIP it entirely: lo = mid + 1                        │
│                                                                     │
│   When VALID (hi = mid):                                           │
│   ───────────────────────                                          │
│   • mid MIGHT BE the answer! (smallest valid we've seen)          │
│   • We CAN'T skip it - must KEEP it in range: hi = mid            │
│   • If we used hi = mid - 1, we might skip the actual answer!     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### The Convergence Guarantee

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   • Loop continues while lo < hi                                   │
│   • Stops when lo == hi (they converge to same point)             │
│   • hi only moves to VALID positions                              │
│   • lo keeps pushing forward, skipping invalid ones               │
│   • They MEET at the boundary = smallest valid answer!            │
│                                                                     │
│   Visual:                                                          │
│   [invalid, invalid, invalid, VALID, valid, valid]                │
│    ^lo                        ^hi                                  │
│              ... converge ...                                      │
│                              ^lo=hi (answer!)                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Why +1 for Maximum?

```
Finding MAX: mid = (lo + hi + 1) // 2

Without +1: lo=4, hi=5 → mid=4 → if valid, lo=4 (STUCK! infinite loop)
With +1:    lo=4, hi=5 → mid=5 → if valid, lo=5 (progress!)
```

### Quick Reference Table

| Goal | mid calculation | When valid | When invalid |
|------|-----------------|------------|--------------|
| Find MIN valid | `(lo + hi) // 2` | `hi = mid` | `lo = mid + 1` |
| Find MAX valid | `(lo + hi + 1) // 2` | `lo = mid` | `hi = mid - 1` |

---

## LeetCode Problems

### Problem 1: LC 1283 - Smallest Divisor Given a Threshold

**Link:** [https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

**Problem:** Given array `nums` and `threshold`, find the smallest divisor such that sum of ceil(nums[i]/divisor) <= threshold.

**Pattern:** Find MINIMUM valid (smallest divisor that satisfies condition)

**Key Insight:** As divisor increases, sum DECREASES (monotonic!). So we binary search for smallest divisor where sum <= threshold.

**Template Modification:**
- `lo = 1` (smallest possible divisor)
- `hi = max(nums)` (any larger just gives len(nums))
- `is_valid(mid)` = sum of ceiling divisions <= threshold

```python
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_valid(divisor):
            # Sum of ceil(num / divisor) for all nums
            total = sum(math.ceil(num / divisor) for num in nums)
            # Alternative without math: (num + divisor - 1) // divisor
            return total <= threshold

        lo, hi = 1, max(nums)

        while lo < hi:
            mid = (lo + hi) // 2

            if is_valid(mid):
                hi = mid      # Valid, try smaller
            else:
                lo = mid + 1  # Invalid, need larger

        return lo
```

**Complexity:** O(n log(max(nums)))

---

### Problem 2: LC 875 - Koko Eating Bananas

**Link:** [https://leetcode.com/problems/koko-eating-bananas/](https://leetcode.com/problems/koko-eating-bananas/)

**Problem:** Koko eats bananas at speed k per hour. Each pile takes ceil(pile/k) hours. Find minimum k to finish all piles in h hours.

**Pattern:** Find MINIMUM valid (smallest speed that finishes in time)

**Key Insight:** Higher speed → fewer hours (monotonic). Binary search for smallest speed where total hours <= h.

**Template Modification:**
- `lo = 1` (eat at least 1 banana/hour)
- `hi = max(piles)` (eating faster than largest pile is pointless)
- `is_valid(k)` = total hours <= h

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum((pile + k - 1) // k for pile in piles)

        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2

            if hours_needed(mid) <= h:
                hi = mid      # Can finish, try slower
            else:
                lo = mid + 1  # Too slow, need faster

        return lo
```

**Complexity:** O(n log(max(piles)))

---

### Problem 3: LC 1011 - Capacity To Ship Packages Within D Days

**Link:** [https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

**Problem:** Ship packages in order. Find minimum ship capacity to ship all in d days.

**Pattern:** Find MINIMUM valid (smallest capacity that ships in time)

**Key Insight:** Larger capacity → fewer days needed (monotonic). Must be able to carry the heaviest single package.

**Template Modification:**
- `lo = max(weights)` (must carry heaviest package)
- `hi = sum(weights)` (ship everything in 1 day)
- `is_valid(capacity)` = days needed <= d

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(capacity):
            day_count = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    day_count += 1
                    current_load = weight
                else:
                    current_load += weight

            return day_count

        lo, hi = max(weights), sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2

            if days_needed(mid) <= days:
                hi = mid      # Can ship, try smaller capacity
            else:
                lo = mid + 1  # Need more capacity

        return lo
```

**Complexity:** O(n log(sum(weights)))

---

### Problem 4: LC 410 - Split Array Largest Sum

**Link:** [https://leetcode.com/problems/split-array-largest-sum/](https://leetcode.com/problems/split-array-largest-sum/)

**Problem:** Split array into k subarrays. Minimize the largest sum among subarrays.

**Pattern:** Find MINIMUM valid (smallest "max sum" that allows k splits)

**Key Insight:** If max allowed sum is X, count how many subarrays needed. Larger X → fewer subarrays.

**Template Modification:**
- `lo = max(nums)` (at minimum, must fit largest element)
- `hi = sum(nums)` (one subarray holds everything)
- `is_valid(max_sum)` = can split into <= k subarrays

```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num

            return subarrays <= k

        lo, hi = max(nums), sum(nums)

        while lo < hi:
            mid = (lo + hi) // 2

            if can_split(mid):
                hi = mid      # Can split, try smaller max
            else:
                lo = mid + 1  # Need larger max allowed

        return lo
```

**Complexity:** O(n log(sum(nums)))

---

### Problem 5: LC 1552 - Magnetic Force Between Two Balls

**Link:** [https://leetcode.com/problems/magnetic-force-between-two-balls/](https://leetcode.com/problems/magnetic-force-between-two-balls/)

**Problem:** Place m balls in positions. Maximize the minimum distance between any two balls.

**Pattern:** Find MAXIMUM valid (largest minimum distance that allows m balls)

**Key Insight:** Larger min distance → harder to place balls. Find max distance where we can still place m balls.

**Template Modification:**
- `lo = 1` (minimum possible distance)
- `hi = (max - min) position` (max possible distance)
- `is_valid(min_dist)` = can place m balls with at least min_dist apart

```python
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(min_dist):
            count = 1
            last_pos = position[0]

            for pos in position[1:]:
                if pos - last_pos >= min_dist:
                    count += 1
                    last_pos = pos

            return count >= m

        lo, hi = 1, position[-1] - position[0]

        while lo < hi:
            mid = (lo + hi + 1) // 2  # +1 because finding MAX

            if can_place(mid):
                lo = mid      # Can place, try larger distance
            else:
                hi = mid - 1  # Can't place, need smaller distance

        return lo
```

**Complexity:** O(n log(max_position))

---

### Problem 6: LC 774 - Minimize Max Distance to Gas Station

**Link:** [https://leetcode.com/problems/minimize-max-distance-to-gas-station/](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) (Premium)

**Problem:** Add k gas stations to minimize the maximum distance between adjacent stations.

**Pattern:** Find MINIMUM valid (smallest max gap achievable with k stations)

**Key Insight:** To achieve max gap of X, each existing gap needs ceil(gap/X) - 1 new stations.

**Template Modification:**
- `lo = 0` (theoretical minimum)
- `hi = max gap` (no stations added)
- `is_valid(max_gap)` = stations needed <= k
- Use floating point binary search with precision

```python
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def stations_needed(max_gap):
            count = 0
            for i in range(len(stations) - 1):
                gap = stations[i + 1] - stations[i]
                count += int(gap / max_gap)  # How many to add in this gap
            return count

        lo, hi = 0, max(stations[i+1] - stations[i] for i in range(len(stations)-1))

        # Floating point binary search
        while hi - lo > 1e-6:
            mid = (lo + hi) / 2

            if stations_needed(mid) <= k:
                hi = mid      # Can achieve, try smaller gap
            else:
                lo = mid      # Need more stations, allow larger gap

        return hi
```

**Complexity:** O(n log(max_gap / precision))

---

## Common Mistakes

1. **Wrong boundary initialization**
   - Forgetting `lo = max(nums)` when each element must fit
   - Setting `hi` too small and missing valid answers

2. **Forgetting +1 for maximum problems**
   - Causes infinite loop when `lo + 1 == hi`

3. **Off-by-one in is_valid**
   - Using `<` instead of `<=` in threshold checks
   - Forgetting to count the first/last element

4. **Integer overflow**
   - Use `mid = lo + (hi - lo) // 2` instead of `(lo + hi) // 2`
   - Though Python handles this, good habit for other languages

5. **Not identifying monotonic relationship**
   - Always verify: "If X works, do all larger/smaller values work?"

---

## Practice Checklist

- [ ] LC 1283 - Smallest Divisor (Easy warm-up)
- [ ] LC 875 - Koko Eating Bananas (Classic)
- [ ] LC 1011 - Ship Packages (Classic)
- [ ] LC 410 - Split Array Largest Sum (Hard)
- [ ] LC 1552 - Magnetic Force (MAX variant)
- [ ] LC 774 - Gas Station (Floating point)
- [ ] LC 668 - Kth Smallest Number in Multiplication Table
- [ ] LC 719 - Find K-th Smallest Pair Distance
- [ ] LC 878 - Nth Magical Number
