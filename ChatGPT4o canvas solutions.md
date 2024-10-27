# coding-interview-preparation

A collection of reusable code snippets and implementations of coding patterns commonly seen in technical interviews. This repository covers 35 essential patterns, ranging from LeetCode and other coding challenges, aimed to improve problem-solving skills by recognizing and applying proven solutions.

## 📚 Credits

This repository is inspired by and references the following resources:

- **[15 LeetCode Patterns](https://blog.algomaster.io/p/15-leetcode-patterns)** by Ashish Pratap Singh (AlgoMaster Newsletter)
- **[20 Patterns to Master Dynamic Programming](https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming)** by Ashish Pratap Singh (AlgoMaster Newsletter)
- **[Video Tutorial](https://www.youtube.com/watch?v=DjYZk8nrXVY\&t=206s)** - An in-depth explanation of common coding interview patterns

These resources were instrumental in the development of this repository, and credit goes to the authors for the foundational patterns covered here.

## 🎯 How to Use This Repository

1. **Identify the Pattern**: Based on the problem statement, use the **Pattern Identification Guide** below to determine the relevant coding pattern.
2. **Explore the Pattern**: Go to the **Detailed Pattern Implementations** section to find a reusable code snippet and explanation of the pattern.
3. **Apply and Modify**: Adapt the code to solve specific problems by tweaking parameters or extending the logic as needed.
4. **Practice and Master**: Regularly revisit these patterns with different problems on platforms like LeetCode, HackerRank, and CodeSignal.

## 🕵️ Pattern Identification Guide

This guide will help you identify which pattern is best suited for a problem:

- **Prefix Sum**: Used for subarray sum calculations across multiple queries.
- **Two Pointers**: Best for sorted arrays, often used for finding pairs or reversing operations.
- **Sliding Window**: For problems involving contiguous subarrays or substrings with specific criteria.
- **Dynamic Programming**: When a problem has overlapping subproblems and can be divided into simpler, recursive subproblems.
- **Binary Search and Modified Variants**: Ideal for problems involving sorted or rotated arrays.

*(Refer to the **`Detailed Pattern Implementations`** section for a full list and more examples)*

## 🧐 Detailed Pattern Implementations

Here, we cover the 35 patterns with code snippets, explanations, and tips on when to apply each pattern. Each pattern has a highly modular, documented code function, making it easy to reuse across various problems.

### 1. Fibonacci Sequence

#### When to Use: Problems that exhibit recurrence relations like F(n) = F(n-1) + F(n-2).

```python
def fibonacci(n):
    """
    Computes the nth Fibonacci number using dynamic programming.
    Parameters:
    n (int): The position in the Fibonacci sequence to compute.
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1  # Base cases
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

### 2. Kadane's Algorithm

#### When to Use: Maximum subarray or subarray-related optimization problems.

```python
def max_subarray_sum(nums):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.
    Parameters:
    nums (list): List of integers.
    Returns:
    int: Maximum sum of any contiguous subarray.
    """
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    
    return max_global
```

### 3. 0/1 Knapsack

#### When to Use: Problems where items can only be included once, and you need to maximize value within constraints.

```python
def knapsack_01(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    Parameters:
    weights (list): List of weights for each item.
    values (list): List of values for each item.
    capacity (int): Maximum weight capacity of the knapsack.
    Returns:
    int: Maximum value that can be obtained with the given capacity.
    """
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]
```

### 4. Unbounded Knapsack

#### When to Use: Problems similar to 0/1 knapsack but where items can be chosen multiple times.

```python
def unbounded_knapsack(weights, values, capacity):
    """
    Solves the Unbounded Knapsack problem where each item can be picked multiple times.
    Parameters:
    weights (list): List of weights for each item.
    values (list): List of values for each item.
    capacity (int): Maximum weight capacity of the knapsack.
    Returns:
    int: Maximum value that can be obtained with the given capacity.
    """
    dp = [0] * (capacity + 1)
    
    for w in range(capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]
```

### 5. Longest Common Subsequence (LCS)

#### When to Use: Problems that involve finding the longest ordered subsequence that exists in two strings.

```python
def longest_common_subsequence(text1, text2):
    """
    Finds the length of the longest common subsequence between two strings.
    Parameters:
    text1 (str): First string.
    text2 (str): Second string.
    Returns:
    int: Length of the longest common subsequence.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]
```

### 6. Longest Increasing Subsequence (LIS)

#### When to Use: Problems involving finding the longest sequence of increasing elements in an array.

```python
def longest_increasing_subsequence(nums):
    """
    Finds the length of the longest increasing subsequence in a list of numbers.
    Parameters:
    nums (list): List of integers.
    Returns:
    int: Length of the longest increasing subsequence.
    """
    dp = [1] * len(nums)  # Initialize LIS length for each element as 1
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)  # The longest LIS across all elements
```

### 7. Palindromic Subsequence

#### When to Use: Problems involving finding palindromic subsequences or substrings in strings.

```python
def longest_palindromic_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence in a string.
    Parameters:
    s (str): Input string.
    Returns:
    int: Length of the longest palindromic subsequence.
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1  # Single character is a palindrome of length 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]
```

### 8. Edit Distance

#### When to Use: Problems involving converting one string to another using operations like insert, delete, or substitute.

```python
def edit_distance(word1, word2):
    """
    Calculates the minimum number of operations to convert one string to another.
    Parameters:
    word1 (str): Source string.
    word2 (str): Target string.
    Returns:
    int: Minimum edit distance (number of operations needed).
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting all characters in word1
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting all characters of word2
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match, no operation needed
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,     # Deletion
                    dp[i][j - 1] + 1,     # Insertion
                    dp[i - 1][j - 1] + 1  # Substitution
                )
    
    return dp[m][n]
