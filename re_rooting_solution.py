from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        subtree_count = [1] * n
        ans = [0] * n

        # DFS 1: Bottom-Up (Post-Order)
        # Calculates subtree size and initial distances for Root (0)
        def post_order(node, parent):
            for child in graph[node]:
                if child != parent:
                    post_order(child, node)
                    subtree_count[node] += subtree_count[child]
                    # Distance to nodes in child's subtree is:
                    # distance from child to them (ans[child]) 
                    # + 1 step for each node in that subtree (subtree_count[child])
                    ans[node] += ans[child] + subtree_count[child]

        # DFS 2: Top-Down (Pre-Order)
        # Re-roots the tree to calculate answer for children using parent's data
        def pre_order(node, parent):
            for child in graph[node]:
                if child != parent:
                    # The Formula: ans[child] = ans[parent] - closer_nodes + farther_nodes
                    # closer_nodes = subtree_count[child]
                    # farther_nodes = n - subtree_count[child]
                    ans[child] = ans[node] - subtree_count[child] + (n - subtree_count[child])
                    pre_order(child, node)

        # 1. Gather stats assuming 0 is root
        post_order(0, None)
        # 2. Distribute stats to find real answers
        pre_order(0, None)

        return ans

# Verification Script
if __name__ == "__main__":
    sol = Solution()
    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    result = sol.sumOfDistancesInTree(n, edges)
    print(f"Input: n={n}, edges={edges}")
    print(f"Output: {result}")
    expected = [8, 12, 6, 10, 10, 10]
    print(f"Correct? {result == expected}")
