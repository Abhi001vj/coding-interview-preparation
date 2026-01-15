# Meta Interview Constraint Variations

## Overview

Meta (Facebook) typically uses standard LeetCode problems but with **modified constraints** or **output format changes**. Unlike Google's scenario wrapping, Meta's variations are more direct - same problem structure, different requirements.

**Key Insight**: Know the standard solution, then adapt to the twist. The twist usually tests edge case handling, optimization, or deeper understanding.

---

## How Meta Presents Problems

### Standard LeetCode Format
```
Given an array and target, return indices of two numbers that add to target.
Return [i, j] where i < j.
```

### Meta Variation
```
Given an array and target, return indices of two numbers that add to target.
Return indices in DESCENDING order. If multiple pairs exist, return the pair
with the SMALLEST sum of indices.
```

**Same algorithm, different output handling.**

---

## Constraint Variation Categories

### Category 1: Output Format Changes

#### Return Order Modifications
| Standard | Meta Variation |
|----------|---------------|
| Return any valid answer | Return lexicographically smallest |
| Return [i, j] where i < j | Return [i, j] in descending order |
| Return one solution | Return ALL solutions |
| Return indices | Return values instead |
| Return count | Return actual elements |

#### Example: Group Anagrams (LC49) - YOUR INTERVIEW PATTERN
**Standard**: Return groups in any order
```python
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]  # Any order OK
```

**Meta Variation**: Return groups sorted by size, then lexicographically
```python
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Groups sorted by size (ascending), within group sorted lexicographically
```

---

### Category 2: Additional Constraints

#### Space Constraints
| Standard | Meta Variation |
|----------|---------------|
| O(n) space allowed | O(1) extra space only |
| Can use hash map | No extra data structures |
| Create new output | Modify in-place |

#### Example: Move Zeroes (LC283)
**Standard**: Move zeroes to end, O(n) space OK
**Meta Variation**: Move zeroes to end, must be in-place, maintain relative order of non-zeros

#### Time Constraints
| Standard | Meta Variation |
|----------|---------------|
| O(n log n) acceptable | Must be O(n) |
| Multiple passes OK | Single pass only |
| Can preprocess | Online/streaming |

#### Example: Two Sum (LC1)
**Standard**: O(n) with hash map
**Meta Variation**: Array is sorted, solve in O(1) extra space (two pointers)

---

### Category 3: Follow-up Questions

Meta loves follow-up questions that extend the original problem:

#### Scaling Follow-ups
- "What if the array doesn't fit in memory?"
- "What if you receive elements as a stream?"
- "What if there are billions of elements?"

#### Optimization Follow-ups
- "Can you do better than O(n log n)?"
- "Can you solve it with O(1) space?"
- "What if we need to call this function repeatedly?"

#### Edge Case Follow-ups
- "What if there are duplicates?"
- "What if input can be negative?"
- "What if the result overflows?"

---

## Pattern-Specific Meta Variations

### Pattern 1: Arrays & Hashing

#### Two Sum Variations
| Variation | Change |
|-----------|--------|
| Two Sum II | Input array is sorted |
| Two Sum III | Design class, multiple add/find calls |
| Two Sum IV | Input is BST |
| **Meta Twist** | Return all pairs, sorted by sum |

#### Subarray Sum Variations
| Standard | Meta Twist |
|----------|-----------|
| Count subarrays with sum K | Return start/end indices of ALL such subarrays |
| Find if subarray exists | Find the SHORTEST subarray |
| Any subarray | CONTIGUOUS subarray only |

---

### Pattern 2: Trees (Heavy Meta Focus)

Meta emphasizes trees heavily. Common variations:

#### Binary Tree Level Order (LC102)
**Standard**: Return levels top to bottom
**Meta Variations**:
- Bottom to top (LC107)
- Zigzag order (LC103)
- Return just the rightmost node of each level (LC199)
- Return just nodes at depth K

#### Lowest Common Ancestor (LC236)
**Standard**: Two nodes guaranteed to exist
**Meta Variations**:
- Nodes might not exist in tree
- Find LCA of K nodes (not just 2)
- Return all ancestors, not just lowest
- Tree has parent pointers

#### Tree Traversal
**Standard**: Return list of values
**Meta Variations**:
- Return nodes at specific depth only
- Return path from root to node
- Return all paths that sum to target
- In-place modification (no new structures)

---

### Pattern 3: Graphs (Heavy Meta Focus)

#### Number of Islands (LC200)
**Standard**: Count islands in grid
**Meta Variations**:
- Return coordinates of all islands
- Find the LARGEST island
- Count islands, but diagonal connections count
- Find minimum cells to flip to connect all islands

#### Clone Graph (LC133)
**Standard**: Deep copy a graph
**Meta Variations**:
- Handle graphs with cycles
- Clone only nodes within K distance
- Return the node that has most connections

