# 394. Decode String

**Difficulty:** Medium
**Pattern:** Stack (Parsing / Nested Structures)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. `k` is guaranteed to be a positive integer. You may assume the input string is always valid.

**Interview Scenario (The "Compression Format" Prompt):**
"You are writing a decompressor for a custom file format used in a legacy graphics system. The format uses a run-length encoding variant where patterns are enclosed in brackets and preceded by a repetition count (e.g., `3[a2[c]]` -> `accaccacc`). The nesting can be arbitrarily deep. Write a parser to expand this format into the full raw data stream."

**Why this transformation?**
*   It frames the problem as a **parsing** task.
*   It highlights the **nesting** aspect, which immediately suggests recursion or a stack.

---

## 2. Clarifying Questions (Phase 1)

1.  **Multi-digit Numbers:** "Can the multiplier `k` have multiple digits (e.g., `10[a]`)?" (Yes, logic must parse full integers).
2.  **Empty Brackets:** "Is `3[]` valid?" (Assume valid input, usually not a test case but good to handle).
3.  **Characters:** "Are there any other special characters besides digits, brackets, and letters?" (No).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Stack.

**Why Stack?**
We process the string from left to right. When we see a `[`, we are entering a new "context" (a nested substring). We need to remember the "multiplier" and the "current string so far" before we enter this new context. When we see `]`, we are finishing the current context and need to "pop" back to the previous context, combining the results. This LIFO (Last-In-First-Out) behavior is perfect for a stack.

**Logic:**
Maintain `current_string` and `current_num`.
*   **Digit:** Update `current_num` (`num = num * 10 + digit`).
*   **'[':** Push `(current_string, current_num)` onto the stack. Reset `current_string` and `current_num` for the inner scope.
*   **']':** Pop `(prev_string, repeat_count)` from stack. Update `current_string = prev_string + repeat_count * current_string`.
*   **Letter:** Append to `current_string`.

---

## 4. Base Template & Modification

**Standard Stack Parsing Template:**
```python
stack = []
curr = ...
for char in s:
    if char is open_bracket:
        stack.append(curr)
        curr = reset()
    elif char is close_bracket:
        prev = stack.pop()
        curr = combine(prev, curr)
    else:
        update(curr)
```

**Modified Logic:**
Handle multi-digit parsing specifically.

---

## 5. Optimal Solution

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the number (could be multi-digit)
                current_num = current_num * 10 + int(char)
                
            elif char == '[':
                # Enter new scope: Push context (string built so far, multiplier for NEXT scope)
                stack.append((current_string, current_num))
                
                # Reset for the new scope
                current_string = ""
                current_num = 0
                
            elif char == ']':
                # Exit scope: Retrieve context
                prev_string, repeat_count = stack.pop()
                
                # Combine: old string + (new string * count)
                current_string = prev_string + (current_string * repeat_count)
                
            else:
                # Regular character, just add to current scope
                current_string += char
                
        return current_string
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(\text{maxK} \times N)$ or length of output.
    *   Ideally linear with respect to the *output* size. If the output is massive (e.g., `100[a]`), we construct that string. In terms of input `N`, it's not strictly linear because of the expansion.
*   **Space Complexity:** $O(N)$
    *   Stack depth depends on the nesting level.

---

## 7. Follow-up & Extensions

**Q: Recursive Solution?**
**A:** We can pass an index reference (or iterator) to a recursive function.
*   `decode(index)`:
    *   Parse loop.
    *   Recurse on `[`.
    *   Return string and new index on `]`.

**Q: What if the string is very large and we only want the k-th character of the decoded string?**
**A:** (LeetCode 880: Decoded String at Index). Do NOT decode the whole string. Calculate the *size* of the decoded string first, then work backwards modulo the size to find the character.

```
