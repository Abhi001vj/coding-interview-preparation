# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 121. Best Time to Buy and Sell Stock
# Easy
# Topics
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

```python
"""
STOCK PROFIT MAXIMIZATION: Complete Analysis
=========================================

Pattern Recognition:
1. Two Pointers
2. Sliding Window
3. Kadane's Algorithm variant
4. Dynamic Programming
"""

def brute_force_solution(prices: List[int]) -> int:
    """
    Approach 1: Brute Force
    Pattern: Compare each possible buy-sell pair
    
    Visual Example: prices = [7,1,5,3,6,4]
    
    Comparison Matrix (* marks valid profits):
    Buy\Sell  7  1  5  3  6  4
    7         0  -6 -2 -4 -1 -3
    1         x  0  *4 *2 *5 *3
    5         x  x  0  -2 *1 -1
    3         x  x  x  0  *3 *1
    6         x  x  x  x  0  -2
    4         x  x  x  x  x  0
    
    Time: O(n²)
    Space: O(1)
    """
    n = len(prices)
    max_profit = 0
    
    for buy in range(n-1):
        for sell in range(buy+1, n):
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
            
    return max_profit

def sliding_window_solution(prices: List[int]) -> int:
    """
    Approach 2: Sliding Window
    Pattern: Track min price and max profit
    
    Example: [7,1,5,3,6,4]
    
    Step-by-step:
    Price  Min   Max_Profit  Explanation
    7      7     0          First price
    1      1     0          New min, no profit
    5      1     4          Potential profit: 5-1=4
    3      1     4          No better profit
    6      1     5          Better profit: 6-1=5
    4      1     5          No better profit
    
    Time: O(n)
    Space: O(1)
    """
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Try to find lower buy price
        min_price = min(min_price, price)
        # Try to find better profit
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)
        
    return max_profit

def dp_solution(prices: List[int]) -> int:
    """
    Approach 3: Dynamic Programming
    Pattern: State transition based on buy/sell decisions
    
    Example: [7,1,5,3,6,4]
    
    State array represents max profit possible by day i:
    Day   Price   Min so far   Max Profit
    0     7       7           0
    1     1       1           0
    2     5       1           4
    3     3       1           4
    4     6       1           5
    5     4       1           5
    
    Time: O(n)
    Space: O(1)
    """
    if not prices:
        return 0
        
    min_price = prices[0]
    dp = [0] * len(prices)
    
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i-1], prices[i] - min_price)
        
    return dp[-1]

def kadane_variant_solution(prices: List[int]) -> int:
    """
    Approach 4: Kadane's Algorithm Variant
    Pattern: Maximum Subarray Difference
    
    Example: [7,1,5,3,6,4]
    
    Convert to daily changes:
    Prices:   [7,1,5,3,6,4]
    Changes:   [-6,4,-2,3,-2]
    
    Track best sequence of changes:
    Change  Current  Max_Profit
    -6      0        0
    4       4        4
    -2      2        4
    3       5        5
    -2      3        5
    
    Time: O(n)
    Space: O(1)
    """
    max_profit = current_profit = 0
    
    for i in range(1, len(prices)):
        # Calculate daily change
        change = prices[i] - prices[i-1]
        # Update current profit (don't go below 0)
        current_profit = max(0, current_profit + change)
        # Update max profit seen so far
        max_profit = max(max_profit, current_profit)
        
    return max_profit

"""
DETAILED ANALYSIS
---------------

Visual Analysis for [7,1,5,3,6,4]:

Timeline visualization:
Day:     1  2  3  4  5  6
Price:   7  1  5  3  6  4
Profit:  0  0  4  2  5  3
MinSoFar:7  1  1  1  1  1
MaxProfit:0  0  4  4  5  5

Key Decision Points:
1. Day 2: Price drops to 1 → New minimum
2. Day 3: Price rises to 5 → Potential profit 4
3. Day 4: Price drops to 3 → Keep previous profit
4. Day 5: Price rises to 6 → New max profit 5
5. Day 6: Price drops to 4 → Keep max profit 5

COMPLEXITY ANALYSIS
-----------------
1. Brute Force:
   Time: O(n²) - Check every pair
   Space: O(1) - Constant space

2. Sliding Window:
   Time: O(n) - Single pass
   Space: O(1) - Two variables

3. Dynamic Programming:
   Time: O(n) - Single pass
   Space: O(1) - Optimized to constant

4. Kadane Variant:
   Time: O(n) - Single pass
   Space: O(1) - Constant space

EDGE CASES
---------
1. Empty array: return 0
2. Single element: return 0
3. Decreasing prices: return 0
4. Equal prices: return 0
5. Very large arrays
6. Negative prices (not in constraints)

OPTIMIZATION TECHNIQUES
---------------------
1. Early termination:
   - If array is sorted in descending order
   - If max profit already found
   
2. Space optimization:
   - Avoid storing all states in DP
   - Use variables instead of arrays
   
3. Time optimization:
   - Single pass algorithms
   - Maintain running min/max
"""

```python
def maxProfit_bruteforce(prices: List[int]) -> int:
    """
    BRUTE FORCE SOLUTION
    ===================
    Example: prices = [7,1,5,3,6,4]
    
    Complete iteration visualization:
    Buy  Sell  Calculation   Profit  MaxProfit
    -------------------------------------------
    7    1     1-7 = -6     0       0
    7    5     5-7 = -2     0       0
    7    3     3-7 = -4     0       0
    7    6     6-7 = -1     0       0
    7    4     4-7 = -3     0       0
    
    1    5     5-1 = 4      4       4
    1    3     3-1 = 2      2       4
    1    6     6-1 = 5      5       5   ← Best profit found
    1    4     4-1 = 3      3       5
    
    5    3     3-5 = -2     0       5
    5    6     6-5 = 1      1       5
    5    4     4-5 = -1     0       5
    
    3    6     6-3 = 3      3       5
    3    4     4-3 = 1      1       5
    
    6    4     4-6 = -2     0       5
    
    Final profit: 5
    """
    res = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell = prices[j]
            res = max(res, sell - buy)
    return res

