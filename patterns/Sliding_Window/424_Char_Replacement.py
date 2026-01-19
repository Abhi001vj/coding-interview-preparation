import collections

# FAANG Interview Stage 1: Clarify
# Q: Only uppercase English letters? -> "Yes"
# Q: k size? -> "0 <= k <= s.length"

# FAANG Interview Stage 2: Plan
# Approach: Sliding Window
# Formula: replacable_chars = length_of_window - count_of_most_frequent_char
# Condition: If replacable_chars > k, the window is INVALID.
# Optimization: We don't need to shrink strictly. We can just shift the window (not shrink max size).
# But for standard template, we will shrink.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        max_f = 0
        l = 0
        res = 0
        
        for r in range(len(s)):
            count[s[r]] += 1
            max_f = max(max_f, count[s[r]])
            
            # Validity Check: (window_len - max_freq) <= k
            # If invalid, shrink from left
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
                # Note: We don't technically need to update max_f down 
                # because a smaller max_f won't produce a new BEST result anyway.
                
            res = max(res, r - l + 1)
            
        return res

# FAANG Interview Stage 4: Verify
if __name__ == "__main__":
    solver = Solution()
    print(f"Test 1 (ABAB, 2): {solver.characterReplacement('ABAB', 2)} (Expected: 4)")
    print(f"Test 2 (AABABBA, 1): {solver.characterReplacement('AABABBA', 1)} (Expected: 4)")
