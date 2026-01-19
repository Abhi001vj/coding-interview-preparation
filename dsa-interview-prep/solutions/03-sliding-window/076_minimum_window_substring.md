# 76. Minimum Window Substring
**Difficulty:** Hard | **Pattern:** Sliding Window (Variable Size - Find Minimum) | **Companies:** Google, Meta, Amazon, Microsoft

---

## 1. Google/Meta Style Question Transformation

### Original LeetCode Problem:
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If no such substring exists, return empty string.

### Google Scenario Wrapper:
> "At Google Docs, users can search for text containing all specified keywords. Given a document `s` and required characters `t`, find the shortest passage in the document that contains all required characters. This powers our 'find all terms' feature."

### Meta Constraint Twist:
> Same problem but: "If multiple windows have the same minimum length, return the one that appears first. Also, track and return the count of ALL minimum windows found."

---

## 2. Clarifying Questions (Ask in Interview!)

1. **Input Constraints:**
   - Can `t` be longer than `s`? → Yes, return ""
   - Can `t` be empty? → Technically yes, return ""
   - Are characters case-sensitive? → Yes, 'A' ≠ 'a'
   - What characters? → Uppercase and lowercase English letters

2. **Edge Cases:**
   - `t` not fully contained in `s` → return ""
   - `t` has duplicates like "AA" → window must have 2 A's
   - `s` equals `t` → return `s`
   - Single character match

3. **Output Requirements:**
   - Return the actual substring, not indices
   - Return "" if no valid window exists

---

## 3. Pattern Recognition

### Why Sliding Window?
- **Key Signal 1:** "Minimum window/substring" → Sliding window for contiguous elements
- **Key Signal 2:** "Contains all characters of t" → Track character counts
- **Key Signal 3:** Need to find **shortest** valid window → Shrink when valid

### Pattern Match:
| Problem Feature | Pattern Indicator |
|-----------------|-------------------|
| "Minimum substring" | Variable-size sliding window (minimize) |
| "Contains all of t" | Need two frequency maps to compare |
| Want shortest | Shrink window while still valid |

### Pattern Type: **Flexible Sliding Window (shrink when valid to minimize)**

---

## 4. Approach Discussion

### Approach 1: Brute Force - O(n² × m)
**Intuition:** Check all substrings starting from each position.

**Steps:**
1. For each starting position, expand until valid
2. Track minimum window found
3. Move to next starting position

**Cons:** TLE, doesn't reuse information

### Approach 2: Optimized Sliding Window - O(n + m)
**Intuition:** Expand right to find valid window, then shrink left to minimize.

**Steps:**
1. Build frequency map for `t`
2. Expand `right` pointer, update window counts
3. When window contains all of `t`, try shrinking `left`
4. Track minimum valid window

---

## 5. Base Template

```python
# Base Template: Find MINIMUM window satisfying condition
def sliding_window_minimum(s, condition):
    """
    Template for finding MINIMUM window satisfying condition.

    Key insight:
    - Expand right to FIND valid window
    - Contract left to MINIMIZE while still valid
    """
    from collections import Counter

    left = 0
    min_len = float('inf')
    min_start = 0

    # Track window state
    need = Counter(t)  # What we need
    have = Counter()   # What we have in window
    formed = 0         # How many unique chars satisfied

    for right in range(len(s)):
        # 1. Add s[right] to window
        char = s[right]
        have[char] += 1

        # 2. Check if this char's requirement is now satisfied
        if char in need and have[char] == need[char]:
            formed += 1

        # 3. Shrink window while VALID (to find minimum)
        while formed == len(need):
            # Update result if this window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            # Remove s[left] from window
            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return s[min_start:min_start + min_len] if min_len != float('inf') else ""
```

---

## 6. Solution - How We Modify the Template

### Template Modification Needed:
- **What changes:** Track "formed" count to know when window is valid
- **Key insight:** Compare counts only when they become equal (not every increment)

