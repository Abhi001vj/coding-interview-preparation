# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0
 

# Constraints:

# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
"""
Problem: Best Time to Buy and Sell Stock with Cooldown (LeetCode 309)
Input: prices = [1,2,3,0,2]
Output: 3

Complete solution with visualizations and step-by-step analysis
Detailed DFS Path Analysis for prices = [1,2,3,0,2]

STEP BY STEP PATH TRACE:
----------------------
Initial call: dfs(0, True) - Day 0, Can Buy
                                        State: (i, buying, cash)
                                        (0, True, 0)
                                   /                         \
                   Buy at day 0                        Skip/Cooldown
              (1, False, -1)                           (1, True, 0)
              /            \                          /            \
    Sell at day 1    Skip day 1              Buy at day 1    Skip day 1
(3, True, 1)    (2, False, -1)        (2, False, -2)    (2, True, 0)
     |               |                       |               |
     ...             ...                     ...             ...

Full Path of Optimal Solution:
----------------------------
1. Start:     (0, True, 0)    - Can buy at day 0
2. Action:    Buy at day 0    - Pay $1
   State:     (1, False, -1)  - Can't buy, have stock
3. Action:    Sell at day 1   - Get $2
   State:     (3, True, 1)    - Must cooldown day 2
4. Action:    Buy at day 3    - Pay $0
   State:     (4, False, 1)   - Can't buy, have stock
5. Action:    Sell at day 4   - Get $2
   Final:     (5, True, 3)    - Total profit $3

DETAILED LOGIC EXPLANATION:
------------------------
1. Why subtract price when buying:
   dfs(i + 1, False) - prices[i]
   Example at i=0:
   - Current price = $1
   - Future profit from dfs(1, False)
   - We SPEND money to buy (-1)
   - Total = future_profit - current_price

2. Why add price when selling:
   dfs(i + 2, True) + prices[i]
   Example at i=1:
   - Current price = $2
   - Future profit from dfs(3, True)
   - We GAIN money from sale (+2)
   - Total = future_profit + current_price

3. Why i+2 for sell but i+1 for buy:
   - After buying: Can sell next day (i+1)
   - After selling: Must cooldown one day, so next action at (i+2)

   
"""
"""
Example: prices = [1,2,3,0,2]

COMPLETE STATE WALKTHROUGH:
------------------------
Initial Call: dfs(0, buying=True)
Current State: At day 0, price=1, CAN_BUY
Choices:
1. Buy at $1:
   - Spend $1
   - Move to dfs(1, buying=False)
2. Cooldown:
   - Spend $0
   - Move to dfs(1, buying=True)

Let's follow BOTH paths completely:

PATH 1 - BUYING AT DAY 0:
-----------------------
Day 0: (buying=True, profit=0)
Action: BUY at $1
New State: (day=1, buying=False, profit=-1)

    Day 1: (buying=False, profit=-1)
    Action: SELL at $2
    New State: (day=3, buying=True, profit=1) [Skip day 2 for cooldown]
    
        Day 3: (buying=True, profit=1)
        Action: BUY at $0
        New State: (day=4, buying=False, profit=1)
        
            Day 4: (buying=False, profit=1)
            Action: SELL at $2
            Final State: (profit=3)

PATH 2 - COOLDOWN AT DAY 0:
-------------------------
Day 0: (buying=True, profit=0)
Action: COOLDOWN
New State: (day=1, buying=True, profit=0)

    Day 1: (buying=True, profit=0)
    Action: BUY at $2
    New State: (day=2, buying=False, profit=-2)
    
        Day 2: (buying=False, profit=-2)
        Action: SELL at $3
        New State: (day=4, buying=True, profit=1)
        
            Day 4: (no more valid moves)
            Final State: (profit=1)

DETAILED MEMOIZATION TABLE FILLING:
--------------------------------
memo[(4, True)] = 0     # Base case, no more days
memo[(4, False)] = 2    # Can only sell at $2
memo[(3, True)] = 2     # Can buy at $0, then sell at $2
memo[(3, False)] = 2    # Can cooldown then sell at $2
memo[(2, True)] = 2     # Max profit possible from day 2
memo[(2, False)] = 3    # Can sell at $3
memo[(1, True)] = 2     # Max profit from buying path
memo[(1, False)] = 3    # Max profit from selling path
memo[(0, True)] = 3     # Maximum final profit

OPTIMAL PATH BREAKDOWN:
--------------------
1. Day 0: BUY at $1
   - State: buying=True
   - Action: Buy
   - Cash flow: -$1
   - New profit: -$1

2. Day 1: SELL at $2
   - State: buying=False
   - Action: Sell
   - Cash flow: +$2
   - New profit: +$1

3. Day 2: COOLDOWN (forced)
   - State: buying=True
   - Action: None
   - Cash flow: $0
   - Profit stays: +$1

4. Day 3: BUY at $0
   - State: buying=True
   - Action: Buy
   - Cash flow: -$0
   - Profit stays: +$1

5. Day 4: SELL at $2
   - State: buying=False
   - Action: Sell
   - Cash flow: +$2
   - Final profit: +$3

WHY THIS IS OPTIMAL:
-----------------
1. First transaction (Buy@1, Sell@2):
   - Profit: +$1
   - Early opportunity to make profit

2. Second transaction (Buy@0, Sell@2):
   - Additional profit: +$2
   - Takes advantage of lowest price

Alternative paths yield less profit:
1. Wait and buy at day 1 (@$2): 
   - Can only make one transaction
   - Maximum profit would be +$1

2. Wait for price drop:
   - Misses the first profit opportunity
   - Cannot recover the lost potential
"""
"""
Stock Trading with Cooldown Solution
Example: prices = [1,2,3,0,2]

COMPLETE DECISION TREE:
                                                 (0,T,$0)
                                    /                              \
                            Buy@$1                              Cooldown
                    (1,F,-$1)                                  (1,T,$0)
                /            \                            /               \
        Sell@$2           Cooldown                   Buy@$2           Cooldown
    (3,T,+$1)          (2,F,-$1)                 (2,F,-$2)          (2,T,$0)
    /         \        /         \               /         \        /         \
Buy@$0    Cooldown  Sell@$3   Cooldown     Sell@$3     Cooldown  Buy@$3   Cooldown
(4,F,+$1) (4,T,+$1) (4,T,+$2) (3,F,-$1)   (4,T,+$1)  (3,F,-$2) (3,F,-$3) (3,T,$0)
   |          |        |          |            |          |         |         |
Sell@$2    End      End        Buy@$0        End       Sell@$0    ...       ...
(END,+$3)  (+$1)    (+$2)     (END,+$0)     (+$1)     (END,-$2)

Where: (day,can_buy,profit) and T=True(can buy), F=False(has stock)

OPTIMAL PATH HIGHLIGHTED:
(0,T,$0) → Buy@$1 → (1,F,-$1) → Sell@$2 → (3,T,+$1) → Buy@$0 → (4,F,+$1) → Sell@$2 → (END,+$3)
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Calculate maximum profit from stock trading with cooldown.
        Time: O(n), Space: O(n), where n is length of prices
        
        Step-by-step approach:
        1. Use memoization to store max profit for each state (day, can_buy)
        2. At each state, try either:
           - cooldown (skip day)
           - buy/sell (if allowed)
        3. Return maximum profit possible from day 0
        """
        
        # Initialize memoization dictionary
        # Key: (day, can_buy)
        # Value: maximum profit possible from this state
        dp = {}
        
        def dfs(i: int, buying: bool) -> int:
            """
            DFS helper function to explore all possible states
            
            Parameters:
            i (int): Current day
            buying (bool): True if we can buy, False if we can sell
            
            Returns:
            int: Maximum profit possible from this state
            
            State Transitions:
            If buying:
                1. Buy: profit -= price[i], next_state = not buying
                2. Cooldown: keep same state
            If not buying (have stock):
                1. Sell: profit += price[i], next_state = buying, skip one day
                2. Cooldown: keep same state
            """
            
            # Base case: reached end of prices array
            if i >= len(prices):
                return 0
                
            # Check if this state was already computed
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # Try cooldown (skip to next day, keep same state)
            # This establishes a baseline profit to compare against
            cooldown = dfs(i + 1, buying)
            
            if buying:
                # We can buy stock
                # Try buying at current price and move to selling state
                # Subtract current price from future profit
                buy = dfs(i + 1, not buying) - prices[i]
                # Take maximum of buying now or cooldown
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # We can sell stock
                # Try selling at current price and move to buying state after cooldown
                # Add current price to future profit
                sell = dfs(i + 2, not buying) + prices[i]
                # Take maximum of selling now or cooldown
                dp[(i, buying)] = max(sell, cooldown)
                
            return dp[(i, buying)]
        
        # Start from day 0 in buying state
        return dfs(0, True)

