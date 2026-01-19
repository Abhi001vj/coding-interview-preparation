# LeetCode 1780: Check if Number is a Sum of Powers of Three
# Google-style: Can we fulfill storage request using distinct chunk sizes (powers of 3)?

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Check if n can be represented as sum of distinct powers of 3.

        Key insight: Convert to base 3 (ternary).
        - If all digits are 0 or 1 → possible (use each power at most once)
        - If any digit is 2 → impossible (would need same power twice)

        Time: O(log₃ n) - we divide by 3 each iteration
        Space: O(1)
        """
        while n > 0:
            remainder = n % 3

            # If remainder is 2, we'd need this power of 3 twice
            if remainder == 2:
                return False

            n //= 3

        return True


# ============================================================
# ALTERNATIVE APPROACH: Greedy subtraction
# ============================================================

class SolutionGreedy:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Greedy: Subtract largest power of 3 that fits, repeat.
        If we ever need the same power twice, return False.

        Time: O(log₃ n)
        Space: O(log₃ n) for used set, or O(1) if we track differently
        """
        used = set()

        while n > 0:
            # Find largest power of 3 <= n
            power = 1
            while power * 3 <= n:
                power *= 3

            # Check if already used
            if power in used:
                return False

            used.add(power)
            n -= power

        return True


# ============================================================
# VERIFICATION
# ============================================================

# Example 1: n = 12
# 12 % 3 = 0, n = 4
# 4 % 3 = 1, n = 1
# 1 % 3 = 1, n = 0
# All remainders ≤ 1 → TRUE ✓
# 12 = 3¹ + 3² = 3 + 9 = 12 ✓

# Example 2: n = 91
# 91 % 3 = 1, n = 30
# 30 % 3 = 0, n = 10
# 10 % 3 = 1, n = 3
# 3 % 3 = 0, n = 1
# 1 % 3 = 1, n = 0
# All remainders ≤ 1 → TRUE ✓
# 91 = 3⁰ + 3² + 3⁴ = 1 + 9 + 81 = 91 ✓

# Example 3: n = 21
# 21 % 3 = 0, n = 7
# 7 % 3 = 1, n = 2
# 2 % 3 = 2 → FOUND 2! → FALSE ✓
# 21 = (210)₃ = 2×3² + 1×3¹ + 0×3⁰
# Would need 3² twice → impossible

# Edge case: n = 1
# 1 % 3 = 1, n = 0
# TRUE ✓ (just use 3⁰ = 1)

# Edge case: n = 3
# 3 % 3 = 0, n = 1
# 1 % 3 = 1, n = 0
# TRUE ✓ (just use 3¹ = 3)

# Edge case: n = 2
# 2 % 3 = 2 → FALSE ✓
# Would need 1 + 1 = two 3⁰'s
