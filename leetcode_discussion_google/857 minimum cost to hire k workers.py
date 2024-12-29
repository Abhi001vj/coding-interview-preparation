# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/
# 857. Minimum Cost to Hire K Workers
# Hard
# Topics
# Companies
# There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

# We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

# Every worker in the paid group must be paid at least their minimum wage expectation.
# In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
# Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Input: quality = [10,20,5], wage = [70,50,30], k = 2
# Output: 105.00000
# Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
# Example 2:

# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
# Output: 30.66667
# Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.
 

# Constraints:

# n == quality.length == wage.length
# 1 <= k <= n <= 104
# 1 <= quality[i], wage[i] <= 104

"""
Minimum Cost to Hire K Workers (LeetCode 857)

Core Challenge:
- Hire exactly k workers
- Must pay at least minimum wage
- Pay must be proportional to quality
- Find minimum total cost

Key Insights:
1. Pay-to-Quality Ratio: wage/quality must be same for all selected workers
2. This ratio must be at least max(wage[i]/quality[i]) among selected workers
3. Total cost = ratio * sum(qualities)

Let's analyze with examples and develop optimal solution:

Approach: Ratio-Based with Max Heap
Time: O(N log N)
Space: O(N)

Visual Example:
quality = [10,20,5], wage = [70,50,30], k = 2

1. Calculate wage/quality ratios:
Worker 0: 70/10 = 7
Worker 1: 50/20 = 2.5
Worker 2: 30/5 = 6

2. Sort by ratio:
Worker 1: ratio=2.5, quality=20  │
Worker 2: ratio=6, quality=5     ├── sorted workers
Worker 0: ratio=7, quality=10    │

3. Process workers maintaining k lowest qualities:
For ratio=2.5:
heap = [20], sum = 20
cost = 2.5 * 20 = 50

For ratio=6:
heap = [20,5], sum = 25
cost = 6 * 25 = 150

For ratio=7:
heap = [10,5], sum = 15
cost = 7 * 15 = 105  ← minimum cost!
"""

from heapq import heappush, heappop
import math

def mincostToHireWorkers(quality: List[int], wage: List[int], k: int) -> float:
    """
    Calculate minimum cost to hire k workers satisfying wage and quality constraints.
    
    Algorithm:
    1. Sort workers by wage/quality ratio
    2. Process each worker as captain (setting the ratio)
    3. Use max heap to maintain k lowest quality workers
    4. Update minimum cost when valid group found
    
    Time: O(N log N) - dominated by sorting
    Space: O(N) - for storing workers and heap
    """
    # Combine worker info and sort by wage/quality ratio
    workers = sorted([(w/q, q, w) for q, w in zip(quality, wage)])
    
    # Use max heap to track k lowest qualities
    heap = []
    quality_sum = 0
    min_cost = math.inf
    
    """
    Visualization of algorithm:
    For each ratio (r), we want k workers with:
    1. Lowest possible qualities
    2. Ratios <= r (automatically satisfied by sorting)
    
    Example State:
    ratio = 6
    heap = [20,5]  (max heap of qualities)
    sum = 25
    cost = 6 * 25 = 150
    
    ┌────────────┐
    │  Max Heap  │
    │   [20,5]   │
    └────────────┘
    """
    
    # Process each worker as potential captain
    for ratio, q, w in workers:
        # Add current worker's quality to heap
        heappush(heap, -q)  # negative for max heap
        quality_sum += q
        
        # If we have more than k workers, remove highest quality
        if len(heap) > k:
            quality_sum += heappop(heap)  # remove highest quality
            
        # If we have k workers, calculate cost
        if len(heap) == k:
            min_cost = min(min_cost, ratio * quality_sum)
    
    return min_cost

"""
Example Walkthrough:
quality = [10,20,5], wage = [70,50,30], k = 2

1. Initial sorting:
   [(2.5, 20, 50), (6, 5, 30), (7, 10, 70)]
   
2. Processing ratio=2.5:
   heap = [-20]
   sum = 20
   cost = 2.5 * 20 = 50
   
3. Processing ratio=6:
   heap = [-20, -5]
   sum = 25
   cost = 6 * 25 = 150
   
4. Processing ratio=7:
   heap = [-10, -5]
   sum = 15
   cost = 7 * 15 = 105 ← minimum!

Proof of Correctness:
1. Why sort by ratio?
   - Any valid solution must have same ratio for all workers
   - This ratio must be ≥ max(wage[i]/quality[i]) of selected workers
   
2. Why process each worker as captain?
   - Captain sets the minimum ratio for group
   - All workers with lower ratios can be paid proportionally
   
3. Why keep k lowest qualities?
   - Total cost = ratio * sum(qualities)
   - For given ratio, want minimum possible quality sum

Common Edge Cases:
1. All workers have same ratio
2. Single worker selected (k=1)
3. All workers must be selected (k=n)
4. Very large quality/wage differences

Test Cases:
"""

