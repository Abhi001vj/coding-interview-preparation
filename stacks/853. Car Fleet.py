# https://leetcode.com/problems/car-fleet/description/
# 853. Car Fleet
# Medium
# Topics
# Companies
# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

# You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

# Return the number of car fleets that will arrive at the destination.

 

# Example 1:

# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

# Output: 3

# Explanation:

# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
# The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
# Example 2:

# Input: target = 10, position = [3], speed = [3]

# Output: 1

# Explanation:

# There is only one car, hence there is only one fleet.
# Example 3:

# Input: target = 100, position = [0,2,4], speed = [4,2,1]

# Output: 1

# Explanation:

# The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
# Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 

# Constraints:

# n == position.length == speed.length
# 1 <= n <= 105
# 0 < target <= 106
# 0 <= position[i] < target
# All the values of position are unique.
# 0 < speed[i] <= 106
"""
CAR FLEET PROBLEM: Comprehensive Analysis
======================================

Pattern Recognition:
1. Monotonic Stack pattern
2. Time to destination calculation
3. Sorting + Stack combination
4. Collision point calculation

Key Insights:
1. Cars can only slow down, never speed up
2. Later positioned cars determine fleet formation
3. Time to target is key for fleet formation
4. Sort by position for easier processing
"""
1. Stack
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
Time & Space Complexity
Time complexity: 
O
(
n
log
⁡
n
)
O(nlogn)
Space complexity: 
O
(
n
)
O(n)
2. Iteration
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets
Time & Space Complexity
Time complexity: 
O
(
n
log
⁡
n
)
O(nlogn)
Space complexity: 
O
(
n
)
O(n)

