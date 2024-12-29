# https://leetcode.com/problems/minimum-number-of-refueling-stops/description/
# 871. Minimum Number of Refueling Stops
# Hard
# Topics
# Companies
# A car travels from a starting position to a destination which is target miles east of the starting position.

# There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

# Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

# Example 1:

# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.
# Example 2:

# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can not reach the target (or even the first gas station).
# Example 3:

# Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation: We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
# We made 2 refueling stops along the way, so we return 2.
 

# Constraints:

# 1 <= target, startFuel <= 109
# 0 <= stations.length <= 500
# 1 <= positioni < positioni+1 < target
# 1 <= fueli < 109

"""
Minimum Number of Refueling Stops (LeetCode 871)

Key Pattern: Greedy with Priority Queue
Time: O(N log N) where N is number of stations
Space: O(N) for the priority queue

Core Algorithm:
1. Track current position and remaining fuel
2. Store visited stations in max heap (by fuel amount)
3. When stuck, use highest fuel station
4. Continue until target reached or impossible

Let's implement with detailed state tracking:
"""

from heapq import heappush, heappop

def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    """
    Example state visualization:
    pos=0, fuel=10, target=100
    stations=[[10,60],[20,30],[30,30],[60,40]]
    
    Initial State:
    0 miles →→→→→ 10 miles →→→→→ 20 miles →→→→→ 30 miles →→→→→ 60 miles →→→→→ 100 miles
    [Start]      [60 fuel]      [30 fuel]      [30 fuel]      [40 fuel]     [Target]
    10 fuel
    
    State Tracker:
    pos = current position
    fuel = current fuel
    stops = number of stops
    pq = available stations (max heap by fuel)
    """
    
    # Initialize state
    pos = 0           # Current position
    fuel = startFuel  # Remaining fuel
    stops = 0         # Number of stops made
    pq = []          # Max heap of available stations (store negative fuel for max heap)
    i = 0            # Current station index
    
    """
    Main Loop Strategy:
    1. While not at target:
       - Add all reachable stations to heap
       - If can't reach next point, use highest fuel station
       - If no stations available, return -1
       
    Example State Changes:
    1. Start: pos=0, fuel=10
       Can reach: station 1 (10 miles)
       
    2. At station 1: pos=10, fuel=0
       Options: [60] in heap
       Use 60 fuel → can reach stations 2,3
       
    3. At station 2/3: pos=30, fuel=40
       Options: [30,30] in heap
       Can reach station 4
    """
    
    # Continue until we reach target
    while pos + fuel < target:
        # Track next minimum position we need to reach
        next_pos = target if i >= len(stations) else stations[i][0]
        
        # Add all reachable stations to priority queue
        while i < len(stations) and pos + fuel >= stations[i][0]:
            """
            Visualization:
            Current: pos=10, fuel=60
            Next station: pos=20, fuel=30
            
            Can reach? pos + fuel >= next_pos
                      10 + 60 >= 20 ✓
            """
            heappush(pq, -stations[i][1])  # Negative for max heap
            i += 1
        
        # If we can't reach next station/target and no stations available
        if not pq:
            """
            Example impossible case:
            pos=10, fuel=5, next_station=20
            pq is empty → can't reach next point
            """
            return -1
        
        # Use highest fuel station
        fuel_used = next_pos - pos if i < len(stations) else target - pos
        pos = next_pos
        
        # Add fuel from station with most fuel
        fuel = fuel - fuel_used + (-heappop(pq))
        stops += 1
        
        """
        State Tracking Example:
        Before: pos=10, fuel=0, pq=[-60]
        Use station: fuel = 0 - 0 + 60 = 60
        After: pos=10, fuel=60, stops=1
        """
    
    return stops

"""
Example Complete Walkthrough:
target = 100, startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

State Changes:
1. Initial: pos=0, fuel=10
   Can reach: first station
   PQ: []

2. At first decision point:
   pos=0, fuel=10, next_pos=10
   Add station 1 to PQ: [-60]
   Need fuel to continue
   Use 60 fuel from PQ
   pos=10, fuel=60, stops=1

3. Continue moving:
   Can reach stations 2 and 3
   Add to PQ: [-30, -30]
   pos=30, fuel=40, stops=1
   Can reach station 4
   Add to PQ: [-40]

4. Final stretch:
   pos=60, fuel=10
   Need more fuel
   Use highest from PQ (40)
   pos=100, fuel=0, stops=2

Return: 2 stops

Edge Cases Handled:
1. Empty stations list:
   - Only need to check if startFuel reaches target

2. Can't reach first station:
   - Handled by first iteration of while loop

3. Multiple stations at same position:
   - Naturally handled by priority queue

4. Exactly enough fuel:
   - Works because we check pos + fuel < target

5. More fuel than needed:
   - Works because we only take fuel when necessary
"""