"""
STEP-BY-STEP EXECUTION for prices=[1,2,3,0,2]:

1. Initial Call: dfs(0, True)
   - Can either buy at $1 or cooldown
   - Try both paths

2. Buy Path from dfs(0, True):
   - Buy at $1: profit = -1
   - Move to dfs(1, False)
   - Can either sell at $2 or cooldown
   - Selling gives better result
   - After selling, forced cooldown brings to day 3
   - Buy at $0, then sell at $2
   - Total profit: 3

3. Cooldown Path from dfs(0, True):
   - Skip day 0, move to dfs(1, True)
   - Can buy at $2 or cooldown again
   - All subsequent paths give less profit
   - Maximum profit through this path: 1

4. Memoization Table Filling:
   dp[(0, True)] = 3    # Maximum profit from start
   dp[(1, False)] = 3   # After buying at day 0
   dp[(1, True)] = 2    # After cooldown at day 0
   dp[(2, False)] = 2   # After cooldown at day 1
   dp[(3, True)] = 2    # After selling at day 1
   dp[(4, False)] = 2   # After buying at day 3
   
5. Return Value:
   dp[(0, True)] = 3    # Maximum profit possible

Key Decisions at Each Step:
Day 0: Buy ($1)  - Better than cooldown
Day 1: Sell ($2) - Better than holding
Day 2: Forced cooldown
Day 3: Buy ($0)  - Better than cooldown
Day 4: Sell ($2) - Last opportunity
"""
class StockTrader:
    def maxProfit(self, prices: list[int]) -> int:
        """
        -------------------------------------------
        VISUALIZATION OF POSSIBLE STATES AND ACTIONS
        -------------------------------------------
        Example: prices = [1,2,3,0,2]
        
        Complete State Space Tree:
                                    (0,buy)
                            /                   \
                (-1,1,sell)                    (0,1,buy)
                /          \                  /          \
        (1,2,cool)    (-1,2,cool)    (-3,2,sell)    (0,2,buy)
           |              |              |              |
           ...            ...            ...            ...
        
        Timeline of Optimal Solution:
        Day:     0    1    2    3    4
        Price:   1    2    3    0    2
        Action:  Buy  Sell Cool Buy  Sell
        Cash:    -1   +1   +1   +1   +3
        
        State Transitions Rules:
        1. After Buy:
           - Can only Sell next day
           - Profit decreases by price
        
        2. After Sell:
           - Must Cooldown next day
           - Profit increases by price
        
        3. After Cooldown:
           - Can either Buy or Cooldown
           - Profit stays same
        
        -------------------------------------
        IMPLEMENTATION 1: RECURSIVE (BRUTE FORCE)
        -------------------------------------
        Time: O(2^n) - two choices at each step
        Space: O(n) - recursion stack depth
        """
        def recursive_solution(prices: list[int]) -> int:
            def dfs(i: int, buying: bool) -> int:
                # Base case: reached end of prices
                if i >= len(prices):
                    return 0
                
                # Try cooldown (skip this day)
                cooldown = dfs(i + 1, buying)
                
                if buying:
                    # Try buying: lose prices[i], can sell next day
                    buy = dfs(i + 1, False) - prices[i]
                    return max(buy, cooldown)
                else:
                    # Try selling: gain prices[i], must cooldown next day
                    sell = dfs(i + 2, True) + prices[i]
                    return max(sell, cooldown)
            
            return dfs(0, True)
        
        """
        -------------------------------------
        IMPLEMENTATION 2: MEMOIZATION (TOP-DOWN DP)
        -------------------------------------
        Time: O(n) - each state computed once
        Space: O(n) - memo table size
        
        Memo Table Evolution for prices=[1,2,3,0,2]:
        
        Initial State:
        Day→    0    1    2    3    4
        Buy:    -    -    -    -    -
        Sell:   -    -    -    -    -
        
        After some calls:
        Day→    0    1    2    3    4
        Buy:    3    2    2    2    0
        Sell:   2    3    2    2    2
        
        Final State:
        Day→    0    1    2    3    4
        Buy:    3    2    2    2    0
        Sell:   2    3    2    2    2
        """
        def memoization_solution(prices: list[int]) -> int:
            memo = {}
            
            def dfs(i: int, buying: bool) -> int:
                if i >= len(prices):
                    return 0
                if (i, buying) in memo:
                    return memo[(i, buying)]
                
                cooldown = dfs(i + 1, buying)
                if buying:
                    buy = dfs(i + 1, False) - prices[i]
                    memo[(i, buying)] = max(buy, cooldown)
                else:
                    sell = dfs(i + 2, True) + prices[i]
                    memo[(i, buying)] = max(sell, cooldown)
                return memo[(i, buying)]
            
            return dfs(0, True)
        
        """
        -------------------------------------
        IMPLEMENTATION 3: BOTTOM-UP DP
        -------------------------------------
        Time: O(n) - fill table once
        Space: O(n) - dp table size
        
        DP Table Evolution for prices=[1,2,3,0,2]:
        
        Initial State:
        Day↓  Buy  Sell
        4     0    0
        3     0    0
        2     0    0
        1     0    0
        0     0    0
        
        After Day 4:
        Day↓  Buy  Sell
        4     0    2    <- Can only sell for price 2
        3     0    0
        2     0    0
        1     0    0
        0     0    0
        
        After Day 3:
        Day↓  Buy  Sell
        4     0    2
        3     2    0    <- Buy at 0, sell later at 2
        2     0    0
        1     0    0
        0     0    0
        
        Final State:
        Day↓  Buy  Sell
        4     0    2
        3     2    0
        2     2    3
        1     2    2
        0     3    2    <- Maximum profit 3
        """
        def bottom_up_solution(prices: list[int]) -> int:
            if not prices:
                return 0
            
            n = len(prices)
            dp = [[0] * 2 for _ in range(n + 1)]
            
            for i in range(n - 1, -1, -1):
                for buying in [True, False]:
                    if buying:
                        buy = dp[i + 1][0] - prices[i]
                        cooldown = dp[i + 1][1]
                        dp[i][1] = max(buy, cooldown)
                    else:
                        sell = (dp[i + 2][1] if i + 2 < n else 0) + prices[i]
                        cooldown = dp[i + 1][0]
                        dp[i][0] = max(sell, cooldown)
            
            return dp[0][1]
        
        """
        -------------------------------------
        IMPLEMENTATION 4: SPACE-OPTIMIZED DP
        -------------------------------------
        Time: O(n) - single pass through prices
        Space: O(1) - constant extra space
        
        Variable Evolution for prices=[1,2,3,0,2]:
        
        Initial State:
        dp1_buy = 0, dp1_sell = 0, dp2_buy = 0
        
        Day 4 (price = 2):
        dp1_buy = 0, dp1_sell = 2, dp2_buy = 0
        
        Day 3 (price = 0):
        dp1_buy = 2, dp1_sell = 0, dp2_buy = 0
        
        Final Evolution:
        dp1_buy = 3, dp1_sell = 2, dp2_buy = 2
        """
        def space_optimized_solution(prices: list[int]) -> int:
            n = len(prices)
            dp1_buy = dp1_sell = 0
            dp2_buy = 0
            
            for i in range(n - 1, -1, -1):
                dp_buy = max(dp1_sell - prices[i], dp1_buy)
                dp_sell = max(dp2_buy + prices[i], dp1_sell)
                
                dp2_buy = dp1_buy
                dp1_buy, dp1_sell = dp_buy, dp_sell
            
            return dp1_buy
        
        # Return result from most optimized solution
        return space_optimized_solution(prices)

# Test the solution
if __name__ == "__main__":
    prices = [1,2,3,0,2]
    trader = StockTrader()
    profit = trader.maxProfit(prices)
    print(f"Maximum profit for prices {prices}: {profit}")