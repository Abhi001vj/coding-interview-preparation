# 444. Sequence Reconstruction

**Difficulty:** Medium  
**Pattern:** Topological Sort (Verification Variant)  
**Key Concept:** Hamiltonian Path / Uniqueness Check

---

## 1. The Core Intuition

This problem asks: **"Is there EXACTLY one way to order these numbers to satisfy all rules?"**

Imagine you are assembling a Lego set.
- `nums` is the instruction manual's final order: `[Base, Walls, Roof]`.
- `sequences` are small hints you found: `[Base, Walls]` and `[Base, Roof]`.

The question is: **Do the hints force you to build the Walls BEFORE the Roof?**
- Hint 1: Base → Walls
- Hint 2: Base → Roof
- **Result:** You know Base is first. But Walls vs. Roof? You have no rule! You could build Roof then Walls.
- **Verdict:** The order is NOT unique. `nums` is not the only supersequence.

To be unique, you need a "Chain of Command" where every single step is forced by a rule.
`A -> B -> C -> D`
There must be a rule saying "A before B", "B before C", "C before D".

---

## 2. How to Spot This "In The Wild"

Look for these triggers in an interview question:

1.  **Dependency Rules:** "Course A must be before Course B", "Task X depends on Task Y".
2.  **Ordering/Sorting:** You are asked to find an order or check if an order is valid.
3.  **"Unique" or "Only":** The problem specifically asks if the valid order is *unique* or if the given array is the *only* solution.

**The "Uniqueness" Trigger:**
- If standard Topological Sort asks "Can we finish courses?", it's a Cycle Detection problem.
- If it asks "Find a valid order", it's a standard Queue/DFS problem.
- If it asks "Is the order UNIQUE?", it is a **Hamiltonian Path** problem.

---

## 3. The Thought Process (Step-by-Step)

### Attempt 1: Brute Force (Don't do this)
"I will generate ALL possible topological sorts and check if there is only 1."
- **Why it fails:** Generating all permutations is $O(N!)$. Impossible for $N=10^4$.

### Attempt 2: Standard Kahn's Algorithm
"I will run the standard Topological Sort (Kahn's Algo) using a Queue."
- **Logic:** In Kahn's algorithm, we add nodes with `indegree == 0` to a queue.
- **Uniqueness Check:** If at any point the `queue.size() > 1`, it means we have two valid choices for the next step.
- **Verdict:** If `queue.size()` is always 1, the sort is unique.
- **Complexity:** $O(V + E)$.
- **Status:** Correct and Accepted. But... can we do better?

### Attempt 3: The "Verification" Shortcut (Master Level)
"Wait, the problem **GAVE ME** the target answer (`nums`). I don't need to *find* the sort. I just need to *verify* it."

**The Insight:**
If `nums = [1, 2, 3, 4]` is the unique sort, then:
1.  1 must point to 2.
2.  2 must point to 3.
3.  3 must point to 4.

If we are missing the edge `2 -> 3`, then 2 and 3 are not locked relative to each other.

**Algorithm:**
1.  Build the graph (Adjacency Set) from `sequences`.
2.  Iterate through `nums` from `0` to `n-2`.
3.  Check: Does the graph contain edge `nums[i] -> nums[i+1]`?
4.  If YES for all: Return `True`.
5.  If NO for any: Return `False`.

**Complexity:**
- Time: $O(V + E)$ to build graph + $O(N)$ to check. Total $O(V+E)$.
- Space: $O(V + E)$.

---

## 4. The Python Solution (Verification Approach)

```python
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # 1. Build the Graph
        # We use a set of tuples for O(1) edge lookup
        edges = set()
        for seq in sequences:
            for i in range(len(seq) - 1):
                u, v = seq[i], seq[i+1]
                edges.add((u, v))
        
        # 2. Check strict ordering in 'nums'
        # For nums to be the ONLY valid sort, every adjacent step must be explicit
        for i in range(len(nums) - 1):
            u = nums[i]
            v = nums[i+1]
            
            # If there is no direct rule saying u -> v, 
            # then u and v are not strictly ordered.
            if (u, v) not in edges:
                return False
                
        return True
```

---

## 5. Variations: What If The Question Changed?

It is crucial to understand how slight wording changes affect the difficulty and solution.

| Question Variant | Difficulty | Logic Required |
| :--- | :--- | :--- |
| **"Is `nums` THE ONLY shortest supersequence?"** | **Medium (Current)** | **Hamiltonian Path Check** <br> Strict adjacency: Edge $u \to v$ must exist for all neighbors. |
| **"Is `nums` ONE OF the shortest supersequences?"** | **Easy** | **Validity Check** <br> Loose order: Check `index[u] < index[v]` for all rules. No need for direct edges. |
| **"Construct ANY shortest supersequence"** | **Medium** | **Standard Topological Sort** <br> Use Kahn's Algo (Queue). Any valid sort is a shortest supersequence here. |
| **"Find Shortest Common Supersequence (Strings)"** | **Hard (DP)** | **LCS / Dynamic Programming** <br> If inputs are general strings (not 1..N perms), this becomes NP-Hard/DP. |

**Key Takeaway:** The "Unique" constraint transforms the problem from a loose relative ordering check into a strict neighbor-connectivity check.

---

## 6. Summary Checklist
- [x] **Graph Build:** Did I capture all dependencies?
- [x] **Adjacency:** Did I check `(nums[i], nums[i+1])` exists?
- [x] **Edge Case:** $N=1$? Loop range `range(0)` handles it correctly.

```