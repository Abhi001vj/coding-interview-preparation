# https://leetcode.com/problems/process-tasks-using-servers/description/

# Code
# Testcase
# Test Result
# Test Result
# 1882. Process Tasks Using Servers
# Medium
# Topics
# Companies
# Hint
# You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

# Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

# At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

# If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

# A server that is assigned task j at second t will be free again at second t + tasks[j].

# Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

# Return the array ans​​​​.

 

# Example 1:

# Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
# Output: [2,2,0,2,1,2]
# Explanation: Events in chronological order go as follows:
# - At second 0, task 0 is added and processed using server 2 until second 1.
# - At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
# - At second 2, task 2 is added and processed using server 0 until second 5.
# - At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
# - At second 4, task 4 is added and processed using server 1 until second 5.
# - At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
# Example 2:

# Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
# Output: [1,4,1,4,1,3,2]
# Explanation: Events in chronological order go as follows: 
# - At second 0, task 0 is added and processed using server 1 until second 2.
# - At second 1, task 1 is added and processed using server 4 until second 2.
# - At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
# - At second 3, task 3 is added and processed using server 4 until second 7.
# - At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
# - At second 5, task 5 is added and processed using server 3 until second 7.
# - At second 6, task 6 is added and processed using server 2 until second 7.
 

# Constraints:

# servers.length == n
# tasks.length == m
# 1 <= n, m <= 2 * 105
# 1 <= servers[i], tasks[j] <= 2 * 105
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 37.4K
# Submissions
# 92K
# Acceptance Rate
# 40.7%
# Topics
# Companies
# Hint 1
# You can maintain a Heap of available Servers and a Heap of unavailable servers
# Hint 2
# Note that the tasks will be processed in the input order so you just need to find the x-th server that will be available according to the rules


```python
"""
PROCESS TASKS USING SERVERS
--------------------------

Key Idea:
1. Use two min heaps:
   - free_servers: (weight, index) for available servers
   - busy_servers: (available_time, weight, index) for busy ones
2. Process tasks in chronological order
3. Track current time and update server availability

Example Visualization:
servers = [3,3,2], tasks = [1,2,3,2,1,2]

Initial State:
free_servers: [(2,2), (3,0), (3,1)]  # (weight, index)
busy_servers: []
current_time: 0

Time 0:
- Task 0 (duration=1) arrives
- Use server 2 (weight=2)
free_servers: [(3,0), (3,1)]
busy_servers: [(1,2,2)]  # (end_time, weight, index)

Time 1:
- Server 2 becomes free
- Task 1 (duration=2) arrives
free_servers: [(2,2), (3,0), (3,1)]
busy_servers: []
- Assign task 1 to server 2
"""

from heapq import heappush, heappop

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Initialize heaps
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        busy_servers = []  # (available_time, weight, index)
        heapq.heapify(free_servers)
        
        current_time = 0
        result = []
        
        for task_idx, task_duration in enumerate(tasks):
            current_time = max(current_time, task_idx)
            
            # Move servers that have finished to free_servers
            while busy_servers and busy_servers[0][0] <= current_time:
                available_time, weight, server_idx = heappop(busy_servers)
                heappush(free_servers, (weight, server_idx))
            
            # If no free servers, jump time to next available server
            if not free_servers:
                current_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= current_time:
                    available_time, weight, server_idx = heappop(busy_servers)
                    heappush(free_servers, (weight, server_idx))
            
            # Get the server with minimum weight (and minimum index if tie)
            weight, server_idx = heappop(free_servers)
            
            # Add server to busy_servers
            heappush(busy_servers, (current_time + task_duration, weight, server_idx))
            result.append(server_idx)
        
        return result

"""
Time Complexity Analysis:
O(M * log N) where:
- M = number of tasks
- N = number of servers
- Each task requires heap operations O(log N)

Space Complexity: O(N) where:
- N = number of servers
- Both heaps combined store N servers

Detailed Example:
servers = [3,3,2], tasks = [1,2,3,2,1,2]

1. Initialize:
   free_servers: [(2,2), (3,0), (3,1)]
   busy_servers: []
   time = 0

2. Task 0 (duration=1):
   - Use server 2
   - busy_servers: [(1,2,2)]
   - result: [2]

3. Task 1 (duration=2):
   - Server 2 becomes free
   - Use server 2 again
   - busy_servers: [(3,2,2)]
   - result: [2,2]

4. Task 2 (duration=3):
   - Use server 0
   - busy_servers: [(3,2,2), (5,3,0)]
   - result: [2,2,0]

And so on...

Key Points:
1. Two heaps maintain server states efficiently
2. Time tracking handles server availability
3. Priority based on weight and index
4. Efficient server reassignment
"""
```