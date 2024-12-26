# https://leetcode.com/problems/course-schedule-iv/description/
# 1462. Course Schedule IV
# Medium
# Topics
# Companies
# Hint
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.

 

# Example 1:


# Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
# Course 0 is not a prerequisite of course 1, but the opposite is true.
# Example 2:

# Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
# Output: [false,false]
# Explanation: There are no prerequisites, and each course is independent.
# Example 3:


# Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]
 

# Constraints:

# 2 <= numCourses <= 100
# 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
# prerequisites[i].length == 2
# 0 <= ai, bi <= numCourses - 1
# ai != bi
# All the pairs [ai, bi] are unique.
# The prerequisites graph has no cycles.
# 1 <= queries.length <= 104
# 0 <= ui, vi <= numCourses - 1
# ui != vi

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 69.6K
# Submissions
# 137.9K
# Acceptance Rate
# 50.5%
# Topics
# Companies
# Hint 1
# Imagine if the courses are nodes of a graph. We need to build an array isReachable[i][j].
# Hint 2
# Start a bfs from each course i and assign for each course j you visit isReachable[i][j] = True.
# Hint 3
# Answer the queries from the isReachable array.
from typing import List
from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Determines if courses are prerequisites of other courses using Floyd-Warshall algorithm.
        
        Time Complexity: O(n^3) where n is numCourses
        Space Complexity: O(n^2) for the reachability matrix
        
        Visualization for Example 3:
        numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]]
        
        Initial graph:
        0 <--- 2 <--- 1
        ^           /
        |         /
        '---------'
        
        Reachability matrix visualization:
           0  1  2
        0  T  F  F    T = True, F = False
        1  T  T  T    Row i, Col j means: Can course i reach course j?
        2  T  F  T
        
        Process:
        1. Build adjacency list:
            0: []
            1: [0, 2]
            2: [0]
            
        2. Floyd-Warshall builds transitive closure:
            - Initially: Only direct prerequisites
            - After: All reachable courses
            
        3. Query resolution:
            - For query [1,0]: Check reachability[1][0] = True
            - For query [1,2]: Check reachability[1][2] = True
        """
        # Initialize reachability matrix
        reachability = [[False] * numCourses for _ in range(numCourses)]
        
        # Set diagonal to True (course is prerequisite of itself)
        for i in range(numCourses):
            reachability[i][i] = True
            
        # Set direct prerequisites
        for pre, course in prerequisites:
            reachability[pre][course] = True
            
        """
        Floyd-Warshall algorithm visualization:
        For k = 0:
           0  1  2
        0  T  F  F
        1  T  T  T
        2  T  F  T
        
        For k = 1:
           0  1  2
        0  T  F  F
        1  T  T  T
        2  T  F  T
        
        For k = 2:
           0  1  2
        0  T  F  F
        1  T  T  T
        2  T  F  T
        """
        # Floyd-Warshall algorithm for transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachability[i][j] = reachability[i][j] or (
                        reachability[i][k] and reachability[k][j]
                    )
                    
        # Process queries using completed reachability matrix
        return [reachability[u][v] for u, v in queries]

    def checkIfPrerequisite_dfs(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Alternative DFS solution for comparison.
        
        Time Complexity: O(Q * (V + E)) where:
        - Q is number of queries
        - V is number of courses
        - E is number of prerequisites
        
        Space Complexity: O(V + E)
        """
        # Build adjacency list
        graph = defaultdict(list)
        for pre, course in prerequisites:
            graph[pre].append(course)
            
        def is_prerequisite(start: int, target: int, visited: set) -> bool:
            if start == target:
                return True
            if start in visited:
                return False
                
            visited.add(start)
            return any(is_prerequisite(next_course, target, visited) 
                      for next_course in graph[start])
                      
        return [is_prerequisite(u, v, set()) for u, v in queries]

"""
Implementation Analysis:

1. Floyd-Warshall Approach:
   Pros:
   - O(1) query time after preprocessing
   - Handles multiple queries efficiently
   - Simple to implement
   
   Cons:
   - O(n^3) preprocessing time
   - O(n^2) space complexity
   - Overkill for few queries

2. DFS Approach:
   Pros:
   - No preprocessing needed
   - Better space complexity
   - Better for sparse graphs
   
   Cons:
   - O(V+E) per query
   - Less efficient for many queries
   
Trade-offs Discussion:
- Use Floyd-Warshall when:
  * Many queries expected
  * Dense prerequisite graph
  * Query response time critical
  
- Use DFS when:
  * Few queries
  * Sparse prerequisite graph
  * Memory constraints

Real-world considerations:
1. Cache frequently queried results
2. Consider parallel processing for large graphs
3. Monitor memory usage in production
"""

# Test code
def test_solution():
    solution = Solution()
    
    # Test case 1
    assert solution.checkIfPrerequisite(
        2, [[1,0]], [[0,1],[1,0]]
    ) == [False, True], "Test case 1 failed"
    
    # Test case 2
    assert solution.checkIfPrerequisite(
        2, [], [[1,0],[0,1]]
    ) == [False, False], "Test case 2 failed"
    
    # Test case 3
    assert solution.checkIfPrerequisite(
        3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]
    ) == [True, True], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()