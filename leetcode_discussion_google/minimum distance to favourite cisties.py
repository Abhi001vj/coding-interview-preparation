# Google Interview Question: Minimum Distance to Favorite Cities

## Original Question
Given:
- A directed graph of cities where edges represent distances
- Current city (starting point)
- List of favorite cities
Find: Minimum distance needed to travel to reach any favorite city

## Example Visualization
```
Graph:
A ---4--→ B ---2--→ C
↓        ↗        ↙
6        3        5
↓      ↗        ↙
D ---1-→ E ---3-→ F

Current city: A
Favorite cities: [C, F]
```

## Solution 1: Dijkstra's Algorithm (Optimal)
```python
from heapq import heappush, heappop

def find_min_distance(graph, start, favorites):
    """
    Time: O(E log V) where E = edges, V = vertices (cities)
    Space: O(V) for distance dict and heap
    """
    # Initialize distances
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    
    # Priority queue [(distance, city)]
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr_city = heappop(pq)
        
        # Found a favorite city - this is minimum as we use priority queue
        if curr_city in favorites:
            return curr_dist
            
        # If we've found a larger distance to this city, skip
        if curr_dist > distances[curr_city]:
            continue
            
        # Check all neighbors
        for neighbor, weight in graph[curr_city].items():
            distance = curr_dist + weight
            
            # Found shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(pq, (distance, neighbor))
    
    return float('inf')  # No favorite city reachable

"""
Example walkthrough:
Start at A:
1. A -> B (dist=4)
2. A -> D (dist=6)
3. B -> C (dist=6) - Found favorite! Return 6
"""
```

## Follow-up Question
Find minimum distance needed to reach any favorite city while passing through a specific city en route.

### Why it's Tricky
1. Need to ensure path includes required city
2. Can't just run Dijkstra's once
3. Need to split into two subproblems

### Solution 2: Two-Phase Dijkstra's
```python
def find_min_distance_via_city(graph, start, required, favorites):
    """
    Time: O(2 * E log V) = O(E log V)
    Space: O(V)
    """
    # Phase 1: Find shortest path to required city
    dist_to_required = find_min_distance(graph, start, {required})
    if dist_to_required == float('inf'):
        return float('inf')
        
    # Phase 2: Find shortest path from required city to any favorite
    dist_to_favorite = find_min_distance(graph, required, favorites)
    if dist_to_favorite == float('inf'):
        return float('inf')
        
    return dist_to_required + dist_to_favorite

"""
Example:
Start: A, Required: E, Favorites: [C, F]

Phase 1: A to E
A → D → E (dist = 7)

Phase 2: E to favorite
E → F (dist = 3)

Total: 7 + 3 = 10
"""
```

## Visualizations for Different Cases
```
Case 1: Direct path exists
A --5-→ B --3-→ C
Required: B, Favorite: C
Result: 8 (5 + 3)

Case 2: Multiple paths
A --5-→ B --3-→ C
↘     ↗
  4  2
    ↘
      D
Required: B, Favorite: C
Result: 7 (4 + 2 + 3)

Case 3: No valid path
A --5-→ B     C
Required: D, Favorite: C
Result: Infinity
```

## Edge Cases to Consider
1. No path to required city
2. No path from required city to favorites
3. Required city is a favorite city
4. Cycles in graph
5. Multiple paths through required city
6. Start city is required city
7. Negative distances (not allowed in problem)

## Space-Time Complexity Analysis

### Original Problem (Single Dijkstra's)
- Time: O(E log V)
  - Each edge processed once
  - Priority queue operations: log V
- Space: O(V)
  - Distance dictionary
  - Priority queue

### Follow-up Problem (Two Dijkstra's)
- Time: O(E log V)
  - Two runs of Dijkstra's
  - Still O(E log V) as constant factor
- Space: O(V)
  - Same space requirements
  - Reuse space between runs

## Why Dijkstra's is Better than DFS
1. DFS might not find shortest path
2. DFS explores unnecessary paths
3. DFS time complexity could be O(V + E) but doesn't guarantee shortest path
4. Dijkstra's guarantees shortest path due to priority queue

## Testing Code
```python
def test_min_distance():
    # Test graph from example
    graph = {
        'A': {'B': 4, 'D': 6},
        'B': {'C': 2},
        'C': {},
        'D': {'E': 1},
        'E': {'F': 3},
        'F': {}
    }
    
    # Test cases
    assert find_min_distance(graph, 'A', {'C'}) == 6
    assert find_min_distance(graph, 'A', {'F'}) == 10
    assert find_min_distance_via_city(graph, 'A', 'E', {'F'}) == 10
```