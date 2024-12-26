# https://leetcode.com/problems/maximum-score-from-removing-substrings/description/
# 1717. Maximum Score From Removing Substrings
# Medium
# Topics
# Companies
# Hint
# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

 

# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
 

# Constraints:

# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s consists of lowercase English letters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 138.3K
# Submissions
# 220K
# Acceptance Rate
# 62.8%
# Topics
# Companies
# 0 - 6 months
# Google
# 3
# 6 months ago
# Bloomberg
# 5
# Hint 1
# Note that it is always more optimal to take one type of substring before another
# Hint 2
# You can use a stack to handle erasures
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, points):
            stack = []
            score = 0
            for char in s:
                if stack and char == second and stack[-1] == first:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return "".join(stack), score
        
        total_score = 0

        if x > y:
            s, score1 = remove_substring(s, 'a', 'b', x)
            s, score2 = remove_substring(s, 'b', 'a', y)
        else:
            s, score1 = remove_substring(s, 'b', 'a', y)
            s, score2 = remove_substring(s, 'a', 'b', x)
        
        return score1 + score2 
    
class Solution:
    """
    Greedy Approach Analysis:
    ------------------------
    Key Insight: Always remove the higher-scoring pattern first!
    
    Why Greedy Works:
    1. If x > y (points for 'ab' > points for 'ba'):
       - Removing 'ab' first never blocks more valuable future removals
       - Any 'ba' that could be formed after removing 'ab' could have been formed before
       
    2. If y > x (points for 'ba' > points for 'ab'):
       - Same logic applies in reverse
       
    Visual Example:
    --------------
    s = "cdbcbbaaabab", x = 4 (for 'ab'), y = 5 (for 'ba')
    
    Since y > x, we remove 'ba' first:
    
    Original:    c d b c b b a a a b a b
                     ^   ^ first 'ba' found (+5)
    After 1st:   c d b c b a a a b a b
                         ^ ^ second 'ba' found (+5)
    After 2nd:   c d b c b a a b a b
                           ^ ^ third 'ba' found (+5)
    After 3rd:   c d b c b a b a b
                             ^ ^ fourth 'ba' found (+5)
    Final:       c d b c b
    
    Total score = 5 + 5 + 5 + 4 = 19
    """
    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Greedy solution using single pass approach
        Time: O(n)  - one pass through string for each pattern
        Space: O(n) - for storing modified string
        """
        def remove_pattern(s: str, p1: str, p2: str, points: int) -> tuple[str, int]:
            # Initialize result string builder and score
            result = []
            score = 0
            
            # Process each character
            for c in s:
                # If we can make the pattern with current char
                if result and result[-1] == p1 and c == p2:
                    result.pop()  # Remove p1
                    score += points  # Add points
                else:
                    result.append(c)  # Add current char to result
                    
            return ''.join(result), score
        
        # First pass - remove pattern with higher points
        if x > y:
            # Remove 'ab' first if it gives more points
            remaining, score1 = remove_pattern(s, 'a', 'b', x)
            # Then remove 'ba'
            _, score2 = remove_pattern(remaining, 'b', 'a', y)
        else:
            # Remove 'ba' first if it gives more points (or equal)
            remaining, score1 = remove_pattern(s, 'b', 'a', y)
            # Then remove 'ab'
            _, score2 = remove_pattern(remaining, 'a', 'b', x)
            
        return score1 + score2

    def maximumGain_verbose(self, s: str, x: int, y: int) -> int:
        """
        Verbose version with step-by-step visualization
        """
        def remove_pattern_with_viz(s: str, p1: str, p2: str, points: int) -> tuple[str, int]:
            result = []
            score = 0
            print(f"\nRemoving pattern '{p1}{p2}' for {points} points each:")
            print(f"Initial: {' '.join(s)}")
            
            for i, c in enumerate(s):
                if result and result[-1] == p1 and c == p2:
                    print(f"Found {p1}{p2} at position {i-1},{i}")
                    result.pop()
                    score += points
                    print(f"After removal: {' '.join(''.join(result) + s[i+1:])}")
                else:
                    result.append(c)
                    
            print(f"Score from this pass: {score}")
            return ''.join(result), score
        
        print(f"\nProcessing string: {s}")
        print(f"Points: {x} for 'ab', {y} for 'ba'")
        
        if x > y:
            print("\nStrategy: Removing 'ab' first (higher points)")
            remaining, score1 = remove_pattern_with_viz(s, 'a', 'b', x)
            _, score2 = remove_pattern_with_viz(remaining, 'b', 'a', y)
        else:
            print("\nStrategy: Removing 'ba' first (higher points)")
            remaining, score1 = remove_pattern_with_viz(s, 'b', 'a', y)
            _, score2 = remove_pattern_with_viz(remaining, 'a', 'b', x)
            
        total = score1 + score2
        print(f"\nTotal score: {total}")
        return total

# Example usage:
"""
s = "cdbcbbaaabab"
solution = Solution()

# Regular version
print(solution.maximumGain(s, 4, 5))  # 19

