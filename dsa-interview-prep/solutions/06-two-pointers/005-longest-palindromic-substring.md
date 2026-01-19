# 5. Longest Palindromic Substring

**Difficulty:** Medium
**Pattern:** Two Pointers (Expand Around Center)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given a string `s`, return the longest palindromic substring in `s`.

**Interview Scenario (The "Vague" Prompt):**
"I have a stream of server logs or perhaps a sequence of DNA data represented as a string. I'm looking for patterns where a sequence reads the same forwards and backwards. Specifically, I need to find the longest such continuous segment within a larger string. How would you approach this?"

**Why this transformation?**
*   It removes the explicit "palindrome" keyword initially to test if you recognize the structure.
*   It contextualizes the problem (DNA, logs), which is common in FAANG interviews.

---

## 2. Clarifying Questions (Phase 1)

Before jumping into code, clarify constraints and edge cases:

1.  **Input Character Set:** "Does the string contain only alphanumeric characters? Should I care about case sensitivity?" (Usually yes for this specific LeetCode problem, but good to ask).
2.  **Empty/Single String:** "What should be returned if the input string is empty or has only one character?" (Return empty string or the character itself).
3.  **Multiple Answers:** "If there are multiple palindromic substrings of the same maximum length, does it matter which one I return?" (Usually return any one of them).
4.  **Constraints:** "What is the maximum length of the string? This helps me determine if an $O(n^2)$ solution is acceptable or if I need something linear." (Usually $N \le 1000$, so $O(n^2)$ is fine).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Two Pointers (Center Expansion Strategy).

**Why not standard Sliding Window?**
Standard sliding window looks for a specific condition in a window of size `k` or expanding `right` until a condition breaks. Palindromes are symmetric. The "condition" depends on both ends matching relative to a *center*.

**Why not Dynamic Programming?**
DP is a valid $O(n^2)$ approach (table `dp[i][j]` is true if `s[i:j]` is a palindrome). However, it requires $O(n^2)$ *space*. The Center Expansion method uses $O(1)$ space.

**The "Base Template" Concept:**
Standard Two Pointers usually converge from ends (`left++`, `right--`) or move in parallel. Here, we **diverge** from a center (`left--`, `right++`).

---

## 4. Base Template & Modification

**Standard Two Pointers (Converging):**
```python
left, right = 0, len(s) - 1
while left < right:
    if s[left] != s[right]: return False
    left += 1
    right -= 1
```

**Modified Template (Diverging / Expand Around Center):**
We need to handle two types of centers:
1.  **Odd Length:** Center is a single character (e.g., "aba", center 'b').
2.  **Even Length:** Center is between two characters (e.g., "abba", center between 'b's).

**Logic:**
Iterate through every index `i`. Treat `i` as the center (odd) AND treat `i, i+1` as the center (even). Expand as long as `s[left] == s[right]`.

---

## 5. Optimal Solution

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        for i in range(len(s)):
            # Case 1: Odd length palindrome (centered at i)
            # e.g., "aba" -> expands from 'b'
            len1 = self.expand_around_center(s, i, i)
            
            # Case 2: Even length palindrome (centered between i and i+1)
            # e.g., "abba" -> expands from 'bb'
            len2 = self.expand_around_center(s, i, i + 1)
            
            # Get the max length found at this center
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update our global tracking
            # We need to calculate the new start and end indices based on the length
            if max_len > (end - start):
                # Example: i=2, max_len=3 ("aba"). start = 2 - (2)//2 = 1. end = 2 + 3//2 = 3.
                # substring s[1:4] is "aba" (exclusive end in python slice, inclusive in logic logic)
                # Let's be precise:
                # If len is odd (e.g. 3), half is 1. start = i - 1, end = i + 1
                # If len is even (e.g. 2), half is 1. start = i - 0, end = i + 1
                
                # Formula derivation:
                # start = i - (max_len - 1) // 2
                # end = i + max_len // 2
                
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # Return substring. Note: Python slice is [start : end+1]
        return s[start : end + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        """
        Expands outward from the given left and right pointers 
        as long as characters match and indices are valid.
        Returns the length of the palindrome found.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Why (right - left - 1)?
        # The while loop breaks when s[left] != s[right].
        # So the actual palindrome is from (left + 1) to (right - 1).
        # Length = (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N^2)$
    *   We iterate through the string ($N$ centers).
    *   At each center, we expand. In the worst case (e.g., "aaaaa"), expansion takes $O(N)$.
    *   Total: $N \times N = N^2$.
*   **Space Complexity:** $O(1)$
    *   We only store variables `start`, `end`, `max_len`. We do not allocate a new DP table or recursion stack.

---

## 7. Follow-up & Extensions

**Q: Can we do better than $O(N^2)$?**
**A:** Yes, there is **Manacher’s Algorithm**, which solves this in $O(N)$ time.
*   **Intuition:** It uses previously computed palindrome boundaries to avoid re-expanding for characters that lie within an existing palindrome.
*   **Interview Advice:** Manacher's is rarely required in a standard 45-minute interview due to its implementation complexity. However, *mentioning* it shows deep domain knowledge. The Expand Around Center ($O(N^2)$) approach is typically the expected "optimal" solution for general engineering roles.

**Q: What if we needed to find the number of palindromic substrings?**
**A:** The same logic applies. Instead of tracking `max_len`, we would increment a `count` variable every time we successfully expand (`left -= 1`, `right += 1`).

```