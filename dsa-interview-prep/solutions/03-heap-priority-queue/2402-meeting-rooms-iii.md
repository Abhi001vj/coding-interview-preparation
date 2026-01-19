# 2402. Meeting Rooms III

**Difficulty:** Hard
**Pattern:** Two Heaps (Simulation)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** You are given an integer `n` (number of rooms) and a 2D integer array `meetings` where `meetings[i] = [start, end]`. All the values of `start` are unique. Meetings are allocated to rooms in the following manner:
1. Each meeting will take place in the unused room with the **lowest number**.
2. If there are no used rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the **same duration** as the original meeting.
3. When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

**Interview Scenario (The "Load Balancer" Prompt):**
"You are designing a job scheduler for a cluster of `N` worker nodes (indexed 0 to N-1). Jobs arrive with a specific start time and duration. We want to maximize the utilization of lower-indexed nodes (perhaps they are cheaper or closer). If all nodes are busy, jobs queue up and wait. When a node frees up, the longest-waiting job grabs it. Which node processes the most jobs?"

**Why this transformation?**
*   It moves from "meeting rooms" to "resource scheduling", a very common system design context.
*   It emphasizes the specific tie-breaking rules (lowest index) and waiting logic.

---

## 2. Clarifying Questions (Phase 1)

1.  **Sorting:** "Are meetings sorted by start time?" (Input isn't guaranteed, so we must sort them first).
2.  **Delay Logic:** "Does the delay shift *subsequent* meetings?" (The problem implies we process meetings in original order. If a meeting is delayed, it finishes later, which might delay future meetings that were waiting for *that specific* room? No, it just occupies a room longer. The "arrival" of future meetings is fixed).
3.  **Tie-Breaking:** "If multiple rooms free up at the same time, which one is chosen?" (The one with the lowest index).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Two Heaps (Free vs. Busy).

**The State:**
We need to track two sets of rooms:
1.  **Available Rooms:** Currently empty. We need to pick the *lowest index*. -> **Min-Heap (index)**.
2.  **Busy Rooms:** Currently occupied. We need to know *when* they become free. -> **Min-Heap (end_time, index)**.

**Simulation Logic:**
1.  Sort meetings by `start_time`.
2.  Iterate through meetings:
    *   **Free up rooms:** Check the "Busy Heap". If `busy_room.end_time <= current_meeting.start`, move it to the "Available Heap".
    *   **Allocation:**
        *   If "Available Heap" is not empty: Pop smallest index. Schedule meeting. Push to "Busy Heap" with `end_time = current_meeting.end`.
        *   If "Available Heap" IS empty: We must wait. Pop the *earliest finishing* room from "Busy Heap".
            *   New Start = `busy_room.end_time`.
            *   New End = `New Start + duration`.
            *   Push back to "Busy Heap".
            *   **Crucial:** We don't put it back in "Available" because it's immediately re-occupied.

---

## 4. Base Template & Modification

**Standard Interval/Heap Template:**
```python
meetings.sort()
free_rooms = [i for i in range(n)]
heapify(free_rooms)
busy_rooms = [] # (end_time, index)

for start, end in meetings:
    while busy_rooms and busy_rooms[0][0] <= start:
        t, idx = heappop(busy_rooms)
        heappush(free_rooms, idx)
    
    if free_rooms:
        idx = heappop(free_rooms)
        heappush(busy_rooms, (end, idx))
    else:
        # Handling delay logic
```

**Modified Logic:**
Handle the delay math correctly (`new_end = room_end + duration`). Track usage counts.

---

## 5. Optimal Solution

```python
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Count of meetings per room
        count = [0] * n
        
        # Sort meetings by start time
        meetings.sort()
        
        # Min-Heap for available rooms (stores just room_index)
        # Prioritizes smallest room index
        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)
        
        # Min-Heap for busy rooms (stores (end_time, room_index))
        # Prioritizes earliest end time, then smallest room index
        busy_rooms = []
        
        for start, end in meetings:
            # 1. Free up rooms that have finished before or at the current meeting's start time
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room_idx = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room_idx)
                
            # 2. Assign room
            if available_rooms:
                # Use the lowest indexed available room
                room_idx = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room_idx))
            else:
                # No room available. Wait for the earliest one to free up.
                earliest_end_time, room_idx = heapq.heappop(busy_rooms)
                
                # The meeting starts when the room becomes free
                # New end time = room's finish time + duration
                duration = end - start
                new_end_time = earliest_end_time + duration
                
                heapq.heappush(busy_rooms, (new_end_time, room_idx))
            
            # Increment count for the chosen room
            count[room_idx] += 1
            
        # Return room with max meetings (lowest index tie-break)
        # argmax with index preference
        max_meetings = -1
        result_room = -1
        for i in range(n):
            if count[i] > max_meetings:
                max_meetings = count[i]
                result_room = i
        return result_room
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(M \log M + M \log N)$
    *   $M$ is number of meetings. $N$ is number of rooms.
    *   Sorting meetings: $O(M \log M)$.
    *   Heap operations: Each meeting involves push/pop on heaps of size $N$. So $O(M \log N)$.
*   **Space Complexity:** $O(N)$
    *   Heaps store $N$ rooms.

---

## 7. Follow-up & Extensions

**Q: What if meetings have priorities?**
**A:** We would need a Priority Queue for the *waiting meetings* as well, instead of just iterating the sorted list.

**Q: Meeting Rooms II (Min rooms required)?**
**A:** That is solved by tracking just start/end events or a single Min-Heap of end times. This problem (Rooms III) is harder because the *number* of rooms is fixed and we track *usage*.
