# Sliding Window

## Introduction

The Sliding Window pattern uses two pointers to define a "window" over a contiguous portion of an array or string. The window expands by moving the right pointer and shrinks by moving the left pointer. It transforms O(n²) brute force into O(n) by reusing computation from the previous window position.

## Pattern Recognition

Use this pattern when you see:
- "Contiguous subarray/substring"
- "Longest/shortest substring with condition"
- "Maximum/minimum in window of size k"
- "Subarray with sum equal to / at most / at least k"
- "At most K distinct characters"
- Keywords: "contiguous", "consecutive", "subarray", "substring"

---

## Base Templates

### Template 1: Fixed Size Window

```python
def fixed_window(arr, k):
    """
    Process all windows of exactly size k.
    """
    n = len(arr)
    window_sum = sum(arr[:k])  # Initialize first window
    result = window_sum

    for i in range(k, n):
        # Slide: remove left element, add right element
        window_sum += arr[i] - arr[i - k]
        result = max(result, window_sum)

    return result
```

### Template 2: Variable Window - Find Longest

```python
def longest_window(s, condition):
    """
    Find longest substring satisfying condition.
    Expand right, shrink left when condition violated.
    """
    left = 0
    max_length = 0
    window_state = {}  # Track window contents

    for right in range(len(s)):
        # Expand: add s[right] to window
        char = s[right]
        window_state[char] = window_state.get(char, 0) + 1

        # Shrink: while condition is violated
        while not condition(window_state):
            left_char = s[left]
            window_state[left_char] -= 1
            if window_state[left_char] == 0:
                del window_state[left_char]
            left += 1

        # Update result
        max_length = max(max_length, right - left + 1)

    return max_length
```

### Template 3: Variable Window - Find Shortest

```python
def shortest_window(s, target_condition):
    """
    Find shortest substring satisfying condition.
    Expand right until valid, then shrink left while still valid.
    """
    left = 0
    min_length = float('inf')
    window_state = {}

    for right in range(len(s)):
        # Expand: add s[right] to window
        char = s[right]
        window_state[char] = window_state.get(char, 0) + 1

        # Shrink: while condition is satisfied
        while is_valid(window_state, target_condition):
            min_length = min(min_length, right - left + 1)
            left_char = s[left]
            window_state[left_char] -= 1
            if window_state[left_char] == 0:
                del window_state[left_char]
            left += 1

    return min_length if min_length != float('inf') else 0
```

### Template 4: Count Subarrays/Substrings

```python
def count_subarrays(arr, condition):
    """
    Count all valid subarrays using "at most K" trick.
    Each valid window [left, right] contributes (right - left + 1) subarrays.
    """
    left = 0
    count = 0
    window_state = {}

    for right in range(len(arr)):
        # Expand
        window_state[arr[right]] = window_state.get(arr[right], 0) + 1

        # Shrink while invalid
        while not condition(window_state):
            window_state[arr[left]] -= 1
            if window_state[arr[left]] == 0:
                del window_state[arr[left]]
            left += 1

        # Count: all subarrays ending at right
        count += right - left + 1

    return count
```

---

## Key Insights

### When to Expand vs Shrink

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   EXPAND (move right pointer):                                     │
│   • Always expand in outer loop                                    │
│   • Add new element to window state                                │
│                                                                     │
│   SHRINK (move left pointer):                                      │
│   • When window is INVALID → shrink until valid (for LONGEST)     │
│   • When window is VALID → shrink while valid (for SHORTEST)      │
│                                                                     │
│   LONGEST: Keep window as large as possible while valid           │
│   SHORTEST: Find minimum valid window                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Counting Subarrays Trick

```
"Exactly K" = "At Most K" - "At Most K-1"

Example: Count subarrays with exactly 3 distinct elements
= count_at_most(3) - count_at_most(2)

At Most K: Each window [left, right] contributes (right - left + 1) subarrays
```

### Window State Options

| Problem Type | Window State |
|--------------|-------------|
| Character frequency | `dict` or `Counter` |
| Sum of elements | Single variable |
| Distinct count | `len(dict)` |
| Maximum in window | Monotonic deque |

---

## LeetCode Problems

### Problem 1: LC 3 - Longest Substring Without Repeating Characters

