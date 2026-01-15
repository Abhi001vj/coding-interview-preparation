# DSA Interview Preparation - Claude Context

## Candidate Profile: Abhilash V J

### Target Companies
- **Google** (L5/Staff level) - 12-month cooldown from January 2025
- **Meta** (Senior SWE/ML) - 6-12 month cooldown from July 2025

### Interview Format Requirements
- **Duration**: 45 minutes per round
- **Problems**: 2 medium OR 1 hard + 1 easy
- **Target Time**: 15-20 min per medium, 10 min easy, 25-30 min hard
- **Language**: Python (preferred)
- **Environment**: Google Docs / CoderPad (NO IDE, NO autocomplete, NO compiler)

---

## Interview History & Detailed Feedback

### Google Interview (January 8, 2025) - FAILED

**Official Feedback:**
> "Your 2 rounds on DSA had good ideas but an inefficient algorithm, buggy codes and slow progress and unfortunately it became a negative round."

**Question Asked: HistorySet (Panda Trees Interview)**
```python
# Design a set that tracks history at each operation
hs = HistorySet()
id1 = hs.add("a")    # returns 1
id2 = hs.add("b")    # returns 2
id3 = hs.add("c")    # returns 3
id4 = hs.remove("c") # returns 4

hs.members(id3) → {"a", "b", "c"}
hs.members(id4) → {"a", "b"}
```

**Your Actual Code (With Bugs Marked):**
```python
class HistorySet:
   def __init__():           # ❌ Missing 'self'
        self.id = -1
        self.history = [[]]

def add(slef, val):          # ❌ 'slef' typo, wrong indentation
     current_his = []
      if self.id >=0:        # ❌ Inconsistent indentation
          current_his = self.history[self.id]
          if val in current_his:
              return slef.id  # ❌ 'slef' typo
      self.history.append(self.history[slef.id]+[val])
      returm self.id +1      # ❌ 'returm' typo, ID NEVER INCREMENTED!

  def remove(sel, val):      # ❌ 'sel' typo, wrong indentation
      if self.id <0:
                returen None  # ❌ 'returen' typo
      self.hosrtoy.append(self.history[slef.id].remove(val)  # ❌ .remove() returns None!
      return slef.id+1

def members(id):             # ❌ Missing 'self'
    return self.hosry[id]    # ❌ 'hosry' typo
```

**Critical Bugs Found (8 typos in ~20 lines!):**
1. `slef` → `self` (3 times)
2. `returm` → `return`
3. `hosrtoy` → `history`
4. `hosry` → `history`
5. `returen` → `return`
6. `sel` → `self`
7. `self.id` never incremented - fundamentally broken
8. `.remove()` returns None - would append None to history
9. Reference vs copy bug - not copying the set

**Pattern**: Snapshot/Versioning (LC1146 Snapshot Array)

---

### Meta Interview (June-July 2025) - FAILED

**Official Feedback:**
> "The coding and behavioral interviews weren't quite strong enough for an offer this time around."

**Question Asked: URL Content Grouping**
```python
# Group URLs with same content
{"a.com": "<html>a</html>", "d.com": "<html>a</html>"}
→ {"a.com": ["d.com"]}
```

**What You Did Well:**
- Correctly identified `defaultdict` for exact matches
- Recognized connection to Accounts Merge (LC721)
- Understood DSU for near-duplicate handling
- Discussed Jaccard similarity, MinHash/LSH for scaling

**What Went Wrong:**
- Took too long explaining approaches before coding
- Bugs in the actual implementation
- Didn't verify code thoroughly

**Pattern**: Hash Map Grouping / Union-Find (LC721 Accounts Merge)

---

### Meta Technical Screening Feedback
**Strengths Noted:**
- Strong foundation in Python & FastAPI
- Awareness of model trade-offs (keeping weights in memory, quantization)
- Understanding of LLM patterns (RAG, concurrency)
- Good grasp of Cloud & DevOps

**Areas for Improvement:**
- FastAPI: Need more specific patterns for cold start latency
- LLM Patterns: Need detailed examples for context window handling
- Coding test: Used deque for task scheduling but didn't explain cooling period constraint
- Infrastructure-as-Code: Terraform risks/benefits not explained deeply

---

## Root Cause Analysis: Why You're Failing

### The Abhilash Pattern™
```
Strong Conceptual Understanding + Weak Code Execution = Rejection
```

