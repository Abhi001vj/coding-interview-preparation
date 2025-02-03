# 1101. The Earliest Moment When Everyone Become Friends
# Medium
# Topics
# Companies
# Hint
# There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

# Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

# Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.

 

# Example 1:

# Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
# Output: 20190301
# Explanation: 
# The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
# The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
# The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
# The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
# The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
# The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.
# Example 2:

# Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
# Output: 3
# Explanation: At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.
 

# Constraints:

# 2 <= n <= 100
# 1 <= logs.length <= 104
# logs[i].length == 3
# 0 <= timestampi <= 109
# 0 <= xi, yi <= n - 1
# xi != yi
# All the values timestampi are unique.
# All the pairs (xi, yi) occur at most one time in the input.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 109.9K
# Submissions
# 167.7K
# Acceptance Rate
# 65.5%
# Topics
# Companies
# Hint 1
# Sort the log items by their timestamp.
# Hint 2
# How can we model this problem as a graph problem?
# Hint 3
# Let's use a union-find data structure. At the beginning we have a graph with N nodes but no edges.
# Hint 4
# Then we loop through the events and unite each node until the number of connected components reach to 1. Notice that each time two different connected components are united the number of connected components decreases by 1.


"""
Problem: Earliest Moment When Everyone Become Friends
Level: Google L5 Interview

DSA Pattern Recognition:
1. Graph Problem - Each person is a node, friendships are edges
2. Connected Components - Need to track when everyone becomes connected
3. Union-Find - Perfect for dynamic connectivity
4. Sorting - Process events chronologically

Example Visualization:
logs = [[20190101,0,1], [20190104,3,4], [20190107,2,3]]
n = 5

Timeline visualization:
t=20190101:  [0-1] [2] [3] [4]
                ↓
t=20190104:  [0-1] [2] [3-4]
                ↓
t=20190107:  [0-1] [2-3-4]

Union-Find Tree Evolution:
Initial:     0   1   2   3   4
            [0] [1] [2] [3] [4]  components=5

After 0-1:   0   1   2   3   4
            [0]-[1] [2] [3] [4]  components=4

After 3-4:   0   1   2   3   4
            [0]-[1] [2] [3]-[4]  components=3

After 2-3:   0   1   2   3   4
            [0]-[1] [2]-[3]-[4]  components=2

Big O Analysis:
Time: O(α(n) * E + E log E) where:
- E = number of edges (logs)
- α(n) = inverse Ackermann function (effectively constant)
- E log E from sorting logs
Space: O(n) for Union-Find data structures
"""

class UnionFind:
    """
    UnionFind with path compression and union by rank.
    Operations are effectively O(1) amortized time.
    """
    def __init__(self, n):
        """
        Initialize Union-Find data structure
        Time: O(n)
        Space: O(n)
        """
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n           # Track tree heights for balancing
        self.components = n           # Track number of separate groups

    def find(self, x):
        """
        Find with path compression optimization
        Time: O(α(n)) ≈ O(1) amortized
        
        Path Compression Visualization:
        Before:      After:
        [A]         [A]
         |           | \
        [B]   =>   [B] [C]
         |
        [C]
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """
        Union with rank optimization
        Time: O(α(n)) ≈ O(1) amortized
        Returns: True if new connection made
        
        Rank Visualization (px.rank < py.rank):
        Before:    After:
        [A]r=1    [B]r=2
         |         | \
        [C]       [D] [A]
                      |
                     [C]
        """
        px, py = self.find(x), self.find(y)
        
        if px == py:  # Already connected
            return False
            
        # Union by rank: attach smaller rank tree under root of higher rank tree
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        
        # If same rank, increment rank of root
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
            
        self.components -= 1  # One less separate component
        return True

    def is_all_connected(self):
        """Check if everyone is in same component
        Time: O(1)
        """
        return self.components == 1

def earliest_friends_time(logs: List[List[int]], n: int) -> int:
    """
    Main solution function
    Time: O(E log E) where E is number of logs
    Space: O(n) where n is number of people
    
    Approach:
    1. Sort logs by timestamp
    2. Process each friendship chronologically
    3. Use Union-Find to track connections
    4. Return earliest time when everyone connected
    """
    # Edge cases
    if not logs or n <= 1:
        return -1
    
    # Sort logs by timestamp
    # Time: O(E log E), Space: O(1) or O(E) depending on sort implementation
    logs.sort(key=lambda x: x[0])
    
    # Initialize Union-Find
    # Time: O(n), Space: O(n)
    uf = UnionFind(n)
    
    # Process each friendship formation
    # Time: O(E * α(n)) ≈ O(E) since α(n) is effectively constant
    for time, x, y in logs:
        # Add new friendship
        uf.union(x, y)
        
        # Check if everyone is now connected
        if uf.is_all_connected():
            return time
    
    return -1

"""
Test Cases:
1. Basic case:
logs = [[1,0,1], [2,1,2], [3,2,3]]
n = 4
Expected: 3

2. Already connected:
logs = [[1,0,1], [2,0,1]]
n = 2
Expected: 1

3. Can't connect everyone:
logs = [[1,0,1], [2,2,3]]
n = 4
Expected: -1

4. Single timestamp connects all:
logs = [[1,0,1], [1,1,2], [1,2,3]]
n = 4
Expected: 1

5. Edge cases:
- Empty logs -> -1
- n = 1 -> -1
- Invalid indices -> -1

Big O Analysis Detailed Breakdown:
1. Sorting logs: O(E log E)
2. Union-Find initialization: O(n)
3. Processing logs:
   - Each union/find: O(α(n))
   - Total for E logs: O(E * α(n))
4. Overall: O(E log E + n)
   Dominated by sorting when E > n
   
Space Complexity Breakdown:
1. Union-Find structures:
   - parent array: O(n)
   - rank array: O(n)
2. Input storage: O(E)
3. Overall: O(n + E)
"""

# Test the solution
def test_earliest_friends():
    test_cases = [
        {
            'logs': [[20190101,0,1],[20190104,3,4],[20190107,2,3],
                    [20190211,1,5],[20190224,2,4],[20190301,0,3]],
            'n': 6,
            'expected': 20190301
        },
        {
            'logs': [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]],
            'n': 4,
            'expected': 3
        }
    ]
    
    for tc in test_cases:
        result = earliest_friends_time(tc['logs'], tc['n'])
        assert result == tc['expected']