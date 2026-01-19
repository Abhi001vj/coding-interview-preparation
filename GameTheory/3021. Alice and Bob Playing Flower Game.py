"""
3021. Alice and Bob Playing Flower Game (Medium)
Pattern: Math / Game Theory / Parity

--------------------------------------------------------------------------------
PROBLEM UNDERSTANDING
--------------------------------------------------------------------------------
Alice and Bob pick flowers: x from N, y from M.
Alice wins if (x + y) is ODD.
Return number of pairs (x, y) such that Alice wins.
1 <= x <= n
1 <= y <= m

--------------------------------------------------------------------------------
INTUITION: ODD + EVEN logic
--------------------------------------------------------------------------------
When is (x + y) Odd?
1. Odd + Even = Odd
2. Even + Odd = Odd

So Alice wins if:
- She picks an ODD number AND Bob picks an EVEN number.
- OR She picks an EVEN number AND Bob picks an ODD number.

Formula:
Pairs = (AliceOdds * BobEvens) + (AliceEvens * BobOdds)

Counting Odds/Evens in range [1, K]:
- Evens = K // 2
- Odds = (K + 1) // 2

--------------------------------------------------------------------------------
ALGORITHM
--------------------------------------------------------------------------------
1. Count odds/evens for n.
2. Count odds/evens for m.
3. Multiply and sum.

Complexity: O(1)
--------------------------------------------------------------------------------
"""

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_even = n // 2
        n_odd = (n + 1) // 2
        
        m_even = m // 2
        m_odd = (m + 1) // 2
        
        return (n_odd * m_even) + (n_even * m_odd)

if __name__ == "__main__":
    sol = Solution()
    print(f"n=3, m=2: {sol.flowerGame(3, 2)}")
    # n=[1,2,3] (2 odd, 1 even)
    # m=[1,2]   (1 odd, 1 even)
    # Pairs: (1,2), (3,2), (2,1) -> 3 pairs.