# Test cases to verify implementation
def test_minRefuelStops():
    test_cases = [
        {
            "target": 1,
            "startFuel": 1,
            "stations": [],
            "expected": 0
        },
        {
            "target": 100,
            "startFuel": 1,
            "stations": [[10,100]],
            "expected": -1
        },
        {
            "target": 100,
            "startFuel": 10,
            "stations": [[10,60],[20,30],[30,30],[60,40]],
            "expected": 2
        }
    ]
    
    for i, test in enumerate(test_cases):
        result = minRefuelStops(
            test["target"],
            test["startFuel"],
            test["stations"]
        )
        assert result == test["expected"], f"Failed case {i+1}"
    
    print("All test cases passed!")

"""
Minimum Number of Refueling Stops - Detailed Solution
--------------------------------------------------

Pattern Recognition:
1. Greedy Choice Property: Always choose station with most fuel when needed
2. Priority Queue Pattern: Need to maintain "best" options seen so far
3. Running Maximum Pattern: Track maximum reachable distance

Time Complexity: O(N log N) where N is number of stations
- Each station is pushed/popped from heap once: O(log N) per operation
- We process each station once: O(N) stations

Space Complexity: O(N)
- Priority Queue can store all stations in worst case

Core Algorithm:
-------------
1. Track maximum reachable distance
2. Store available stations in max heap
3. When can't reach target, use highest fuel station
4. Continue until target reached or impossible

Visual State Management:
---------------------
Example: target=100, startFuel=10, stations=[[10,60],[20,30],[30,30],[60,40]]

Initial State:
0 →→→→→ 10 →→→→→ 20 →→→→→ 30 →→→→→ 60 →→→→→ 100
[S]      [60]     [30]     [30]     [40]     [T]
10 fuel

State Components:
┌─────────────┐   ┌──────────────┐
│ curr_fuel   │   │ Max Heap     │
│ curr_pos    │   │ (available   │
│ prev_pos    │   │  stations)   │
└─────────────┘   └──────────────┘
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        Find minimum stops needed to reach target with given fuel constraints.
        
        Parameters:
        -----------
        target : int
            Distance to destination
        startFuel : int
            Initial fuel amount
        stations : List[List[int]]
            List of [position, fuel] pairs for each station
            
        Returns:
        --------
        int
            Minimum stops needed or -1 if impossible
            
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        """
        prev_position = 0     # Last position we "locked in"
        curr_fuel = startFuel # Current available fuel
        stops = 0            # Number of stops made
        pq = []             # Max heap (storing negative values)
        i = 0               # Current station index
        
        """
        Main Loop Visualization:
        
        Each iteration:
        1. Calculate furthest reachable position
        2. Add all reachable stations to heap
        3. If can't reach target, use best station
        
        Example State Changes:
        ---------------------
        Initial:
        pos=0, fuel=10
        Can reach: 0 + 10 = 10
        Heap: []
        
        After adding station 1:
        Heap: [-60]
        Use 60 fuel
        New reach: 0 + 70 = 70
        Can add stations 2,3,4
        """
        
        while prev_position + curr_fuel < target:
            # Calculate furthest reachable position
            curr_position = prev_position + curr_fuel
            
            """
            Station Processing:
            ------------------
            pos=0, fuel=70
            Reachable stations visual:
            0 →→→→→→→→→→→→→→→→→→→→→→→ 70
                  [30]     [30]     [40]
                  add      add      add
            """
            # Add all reachable stations to our options
            while i < len(stations) and stations[i][0] <= curr_position:
                heappush(pq, -stations[i][1])  # Negative for max heap
                i += 1
            
            # If no stations available but haven't reached target
            if not pq:
                """
                Impossible Case Example:
                pos=0, fuel=5, target=100
                No stations within reach
                ↓
                [S] →→→→→ | - - - - - [T]
                5 fuel    |  Can't reach
                """
                return -1
            
            """
            Refueling Strategy:
            ------------------
            Choose station with most fuel
            Add its fuel to our current fuel
            
            Example:
            Heap: [-60, -30, -30]
            Pop -60 → Add 60 fuel
            New fuel = 70
            """
            # Use the station with most fuel
            curr_fuel = curr_fuel + (-heappop(pq))
            stops += 1
        
        return stops

"""
Complete Example Walkthrough:
---------------------------
target = 100, startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

1. Initial State:
   prev_pos = 0
   curr_fuel = 10
   reachable = 10
   Add station 1 (60 fuel)
   
2. First Refuel:
   Use 60 fuel
   curr_fuel = 70
   reachable = 70
   Add stations 2,3,4
   
3. Second Refuel:
   Use 40 fuel (best remaining)
   curr_fuel = 110
   reachable = 110 > target
   Done!

Return: 2 stops

Edge Cases Handled:
-----------------
1. Empty stations list: 
   - Check if startFuel reaches target
   
2. Can't reach first station:
   - curr_position < first station position
   - pq empty → return -1
   
3. Exactly enough fuel:
   - Works because while loop condition checks for strictly less

4. Multiple stations at same position:
   - All added to heap
   - Best one used first

Why This is Optimal:
------------------
1. Greedy Choice Property:
   - When we need fuel, using station with most fuel is optimal
   - No benefit in saving higher fuel station for later
   
2. Priority Queue Maintenance:
   - Always have access to best remaining option
   - O(log N) operations maintain efficiency

3. Position Tracking:
   - Don't need to track actual movement
   - Only care about maximum reachable distance
"""