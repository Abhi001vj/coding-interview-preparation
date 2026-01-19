import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import random

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
        # For visualization: track history of operations
        self.history = [] 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True # Merged
        return False # Already connected (Cycle)

class Solution:
    def explain_problem(self):
        print(f"{'='*80}")
        print(f"PROBLEM: 684. Redundant Connection (Union-Find Pattern)")
        print(f"{'='*80}")
        print("GOAL: Find the edge that, when added, creates a cycle in the graph.")
        print("\nINTUITION:")
        print("- Start with N isolated nodes.")
        print("- Process edges one by one.")
        print("- For edge (u, v):")
        print("  1. Find root(u) and root(v).")
        print("  2. If root(u) != root(v): Merge them (Union). They are now one component.")
        print("  3. If root(u) == root(v): They are ALREADY connected! Adding this edge")
        print("     closes a loop. THIS is the redundant connection.")
        print(f"{'='*80}\n")

    def findRedundantConnection(self, edges):
        self.explain_problem()
        
        # Determine N from max node value
        n = 0
        for u, v in edges:
            n = max(n, u, v)
            
        dsu = DSU(n)
        
        # Events for visualization: ('type', u, v, root_u, root_v, success)
        events = []
        redundant = None
        
        print(">>> Processing Edges...")
        for u, v in edges:
            root_u = dsu.find(u)
            root_v = dsu.find(v)
            
            print(f"    Edge ({u}, {v}): Root({u})={root_u}, Root({v})={root_v} ...", end=" ")
            
            if dsu.union(u, v):
                print("Union Successful (Merged)")
                events.append(('union', u, v, root_u, root_v, True))
            else:
                print("CYCLE DETECTED! (Redundant)")
                events.append(('cycle', u, v, root_u, root_v, False))
                redundant = [u, v]
                break # Found the answer
                
        print(f"\nRESULT: {redundant}")
        
        # --- Visualization Logic ---
        try:
            self.run_animation(n, edges, events)
        except Exception as e:
            print(f"Visualization error: {e}")
            
        return redundant

    def run_animation(self, n, all_edges, events):
        fig, ax = plt.subplots(figsize=(10, 7))
        G = nx.Graph()
        G.add_nodes_from(range(1, n + 1))
        
        # Fixed layout circle
        pos = nx.circular_layout(G)
        
        # Colors for component tracking
        # We will dynamically update node colors based on their representative set
        # But determining sets dynamically for coloring is tricky without re-running DSU.
        # Simplification: Just show the graph structure updates.
        
        def update(frame):
            ax.clear()
            ax.set_title(f"Union-Find Step {frame+1}/{len(events)}", fontsize=14)
            
            # Reconstruct state up to this frame
            current_G = nx.Graph()
            current_G.add_nodes_from(range(1, n + 1))
            
            # Add all edges processed SO FAR (including the current one)
            processed_edges = [all_edges[i] for i in range(frame + 1)]
            current_G.add_edges_from(processed_edges[:-1]) # All previous edges
            
            # Draw existing graph
            nx.draw_networkx_nodes(current_G, pos, ax=ax, node_color='lightgray', node_size=800)
            nx.draw_networkx_labels(current_G, pos, ax=ax, font_weight='bold')
            nx.draw_networkx_edges(current_G, pos, ax=ax, edge_color='gray', width=2)
            
            # Highlight CURRENT action
            event_type, u, v, ru, rv, success = events[frame]
            
            if event_type == 'union':
                ax.set_title(f"Edge ({u}, {v}): Roots {ru} != {rv} → MERGE ✅", color='green', fontsize=16, fontweight='bold')
                nx.draw_networkx_edges(current_G, pos, ax=ax, edgelist=[(u,v)], edge_color='green', width=5)
            elif event_type == 'cycle':
                ax.set_title(f"Edge ({u}, {v}): Roots {ru} == {rv} → CYCLE DETECTED ❌", color='red', fontsize=16, fontweight='bold')
                nx.draw_networkx_edges(current_G, pos, ax=ax, edgelist=[(u,v)], edge_color='red', width=5)
                
            # Explanation text
            plt.text(0.5, -0.1, f"Nodes {u} and {v} are being processed.", 
                     horizontalalignment='center', transform=ax.transAxes, fontsize=12)

        ani = animation.FuncAnimation(fig, update, frames=len(events), interval=1500, repeat=False)
        plt.show()

if __name__ == "__main__":
    solver = Solution()
    # Test Case: [1,2], [1,3], [2,3] -> Cycle at [2,3]
    print("\nRunning Visualizer for Edges: [[1,2], [1,3], [2,3]]")
    solver.findRedundantConnection([[1,2], [1,3], [2,3]])
    
    # Larger Test Case: [1,2], [2,3], [3,4], [1,4], [1,5] -> Cycle at [1,4]
    # print("\nRunning Visualizer for Larger Graph...")
    # solver.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])
