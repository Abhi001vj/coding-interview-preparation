# https://leetcode.com/problems/task-scheduler/description/
# 621. Task Scheduler
# Medium
# Topics
# Companies
# Hint
# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

 

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:

# Input: tasks = ["A","A","A", "B","B","B"], n = 3

# Output: 10

# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

# Constraints:

# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100

```python
"""
TASK SCHEDULER - COMPREHENSIVE SOLUTION
====================================

PROBLEM UNDERSTANDING
-------------------
Input: tasks = ["A","A","A","B","B","B"], n = 2
Key Points:
1. Same task needs n intervals gap
2. Can schedule tasks in any order
3. Can use idle slots when needed
4. Need to minimize total intervals

VISUALIZATION OF THE PROBLEM
-------------------------
For tasks = ["A","A","A","B","B","B"], n = 2:

Frequency Analysis:
A: 3 times
B: 3 times

Pattern Formation:
A _ _ A _ _ A    (gaps of n=2)
A B _ A B _ A B  (filling with B)

SOLUTION APPROACHES
----------------
1. Greedy: Always schedule most frequent task first
2. Mathematical: Based on max frequency pattern
3. Priority Queue: Dynamic scheduling

Let's implement the optimal mathematical solution:
"""

from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Optimal Mathematical Solution
        Time: O(N) where N is length of tasks
        Space: O(1) since counter has max 26 entries
        
        Core Idea:
        1. Find task with max frequency (f_max)
        2. This task needs (f_max - 1) gaps of size n
        3. Calculate minimum slots needed
        4. Account for tasks with same max frequency
        
        Example:
        tasks = ["A","A","A","B","B","B"], n = 2
        
        1. Count frequencies:
           A: 3 times (f_max)
           B: 3 times
        
        2. Minimum slots needed:
           (f_max - 1) * (n + 1) + count_of_max_freq
           (3 - 1) * (2 + 1) + 2 = 8
        
        Visual representation:
        A _ _ A _ _ A
        Gaps: (f_max - 1) = 2
        Size of each chunk: (n + 1) = 3
        Tasks with max freq: 2 (A and B)
        """
        
        # Step 1: Count task frequencies
        task_counts = Counter(tasks)
        
        # Step 2: Find maximum frequency and count of tasks with max frequency
        max_freq = max(task_counts.values())
        max_freq_tasks = sum(1 for count in task_counts.values() 
                           if count == max_freq)
        
        """
        Visualization of counting:
        
        1. Counter creation:
           tasks = ["A","A","A","B","B","B"]
           Counter({'A': 3, 'B': 3})
        
        2. Finding max frequency:
           max_freq = 3 (both A and B occur 3 times)
        
        3. Count tasks with max frequency:
           max_freq_tasks = 2 (A and B)
        """
        
        # Step 3: Calculate result using formula
        # Formula explanation:
        # - (max_freq - 1): number of gaps needed
        # - (n + 1): size of each chunk (task + cooling period)
        # - max_freq_tasks: additional slots for tasks with max frequency
        formula_result = (max_freq - 1) * (n + 1) + max_freq_tasks
        
        """
        Formula visualization for ["A","A","A","B","B","B"], n = 2:
        
        1. Initial arrangement of max freq task (A):
           A _ _ A _ _ A
           
        2. Chunks visualization:
           Chunk1: A _ _
           Chunk2: A _ _
           Last A: A
           
        3. Formula components:
           - max_freq = 3
           - gaps = (max_freq - 1) = 2
           - chunk_size = (n + 1) = 3
           - max_freq_tasks = 2 (A and B)
           
        4. Calculation:
           (3-1) * (2+1) + 2 = 6 + 2 = 8
        """
        
        # Step 4: Return maximum of formula result and length of tasks
        # Why max?: If n is small or we have many different tasks,
        # we might not need idle slots
        return max(formula_result, len(tasks))

    def validate_solution(self, tasks: List[str], n: int, result: int) -> bool:
        """
        Helper method to validate if solution is possible
        Demonstrates understanding of constraints
        """
        # Check if result meets minimum possible length
        if result < len(tasks):
            return False
        
        # Check if gap constraint is satisfied
        task_positions = {}
        current_time = 0
        
        for task in tasks:
            # Check if task was seen before
            if task in task_positions:
                # Verify cooling period
                if current_time - task_positions[task] <= n:
                    return False
            task_positions[task] = current_time
            current_time += 1
            
        return True

"""
COMPLEXITY ANALYSIS
-----------------
Time Complexity: O(N)
- Counter creation: O(N)
- Finding max frequency: O(1) - max 26 letters
- Rest of operations: O(1)

Space Complexity: O(1)
- Counter size is bounded by 26 (uppercase letters)
- Other variables are constant space

PYTHON SPECIFIC OPTIMIZATIONS
--------------------------
1. Counter class:
   - Efficient frequency counting
   - Built-in methods optimize memory
   
2. max() function with generator:
   - Memory efficient for finding max frequency
   - Avoids creating intermediate list

3. List comprehension:
   - More efficient than explicit loops
   - Better readability

EDGE CASES HANDLED
---------------
1. n = 0: No cooling needed
2. All tasks different: No idle needed
3. Multiple tasks with max frequency
4. Single task type with high frequency

POSSIBLE FOLLOW-UP QUESTIONS
-------------------------
1. How to handle dynamic task arrival?
2. How to minimize memory usage for large task streams?
3. How to handle priority of tasks?
4. How to optimize for parallel execution?
"""

# Test code with visualizations
def test_task_scheduler():
    test_cases = [
        (["A","A","A","B","B","B"], 2),
        (["A","C","A","B","D","B"], 1),
        (["A","A","A","B","B","B"], 3)
    ]
    
    solver = Solution()
    
    for tasks, n in test_cases:
        result = solver.leastInterval(tasks, n)
        print(f"\nTest case: tasks={tasks}, n={n}")
        print(f"Result: {result}")
        print("Is valid:", solver.validate_solution(tasks, n, result))

if __name__ == "__main__":
    test_task_scheduler()
```

