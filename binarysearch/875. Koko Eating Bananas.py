# https://leetcode.com/problems/koko-eating-bananas/description/
# 875. Koko Eating Bananas
# Solved
# Medium
# Topics
# Companies
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

```python
def minEatingSpeed(piles: List[int], h: int) -> int:
    """
    Binary Search approach to find minimum eating speed k
    
    Example 1 Detailed Analysis:
    piles = [3,6,7,11], h = 8
    
    Search Space Analysis:
    - Minimum speed possible = 1 (eat 1 banana/hour)
    - Maximum speed needed = max(piles) = 11 (no need to eat faster)
    
    Binary Search Steps:
    1. Initial Range: [1, 11]
       Mid = 6
       Hours needed at k=6:
       [3,6,7,11] -> [1,1,2,2] = 6 hours (valid)
       Can we go slower? Try left half
       
    2. Range: [1, 5]
       Mid = 3
       Hours needed at k=3:
       [3,6,7,11] -> [1,2,3,4] = 10 hours (invalid)
       Must go faster, try right half
       
    3. Range: [4, 5]
       Mid = 4
       Hours needed at k=4:
       [3,6,7,11] -> [1,2,2,3] = 8 hours (valid)
       Can we go slower? Left half empty
       
    Therefore, k = 4 is minimum valid speed
    
    Time Visualization for k=4:
    Hour 1: Pile 1 (3) -> [0,6,7,11]     ate 3
    Hour 2: Pile 2 (6) -> [0,2,7,11]     ate 4
    Hour 3: Pile 2 (2) -> [0,0,7,11]     ate 2
    Hour 4: Pile 3 (7) -> [0,0,3,11]     ate 4
    Hour 5: Pile 3 (3) -> [0,0,0,11]     ate 3
    Hour 6: Pile 4 (11) -> [0,0,0,7]     ate 4
    Hour 7: Pile 4 (7) -> [0,0,0,3]      ate 4
    Hour 8: Pile 4 (3) -> [0,0,0,0]      ate 3
    """
    def canEatAll(speed: int) -> bool:
        """
        Helper function to check if Koko can eat all bananas at given speed
        Returns hours needed for current speed
        
        Example calculation for speed=4:
        Pile 1 (3): ceil(3/4) = 1 hour
        Pile 2 (6): ceil(6/4) = 2 hours
        Pile 3 (7): ceil(7/4) = 2 hours
        Pile 4 (11): ceil(11/4) = 3 hours
        Total = 8 hours
        """
        return sum((pile - 1) // speed + 1 for pile in piles) <= h
    
    # Binary search for minimum valid k
    left, right = 1, max(piles)  # Initialize search range
    result = right  # Start with maximum possible k
    
    while left <= right:
        mid = (left + right) // 2
        if canEatAll(mid):
            # Speed is valid, try to go slower
            result = mid
            right = mid - 1
        else:
            # Speed is too slow, must go faster
            left = mid + 1
            
    return result

def test_with_visualization():
    """
    Test cases with detailed visualization
    """
    test_cases = [
        ([3,6,7,11], 8),
        ([30,11,23,4,20], 5),
        ([30,11,23,4,20], 6)
    ]
    
    for piles, h in test_cases:
        k = minEatingSpeed(piles, h)
        print(f"\nTest case: piles={piles}, h={h}")
        print(f"Minimum speed k={k}")
        
        # Visualize eating process
        remaining = piles.copy()
        for hour in range(h):
            for i in range(len(remaining)):
                if remaining[i] > 0:
                    eaten = min(k, remaining[i])
                    remaining[i] -= eaten
                    print(f"Hour {hour+1}: Ate {eaten} from pile {i+1}")
                    print(f"Remaining: {remaining}")
                    break

"""
Time & Space Complexity Analysis:
--------------------------------
Time: O(n * log m) where:
- n = length of piles
- m = max(piles)
- log m for binary search range
- n for checking each speed

Space: O(1) constant extra space

Pattern Recognition:
------------------
1. Binary Search on Answer
   - Monotonic condition: if speed k works, k+1 also works
   - Clear bounds: [1, max(piles)]
   
2. Ceiling Division Pattern
   - Hours needed = ceil(pile/speed)
   - Optimization: (pile-1)//speed + 1

Edge Cases:
----------
1. h = len(piles): Must eat each pile in 1 hour
2. Single pile: Direct calculation
3. h = sum(piles): Can eat 1 banana/hour
4. Very large piles: Need to handle integer overflow
"""
```
```python
def minEatingSpeed(piles: List[int], h: int) -> int:
    """
    CEILING DIVISION EXPLANATION
    --------------------------
    Let's use pile = 7 bananas, speed = 3 bananas/hour
    
    Regular Division: 7/3 = 2.333...
    Ceiling Division: ceil(7/3) = 3 hours
    
    Why 3 hours is correct:
    Hour 1: Eats 3 bananas, 4 remain
    Hour 2: Eats 3 bananas, 1 remains
    Hour 3: Eats 1 banana, 0 remain
    
    If we used floor division (7//3 = 2):
    - Would only account for 6 bananas (3 * 2)
    - Would miss the last banana!
    
    Examples with different piles:
    
    1. Pile = 10, Speed = 3
       Regular: 10/3 = 3.333...
       Ceiling: ceil(10/3) = 4 hours needed
       Actual eating:
       Hour 1: 3 bananas (7 left)
       Hour 2: 3 bananas (4 left)
       Hour 3: 3 bananas (1 left)
       Hour 4: 1 banana  (0 left)
    
    2. Pile = 6, Speed = 3
       Regular: 6/3 = 2
       Ceiling: ceil(6/3) = 2 hours needed
       Actual eating:
       Hour 1: 3 bananas (3 left)
       Hour 2: 3 bananas (0 left)
    """
    def calculateHours(speed: int) -> int:
        # Three ways to implement ceiling division:
        
        # Method 1: Using (n-1)//k + 1
        hours1 = sum((pile - 1) // speed + 1 for pile in piles)
        
        # Method 2: Using math.ceil
        import math
        hours2 = sum(math.ceil(pile / speed) for pile in piles)
        
        # Method 3: Using (n + k - 1) // k
        hours3 = sum((pile + speed - 1) // speed for pile in piles)
        
        return hours1
    
```python
def minEatingSpeed(piles: List[int], h: int) -> int:
    """
    CEILING DIVISION EXPLANATION
    --------------------------
    Let's use pile = 7 bananas, speed = 3 bananas/hour
    
    Regular Division: 7/3 = 2.333...
    Ceiling Division: ceil(7/3) = 3 hours
    
    Why 3 hours is correct:
    Hour 1: Eats 3 bananas, 4 remain
    Hour 2: Eats 3 bananas, 1 remains
    Hour 3: Eats 1 banana, 0 remain
    
    If we used floor division (7//3 = 2):
    - Would only account for 6 bananas (3 * 2)
    - Would miss the last banana!
    
    Examples with different piles:
    
    1. Pile = 10, Speed = 3
       Regular: 10/3 = 3.333...
       Ceiling: ceil(10/3) = 4 hours needed
       Actual eating:
       Hour 1: 3 bananas (7 left)
       Hour 2: 3 bananas (4 left)
       Hour 3: 3 bananas (1 left)
       Hour 4: 1 banana  (0 left)
    
    2. Pile = 6, Speed = 3
       Regular: 6/3 = 2
       Ceiling: ceil(6/3) = 2 hours needed
       Actual eating:
       Hour 1: 3 bananas (3 left)
       Hour 2: 3 bananas (0 left)
    """
    def calculateHours(speed: int) -> int:
        # Three ways to implement ceiling division:
        
        # Method 1: Using (n-1)//k + 1
        hours1 = sum((pile - 1) // speed + 1 for pile in piles)
        
        # Method 2: Using math.ceil
        import math
        hours2 = sum(math.ceil(pile / speed) for pile in piles)
        
        # Method 3: Using (n + k - 1) // k
        hours3 = sum((pile + speed - 1) // speed for pile in piles)
        
        return hours1
    
    # Example showing why ceiling is needed:
    """
    For piles = [3,6,7,11], speed = 4:
    
    Pile 1 (3 bananas):
    Regular: 3/4 = 0.75
    Ceiling: ceil(3/4) = 1 hour needed
    Reality: Must spend 1 full hour
    
    Pile 2 (6 bananas):
    Regular: 6/4 = 1.5
    Ceiling: ceil(6/4) = 2 hours needed
    Reality: 
    Hour 1: 4 bananas
    Hour 2: 2 bananas
    
    Pile 3 (7 bananas):
    Regular: 7/4 = 1.75
    Ceiling: ceil(7/4) = 2 hours needed
    Reality:
    Hour 1: 4 bananas
    Hour 2: 3 bananas
    
    Pile 4 (11 bananas):
    Regular: 11/4 = 2.75
    Ceiling: ceil(11/4) = 3 hours needed
    Reality:
    Hour 1: 4 bananas
    Hour 2: 4 bananas
    Hour 3: 3 bananas
    """
    
    left, right = 1, max(piles)
    result = right
    
    while left <= right:
        k = (left + right) // 2
        if calculateHours(k) <= h:
            result = k
            right = k - 1
        else:
            left = k + 1
            
    return result
```
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        if h >= sum(piles):
            return 1
            
        left = (sum(piles) + h - 1) // h 
        right = max(piles)
        result = right
        
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
                if hours > h: 
                    break
                    
            if hours <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
                
        return result