```python
def carFleet_stack(target: int, position: List[int], speed: List[int]) -> int:
    """
    Stack Approach Detailed Example:
    target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    
    1. Create and Sort Position-Speed Pairs (Descending):
    Before sort: [(10,2), (8,4), (0,1), (5,1), (3,3)]
    After sort:  [(10,2), (8,4), (5,1), (3,3), (0,1)]
                  Right → Left (Cars closer to target first)
    
    2. Process Each Car and Track Time to Target:
    
    Car 1 (pos=10, speed=2):
        time = (12-10)/2 = 1.0
        stack = [1.0]
        
    Car 2 (pos=8, speed=4):
        time = (12-8)/4 = 1.0
        stack = [1.0, 1.0]
        1.0 <= 1.0 → Pop last time
        stack = [1.0]  # Forms fleet with Car 1
        
    Car 3 (pos=5, speed=1):
        time = (12-5)/1 = 7.0
        stack = [1.0, 7.0]
        7.0 > 1.0 → Keep separate fleet
        
    Car 4 (pos=3, speed=3):
        time = (12-3)/3 = 3.0
        stack = [1.0, 7.0, 3.0]
        3.0 <= 7.0 → Pop last time
        stack = [1.0, 7.0]  # Will catch up to Car 3
        
    Car 5 (pos=0, speed=1):
        time = (12-0)/1 = 12.0
        stack = [1.0, 7.0, 12.0]
        12.0 > 7.0 → Keep separate fleet
        
    Final stack = [1.0, 7.0, 12.0]
    Number of fleets = 3
    """
    # Create and sort position-speed pairs
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)  # Sort by position descending
    
    stack = []
    for p, s in pair:
        time = (target - p) / s
        stack.append(time)
        # If current car catches up to car in front
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()  # Remove current car (becomes part of fleet)
    return len(stack)

def carFleet_iteration(target: int, position: List[int], speed: List[int]) -> int:
    """
    Iteration Approach Detailed Example:
    target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    
    1. Initial Sort (Same as stack approach):
    Sorted pairs: [(10,2), (8,4), (5,1), (3,3), (0,1)]
    
    2. Process Cars Sequentially:
    
    First Car (pos=10, speed=2):
        time = (12-10)/2 = 1.0
        prevTime = 1.0
        fleets = 1
        
    Second Car (pos=8, speed=4):
        time = (12-8)/4 = 1.0
        1.0 <= prevTime (1.0) → Same fleet
        fleets = 1
        
    Third Car (pos=5, speed=1):
        time = (12-5)/1 = 7.0
        7.0 > prevTime (1.0) → New fleet
        prevTime = 7.0
        fleets = 2
        
    Fourth Car (pos=3, speed=3):
        time = (12-3)/3 = 3.0
        3.0 <= prevTime (7.0) → Same fleet
        fleets = 2
        
    Fifth Car (pos=0, speed=1):
        time = (12-0)/1 = 12.0
        12.0 > prevTime (7.0) → New fleet
        prevTime = 12.0
        fleets = 3
    
    Visual Timeline:
    t=0:   0---3---5---8---10--|12
           *   *   *   *   *    target
           
    t=1:   1---6---6---12--12--|12
           *   *   *   [Fleet1] 
           
    t=3:   3---12--8---12--12--|12
           *   [F2] *   [F1]
           
    t=7:   7---12--12--12--12--|12
           *   [Fleet2]  [F1]
           
    t=12:  12--12--12--12--12--|12
           [F3][Fleet2]  [F1]
    """
    # Create and sort pairs
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    
    if not pair: 
        return 0
        
    fleets = 1  # Start with first car as a fleet
    prevTime = (target - pair[0][0]) / pair[0][1]
    
    # Check each car against previous fleet
    for i in range(1, len(pair)):
        currPos, currSpeed = pair[i]
        currTime = (target - currPos) / currSpeed
        
        # If current car takes longer, it forms new fleet
        if currTime > prevTime:
            fleets += 1
            prevTime = currTime
            
    return fleets

"""
Key Differences Between Approaches:

1. State Management:
   Stack: Uses stack to track fleet times
   Iteration: Uses single variable for previous fleet time

2. Memory Usage:
   Stack: O(n) for stack in worst case
   Iteration: O(1) extra space (excluding sort space)

3. Code Clarity:
   Stack: More intuitive for visualizing fleets
   Iteration: More straightforward logic

4. Performance:
   Both O(n log n) due to sorting
   Iteration might be slightly faster due to less overhead

Common Elements:
1. Sort by position in descending order
2. Compare arrival times to determine fleets
3. Both handle same edge cases
4. Both give same results
"""
def car_fleet_monotonic_stack(target: int, position: List[int], speed: List[int]) -> int:
    """
    Approach 1: Monotonic Stack
    Pattern: Decreasing monotonic stack of arrival times
    
    Example: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    
    Step 1: Sort by position (descending)
    Position: [10, 8, 5, 3, 0]
    Speed:    [2,  4, 1, 3, 1]
    
    Time to target calculation:
    Car 1: (12-10)/2 = 1.0 hours
    Car 2: (12-8)/4  = 1.0 hours
    Car 3: (12-5)/1  = 7.0 hours
    Car 4: (12-3)/3  = 3.0 hours
    Car 5: (12-0)/1  = 12.0 hours
    
    Stack Evolution:
    1. [1.0]                 # Car at pos 10
    2. [1.0]                 # Car at pos 8 (same time, becomes fleet)
    3. [1.0, 7.0]           # Car at pos 5 (slower, new fleet)
    4. [1.0, 7.0]           # Car at pos 3 (catches up to fleet)
    5. [1.0, 7.0, 12.0]     # Car at pos 0 (slower, new fleet)
    
    Final fleets: 3
    """
    # Sort cars by position in descending order
    cars = sorted(zip(position, speed), reverse=True)
    stack = []  # Store arrival times
    
    for pos, spd in cars:
        # Calculate time to reach target
        time = (target - pos) / spd
        
        # Add to stack if slower than previous fleet
        if not stack or time > stack[-1]:
            stack.append(time)
            
    return len(stack)

def car_fleet_simulation(target: int, position: List[int], speed: List[int]) -> int:
    """
    Approach 2: Forward Simulation
    Pattern: Time-based simulation with collision detection
    
    Visualization for target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]:
    
    Time 0:   0   3   5   8   10   |target=12
              *   *   *   *   *     
    
    Time 1:   1   6   6   12  12   |target=12
              *   *   *    **       Fleet 1 forms
    
    Time 2:   2   9   7   12  12   |target=12
              *   *   *    **       
    
    Time 3:   3   12  8   12  12   |target=12
              *   *   *    **       
    
    Final:    Fleet1(pos 8,10), Fleet2(pos 0), Fleet3(pos 3,5)
    """
    # Create car objects with position, speed, and time to target
    cars = [(p, s, (target-p)/s) for p, s in zip(position, speed)]
    cars.sort()  # Sort by position
    
    fleets = []
    for pos, spd, time in cars:
        # Check if this car catches up to previous fleet
        while fleets and fleets[-1][2] >= time:
            fleets.pop()
        fleets.append((pos, spd, time))
    
    return len(fleets)

def car_fleet_math(target: int, position: List[int], speed: List[int]) -> int:
    """
    Approach 3: Mathematical Solution
    Pattern: Collision point calculation
    
    For cars i and j to form a fleet:
    position[i] + speed[i] * t = position[j] + speed[j] * t
    
    Solve for collision time:
    t = (position[j] - position[i])/(speed[i] - speed[j])
    
    Example calculation:
    Cars at pos 8 and 10:
    t = (10-8)/(2-4) = 1 hour
    
    If collision time ≤ target time, they form fleet
    """
    times = []
    for p, s in sorted(zip(position, speed)):
        # Calculate time to target
        t = (target - p) / s
        # If this car is slower than previous fleet
        while times and times[-1] <= t:
            times.pop()
        times.append(t)
    return len(times)

"""
COMPLEXITY ANALYSIS
------------------

1. Monotonic Stack Approach:
   Time: O(n log n) - Sorting dominates
   Space: O(n) - Stack storage

2. Simulation Approach:
   Time: O(n log n) - Sorting dominates
   Space: O(n) - Fleet storage

3. Mathematical Approach:
   Time: O(n log n) - Sorting dominates
   Space: O(n) - Times array

EDGE CASES AND SPECIAL CONDITIONS
-------------------------------
1. Single car: Always returns 1
2. All same position: Impossible due to constraint
3. All same speed: Number of unique positions
4. All reach target same time: 1 fleet
5. No collisions: Each car is own fleet

OPTIMIZATION TECHNIQUES
----------------------
1. Early pruning:
   - If all speeds same, count unique positions
   - If target very large, check only final positions
2. Space optimization:
   - Reuse position array for sorting
   - In-place fleet counting possible
3. Time optimization:
   - Use counting sort if position range small
   - Process cars from back to avoid stack

RELATED PROBLEMS
---------------
1. Meeting Rooms II
2. Merge Intervals
3. Minimum Number of Arrows to Burst Balloons
4. The Skyline Problem
"""

```python
def car_fleet_detailed(target: int, position: List[int], speed: List[int]) -> int:
    """
    Detailed Example: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    
    1. Initial Sort by Position (Descending):
    Position: [10, 8,  5,  3,  0]
    Speed:    [2,  4,  1,  3,  1]
    
    2. Time to Target Calculations:
    Car at pos 10 (speed 2): 
        - Distance to target = 12 - 10 = 2
        - Time = 2/2 = 1.0 hours
        - Will reach target at t = 1.0
        
    Car at pos 8 (speed 4):
        - Distance to target = 12 - 8 = 4
        - Time = 4/4 = 1.0 hours
        - Will reach target at t = 1.0
        - Forms fleet with car at pos 10 because:
          * Same arrival time
          * Position is behind previous car
    
    Car at pos 5 (speed 1):
        - Distance to target = 12 - 5 = 7
        - Time = 7/1 = 7.0 hours
        - Will reach target at t = 7.0
        - New fleet because:
          * 7.0 > 1.0 (arrives later than previous fleet)
          * Cannot catch up to previous fleet
    
    Car at pos 3 (speed 3):
        - Distance to target = 12 - 3 = 9
        - Time = 9/3 = 3.0 hours
        - Will reach target at t = 3.0
        - Forms new fleet because:
          * 3.0 > 1.0 (arrives later than first fleet)
          * But 3.0 < 7.0 (catches up to fleet at pos 5)
          * Will merge with car at pos 5's fleet
    
    Car at pos 0 (speed 1):
        - Distance to target = 12 - 0 = 12
        - Time = 12/1 = 12.0 hours
        - Will reach target at t = 12.0
        - New fleet because:
          * 12.0 > 3.0 (arrives later than all previous fleets)
          * Cannot catch up to any previous fleet
    
    Stack Evolution with Detailed Reasoning:
    1. Stack: [1.0]        # First car
    2. Stack: [1.0]        # Second car merges (same time)
    3. Stack: [1.0, 7.0]   # Third car slower, can't catch up
    4. Stack: [1.0, 3.0]   # Fourth car faster than 7.0, replaces it
    5. Stack: [1.0, 3.0, 12.0] # Fifth car slowest, new fleet

    Visual Position-Time Graph:
    t=0   : 0---3---5---8---10-|12 (target)
    t=1   : 1---6---6---12--12-|
    t=2   : 2---9---7---12--12-|
    t=3   : 3---12--8---12--12-|
    t=7   : 7---12--12--12--12-|
    t=12  : 12--12--12--12--12-|
    
    Fleet Formation Process:
    1. Cars at 10 and 8 meet at target at t=1.0
       - Form Fleet 1 (speed=min(2,4)=2)
    
    2. Car at 5 never catches up (arrives t=7.0)
       - Forms Fleet 2 (speed=1)
    
    3. Car at 3 catches up to car at 5
       - Forms Fleet 3 (speed=min(3,1)=1)
    
    4. Car at 0 never catches up
       - Forms Fleet 4 (speed=1)
    """
    cars = sorted(zip(position, speed), reverse=True)
    stack = []  # [(pos, speed, time_to_target)]
    
    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
            
    return len(stack)
