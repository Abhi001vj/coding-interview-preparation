# 12. Integer to Roman

**Difficulty:** Medium
**Pattern:** Greedy / Math Simulation

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an integer, convert it to a Roman numeral. (Input is guaranteed to be within the range from 1 to 3999).

**Interview Scenario (The "Coin Change" Prompt):**
"Design a system to convert modern numbers into an ancient accounting format (or a specialized denomination system). The system has specific symbols for values like 1000, 500, 100, etc. It also has a 'subtractive' rule where 4 is written as 5-1 (IV) rather than 1+1+1+1 (IIII). Given an integer amount, output the string representation using the fewest number of symbols."

**Why this transformation?**
*   It highlights that this is essentially a **Greedy** problem (like making change with the largest coins possible).
*   It removes the "Roman" context slightly to ensure you understand the *mechanics* of the subtractive notation (IV, IX, XL, XC, etc.) as distinct "denominations".

---

## 2. Clarifying Questions (Phase 1)

1.  **Input Range:** "What is the maximum value? 3999?" (Yes, standard Roman numerals don't usually go higher without new symbols).
2.  **Validation:** "Do I need to handle negative numbers or zero?" (No, Romans didn't have a zero concept in this context).
3.  **Output Case:** "Upper case only?" (Yes).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Greedy Approach with Lookup Table.

**Why Greedy?**
To represent a number with the *fewest* symbols (standard Roman form), we should always try to subtract the *largest possible* value that fits.
Example: 49.
*   Can we take 50 (L)? No.
*   Can we take 40 (XL)? Yes. Remainder 9.
*   Can we take 9 (IX)? Yes. Remainder 0.
Result: XLIX.

**Data Structure:**
We need a list of values and symbols, *including* the subtractive pairs, sorted from largest to smallest.
`[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), ...]`

---

## 4. Base Template & Modification

**Standard Greedy Loop:**
```python
values = [...]
res = ""
for val, sym in values:
    while num >= val:
        res += sym
        num -= val
```

**Modified Logic:**
There is barely any modification needed. The "trick" is ensuring the lookup table is complete (includes 900, 400, 90, 40, 9, 4).

---

## 5. Optimal Solution

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of values to symbols, including the subtractive cases
        # Order matters: Largest to smallest for Greedy approach
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        
        res = []
        
        for value, symbol in value_symbols:
            # If the input number is 0, we are done
            if num == 0:
                break
                
            # Count how many times the current value fits into num
            count, num = divmod(num, value)
            
            # Append that many symbols
            res.append(symbol * count)
            
        return "".join(res)
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(1)$
    *   The loop runs a fixed number of times (13 denominations). The input is capped at 3999, so the inner `divmod` or subtraction doesn't depend on $N$ in a way that scales indefinitely. Technically it's $O(1)$ given the fixed constraints. If $N$ were arbitrary, it's $O(\log N)$ (digits).
*   **Space Complexity:** $O(1)$
    *   For the storage of the result and the fixed table.

---

## 7. Follow-up & Extensions

**Q: Reverse it (Roman to Integer).**
**A:** Iterate through the string. If `value[i] < value[i+1]`, subtract `value[i]`. Else, add it. (e.g., IV: 1 < 5, so -1 + 5 = 4).

**Q: How would you handle large numbers (e.g., 10,000) if we added a convention like a bar over a letter means x1000?**
**A:** I would extend the `value_symbols` table with the new symbols (`(10000, 'X̅')`, etc.) and the logic remains exactly the same.
