"""
3625. Count Number of Trapezoids II (Hard)
Pattern: Computational Geometry + Hash Maps (Grouping) + Inclusion-Exclusion

--------------------------------------------------------------------------------
PROBLEM UNDERSTANDING
--------------------------------------------------------------------------------
Given N points, find the number of unique convex quadrilaterals with AT LEAST
one pair of parallel sides.

Input:  [[x,y], [x,y], ...]
Output: Integer count.

Constraints:
- N <= 500
- Points are distinct.

--------------------------------------------------------------------------------
CLARIFYING QUESTIONS
--------------------------------------------------------------------------------
1. "Is a parallelogram a trapezoid?"
   - Yes, the definition says "at least one pair of parallel sides".
2. "Do collinear points count?"
   - No, a trapezoid must be a convex quadrilateral. If 3 or 4 points are collinear,
     it's a triangle or line, not a quadrilateral.
3. "Are coordinates integers?"
   - Yes, so we can use GCD for exact slope representation (no floating point errors).

--------------------------------------------------------------------------------
APPROACH ANALYSIS
--------------------------------------------------------------------------------

BRUTE FORCE:
- Iterate all subsets of 4 points: O(N^4).
- With N=500, N^4 ≈ 62 billion operations. Too slow (TLE).

OPTIMAL APPROACH: O(N^2)
- Instead of picking 4 points, we pick PAIRS of points (Segments).
- A trapezoid is formed by two segments that are parallel and disjoint.

KEY INSIGHT 1: Grouping by Slope
- Iterate all pairs of points (segments).
- Calculate the slope for each segment.
- Group segments by slope.
- Any two segments in the same "slope bucket" are parallel candidates.

KEY INSIGHT 2: Handling Collinearity
- If two segments lie on the SAME infinite line, they don't form a quadrilateral.
- We must subtract these cases.
- We further group segments by "Line Constant" (Interception).

KEY INSIGHT 3: The Double Counting Problem (Inclusion-Exclusion)
- A "Pure Trapezoid" (exactly 1 parallel pair) is counted ONCE in our slope iteration.
- A "Parallelogram" (exactly 2 parallel pairs) is counted TWICE (once for the first
  pair of parallel sides, and again for the second pair).
- We want: Total = (Pure Trapezoids) + (Parallelograms)
- We have: Sum = (Pure Trapezoids) + 2 * (Parallelograms)
- Formula: Result = Sum - (Parallelograms)

--------------------------------------------------------------------------------
VISUALIZATION TRACE
--------------------------------------------------------------------------------
Points: A, B, C, D forming a Parallelogram.
Sides: AB || CD (Slope m1), AC || BD (Slope m2).

1. Slope Map Accumulation:
   - Bucket m1 contains: [Segment AB, Segment CD] -> 1 pair found.
   - Bucket m2 contains: [Segment AC, Segment BD] -> 1 pair found.
   - Total Slope Count = 2.

2. Vector Map (Parallelogram) Accumulation:
   - Vector AB is identical to Vector DC (same length & slope).
   - Bucket (dx, dy) contains: [AB, DC] -> 1 pair found.
   - Total Parallelogram Count = 1.

3. Final Calculation:
   - Result = SlopeCount - ParallelogramCount
   - Result = 2 - 1 = 1.
   - Correct! We found 1 unique shape.

--------------------------------------------------------------------------------
"""

import math
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        
        # 1. Data Structures
        # slope_map: slope -> (line_constant -> count of segments)
        # Used to count ALL parallel pairs (Trapezoids + 2*Parallelograms)
        slope_map = defaultdict(lambda: defaultdict(int))
        
        # vector_map: (dx, dy) -> count of segments
        # Used to count Parallelograms (same slope AND same length)
        vector_map = defaultdict(int)
        
        # 2. Iterate all unique pairs to populate maps
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                dx = x1 - x2
                dy = y1 - y2
                
                # --- A. Slope Logic (Direction Agnostic) ---
                # Normalize via GCD to get simplest form
                g = math.gcd(dx, dy)
                s_dx, s_dy = dx // g, dy // g
                
                # Canonical sign: Ensure x is positive, or y positive if x is 0
                if s_dx < 0 or (s_dx == 0 and s_dy < 0):
                    s_dx, s_dy = -s_dx, -s_dy
                
                slope_key = (s_dx, s_dy)
                
                # Line Constant: Ax + By = C
                # Cross product trick: s_dx * y - s_dy * x = Constant
                # Uniquely identifies the infinite line this segment sits on
                line_constant = s_dx * y1 - s_dy * x1
                
                slope_map[slope_key][line_constant] += 1
                
                # --- B. Vector Logic (Direction Specific Magnitude) ---
                # For parallelograms, length matters. (dx, dy) captures length.
                # However, segment P1->P2 is same as P2->P1.
                # Canonicalize vector direction for counting
                v_dx, v_dy = dx, dy
                if v_dx < 0 or (v_dx == 0 and v_dy < 0):
                    v_dx, v_dy = -v_dx, -v_dy
                
                vector_map[(v_dx, v_dy)] += 1

        total_parallel_pairs = 0
        
        # 3. Calculate Potential Trapezoids (Sum of Pairs per Slope)
        for slope, lines in slope_map.items():
            total_segments_on_slope = 0
            collinear_pairs = 0
            
            # Aggregate segments for this slope
            for count in lines.values():
                total_segments_on_slope += count
                # Pairs on the SAME line are collinear -> Invalid
                # nC2 = n * (n-1) / 2
                collinear_pairs += count * (count - 1) // 2
            
            # All pairs with this slope
            all_pairs = total_segments_on_slope * (total_segments_on_slope - 1) // 2
            
            # Add valid parallel pairs (disjoint lines)
            total_parallel_pairs += (all_pairs - collinear_pairs)

        # 4. Calculate Parallelograms (Sum of Pairs per Vector)
        parallelograms = 0
        for count in vector_map.values():
            # If segments have same vector (slope + length), they form a parallelogram
            parallelograms += count * (count - 1) // 2
            
        # 5. Apply Inclusion-Exclusion
        # Total Parallel Pairs = 1 * (Pure Trapezoids) + 2 * (Parallelograms)
        # We want: (Pure Trapezoids) + 1 * (Parallelograms)
        # So: Result = Total Parallel Pairs - Parallelograms
        return total_parallel_pairs - parallelograms

# ------------------------------------------------------------------------------
# TEST CASE
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    pts1 = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
    print(f"Input: {pts1}")
    print(f"Trapezoids: {sol.countTrapezoids(pts1)}") # Expected: 2
    
    # Example 2
    pts2 = [[0,0],[1,0],[0,1],[2,1]]
    print(f"\nInput: {pts2}")
    print(f"Trapezoids: {sol.countTrapezoids(pts2)}") # Expected: 1 (Parallelogram)
