# 7. Reverse Integer

**Difficulty:** Medium
**Pattern:** Math / Digit Extraction

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range $[-2^{31}, 2^{31} - 1]$, then return 0.

**Interview Scenario (The "Constraint" Prompt):**
"Design a function for a legacy banking system or a microcontroller display driver. The system receives a numeric value, but due to an endianness or display driver bug, the digits need to be processed in reverse order. However, the hardware registers are strictly 32-bit signed. If the reversed value overflows this register, we must return an error code (0) to prevent a system crash. You cannot use 64-bit integers to store the temporary result."

**Why this transformation?**
*   It emphasizes the **overflow constraint**, which is the core of this problem.
*   It forbids the easy solution: "Convert to long/double, reverse, then check." You must check *during* the process (strictly speaking, though Python handles large integers automatically, you should simulate the 32-bit constraint).

---

## 2. Clarifying Questions (Phase 1)

1.  **Negative Numbers:** "How should -123 be handled?" (Result should be -321. The sign is preserved).
2.  **Trailing Zeros:** "What about 120?" (Result is 21. Leading zeros in the output are dropped).
3.  **Environment Constraints:** "Can I assume I'm running on a 64-bit machine but need to simulate 32-bit logic, or is the environment strictly 32-bit?" (Important for languages like C++/Java. In Python, integers are arbitrary precision, so we must manually check bounds).
4.  **Overflow Behavior:** "Return 0 specifically on overflow?" (Yes).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Math / Digit Extraction (Pop & Push).

**The Logic:**
We can treat the integer like a stack of digits.
*   **Pop** the last digit: `digit = x % 10`
*   **Push** it to the result: `rev = rev * 10 + digit`
*   **Reduce** the input: `x = x // 10`

**The "Gotcha" (Overflow):**
In a strict 32-bit environment, the line `rev = rev * 10 + digit` could crash or wrap around if `rev` is already large.
We must check if `rev` is about to overflow *before* doing the multiplication.

---

## 4. Base Template & Modification

**Standard Digit Extraction:**
```python
res = 0
while x > 0:
    digit = x % 10
    res = res * 10 + digit
    x = x // 10
```

**Modified Template (Handling Negatives & Bounds):**
1.  **Negatives:** `x % 10` in Python behaves differently for negative numbers (e.g., `-123 % 10` is `7`, not `-3`).
    *   *Fix:* Work with `abs(x)` and restore the sign later.
2.  **Bounds Check:**
    *   `MAX_INT = 2**31 - 1`
    *   `MIN_INT = -2**31`
    *   In Python, we can reverse first and *then* check constraints because Python ints won't overflow. However, to "roleplay" the interview correctly, we should discuss the check.

---

## 5. Optimal Solution

```python
class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer boundaries
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        
        # 1. Handle Sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_x = 0
        
        # 2. Digit Extraction Loop
        while x != 0:
            # Pop the last digit
            digit = x % 10
            x //= 10
            
            # 3. Overflow Check (Strict Simulation)
            # In C++/Java, we would check here BEFORE multiplying:
            # if (reversed_x > MAX_INT // 10) or (reversed_x == MAX_INT // 10 and digit > 7): return 0
            
            # Since Python handles large integers gracefully, we can build it 
            # and check at the end, OR check continuously. 
            # For the most "faithful" logic:
            if reversed_x > (MAX_INT - digit) // 10:
                return 0
                
            # Push digit
            reversed_x = reversed_x * 10 + digit
            
        # Restore sign
        reversed_x *= sign
        
        # Final check (redundant if strict check above is perfect, but safe for Python logic)
        if reversed_x < MIN_INT or reversed_x > MAX_INT:
            return 0
            
        return reversed_x
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(\log_{10}(x))$
    *   The loop runs once for every digit in the number. A 32-bit integer has at most 10 digits. So effectively $O(1)$ or $O(d)$ where $d$ is number of digits.
*   **Space Complexity:** $O(1)$
    *   We use a constant amount of extra space variables.

---

## 7. Follow-up & Extensions

**Q: How would you implement this in a language like C++ without 64-bit integers?**
**A:** You must perform the check `if (rev > INT_MAX/10 || (rev == INT_MAX/10 && pop > 7))` before updating `rev`. This ensures we never cross the boundary.

**Q: What if the input was a string?**
**A:** This becomes "String to Integer (atoi)", which involves parsing, handling whitespace, signs, and the same overflow logic.