---

### Pattern 4: Strings

#### Valid Palindrome (LC125)
**Standard**: Ignore non-alphanumeric
**Meta Variations**:
- Allow at most K character removals
- Count minimum removals needed
- Find longest palindromic substring within

#### Longest Substring Without Repeating (LC3)
**Standard**: Return length
**Meta Variations**:
- Return the actual substring
- Return ALL substrings of maximum length
- Allow at most K repeats per character

---

## Meta Interview Format Specifics

### What Meta Says (Recruiter Info)
- Focus on: Trees, Graphs, Strings
- NO dynamic programming questions
- Heavy emphasis on communication
- Usually 1-2 problems per 45 minutes

### Typical Problem Difficulty
| Round | Difficulty | Count |
|-------|-----------|-------|
| Phone Screen | 1 Easy or 1 Medium | 1 |
| Onsite R1-R2 | Medium to Medium-Hard | 2 |

---

## Example Meta-Style Problems

### Example 1: URL Content Grouping (YOUR INTERVIEW)

**Standard Version (LC49-like)**:
```python
# Group URLs by content
urls = {"a.com": "<html>a</html>", "b.com": "<html>a</html>"}
# Output: {"a.com": ["b.com"]}  # Any representative is fine
```

**Meta Twist Applied**:
```python
# Group URLs by content
# BUT: Choose lexicographically smallest URL as representative
# AND: Sort grouped URLs lexicographically
urls = {"z.com": "<html>a</html>", "a.com": "<html>a</html>", "m.com": "<html>a</html>"}
# Output: {"a.com": ["m.com", "z.com"]}  # a.com is lex smallest, values sorted
```

### Example 2: Meeting Rooms

**Standard (LC253)**:
```python
# Find minimum rooms needed
intervals = [[0,30],[5,10],[15,20]]
# Output: 2
```

**Meta Twist**:
```python
# Find minimum rooms AND return which meetings are in which room
intervals = [[0,30],[5,10],[15,20]]
# Output: (2, [[0], [1, 2]])  # Room 0 has meeting 0, Room 1 has meetings 1,2
```

### Example 3: Valid Parentheses

**Standard (LC20)**:
```python
# Return True/False if valid
s = "()[]{}"
# Output: True
```

**Meta Twist**:
```python
# Return the INDEX of first invalid bracket, or -1 if valid
s = "([)]"
# Output: 2  # The ] at index 2 is the first invalid character
```

### Example 4: Merge Intervals

**Standard (LC56)**:
```python
# Merge overlapping intervals
intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
```

**Meta Twist**:
```python
# Merge overlapping intervals
# ALSO return how many original intervals each merged interval contains
intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [([1,6], 2), ([8,10], 1), ([15,18], 1)]
```

---

## Common Meta Interview Patterns

### Pattern Recognition
When you see these in Meta interviews:

| Problem Theme | Likely Pattern | Common Twist |
|--------------|----------------|--------------|
| Tree traversal | BFS/DFS | Return specific format |
| Finding groups | DSU/DFS | Return representative selection |
| Interval problems | Sorting + greedy | Additional output info |
| String matching | Sliding window | All matches, not just one |
| Graph connectivity | BFS/DFS | Path/distance info |

---

## Preparation Strategy for Meta

### 1. Master the Standard Problem First
Solve the base LeetCode problem until you can do it quickly and bug-free.

### 2. Think About Variations
After solving, ask yourself:
- What if I needed to return all answers?
- What if I needed specific ordering?
- What if I had space constraints?
- What if input was streaming?

### 3. Practice Output Formatting
Many bugs come from incorrect output format. Practice:
- Sorting results correctly
- Handling tie-breakers
- Returning appropriate data types

### 4. Prepare for Follow-ups
Have answers ready for:
- "How would you scale this?"
- "What's the time/space complexity?"
- "Can you optimize further?"

---

## Quick Reference: Standard to Meta Twist

| Standard Problem | Common Meta Twist |
|-----------------|-------------------|
| Return any valid | Return lexicographically smallest |
| Return count | Return actual elements |
| O(n) space | O(1) space required |
| Return boolean | Return index/position of failure |
| Find one | Find all |
| Any order | Specific sorted order |
| Tree with 2 nodes | Tree with K nodes |
| Fixed input | Streaming input |
| Single call | Design for multiple calls |

---

## Interview Tips for Meta Variations

1. **Clarify output format FIRST** - Ask exactly what format they want
2. **Ask about edge cases** - Empty input, single element, all same
3. **Confirm sorting requirements** - Ascending/descending, tie-breakers
4. **Handle all cases** - Meta tests edge cases thoroughly
5. **Optimize proactively** - Mention better approaches even if not required
6. **Communicate clearly** - Meta values clear explanation as much as code
