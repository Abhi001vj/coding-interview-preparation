"""
PROBLEM ANALYSIS:
----------------
1. Game Characteristics:
   - 2 player alternating moves (like chess/tic-tac-toe)
   - Perfect information game
   - Finite states
   - No cycles (stacks only grow)
   → This suggests Minimax/Game Theory approach

2. State Space Analysis:
   Initial State:
   12 stacks of height 1 (3 tiles each of 4 colors)
   [W][W][W][G][G][G][R][R][R][B][B][B]

   Valid Moves:
   a) Same height stacks can combine
   b) Same top color stacks can combine
   
   Visualization of sample moves:
   [W][W][G][G]
      ↙     ↘
   [W][G]   [W][G]
   [W]      [G]

3. Key Insights:
   - Game must end (stacks can only combine/grow)
   - Can represent as game tree
   - Winning states: when no valid moves left
   - Perfect play = each player makes optimal move

SOLUTION APPROACH:
----------------
1. Use Game Tree + Minimax:
   - Each node = game state
   - Edges = valid moves
   - Leaf nodes = game over states
   - Minimax determines optimal play

2. State Representation:
   - Need efficient way to track:
     * Stack heights
     * Top colors
     * Current player's turn
"""

from collections import Counter, defaultdict
from typing import List, Tuple

def can_combine(stack1: Tuple[int, str], stack2: Tuple[int, str]) -> bool:
    """
    Determines if two stacks can be combined.
    Each stack is (height, top_color)
    
    Example:
    (1,'W'), (1,'G') -> True (same height)
    (2,'W'), (1,'W') -> True (same color)
    (2,'W'), (1,'G') -> False
    """
    height1, color1 = stack1
    height2, color2 = stack2
    return height1 == height2 or color1 == color2

def get_state_key(stacks: List[Tuple[int, str]]) -> tuple:
    """
    Creates hashable state representation.
    Sorts stacks to ensure same state has same key.
    
    Example:
    [(1,'W'),(2,'G')] -> ((1,'W'),(2,'G'))
    """
    return tuple(sorted(stacks))

def get_next_states(stacks: List[Tuple[int, str]]) -> List[List[Tuple[int, str]]]:
    """
    Generates all possible next states from current state.
    
    Example:
    [(1,'W'),(1,'W'),(1,'G')]
    →
    [[(2,'W'),(1,'G')],    # Combined W+W
     [(1,'W'),(2,'G')]]    # Combined W+G
    """
    next_states = []
    n = len(stacks)
    
    for i in range(n):
        for j in range(i + 1, n):
            if can_combine(stacks[i], stacks[j]):
                # Create new state with combined stacks
                new_state = []
                for k in range(n):
                    if k != i and k != j:
                        new_state.append(stacks[k])
                # Add combined stack
                new_height = stacks[i][0] + stacks[j][0]
                new_color = stacks[j][1]  # Top stack's color
                new_state.append((new_height, new_color))
                next_states.append(new_state)
    
    return next_states

def solve_game(stacks: List[Tuple[int, str]], memo={}) -> bool:
    """
    Returns True if current player wins with perfect play.
    Uses minimax with memoization.
    
    Time: O(number of unique states * branching factor)
    Space: O(number of unique states)
    
    Example trace for simple state:
    [W,W,G]
    Player 1's turn:
    - Can combine W+W → [WW,G] → Player 2 has no moves → Player 1 wins
    - Can combine W+G → [WG,W] → Player 2 can move → Keep exploring
    """
    state_key = get_state_key(stacks)
    
    if state_key in memo:
        return memo[state_key]
    
    # Get all possible next states
    next_states = get_next_states(stacks)
    
    # No moves left = current player loses
    if not next_states:
        memo[state_key] = False
        return False
        
    # Try each move, if any lead to win, current player wins
    for next_state in next_states:
        # If opponent loses after our move, we win
        if not solve_game(next_state, memo):
            memo[state_key] = True
            return True
            
    # If all moves lead to opponent winning, we lose
    memo[state_key] = False
    return False

def main():
    """
    Setup initial game state and determine winner
    """
    # Initial state: 3 tiles each of 4 colors
    initial_stacks = [(1,'W'), (1,'W'), (1,'W'),
                     (1,'G'), (1,'G'), (1,'G'),
                     (1,'R'), (1,'R'), (1,'R'),
                     (1,'B'), (1,'B'), (1,'B')]
    
    # Solve game
    player1_wins = solve_game(initial_stacks)
    print(f"With perfect play, {'Player 1' if player1_wins else 'Player 2'} wins")


"""
ME: Let me first confirm my understanding of the problem:
- 12 tiles: 3 each of 4 colors
- Players take turns combining stacks
- Can combine if: same height OR same top color
- Lose if no valid moves on your turn
Is this correct?

INTERVIEWER: Yes, that's correct.

ME: Before I start coding, could we work through a small example to ensure
I understand the mechanics? Maybe with just 4 tiles: [W,W,G,G]?

INTERVIEWER: Good idea, let's do that.

ME: Great! Let's trace this:
[W][W][G][G] -> Player 1's turn
Possible moves:
1. Combine W+W: [WW][G][G]
2. Combine W+G: [WG][W][G]
3. Combine G+G: [W][W][GG]

Would you like me to continue with one of these paths?

INTERVIEWER: Yes, show me what happens after W+W.

ME: After W+W:
[WW][G][G] -> Player 2's turn
Only possible move is G+G (same height/color)
[WW][GG] -> Player 1's turn
No valid moves (different heights, different colors)
Therefore Player 2 wins!

Let me write some test cases to verify my understanding:
"""

