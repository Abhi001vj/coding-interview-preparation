# 3. Longest Substring Without Repeating Characters
**Difficulty:** Medium | **Pattern:** Sliding Window (Variable Size) | **Companies:** Google, Meta, Amazon, Microsoft

---

## 1. Google/Meta Style Question Transformation

### Original LeetCode Problem:
Given a string `s`, find the length of the longest substring without repeating characters.

### Google Scenario Wrapper:
> "At Google Search, we're analyzing user query patterns. Given a stream of keystrokes, find the longest sequence of unique characters typed without repetition. This helps identify optimal autocomplete suggestion lengths."

### Meta Constraint Twist:
> Same problem but: "Return the actual substring, not just its length. If multiple substrings have the same max length, return the lexicographically smallest one."

---

## 2. Clarifying Questions (Ask in Interview!)

Before coding, always clarify:

1. **Input Constraints:**
   - What characters can the string contain? (ASCII? Unicode? Only lowercase?)
   - What's the max length of input? (0 ≤ s.length ≤ 5 × 10⁴)
   - Can the string be empty? → Yes, return 0

2. **Edge Cases:**
   - Empty string → return 0
   - Single character → return 1
   - All same characters "aaaa" → return 1
   - All unique characters "abcd" → return 4

3. **Output Requirements:**
   - Return length (integer), not the substring itself
   - No need to return starting index

---

## 3. Pattern Recognition

### Why Sliding Window?
- **Key Signal 1:** "Longest substring" → Looking for contiguous sequence
- **Key Signal 2:** "Without repeating" → Need to track what's in current window
- **Key Signal 3:** We can expand/shrink window based on condition

### Pattern Match:
| Problem Feature | Pattern Indicator |
|-----------------|-------------------|
| "Longest substring" | Variable-size sliding window |
| "Without repeating characters" | Need HashSet/HashMap to track window contents |
| Contiguous elements | Sliding window, not subsequence |
| Maximize length | Expand window when valid, shrink when invalid |

### Pattern Type: **Flexible Sliding Window (shrink when invalid)**

---

## 4. Approach Discussion

### Approach 1: Brute Force - O(n³) / O(min(n, m))
**Intuition:** Check all substrings, verify each has unique characters.

**Steps:**
1. Generate all substrings O(n²)
2. For each, check if all characters unique O(n)
3. Track maximum length

**Pros:** Simple to understand
**Cons:** TLE for large inputs, extremely inefficient

### Approach 2: Sliding Window with Set - O(n) / O(min(n, m))
**Intuition:** Expand window right, shrink left when duplicate found.

**Steps:**
1. Use HashSet to track characters in current window
2. Expand right pointer, add character
3. If duplicate, shrink left until no duplicate
4. Update max length

**Pros:** Linear time, intuitive
**Cons:** Slightly more operations than optimal

### Approach 3: Sliding Window with HashMap (Optimal) - O(n) / O(min(n, m))
**Intuition:** Jump left pointer directly to position after last occurrence of duplicate.

**Steps:**
1. Use HashMap to store character → last seen index
2. When duplicate found, jump left to max(left, last_seen + 1)
3. Update max length at each step

**Pros:** Single pass, no inner while loop
**Cons:** Slightly more complex logic

---

## 5. Base Template

```python
# Base Template: Flexible Sliding Window (Variable Size)
def sliding_window_flexible(s):
    """
    Template for finding longest/shortest subarray/substring
    satisfying some condition.

    Key insight:
    - Expand right to explore
    - Contract left to maintain validity
    """
    left = 0
    result = 0  # or float('inf') for minimum
    window_state = {}  # Track window contents

    for right in range(len(s)):
        # 1. Add s[right] to window state
        char = s[right]
        window_state[char] = window_state.get(char, 0) + 1

        # 2. Shrink window while invalid
        while window_is_invalid(window_state):
            # Remove s[left] from window state
            left_char = s[left]
            window_state[left_char] -= 1
            if window_state[left_char] == 0:
                del window_state[left_char]
            left += 1

        # 3. Update result (window is now valid)
        result = max(result, right - left + 1)

    return result
```

---

## 6. Solution - How We Modify the Template

### Template Modification Needed:
- **What changes:** "Window invalid" = any character appears more than once
- **Optimization:** Use HashMap with index instead of count to jump left pointer directly

### Solution 1: Sliding Window with Set (Easier to understand)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window with HashSet.

        Expand right, shrink left when duplicate found.

        Time: O(n) - each character visited at most twice
        Space: O(min(n, m)) where m is charset size
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Shrink window while current char is duplicate
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add current char to window
            char_set.add(s[right])

            # Update max length
            max_length = max(max_length, right - left + 1)

        return max_length
```

### Solution 2: Sliding Window with HashMap (Optimal)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Optimized sliding window - jump left pointer directly.

        Instead of shrinking one by one, jump left to
        position after last occurrence of duplicate char.

        Time: O(n) - single pass
        Space: O(min(n, m)) where m is charset size
        """
        char_index = {}  # char -> last seen index
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            # If char seen before AND is within current window
            if char in char_index and char_index[char] >= left:
                # Jump left to position after last occurrence
                left = char_index[char] + 1

            # Update last seen index for current char
            char_index[char] = right

            # Update max length
            max_length = max(max_length, right - left + 1)

        return max_length
```

### Visual Walkthrough for "abcabcbb":

