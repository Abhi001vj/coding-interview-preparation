# DSA Algorithm Templates

A comprehensive collection of algorithm patterns and templates for coding interviews. Each template includes:

- **Pattern Recognition** - Keywords and signals to identify when to use
- **Base Templates** - Clean, reusable code templates
- **Key Insights** - Visual explanations of why the algorithm works
- **LeetCode Problems** - 8-10 curated problems with solutions showing how to adapt the template
- **Common Mistakes** - Pitfalls to avoid
- **Practice Checklist** - Problems to master the pattern

---

## Quick Reference

| # | Template | Key Signal | Time |
|---|----------|-----------|------|
| 01 | [Binary Search on Answer](01-binary-search-on-answer.md) | "Minimize maximum" / "Find smallest X where..." | O(n log range) |
| 02 | [Monotonic Stack](02-monotonic-stack.md) | "Next/previous greater/smaller" | O(n) |
| 03 | [Heap / Priority Queue](03-heap-priority-queue.md) | "K-th largest" / "Top K" / "Merge K sorted" | O(n log k) |
| 04 | [Interval Problems](04-interval-problems.md) | "Overlapping intervals" / "Meeting rooms" | O(n log n) |
| 05 | [Sliding Window](05-sliding-window.md) | "Contiguous subarray" / "Longest substring" | O(n) |
| 06 | [Two Pointers](06-two-pointers.md) | "Sorted array" / "Pair with target sum" | O(n) |
| 07 | [Backtracking](07-backtracking.md) | "Generate all" / "Permutations" / "N-Queens" | O(2^n) or O(n!) |
| 08 | [Game Theory DP](08-game-theory-dp.md) | "Two players" / "Play optimally" | O(n²) |
| 09 | [Trie & Bit Manipulation](09-trie-bit-manipulation.md) | "Prefix search" / "Maximum XOR" | O(n * 32) |

---

## Pattern Selection Flowchart

```
                    What's the problem about?
                              │
        ┌─────────────────────┼─────────────────────┐
        ↓                     ↓                     ↓
   ARRAY/STRING           OPTIMIZATION          GENERATE ALL
        │                     │                     │
   ┌────┴────┐          ┌────┴────┐                ↓
   ↓         ↓          ↓         ↓           BACKTRACKING
Sorted?  Subarray?   Min/Max?  Two Players?
   │         │          │         │
   ↓         ↓          ↓         ↓
TWO PTR  SLIDING     BINARY    GAME THEORY
         WINDOW      SEARCH        DP
                        │
              ┌─────────┼─────────┐
              ↓         ↓         ↓
         On Array?  On Answer?  K-th?
              │         │         │
              ↓         ↓         ↓
          Standard   BS on      HEAP
            BS      Answer
```

---

## Templates by Category

### Search & Optimization
- [01 - Binary Search on Answer](01-binary-search-on-answer.md) - Find optimal value satisfying condition

### Stack-Based
- [02 - Monotonic Stack](02-monotonic-stack.md) - Next/previous greater/smaller element

### Priority-Based
- [03 - Heap / Priority Queue](03-heap-priority-queue.md) - K-th elements, merge sorted lists

### Range-Based
- [04 - Interval Problems](04-interval-problems.md) - Overlapping intervals, scheduling

### Window-Based
- [05 - Sliding Window](05-sliding-window.md) - Contiguous subarray/substring optimization

### Pointer-Based
- [06 - Two Pointers](06-two-pointers.md) - Sorted arrays, pair finding, partitioning

### Exhaustive Search
- [07 - Backtracking](07-backtracking.md) - Generate all combinations/permutations

### Game Strategy
- [08 - Game Theory DP](08-game-theory-dp.md) - Two-player optimal strategy

### Specialized Structures
- [09 - Trie & Bit Manipulation](09-trie-bit-manipulation.md) - Prefix trees, XOR optimization

---