def test_mincostToHireWorkers():
    test_cases = [
        {
            "quality": [10,20,5],
            "wage": [70,50,30],
            "k": 2,
            "expected": 105.0
        },
        {
            "quality": [3,1,10,10,1],
            "wage": [4,8,2,2,7],
            "k": 3,
            "expected": 30.666666666666664
        },
        # Edge cases
        {
            "quality": [1,1,1],
            "wage": [10,10,10],
            "k": 2,
            "expected": 20.0
        }
    ]
    
    for i, test in enumerate(test_cases):
        result = mincostToHireWorkers(
            test["quality"],
            test["wage"],
            test["k"]
        )
        assert abs(result - test["expected"]) < 1e-5, f"Failed case {i+1}"
    
    print("All test cases passed!")

"""
Detailed State Analysis for Minimum Cost K Workers
Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3

1. Initial Processing:
   Calculate wage/quality ratios and sort workers
   Format: (ratio, quality, wage)

   Initial Workers:
   Index   Quality   Wage    Ratio
   0       3         4       1.33
   1       1         8       8.00
   2       10        2       0.20
   3       10        2       0.20
   4       1         7       7.00

   After Sorting by Ratio:
   [(0.20, 10, 2),   # Worker 2
    (0.20, 10, 2),   # Worker 3
    (1.33, 3, 4),    # Worker 0
    (7.00, 1, 7),    # Worker 4
    (8.00, 1, 8)]    # Worker 1

2. Processing Each Worker as Captain:
   We'll maintain a max heap of qualities and track total quality sum

State Changes for Worker 2 (ratio = 0.20):
---------------------------------------
Current ratio = 0.20
Add quality 10 to heap
Heap: [-10]
Quality sum: 10
Workers: 1 (need 3)
Cost = 0.20 * 10 = 2.0 (not valid yet, need 3 workers)

Visual:
MaxHeap: [10]
         ↑
Current sum = 10

State Changes for Worker 3 (ratio = 0.20):
---------------------------------------
Current ratio = 0.20
Add quality 10 to heap
Heap: [-10, -10]
Quality sum: 20
Workers: 2 (need 3)
Cost = 0.20 * 20 = 4.0 (not valid yet, need 3 workers)

Visual:
MaxHeap: [10,10]
          ↑
Current sum = 20

State Changes for Worker 0 (ratio = 1.33):
---------------------------------------
Current ratio = 1.33
Add quality 3 to heap
Heap: [-10, -10, -3]
Quality sum: 23
Workers: 3 (exactly k!)
Cost = 1.33 * 23 = 30.66667 ← First valid solution!

Visual:
MaxHeap: [10,10,3]
          ↑
Current sum = 23

State Changes for Worker 4 (ratio = 7.00):
---------------------------------------
Current ratio = 7.00
Add quality 1 to heap
Heap: [-10, -10, -3, -1]
Remove largest: -10
Heap: [-10, -3, -1]
Quality sum: 14
Workers: 3
Cost = 7.00 * 14 = 98.0 (worse than previous)

Visual:
MaxHeap: [10,3,1]
          ↑
Current sum = 14

State Changes for Worker 5 (ratio = 8.00):
---------------------------------------
Current ratio = 8.00
Add quality 1 to heap
Heap: [-10, -3, -1, -1]
Remove largest: -10
Heap: [-3, -1, -1]
Quality sum: 5
Workers: 3
Cost = 8.00 * 5 = 40.0 (worse than previous)

Visual:
MaxHeap: [3,1,1]
         ↑
Current sum = 5

Final Result:
-----------
Minimum cost = 30.66667
Selected workers:
1. Worker 2: quality=10, wage=2
2. Worker 3: quality=10, wage=2
3. Worker 0: quality=3, wage=4

Why This is Optimal:
1. First two workers have lowest ratio (0.2)
   - They're most cost-efficient
   - Even though quality is high (10), wage is low (2)

2. Adding Worker 0 (ratio 1.33):
   - Forces us to pay ratio=1.33 to everyone
   - Total cost = 1.33 * (10+10+3) = 30.66667

3. Other combinations are more expensive:
   Using smallest qualities (1,1,3):
   - Would need ratio=8.0 (from Worker 1)
   - Cost = 8.0 * (1+1+3) = 40.0

Heap Operations Explained:
-------------------------
1. Using max heap to maintain smallest k qualities
2. When we exceed k elements:
   - Remove largest quality
   - This minimizes quality sum for current ratio
3. Negative values in heap because Python has min heap
   - Store as negative to simulate max heap

Cost Calculation:
----------------
For each worker (ratio r):
1. Maintain k smallest qualities in heap
2. Total cost = r * sum(qualities)
3. Must use worker's ratio as minimum
   (can't pay less than their wage/quality ratio)

This way we:
1. Try each possible minimum ratio
2. For each ratio, use optimal (smallest) qualities
3. Find global minimum cost across all ratios
"""

