"""
https://leetcode.com/discuss/interview-question/2199394/Google-or-Phone-or-Time-for-turn
Problem description
Joseph is standing at k+1th position in a queue at an insurance company's office 
and there are n counters at the office, ith counter takes time[i] time (minutes) 
to process a request. The security guard assigns a counter to the person standing 
in the front of the queue as soon as a counter is available or if multiple counters
are available, then the security official assigns the counter with minimum id 
(consider id as index). What would be the time at which Joseph's request would be 
processed aka the ending time when Joseph leaves the office?

Examples
Input: time=[3,2,5], k=4
Output: 6
Explanation: Joseph is standing at 5th position (1-indexed). Initially, all counters
are empty so people at positions 1-3 are put to the respective counters. After 2 
minutes, counter 2 (1-indexed) gets empty and person at position 4 is assigned to the 
counter. After 1 more minute, counter 1 gets empty and now Joseph is assigned the 
counter 1. Joseph leaves after 3 minutes from the counter. So, in total, Joseph spends 
6 minutes in the office.
"""
from heapq import heappush, heappop, heapify

def timeForTurn(n, times, k):
    if n > k:
        return times[k]
    
    heap = [(time, i) for i, time in enumerate(times)]
    heapify(heap)

    for j in range(k-n):
        etime, index = heappop(heap)
        new_etime = etime + times[index]
        heappush(heap, (new_etime, index))

    etime, index = heappop(heap)
    return etime + times[index]

def main():
    print(timeForTurn(3, [3,2,5], 4))  # 6
    print(timeForTurn(3, [3,2,5], 3))  # 4
    print(timeForTurn(3, [3,2,5], 2))  # 5

if __name__ == "__main__":
    main()
"""
PATTERN RECOGNITION:
------------------
This is a Scheduling/Simulation problem that can be solved using:
1. Priority Queue (Min Heap)
2. Custom sorting/comparison logic
3. Time-based simulation

Visual Representation:
Time →  0   1   2   3   4   5   6   7   8
C0    [---P1---][-----P5(Joseph)-----]
C1    [--P2--][--P4--]
C2    [-------P3-------]
Queue:  1 2 3 4 5

Key Insights:
1. Need to track end times for each counter
2. Must consider counter ID for ties
3. Joseph (k+1th person) must wait for k people before them

DATA STRUCTURE ANALYSIS:
----------------------
Options considered:
1. Array + Sorting:
   + Simple to implement
   - O(n log n) per operation
   
2. Priority Queue (Chosen):
   + O(log n) per operation
   + Natural fit for time-based processing
   + Easy to maintain sorted order
   + Efficient for repeatedly finding minimum

3. Simulation Array:
   + Easy to visualize
   - Wasteful for sparse times
   - Harder to handle variable processing times
"""
"""
For times = [3,2,5]

First iteration simulation:
-------------------------
Initial heap: [(0,0), (0,1), (0,2)]
Pop (0,0) -> Counter 0 gets first person
New end time = 0 + times[0] = 0 + 3 = 3
Push (3,0)

Heap state after first iteration:
Before: [(0,0), (0,1), (0,2)]
After:  [(0,1), (0,2), (3,0)]  # Correct!

Second iteration:
---------------
Pop (0,1) -> Counter 1 gets second person
New end time = 0 + times[1] = 0 + 2 = 2
Push (2,1)

Heap state:
Before: [(0,1), (0,2), (3,0)]
After:  [(0,2), (2,1), (3,0)]

Third iteration:
--------------
Pop (0,2) -> Counter 2 gets third person
New end time = 0 + times[2] = 0 + 5 = 5
Push (5,2)

Heap state:
Before: [(0,2), (2,1), (3,0)]
After:  [(2,1), (3,0), (5,2)]

Fourth iteration:
---------------
Pop (2,1) -> Counter 1 gets fourth person
New end time = 2 + times[1] = 2 + 2 = 4
Push (4,1)

Heap state:
Before: [(2,1), (3,0), (5,2)]
After:  [(3,0), (4,1), (5,2)]

Finally, for Joseph (fifth person):
--------------------------------
Pop (3,0) -> Counter 0 gets Joseph
Final time = 3 + times[0] = 3 + 3 = 6
"""
import heapq
from typing import List

def process_queue(n: int, times: List[int], k: int) -> int:
    """
    Calculate when the k+1th person (Joseph) will finish their request.
    
    Parameters:
    n: number of counters
    times: list of processing times for each counter
    k: Joseph's position (0-based) in queue
    
    Returns:
    int: Time when Joseph's request completes
    
    Time Complexity: O(k log n)
    Space Complexity: O(n)
    
    Visual Example:
    n=3, times=[3,2,5], k=4
    
    Initial State:
    Counters: C0(0), C1(0), C2(0)
    Queue: [P1 P2 P3 P4 P5(J)]
    
    Simulation:
    1. P1 → C0: [(C0,3), (C1,0), (C2,0)]
    2. P2 → C1: [(C1,2), (C2,0), (C0,3)]
    3. P3 → C2: [(C1,2), (C0,3), (C2,5)]
    4. P4 → C1: [(C0,3), (C2,5), (C1,4)]
    5. P5(J)→C0: [(C1,4), (C2,5), (C0,6)]
    """
    
    # Custom heap entries: (end_time, counter_id)
    # Counter_id used for breaking ties
    heap = [(0, i) for i in range(n)]
    heapq.heapify(heap)
    
    """
    Heap visualization after initialization:
            (0,0)
           /     \
        (0,1)   (0,2)
    """
    
    # Process k people before Joseph
    for _ in range(k):
        end_time, counter = heapq.heappop(heap)
        # New end time = current end time + processing time
        heapq.heappush(heap, (end_time + times[counter], counter))
        
        """
        Example heap state after first iteration:
        Before: [(0,0), (0,1), (0,2)]
        After:  [(0,1), (0,2), (3,0)]
        """
    
    # Process Joseph's request
    end_time, counter = heapq.heappop(heap)
    final_time = end_time + times[counter]
    
    """
    Final state visualization for example:
    Time →  0   1   2   3   4   5   6   7   8
    C0    [---P1---][-----P5(Joseph)-----]
    C1    [--P2--][--P4--]
    C2    [-------P3-------]
    """
    
    return final_time

# Test with example case
def test_process_queue():
    """
    Test cases with visualizations
    """
    test_cases = [
        {
            'n': 3,
            'times': [3, 2, 5],
            'k': 4,
            'expected': 6
        },
        # Add more test cases
    ]
    
    for tc in test_cases:
        result = process_queue(tc['n'], tc['times'], tc['k'])
        print(f"\nTest Case:")
        print(f"n = {tc['n']}, times = {tc['times']}, k = {tc['k']}")
        print(f"Expected: {tc['expected']}, Got: {result}")
        
        # Visualization of processing
        max_time = max(result, tc['expected'])
        for i in range(tc['n']):
            print(f"C{i}: ", end="")
            timeline = ["·"] * (max_time + 1)
            # Add processing visualization here
            print("".join(timeline))

if __name__ == "__main__":
    test_process_queue()