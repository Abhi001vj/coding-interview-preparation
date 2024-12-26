# 6. Zigzag Conversion
# Medium
# Topics
# Companies
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        i = 0
        d = i
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)
            if i == 0:
                d =1
            elif i == numRows - 1:
                d = -1
            i += d

        ret = ''
        for i in range(numRows):
            ret += ''.join(rows[i])
        
        return ret
    

```python
"""
Zigzag String Conversion - Detailed Analysis
=========================================

Understanding the Pattern:
Let's visualize how "PAYPALISHIRING" is written in zigzag with 3 rows:

P   A   H   N  <- Row 0: Chars at positions 0, 4, 8, 12
A P L S I I G  <- Row 1: Chars at positions 1,3, 5,7, 9,11, 13
Y   I   R      <- Row 2: Chars at positions 2, 6, 10

Pattern Recognition:
1. Each complete zigzag cycle spans 2*(numRows-1) characters
2. For first and last rows: chars appear at fixed intervals
3. For middle rows: chars appear in pairs (down-stroke & up-stroke)

Let's solve this step by step.
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert string to zigzag pattern and read line by line.
        
        Approach: Use string builders for each row.
        Time Complexity: O(n) where n is length of string
        Space Complexity: O(n) for storing result
        
        Visual Example for s="PAYPALISHIRING", numRows=3:
        Iteration:  0123456789012
        String:     PAYPALISHIRING
        Pattern:    
        Row 0:     P   A   H   N
        Row 1:     A P L S I I G
        Row 2:     Y   I   R    
        
        Cycle length = 2*(numRows-1) = 4
        """
        # Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize array of strings for each row
        rows = [''] * numRows
        
        # Variables to track current position
        current_row = 0
        step = 1  # 1 for moving down, -1 for moving up
        
        """
        Visualization of movement:
        Step = 1 (down):  Step = -1 (up):
        P                 A P
        A                 Y
        Y
        
        Complete cycle example:
        P     (down)
        A     (down)
        Y     (up)
        P     (up)
        A     (down)
        ...
        """
        
        # Process each character in string
        for char in s:
            # Add current character to its row
            rows[current_row] += char
            
            # Change direction if we hit top or bottom row
            if current_row == 0:
                step = 1  # start moving down
            elif current_row == numRows - 1:
                step = -1  # start moving up
                
            # Move to next row
            current_row += step
        
        # Combine all rows into final result
        return ''.join(rows)

    def convert_cycle_method(self, s: str, numRows: int) -> str:
        """
        Alternative approach using cycle length calculation.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Pattern Analysis for numRows = 4:
        P     I    N  <- Row 0: Chars at positions 0, 6, 12
        A   L S  I G  <- Row 1: Chars at positions 1, 5, 7, 11, 13
        Y A   H R     <- Row 2: Chars at positions 2, 4, 8, 10
        P     I       <- Row 3: Chars at positions 3, 9
        
        Cycle length = 2*(numRows-1) = 6
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = []
        cycle_len = 2 * (numRows - 1)
        
        # Process each row
        for row in range(numRows):
            for i in range(row, len(s), cycle_len):
                # Add the main character in the current row
                result.append(s[i])
                
                # For middle rows, add the character in the upward stroke
                if row > 0 and row < numRows - 1:
                    up_stroke_idx = i + cycle_len - 2 * row
                    if up_stroke_idx < len(s):
                        result.append(s[up_stroke_idx])
        
        return ''.join(result)

def demonstrate_solutions():
    """
    Demonstrate and test both approaches with examples.
    """
    test_cases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("AB", 1, "AB")
    ]
    
    solution = Solution()
    
    for s, numRows, expected in test_cases:
        print(f"\nTest Case: s = {s}, numRows = {numRows}")
        print("Expected:", expected)
        
        # Test both approaches
        result1 = solution.convert(s, numRows)
        result2 = solution.convert_cycle_method(s, numRows)
        
        print("Row Builder Result:", result1)
        print("Cycle Method Result:", result2)
        
        # Visualize the zigzag pattern
        print("\nZigzag Pattern:")
        visualize_zigzag(s, numRows)

def visualize_zigzag(s: str, numRows: int):
    """
    Helper function to visualize the zigzag pattern.
    """
    if numRows == 1:
        print(s)
        return
        
    # Create empty matrix
    cycle_len = 2 * (numRows - 1)
    n_cycles = (len(s) + cycle_len - 1) // cycle_len
    width = n_cycles * (numRows - 1)
    matrix = [[' ' for _ in range(width)] for _ in range(numRows)]
    
    # Fill matrix
    col = 0
    curr_row = 0
    going_down = True
    
    for char in s:
        matrix[curr_row][col] = char
        
        if going_down:
            if curr_row == numRows - 1:
                going_down = False
                curr_row -= 1
                col += 1
            else:
                curr_row += 1
        else:
            if curr_row == 0:
                going_down = True
                curr_row += 1
            else:
                curr_row -= 1
                col += 1
    
    # Print matrix
    for row in matrix:
        print(''.join(row))

if __name__ == "__main__":
    demonstrate_solutions()

"""
Key Insights and Patterns:
------------------------
1. Pattern Recognition:
   - Zigzag follows a predictable cycle
   - Each cycle length is 2*(numRows-1)
   - First/last rows have regular spacing
   - Middle rows have two characters per cycle

2. Implementation Approaches:
   - Row-by-row string building
   - Cycle-based calculation
   - Matrix visualization
   
3. Edge Cases:
   - numRows = 1
   - String length < numRows
   - Empty string
   - Single character
   
4. Optimization Techniques:
   - Avoid creating actual matrix
   - Use string builders
   - Calculate positions directly
   - Early termination for edge cases
"""
```

I've provided two different approaches to solve this problem:

1. **Row Builder Approach**:
   - Builds strings row by row
   - Simulates actual movement in zigzag pattern
   - More intuitive to understand
   - Good for explaining in interviews

2. **Cycle Method Approach**:
   - Uses mathematical pattern of character positions
   - More efficient for implementation
   - Requires understanding of the cycle pattern
   - Better for production code

The visualization helper function helps to understand how the pattern works and can be valuable during interviews to demonstrate understanding.

Would you like me to explain any specific part in more detail?