# Sliding Window Pattern

**Core Concept:** Use a dynamic window `[left, right]` to satisfy a constraint.
- **Expand (Right):** Include new elements to reach a valid state or maximize a value.
- **Shrink (Left):** Remove old elements to restore validity (if broken) or minimize window size.

---

## 🛑 The "FAANG" Template (Memorize This)

```python
def sliding_window(s):
    # 1. Initialize State
    left = 0
    window_state = {} # e.g., Counter, sum, or unique set
    best_result = 0 # or float('inf') for minimization

    # 2. Expand Window (Right Pointer)
    for right in range(len(s)):
        char = s[right]
        # Update State: Add s[right]
        # window_state.add(char) ...

        # 3. Shrink Window (Left Pointer) - WHILE invalid
        while not is_valid(window_state):
            remove_char = s[left]
            # Update State: Remove s[left]
            # window_state.remove(remove_char) ...
            left += 1

        # 4. Update Result (After restoring validity)
        best_result = max(best_result, right - left + 1)
    
    return best_result
```

## 🎯 Key Variations

1.  **Longest Valid Subarray:** `max(ans, R - L + 1)` **after** the `while` loop.
    *   *Example:* Longest Substring Without Repeating Characters (LC 3).
2.  **Shortest Valid Subarray:** `min(ans, R - L + 1)` **inside** the `while` loop (because that's when it's valid!).
    *   *Example:* Minimum Window Substring (LC 76).
3.  **Fixed Size Window:** No `while` loop. Just `if right >= k - 1: left += 1`.
    *   *Example:* Find All Anagrams (LC 438).
