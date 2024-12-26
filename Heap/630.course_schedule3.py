
# https://leetcode.com/problems/course-schedule-iii/description/
# Code
# Testcase
# Test Result
# Test Result
# 630. Course Schedule III
# Solved
# Hard
# Topics
# Companies
# Hint
# There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

# You will start on the 1st day and you cannot take two or more courses simultaneously.

# Return the maximum number of courses that you can take.

 

# Example 1:

# Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3
# Explanation: 
# There are totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
# Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
# The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
# Example 2:

# Input: courses = [[1,2]]
# Output: 1
# Example 3:

# Input: courses = [[3,2],[4,3]]
# Output: 0
 

# Constraints:

# 1 <= courses.length <= 104
# 1 <= durationi, lastDayi <= 104

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 117.6K
# Submissions
# 291.5K
# Acceptance Rate
# 40.3%
# Topics
# Companies
# Hint 1
# During iteration, say I want to add the current course, currentTotalTime being total time of all courses taken till now, but adding the current course might exceed my deadline or it doesn’t.

# 1. If it doesn’t, then I have added one new course. Increment the currentTotalTime with duration of current course.
# Hint 2
# 2. If it exceeds deadline, I can swap current course with current courses that has biggest duration.
# * No harm done and I might have just reduced the currentTotalTime, right?
# * What preprocessing do I need to do on my course processing order so that this swap is always legal?
from typing import List
import heapq

def scheduleCourse(courses: List[List[int]]) -> int:
    """
    Determines the maximum number of courses that can be taken given time constraints.
    
    Time Complexity:
    - Sorting: O(n log n)
    - Heap operations: O(n log n) - we do at most n push/pop operations
    Total: O(n log n) where n is number of courses
    
    Space Complexity:
    - Heap: O(n) - stores at most n courses
    - Sorting: O(n) or O(log n) depending on implementation
    Total: O(n)
    
    Input visualization for [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]:
    
    Timeline visualization (before sorting):
    Course 1: [=======]                 (0-7, deadline 17)
    Course 2: [===]                     (0-3, deadline 12)
    Course 3: [==========]              (0-10, deadline 20)
    Course 4: [=========]               (0-9, deadline 10)
    Course 5: [=====]                   (0-5, deadline 20)
    Course 6: [==========]              (0-10, deadline 19)
    Course 7: [====]                    (0-4, deadline 18)
    
    After sorting by deadline:
    Course 4: [=========]               (0-9, deadline 10)
    Course 2: [===]                     (0-3, deadline 12)
    Course 1: [=======]                 (0-7, deadline 17)
    Course 7: [====]                    (0-4, deadline 18)
    Course 6: [==========]              (0-10, deadline 19)
    Course 3: [==========]              (0-10, deadline 20)
    Course 5: [=====]                   (0-5, deadline 20)
    """
    # Sort courses by end day (deadline)
    courses.sort(key=lambda x: x[1])
    heap = []  # max heap to store durations
    total_time = 0
    
    # Process visualization
    """
    Step by step for our example:
    1. [9,10]:
       total_time = 9, heap = [-9]
    
    2. [3,12]:
       total_time = 12, heap = [-9, -3]
       12 > 12? No action needed
    
    3. [7,17]:
       total_time = 19, heap = [-9, -3, -7]
       19 > 17? Yes, remove 9 (longest)
       total_time = 10, heap = [-7, -3]
    
    4. [4,18]:
       total_time = 14, heap = [-7, -3, -4]
       14 > 18? No action needed
    
    5. [10,19]:
       total_time = 24, heap = [-7, -3, -4, -10]
       24 > 19? Yes, remove 10 (longest)
       total_time = 14, heap = [-7, -3, -4]
    """
    for duration, deadline in courses:
        total_time += duration
        heapq.heappush(heap, -duration)  # negative for max heap
        
        # If current schedule exceeds deadline
        if total_time > deadline:
            # Remove the longest course taken so far
            longest_duration = -heapq.heappop(heap)
            total_time -= longest_duration
            
    return len(heap)

# Test the solution
courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
result = scheduleCourse(courses)
print(f"Maximum number of courses: {result}")

"""
Final Schedule Explanation:
-------------------------
The optimal solution takes 4 courses:
1. [3,12]  - Duration: 3, Completes by day 3
2. [4,18]  - Duration: 4, Completes by day 7
3. [5,20]  - Duration: 5, Completes by day 12
4. [7,17]  - Duration: 7, Completes by day 19

Why this is optimal:
1. We prioritize earlier deadlines first
2. When we can't fit a course, we remove the longest course taken so far
3. This ensures we maximize the number of courses while respecting deadlines

Key optimization techniques:
1. Sort by deadline to ensure we process courses in order of urgency
2. Use max heap to quickly find and remove longest duration when needed
3. Keep running total of time to check deadline constraints

Space-Time Complexity Analysis:
-----------------------------
Time: O(n log n)
- Sorting: O(n log n)
- Heap operations: O(log n) per operation, n operations = O(n log n)
- Total: O(n log n)

Space: O(n)
- Heap storage: O(n)
- Sorting space: O(n) or O(log n) depending on implementation
- Total: O(n)

This solution is optimal in terms of both time and space complexity:
- We can't do better than O(n log n) because we need to at least look at all courses
- We need O(n) space to store the courses we take
"""