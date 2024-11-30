# https://leetcode.com/problems/coin-change-ii/description/
# 518. Coin Change II
# Medium
# Topics
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

 

# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10]
# Output: 1
 

# Constraints:

# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000

"""
COIN CHANGE II - COMPREHENSIVE ANALYSIS
Problem: Find number of ways to make amount using given coins with infinite supply

Example: amount = 5, coins = [1,2,5]
Output: 4

DECISION TREE VISUALIZATION:
                                 (i=0,amount=5)
                        /                          \
                Use coin[0]=1                Don't use coin[0]
            (i=0,amount=4)                    (i=1,amount=5)
            /           \                    /              \
    Use coin[0]    Don't use coin[0]   Use coin[1]    Don't use coin[1]
    (0,3)          (1,4)               (1,3)          (2,5)
    ...            ...                 ...            ...

Complete pattern for amount=5:
5 = 5                     [Using 5]
5 = 2 + 2 + 1            [Using 2,2,1]
5 = 2 + 1 + 1 + 1        [Using 2,1,1,1]
5 = 1 + 1 + 1 + 1 + 1    [Using 1,1,1,1,1]

SOLUTION APPROACHES WITH DETAILED ANALYSIS:
"""

#1. RECURSIVE SOLUTION (BRUTE FORCE)
class CoinChangeSolutions:
    def recursive_change(self, amount: int, coins: list[int]) -> int:
        """
        Recursive solution showing all possible combinations.
        
        State Space Tree for amount=5, coins=[1,2,5]:
        Each node format: (index, remaining_amount)
        
                                (0,5)
                        /                \
                Use 1                Don't use 1
               (0,4)                     (1,5)
            /         \               /         \
         (0,3)       (1,4)        (1,3)       (2,5)
        /     \     /     \      /     \     /     \
      (0,2)  (1,3) ...   ...   ...    ...  ...    ...
        
        Time: O(2^max(n,am)), Space: O(max(n,am))
        where n=coins length, a=amount, m=min coin value
        """
        coins.sort()  # Sort for optimization
        
        def dfs(i: int, remaining: int, path: list = None) -> int:
            if path is None: path = []
            
            # Base cases
            if remaining == 0:  # Found valid combination
                print(f"Found combination: {path}")
                return 1
            if i >= len(coins):  # Out of coins
                return 0
                
            ways = 0
            # Try using current coin if possible
            if remaining >= coins[i]:
                # Include current coin and stay at same index (can reuse)
                path.append(coins[i])
                ways += dfs(i, remaining - coins[i], path)
                path.pop()
                
                # Don't use current coin, move to next
                ways += dfs(i + 1, remaining, path)
            return ways
            
        return dfs(0, amount)

    #2. MEMOIZATION (TOP-DOWN DP)
    def memoized_change(self, amount: int, coins: list[int]) -> int:
        """
        Memoization approach with state caching.
        
        Memo table structure for amount=5, coins=[1,2,5]:
        Rows: coin indices
        Cols: amounts from 0 to target
        
        memo[i][a] = ways to make amount 'a' using coins[i:]
        
             0  1  2  3  4  5
        [1]  1  1  1  1  1  1
        [2]  1  0  1  1  2  2
        [5]  1  0  0  0  0  1
        
        Time: O(n*a), Space: O(n*a)
        """
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        
        def print_memo(note: str = ""):
            print(f"\nMemo table {note}:")
            print("     " + " ".join(f"{i:2}" for i in range(amount + 1)))
            for i, coin in enumerate(coins):
                row = [str(memo[i][j]).rjust(2) for j in range(amount + 1)]
                print(f"[{coin:2}] {' '.join(row)}")
        
        def dfs(i: int, remaining: int) -> int:
            # Base cases
            if remaining == 0:
                return 1
            if i >= len(coins):
                return 0
                
            # Check memo
            if memo[i][remaining] != -1:
                return memo[i][remaining]
                
            ways = 0
            # Try using current coin
            if remaining >= coins[i]:
                ways = dfs(i + 1, remaining)  # Don't use coin
                ways += dfs(i, remaining - coins[i])  # Use coin
                
            memo[i][remaining] = ways
            print_memo(f"after processing i={i}, remaining={remaining}")
            return ways
            
        return dfs(0, amount)

    #3. BOTTOM-UP DP
    def bottom_up_change(self, amount: int, coins: list[int]) -> int:
        """
        Bottom-up DP showing table construction.
        
        DP table visualization for amount=5, coins=[1,2,5]:
        
        Initial:
             0  1  2  3  4  5
        []   1  0  0  0  0  0
        [1]  1  0  0  0  0  0
        [2]  1  0  0  0  0  0
        [5]  1  0  0  0  0  0
        
        Final:
             0  1  2  3  4  5
        []   1  0  0  0  0  0
        [1]  1  1  1  1  1  1
        [2]  1  1  2  2  3  3
        [5]  1  1  2  2  3  4
        
        Time: O(n*a), Space: O(n*a)
        """
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        # Base case: empty sum
        for i in range(n + 1):
            dp[i][0] = 1
            
        def print_dp(step: str):
            print(f"\nDP Table after {step}:")
            print("     " + " ".join(f"{i:2}" for i in range(amount + 1)))
            for i in range(n + 1):
                coin = coins[i-1] if i > 0 else 0
                row = [str(dp[i][j]).rjust(2) for j in range(amount + 1)]
                print(f"[{coin:2}] {' '.join(row)}")
        
        print_dp("initialization")
        
        # Fill table
        for i in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                # Don't use current coin
                dp[i][a] = dp[i + 1][a]
                # Use current coin if possible
                if a >= coins[i]:
                    dp[i][a] += dp[i][a - coins[i]]
                    
            print_dp(f"processing coin {coins[i]}")
        
        return dp[0][amount]

    #4. SPACE-OPTIMIZED DP
    def optimized_change(self, amount: int, coins: list[int]) -> int:
        """
        Space-optimized version using 1D array.
        
        DP array evolution for amount=5, coins=[1,2,5]:
        
        Initial:    [1,0,0,0,0,0]
        After [1]:  [1,1,1,1,1,1]
        After [2]:  [1,1,2,2,3,3]
        After [5]:  [1,1,2,2,3,4]
        
        Time: O(n*a), Space: O(a)
        """
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case
        
        def print_state(coin: int):
            print(f"\nDP array after processing coin {coin}:")
            print(" ".join(f"{x:2}" for x in range(amount + 1)))
            print(" ".join(f"{x:2}" for x in dp))
        
        print_state("initial")
        
        for coin in reversed(coins):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1
            
            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a >= coin:
                    nextDP[a] += nextDP[a - coin]
            
            dp = nextDP
            print_state(coin)
            
        return dp[amount]