| Skill | Level | Evidence |
|-------|-------|----------|
| Problem Recognition | ✅ Strong | Identified Snapshot Array, Accounts Merge patterns |
| Algorithm Knowledge | ✅ Strong | Knew DSU, hashing, similarity algorithms |
| Approach Discussion | ✅ Strong | Discussed multiple solutions, tradeoffs |
| Code Writing | ❌ Weak | 8 typos, logic bugs in HistorySet |
| Time Management | ❌ Weak | "Slow progress" feedback |
| Verification | ❌ Weak | Bugs would be caught by tracing |

### Bug Pattern Categories

**1. Typing Under Pressure**
- You make typos when stressed (`slef`, `hosrtoy`)
- These aren't knowledge gaps - they're execution gaps
- **Fix:** Practice typing code without autocomplete daily

**2. Logic Gaps During Translation**
- You know `.remove()` returns None (you've used Python for years)
- Under pressure, you wrote `list.append(list.remove(x))`
- **Fix:** Verbalize what each line does as you write it

**3. No Verification Habit**
- `self.id` was never incremented - tracing once would catch this
- **Fix:** ALWAYS trace through code before saying "done"

**4. Speed vs Correctness Imbalance**
- You rush to write code, creating bugs
- Then spend time debugging instead of extending
- **Fix:** Write slower, verify faster

---

## Corrected HistorySet Implementation

```python
class HistorySet:
    def __init__(self):
        self.snapshots = [set()]  # snapshots[i] = set after operation i
        self.current = set()
        self.op_id = 0

    def add(self, val: str) -> int:
        """Add value and return operation ID."""
        if val in self.current:
            return self.op_id  # No change, return current ID

        self.current.add(val)
        self.snapshots.append(set(self.current))  # Deep copy!
        self.op_id += 1
        return self.op_id

    def remove(self, val: str) -> int:
        """Remove value and return operation ID."""
        if val not in self.current:
            return self.op_id  # No change

        self.current.discard(val)
        self.snapshots.append(set(self.current))  # Deep copy!
        self.op_id += 1
        return self.op_id

    def members(self, op_id: int = None) -> set:
        """Return set at given operation ID."""
        if op_id is None:
            return set(self.current)
        if 0 <= op_id < len(self.snapshots):
            return set(self.snapshots[op_id])
        raise ValueError(f"Invalid operation ID: {op_id}")
```

**Space-Optimized Version (What you discussed but couldn't implement):**
```python
class HistorySetOptimized:
    """Uses diff chain instead of full snapshots - O(n) space."""

    def __init__(self):
        self.history = []  # [(prev_id, action, value), ...]
        self.current = set()
        self.op_id = -1

    def add(self, val: str) -> int:
        if val in self.current:
            return self.op_id
        self.history.append((self.op_id, 'add', val))
        self.current.add(val)
        self.op_id += 1
        return self.op_id

    def remove(self, val: str) -> int:
        if val not in self.current:
            return self.op_id
        self.history.append((self.op_id, 'remove', val))
        self.current.discard(val)
        self.op_id += 1
        return self.op_id

    def members(self, op_id: int = None) -> set:
        if op_id is None or op_id == self.op_id:
            return set(self.current)

        # Reconstruct by replaying history
        ops = []
        curr = op_id
        while curr >= 0:
            prev, action, val = self.history[curr]
            ops.append((action, val))
            curr = prev

        result = set()
        for action, val in reversed(ops):
            if action == 'add':
                result.add(val)
            else:
                result.discard(val)
        return result
```

---

## Critical Weaknesses to Address

### 1. Algorithm Efficiency Gap
- **Symptom**: Jumping to first solution without considering alternatives
- **Root Cause**: Not spending enough time on problem analysis
- **Fix**: Always identify 2-3 approaches before coding, compare Big-O

### 2. Implementation Bugs
- **Your Common Bug Patterns**:
  - Typos under pressure (`slef`, `returm`, `hosrtoy`)
  - Off-by-one errors in loops/indices
  - Forgetting to handle empty/null inputs
  - Reference vs copy bugs (append reference instead of copy)
  - `.remove()` returns None - common Python gotcha
  - Variable never updated (self.id never incremented)
- **Fix**: Use structured verification checklist before submitting

### 3. Time Management
- **Current Pattern**:
  - Too long on problem understanding (>10 min)
  - Coding without clear plan
  - Not allocating time for testing
- **Target Time Allocation (45 min interview)**:
  - Clarification & examples: 5 min
  - Approach discussion: 5-7 min
  - Coding: 20-25 min
  - Testing & optimization: 8-10 min

### 4. Communication During Coding
- **Issue**: Going silent while coding
- **Fix**: Narrate every decision - "I'm using a hashmap here because..."

---

## Patterns That Need Most Practice

### High Priority (Failed in interviews)
1. **Snapshot/Version Control** - HistorySet, Snapshot Array (LC1146)
2. **Union-Find (DSU)** - Accounts Merge (LC721), URL grouping
3. **Sliding Window** - Max Consecutive Ones III, Fruit Into Baskets
4. **Stack-based** - Task Scheduler (LC621), monotonic stack problems

### Medium Priority (Slow/buggy)
5. **Binary Search variations** - Rotated arrays, answer binary search
6. **Graph traversal** - BFS/DFS with state
7. **Dynamic Programming** - House Robber variants, subsequence problems
8. **Two Pointers** - 3Sum, Container With Most Water

### Needs Speed Improvement
9. **Tree traversals** - All variants
10. **Heap/Priority Queue** - Kth largest, merge k lists
11. **Backtracking** - Permutations, combinations
12. **Prefix Sum** - Subarray sum problems

---

## Pre-Coding Checklist (USE EVERY TIME)

### Before Writing ANY Code
```
□ Turn OFF autocomplete
□ Set timer visible
□ Have scratch paper ready
□ Say out loud: "Clarify → Approach → Code → Verify"
```

### Before EVERY Function
```
□ What are the inputs and their types?
□ What should I return?
□ What are the edge cases? (empty, single, duplicates, negative)
□ Am I copying or referencing?
```

### After Writing Code
```
□ Trace with simple input
□ Trace with edge case
□ Check EVERY variable initialization
□ Check EVERY return statement
□ Check if IDs/counters are incremented
□ Spell check: self, return, history
```

---

## Success Metrics

### Short-term (Weekly)
- [ ] Solve 15+ problems per week
- [ ] <25 min average for medium problems
- [ ] <3 bugs per problem before submission
- [ ] Zero typos in code

### Medium-term (8 weeks)
- [ ] Complete 100 curated problems
- [ ] All 12 patterns mastered with templates memorized
- [ ] 5+ mock interviews with passing scores
- [ ] Can solve HistorySet in 15 min with 0 bugs

### Long-term (Interview Ready)
- [ ] Solve 2 mediums in 45 min consistently
- [ ] Zero-bug first submissions 80%+ of time
- [ ] Clear communication throughout (recorded and reviewed)
- [ ] Pass 3 consecutive mock interviews

---

## Interview Style Differences

### Google Style
- **Wraps problems in practical scenarios**
- Example: "Design a version control system for a set" instead of "Snapshot Array"
- Expects you to ask clarifying questions
- Values elegant, optimal solutions
- Will ask follow-up optimizations

### Meta Style
- **Twists output format or constraints**
- Example: Standard LC problem but "return indices sorted in reverse"
- No dynamic programming questions (per recruiter)
- Heavy focus on: Trees, Graphs, Strings
- Values clean code and communication

---

## Session Commands

When working with Claude on DSA practice:

- `/practice [topic]` - Get a problem from weak areas
- `/review` - Review last solution for bugs and improvements
- `/mock` - Start a timed mock interview
- `/explain [concept]` - Deep dive on a pattern/algorithm
- `/debug` - Help find bugs in current solution
- `/google` - Practice with Google-style scenario wrapping
- `/meta` - Practice with Meta-style constraint variations

---

## Files in This Repository

```
dsa-interview-prep/
├── CLAUDE.md                         # This file (context)
├── QUICKSTART.md                     # How to use everything
├── .claude/settings.json             # Claude CLI settings
├── agents/
│   ├── interviewer.md                # Mock interviewer agent
│   ├── coach.md                      # DSA coach agent
│   └── reviewer.md                   # Code review agent
├── skills/dsa-practice/
│   ├── SKILL.md                      # Practice skill definition
│   ├── scripts/
│   │   ├── generate_problem.py       # Problem generator
│   │   └── tracker.py                # Progress tracker
│   └── references/
│       ├── patterns.md               # 12 algorithm patterns
│       ├── complexity-cheatsheet.md  # Big O reference
│       ├── common-bugs.md            # Bug patterns to avoid
│       ├── problem-bank.md           # 600+ curated problems
│       ├── google-scenarios.md       # Google scenario wrappers
│       └── meta-variations.md        # Meta constraint twists
└── assets/
    ├── 8-week-plan.md                # Structured study plan
    └── practice-session-template.md   # Session tracking
```
