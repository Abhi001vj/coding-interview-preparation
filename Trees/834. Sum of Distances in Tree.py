"""
834. Sum of Distances in Tree (Hard)
Pattern: Re-rooting DP (Dynamic Programming on Trees) / Up-Down DP

--------------------------------------------------------------------------------
PROBLEM UNDERSTANDING
--------------------------------------------------------------------------------
We need the sum of distances from EVERY node to ALL other nodes.
Naive BFS from every node is O(N^2), which is too slow (N <= 30,000).
We need an O(N) solution.

--------------------------------------------------------------------------------
THE "MOVING HOUSE" INTUITION (Analogy)
--------------------------------------------------------------------------------
Imagine organizing a meetup.
1. First, we calculate the total travel distance if everyone meets at Node 0.
   (This is the "Bottom-Up" DFS 1).

2. Then, we think: "What if we move the meeting to neighbor Node 2?"
   (This is the "Top-Down" DFS 2).

   - Who walks LESS?
     Everyone living in Node 2's subtree (including Node 2) is now 1 step closer.
   - Who walks MORE?
     Everyone NOT in Node 2's subtree (Node 0 and others) is now 1 step farther.

   Formula:
   New_Dist = Old_Dist - (Nodes_Closer) + (Nodes_Farther)

   This calculation is O(1) for each edge!

--------------------------------------------------------------------------------
THE ALGORITHM: TWO PASSES
--------------------------------------------------------------------------------

PHASE 1: Post-Order DFS (Bottom-Up)
- Goal: Gather info for the ROOT (Node 0) and subtree sizes.
- Logic:
    count[node] = 1 (self) + sum(count[children])
    ans[node]   = sum(ans[child] + count[child])
    
    Why "ans[child] + count[child]"?
    To reach nodes in child's subtree from parent, we travel to child (1 step)
    then to the target nodes. That 1 step is taken 'count[child]' times.

PHASE 2: Pre-Order DFS (Top-Down)
- Goal: Use Parent's answer to compute Children's answer.
- Logic:
    ans[child] = ans[parent] - count[child] + (N - count[child])
                 ^ Parent's   ^ Getting      ^ Getting
                   Total        Closer         Farther

--------------------------------------------------------------------------------
VISUALIZATION TRACE (Example: 0 -- 1 -- 2)
--------------------------------------------------------------------------------
Tree: (0) -- (1) -- (2)
N = 3

DFS 1 (Bottom-Up):
- Visit 2: count[2]=1, ans[2]=0
- Visit 1: 
    count[1] = 1 + count[2] = 2
    ans[1]   = ans[2] + count[2] = 0 + 1 = 1
- Visit 0:
    count[0] = 1 + count[1] = 3
    ans[0]   = ans[1] + count[1] = 1 + 2 = 3 (Correct for Node 0)

DFS 2 (Top-Down):
- Move 0 -> 1:
    ans[1] = ans[0] - count[1] + (N - count[1])
           = 3      - 2        + (3 - 2)
           = 3 - 2 + 1 = 2
    (Check: 1->0 is 1, 1->2 is 1. Total 2. Correct.)

- Move 1 -> 2:
    ans[2] = ans[1] - count[2] + (N - count[2])
           = 2      - 1        + (3 - 1)
           = 2 - 1 + 2 = 3
    (Check: 2->1 is 1, 2->0 is 2. Total 3. Correct.)

"""

from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # count[i] = number of nodes in subtree rooted at i (when 0 is root)
        count = [1] * n
        # ans[i] = sum of distances from i to all other nodes
        ans = [0] * n

        def post_order(node, parent):
            """
            DFS 1: Bottom-Up
            Aggregates subtree counts and calculates answer for the Root (0).
            """
            for child in graph[node]:
                if child != parent:
                    post_order(child, node)
                    
                    # 1. Update Subtree Count
                    # We add child's count to parent because parent's subtree includes child's
                    count[node] += count[child]
                    
                    # 2. Update Answer (Accumulate Distances)
                    # ans[child] is sum of distances within child's subtree.
                    # count[child] is the 1 extra step parent takes to reach each node in that subtree.
                    ans[node] += ans[child] + count[child]

        def pre_order(node, parent):
            """
            DFS 2: Top-Down
            Uses the Parent's fully calculated answer to determine Child's answer in O(1).
            """
            for child in graph[node]:
                if child != parent:
                    # The Re-rooting Equation:
                    # new_ans = old_ans - (nodes_getting_closer) + (nodes_getting_farther)
                    ans[child] = ans[node] - count[child] + (n - count[child])
                    
                    pre_order(child, node)

        # Step 1: Gather info at the root
        post_order(0, None)
        
        # Step 2: Distribute info to the children
        pre_order(0, None)
        
        return ans

# ------------------------------------------------------------------------------
# VISUALIZATION SCRIPT (Runnable Trace)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    def run_visualization():
        print("\n=== RUNNING VISUALIZATION ===")
        print("Tree:     0")
        print("         / \")
        print("        1   2")
        print("           /|\")
        print("          3 4 5")
        
        n = 6
        edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
        
        sol = Solution()
        result = sol.sumOfDistancesInTree(n, edges)
        
        print(f"\nResult: {result}")
        print("Expected: [8, 12, 6, 10, 10, 10]")
        
        print("\nVerification of Logic for Move 0 -> 2:")
        print("ans[0] = 8")
        print("count[2] (Subtree 2,3,4,5) = 4")
        print("Nodes NOT in Subtree 2 (0,1) = 6 - 4 = 2")
        print("Formula: ans[2] = ans[0] - count[2] + (N - count[2])")
        print(f"         ans[2] = 8      - 4        + 2  = 6")
        print(f"Calculated ans[2] is {result[2]}")

    run_visualization()

