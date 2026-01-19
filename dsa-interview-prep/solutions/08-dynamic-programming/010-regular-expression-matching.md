# 10. Regular Expression Matching

**Difficulty:** Hard
**Pattern:** Dynamic Programming (2D Grid)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*`.
*   `.` Matches any single character.
*   `*` Matches zero or more of the preceding element.

**Interview Scenario (The "Compiler/Search" Prompt):**
"We are building a simplified search engine or a file system query tool (like a mini `grep`). Users can define search patterns using wildcards. Specifically, they can use a dot to represent any character and a star to say 'repeat the previous character any number of times (including zero)'. Write the core matching function `isMatch(text, pattern)`."

**Why this transformation?**
*   It tests if you understand the difference between *file globbing* (where `*` usually means "any string") and *regex* (where `*` modifies the *previous* character).
*   It frames it as a state machine or parsing problem.

---

## 2. Clarifying Questions (Phase 1)

1.  **Star Behavior:** "Does `*` start a sequence or modify the previous? e.g., if pattern is `*a`, is that valid?" (Usually, the problem guarantees `*` is preceded by a valid character. If not, ask how to handle malformed patterns).
2.  **Zero Matches:** "Confirming that `a*` can match an empty string?" (Yes, it matches zero `a`s).
3.  **Dot-Star:** "How does `.*` behave?" (It matches any sequence of characters, effectively "any string").
4.  **Empty Strings:** "What if `s` is empty and `p` is `a*`?" (Should match). "What if `p` is empty and `s` is `a`?" (Should not match).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Dynamic Programming (Top-Down Memoization or Bottom-Up 2D Table).

**Why not Greedy?**
Consider `s = "aa"`, `p = "a*a"`.
A greedy approach might consume both `a`s with `a*` and fail to match the final `a`. Or it might consume nothing. We need to try *all* possibilities (consume 0, 1, 2... instances). This branching suggests Recursion/DP.

**The State:**
Let `dp[i][j]` represent whether `s[i:]` matches `p[j:]` (Suffix matching) OR whether `s[:i]` matches `p[:j]` (Prefix matching). Prefix matching is usually more intuitive for iteration.

**State Definition (Prefix):**
`dp[i][j]` = `True` if the first `i` characters of `s` match the first `j` characters of `p`.

---

## 4. Base Template & Modification

**Standard 2D DP Template:**
```python
dp = [[False] * (n + 1) for _ in range(m + 1)]
dp[0][0] = True
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if condition: dp[i][j] = ...
```

**Modified Logic for Regex:**

1.  **Character Match (`p[j-1]` is 'a' or '.'):**
    *   If `s[i-1] == p[j-1]` or `p[j-1] == '.'`:
        *   `dp[i][j] = dp[i-1][j-1]` (Inherit status from diagonal).

2.  **Star Match (`p[j-1]` is '*'):**
    *   This is the tricky part. The `*` acts on `p[j-2]`.
    *   **Option A (Zero occurrences):** We ignore `p[j-2]` and `p[j-1]`.
        *   `dp[i][j] = dp[i][j-2]`
    *   **Option B (One or more occurrences):** If `s[i-1]` matches `p[j-2]` (or `p[j-2]` is '.'), we can "consume" one character of `s` and stay on the same pattern `p`.
        *   `dp[i][j] = dp[i-1][j]`

---

## 5. Optimal Solution

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] means s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base Case: Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, .* that match empty string
        # We iterate through the pattern (row 0 of DP table)
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # The '*' removes the preceding element (j-2), so look back 2
                dp[0][j] = dp[0][j-2]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: Direct match or '.'
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                
                # Case 2: '*'
                elif p[j-1] == '*':
                    # Two sub-cases:
                    # 1. Zero occurrences of the character before '*': 
                    #    Look at dp[i][j-2] (skip char and star)
                    dp[i][j] = dp[i][j-2]
                    
                    # 2. One or more occurrences:
                    #    Check if the character before '*' (p[j-2]) matches s[i-1]
                    #    If so, we can inherit from dp[i-1][j] (consume s char, keep p)
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                        
        return dp[m][n]
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(M \times N)$
    *   We fill a table of size $(M+1)(N+1)$, doing constant work per cell.
*   **Space Complexity:** $O(M \times N)$
    *   The table storage.
    *   *Optimization:* We can optimize to $O(N)$ space because row `i` only depends on row `i` and `i-1`.

---

## 7. Follow-up & Extensions

**Q: What if we add a '+' wildcard (one or more)?**
**A:** Logic is similar to `*`, but "Zero occurrences" option is removed. We would require at least one match before entering the "consumer" loop.

**Q: Implement this recursively.**
**A:** This is often easier to write in an interview first if you are stuck on the DP indices.
```python
@cache
def dfs(i, j):
    if j >= len(p): return i >= len(s)
    match = i < len(s) and (s[i] == p[j] or p[j] == '.')
    if j + 1 < len(p) and p[j+1] == '*':
        return dfs(i, j+2) or (match and dfs(i+1, j))
    return match and dfs(i+1, j+1)
```
This is a perfectly valid "Optimal" solution due to Python's memoization.

```