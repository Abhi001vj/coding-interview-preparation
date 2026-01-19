# Topological Sort Pattern

Topological Sort is an algorithm for linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge $(u, v)$, vertex $u$ comes before vertex $v$ in the ordering.

## Core Concepts
- **In-degree:** Number of incoming edges to a node.
- **Source Node:** Node with in-degree 0 (start of dependency chain).
- **Kahn's Algorithm (BFS):** Uses a queue to process nodes with 0 in-degree.
- **DFS Approach:** Uses recursion and a stack to build the order.

## Problem List

| Problem | Difficulty | Key Concept | Solution |
|:---|:---|:---|:---|
| [444. Sequence Reconstruction](444_sequence_reconstruction.py) | Medium | **Uniqueness Check** (Hamiltonian Path) | [Python](444_sequence_reconstruction.py) |

## Pattern Variations

### 1. Basic Topological Sort (Course Schedule II)
- **Goal:** Find ANY valid ordering.
- **Logic:** Standard Kahn's Algo (Queue) or DFS.

### 2. Cycle Detection (Course Schedule I)
- **Goal:** Check if sorting is possible.
- **Logic:** If sorted count < N, there is a cycle.

### 3. Unique Ordering (Sequence Reconstruction)
- **Goal:** Check if there is EXACTLY one valid topological sort.
- **Logic:** In Kahn's algorithm, the queue must always have size 1. Alternatively, check for Hamiltonian Path (adjacent nodes in sorted order must have an edge).

### 4. Lexicographically Smallest (Alien Dictionary)
- **Goal:** Resolve ambiguity using specific rules.
- **Logic:** Use a Min-Heap (Priority Queue) instead of a standard Queue.
