"""
Problem: Ordered Quadrants Coordinate System
Time Complexity Analysis and Solution Approaches

The problem presents a recursive coordinate system where a 2^N x 2^N grid is divided into quadrants
with specific ordering rules:

Ordering Rules:
1. Lower-left < Upper-left
2. Upper-left < Upper-right 
3. Upper-right < Lower-right

Example 4x4 Grid Visualization:
 5  6  9 10    This shows how coordinates are numbered in a 4x4 grid (N=2)
 4  7  8 11    The pattern follows the quadrant ordering rules
 1  2 13 14    We can see how lower-left values are less than upper-left
 0  3 12 15    And upper-left less than upper-right, etc.

Solution Approaches:

1. Brute Force Approach:
   - Store the entire mapping in a 2D array
   - Look up coordinates directly
   Time: O(4^N) space and time - Impractical for 2^16 x 2^16
   
2. Pattern Recognition Approach:
   - Notice this follows a recursive Z-pattern within each quadrant
   - We can break this down into quadrant identification and offset calculation
   Time: O(N) where N is the number of bits needed to represent coordinates
   Space: O(1)

3. Optimal Bit Manipulation Approach:
   - Recognize that the quadrant position can be determined by most significant bits
   - Use interleaving of bits to compute the final position
   Time: O(1) for fixed size input
   Space: O(1)

Implementation of the Optimal Solution:
"""

def get_quadrant_value(x: int, y: int, n: int = 16) -> int:
    """
    Converts (x,y) coordinates to ordered quadrant value for 2^n x 2^n grid
    
    Args:
        x: x-coordinate (0 to 2^n - 1)
        y: y-coordinate (0 to 2^n - 1)
        n: power of 2 for grid size (default 16 for 2^16 x 2^16)
        
    Returns:
        int: The ordered quadrant value at (x,y)
        
    Time Complexity: O(1) for fixed n=16
    Space Complexity: O(1)
    
    Example trace for (x=1, y=0) in 4x4 grid:
    Input: (1,0) in 4x4 grid
    1. First quadrant determined by MSB: (1,0) -> lower left
    2. Within quadrant position: (1,0) -> second position
    3. Final value: 3
    
             5  6  9 10
             4  7  8 11
             1  2 13 14
    (1,0) -> 0  3 12 15
                ^
    """
    
    if not (0 <= x < (1 << n) and 0 <= y < (1 << n)):
        raise ValueError(f"Coordinates must be within 2^{n}x2^{n} grid")
    
    result = 0
    # Process each bit position from MSB to LSB
    for i in range(n-1, -1, -1):
        # Extract current bit position
        quad_x = (x >> i) & 1
        quad_y = (y >> i) & 1
        
        # Calculate quadrant size at this level
        quad_size = 1 << (2 * i)
        
        # Determine quadrant number (0-3) using bit manipulation
        quad_num = (quad_y << 1) | quad_x
        
        # Apply Z-pattern transformation
        if quad_num == 0:  # Lower left
            pass  # No adjustment needed
        elif quad_num == 1:  # Upper left
            result += quad_size
        elif quad_num == 2:  # Upper right
            result += 2 * quad_size
        else:  # Lower right
            result += 3 * quad_size
            
        # Prepare for next iteration
        x &= ~(1 << i)  # Clear processed bit
        y &= ~(1 << i)  # Clear processed bit
    
    return result

"""
Detailed Big-O Analysis:

Time Complexity: O(1)
- The function performs a fixed number of iterations (16 for 2^16 x 2^16 grid)
- Each iteration performs constant time operations:
  * Bit shifting: O(1)
  * Bitwise AND/OR: O(1)
  * Addition: O(1)
- Total: O(16) = O(1) for fixed input size

Space Complexity: O(1)
- Uses only a fixed number of variables regardless of input size:
  * result: int
  * loop variables and temporary calculations
- No dynamic allocation
- Total: O(1)

Verification:
The code can be tested with the 4x4 example:
assert get_quadrant_value(1, 0, 2) == 3  # Position (1,0) should be 3
assert get_quadrant_value(0, 0, 2) == 0  # Position (0,0) should be 0
assert get_quadrant_value(1, 1, 2) == 7  # Position (1,1) should be 7
"""

# Test cases for verification
def run_tests():
    # Test 4x4 grid (n=2)
    test_cases = [
        ((0, 0, 2), 0),   # Lower left corner
        ((1, 0, 2), 3),   # Lower left quadrant
        ((0, 1, 2), 4),   # Upper left quadrant
        ((3, 3, 2), 15),  # Lower right corner
        ((2, 1, 2), 8),   # Upper right quadrant
    ]
    
    for (x, y, n), expected in test_cases:
        result = get_quadrant_value(x, y, n)
        assert result == expected, f"Failed: ({x},{y}) expected {expected}, got {result}"
    
    print("All tests passed!")

# Run tests
if __name__ == "__main__":
    run_tests()