```


```python
def car_fleet_simulation(target: int, position: List[int], speed: List[int]) -> int:
    """
    Let's simulate every hour for target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]
    
    Initial State (t=0):
    positions = [10,8,0,5,3]
    speeds =    [2,4,1,1,3]
    
    Hour-by-hour simulation:
    
    Time 0:
    pos = [10, 8,  0,  5,  3 ]  # Initial positions
    Car1 (pos=10,spd=2): 10 -> target in (12-10)/2 = 1 hour
    Car2 (pos=8, spd=4): 8  -> target in (12-8)/4 = 1 hour
    Car3 (pos=0, spd=1): 0  -> target in (12-0)/1 = 12 hours
    Car4 (pos=5, spd=1): 5  -> target in (12-5)/1 = 7 hours
    Car5 (pos=3, spd=3): 3  -> target in (12-3)/3 = 3 hours
    
    Time 1:
    pos = [12, 12, 1,  6,  6 ]
    fleets_formed = 1 (Cars 1&2 meet at target)
    Car1: Reached target
    Car2: Reached target, joins Car1's fleet
    Car3: Moved to position 1
    Car4: Moved to position 6
    Car5: Moved to position 6, catches up to Car4
    
    Time 2:
    pos = [12, 12, 2,  7,  9 ]
    fleets_formed = 1
    Car3: At position 2
    Car4: At position 7
    Car5: At position 9 (can't pass Car4, slows to speed 1)
    
    Time 3:
    pos = [12, 12, 3,  8, 12]
    fleets_formed = 2 (Car5 reaches target)
    Car3: At position 3
    Car4: At position 8
    Car5: Reached target
    
    Time 7:
    pos = [12, 12, 7, 12, 12]
    fleets_formed = 3 (Car4 reaches target)
    Car3: At position 7
    Car4: Reached target
    
    Time 12:
    pos = [12, 12, 12, 12, 12]
    fleets_formed = 3 (Final state)
    Car3: Finally reaches target
    
    Code execution with detailed state tracking:
    """
    # Sort cars by position and track their states
    cars = sorted(zip(position, speed), reverse=True)  # Sort from right to left
    stack = []  # Track arrival times
    
    print("Initial car states:")
    for i, (pos, spd) in enumerate(cars):
        time = (target - pos) / spd
        print(f"Car {i+1}: pos={pos}, speed={spd}, arrival_time={time:.1f}")
        
        # Only create new fleet if this car is slower (arrives later)
        if not stack or time > stack[-1]:
            stack.append(time)
            print(f"Created new fleet: arrives at t={time:.1f}")
        else:
            print(f"Joins existing fleet arriving at t={stack[-1]:.1f}")
            
        print(f"Current fleets: {len(stack)}\n")
    
    return len(stack)