### Solution (Optimal)

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Sliding window with character frequency tracking.

        Key insight: Track how many unique characters
        have their required count satisfied.

        Time: O(|s| + |t|)
        Space: O(|s| + |t|) for frequency maps
        """
        if not t or not s:
            return ""

        from collections import Counter

        # Build frequency map for t
        need = Counter(t)
        required = len(need)  # Number of unique chars in t

        # Window state
        have = {}
        formed = 0  # Unique chars in window with required count

        # Result tracking
        min_len = float('inf')
        result = (0, 0)  # (start, end) of result window

        left = 0

        for right in range(len(s)):
            # Add character from the right
            char = s[right]
            have[char] = have.get(char, 0) + 1

            # Check if current char's count matches required
            if char in need and have[char] == need[char]:
                formed += 1

            # Try to shrink window while it's valid
            while left <= right and formed == required:
                char = s[left]

                # Save smallest window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = (left, right + 1)

                # Remove from left
                have[char] -= 1
                if char in need and have[char] < need[char]:
                    formed -= 1

                left += 1

        return "" if min_len == float('inf') else s[result[0]:result[1]]
```

### Visual Walkthrough for s="ADOBECODEBANC", t="ABC":

```
need = {'A': 1, 'B': 1, 'C': 1}, required = 3

Step-by-step:
right=0: 'A' → have={'A':1}, formed=1 (A satisfied)
right=1: 'D' → have={'A':1,'D':1}, formed=1
right=2: 'O' → have={'A':1,'D':1,'O':1}, formed=1
right=3: 'B' → have={'A':1,'D':1,'O':1,'B':1}, formed=2 (B satisfied)
right=4: 'E' → have={'A':1,'D':1,'O':1,'B':1,'E':1}, formed=2
right=5: 'C' → have={'A':1,'D':1,'O':1,'B':1,'E':1,'C':1}, formed=3 ✓ VALID!

  Now shrink:
  Window "ADOBEC" (len=6), save as result
  Remove 'A' → formed=2, left=1, window invalid

right=6: 'O' → formed=2
right=7: 'D' → formed=2
right=8: 'E' → formed=2
right=9: 'B' → have['B']=2, formed=2 (already satisfied)
right=10: 'A' → have['A']=2, formed=3 ✓ VALID!

  Now shrink:
  Window "DOBECODEBA" (len=10) - not smaller, skip
  Remove 'D' → still valid
  Window "OBECODEBA" (len=9) - not smaller
  Remove 'O' → still valid
  ...continue shrinking...
  Window "CODEBA" (len=6) - same as best
  Remove 'C' → formed=2, invalid

right=11: 'N' → formed=2
right=12: 'C' → have['C']=2, formed=3 ✓ VALID!

  Now shrink:
  Window "EBANC" (len=5) - SMALLER! Save as result
  Remove 'E' → still valid
  Window "BANC" (len=4) - SMALLER! Save as result
  Remove 'B' → formed=2, invalid

Final result: "BANC"
```

---

## 7. Complexity Analysis

### Time Complexity: O(|s| + |t|)
- Building `need` map: O(|t|)
- Each character in `s` is visited at most twice (once by `right`, once by `left`)
- Total: O(|s|) for sliding window
- Overall: O(|s| + |t|)

### Space Complexity: O(|s| + |t|)
- `need` map: O(|t|) - but bounded by character set (26 for lowercase)
- `have` map: O(|s|) worst case
- In practice: O(52) for English letters = O(1)

---

## 8. Test Cases & Edge Cases

```python
# Test Case 1: Basic example
Input: s = "ADOBECODEBANC", t = "ABC"
Expected: "BANC"

# Test Case 2: Exact match
Input: s = "a", t = "a"
Expected: "a"

# Test Case 3: No valid window
Input: s = "a", t = "aa"
Expected: ""
Trace: Need 2 'a's but only have 1

# Test Case 4: t has duplicates
Input: s = "aa", t = "aa"
Expected: "aa"

# Test Case 5: Multiple valid windows
Input: s = "ABAACBAB", t = "ABC"
Expected: "ACB" (first minimum window)

# Test Case 6: t is entire s
Input: s = "ABC", t = "ABC"
Expected: "ABC"
```

---

## 9. Common Mistakes to Avoid

1. **Using `formed == len(t)` instead of `formed == len(need)`:**
   ```python
   # WRONG - counts total chars including duplicates
   while formed == len(t):

   # CORRECT - counts unique chars satisfied
   while formed == required:  # required = len(need)
   ```

2. **Incrementing `formed` every time count increases:**
   ```python
   # WRONG
   if char in need:
       have[char] += 1
       formed += 1  # Wrong! Only when count MATCHES

   # CORRECT
   if char in need and have[char] == need[char]:
       formed += 1  # Only when exactly matching required count
   ```

3. **Off-by-one in result slicing:**
   ```python
   # WRONG
   result = s[start:end]  # If end is right pointer

   # CORRECT
   result = s[start:end+1]  # Or store (start, end+1)
   ```

4. **Forgetting to handle empty input:**
   ```python
   if not t or not s:
       return ""
   ```

---

## 10. Follow-up Questions

### Follow-up 1: "What if we need to return all minimum windows?"
**Answer:** Don't return early, collect all windows with minimum length
```python
if right - left + 1 == min_len:
    results.append(s[left:right+1])
elif right - left + 1 < min_len:
    min_len = right - left + 1
    results = [s[left:right+1]]
```

### Follow-up 2: "What if t can have wildcards?"
**Answer:** Treat wildcard as "match any character" - skip the character check for wildcards in `need`

### Follow-up 3: "Optimize for very long s with small t"
**Answer:** Filter s to only relevant positions (indices where s[i] is in t)
```python
# Create filtered list of (index, char) for relevant chars only
filtered = [(i, c) for i, c in enumerate(s) if c in need]
# Apply sliding window on filtered list
```

### Related Problems:
- LC 3 - Longest Substring Without Repeating (Sliding window - maximize)
- LC 438 - Find All Anagrams in a String (Fixed window with char counts)
- LC 567 - Permutation in String (Fixed window matching)
- LC 30 - Substring with Concatenation of All Words (Harder - word-level matching)

---

## 11. Interview Tips

- **Time Target:** 25-30 minutes for this hard problem
- **Communication Points:**
  - "This is a minimum window problem - I'll use sliding window"
  - "I need to track how many characters are satisfied"
  - "Key insight: only check when count EQUALS required, not every increment"
  - "Shrink while valid to find minimum"
- **Red Flags to Avoid:**
  - Comparing entire frequency maps at each step (O(26) overhead)
  - Not handling duplicate characters in `t`
  - Returning wrong indices/substring
