# https://leetcode.com/problems/car-pooling/description/
# 1094. Car Pooling
# Medium
# Topics
# Companies
# Hint
# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
 

# Constraints:

# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 105
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 241.2K
# Submissions
# 431.1K
# Acceptance Rate
# 55.9%
# Topics
# Companies
# Hint 1
# Sort the pickup and dropoff events by location, then process them in order.

# Let's break this down step by step. The key insight is to track passenger changes at each point. Let me help you think through the solution:

# First, let's understand why sorting by start time alone isn't enough:

# pythonCopytrips = [[2,1,5],[3,3,7]]  # [passengers, start, end]
# Let's visualize this:
# CopyTrip 1:    |--2 passengers--|
#            1                5
# Trip 2:        |--3 passengers--|
#                3                7
# Your current approach has two issues:

# You're only tracking pickups, not dropoffs
# You need to know when people get off to free up capacity

# Let's consider different approaches:

# Approach 1 (Event simulation):

# pythonCopydef carPooling(self, trips, capacity):
#     # Create events array: [location, passenger_change]
#     events = []
#     for num_pass, start, end in trips:
#         events.append([start, num_pass])     # pickup: add passengers
#         events.append([end, -num_pass])      # dropoff: remove passengers
    
#     events.sort()  # Sort by location
# Would you like to continue with this approach and see how we can track the running total of passengers? Or would you prefer to explore a different approach?
# The key insight is that we need to:

# Track both pickups and dropoffs
# Process events in order of location
# Keep running total of passengers
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for num_pass, start, end in trips:
            events.append([start, num_pass])
            events.append([end, -num_pass])
        
        events.sort()
        current_passengers = 0
        for loc, num_pass in events:
            current_passengers += num_pass
            if current_passengers > capacity:
                return False
        return True
