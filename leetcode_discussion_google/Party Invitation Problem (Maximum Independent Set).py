"""
Party Invitation Problem (Maximum Independent Set)

Input: [(1,2), (2,3), (3,4)]
Graph Visualization:
1 -- 2 -- 3 -- 4
Where -- represents "don't like each other"

Approaches:
1. Brute Force (try all combinations)
2. Graph Coloring
3. Dynamic Programming
"""

from collections import defaultdict
from typing import List, Set, Dict, Tuple

class Solution:
    def maxGuests(self, dislikes: List[Tuple[int, int]]) -> int:
        """
        Find maximum number of guests that can be invited
        Time: O(2^N) where N is number of people
        Space: O(N) for recursion stack and graph
        
        Visual example:
        dislikes = [(1,2), (2,3), (3,4)]
        
        Try including 1:
           1
           ↓
        Can't include 2
           ↓
        Can include 3
           ↓
        Can't include 4
        Count = 2 (1,3)
        """
        # Build adjacency list
        graph = defaultdict(set)
        people = set()
        
        # Create graph
        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)
            people.add(a)
            people.add(b)
            
        def is_valid_addition(guest: int, invited: Set[int]) -> bool:
            """
            Check if adding this guest creates conflicts
            Example: 
            invited = {1}, guest = 3
            Check if 3 dislikes anyone in {1}
            """
            return all(g not in graph[guest] for g in invited)
        
        def backtrack(candidates: Set[int], invited: Set[int]) -> int:
            """
            Try all possible combinations of guests
            
            Example state:
            candidates = {1,2,3,4}
            invited = {}
            
            Try including 1:
            candidates = {2,3,4}
            invited = {1}
            """
            if not candidates:
                return len(invited)
                
            # Try including next person
            person = candidates.pop()
            candidates_copy = set(candidates)
            max_guests = 0
            
            # Option 1: Include this person
            if is_valid_addition(person, invited):
                invited.add(person)
                # Remove their enemies from candidates
                candidates -= graph[person]
                include = backtrack(candidates, invited)
                max_guests = max(max_guests, include)
                # Restore state
                invited.remove(person)
                candidates = candidates_copy
                
            # Option 2: Skip this person
            exclude = backtrack(candidates, invited)
            max_guests = max(max_guests, exclude)
            
            # Restore state
            candidates.add(person)
            return max_guests
            
        return backtrack(people, set())

    def maxGuestsColoring(self, dislikes: List[Tuple[int, int]]) -> int:
        """
        Alternative approach using graph coloring
        Time: O(V+E) where V is vertices and E is edges
        Space: O(V) for colors and graph
        
        Visual:
        1(R) -- 2(B) -- 3(R) -- 4(B)
        Take max(count of Red, count of Blue)
        """
        graph = defaultdict(set)
        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)
            
        colors = {}  # 1: Red, -1: Blue
        
        def can_color(person: int, color: int) -> bool:
            """Check if we can assign color to person"""
            return all(colors.get(enemy, color) != color 
                      for enemy in graph[person])
        
        def color_graph(person: int, color: int) -> bool:
            """
            Color graph using two colors
            Returns if valid coloring is possible
            """
            colors[person] = color
            # Color all neighbors with opposite color
            for enemy in graph[person]:
                if enemy not in colors:
                    if not color_graph(enemy, -color):
                        return False
                elif colors[enemy] == color:
                    return False
            return True
            
        # Try coloring from each uncolored vertex
        for person in graph:
            if person not in colors:
                if not color_graph(person, 1):
                    return 0  # Not possible to color
                    
        # Count colors
        red = sum(1 for c in colors.values() if c == 1)
        blue = sum(1 for c in colors.values() if c == -1)
        return max(red, blue)

# Test cases
def test_party_invites():
    """
    Test with various scenarios:
    1. Linear conflicts
    2. Circular conflicts
    3. Disconnected groups
    4. No conflicts
    5. Everyone conflicts
    """
    test_cases = [
        ([(1,2), (2,3), (3,4)], 2),
        ([(1,2), (2,3), (3,1)], 1),
        ([(1,2), (3,4)], 2),
        ([], 0),
        ([(1,2), (2,3), (3,4), (4,1)], 2)
    ]
    
    solution = Solution()
    for dislikes, expected in test_cases:
        assert solution.maxGuests(dislikes) == expected
        assert solution.maxGuestsColoring(dislikes) == expected

"""
Edge Cases:
1. Empty dislike list
2. Single dislike pair
3. Circular conflicts
4. Disconnected groups
5. Everyone dislikes everyone
6. No dislikes at all

Analysis:
1. Brute Force (Backtracking):
   - Try all combinations
   - Time: O(2^N)
   - Space: O(N)

2. Graph Coloring:
   - 2-color the graph
   - Time: O(V+E)
   - Space: O(V)
   
3. Alternative approaches:
   - Maximum Independent Set algorithms
   - Bipartite matching
   - Dynamic Programming (for special cases)
"""