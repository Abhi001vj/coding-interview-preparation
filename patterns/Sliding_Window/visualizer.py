import matplotlib.pyplot as plt
import matplotlib.animation as animation
import collections

class SlidingWindowVisualizer:
    def __init__(self, s, target_func, title="Sliding Window"):
        """
        s: The input string or array
        target_func: Function(window_counts) -> bool (is valid?)
        """
        self.s = s
        self.events = [] # ('expand', L, R, valid), ('shrink', L, R, valid)
        self.target_func = target_func
        self.title = title
        self.run_simulation()

    def run_simulation(self):
        left = 0
        counts = collections.Counter()
        
        for right in range(len(self.s)):
            char = self.s[right]
            counts[char] += 1
            
            # Record Expansion
            is_valid = self.target_func(counts)
            self.events.append(('expand', left, right, is_valid, dict(counts)))
            
            # Shrink Logic (Generic 'while invalid' or specific logic)
            # For visualization, we assume "Longest Valid" logic (Shrink if INVALID)
            # You can adapt this for "Shortest Valid" (Shrink if VALID)
            while not self.target_func(counts):
                remove_char = self.s[left]
                counts[remove_char] -= 1
                if counts[remove_char] == 0:
                    del counts[remove_char]
                left += 1
                
                # Record Shrink
                is_valid = self.target_func(counts)
                self.events.append(('shrink', left, right, is_valid, dict(counts)))

    def animate(self):
        fig, ax = plt.subplots(figsize=(12, 4))
        
        def update(frame):
            ax.clear()
            action, L, R, valid, state = self.events[frame]
            
            # Setup Plot
            ax.set_xlim(-1, len(self.s))
            ax.set_ylim(0, 2)
            ax.set_yticks([])
            ax.set_title(f"{self.title}\nStep {frame+1}: {action.upper()} | Window [{L}:{R}] | Valid: {valid}", fontsize=14)
            
            # Draw Elements
            for i, char in enumerate(self.s):
                color = 'black'
                font_weight = 'normal'
                bg_color = 'white'
                
                # In Window?
                if L <= i <= R:
                    bg_color = '#d1e7dd' if valid else '#f8d7da' # Greenish if valid, Reddish if invalid
                    font_weight = 'bold'
                
                # Draw Box
                rect = plt.Rectangle((i - 0.4, 0.5), 0.8, 0.8, facecolor=bg_color, edgecolor='black')
                ax.add_patch(rect)
                ax.text(i, 0.9, str(char), ha='center', fontsize=12, fontweight=font_weight)
                ax.text(i, 0.3, str(i), ha='center', fontsize=8, color='gray')

            # Draw Pointers
            ax.annotate('L', xy=(L, 0.5), xytext=(L, 0.1), arrowprops=dict(facecolor='blue', shrink=0.05), ha='center', color='blue', fontweight='bold')
            ax.annotate('R', xy=(R, 0.5), xytext=(R, 0.1), arrowprops=dict(facecolor='red', shrink=0.05), ha='center', color='red', fontweight='bold')

            # State Text
            state_str = str(state).replace("'", "")
            ax.text(len(self.s)/2, 1.6, f"State: {state_str}", ha='center', fontsize=10, bbox=dict(facecolor='#f0f0f0', alpha=0.5))

        ani = animation.FuncAnimation(fig, update, frames=len(self.events), interval=1000, repeat=False)
        plt.show()

# Example Usage (Uncomment to run directly)
if __name__ == "__main__":
    # Example: Longest Substring Without Repeating Characters
    # Constraint: max frequency of any char <= 1
    def no_repeats(counts):
        return all(c <= 1 for c in counts.values())

    vis = SlidingWindowVisualizer("abcabcbb", no_repeats, "LC 3. Longest Substring No Repeats")
    vis.animate()
