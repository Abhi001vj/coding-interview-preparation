# Interval Problems

## Introduction

Interval problems involve operations on ranges represented as [start, end] pairs. The key insight is that **sorting** transforms these problems into linear scans. The choice of sorting by start or end depends on what you're trying to achieve.

## Pattern Recognition

Use this pattern when you see:
- "Overlapping intervals"
- "Merge intervals"
- "Meeting rooms"
- "Minimum arrows/points to cover"
- "Maximum non-overlapping intervals"
- "Insert/remove interval"
- Array of [start, end] pairs

---

## Base Templates

### Template 1: Merge Overlapping Intervals (Sort by START)

```python
def merge_intervals(intervals):
    """
    Merge all overlapping intervals.
    Sort by START to process intervals in order.
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last = merged[-1]

        if start <= last[1]:  # Overlapping
            last[1] = max(last[1], end)  # Extend end
        else:
            merged.append([start, end])

    return merged
```

### Template 2: Minimum Points to Cover (Sort by END)

```python
def min_points_to_cover(intervals):
    """
    Minimum points/arrows to hit all intervals.
    Sort by END - greedy "finish earliest first".
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]

    for start, finish in intervals[1:]:
        if start > end:  # Current point doesn't cover this
            count += 1
            end = finish  # Place new point at interval end

    return count
```

### Template 3: Maximum Non-Overlapping (Sort by END)

```python
def max_non_overlapping(intervals):
    """
    Maximum number of non-overlapping intervals.
    Sort by END - greedy "finish earliest first".
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]

    for start, finish in intervals[1:]:
        if start >= end:  # No overlap (can start exactly when previous ends)
            count += 1
            end = finish

    return count
```

### Template 4: Meeting Rooms (Sort by START + Heap)

```python
import heapq

def min_meeting_rooms(intervals):
    """
    Minimum rooms needed for all meetings.
    Sort by START, use heap to track end times.
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = []  # End times of ongoing meetings

    for start, end in intervals:
        # If earliest ending meeting is done, reuse that room
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        heapq.heappush(heap, end)

    return len(heap)
```

---

## Key Insights

### When to Sort by What?

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   Sort by END when:                                                 │
│   • Finding minimum points/arrows to cover all                     │
│   • Finding maximum non-overlapping intervals                      │
│   • Greedy "finish earliest first" strategy                        │
│   • Activity selection problem                                      │
│                                                                     │
│   Sort by START when:                                               │
│   • Merging overlapping intervals                                  │
│   • Processing intervals in order                                  │
│   • Meeting rooms (with heap for end times)                        │
│   • Insert interval                                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Overlap Conditions

```
Two intervals [a1, b1] and [a2, b2] overlap if and only if:
    a1 <= b2 AND a2 <= b1

Simplified (when sorted by start): a2 <= b1 (second starts before first ends)

No overlap: a2 > b1 (second starts after first ends)
```

---

## LeetCode Problems

### Problem 1: LC 56 - Merge Intervals

**Link:** [https://leetcode.com/problems/merge-intervals/](https://leetcode.com/problems/merge-intervals/)

**Problem:** Merge all overlapping intervals.

**Pattern:** Sort by START, extend end when overlapping

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return merged
```

**Complexity:** O(n log n)

---

### Problem 2: LC 57 - Insert Interval

**Link:** [https://leetcode.com/problems/insert-interval/](https://leetcode.com/problems/insert-interval/)

**Problem:** Insert new interval and merge if necessary.

**Pattern:** Three phases - before, overlap, after

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
```

**Complexity:** O(n)

---

### Problem 3: LC 435 - Non-overlapping Intervals

**Link:** [https://leetcode.com/problems/non-overlapping-intervals/](https://leetcode.com/problems/non-overlapping-intervals/)

**Problem:** Minimum intervals to remove for no overlaps.

**Pattern:** Sort by END, count max non-overlapping

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        non_overlapping = 1
        end = intervals[0][1]

        for start, finish in intervals[1:]:
            if start >= end:  # No overlap
                non_overlapping += 1
                end = finish

        return len(intervals) - non_overlapping
```

**Complexity:** O(n log n)

---

### Problem 4: LC 452 - Minimum Number of Arrows to Burst Balloons

**Link:** [https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

**Problem:** Minimum arrows to burst all balloons (intervals).

**Pattern:** Sort by END, greedy placement

```python
class Solution:
    def findMinArrowPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]

        for start, finish in points[1:]:
            if start > end:  # Arrow doesn't reach this balloon
                arrows += 1
                end = finish

        return arrows
```

**Complexity:** O(n log n)

---

### Problem 5: LC 253 - Meeting Rooms II

**Link:** [https://leetcode.com/problems/meeting-rooms-ii/](https://leetcode.com/problems/meeting-rooms-ii/) (Premium)

**Problem:** Minimum conference rooms needed.

**Pattern:** Sort by START + Min Heap

```python
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        heap = []  # End times

        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)
