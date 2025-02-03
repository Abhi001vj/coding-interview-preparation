"""
Problem: Count Distinct Island Shapes
Part 1: Without rotations/mirrors (Basic)
Part 2: With rotations/mirrors (Advanced)

Example Grid:
[ 1, 1, 1, 1, 0, 0]
[ 1, 1, 0, 0, 0, 1]
[ 0, 0, 1, 1, 0, 1]
[ 1, 1, 0, 0, 0, 0]
[ 0, 0, 1, 1, 1, 1]
[ 1, 0, 1, 1, 0, 0]

Visualization of shapes:
Shape1 (6-cell):     Shape2 (6-cell):     Shape3 (2-cell):    Shape4 (1-cell):
# # # #              # #                   # #                 #
# #                  # #
                     # #
"""

from typing import List, Set, Tuple
from collections import defaultdict

class IslandCounter:
    def __init__(self):
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
    def count_distinct_islands(self, grid: List[List[int]]) -> int:
        """
        Count distinct island shapes without considering rotations/mirrors
        Time: O(R*C), Space: O(R*C) where R=rows, C=columns
        
        Strategy:
        1. For each island, collect coordinates relative to start point
        2. Use these relative coordinates as shape signature
        3. Store unique signatures in a set
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visited = set()
        distinct_shapes = set()
        
        def collect_shape(r: int, c: int, start_r: int, start_c: int) -> List[Tuple[int, int]]:
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] == 0 or (r, c) in visited):
                return []
                
            visited.add((r, c))
            shape = [(r - start_r, c - start_c)]  # coordinates relative to start
            
            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                shape.extend(collect_shape(nr, nc, start_r, start_c))
                
            return shape
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    shape = collect_shape(r, c, r, c)
                    distinct_shapes.add(tuple(sorted(shape)))  # sort for canonical form
                    
        return len(distinct_shapes)
        
    def count_distinct_islands_with_rotation(self, grid: List[List[int]]) -> int:
        """
        Count distinct island shapes considering all rotations and mirrors
        Time: O(R*C * log(S)) where S is max size of an island
        Space: O(R*C)
        
        Normalization Strategy:
        1. Collect all points in the island
        2. Generate all 8 transformations (4 rotations * 2 mirrors)
        3. Normalize by:
           - Translating to origin (0,0)
           - Sorting points lexicographically
           - Using the lexicographically smallest version as canonical form
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visited = set()
        distinct_shapes = set()
        
        def collect_points(r: int, c: int) -> List[Tuple[int, int]]:
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] == 0 or (r, c) in visited):
                return []
                
            visited.add((r, c))
            points = [(r, c)]
            
            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                points.extend(collect_points(nr, nc))
                
            return points
            
        def normalize_shape(points: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], ...]:
            """
            Normalize shape by trying all transformations and selecting the canonical form
            """
            def get_transformations(point: Tuple[int, int]) -> List[Tuple[int, int]]:
                x, y = point
                # All 8 possible transformations (4 rotations * 2 mirrors)
                return [
                    (x, y),   # original
                    (-x, y),  # mirror horizontally
                    (x, -y),  # mirror vertically
                    (-x, -y), # mirror both
                    (y, x),   # rotate 90° + variants
                    (-y, x),
                    (y, -x),
                    (-y, -x)
                ]
            
            canonical_form = None
            
            # Try each transformation
            for i in range(8):
                transformed = []
                for point in points:
                    x, y = get_transformations(point)[i]
                    transformed.append((x, y))
                
                # Normalize to origin
                min_x = min(x for x, _ in transformed)
                min_y = min(y for _, y in transformed)
                normalized = [(x - min_x, y - min_y) for x, y in transformed]
                normalized.sort()  # Sort for canonical form
                
                if canonical_form is None or tuple(normalized) < canonical_form:
                    canonical_form = tuple(normalized)
            
            return canonical_form
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    points = collect_points(r, c)
                    canonical_shape = normalize_shape(points)
                    distinct_shapes.add(canonical_shape)
                    
        return len(distinct_shapes)

# Test the implementation
def test_island_counter():
    grid = [
        [1, 1, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0]
    ]
    
    counter = IslandCounter()
    
    # Test Part 1: Without rotations
    result1 = counter.count_distinct_islands(grid)
    assert result1 == 4, f"Expected 4 distinct shapes without rotation, got {result1}"
    
    # Test Part 2: With rotations
    result2 = counter.count_distinct_islands_with_rotation(grid)
    assert result2 == 3, f"Expected 3 distinct shapes with rotation, got {result2}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_island_counter()

