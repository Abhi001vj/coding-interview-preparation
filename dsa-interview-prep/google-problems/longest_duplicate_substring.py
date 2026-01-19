# LeetCode 1044: Longest Duplicate Substring
# Google-style: Find longest repeated phrase in plagiarism detection

# ============================================================
# APPROACH 1: Simple Sliding Window + Set (Easier to understand)
# ============================================================

class SolutionSimple:
    def longestDupSubstring(self, s: str) -> str:
        """
        Simple approach: Try each length, use set to find duplicates.

        Time: O(n²) - might TLE for large inputs
        Space: O(n²) - storing substrings

        Good for interviews if optimal is too complex to code quickly.
        """
        n = len(s)

        # Try lengths from longest to shortest
        for length in range(n - 1, 0, -1):
            seen = set()

            # Slide window of this length
            for i in range(n - length + 1):
                substring = s[i:i + length]

                if substring in seen:
                    return substring

                seen.add(substring)

        return ""


# ============================================================
# APPROACH 2: Binary Search + Rolling Hash (Optimal)
# ============================================================

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
        Optimal approach:
        1. Binary search on the length of duplicate
        2. Use rolling hash (Rabin-Karp) to check if duplicate exists

        Key insight: If duplicate of length K exists,
                     duplicates of length K-1 also exist.
                     → Binary search works!

        Time: O(n log n)
        Space: O(n)
        """
        n = len(s)

        # Convert string to numbers for hashing
        nums = [ord(c) - ord('a') for c in s]

        # Rabin-Karp parameters
        base = 26
        mod = 2**63 - 1  # Large prime to reduce collisions

        def has_duplicate(length: int) -> str:
            """
            Check if duplicate substring of given length exists.
            Uses rolling hash for O(n) check.
            Returns the duplicate if found, else empty string.
            """
            if length == 0:
                return ""

            # Compute hash of first window
            h = 0
            for i in range(length):
                h = (h * base + nums[i]) % mod

            # Store hash -> starting index
            seen = {h: 0}

            # Precompute base^length for rolling
            base_power = pow(base, length, mod)

            # Slide window
            for i in range(1, n - length + 1):
                # Rolling hash: remove left char, add right char
                h = (h * base - nums[i - 1] * base_power + nums[i + length - 1]) % mod

                if h in seen:
                    # Verify to handle hash collision
                    j = seen[h]
                    if s[i:i + length] == s[j:j + length]:
                        return s[i:i + length]

                seen[h] = i

            return ""

        # Binary search on length
        result = ""
        left, right = 1, n - 1

        while left <= right:
            mid = (left + right) // 2

            duplicate = has_duplicate(mid)

            if duplicate:
                result = duplicate  # Found duplicate of this length
                left = mid + 1      # Try longer
            else:
                right = mid - 1     # Try shorter

        return result


# ============================================================
# VERIFICATION
# ============================================================

# Example 1: s = "banana"
#
# Binary search: left=1, right=5
#
# mid=3: Check length 3
#   "ban" hash=h1, "ana" hash=h2, "nan" hash=h3, "ana" hash=h2
#   "ana" appears twice! → found duplicate of length 3
#   result = "ana", try longer (left=4)
#
# mid=4: Check length 4
#   "bana" "anan" "nana" - all unique hashes
#   No duplicate of length 4, try shorter (right=3)
#
# left=4 > right=3 → DONE
# Return "ana" ✓


# Example 2: s = "abcd"
#
# mid=2: "ab" "bc" "cd" - all unique
# mid=1: "a" "b" "c" "d" - all unique
# Return "" ✓


# Why Rolling Hash?
# ─────────────────
# Naive: Compare all substrings of length L → O(L) per comparison
# Rolling hash: Compute next hash from previous in O(1)
#
# Hash("ana") = a*26² + n*26¹ + a*26⁰
#
# To get hash("nan") from hash("ana"):
#   Remove 'a' from front: subtract a*26²
#   Shift left: multiply by 26
#   Add 'n' at end: add n
#
# Formula: new_hash = (old_hash * base - removed * base^L + added) % mod
