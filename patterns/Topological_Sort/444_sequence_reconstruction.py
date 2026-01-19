import collections
import time
from typing import List

# Try to import visualization tools
try:
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import networkx as nx
    VISUALIZATION_AVAILABLE = True
except ImportError:
    VISUALIZATION_AVAILABLE = False
    print("Warning: 'networkx' or 'matplotlib' not found. Visualizations skipped.")

class Solution:
    def explain_problem(self):
        print(f"\n{'='*80}")
        print(f"PROBLEM: 444. Sequence Reconstruction (Topological Sort / Graph)")
        print(f"{'='*80}")
        print("GOAL: Determine if 'nums' is the ONLY shortest supersequence of 'sequences'.")
        print("\nWHAT DOES THIS MEAN?")
        print("1. 'nums' must be a valid Topological Sort of the graph defined by 'sequences'.")
        print("2. It must be the UNIQUE topological sort.")
        print("\nVISUAL INTUITION:")
        print("- Imagine 'nums' as a straight path: [1] -> [2] -> [3] -> [4]")
        print("- For this order to be UNIQUE, every step must be 'forced'.")
        print("- There must be an explicit edge 1->2, an explicit edge 2->3, etc.")
        print("- If we have 1->2 and 3->4, but NO edge between 2 and 3, then 2 and 3")
        print("  could swap places! The order is not fixed. -> Returns False.")
        print(f"{'='*80}\n")

    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        self.explain_problem()
        
        # --- logic setup ---
        adj = collections.defaultdict(set)
        edges_set = set()
        nodes = set()
        
        # For visualization
        animation_events = [] # List of events: ('type', data...)
        
        print(">>> Step 1: Building Graph...")
        for seq in sequences:
            for i in range(len(seq) - 1):
                u, v = seq[i], seq[i+1]
                if v not in adj[u]:
                    adj[u].add(v)
                    edges_set.add((u, v))
                    nodes.add(u)
                    nodes.add(v)
                    print(f"    + Edge: {u} -> {v}")
                    animation_events.append(('build', u, v))
        
        # Ensure all nodes in nums are in the node set for vis
        for n in nums: nodes.add(n)

        print("\n>>> Step 2: Verifying Uniqueness (Hamiltonian Path)...")
        is_valid = True
        missing_edge = None
        
        for i in range(len(nums) - 1):
            u, v = nums[i], nums[i+1]
            print(f"    Checking constraint: {u} -> {v}...", end=" ")
            
            if (u, v) not in edges_set:
                print("MISSING! ❌")
                is_valid = False
                missing_edge = (u, v)
                animation_events.append(('check_fail', u, v))
                break # Fail early logic, but for vis we might want to stop here
            else:
                print("OK ✅")
                animation_events.append(('check_ok', u, v))
        
        result_msg = "VALID (Unique)" if is_valid else "INVALID (Not Unique)"
        print(f"\nFINAL RESULT: {is_valid} [{result_msg}]")
        
        if VISUALIZATION_AVAILABLE:
            self.run_animation(nums, nodes, edges_set, animation_events, is_valid)
            
        return is_valid

    def run_animation(self, nums, all_nodes, all_edges, events, final_result):
        """
        Creates a single window animation of the process.
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        G = nx.DiGraph()
        G.add_nodes_from(all_nodes)
        G.add_edges_from(all_edges)
        
        # Fixed layout so nodes don't jump around
        # We try to align them in a line if possible to match 'nums' visual intuition
        pos = {}
        for i, node in enumerate(nums):
            pos[node] = (i, 0) # Position nodes linearly: (0,0), (1,0)...
        
        # Add any extra nodes not in nums (shouldn't happen per constraints but safety)
        for node in all_nodes:
            if node not in pos:
                pos[node] = (0, 1)

        # Initial drawing lists
        current_edges = []
        edge_colors = []
        
        def update(frame):
            ax.clear()
            ax.set_title(f"Frame {frame+1}/{len(events)}", fontsize=10)
            
            # Base Draw
            nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightgray', node_size=1500)
            nx.draw_networkx_labels(G, pos, ax=ax, font_size=12, font_weight='bold')
            
            # Determine state based on current event index
            if frame < len(events):
                event_type, u, v = events[frame]
                
                if event_type == 'build':
                    ax.set_title(f"Building Graph: Added {u} -> {v}", fontsize=14, color='blue')
                    # Draw all edges up to this point
                    # For simplicity in this lightweight animation, we'll draw static G edges
                    # and highlight the new one
                    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray', arrows=True, width=1)
                    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[(u,v)], edge_color='blue', width=3)
                    
                elif event_type == 'check_ok':
                    ax.set_title(f"Verifying: {u} -> {v} EXISTS ✅", fontsize=14, color='green')
                    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray', arrows=True, width=1)
                    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[(u,v)], edge_color='green', width=4)
                    
                elif event_type == 'check_fail':
                    ax.set_title(f"Verifying: {u} -> {v} MISSING ❌", fontsize=14, color='red')
                    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray', arrows=True, width=1)
                    # Draw missing edge as dashed red
                    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[(u,v)], edge_color='red', style='dashed', width=4)
            else:
                # Final Frame
                color = 'green' if final_result else 'red'
                text = "VALID: Unique Sequence" if final_result else "INVALID: Ambiguous Order"
                ax.set_title(f"Result: {text}", fontsize=16, color=color, fontweight='bold')
                nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray', arrows=True)

            # Draw 'nums' order hint at bottom
            plt.text(0.5, -0.1, f"Target Order: {nums}", horizontalalignment='center', transform=ax.transAxes)

        ani = animation.FuncAnimation(fig, update, frames=len(events)+5, interval=1000, repeat=False)
        plt.show()

if __name__ == "__main__":
    solver = Solution()
    
    # Run a test case
    # Try the ambiguous one first to show the red failure
    print("\n\nRUNNING TEST CASE 1: [1,2,3] with [[1,2], [1,3]]")
    solver.sequenceReconstruction([1,2,3], [[1,2], [1,3]])
    
    # Commented out to prevent immediate second window, user can uncomment
    # print("\n\nRUNNING TEST CASE 2: [1,2,3] with [[1,2], [1,3], [2,3]]")
    # solver.sequenceReconstruction([1,2,3], [[1,2], [1,3], [2,3]])