**Link:** [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

**Problem:** Find length of longest substring without repeating characters.

**Pattern:** Variable window - shrink when duplicate found

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # char -> last seen index
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # If char in window, shrink to exclude previous occurrence
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
```

**Alternative with set:**

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            while char in window:
                window.remove(s[left])
                left += 1

            window.add(char)
            max_length = max(max_length, right - left + 1)

        return max_length
```

**Complexity:** O(n)

---

### Problem 2: LC 76 - Minimum Window Substring

**Link:** [https://leetcode.com/problems/minimum-window-substring/](https://leetcode.com/problems/minimum-window-substring/)

**Problem:** Find smallest substring containing all characters of target.

**Pattern:** Variable window - find shortest valid

```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        target_count = Counter(t)
        required = len(target_count)
        formed = 0

        window_count = {}
        left = 0
        min_len = float('inf')
        min_start = 0

        for right, char in enumerate(s):
            # Expand
            window_count[char] = window_count.get(char, 0) + 1

            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            # Shrink while valid
            while formed == required:
                # Update result
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # Remove left char
                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    formed -= 1

                left += 1

        return s[min_start:min_start + min_len] if min_len != float('inf') else ""
```

**Complexity:** O(m + n)

---

### Problem 3: LC 424 - Longest Repeating Character Replacement

**Link:** [https://leetcode.com/problems/longest-repeating-character-replacement/](https://leetcode.com/problems/longest-repeating-character-replacement/)

**Problem:** Longest substring with at most k character replacements.

**Pattern:** Variable window - shrink when replacements > k

**Key Insight:** Window is valid if (window size - max frequency) <= k

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            max_freq = max(max_freq, count[char])

            # Shrink if too many replacements needed
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
```

**Complexity:** O(n)

---

### Problem 4: LC 567 - Permutation in String

**Link:** [https://leetcode.com/problems/permutation-in-string/](https://leetcode.com/problems/permutation-in-string/)

**Problem:** Check if s1's permutation is substring of s2.

**Pattern:** Fixed window of size len(s1)

```python
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if window_count == s1_count:
            return True

        for i in range(len(s1), len(s2)):
            # Add new char
            window_count[s2[i]] += 1

            # Remove old char
            old_char = s2[i - len(s1)]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]

            if window_count == s1_count:
                return True

        return False
```

**Complexity:** O(n)

---

### Problem 5: LC 1004 - Max Consecutive Ones III

**Link:** [https://leetcode.com/problems/max-consecutive-ones-iii/](https://leetcode.com/problems/max-consecutive-ones-iii/)

**Problem:** Longest subarray of 1s with at most k flips.

**Pattern:** Variable window - shrink when zeros > k

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
```

**Complexity:** O(n)

---

### Problem 6: LC 209 - Minimum Size Subarray Sum

**Link:** [https://leetcode.com/problems/minimum-size-subarray-sum/](https://leetcode.com/problems/minimum-size-subarray-sum/)

**Problem:** Find shortest subarray with sum >= target.

**Pattern:** Variable window - find shortest valid

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink while valid
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
```

**Complexity:** O(n)

---

### Problem 7: LC 992 - Subarrays with K Different Integers

**Link:** [https://leetcode.com/problems/subarrays-with-k-different-integers/](https://leetcode.com/problems/subarrays-with-k-different-integers/)

**Problem:** Count subarrays with exactly K distinct integers.

**Pattern:** "Exactly K" = "At Most K" - "At Most K-1"

```python
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(k):
            count = {}
            left = 0
            result = 0

            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1

                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1

                result += right - left + 1

            return result

        return at_most_k(k) - at_most_k(k - 1)
```

**Complexity:** O(n)

---

### Problem 8: LC 438 - Find All Anagrams in a String

**Link:** [https://leetcode.com/problems/find-all-anagrams-in-a-string/](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

**Problem:** Find start indices of all anagrams of p in s.

**Pattern:** Fixed window of size len(p)

```python
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window_count = Counter(s[:len(p) - 1])
        result = []

        for i in range(len(p) - 1, len(s)):
            # Add new char
            window_count[s[i]] += 1

            if window_count == p_count:
                result.append(i - len(p) + 1)

            # Remove old char
            old_char = s[i - len(p) + 1]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]

        return result
```

**Complexity:** O(n)

---

### Problem 9: LC 239 - Sliding Window Maximum

**Link:** [https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

**Problem:** Maximum of each sliding window of size k.

**Pattern:** Fixed window + Monotonic Deque

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Store indices, values are decreasing
        result = []

        for i, num in enumerate(nums):
            # Remove elements outside window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements (they can't be max)
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            # Window is full, record max
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
```

**Complexity:** O(n)

---

### Problem 10: LC 340 - Longest Substring with At Most K Distinct Characters

**Link:** [https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) (Premium)

**Problem:** Longest substring with at most k distinct characters.

**Pattern:** Variable window - shrink when distinct > k

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1

            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
```

**Complexity:** O(n)

---

## Common Mistakes

1. **Forgetting to update window state when shrinking**
   - Must remove left element before moving left pointer

2. **Off-by-one with window size**
   - Window size = `right - left + 1`

3. **Not deleting zero-count entries**
   - Can affect `len(dict)` calculations

4. **Using wrong template for longest vs shortest**
   - Longest: shrink while invalid
   - Shortest: shrink while valid

5. **Forgetting edge cases**
   - Empty string
   - K = 0
   - String shorter than required

---

## Practice Checklist

- [ ] LC 3 - Longest Substring Without Repeating (Classic)
- [ ] LC 76 - Minimum Window Substring (Shortest valid)
- [ ] LC 424 - Longest Repeating Character Replacement (k changes)
- [ ] LC 567 - Permutation in String (Fixed window)
- [ ] LC 1004 - Max Consecutive Ones III (k flips)
- [ ] LC 209 - Minimum Size Subarray Sum (Shortest sum)
- [ ] LC 992 - Subarrays with K Distinct (Count with trick)
- [ ] LC 438 - Find All Anagrams (Fixed window matching)
- [ ] LC 239 - Sliding Window Maximum (Monotonic deque)
- [ ] LC 340 - At Most K Distinct Characters (Variable window)