## Master Cheat Sheet

### The "Opposite" Rule

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   HEAP:                                                         │
│   • K-th LARGEST  →  MIN heap size K (kicks smallest)          │
│   • K-th SMALLEST →  MAX heap size K (kicks largest)           │
│                                                                 │
│   MONOTONIC STACK:                                              │
│   • Find GREATER  →  DECREASING stack (small waits on top)     │
│   • Find SMALLER  →  INCREASING stack (large waits on top)     │
│                                                                 │
│   The "opposite" structure creates a GATEKEEPER!               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Binary Search Templates

```
FIND MINIMUM valid:
    while lo < hi:
        mid = (lo + hi) // 2
        if is_valid(mid):
            hi = mid         ← Keep mid, might be answer
        else:
            lo = mid + 1     ← Skip mid, definitely wrong

FIND MAXIMUM valid:
    while lo < hi:
        mid = (lo + hi + 1) // 2    ← +1 prevents infinite loop
        if is_valid(mid):
            lo = mid         ← Keep mid, might be answer
        else:
            hi = mid - 1     ← Skip mid, definitely wrong
```

### Interval Sorting

```
Sort by END:   Min arrows, Max non-overlapping
Sort by START: Merge intervals, Meeting rooms
```

### Sliding Window

```
LONGEST:  Shrink while INVALID
SHORTEST: Shrink while VALID
COUNT:    "Exactly K" = "At Most K" - "At Most K-1"
```

---

## Study Order (Recommended)

### Week 1-2: Foundation
1. [Two Pointers](06-two-pointers.md) - Foundation for many patterns
2. [Sliding Window](05-sliding-window.md) - Builds on two pointers
3. [Binary Search on Answer](01-binary-search-on-answer.md) - Critical for optimization

### Week 3-4: Stack & Heap
4. [Monotonic Stack](02-monotonic-stack.md) - Essential pattern
5. [Heap / Priority Queue](03-heap-priority-queue.md) - K-th and merge problems

### Week 5-6: Intervals & Backtracking
6. [Interval Problems](04-interval-problems.md) - Scheduling problems
7. [Backtracking](07-backtracking.md) - Exhaustive search

### Week 7-8: Advanced
8. [Game Theory DP](08-game-theory-dp.md) - Two-player games
9. [Trie & Bit Manipulation](09-trie-bit-manipulation.md) - Specialized problems

---

## Total Problems Covered

| Template | Problems | Difficulty Range |
|----------|----------|------------------|
| Binary Search | 9 | Easy - Hard |
| Monotonic Stack | 10 | Medium - Hard |
| Heap | 10 | Easy - Hard |
| Intervals | 10 | Easy - Medium |
| Sliding Window | 10 | Medium - Hard |
| Two Pointers | 10 | Easy - Medium |
| Backtracking | 10 | Medium - Hard |
| Game Theory | 8 | Medium - Hard |
| Trie/Bits | 10 | Easy - Hard |
| **Total** | **~87 problems** | |

---

## How to Use These Templates

### During Practice
1. Read the **Pattern Recognition** section first
2. Understand the **Base Template** and **Key Insights**
3. Work through problems in order (easier to harder)
4. For each problem, identify template modification needed
5. Check **Common Mistakes** if stuck

### During Interviews
1. Identify pattern from problem signals
2. Recall base template from memory
3. State the template modification needed out loud
4. Write code, following the template structure
5. Verify with edge cases

### Building Muscle Memory
1. Practice typing templates without looking
2. Time yourself on template problems
3. Explain the "why" out loud as you code
4. Review failed problems and note the pattern

---

## Quick Links

- [Original templates.md reference](../templates.md) - Historical reference
- [12 Essential Patterns](../skills/dsa-practice/references/patterns.md) - Condensed patterns
- [Common Bugs](../skills/dsa-practice/references/common-bugs.md) - Bug patterns to avoid
