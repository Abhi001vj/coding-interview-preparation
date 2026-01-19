# Snapshot Array (Time-Travel Data Structures)

This pattern involves designing data structures that can query their state at a specific point in the past ("snapshot").

## Core Concepts
- **Versioning:** Every modification increments a global `snap_id` or creates a new "version" entry.
- **Storage:** Instead of `arr[index] = value`, we store `arr[index] = List[(snap_id, value)]`.
- **Retrieval (Binary Search):** To find the value at `snap_id = K`, we binary search the history list for the largest ID $\le K$.

## Pattern Variations & Examples

| Problem | Difficulty | Key Concept | Modification to Base Pattern |
|:---|:---|:---|:---|
| **[1146. Snapshot Array](https://leetcode.com/problems/snapshot-array/)** | Medium | **Base Pattern** | Use `List[List[pair]]` and `bisect_right`. |
| **[981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)** | Medium | **Map + Binary Search** | Same as Snapshot Array, but keys are Strings and versions are explicit Timestamps. |
| **[460. LFU Cache](https://leetcode.com/problems/lfu-cache/)** | Hard | **Tie-Breaking** | Uses a "time" counter to break ties for Least Frequently Used items. |
| **[114. Flatten Binary Tree](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)** | Medium | **History/State** | While not strict "Snapshot", Morris Traversal uses links to return to past state. (Loose connection). |
| **[Design Version Control System]** | System Design | **Concept** | Git-like systems use DAGs, but linear history is the simplified "Snapshot" model. |

## Complexity
- **Set/Snap:** $O(1)$.
- **Get:** $O(\log S)$ where $S$ is the number of snapshots/updates for that index.
- **Space:** $O(S)$ total updates.

## Visualization
Run the included python script `1146_snapshot_visualizer.py` to see how the inner lists grow and how binary search finds the correct version.