def maxProfit_twopointers(prices: List[int]) -> int:
    """
    TWO POINTERS SOLUTION
    ====================
    Example: prices = [7,1,5,3,6,4]
    
    Step by step pointer movement:
    
    Initial: l=0, r=1
    [7→,1,5,3,6,4]
     L R
    profit = 1-7 = -6, l moves to r
    
    Step 1: l=1, r=2
    [7,1→,5,3,6,4]
        L R
    profit = 5-1 = 4, maxP = 4
    
    Step 2: l=1, r=3
    [7,1→,5,3,6,4]
        L   R
    profit = 3-1 = 2, maxP = 4
    
    Step 3: l=1, r=4
    [7,1→,5,3,6,4]
        L     R
    profit = 6-1 = 5, maxP = 5
    
    Step 4: l=1, r=5
    [7,1→,5,3,6,4]
        L       R
    profit = 4-1 = 3, maxP = 5
    
    Visual state tracking:
    L  R  Buy  Sell  Profit  MaxProfit
    0  1   7    1     -6       0
    1  2   1    5      4       4
    1  3   1    3      2       4
    1  4   1    6      5       5
    1  5   1    4      3       5
    """
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP

def maxProfit_dp(prices: List[int]) -> int:
    """
    DYNAMIC PROGRAMMING SOLUTION
    ==========================
    Example: prices = [7,1,5,3,6,4]
    
    State evolution table:
    Index  Price  MinBuy  Profit  MaxProfit
    -------------------------------------
    0       7      7       0       0    Initial
    1       1      1       0       0    New minimum
    2       5      1       4       4    First profit
    3       3      1       2       4    No change
    4       6      1       5       5    New max profit
    5       4      1       3       5    No change
    
    Visual profit calculation at each step:
    
    Step 1: price = 7
    minBuy = 7, maxP = 0
    [7→,1,5,3,6,4]
    
    Step 2: price = 1
    minBuy = 1, maxP = 0
    [7,1→,5,3,6,4]
    
    Step 3: price = 5
    profit = 5-1 = 4
    minBuy = 1, maxP = 4
    [7,1,5→,3,6,4]
    
    Step 4: price = 3
    profit = 3-1 = 2
    minBuy = 1, maxP = 4
    [7,1,5,3→,6,4]
    
    Step 5: price = 6
    profit = 6-1 = 5
    minBuy = 1, maxP = 5
    [7,1,5,3,6→,4]
    
    Step 6: price = 4
    profit = 4-1 = 3
    minBuy = 1, maxP = 5
    [7,1,5,3,6,4→]
    """
    maxP = 0
    minBuy = prices[0]
    
    for sell in prices:
        # Try to maximize profit with current sell price
        maxP = max(maxP, sell - minBuy)
        # Update minimum buy price if found lower
        minBuy = min(minBuy, sell)
    return maxP

"""
COMPARISON OF APPROACHES
======================

1. Brute Force
   Pros:
   - Simple to understand and implement
   - Works for small inputs
   Cons:
   - O(n²) time complexity
   - Redundant calculations
   
2. Two Pointers
   Pros:
   - O(n) time complexity
   - Intuitive sliding window approach
   - Space efficient
   Cons:
   - Need to understand pointer movement logic
   
3. Dynamic Programming
   Pros:
   - O(n) time complexity
   - Most elegant solution
   - Easy to extend for variations
   Cons:
   - Might be harder to understand initially

SPACE-TIME COMPLEXITY ANALYSIS
============================

1. Brute Force:
   Time: O(n²) - nested loops
   Space: O(1) - single variable

2. Two Pointers:
   Time: O(n) - single pass
   Space: O(1) - two pointers

3. Dynamic Programming:
   Time: O(n) - single pass
   Space: O(1) - two variables

EDGE CASES AND HANDLING
=====================
1. Empty array:
   - All solutions handle with initial returns
   
2. Single element:
   - Returns 0 (can't buy and sell same day)
   
3. Decreasing prices:
   - Returns 0 (no profit possible)
   
4. Equal prices:
   - Returns 0 (no profit possible)
"""