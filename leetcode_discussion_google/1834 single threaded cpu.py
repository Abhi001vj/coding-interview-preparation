# https://leetcode.com/problems/single-threaded-cpu/
# 1834. Single-Threaded CPU
# Medium
# Topics
# Companies
# Hint
# You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

# You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

# If the CPU is idle and there are no available tasks to process, the CPU remains idle.
# If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
# Once a task is started, the CPU will process the entire task without stopping.
# The CPU can finish a task then start a new one instantly.
# Return the order in which the CPU will process the tasks.

 

# Example 1:

# Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
# Output: [0,2,3,1]
# Explanation: The events go as follows: 
# - At time = 1, task 0 is available to process. Available tasks = {0}.
# - Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
# - At time = 2, task 1 is available to process. Available tasks = {1}.
# - At time = 3, task 2 is available to process. Available tasks = {1, 2}.
# - Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
# - At time = 4, task 3 is available to process. Available tasks = {1, 3}.
# - At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
# - At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
# - At time = 10, the CPU finishes task 1 and becomes idle.
# Example 2:

# Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# Output: [4,3,2,0,1]
# Explanation: The events go as follows:
# - At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
# - Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
# - At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
# - At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
# - At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
# - At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
# - At time = 40, the CPU finishes task 1 and becomes idle.
 

# Constraints:

# tasks.length == n
# 1 <= n <= 105
# 1 <= enqueueTimei, processingTimei <= 109
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 118.3K
# Submissions
# 257.3K
# Acceptance Rate
# 46.0%
# Topics
# Companies
# Hint 1
# To simulate the problem we first need to note that if at any point in time there are no enqueued tasks we need to wait to the smallest enqueue time of a non-processed element
# Hint 2
# We need a data structure like a min-heap to support choosing the task with the smallest processing time from all the enqueued tasks

"""
SINGLE-THREADED CPU TASK SCHEDULING

Key Components:
1. Sort tasks by enqueue time
2. Min heap for available tasks
3. Time simulation

Example Visualization:
tasks = [[1,2],[2,4],[3,2],[4,1]]

Time=1:
Enqueued: Task 0 (1,2)
Available: [(2, 0)]  # (processing_time, index)
CPU: Processing Task 0

Time=2:
Enqueued: Task 1 (2,4)
Available: [(4, 1)]
CPU: Processing Task 0

Time=3:
Enqueued: Task 2 (3,2)
Available: [(2, 2), (4, 1)]
CPU: Finished Task 0, Start Task 2

Time=4:
Enqueued: Task 3 (4,1)
Available: [(1, 3), (4, 1)]
CPU: Processing Task 2

Time=5:
CPU: Finished Task 2, Start Task 3
Available: [(4, 1)]

Time=6:
CPU: Finished Task 3, Start Task 1
Available: []

Time=10:
CPU: Finished Task 1
Result: [0,2,3,1]
"""

from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Add index to each task for tracking
        tasks = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        # Sort by enqueue time
        tasks.sort()
        
        result = []
        # Min heap for available tasks: (processing_time, index)
        available_tasks = []
        
        # Current time and task pointer
        current_time = 0
        task_pointer = 0
        
        """
        Time Simulation Process:
        1. Move time to next event (either task available or CPU free)
        2. Add all tasks that become available
        3. Process shortest available task
        4. Repeat until all tasks processed
        
        Example state for [[1,2],[2,4],[3,2],[4,1]]:
        
        Initial:
        tasks = [(1,2,0), (2,4,1), (3,2,2), (4,1,3)]
        available_tasks = []
        current_time = 0
        result = []
        
        After Time=1:
        available_tasks = [(2,0)]  # (proc_time, index)
        current_time = 1
        result = []
        """
        
        while task_pointer < len(tasks) or available_tasks:
            # If no tasks available, jump time to next task
            if not available_tasks and task_pointer < len(tasks):
                current_time = max(current_time, tasks[task_pointer][0])
            
            # Add all tasks that have become available
            while (task_pointer < len(tasks) and 
                   tasks[task_pointer][0] <= current_time):
                enqueue_time, proc_time, index = tasks[task_pointer]
                heapq.heappush(available_tasks, (proc_time, index))
                task_pointer += 1
            
            if available_tasks:
                proc_time, index = heapq.heappop(available_tasks)
                result.append(index)
                current_time += proc_time
        
        return result

"""
Time Complexity Analysis: O(N log N)
1. Sorting tasks: O(N log N)
2. Processing tasks:
   - Each task pushed once: O(N log N)
   - Each task popped once: O(N log N)
   Total: O(N log N)

Space Complexity: O(N)
1. tasks array with indices: O(N)
2. Priority queue: O(N)
3. Result array: O(N)

Why Priority Queue?
1. Need to always pick shortest processing time
2. Heap gives us O(log N) insert and O(log N) remove-min
3. Perfect for maintaining sorted order of available tasks

Example of Multiple Tasks with Same Time:
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]

Time=7:
available_tasks = [
    (2, 4),  # Task 4
    (4, 3),  # Task 3
    (5, 2),  # Task 2
    (10, 0), # Task 0
    (12, 1)  # Task 1
]

Process order: 4 -> 3 -> 2 -> 0 -> 1
Because shortest processing time wins!
"""