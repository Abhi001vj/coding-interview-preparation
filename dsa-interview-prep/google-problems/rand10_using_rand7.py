# LeetCode 470: Implement Rand10() Using Rand7()
# Google-style: Build 10-variant A/B test RNG from legacy 7-variant RNG

# The rand7() API is already defined for you.
# def rand7():
#     return random.randint(1, 7)

class Solution:
    def rand10(self) -> int:
        """
        Generate uniform random integer in [1, 10] using only rand7().

        Approach: Rejection Sampling
        - Two calls: rand7() gives range [1, 49] uniformly
        - Use [1, 40] -> maps to [1, 10] (4 values each)
        - Reject [41, 49] and retry
        """
        while True:
            # Generate uniform random in [1, 49]
            # row: 0-6, col: 1-7
            row = rand7() - 1      # 0 to 6
            col = rand7()          # 1 to 7
            idx = row * 7 + col    # 1 to 49 (uniform)

            # Accept if in [1, 40], reject [41, 49]
            if idx <= 40:
                # Map to [1, 10]
                # idx 1-4 -> 1, idx 5-8 -> 2, ..., idx 37-40 -> 10
                return (idx - 1) % 10 + 1


# ============================================================
# OPTIMIZED VERSION: Reuse rejected values
# ============================================================

class SolutionOptimized:
    def rand10(self) -> int:
        """
        Optimized: Reuse rejected values to reduce rand7() calls.

        Instead of throwing away [41-49], we can use them:
        - 41-49 gives us 9 values -> use rand7() to get 63 values
        - Use [1-60] from that, reject [61-63]
        - From [61-63], we get 3 values -> use rand7() for 21 values
        - Use [1-20], reject [21]

        Expected calls: ~2.19 (improvement from 2.45)
        """
        while True:
            # First level: 49 values
            a = rand7()
            b = rand7()
            idx = (a - 1) * 7 + b  # 1-49

            if idx <= 40:
                return (idx - 1) % 10 + 1

            # Second level: use leftover (41-49 -> 1-9) with new rand7()
            # 9 * 7 = 63 values
            c = rand7()
            idx = (idx - 40 - 1) * 7 + c  # 1-63

            if idx <= 60:
                return (idx - 1) % 10 + 1

            # Third level: use leftover (61-63 -> 1-3) with new rand7()
            # 3 * 7 = 21 values
            d = rand7()
            idx = (idx - 60 - 1) * 7 + d  # 1-21

            if idx <= 20:
                return (idx - 1) % 10 + 1

            # idx = 21: reject and start over (probability = 1/21 * 3/63 * 9/49)


# Verification with example trace:
#
# If rand7() returns 3, 5:
#   row = 3 - 1 = 2
#   col = 5
#   idx = 2 * 7 + 5 = 19
#   19 <= 40? Yes, accept
#   (19 - 1) % 10 + 1 = 18 % 10 + 1 = 8 + 1 = 9
#   Return 9 ✓
#
# If rand7() returns 6, 7:
#   row = 6 - 1 = 5
#   col = 7
#   idx = 5 * 7 + 7 = 42
#   42 <= 40? No, reject and retry ✓
#
# Edge case: rand7() returns 1, 1:
#   row = 0, col = 1
#   idx = 0 * 7 + 1 = 1
#   (1 - 1) % 10 + 1 = 0 + 1 = 1 ✓
#
# Edge case: rand7() returns 6, 5:
#   row = 5, col = 5
#   idx = 5 * 7 + 5 = 40
#   (40 - 1) % 10 + 1 = 39 % 10 + 1 = 9 + 1 = 10 ✓