```

### 9. Subset Sum

#### When to Use: Problems involving finding subsets of elements that add up to a specific target value.

```python
def subset_sum(nums, target):
    """
    Determines if there is a subset of the given list with a sum equal to the target value.
    Parameters:
    nums (list): List of non-negative integers.
    target (int): Target sum value.
    Returns:
    bool: True if there is a subset that adds up to the target, otherwise False.
    """
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True  # A sum of 0 is always possible with an empty subset
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][target]
```

### 10. String Partition

#### When to Use: Problems involving partitioning a string into smaller substrings that satisfy certain conditions.

```python
def min_cut_palindrome_partition(s):
    """
    Finds the minimum number of cuts needed to partition a string such that every substring is a palindrome.
    Parameters:
    s (str): Input string.
    Returns:
    int: Minimum number of cuts required.
    """
    n = len(s)
    dp = [0] * n
    palindrome = [[False] * n for _ in range(n)]
    
    for i in range(n):
        min_cut = i
        for j in range(i + 1):
            if s[i] == s[j] and (i - j < 2 or palindrome[j + 1][i - 1]):
                palindrome[j][i] = True
                min_cut = 0 if j == 0 else min(min_cut, dp[j - 1] + 1)
        dp[i] = min_cut
    
    return dp[-1]
```

### 11. Catalan Numbers

#### When to Use: Problems that involve counting the number of ways to arrange elements that follow certain recursive relationships, such as valid parentheses or binary search trees.

```python
def catalan_number(n):
    """
    Computes the nth Catalan number using dynamic programming.
    Parameters:
    n (int): The index of the Catalan number.
    Returns:
    int: The nth Catalan number.
    """
    if n == 0 or n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    
    return dp[n]