def test_babylon_game():
    """
    Test cases to verify game mechanics
    """
    # Test 1: Simple 4-tile game we just discussed
    test1 = [(1,'W'), (1,'W'), (1,'G'), (1,'G')]
    print("\nTest 1: Simple 4-tile game")
    print_game_state(test1)
    result = solve_game(test1)
    print(f"Player 1 {'wins' if result else 'loses'}")
    
    # Test 2: Edge case - just 2 tiles
    test2 = [(1,'W'), (1,'G')]
    print("\nTest 2: Two tiles")
    print_game_state(test2)
    result = solve_game(test2)
    print(f"Player 1 {'wins' if result else 'loses'}")
    
    # Test 3: Let's get interviewer's input
    print("\nWhat other test cases should we consider?")

def print_game_state(stacks):
    """
    Visualize game state for easier debugging
    """
    print("Current state:")
    for height, color in stacks:
        print(f"[{''.join(color * height)}]", end=" ")
    print()

"""
ME: I've implemented some basic test cases. Before running the full 12-tile
game, would you like me to add any specific test scenarios? Also:

1. Should we validate inputs? (e.g., exactly 3 tiles per color)
2. Should we handle invalid moves or assume valid input?
3. For the 12-tile game, would you like to see step-by-step moves or just
   the final result?

INTERVIEWER: Let's add a test case where combining same colors is crucial.

ME: Great suggestion! Let me add that:
"""

def test_color_strategy():
    """
    Test case where color matching is strategic
    Example: [W,W,G] -> combining W+W first leads to loss
                       but W+G might lead to win
    """
    test_color = [(1,'W'), (1,'W'), (1,'G')]
    print("\nTest Color Strategy:")
    print_game_state(test_color)
    
    # Show possible first moves
    print("Possible first moves:")
    next_states = get_next_states(test_color)
    for i, state in enumerate(next_states, 1):
        print(f"Move {i}:")
        print_game_state(state)
    
    result = solve_game(test_color)
    print(f"Player 1 {'wins' if result else 'loses'}")

"""
ME: Would you like me to:
1. Add more test cases?
2. Show the full game tree for any specific case?
3. Add move validation?
4. Implement a play function to actually play against the computer?

This way we can ensure the solution is thoroughly tested and meets all
requirements.
"""

"""
ME: Let me show why I'd prefer starting with a smaller example before the full 12-tile case.

Small Example (4 tiles: WWGG):
-----------------------------
Initial:   [W][W][G][G]

Complete Game Tree:
                    [W,W,G,G]
                   /    |    \
           [WW,G,G]  [WG,W,G]  [W,W,GG]
                |        |         |
           [WW,GG]   [WG,WG]   [WW,GG]
                ×        ×         ×
(× means no valid moves - previous player wins)

This is manageable to:
1. Trace manually
2. Verify correctness
3. Debug edge cases
4. Understand state transitions

Full 12-tile Case:
-----------------
[W,W,W,G,G,G,R,R,R,B,B,B]

Let's see just first level of moves to understand complexity:

Same Height Combinations (just first turn):
- W+W → [WW,W,G,G,G,R,R,R,B,B,B]
- W+G → [WG,W,W,G,G,R,R,R,B,B,B]
- W+R → [WR,W,W,G,G,G,R,R,B,B,B]
- W+B → [WB,W,W,G,G,G,R,R,R,B,B]
- G+G → [W,W,W,GG,G,R,R,R,B,B,B]
... and many more

Even just first move has:
- 66 possible combinations (12C2 where heights match)
- Each leading to different states
- Tree grows exponentially

Would you like me to:
1. Code a function to count valid moves at each level?
2. Show the full solution but print only key decision points?
3. Add visualization for critical game states?
"""

def analyze_branching_factor():
    """
    Analyze complexity of 12-tile game
    """
    initial = [(1,'W'), (1,'W'), (1,'W'),
              (1,'G'), (1,'G'), (1,'G'),
              (1,'R'), (1,'R'), (1,'R'),
              (1,'B'), (1,'B'), (1,'B')]
    
    moves = get_next_states(initial)
    print(f"First turn possibilities: {len(moves)}")
    
    # Sample a few moves to show diversity
    print("\nSample first moves:")
    for i, state in enumerate(moves[:3]):
        print(f"\nMove {i+1}:")
        print_game_state(state)

def print_game_state(state):
    """Enhanced visualization"""
    stacks = []
    for height, color in state:
        stack = color * height
        stacks.append(f"[{stack}]")
    print(" ".join(stacks))

"""
ME: For a Google L5 interview, I believe it's important to show:
1. Understanding of problem complexity
2. Ability to break down into manageable pieces
3. Testing strategy for complex cases
4. Performance considerations

Would you prefer I:
A. Continue with small examples to prove correctness?
B. Implement sampling of full game tree?
C. Add heuristics to handle complexity?
"""