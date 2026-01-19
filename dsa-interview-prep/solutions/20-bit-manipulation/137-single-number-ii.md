# 137. Single Number II

**Difficulty:** Medium
**Pattern:** Bit Manipulation

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element that appears once. You must implement a solution with a linear runtime complexity and use only constant extra space.

**Interview Scenario (The "Faulty Sensor Reading" Prompt):
"You are collecting readings from multiple redundant sensors. Due to a design choice, each valid reading is transmitted three times to ensure reliability. However, one sensor is faulty and sends only a single, unique reading. All other readings are consistent in groups of three. Identify the unique, non-triplicated reading from the aggregated stream. You have strict memory and processing constraints."

**Why this transformation?**
*   It provides a real-world context for identifying an anomaly.
*   It explicitly emphasizes the **constant space** and **linear time** constraints, ruling out hash maps or sorting.

---

## 2. Clarifying Questions (Phase 1)

1.  **Input Range:** "Are numbers positive, negative, or both?" (Can be both, affecting bit representation for negatives).
2.  **Number of Occurrences:** "Is it always exactly three times for others, and once for the single?" (Yes).
3.  **Maximum Value:** "What is the maximum value of numbers? This determines the number of bits to check." (Typically 32-bit integers).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Bit Manipulation (Counting Bits).

**The Logic:**
If every number appears three times, then for each bit position (0 to 31 for 32-bit integers), the sum of that bit across all numbers in the array will be a multiple of 3, *unless* the single number has that bit set.

**Algorithm:**
1.  Initialize `single_number = 0`.
2.  Iterate through each bit position `i` from 0 to 31 (or 63 for 64-bit integers).
3.  For each bit position `i`:
    *   Count how many numbers in `nums` have the `i`-th bit set.
    *   `bit_sum = 0`.
    *   For `num` in `nums`:
        *   `if (num >> i) & 1: bit_sum += 1`.
    *   If `bit_sum % 3 != 0`, it means the single number has its `i`-th bit set.
    *   Set the `i`-th bit in `single_number`: `single_number |= (1 << i)`.
4.  Return `single_number`.

**Handling Negatives:**
Python handles large integers and bitwise operations transparently, so the standard approach works. For languages like C++/Java, you need to be careful with negative numbers and their 2's complement representation. Often, problems assume non-negative or require specific handling for the sign bit.

---

## 4. Base Template & Modification

**Standard Bit Counting Template:**
```python
result = 0
for bit_pos in range(num_bits):
    count = 0
    for num in array:
        if (num >> bit_pos) & 1: count += 1
    if count % K != 0: # K is number of times others appear
        result |= (1 << bit_pos)
```

**Modified Logic:** None, this is the canonical template for `K` occurrences.

---

## 5. Optimal Solution

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        
        # Iterate through each bit position (0 to 31 for 32-bit integers)
        # Note: In Python, integers have arbitrary precision. We simulate 32-bit.
        for i in range(32):
            bit_sum = 0
            # Count how many numbers have the i-th bit set
            for num in nums:
                # Check if the i-th bit of `num` is 1
                if (num >> i) & 1:
                    bit_sum += 1
            
            # If the sum of the i-th bits is not a multiple of 3,
            # it means the unique number has its i-th bit set.
            if bit_sum % 3 != 0:
                # Set the i-th bit in our answer
                ans |= (1 << i)
        
        # Handle negative numbers for 32-bit representation (Python specific)
        # If the 31st bit is set and the number is considered negative in 2's complement
        # (i.e., ans is a large positive number that represents a negative number)
        # Convert to its true negative form if it was originally a negative number
        if ans >= 2**31:
            ans -= 2**32
            
        return ans
```

-----

## 6. Big O Analysis

*   **Time Complexity:** $O(N \times \text{num_bits})$
    *   We iterate through `num_bits` (constant, usually 32 or 64).
    *   For each bit, we iterate through all `N` numbers.
*   **Space Complexity:** $O(1)$
    *   Only a few integer variables used.

---

## 7. Follow-up & Extensions

**Q: Single Number I (every element appears twice except for one)?**
**A:** Use XOR. `a ^ a = 0`. `a ^ b ^ a = b`. XORing all numbers together will give the single number.

**Q: What if every element appears `K` times except for one?**
**A:** Generalize the bit counting: `if bit_sum % K != 0: ans |= (1 << i)`.

**Q: Using finite state machine (more complex, but $O(1)$ space and $O(N)$ time with fewer bit ops).**
**A:** Use two variables (`ones`, `twos`).
*   `ones = (ones ^ num) & ~twos`
*   `twos = (twos ^ num) & ~ones`
This is a clever trick, but often not expected unless specifically hinted at, as the bit counting is more straightforward to derive.

```