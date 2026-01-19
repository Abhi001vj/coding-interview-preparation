# LeetCode 351: Android Unlock Patterns
# Google-style: Count valid lock screen patterns

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """
        Count valid unlock patterns of length m to n.

        Approach: Backtracking with jump table
        1. Precompute which moves require intermediate dot
        2. Backtrack from each starting position
        3. Use symmetry to reduce computation

        Time: O(n!) but pruned heavily
        Space: O(n) for recursion stack
        """
        # Jump table: jump[i][j] = dot that must be visited before i→j
        # 0 means no intermediate dot required
        jump = [[0] * 10 for _ in range(10)]

        # Horizontal jumps
        jump[1][3] = jump[3][1] = 2
        jump[4][6] = jump[6][4] = 5
        jump[7][9] = jump[9][7] = 8

        # Vertical jumps
        jump[1][7] = jump[7][1] = 4
        jump[2][8] = jump[8][2] = 5
        jump[3][9] = jump[9][3] = 6

        # Diagonal jumps
        jump[1][9] = jump[9][1] = 5
        jump[3][7] = jump[7][3] = 5

        def backtrack(curr: int, remaining: int, visited: set) -> int:
            """
            Count patterns starting from curr with 'remaining' more dots to add.
            """
            # Base case: no more dots to add
            if remaining == 0:
                return 1

            count = 0
            visited.add(curr)

            for next_dot in range(1, 10):
                # Skip if already visited
                if next_dot in visited:
                    continue

                # Check if jump is valid
                mid = jump[curr][next_dot]

                # Valid move if:
                # 1. No intermediate dot required (mid == 0), OR
                # 2. Intermediate dot already visited
                if mid == 0 or mid in visited:
                    count += backtrack(next_dot, remaining - 1, visited)

            visited.remove(curr)
            return count

        total = 0

        # Count patterns of each valid length
        for length in range(m, n + 1):
            # Use symmetry:
            # - Corners (1,3,7,9) are symmetric → multiply by 4
            # - Edges (2,4,6,8) are symmetric → multiply by 4
            # - Center (5) → count once

            # Patterns starting from corner (1)
            total += backtrack(1, length - 1, set()) * 4

            # Patterns starting from edge (2)
            total += backtrack(2, length - 1, set()) * 4

            # Patterns starting from center (5)
            total += backtrack(5, length - 1, set())

        return total


# ============================================================
# ALTERNATIVE: Without symmetry optimization (clearer logic)
# ============================================================

class SolutionSimple:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """Simpler version without symmetry optimization."""

        # Jump table
        jump = [[0] * 10 for _ in range(10)]
        jump[1][3] = jump[3][1] = 2
        jump[1][7] = jump[7][1] = 4
        jump[1][9] = jump[9][1] = 5
        jump[2][8] = jump[8][2] = 5
        jump[3][7] = jump[7][3] = 5
        jump[3][9] = jump[9][3] = 6
        jump[4][6] = jump[6][4] = 5
        jump[7][9] = jump[9][7] = 8

        def backtrack(curr, remaining, visited):
            if remaining == 0:
                return 1

            count = 0
            visited.add(curr)

            for next_dot in range(1, 10):
                if next_dot in visited:
                    continue

                mid = jump[curr][next_dot]
                if mid == 0 or mid in visited:
                    count += backtrack(next_dot, remaining - 1, visited)

            visited.remove(curr)
            return count

        total = 0
        for length in range(m, n + 1):
            for start in range(1, 10):
                total += backtrack(start, length - 1, set())

        return total


# ============================================================
# VERIFICATION
# ============================================================

# Example 1: m=1, n=1
# Each single dot is a valid pattern
# Answer: 9 ✓

# Example 2: m=1, n=2
# Length 1: 9 patterns
# Length 2: All valid moves from each dot
#   From 1: can go to 2,4,5,6,8 (5 moves) - can't go to 3,7,9 without intermediate
#   Wait, 1→6 and 1→8 are valid (no jump needed)!
#   Actually from 1: 2,4,5,6,8 = 5 valid (not 3,7,9)
#   From 2: 1,3,4,5,6,7,9 = 7 valid (not 8)
#   From 5: all 8 others valid
#   By symmetry: corners give 5 each (×4=20), edges give 7 each (×4=28), center gives 8
#   Length 2 total = 20 + 28 + 8 = 56
#   Total = 9 + 56 = 65 ✓


# Grid visualization:
#
#   1 — 2 — 3
#   |  \|/  |
#   4 — 5 — 6
#   |  /|\  |
#   7 — 8 — 9
#
# Knight-like moves (e.g., 1→6, 1→8, 2→9) don't require intermediates!
# Only straight-line jumps through center of another dot require intermediates.
