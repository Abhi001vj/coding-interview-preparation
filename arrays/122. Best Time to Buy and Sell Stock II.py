# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

# Constraints:

# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104

"""
Best Time to Buy and Sell Stock II - Solution Evolution
====================================================

Problem Definition:
-----------------
Given daily stock prices, find maximum profit by buying and selling multiple times.
Rules:
1. Can only hold one share at a time
2. Can buy and sell on the same day
3. Can make multiple transactions

Visual Example:
-------------
Prices: [7, 1, 5, 3, 6, 4]

         7
         │     6
         │     │   4
         │  5  │   │
         │  │  │   │
         │  │ 3│   │
    1    │  │  │   │
    │    │  │  │   │
    │    │  │  │   │
    │    │  │  │   │
────┴────┴──┴──┴───┴──
Day  1  2  3  4  5  6

Profitable trades: 
1. Buy at 1, sell at 5 (profit: 4)
2. Buy at 3, sell at 6 (profit: 3)
Total profit: 7
"""

from typing import List

class StockTradingSolutions:
    def approach1_brute_force(self, prices: List[int]) -> int:
        """
        Brute Force Approach - Generate All Possible Transaction Combinations
        -----------------------------------------------------------------
        Strategy:
        1. Try every possible combination of buy and sell days
        2. For each buy day, try all future sell days
        3. Recursively try remaining days for next transaction
        
        Time: O(2^n) - for each day, we have 2 choices (trade or not)
        Space: O(n) - recursion stack
        """
        def try_all_combinations(index: int, can_buy: bool) -> int:
            # Base case: reached end of prices
            if index >= len(prices):
                return 0
                
            # Initialize maximum profit for current state
            max_profit = 0
            
            if can_buy:
                # Option 1: Buy stock today
                buy_profit = try_all_combinations(index + 1, False) - prices[index]
                # Option 2: Don't buy today
                skip_profit = try_all_combinations(index + 1, True)
                max_profit = max(buy_profit, skip_profit)
            else:
                # Option 1: Sell stock today
                sell_profit = try_all_combinations(index + 1, True) + prices[index]
                # Option 2: Don't sell today
                skip_profit = try_all_combinations(index + 1, False)
                max_profit = max(sell_profit, skip_profit)
                
            return max_profit
            
        return try_all_combinations(0, True)

    def approach2_dynamic_programming(self, prices: List[int]) -> int:
        """
        Dynamic Programming Approach - State Transition
        -------------------------------------------
        Strategy:
        1. Use DP array to store max profit for each state
        2. State: (day, holding_stock)
        3. Transitions: buy, sell, or skip
        
        Time: O(n) - process each day once
        Space: O(n) - DP array
        """
        n = len(prices)
        # dp[i][0] = max profit on day i without holding stock
        # dp[i][1] = max profit on day i while holding stock
        dp = [[0] * 2 for _ in range(n + 1)]
        
        # Initialize: cannot hold stock on day 0
        dp[0][1] = float('-inf')
        
        for i in range(n):
            # Not holding stock
            dp[i + 1][0] = max(dp[i][0],                # skip
                              dp[i][1] + prices[i])     # sell
            
            # Holding stock
            dp[i + 1][1] = max(dp[i][1],               # skip
                              dp[i][0] - prices[i])     # buy
            
        return dp[n][0]

    def approach3_greedy(self, prices: List[int]) -> int:
        """
        Greedy Approach - Valley-Peak Pattern
        ----------------------------------
        Strategy:
        1. Buy at every valley
        2. Sell at every peak
        3. Accumulate all positive price differences
        
        Time: O(n) - single pass through prices
        Space: O(1) - constant extra space
        
        Key Insight: Any sequence of profitable trades can be broken down
        into a series of adjacent day trades that give the same profit.
        """
        total_profit = 0
        
        for i in range(1, len(prices)):
            # If price went up, we could have bought yesterday and sold today
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
                
        return total_profit

    def approach4_state_machine(self, prices: List[int]) -> int:
        """
        State Machine Approach - Two States
        --------------------------------
        Strategy:
        1. Maintain two states: holding and not holding stock
        2. Update states based on best possible action
        3. Transitions between states represent buy/sell actions
        
        Time: O(n) - single pass
        Space: O(1) - constant space
        """
        holding = float('-inf')  # Maximum profit while holding stock
        not_holding = 0         # Maximum profit while not holding stock
        
        for price in prices:
            # Previous best profit becomes our new reference
            prev_holding = holding
            prev_not_holding = not_holding
            
            # Update maximum profit for each state
            holding = max(prev_holding,           # keep holding
                         prev_not_holding - price) # buy stock
            
            not_holding = max(prev_not_holding,    # keep not holding
                            prev_holding + price)   # sell stock
            
        return not_holding

    def demonstrate_solutions(self):
        """Test all approaches with example cases."""
        test_cases = [
            ([7,1,5,3,6,4], "Example 1: Multiple trades"),
            ([1,2,3,4,5], "Example 2: Ascending prices"),
            ([7,6,4,3,1], "Example 3: Descending prices"),
            ([3,3,3,3], "Example 4: Flat prices")
        ]
        
        approaches = [
            (self.approach1_brute_force, "Brute Force"),
            (self.approach2_dynamic_programming, "Dynamic Programming"),
            (self.approach3_greedy, "Greedy"),
            (self.approach4_state_machine, "State Machine")
        ]
        
        print("Testing All Approaches:")
        print("=====================")
        
        for prices, case_name in test_cases:
            print(f"\n{case_name}:")
            print(f"Prices: {prices}")
            for approach, name in approaches:
                result = approach(prices)
                print(f"{name}: {result}")