```

### 12. Matrix Chain Multiplication

#### When to Use: Problems involving determining the optimal order of operations to minimize the cost of performing a series of operations.

```python
def matrix_chain_order(dimensions):
    """
    Determines the minimum number of scalar multiplications needed to compute the matrix chain product.
    Parameters:
    dimensions (list): List of matrix dimensions.
    Returns:
    int: Minimum number of multiplications required.
    """
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]
```

### 13. Count Distinct Ways

#### When to Use: Problems involving counting the number of distinct ways to reach a particular state.

```python
def count_ways(n):
    """
    Counts the number of distinct ways to reach the nth step.
    Parameters:
    n (int): Number of steps.
    Returns:
    int: Number of distinct ways to reach the nth step.
    """
    if n == 0 or n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

### 14. DP on Grids

#### When to Use: Problems involving navigating or optimizing paths within a grid (2D array).

```python
def min_path_sum(grid):
    """
    Finds the minimum path sum from top left to bottom right of a grid.
    Parameters:
    grid (list of list of int): 2D list representing the grid.
    Returns:
    int: Minimum path sum from top left to bottom right.
    """
    m, n = len(grid), len(grid[0])
    
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]
    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]
    
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    
    return grid[m - 1][n - 1]
```

### 15. DP on Trees

#### When to Use: Problems involving tree-structured data represented by nodes and edges, where each node's value depends on its children or parents.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    """
    Finds the maximum path sum in a binary tree.
    Parameters:
    root (TreeNode): Root node of the binary tree.
    Returns:
    int: Maximum path sum.
    """
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left_max = max(dfs(node.left), 0)
        right_max = max(dfs(node.right), 0)
        max_sum = max(max_sum, left_max + right_max + node.val)
        
        return max(left_max, right_max) + node.val
    
    max_sum = float('-inf')
    dfs(root)
    return max_sum
```

### 16. DP on Graphs

#### When to Use: Problems involving graph structures, finding optimal paths, cycles, or connected components.

```python
def cheapest_flights_within_k_stops(n, flights, src, dst, k):
    """
    Finds the cheapest price for a flight from src to dst with at most k stops.
    Parameters:
    n (int): Number of nodes.
    flights (list of tuples): List of flights represented as (start, end, cost).
    src (int): Source node.
    dst (int): Destination node.
    k (int): Maximum number of stops allowed.
    Returns:
    int: Cheapest price or -1 if no such route exists.
    """
    from collections import deque
    import math
    
    graph = {i: [] for i in range(n)}
    for start, end, cost in flights:
        graph[start].append((end, cost))
    
    queue = deque([(src, 0, 0)])  # (current_node, current_cost, stops)
    min_cost = {src: 0}
    result = math.inf
    
    while queue:
        node, cost, stops = queue.popleft()
        if node == dst:
            result = min(result, cost)
            continue
        if stops > k:
            continue
        
        for neighbor, price in graph[node]:
            new_cost = cost + price
            if new_cost < min_cost.get(neighbor, math.inf):
                min_cost[neighbor] = new_cost
                queue.append((neighbor, new_cost, stops + 1))
    
    return result if result != math.inf else -1
```

### 17. Digit DP

#### When to Use: Problems involving counting or summing over a range of numbers based on digit properties.

```python
def count_numbers_with_unique_digits(n):
    """
    Counts how many numbers of length n have unique digits.
    Parameters:
    n (int): Length of the number.
    Returns:
    int: Count of numbers with unique digits.
    """
    if n == 0:
        return 1
    
    count = 10  # For n = 1
    unique_digits = 9
    available_numbers = 9
    
    for i in range(2, n + 1):
        unique_digits *= available_numbers
        count += unique_digits
        available_numbers -= 1
    
    return count
```

### 18. Bitmasking DP

#### When to Use: Problems involving subsets or combinations of elements with constraints.

```python
def shortest_path_visiting_all_nodes(graph):
    """
    Finds the shortest path length that visits all nodes in an undirected graph.
    Parameters:
    graph (list of list of int): Adjacency list representing the graph.
    Returns:
    int: Length of the shortest path visiting all nodes.
    """
    from collections import deque
    
    n = len(graph)
    queue = deque([(i, 1 << i, 0) for i in range(n)])  # (node, visited, cost)
    visited = {(i, 1 << i) for i in range(n)}
    
    while queue:
        node, mask, cost = queue.popleft()
        if mask == (1 << n) - 1:
            return cost
        
        for neighbor in graph[node]:
            next_mask = mask | (1 << neighbor)
            if (neighbor, next_mask) not in visited:
                queue.append((neighbor, next_mask, cost + 1))
                visited.add((neighbor, next_mask))
    
    return -1
```

### 19. Probability DP

#### When to Use: Problems involving probability calculations or expected values.

```python
def knight_probability(n, k, row, column):
    """
    Finds the probability that a knight remains on the board after k moves.
    Parameters:
    n (int): Size of the board (n x n).
    k (int): Number of moves.
    row (int): Starting row of the knight.
    column (int): Starting column of the knight.
    Returns:
    float: Probability that the knight remains on the board.
    """
    directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
    dp[0][row][column] = 1
    
    for step in range(1, k + 1):
        for r in range(n):
            for c in range(n):
                for dr, dc in directions:
                    prev_r, prev_c = r - dr, c - dc
                    if 0 <= prev_r < n and 0 <= prev_c < n:
                        dp[step][r][c] += dp[step - 1][prev_r][prev_c] / 8.0
    
    return sum(dp[k][r][c] for r in range(n) for c in range(n))
```

### 20. State Machine DP

#### When to Use: Problems involving modeling a series of states and transitions between these states.

```python
def max_profit_with_cooldown(prices):
    """
    Calculates the maximum profit that can be achieved with cooldowns between stock trades.
    Parameters:
    prices (list of int): List of stock prices.
    Returns:
    int: Maximum profit achievable.
    """
    if not prices:
        return 0
    
    n = len(prices)
    hold = [0] * n
    sell = [0] * n
    rest = [0] * n
    
    hold[0] = -prices[0]
    for i in range(1, n):
        hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
        sell[i] = hold[i - 1] + prices[i]
        rest[i] = max(rest[i - 1], sell[i - 1])
    
    return max(sell[-1], rest[-1])
```
```python
# Pattern 11: Catalan Numbers
def nth_catalan(n: int) -> int:
    """Calculates nth Catalan number using DP.
    
    Used for:
    - Count number of valid parentheses expressions
    - Count unique BST structures
    - Count ways to triangulate polygon
    
    Args:
        n: Position in Catalan sequence
        
    Returns:
        nth Catalan number
        
    Time: O(n²), Space: O(n)
    Example:
        >>> [nth_catalan(i) for i in range(5)]
        [1, 1, 2, 5, 14]
    """
    if n <= 1:
        return 1
        
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
            
    return dp[n]

def generate_parentheses(n: int) -> List[str]:
    """Generates all valid combinations of n pairs of parentheses.
    
    Time: O(4^n/sqrt(n)), Space: O(n)
    Example:
        >>> generate_parentheses(3)
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    """
    def backtrack(s: List[str], left: int, right: int) -> None:
        if len(s) == 2 * n:
            result.append(''.join(s))
            return
            
        if left < n:
            s.append('(')
            backtrack(s, left + 1, right)
            s.pop()
            
        if right < left:
            s.append(')')
            backtrack(s, left, right + 1)
            s.pop()
            
    result = []
    backtrack([], 0, 0)
    return result

# Pattern 12: Matrix Chain Multiplication
def matrix_chain_order(dimensions: List[int]) -> int:
    """Finds minimum multiplications needed for matrix chain.
    
    Args:
        dimensions: List where dimensions[i-1] x dimensions[i] is size of matrix i
        
    Returns:
        Minimum number of scalar multiplications needed
        
    Time: O(n³), Space: O(n²)
    Example:
        >>> matrix_chain_order([10, 30, 5, 60])
        4500  # ((A × B) × C)
    """
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = (dp[i][k] + dp[k+1][j] + 
                       dimensions[i] * dimensions[k+1] * dimensions[j+1])
                dp[i][j] = min(dp[i][j], cost)
                
    return dp[0][n-1]

# Pattern 13: Count Distinct Ways
def decode_ways(s: str) -> int:
    """Counts number of ways to decode string to letters (A=1, B=2, ..., Z=26).
    
    Time: O(n), Space: O(1)
    Example:
        >>> decode_ways("226")
        3  # "2,2,6", "22,6", "2,26"
    """
    if not s or s[0] == '0':
        return 0
        
    n = len(s)
    prev2, prev1 = 1, 1
    
    for i in range(1, n):
        curr = 0
        # Single digit
        if s[i] != '0':
            curr += prev1
        # Two digits
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            curr += prev2
        prev2, prev1 = prev1, curr
        
    return prev1

# Pattern 14: DP on Grids
def unique_paths(m: int, n: int) -> int:
    """Counts unique paths from top-left to bottom-right in grid.
    
    Can only move right or down.
    
    Time: O(m*n), Space: O(n)
    Example:
        >>> unique_paths(3, 7)
        28
    """
    dp = [1] * n  # First row all 1s
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
            
    return dp[n-1]

def min_path_sum(grid: List[List[int]]) -> int:
    """Finds path with minimum sum from top-left to bottom-right.
    
    Time: O(m*n), Space: O(n)
    Example:
        >>> min_path_sum([[1,3,1],[1,5,1],[4,2,1]])
        7  # Path: 1→3→1→1→1
    """
    m, n = len(grid), len(grid[0])
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    
    for i in range(m):
        for j in range(n):
            dp[j + 1] = min(dp[j], dp[j + 1]) + grid[i][j]
            
    return dp[n]

# Pattern 15: DP on Trees
def rob_tree(root: Optional[TreeNode]) -> int:
    """Finds maximum amount that can be robbed from binary tree house.
    
    Cannot rob directly connected houses.
    
    Time: O(n), Space: O(h)
    Example:
        >>> rob_tree([3,2,3,null,3,null,1])
        7  # Rob houses with values 3 + 3 + 1
    """
    def rob_subtree(node: Optional[TreeNode]) -> Tuple[int, int]:
        if not node:
            return 0, 0
            
        left_rob, left_not_rob = rob_subtree(node.left)
        right_rob, right_not_rob = rob_subtree(node.right)
        
        # If we rob this node
        rob = node.val + left_not_rob + right_not_rob
        # If we don't rob this node
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return rob, not_rob
        
    return max(rob_subtree(root))

# Pattern 16: DP on Graphs
def cheapest_flights(n: int, flights: List[List[int]], src: int, 
                    dst: int, k: int) -> int:
    """Finds cheapest price from src to dst with at most k stops.
    
    Time: O(k*|E|), Space: O(n)
    Example:
        >>> cheapest_flights(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
        200  # 0->1->2
    """
    prices = [float('inf')] * n
    prices[src] = 0
    
    for _ in range(k + 1):
        temp_prices = prices.copy()
        for s, d, p in flights:
            if prices[s] != float('inf'):
                temp_prices[d] = min(temp_prices[d], prices[s] + p)
        prices = temp_prices
        
    return prices[dst] if prices[dst] != float('inf') else -1

# Pattern 17: Digit DP
def count_numbers_with_unique_digits(n: int) -> int:
    """Counts numbers with unique digits from 0 to 10^n - 1.
    
    Time: O(n), Space: O(1)
    Example:
        >>> count_numbers_with_unique_digits(2)
        91  # 0-99 excluding numbers like 11, 22, etc.
    """
    if n == 0:
        return 1
    if n > 10:
        return 0
        
    used = [False] * 10
    
    def count_unique(pos: int, is_num: bool, tight: bool) -> int:
        if pos == 0:
            return 1
            
        count = 0
        # If no digit used yet, can start with 0
        if not is_num:
            count = count_unique(pos - 1, False, False)
            
        # Try each digit
        start = 0 if is_num else 1
        for d in range(start, 10):
            if not used[d]:
                used[d] = True
                count += count_unique(pos - 1, True, False)
                used[d] = False
                
        return count
        
    return count_unique(n, False, True)

# Pattern 18: Bitmasking DP
def shortest_path_visiting_all_nodes(graph: List[List[int]]) -> int:
    """Finds shortest path that visits all nodes in graph.
    
    Time: O(n * 2^n), Space: O(n * 2^n)
    Example:
        >>> shortest_path_visiting_all_nodes([[1,2,3],[0],[0],[0]])
        4
    """
    n = len(graph)
    ending_mask = (1 << n) - 1
    queue = deque([(1 << i, i, 0) for i in range(n)])
    seen = {(1 << i, i) for i in range(n)}
    
    while queue:
        mask, node, dist = queue.popleft()
        if mask == ending_mask:
            return dist
            
        for next_node in graph[node]:
            next_mask = mask | (1 << next_node)
            if (next_mask, next_node) not in seen:
                seen.add((next_mask, next_node))
                queue.append((next_mask, next_node, dist + 1))
                
    return -1

# Pattern 19: Probability DP
def knight_probability(n: int, k: int, row: int, column: int) -> float:
    """Calculates probability knight remains on board after k moves.
    
    Time: O(k*n²), Space: O(n²)
    Example:
        >>> knight_probability(3, 2, 0, 0)
        0.0625
    """
    moves = [
        (-2,-1), (-2,1), (-1,-2), (-1,2),
        (1,-2), (1,2), (2,-1), (2,1)
    ]
    
    dp = [[0] * n for _ in range(n)]
    dp[row][column] = 1
    
    for _ in range(k):
        next_dp = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                for dr, dc in moves:
                    next_r, next_c = r + dr, c + dc
                    if 0 <= next_r < n and 0 <= next_c < n:
                        next_dp[next_r][next_c] += dp[r][c] / 8.0
        dp = next_dp
        
    return sum(sum(row) for row in dp)

# Pattern 20: State Machine DP
def best_time_to_buy_sell_stock(prices: List[int]) -> int:
    """Maximizes profit from stock trading with cooldown.
    
    Time: O(n), Space: O(1)
    Example:
        >>> best_time_to_buy_sell_stock([1,2,3,0,2])
        3  # Buy at 1, sell at 3, buy at 0, sell at 2
    """
    sold = float('-inf')  # Just sold
    held = float('-inf')  # Holding stock
    reset = 0  # Ready to buy
    
    for price in prices:
        prev_sold = sold
        sold = held + price  # Sell stock
        held = max(held, reset - price)  # Keep holding or buy
        reset = max(reset, prev_sold)  # Stay ready or cooldown
        
    return max(sold, reset)
```

This completes all 20 DP patterns with:
1. Clear implementations
2. Detailed comments
3. Time/Space complexity
4. Example usage
5. Problem-specific explanations

Would you like me to:
1. Add more example problems?
2. Include test cases?
3. Add pattern variations?
4. Expand any particular pattern?
5. Add more detailed explanations?

Each pattern is implemented with real interview/LeetCode problems in mind and includes optimizations commonly expected in coding interviews.
## 🚀 Conclusion

This repository is designed to serve as a toolkit for mastering the most essential coding patterns. Each function provided here is modular and documented thoroughly, allowing you to quickly adapt the logic to specific coding problems. By regularly practicing and revisiting these patterns, you’ll build the intuition needed to tackle a wide range of coding challenges in interviews and real-world applications.

### 🛠️ Happy Coding!