"""
Key Insights for Shape Normalization:

1. Without Rotations/Mirrors:
   - Simply use relative coordinates from start point
   - Sort coordinates for canonical form
   - Time: O(N) where N is total cells

2. With Rotations/Mirrors:
   - Generate all 8 possible transformations
   - Normalize each to origin (0,0)
   - Sort points lexicographically
   - Use lexicographically smallest as canonical
   - Time: O(N*log(N)) due to sorting

The normalization approach avoids having to:
- Store all rotations/mirrors
- Compare shapes pairwise
- Handle floating-point precision issues

Example of how normalization works:
Original shape:      After normalizing to origin:
  #                    #
# # #      -->      # # #
  #                    #
All 8 transformations will normalize to this same canonical form.
"""

# Step 1: Basic Island Detection using DFS Template
"""
First, let's use the basic DFS pattern from the template to detect a single island:

Grid Example:
1 1 1 1 0 0
1 1 0 0 0 1
0 0 1 1 0 1

Step 1.1: Basic Island Detection
"""

def detect_island(grid, row, col, visited):
    # Base cases from template
    if (row < 0 or row >= len(grid) or 
        col < 0 or col >= len(grid[0]) or 
        grid[row][col] == 0 or 
        (row, col) in visited):
        return []
    
    visited.add((row, col))
    
    # Using delta pattern from template for 4-directional movement
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    island = [(row, col)]
    
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        island.extend(detect_island(grid, new_row, new_col, visited))
    
    return island

# Step 2: Shape Recognition without Rotation
"""
Now we need to identify unique shapes. Key insight: 
- Convert absolute coordinates to relative coordinates
- Use starting point of each island as reference (0,0)

Grid Example showing same shape at different positions:
1 1    0 0
1 0    1 1
"""

def get_island_shape(grid, row, col, visited):
    if (row < 0 or row >= len(grid) or 
        col < 0 or col >= len(grid[0]) or 
        grid[row][col] == 0 or 
        (row, col) in visited):
        return []
    
    visited.add((row, col))
    # Key change: Store coordinates relative to start point
    shape = [(0, 0)]  # Starting point becomes origin
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        # Convert child coordinates to relative position
        child_points = get_island_shape(grid, new_row, new_col, visited)
        for child_r, child_c in child_points:
            shape.append((child_r + dx, child_c + dy))
    
    return shape

# Step 3: Final Solution without Rotation
def count_distinct_islands(grid):
    if not grid or not grid[0]:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    visited = set()
    distinct_shapes = set()
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                # Get shape and convert to tuple for set storage
                shape = tuple(sorted(get_island_shape(grid, r, c, visited)))
                distinct_shapes.add(shape)
    
    return len(distinct_shapes)

# Step 4: Adding Rotation Support
"""
Key insight for handling rotations:
Instead of comparing all rotations, normalize each shape by:
1. Finding all possible rotations/reflections
2. Converting to origin coordinates
3. Taking lexicographically smallest version as canonical form
"""

def normalize_shape(points):
    def get_rotations(x, y):
        # All 8 possible transformations (4 rotations × 2 reflections)
        return [
            (x, y),   # original
            (-x, y),  # flip horizontal
            (x, -y),  # flip vertical
            (-x, -y), # both flips
            (y, x),   # 90° rotation and variants
            (-y, x),
            (y, -x),
            (-y, -x)
        ]
    
    canonical = None
    # Try all transformations
    for i in range(8):
        transformed = []
        for x, y in points:
            transformed.append(get_rotations(x, y)[i])
        
        # Normalize to origin
        if transformed:
            min_x = min(x for x, _ in transformed)
            min_y = min(y for _, y in transformed)
            normalized = [(x - min_x, y - min_y) for x, y in transformed]
            normalized.sort()
            
            if canonical is None or tuple(normalized) < canonical:
                canonical = tuple(normalized)
    
    return canonical

# Final Solution with Rotation Support
def count_distinct_islands_with_rotation(grid):
    if not grid or not grid[0]:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    visited = set()
    distinct_shapes = set()
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                shape = get_island_shape(grid, r, c, visited)
                # Normalize shape considering rotations
                canonical_shape = normalize_shape(shape)
                distinct_shapes.add(canonical_shape)
    
    return len(distinct_shapes)

"""
Key Changes from Original DFS Template:
1. Added shape tracking using relative coordinates
2. Added normalization step for rotation handling
3. Modified return values to track shapes instead of just counts

Constraints and Their Impact:
1. Original: Just count islands
   - Basic DFS template sufficient
2. Added: Identify unique shapes
   - Need relative coordinate system
3. Added: Handle rotations
   - Need shape normalization
   - Added transformation matrices

Each constraint led to a specific modification of the base DFS pattern
while maintaining the core traversal logic.
"""