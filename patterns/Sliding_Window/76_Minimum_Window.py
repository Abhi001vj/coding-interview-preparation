import collections

# FAANG Interview Stage 1: Clarify
# Q: Does 't' contain duplicates? -> "Yes (e.g. t='AA')"
# Q: What if no window exists? -> "Return empty string"
# Q: O(N) required? -> "Yes"

# FAANG Interview Stage 2: Plan
# Approach: Sliding Window with Frequency Map
# 1. Count chars in 't' (target_counts).
# 2. Expand 'right', add s[right] to window_counts.
# 3. Track 'formed' chars. If window_counts[c] == target_counts[c], formed++.
# 4. WHILE formed == required_unique_chars (Valid Window):
#    a. Update min_len result.
#    b. Shrink 'left' (remove s[left]).
#    c. If removal breaks validity (count < target), formed--.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = collections.Counter(t)
        required = len(dict_t)

        # Filter s? No, just iterate.
        l, r = 0, 0
        formed = 0
        window_counts = collections.defaultdict(int)

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] += 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count of unique characters.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# FAANG Interview Stage 4: Verify
if __name__ == "__main__":
    solver = Solution()
    # Test 1
    # s="ADOBECODEBANC", t="ABC" -> "BANC"
    print(f"Test 1: {solver.minWindow('ADOBECODEBANC', 'ABC')} (Expected: 'BANC')")
    
    # Test 2
    # s="a", t="a" -> "a"
    print(f"Test 2: {solver.minWindow('a', 'a')} (Expected: 'a')")
    
    # Test 3
    # s="a", t="aa" -> ""
    print(f"Test 3: {solver.minWindow('a', 'aa')} (Expected: '')")