"""
COMPARISON OF APPROACHES:

1. Recursive:
   - Intuitive but inefficient
   - Shows all combinations explicitly
   - Exponential time complexity

2. Memoization:
   - Caches results for reuse
   - Good for sparse problems
   - Extra space for recursion stack

3. Bottom-Up DP:
   - Systematic table filling
   - No recursion overhead
   - Uses 2D array

4. Space-Optimized:
   - Most efficient space usage
   - Harder to track combinations
   - Best for production use

Key Patterns:
1. Overlapping subproblems
2. State representation (i, amount)
3. Transition: use or don't use coin
4. Base cases: amount=0 or no coins
"""

# Test with example
if __name__ == "__main__":
    solver = CoinChangeSolutions()
    amount = 5
    coins = [1,2,5]
    
    print("\nTesting all approaches with amount=5, coins=[1,2,5]")
    print("\n1. Recursive Solution:")
    print(f"Ways: {solver.recursive_change(amount, coins)}")
    
    print("\n2. Memoized Solution:")
    print(f"Ways: {solver.memoized_change(amount, coins)}")
    
    print("\n3. Bottom-Up DP Solution:")
    print(f"Ways: {solver.bottom_up_change(amount, coins)}")
    
    print("\n4. Space-Optimized Solution:")
    print(f"Ways: {solver.optimized_change(amount, coins)}")