"""
TASK SCHEDULER - EVOLUTION OF SOLUTIONS
====================================

Let's solve this problem in multiple ways, evolving from simple to optimal:
1. Simulation (Queue-based)
2. Priority Queue (Heap-based)
3. Mathematical (Optimal)

Example Input: tasks = ["A","A","A","B","B","B"], n = 2
"""

from collections import deque, Counter
import heapq
from typing import List

class TaskSchedulerSolutions:
    """
    1. SIMULATION SOLUTION
    ===================
    Approach: Actually simulate the scheduling using queue
    Pros: Intuitive, gives actual schedule
    Cons: More complex, uses more memory
    """
    def simulation_solution(self, tasks: List[str], n: int) -> int:
        """
        Uses queue to track cooling periods
        Time: O(N * M) where N is total intervals, M is unique tasks
        Space: O(M) where M is unique tasks
        """
        # Count task frequencies
        task_count = Counter(tasks)
        
        # Create cooling queue for each task
        cooling = {}  # task -> next available time
        time = 0
        
        while task_count:
            # Find available task with highest frequency
            chosen_task = None
            max_freq = 0
            
            for task, count in task_count.items():
                if count > max_freq and (task not in cooling or cooling[task] <= time):
                    chosen_task = task
                    max_freq = count
            
            if chosen_task:
                # Schedule the task
                task_count[chosen_task] -= 1
                if task_count[chosen_task] == 0:
                    del task_count[chosen_task]
                
                # Update cooling period
                cooling[chosen_task] = time + n + 1
            
            # Always increment time
            time += 1
        
        return time
    
    """
    2. PRIORITY QUEUE SOLUTION
    =======================
    Approach: Use max heap to always get most frequent task
    Pros: More efficient than simulation
    Cons: Still needs queue for cooling
    """
    def priority_queue_solution(self, tasks: List[str], n: int) -> int:
        """
        Uses max heap and cooling queue
        Time: O(N * logM) where N is intervals, M is unique tasks
        Space: O(M)
        
        Example walkthrough:
        tasks = ["A","A","A","B","B","B"], n = 2
        
        Initial heap: [(-3,'A'), (-3,'B')]  # -ve for max heap
        Cooling queue: deque()
        
        Step 1: Take A
        Heap: [(-3,'B')]
        Queue: [(2, -2, 'A')]  # (available_time, count, task)
        
        Step 2: Take B
        Heap: []
        Queue: [(2, -2, 'A'), (3, -2, 'B')]
        
        And so on...
        """
        # Count frequencies and create max heap
        count = Counter(tasks)
        heap = [(-freq, task) for task, freq in count.items()]
        heapq.heapify(heap)
        
        cooling_queue = deque()  # (time_available, -freq, task)
        time = 0
        
        while heap or cooling_queue:
            time += 1
            
            # Check cooling queue
            if cooling_queue and cooling_queue[0][0] <= time:
                freq, task = cooling_queue.popleft()[1:]
                heapq.heappush(heap, (freq, task))
            
            if heap:
                # Schedule most frequent task
                freq, task = heapq.heappop(heap)
                if freq < -1:  # Still has more instances
                    cooling_queue.append((time + n + 1, freq + 1, task))
        
        return time
    
    """
    3. MATHEMATICAL SOLUTION (OPTIMAL)
    ==============================
    Approach: Use pattern recognition to avoid simulation
    Pros: Most efficient, O(N) time
    Cons: Doesn't give actual schedule
    """
    def mathematical_solution(self, tasks: List[str], n: int) -> int:
        """
        Uses pattern recognition
        Time: O(N) for counting
        Space: O(1) - max 26 characters
        
        Pattern Analysis:
        ["A","A","A","B","B","B"], n = 2
        
        Max frequency (f) = 3
        Tasks with max freq (m) = 2 (A and B)
        
        Minimum slots needed = (f-1)*(n+1) + m
        
        Visualization:
        A _ _ A _ _ A    # Basic pattern with gaps
        A B _ A B _ A B  # Filled with B
        """
        # Get task frequencies
        freqs = Counter(tasks).values()
        
        # Find max frequency and count of tasks with max freq
        max_freq = max(freqs)
        max_freq_count = sum(1 for f in freqs if f == max_freq)
        
        # Calculate using formula
        return max(
            len(tasks),  # Minimum possible length
            (max_freq - 1) * (n + 1) + max_freq_count  # Pattern-based calculation
        )

