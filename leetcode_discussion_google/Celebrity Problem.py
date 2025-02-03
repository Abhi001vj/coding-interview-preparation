"""
Celebrity Problem

Key Insight:
Celebrity is a vertex with:
- in-degree = n-1 (everyone knows them)
- out-degree = 0 (they know no one)

Visual Example:
n = 3
M = [
    [0,1,0],  # Person 0 knows 1
    [0,0,0],  # Person 1 knows no one
    [0,1,0]   # Person 2 knows 1
]

Graph:
0 ----→ 1 ←---- 2
Person 1 is celebrity (everyone knows them, they know no one)
"""

def findCelebrity(n: int, M: List[List[int]]) -> int:
    """
    Solution using Stack Approach
    Time: O(n)
    Space: O(n) for stack
    
    Visual Process:
    1. Push all people to stack
    2. Keep comparing top 2 people
    3. Eliminate non-celebrity
    """
    def knows(a: int, b: int) -> bool:
        return M[a][b] == 1
    
    # Push all people to stack
    stack = list(range(n))
    
    # Eliminate until one potential celebrity remains
    while len(stack) >= 2:
        a = stack.pop()
        b = stack.pop()
        
        """
        Elimination Logic:
        - If A knows B: A can't be celebrity (push B back)
        - If A doesn't know B: B can't be celebrity (push A back)
        
        Example state for n=3:
        Initial stack: [0,1,2]
        Step 1: Compare 2,1
        - If 2 knows 1: keep 1
        - If 2 doesn't know 1: keep 2
        """
        if knows(a, b):
            stack.append(b)  # a knows b, a can't be celebrity
        else:
            stack.append(a)  # a doesn't know b, b can't be celebrity
            
    # Verify the candidate
    candidate = stack[0]
    
    """
    Verification requires:
    1. Row check: candidate knows no one (all 0s)
    2. Column check: everyone knows candidate (all 1s except diagonal)
    
    Example verification for candidate 1:
    Row: [0,0,0] ✓ (knows no one)
    Col: [1,0,1] ✓ (everyone except self knows them)
    """
    
    # Check row (celebrity should know no one)
    for j in range(n):
        if candidate != j and knows(candidate, j):
            return -1
            
    # Check column (everyone should know celebrity)
    for i in range(n):
        if candidate != i and not knows(i, candidate):
            return -1
            
    return candidate

def findCelebrityOptimal(n: int, M: List[List[int]]) -> int:
    """
    Two Pointer Approach (More Space Efficient)
    Time: O(n)
    Space: O(1)
    
    Visual Process:
    Use two pointers to eliminate non-celebrities
    """
    def knows(a: int, b: int) -> bool:
        return M[a][b] == 1
    
    candidate = 0
    
    # Find potential candidate
    for i in range(1, n):
        """
        Compare current candidate with i
        Example for i=1:
        - If candidate knows 1: 1 becomes new candidate
        - If candidate doesn't know 1: keep current candidate
        """
        if knows(candidate, i):
            candidate = i
            
    # Verify candidate
    for i in range(n):
        if candidate != i:
            if knows(candidate, i) or not knows(i, candidate):
                return -1
                
    return candidate

def test_celebrity():
    """
    Test Cases:
    1. Basic case with celebrity
    2. No celebrity
    3. Multiple potential celebrities
    4. Single person
    """
    test_cases = [
        # Basic case with celebrity
        {
            'n': 3,
            'M': [
                [0,1,0],
                [0,0,0],
                [0,1,0]
            ],
            'expected': 1
        },
        # No celebrity
        {
            'n': 3,
            'M': [
                [0,1,0],
                [1,0,0],
                [0,1,0]
            ],
            'expected': -1
        },
        # Single person
        {
            'n': 1,
            'M': [[0]],
            'expected': 0
        }
    ]
    
    for tc in test_cases:
        result = findCelebrity(tc['n'], tc['M'])
        assert result == tc['expected'], f"Expected {tc['expected']}, got {result}"
        
        result = findCelebrityOptimal(tc['n'], tc['M'])
        assert result == tc['expected'], f"Expected {tc['expected']}, got {result}"

"""
Edge Cases:
1. n = 1 (single person)
2. No celebrity exists
3. Multiple people with no outgoing edges
4. All know each other
5. No one knows anyone

Time Complexity Analysis:
1. Stack Approach:
   - Push to stack: O(n)
   - Pop and compare: O(n)
   - Verification: O(n)
   Total: O(n)

2. Two Pointer Approach:
   - Find candidate: O(n)
   - Verify candidate: O(n)
   Total: O(n)

Space Complexity:
1. Stack: O(n)
2. Two Pointer: O(1)

Key Insights:
1. Celebrity must have in-degree = n-1
2. Celebrity must have out-degree = 0
3. Can eliminate non-celebrities efficiently
4. Need final verification of candidate
"""