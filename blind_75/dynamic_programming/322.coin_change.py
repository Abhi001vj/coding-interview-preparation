# https://leetcode.com/problems/coin-change/
# 322. Coin Change
# Medium
# Topics
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


class Solution:
    def coinChange(self, coins, amount):
        # Create dp array with amount + 1 as initial value (impossible value)
        dp = [amount + 1] * (amount + 1)
        # Base case: 0 amount needs 0 coins
        dp[0] = 0
        
        # For each amount from 1 to target amount
        for i in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                # If the coin value is less than or equal to current amount
                if coin <= i:
                    # Take minimum of current solution and 1 + solution for (amount - coin)
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        # If no solution found, return -1, else return the solution
        return dp[amount] if dp[amount] != amount + 1 else -1