```
Step 1: "a"
        left=0, right=0
        char_index = {'a': 0}
        window = "a", length = 1
        max_length = 1

Step 2: "ab"
        left=0, right=1
        char_index = {'a': 0, 'b': 1}
        window = "ab", length = 2
        max_length = 2

Step 3: "abc"
        left=0, right=2
        char_index = {'a': 0, 'b': 1, 'c': 2}
        window = "abc", length = 3
        max_length = 3

Step 4: "abca" → 'a' is duplicate!
        'a' was at index 0, so left = 0 + 1 = 1
        left=1, right=3
        char_index = {'a': 3, 'b': 1, 'c': 2}
        window = "bca", length = 3
        max_length = 3

Step 5: "bcab" → 'b' is duplicate!
        'b' was at index 1, so left = 1 + 1 = 2
        left=2, right=4
        char_index = {'a': 3, 'b': 4, 'c': 2}
        window = "cab", length = 3
        max_length = 3

Step 6: "abc" → 'c' is duplicate!
        'c' was at index 2, so left = 2 + 1 = 3
        left=3, right=5
        char_index = {'a': 3, 'b': 5, 'c': 5}
        window = "abc", length = 3
        max_length = 3

Step 7: "cb" → 'b' is duplicate!
        'b' was at index 5, so left = 5 + 1 = 6
        left=6, right=6
        char_index = {'a': 3, 'b': 6, 'c': 5}
        window = "b", length = 1
        max_length = 3

Step 8: "bb" → 'b' is duplicate!
        'b' was at index 6, so left = 6 + 1 = 7
        left=7, right=7
        char_index = {'a': 3, 'b': 7, 'c': 5}
        window = "b", length = 1
        max_length = 3

Final Answer: 3
```

---

## 7. Complexity Analysis

### Time Complexity: O(n)
- **Solution 1 (Set):** Each character is added once and removed at most once → O(2n) = O(n)
- **Solution 2 (HashMap):** Single pass, each character processed once → O(n)

### Space Complexity: O(min(n, m))
- Where n = string length, m = size of character set
- For ASCII: O(128) = O(1)
- For Unicode: O(n) worst case
- HashMap/Set stores at most min(n, m) characters

### Why This is Optimal:
- Must read every character at least once → Ω(n) lower bound
- Our solution achieves O(n) → optimal

---

## 8. Test Cases & Edge Cases

```python
# Test Case 1: Basic example
Input: "abcabcbb"
Expected: 3
Trace: "abc" is longest substring without repeating

# Test Case 2: All same characters
Input: "bbbbb"
Expected: 1
Trace: Each 'b' is duplicate, window always size 1

# Test Case 3: No repeating at all
Input: "pwwkew"
Expected: 3
Trace: "wke" or "kew" - both length 3

# Test Case 4: Empty string
Input: ""
Expected: 0
Trace: No characters, return 0

# Test Case 5: Single character
Input: "a"
Expected: 1

# Test Case 6: Two characters alternating
Input: "abababab"
Expected: 2
Trace: "ab" repeats, max unique is 2

# Test Case 7: Space and special characters
Input: "a b c"
Expected: 3
Trace: "a b" or " b " or "b c" - space counts as character
```

---

## 9. Common Mistakes to Avoid

1. **Forgetting the `>= left` check in HashMap solution:**
   ```python
   # WRONG - doesn't check if char is in current window
   if char in char_index:
       left = char_index[char] + 1

   # CORRECT - only jump if char is within current window
   if char in char_index and char_index[char] >= left:
       left = char_index[char] + 1
   ```

2. **Off-by-one error in window length:**
   ```python
   # WRONG
   max_length = max(max_length, right - left)

   # CORRECT (window is inclusive on both ends)
   max_length = max(max_length, right - left + 1)
   ```

3. **Removing wrong character in Set solution:**
   ```python
   # WRONG - removing current char instead of left char
   while s[right] in char_set:
       char_set.remove(s[right])  # Should be s[left]!
   ```

4. **Not updating HashMap after duplicate handling:**
   ```python
   # Must ALWAYS update char_index[char] = right
   # Even after finding duplicate
   ```

---

## 10. Follow-up Questions

### Follow-up 1: "Return the actual substring, not just length"
**Answer:** Track `start` index when updating `max_length`, return `s[start:start+max_length]`
```python
if right - left + 1 > max_length:
    max_length = right - left + 1
    start = left
return s[start:start + max_length]
```

### Follow-up 2: "What if we want at most K repeating characters?"
**Answer:** Change condition to use count map instead of set
```python
# Count occurrences, shrink when any char count > K
while any(count > K for count in char_count.values()):
    left_char = s[left]
    char_count[left_char] -= 1
    left += 1
```

### Follow-up 3: "What if string is streaming (infinite)?"
**Answer:** Same algorithm works! Just process character by character, don't need entire string upfront. HashMap stores only current window contents.

### Follow-up 4: "Optimize for very small charset (e.g., only 'a'-'z')?"
**Answer:** Use fixed-size array instead of HashMap
```python
char_index = [-1] * 26  # For 'a'-'z'
# Access: char_index[ord(c) - ord('a')]
```

### Related Problems:
- LC 159 - Longest Substring with At Most Two Distinct Characters (Similar, limit distinct chars)
- LC 340 - Longest Substring with At Most K Distinct Characters (Generalization)
- LC 424 - Longest Repeating Character Replacement (Sliding window + different condition)
- LC 76 - Minimum Window Substring (Harder, find minimum window containing all target chars)

---

## 11. Interview Tips

- **Time Target:** 15-20 minutes for this medium problem
- **Communication Points:**
  - "I see this is asking for longest substring - that signals sliding window"
  - "Without repeating means I need to track what's in my current window"
  - "I'll use a HashSet/HashMap to check for duplicates in O(1)"
  - "Let me trace through an example before coding..."
- **Red Flags to Avoid:**
  - Jumping into brute force O(n³) without discussing optimization
  - Not clarifying what "substring" means (contiguous vs subsequence)
  - Forgetting to handle empty string edge case
