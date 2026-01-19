import matplotlib.pyplot as plt
import matplotlib.animation as animation
import bisect

class SnapshotArray:
    def __init__(self, length):
        self.snap_id = 0
        # List of lists. Each entry is (snap_id, value)
        # Initial value is 0 at snap_id 0
        self.history = [[(0, 0)] for _ in range(length)]
        self.events = [] # For visualization

    def set(self, index, val):
        self.events.append(('set', index, val, self.snap_id))
        # Logic: If we already have an entry for current snap_id, update it.
        # Otherwise, append new entry.
        if self.history[index][-1][0] == self.snap_id:
            self.history[index][-1] = (self.snap_id, val)
        else:
            self.history[index].append((self.snap_id, val))

    def snap(self):
        self.events.append(('snap', self.snap_id, self.snap_id + 1))
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        # Binary search
        # We want the rightmost entry where entry.snap_id <= snap_id
        hist = self.history[index]
        i = bisect.bisect_right(hist, (snap_id, float('inf'))) - 1
        val = hist[i][1]
        self.events.append(('get', index, snap_id, val, hist[:]))
        return val

class Visualizer:
    def explain_problem(self):
        print(f"\n{'='*80}")
        print(f"PROBLEM: 1146. Snapshot Array (Time-Travel Pattern)")
        print(f"{'='*80}")
        print("GOAL: Implement an array that supports taking snapshots and retrieving")
        print("      values from past snapshots.")
        print("\nINTUITION:")
        print("- Regular Array: [5, 10, 0]")
        print("- Snapshot Array: We store a HISTORY for each index.")
        print("  Index 0: [(snap0, 0), (snap2, 5)]")
        print("  Index 1: [(snap0, 0), (snap1, 10), (snap3, 20)]")
        print("\n- GET(index=1, snap=2)?")
        print("  Look at Index 1 history. We want entry with highest ID <= 2.")
        print("  Entries: (0,0), (1,10), (3,20)")
        print("  snap=2 matches (1,10) because 3 is too big.")
        print("  Return 10.")
        print(f"{'='*80}\n")

    def run_demo(self):
        self.explain_problem()
        
        # Scenario: Length 3 array
        arr = SnapshotArray(3)
        print(">>> Initialized SnapshotArray(3)")
        
        # Operations
        print(">>> Set(0, 5)")
        arr.set(0, 5)
        
        print(">>> SNAP! (Returns ID 0)")
        arr.snap()
        
        print(">>> Set(0, 6)")
        arr.set(0, 6)
        
        print(">>> Set(1, 10)")
        arr.set(1, 10) # Valid for snap 1
        
        print(">>> SNAP! (Returns ID 1)")
        arr.snap()
        
        print(">>> GET(0, snap_id=0) -> Expect 5")
        v1 = arr.get(0, 0)
        print(f"    Result: {v1}")
        
        print(">>> GET(0, snap_id=1) -> Expect 6")
        v2 = arr.get(0, 1)
        print(f"    Result: {v2}")

        print(">>> GET(1, snap_id=0) -> Expect 0 (Default)")
        v3 = arr.get(1, 0)
        print(f"    Result: {v3}")

        # Visualization
        try:
            self.animate(arr.events)
        except Exception as e:
            print(f"Visualization error: {e}")

    def animate(self, events):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # State tracking for visualization
        # Visual representation: 3 rows (indices).
        # Each row shows boxes representing the history list.
        current_history = [[(0, 0)] for _ in range(3)]
        current_snap = 0
        
        def update(frame):
            ax.clear()
            ax.set_title(f"Operation {frame+1}/{len(events)}", fontsize=14)
            ax.set_xlim(-1, 8)
            ax.set_ylim(-1, 3)
            ax.set_yticks([0, 1, 2])
            ax.set_yticklabels(['Idx 0', 'Idx 1', 'Idx 2'])
            ax.grid(True, axis='y', linestyle='--', alpha=0.3)
            
            # Process event for THIS frame to update state
            event = events[frame]
            etype = event[0]
            
            nonlocal current_snap
            highlight_rect = None
            msg = ""
            
            if etype == 'set':
                idx, val, snap = event[1], event[2], event[3]
                msg = f"SET(idx={idx}, val={val}) @ Snap {snap}"
                # Update logic copy
                if current_history[idx][-1][0] == snap:
                    current_history[idx][-1] = (snap, val)
                else:
                    current_history[idx].append((snap, val))
                highlight_rect = (idx, len(current_history[idx])-1, 'green') # New/Updated
                
            elif etype == 'snap':
                old_s, new_s = event[1], event[2]
                current_snap = new_s
                msg = f"SNAP! {old_s} -> {new_s}"
                
            elif etype == 'get':
                idx, query_snap, res, full_hist = event[1], event[2], event[3], event[4]
                msg = f"GET(idx={idx}, snap={query_snap}) -> {res}"
                # Find which index was picked
                pick_i = bisect.bisect_right(full_hist, (query_snap, float('inf'))) - 1
                highlight_rect = (idx, pick_i, 'orange') # Found
            
            ax.set_xlabel(f"Global Snap ID: {current_snap}", fontsize=12, fontweight='bold')
            ax.text(0.5, 1.05, msg, transform=ax.transAxes, ha='center', fontsize=14, color='blue')

            # Draw the history lists
            for r in range(3):
                hist = current_history[r]
                for c, (s_id, val) in enumerate(hist):
                    # Draw box
                    color = 'white'
                    edge = 'black'
                    lw = 1
                    
                    if highlight_rect and highlight_rect[0] == r and highlight_rect[1] == c:
                        color = highlight_rect[2] # Green or Orange
                        lw = 3
                        
                    rect = plt.Rectangle((c, r - 0.25), 0.8, 0.5, facecolor=color, edgecolor=edge, linewidth=lw)
                    ax.add_patch(rect)
                    ax.text(c + 0.4, r, f"S:{s_id}\nV:{val}", ha='center', va='center', fontsize=10)

        ani = animation.FuncAnimation(fig, update, frames=len(events), interval=2000, repeat=False)
        plt.show()

if __name__ == "__main__":
    vis = Visualizer()
    vis.run_demo()