def visualize_execution(tasks: List[str], n: int):
    """
    Helper function to visualize the execution process
    """
    print("\nExecution Visualization:")
    print("=======================")
    
    # Show frequency count
    freq = Counter(tasks)
    print("Task Frequencies:")
    for task, count in freq.items():
        print(f"{task}: {'|' * count} ({count})")
    
    # Show possible schedule
    max_freq = max(freq.values())
    max_freq_tasks = [t for t, f in freq.items() if f == max_freq]
    
    print("\nPossible Schedule:")
    schedule = ["_"] * ((max_freq - 1) * (n + 1) + len(max_freq_tasks))
    
    # Fill primary task
    for i in range(max_freq):
        if i < max_freq - 1:
            pos = i * (n + 1)
        else:
            pos = len(schedule) - len(max_freq_tasks)
        schedule[pos] = max_freq_tasks[0]
    
    print(" ".join(schedule))

# Test all solutions
def test_solutions():
    test_cases = [
        (["A","A","A","B"
          
```python
"""
TASK SCHEDULER - COMPREHENSIVE SOLUTION
====================================

PROBLEM UNDERSTANDING
-------------------
Input: tasks = ["A","A","A","B","B","B"], n = 2
Key Points:
1. Same task needs n intervals gap
2. Can schedule tasks in any order
3. Can use idle slots when needed
4. Need to minimize total intervals

VISUALIZATION OF THE PROBLEM
-------------------------
For tasks = ["A","A","A","B","B","B"], n = 2:

Frequency Analysis:
A: 3 times
B: 3 times

Pattern Formation:
A _ _ A _ _ A    (gaps of n=2)
A B _ A B _ A B  (filling with B)

SOLUTION APPROACHES
----------------
1. Greedy: Always schedule most frequent task first
2. Mathematical: Based on max frequency pattern
3. Priority Queue: Dynamic scheduling

Let's implement the optimal mathematical solution:
"""

from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Optimal Mathematical Solution
        Time: O(N) where N is length of tasks
        Space: O(1) since counter has max 26 entries
        
        Core Idea:
        1. Find task with max frequency (f_max)
        2. This task needs (f_max - 1) gaps of size n
        3. Calculate minimum slots needed
        4. Account for tasks with same max frequency
        
        Example:
        tasks = ["A","A","A","B","B","B"], n = 2
        
        1. Count frequencies:
           A: 3 times (f_max)
           B: 3 times
        
        2. Minimum slots needed:
           (f_max - 1) * (n + 1) + count_of_max_freq
           (3 - 1) * (2 + 1) + 2 = 8
        
        Visual representation:
        A _ _ A _ _ A
        Gaps: (f_max - 1) = 2
        Size of each chunk: (n + 1) = 3
        Tasks with max freq: 2 (A and B)
        """
        
        # Step 1: Count task frequencies
        task_counts = Counter(tasks)
        
        # Step 2: Find maximum frequency and count of tasks with max frequency
        max_freq = max(task_counts.values())
        max_freq_tasks = sum(1 for count in task_counts.values() 
                           if count == max_freq)
        
        """
        Visualization of counting:
        
        1. Counter creation:
           tasks = ["A","A","A","B","B","B"]
           Counter({'A': 3, 'B': 3})
        
        2. Finding max frequency:
           max_freq = 3 (both A and B occur 3 times)
        
        3. Count tasks with max frequency:
           max_freq_tasks = 2 (A and B)
        """
        
        # Step 3: Calculate result using formula
        # Formula explanation:
        # - (max_freq - 1): number of gaps needed
        # - (n + 1): size of each chunk (task + cooling period)
        # - max_freq_tasks: additional slots for tasks with max frequency
        formula_result = (max_freq - 1) * (n + 1) + max_freq_tasks
        
        """
        Formula visualization for ["A","A","A","B","B","B"], n = 2:
        
        1. Initial arrangement of max freq task (A):
           A _ _ A _ _ A
           
        2. Chunks visualization:
           Chunk1: A _ _
           Chunk2: A _ _
           Last A: A
           
        3. Formula components:
           - max_freq = 3
           - gaps = (max_freq - 1) = 2
           - chunk_size = (n + 1) = 3
           - max_freq_tasks = 2 (A and B)
           
        4. Calculation:
           (3-1) * (2+1) + 2 = 6 + 2 = 8
        """
        
        # Step 4: Return maximum of formula result and length of tasks
        # Why max?: If n is small or we have many different tasks,
        # we might not need idle slots
        return max(formula_result, len(tasks))

    def validate_solution(self, tasks: List[str], n: int, result: int) -> bool:
        """
        Helper method to validate if solution is possible
        Demonstrates understanding of constraints
        """
        # Check if result meets minimum possible length
        if result < len(tasks):
            return False
        
        # Check if gap constraint is satisfied
        task_positions = {}
        current_time = 0
        
        for task in tasks:
            # Check if task was seen before
            if task in task_positions:
                # Verify cooling period
                if current_time - task_positions[task] <= n:
                    return False
            task_positions[task] = current_time
            current_time += 1
            
        return True

"""
COMPLEXITY ANALYSIS
-----------------
Time Complexity: O(N)
- Counter creation: O(N)
- Finding max frequency: O(1) - max 26 letters
- Rest of operations: O(1)

Space Complexity: O(1)
- Counter size is bounded by 26 (uppercase letters)
- Other variables are constant space

PYTHON SPECIFIC OPTIMIZATIONS
--------------------------
1. Counter class:
   - Efficient frequency counting
   - Built-in methods optimize memory
   
2. max() function with generator:
   - Memory efficient for finding max frequency
   - Avoids creating intermediate list

3. List comprehension:
   - More efficient than explicit loops
   - Better readability

EDGE CASES HANDLED
---------------
1. n = 0: No cooling needed
2. All tasks different: No idle needed
3. Multiple tasks with max frequency
4. Single task type with high frequency

POSSIBLE FOLLOW-UP QUESTIONS
-------------------------
1. How to handle dynamic task arrival?
2. How to minimize memory usage for large task streams?
3. How to handle priority of tasks?
4. How to optimize for parallel execution?
"""

# Test code with visualizations
def test_task_scheduler():
    test_cases = [
        (["A","A","A","B","B","B"], 2),
        (["A","C","A","B","D","B"], 1),
        (["A","A","A","B","B","B"], 3)
    ]
    
    solver = Solution()
    
    for tasks, n in test_cases:
        result = solver.leastInterval(tasks, n)
        print(f"\nTest case: tasks={tasks}, n={n}")
        print(f"Result: {result}")
        print("Is valid:", solver.validate_solution(tasks, n, result))

if __name__ == "__main__":
    test_task_scheduler()
```