Let me break down the thought process that leads to this solution. This kind of reasoning is exactly what's expected in a Google L5 interview.

First, let's understand what we're trying to optimize:

pythonCopy# Given:
- We must pay proportional to quality
- Each worker has minimum wage requirement
- Need exactly k workers

Key Observation 1: Pay Ratio

pythonCopy# If we hire workers A and B:
A's pay / A's quality = B's pay / B's quality = some ratio 'r'

# Therefore:
- Every worker's pay = r * (their quality)
- Total cost = r * sum(qualities of selected workers)

Key Observation 2: Minimum Ratio

pythonCopy# For each worker:
minimum_wage/quality = minimum ratio needed

Example:
Worker: quality=10, wage=20
- minimum ratio = 20/10 = 2
- can't pay less than $2 per quality unit
- can pay more than $2 per quality unit

Critical Insight - Setting the Ratio:

pythonCopy# When we select a group:
- Must pay at least their minimum ratio requirements
- Therefore, ratio must be ≥ max(wage[i]/quality[i]) of selected workers

Example:
Worker1: ratio=2.0
Worker2: ratio=3.0
Worker3: ratio=1.0
If we select all three → must use ratio=3.0

This leads to our strategy:

pythonCopyFor each possible ratio r (try each worker's ratio):
    1. Can only use workers with minimum ratio ≤ r
    2. Total cost = r * sum(qualities)
    3. Want smallest possible sum of qualities

Why Max Heap for Qualities:

pythonCopy# For given ratio r:
Cost = r * sum(qualities)
r is fixed, so minimize sum(qualities)

Example:
ratio = 3.0
qualities available = [10,2,5,8,1]
k = 3
Want 3 smallest qualities → need max heap to remove largest!

Why not use ratio in heap?

pythonCopy# Common wrong approach:
"Let's keep track of ratios in heap"

Problem: Ratio isn't what we're minimizing!
- We MUST use maximum ratio among selected workers
- After that, ratio is FIXED
- Only thing we can minimize is sum of qualities

Pattern Recognition Tips:

pythonCopy1. When you see "proportional":
   → Look for ratios

2. When you have a fixed quantity (k):
   → Often need heap to maintain top/bottom k

3. When minimizing product (ratio * sum):
   → Try fixing one term, minimize other

4. When you can't use all items:
   → Consider sorting by some criteria
Here's how we could arrive at this solution in an interview:

Start with Brute Force:

pythonCopy# Try all combinations of k workers
for each combination:
    calculate minimum ratio needed
    calculate total cost
# O(n^k) - clearly too slow

Optimize - Key Insight:

pythonCopy# Observation:
- If worker W is in optimal solution with ratio r
- All workers with lower minimum ratio requirements can accept r
- So sort by ratio, try each worker as "captain" (setting ratio)

Further Optimization:

pythonCopy# For each ratio:
- Need k workers with smallest qualities
- Max heap helps maintain smallest k qualities efficiently
The pattern here is:

Start with constraints (proportional pay, minimum wage)
Find what's fixed vs what we can optimize
Sort by one criteria (ratio)
Use heap to optimize other criteria (qualities)

This type of problem appears in different forms:

Maximum profit with fixed cost ratio
Resource allocation with proportional constraints
Any problem involving picking k items with ratio constraints