# Example usage with detailed output:
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

result = car_fleet_simulation(target, position, speed)
print(f"Final number of fleets: {result}")

"""
Code Execution Breakdown:

1. First car (pos=10, speed=2):
   time = (12-10)/2 = 1.0
   stack = [1.0]
   
2. Second car (pos=8, speed=4):
   time = (12-8)/4 = 1.0
   1.0 == stack[-1], joins first fleet
   stack = [1.0]
   
3. Third car (pos=5, speed=1):
   time = (12-5)/1 = 7.0
   7.0 > stack[-1], creates new fleet
   stack = [1.0, 7.0]
   
4. Fourth car (pos=3, speed=3):
   time = (12-3)/3 = 3.0
   3.0 > stack[0] but < stack[1]
   Replaces larger time as it will catch up
   stack = [1.0, 3.0]
   
5. Fifth car (pos=0, speed=1):
   time = (12-0)/1 = 12.0
   12.0 > stack[-1], creates new fleet
   stack = [1.0, 3.0, 12.0]

Final stack = [1.0, 3.0, 12.0]
Number of fleets = 3
"""
```
```python
def car_fleet_detailed(target: int, position: List[int], speed: List[int]) -> int:
    """
    Detailed Example: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    
    1. Initial Sort by Position (Descending):
    Position: [10, 8,  5,  3,  0]
    Speed:    [2,  4,  1,  3,  1]
    
    2. Time to Target Calculations:
    Car at pos 10 (speed 2): 
        - Distance to target = 12 - 10 = 2
        - Time = 2/2 = 1.0 hours
        - Will reach target at t = 1.0
        
    Car at pos 8 (speed 4):
        - Distance to target = 12 - 8 = 4
        - Time = 4/4 = 1.0 hours
        - Will reach target at t = 1.0
        - Forms fleet with car at pos 10 because:
          * Same arrival time
          * Position is behind previous car
    
    Car at pos 5 (speed 1):
        - Distance to target = 12 - 5 = 7
        - Time = 7/1 = 7.0 hours
        - Will reach target at t = 7.0
        - New fleet because:
          * 7.0 > 1.0 (arrives later than previous fleet)
          * Cannot catch up to previous fleet
    
    Car at pos 3 (speed 3):
        - Distance to target = 12 - 3 = 9
        - Time = 9/3 = 3.0 hours
        - Will reach target at t = 3.0
        - Forms new fleet because:
          * 3.0 > 1.0 (arrives later than first fleet)
          * But 3.0 < 7.0 (catches up to fleet at pos 5)
          * Will merge with car at pos 5's fleet
    
    Car at pos 0 (speed 1):
        - Distance to target = 12 - 0 = 12
        - Time = 12/1 = 12.0 hours
        - Will reach target at t = 12.0
        - New fleet because:
          * 12.0 > 3.0 (arrives later than all previous fleets)
          * Cannot catch up to any previous fleet
    
    Stack Evolution with Detailed Reasoning:
    1. Stack: [1.0]        # First car
    2. Stack: [1.0]        # Second car merges (same time)
    3. Stack: [1.0, 7.0]   # Third car slower, can't catch up
    4. Stack: [1.0, 3.0]   # Fourth car faster than 7.0, replaces it
    5. Stack: [1.0, 3.0, 12.0] # Fifth car slowest, new fleet

    Visual Position-Time Graph:
    t=0   : 0---3---5---8---10-|12 (target)
    t=1   : 1---6---6---12--12-|
    t=2   : 2---9---7---12--12-|
    t=3   : 3---12--8---12--12-|
    t=7   : 7---12--12--12--12-|
    t=12  : 12--12--12--12--12-|
    
    Fleet Formation Process:
    1. Cars at 10 and 8 meet at target at t=1.0
       - Form Fleet 1 (speed=min(2,4)=2)
    
    2. Car at 5 never catches up (arrives t=7.0)
       - Forms Fleet 2 (speed=1)
    
    3. Car at 3 catches up to car at 5
       - Forms Fleet 3 (speed=min(3,1)=1)
    
    4. Car at 0 never catches up
       - Forms Fleet 4 (speed=1)
    """
    cars = sorted(zip(position, speed), reverse=True)
    stack = []  # [(pos, speed, time_to_target)]
    
    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
            
    return len(stack)
```