# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Pattern:** Sliding Window / Hash Set (or Hash Map)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given a string `s`, find the length of the longest substring without repeating characters.

**Interview Scenario (The "Unique Identifier" Prompt):**
"You are analyzing a data stream that consists of a sequence of characters. You need to identify the longest contiguous segment of this stream where all characters are unique (e.g., in a sequence 'abacaba', 'bac' is a candidate). This is useful for identifying unique patterns or valid identifiers in a log. What is the length of this longest segment?"

**Why this transformation?**
*   It provides a practical context for identifying unique sequences.
*   It emphasizes the "contiguous" nature of substrings and the "unique characters" constraint.

---

## 2. Clarifying Questions (Phase 1)

1.  **Empty String:** "What if the input string is empty?" (Return 0).
2.  **Character Set:** "Are we dealing with ASCII, Unicode, or a limited alphabet?" (Usually ASCII for simplicity, but a `dict` or `set` handles any character type).
3.  **Case Sensitivity:** "Is `A` the same as `a`?" (Usually case-sensitive unless specified).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Sliding Window (Variable Size).

**The Logic:**
We want to find the longest subarray (window) that contains all unique characters.

1.  Use two pointers, `left` and `right`, to define the current window `[left, right]`.
2.  Use a `HashSet` (or `HashMap` to store character counts) to keep track of characters within the current window.
3.  Expand the window with `right`:
    *   Add `s[right]` to the `HashSet`.
4.  Shrink the window with `left`:
    *   If `s[right]` is *already* in the `HashSet`, it means we have a duplicate. We must shrink the window from the `left` until the duplicate is removed.
    *   Remove `s[left]` from the `HashSet`.
    *   Increment `left`.
5.  At each valid window (all characters unique), update `max_length = max(max_length, right - left + 1)`.

---

## 4. Base Template & Modification

**Standard Sliding Window Template (Variable Size, based on duplicate detection):**
```python
left = 0
max_len = 0
window_set = set()
for right in range(len(s)):
    while s[right] in window_set:
        window_set.remove(s[left])
        left += 1
    window_set.add(s[right])
    max_len = max(max_len, right - left + 1)
```

**Modified Logic:** None, this is the canonical template for this problem.

---

## 5. Optimal Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        # `char_set` stores characters currently within the sliding window
        char_set = set()
        max_length = 0
        left = 0 # Left pointer of the sliding window
        
        # Iterate with the right pointer to expand the window
        for right in range(len(s)):
            # If the character at `right` is already in the set,
            # it means we have a duplicate. We need to shrink the window from the left.
            while s[right] in char_set:
                # Remove the character at `left` from the set
                char_set.remove(s[left])
                
                left += 1 # Shrink window from the left
            
            # Add the current character at `right` to the set
            char_set.add(s[right])
            
            # At this point, the window [left, right] contains all unique characters.
            # Calculate the current window size and update max_length.
            max_length = max(max_length, right - left + 1)
            
        return max_length
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   Both `left` and `right` pointers traverse the array at most once.
    *   Hash set operations (add, remove, check `in`) take $O(1)$ on average.
*   **Space Complexity:** $O(K)$ where $K$ is the size of the character set (e.g., 26 for English lowercase, 128 for ASCII, 256 for extended ASCII).
    *   In the worst case (all unique characters), the set can store up to `N` characters. But practically, it's bounded by the alphabet size.

---

## 7. Follow-up & Extensions

**Q: Return the actual substring, not just the length.**
**A:** Track `start_index` and `end_index` along with `max_length`. When `max_length` is updated, also update `start_index` to `left` and `end_index` to `right`.

**Q: What if we needed to handle characters outside ASCII (e.g., Unicode)?**
**A:** The `set` (or `dict`) approach works universally for any hashable character.