```

**Alternative: Line Sweep**

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))   # Meeting starts
            events.append((end, -1))    # Meeting ends

        events.sort()

        rooms = max_rooms = 0
        for time, delta in events:
            rooms += delta
            max_rooms = max(max_rooms, rooms)

        return max_rooms
```

**Complexity:** O(n log n)

---

### Problem 6: LC 252 - Meeting Rooms

**Link:** [https://leetcode.com/problems/meeting-rooms/](https://leetcode.com/problems/meeting-rooms/) (Premium)

**Problem:** Can one person attend all meetings?

**Pattern:** Sort by START, check for overlaps

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True
```

**Complexity:** O(n log n)

---

### Problem 7: LC 986 - Interval List Intersections

**Link:** [https://leetcode.com/problems/interval-list-intersections/](https://leetcode.com/problems/interval-list-intersections/)

**Problem:** Find intersections of two sorted interval lists.

**Pattern:** Two pointers (both lists already sorted)

```python
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            # Check for intersection
            start = max(a_start, b_start)
            end = min(a_end, b_end)

            if start <= end:
                result.append([start, end])

            # Move pointer with smaller end
            if a_end < b_end:
                i += 1
            else:
                j += 1

        return result
```

**Complexity:** O(m + n)

---

### Problem 8: LC 1288 - Remove Covered Intervals

**Link:** [https://leetcode.com/problems/remove-covered-intervals/](https://leetcode.com/problems/remove-covered-intervals/)

**Problem:** Remove intervals completely covered by another.

**Pattern:** Sort by start (asc), then end (desc)

**Key Insight:** Sort by start ascending, end descending. Then interval is covered if its end <= previous max end.

```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start ascending, then end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))

        remaining = 0
        max_end = 0

        for start, end in intervals:
            if end > max_end:  # Not covered
                remaining += 1
                max_end = end

        return remaining
```

**Complexity:** O(n log n)

---

### Problem 9: LC 759 - Employee Free Time

**Link:** [https://leetcode.com/problems/employee-free-time/](https://leetcode.com/problems/employee-free-time/) (Premium)

**Problem:** Find common free time for all employees.

**Pattern:** Merge all intervals, find gaps

```python
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flatten all intervals
        all_intervals = []
        for emp in schedule:
            for interval in emp:
                all_intervals.append([interval.start, interval.end])

        # Sort and merge
        all_intervals.sort()
        merged = [all_intervals[0]]

        for start, end in all_intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        # Find gaps
        result = []
        for i in range(1, len(merged)):
            result.append(Interval(merged[i-1][1], merged[i][0]))

        return result
```

**Complexity:** O(n log n) where n = total intervals

---

### Problem 10: LC 1272 - Remove Interval

**Link:** [https://leetcode.com/problems/remove-interval/](https://leetcode.com/problems/remove-interval/) (Premium)

**Problem:** Remove parts of intervals that overlap with toBeRemoved.

**Pattern:** Check each interval for overlap with removal range

```python
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        remove_start, remove_end = toBeRemoved

        for start, end in intervals:
            if end <= remove_start or start >= remove_end:
                # No overlap
                result.append([start, end])
            else:
                # Partial overlap - add non-overlapping parts
                if start < remove_start:
                    result.append([start, remove_start])
                if end > remove_end:
                    result.append([remove_end, end])

        return result
```

**Complexity:** O(n)

---

## Common Mistakes

1. **Wrong sorting key**
   - Sort by END for greedy selection (min arrows, max non-overlapping)
   - Sort by START for merging and processing in order

2. **Off-by-one with boundaries**
   - `start <= end` vs `start < end` for overlap
   - Touching intervals [1,2] and [2,3] - overlapping or not?

3. **Modifying intervals while iterating**
   - Make a copy or use separate result list

4. **Not handling edge cases**
   - Empty intervals list
   - Single interval
   - All intervals overlap

5. **Forgetting to sort**
   - Most interval algorithms assume sorted input

---

## Practice Checklist

- [ ] LC 56 - Merge Intervals (Basic merging)
- [ ] LC 57 - Insert Interval (Three-phase)
- [ ] LC 435 - Non-overlapping Intervals (Greedy removal)
- [ ] LC 452 - Minimum Arrows (Greedy coverage)
- [ ] LC 253 - Meeting Rooms II (Heap + sort)
- [ ] LC 252 - Meeting Rooms (Simple overlap check)
- [ ] LC 986 - Interval List Intersections (Two pointers)
- [ ] LC 1288 - Remove Covered Intervals (Clever sorting)
- [ ] LC 759 - Employee Free Time (Find gaps)
- [ ] LC 1272 - Remove Interval (Handle partial overlap)