def main():
    """
    Main function to demonstrate solutions and insights.
    """
    solver = StockTradingSolutions()
    solver.demonstrate_solutions()
    
    print("\nKey Insights and Patterns:")
    print("=========================")
    print("1. Problem Patterns:")
    print("   - State machine (holding vs not holding)")
    print("   - Valley-peak pattern")
    print("   - Optimal substructure")
    
    print("\n2. Solution Evolution:")
    print("   - Brute force → DP → Greedy")
    print("   - Space optimization")
    print("   - State reduction")
    
    print("\n3. Trade-offs:")
    print("   - Time vs Space complexity")
    print("   - Code complexity vs Performance")
    print("   - Memory usage vs Clarity")

if __name__ == "__main__":
    main()

"""
Additional Notes:
---------------
1. DSA Patterns Used:
   - State machines
   - Dynamic programming
   - Greedy algorithms
   - Valley-peak pattern

2. Interview Tips:
   - Start with brute force
   - Optimize step by step
   - Consider space optimization
   - Explain trade-offs

3. Common Pitfalls:
   - Missing edge cases
   - Overcomplicated DP
   - Not recognizing greedy opportunity
   - Incorrect state transitions
"""

"""
Valley-Peak Solution Analysis - Best Time to Buy and Sell Stock II
===============================================================

Key Insight:
The solution uses a valley-peak pattern where we:
1. Find a valley (local minimum) to buy
2. Find next peak (local maximum) to sell
3. Repeat until end of array

Visual Example:
Prices: [7,1,5,3,6,4]

         7
         │     6
         │     │   4
         │  5  │   │
         │  │  │   │
         │  │ 3│   │
    1    │  │  │   │
    │    │  │  │   │
    │    │  │  │   │
    │    │  │  │   │
────┴────┴──┴──┴───┴──
Day  1  2  3  4  5  6

Valley-Peak Pairs:
Valley (1) -> Peak (5): Profit = 4
Valley (3) -> Peak (6): Profit = 3
Total Profit = 7
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Valley-Peak Pattern Solution
        ---------------------------
        Strategy: Identify local minima (valleys) and maxima (peaks)
        to determine optimal buy and sell points.
        
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(1) - constant extra space
        """
        if not prices:  # Handle empty input
            return 0
            
        i = 0
        lo = prices[0]  # Current valley (buy point)
        hi = prices[0]  # Current peak (sell point)
        profit = 0
        n = len(prices)
        
        while i < n - 1:
            # Find next valley (local minimum)
            # Keep moving while price is decreasing
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            lo = prices[i]  # Found a valley
            
            # Find next peak (local maximum)
            # Keep moving while price is increasing
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            hi = prices[i]  # Found a peak
            
            # Add profit from this valley-peak pair
            profit += hi - lo
        
        return profit

def demonstrate_valley_peak():
    """
    Demonstrate how the valley-peak solution works with examples
    """
    test_cases = [
        ([7,1,5,3,6,4], "Multiple Valleys and Peaks"),
        ([1,2,3,4,5], "Strictly Increasing"),
        ([5,4,3,2,1], "Strictly Decreasing"),
        ([3,3,3,3], "Flat Prices")
    ]
    
    solution = Solution()
    
    print("Valley-Peak Pattern Analysis:")
    print("============================")
    
    for prices, description in test_cases:
        print(f"\n{description}")
        print(f"Prices: {prices}")
        
        # Track valleys and peaks found
        i = 0
        valleys = []
        peaks = []
        
        while i < len(prices) - 1:
            # Find valley
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valleys.append((i, prices[i]))
            
            # Find peak
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peaks.append((i, prices[i]))
        
        print("Valleys found:", [f"Day {v[0]}: {v[1]}" for v in valleys])
        print("Peaks found:", [f"Day {p[0]}: {p[1]}" for p in peaks])
        print(f"Total Profit: {solution.maxProfit(prices)}")

"""
Pattern Analysis:
---------------
1. Algorithm Type: Two-Pointer / Valley-Peak Pattern
   - Uses single pointer (i) to traverse array
   - Identifies local minima and maxima

2. Key DSA Concepts:
   - Local minima/maxima finding
   - Sequential pattern matching
   - Greedy approach (take every profitable trade)

3. Implementation Patterns:
   - Double while-loop structure
   - Boundary checking (i < n-1)
   - Accumulator pattern (profit sum)

4. Optimization Features:
   - Single pass through array (O(n))
   - Constant extra space (O(1))
   - No need to store all valleys/peaks

5. Edge Cases Handled:
   - Strictly increasing prices
   - Strictly decreasing prices
   - Flat prices
   - Last element processing

Common Patterns with Other Problems:
---------------------------------
1. Stock Problems:
   - Valley-peak pattern common in stock problems
   - Local optima identification
   - Cumulative profit calculation

2. Array Traversal:
   - Boundary checking
   - Two-pointer variation
   - Local property checking
"""

if __name__ == "__main__":
    demonstrate_valley_peak()