# Verbose version with visualization
solution.maximumGain_verbose(s, 4, 5)
# Output will show step-by-step process:
# Processing string: cdbcbbaaabab
# Points: 4 for 'ab', 5 for 'ba'
# 
# Strategy: Removing 'ba' first (higher points)
# Removing pattern 'ba' for 5 points each:
# Initial: c d b c b b a a a b a b
# Found ba at position 5,6
# After removal: c d b c b a a a b a b
# Found ba at position 7,8
# After removal: c d b c b a a b a b
# ...and so on
"""
class Solution:
    """
    Problem: Maximum Score From Removing Substrings
    ---------------------------------------------
    Given: 
    - String s
    - Two integers x and y
    - Can remove "ab" for x points or "ba" for y points
    - Need to maximize total points
    
    Three Solution Approaches:
    1. Stack-based (Optimal)
    2. String Simulation
    3. Recursive (Brute Force)
    
    Example String: s = "cdbcbbaaabab", x = 4, y = 5
    
    Visual Process for Stack Solution:
    --------------------------------
    Since y > x, process "ba" first:
    
    Initial: c d b c b b a a a b a b
    Step 1:  c d[b c]b b a a a b a b  Remove 'bc' -> stack
    Step 2:  c d b c b[b a]a a b a b  Remove 'ba' -> +5 points
    Step 3:  c d b c b a[a a]b a b    Keep 'aa'
    Step 4:  c d b c b a a a[b a]b    Remove 'ba' -> +5 points
    Step 5:  c d b c b a a a b[a b]   Remove last 'ab' -> +4 points
    
    Visual Process for String Simulation:
    -----------------------------------
    Initial:     "cdbcbbaaabab"
    First 'ba':  "cdbcb|aa|abab"    -> "cdbcbaabab"     +5
    Second 'ba': "cdbcb|aa|bab"     -> "cdbcbaab"       +5
    Third 'ba':  "cdbcb|aa|b"       -> "cdbcba"         +5
    Fourth 'ab': "cdbcb|a|"         -> "cdbc"           +4
    Final score: 19
    
    Visual Process for Recursive:
    ---------------------------
    Tree visualization of choices:
                    cdbcbbaaabab
                    /           \
        remove 'ba'             remove 'ab'
        cdbcbaabab              cdbcbbaaab
           /    \                /        \
      remove 'ba' remove 'ab'  remove 'ba' remove 'ab'
         ...        ...           ...        ...
    """
    
    def maximumGain_stack(self, s: str, x: int, y: int) -> int:
        """
        Solution 1: Stack-based (Optimal)
        Time: O(n)
        Space: O(n)
        
        Process:
        1. Use stack to track characters
        2. When matching pair found, pop and add points
        3. Process higher value substring first
        """
        def process_substring(s: str, first: str, second: str, points: int) -> tuple[str, int]:
            stack = []
            score = 0
            
            for char in s:
                # If stack has matching pair, remove it and add points
                if stack and char == second and stack[-1] == first:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            
            return ''.join(stack), score
        
        # Process higher value substring first
        total_score = 0
        if x > y:
            # Remove 'ab' first
            s, score1 = process_substring(s, 'a', 'b', x)
            s, score2 = process_substring(s, 'b', 'a', y)
        else:
            # Remove 'ba' first
            s, score1 = process_substring(s, 'b', 'a', y)
            s, score2 = process_substring(s, 'a', 'b', x)
            
        return score1 + score2

    def maximumGain_simulation(self, s: str, x: int, y: int) -> int:
        """
        Solution 2: String Simulation
        Time: O(n²)
        Space: O(n)
        
        Process:
        1. Find first occurrence of target substring
        2. Remove it and add points
        3. Continue until no more substrings found
        4. Repeat for second substring type
        """
        def remove_all(s: str, pattern: str, points: int) -> tuple[str, int]:
            score = 0
            while True:
                idx = s.find(pattern)
                if idx == -1:
                    break
                s = s[:idx] + s[idx + 2:]  # Remove pattern
                score += points
            return s, score
        
        total_score = 0
        if x > y:
            # Process 'ab' first
            s, score1 = remove_all(s, 'ab', x)
            s, score2 = remove_all(s, 'ba', y)
        else:
            # Process 'ba' first
            s, score1 = remove_all(s, 'ba', y)
            s, score2 = remove_all(s, 'ab', x)
            
        return score1 + score2

    def maximumGain_recursive(self, s: str, x: int, y: int) -> int:
        """
        Solution 3: Recursive (Brute Force)
        Time: O(2^n)
        Space: O(n) - recursion stack
        
        Process:
        1. At each step, try removing either 'ab' or 'ba'
        2. Recursively calculate score for each choice
        3. Take maximum of all possible paths
        """
        def recursive_remove(s: str) -> int:
            if len(s) < 2:  # Base case
                return 0
            
            # Try removing 'ab'
            max_score = 0
            idx_ab = s.find('ab')
            if idx_ab != -1:
                # Score from removing 'ab' + score from rest of string
                score_ab = x + recursive_remove(s[:idx_ab] + s[idx_ab + 2:])
                max_score = max(max_score, score_ab)
            
            # Try removing 'ba'
            idx_ba = s.find('ba')
            if idx_ba != -1:
                # Score from removing 'ba' + score from rest of string
                score_ba = y + recursive_remove(s[:idx_ba] + s[idx_ba + 2:])
                max_score = max(max_score, score_ba)
            
            return max_score
        
        return recursive_remove(s)

    """
    Comparison of Solutions:
    ----------------------
    1. Stack-based:
       - Most efficient: O(n) time
       - Clean implementation
       - Best for interviews
       
    2. String Simulation:
       - Intuitive approach
       - O(n²) time due to string operations
       - Good for small strings
       
    3. Recursive:
       - Explores all possibilities
       - Exponential time O(2^n)
       - Good for understanding problem
       - Not practical for large strings
       
    Example Usage:
    -------------
    s = "cdbcbbaaabab"
    x = 4  # points for removing "ab"
    y = 5  # points for removing "ba"
    
    solution = Solution()
    print(solution.maximumGain_stack(s, x, y))  # 19
    print(solution.maximumGain_simulation(s, x, y))  # 19
    print(solution.maximumGain_recursive(s, x, y))  # 19
    """