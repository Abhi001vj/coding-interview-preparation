# https://leetcode.com/problems/meeting-scheduler/
# 1229. Meeting Scheduler
# Solved
# Medium
# Topics
# Companies
# Hint
# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

# If there is no common time slot that satisfies the requirements, return an empty array.

# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

# Example 1:

# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]
# Example 2:

# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# Output: []
 

# Constraints:

# 1 <= slots1.length, slots2.length <= 104
# slots1[i].length, slots2[i].length == 2
# slots1[i][0] < slots1[i][1]
# slots2[i][0] < slots2[i][1]
# 0 <= slots1[i][j], slots2[i][j] <= 109
# 1 <= duration <= 106
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 89.1K
# Submissions
# 161.3K
# Acceptance Rate
# 55.3%
# Topics
# Companies
# Hint 1
# Assume that in the solution, the selected slot from slotsA is bigger than the respectively selected slot from slotsB.
# Hint 2
# Use two pointers in order to try all the possible intersections, and check the length.
# Hint 3
# Do the same in step N° 1 but now assume that the selected slot from slotsB is bigger, return the minimum of the two options.

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i = j =0
        res = []
        while i < len(slots1) and  j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])

            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
    
        return []
    
def minAvailableDuration(slots1, slots2, duration):
    """
    Example visualization for slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
    
    Timeline visualization:
    
    slots1:     |----1----|     |-----2-----|    |-----3-----|
                10        50     60         120   140        210
    
    slots2:  |--A--|            |--B--|
             0    15            60   70
                                
    Overlap cases:
    
    Case 1: slots1[0]=[10,50] vs slots2[0]=[0,15]
            max(start)=max(10,0)=10   -> Latest start of overlap
            min(end)=min(50,15)=15    -> Earliest end of overlap
            overlap=[10,15], length=5  -> Not enough for duration=8
    
    Case 2: slots1[1]=[60,120] vs slots2[1]=[60,70]
            max(start)=max(60,60)=60  -> Latest start of overlap
            min(end)=min(120,70)=70   -> Earliest end of overlap
            overlap=[60,70], length=10 -> Enough for duration=8!
            Return [60,68]            -> Start at 60, add duration=8
    """
    # Sort both arrays by start time
    slots1.sort()
    slots2.sort()
    i = j = 0
    
    while i < len(slots1) and j < len(slots2):
        # Find the overlap period
        # max(start) ensures we start at the later of the two start times
        # This is because both people need to be available
        start = max(slots1[i][0], slots2[j][0])
        
        # min(end) ensures we end at the earlier of the two end times
        # This is because we lose availability of one person after their slot ends
        end = min(slots1[i][1], slots2[j][1])
        
        # Current state tracking
        """
        Iteration 1:
        i=0, j=0
        slots1[i]=[10,50], slots2[j]=[0,15]
        start=max(10,0)=10, end=min(50,15)=15
        overlap=5 < duration=8, move j pointer (15 < 50)
        
        Iteration 2:
        i=0, j=1
        slots1[i]=[10,50], slots2[j]=[60,70]
        No overlap (50 < 60), move i pointer
        
        Iteration 3:
        i=1, j=1
        slots1[i]=[60,120], slots2[j]=[60,70]
        start=max(60,60)=60, end=min(120,70)=70
        overlap=10 >= duration=8
        Return [60,68]
        """
        
        # If overlap is sufficient, return immediately
        if end - start >= duration:
            return [start, start + duration]
            
        # Move pointer of the interval that ends earlier
        # This is because we won't find any better overlap with that interval
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1
    
    return []

# Test case
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8


def minAvailableDuration(slots1, slots2, duration):
    """
    Example 2 visualization for:
    slots1 = [[10,50],[60,120],[140,210]]
    slots2 = [[0,15],[60,70]]
    duration = 12
    
    Timeline visualization:
    
    slots1:     |----1----|     |-----2-----|    |-----3-----|
                10        50     60         120   140        210
    
    slots2:  |--A--|            |--B--|
             0    15            60   70
                                
    Overlap analysis:
    
    Case 1: slots1[0]=[10,50] vs slots2[0]=[0,15]
            max(start)=max(10,0)=10   -> Latest start time
            min(end)=min(50,15)=15    -> Earliest end time
            overlap=[10,15], length=5  -> Too short for duration=12
            Move j pointer (15 < 50)
    
    Case 2: slots1[0]=[10,50] vs slots2[1]=[60,70]
            No overlap (50 < 60)
            Move i pointer
    
    Case 3: slots1[1]=[60,120] vs slots2[1]=[60,70]
            max(start)=max(60,60)=60  -> Latest start time
            min(end)=min(120,70)=70   -> Earliest end time
            overlap=[60,70], length=10 -> Too short for duration=12
            Move j pointer (70 < 120)
    
    Case 4: No more slots in slots2 to compare
            Return []
    """
    slots1.sort()
    slots2.sort()
    i = j = 0
    
    while i < len(slots1) and j < len(slots2):
        # Current state tracking for each iteration
        """
        Iteration 1:
        i=0, j=0
        slots1[i]=[10,50], slots2[j]=[0,15]
        start=max(10,0)=10, end=min(50,15)=15
        overlap=5 < duration=12
        Move j (15 < 50)
        
        Iteration 2:
        i=0, j=1
        slots1[i]=[10,50], slots2[j]=[60,70]
        No overlap (50 < 60)
        Move i
        
        Iteration 3:
        i=1, j=1
        slots1[i]=[60,120], slots2[j]=[60,70]
        start=max(60,60)=60, end=min(120,70)=70
        overlap=10 < duration=12
        Move j (70 < 120)
        
        Iteration 4:
        j=2 (out of bounds), exit loop
        Return []
        """
        
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])
        
        if end - start >= duration:
            return [start, start + duration]
            
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1
    
    return []

# Test case
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 12