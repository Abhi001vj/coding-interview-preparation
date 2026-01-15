# DSA Interview Prep - Session Memory

## Last Updated: January 6, 2026

---

## Candidate Profile: Abhilash V J

### Target Companies & Timeline
- **Google** (L5/Staff) - 12-month cooldown from January 2025 → eligible January 2026
- **Meta** (Senior SWE/ML) - 6-12 month cooldown from July 2025 → eligible January-July 2026

### Interview Format
- 45 minutes per round
- 2 medium problems OR 1 hard + 1 easy
- Python preferred
- NO IDE, NO autocomplete (Google Docs / CoderPad)

---

## Interview History & Failures

### Google Interview - January 8, 2025 - FAILED
**Feedback**: "good ideas but inefficient algorithm, buggy codes and slow progress"

**Question**: HistorySet (Snapshot/Versioning pattern)
```python
# Design a set that tracks history at each operation
hs = HistorySet()
id1 = hs.add("a")    # returns 1
hs.members(id3) → {"a", "b", "c"}
```

**Bugs Made (8 typos in ~20 lines)**:
1. `slef` → `self` (3 times)
2. `returm` → `return`
3. `hosrtoy` → `history`
4. `hosry` → `history`
5. `returen` → `return`
6. `sel` → `self`
7. `self.id` never incremented - fundamentally broken
8. `.remove()` returns None - would append None to history
9. Reference vs copy bug - not copying the set

**Pattern**: LC1146 Snapshot Array

---

### Meta Interview - June/July 2025 - FAILED
**Feedback**: "coding and behavioral interviews weren't quite strong enough"

**Question**: URL Content Grouping
```python
# Group URLs with same content
{"a.com": "<html>a</html>", "d.com": "<html>a</html>"}
→ {"a.com": ["d.com"]}
```

**What Went Wrong**:
- Took too long explaining approaches before coding
- Bugs in actual implementation
- Didn't verify code thoroughly

**Pattern**: LC721 Accounts Merge / Hash Map Grouping

---

## The Abhilash Pattern™
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

---

## Files in This Repository

### Core Files
| File | Purpose |
|------|---------|
| `CLAUDE.md` | Main context file with interview history, bugs, patterns |
| `QUICKSTART.md` | How to use the system |
| `MEMORY.md` | This file - session memory for resuming |

### Agents (`agents/`)
| File | Purpose |
|------|---------|
| `interviewer.md` | Mock interviewer with actual interview questions, bug tracking |
| `coach.md` | DSA coaching agent |
| `reviewer.md` | Code review agent |

### Skills (`skills/dsa-practice/`)
| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition for `/practice` command |
| `scripts/generate_problem.py` | Problem generator with `--company google|meta` support |
| `scripts/tracker.py` | Progress tracking |

### References (`skills/dsa-practice/references/`)
| File | Purpose |
|------|---------|
| `problem-bank.md` | 600+ problems organized by pattern, difficulty, company |
| `patterns.md` | 12 algorithm patterns with templates |
| `common-bugs.md` | Bug patterns to avoid (includes Abhilash's specific bugs) |
| `complexity-cheatsheet.md` | Big O reference |
| `google-scenarios.md` | **NEW** - How Google wraps problems in scenarios |
| `meta-variations.md` | **NEW** - How Meta modifies constraints/output |

### Assets (`assets/`)
| File | Purpose |
|------|---------|
| `8-week-plan.md` | Structured study plan |
| `practice-session-template.md` | Session tracking template |

---

## Company-Specific Styles

### Google Style
- Wraps problems in practical scenarios (Google Docs, YouTube, Maps, etc.)
- Example: "Design version control for Google Docs" = Snapshot Array
- Expects clarifying questions
- Values elegant, optimal solutions
- Will ask follow-up optimizations

### Meta Style
- Same LeetCode problems with constraint/output modifications
- Example: "Return ALL pairs, sorted" instead of "return any pair"
- Focus on: Trees, Graphs, Strings
- NO dynamic programming questions
- Heavy emphasis on communication

---

## Priority Patterns to Master

### Highest Priority (Failed in interviews)
1. **Snapshot/Versioning** - HistorySet, LC1146
2. **Union-Find (DSU)** - Accounts Merge LC721, URL grouping

### High Priority (Weak areas)
3. Sliding Window
4. Monotonic Stack
5. Binary Search variations
6. Graph BFS/DFS

### Medium Priority
7. Dynamic Programming (Google only - Meta doesn't ask)
8. Two Pointers
9. Tree traversals (Meta emphasis)
10. Heap/Priority Queue

---

## Key Commands

### Generate Problems
```bash
# Random problem weighted by weakness
python scripts/generate_problem.py

# Google-style with scenario wrapper
python scripts/generate_problem.py --company google

# Meta-style with constraint variation
python scripts/generate_problem.py --company meta

# Specific pattern
python scripts/generate_problem.py --pattern union-find -d medium

# List all patterns
python scripts/generate_problem.py --list-patterns

# List company-specific problems
python scripts/generate_problem.py --list-company google
```

### Session Commands (when using with Claude)
- `/practice [topic]` - Get a problem from weak areas
- `/review` - Review last solution for bugs
- `/mock` - Start timed mock interview
- `/google` - Practice with Google-style scenarios
- `/meta` - Practice with Meta-style variations

---

## Pre-Coding Checklist (CRITICAL)

### Before Writing ANY Code
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

### Target Goals
- [ ] Solve 2 mediums in 45 min consistently
- [ ] Zero-bug first submissions 80%+ of time
- [ ] <25 min average for medium problems
- [ ] <3 bugs per problem before submission
- [ ] Zero typos in code

### Progress Tracking
| Week | Problems | Avg Time | Bug-Free Rate | Mock Pass |
|------|----------|----------|---------------|-----------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

---

## What Was Completed This Session

1. ✅ Created `google-scenarios.md` - Google scenario wrapper guide
2. ✅ Created `meta-variations.md` - Meta constraint variation guide
3. ✅ Updated `generate_problem.py` with:
   - `--company google|meta` flag
   - `--list-company` flag
   - Google scenario display
   - Meta variation display
   - Company tags on all problems
4. ✅ Updated `interviewer.md` with:
   - Actual interview questions (HistorySet, URL Grouping)
   - Expected solutions
   - "Watch For These Bugs" section
   - Google-style problems (G1-G5)
   - Meta-style problems (M1-M5)
   - Candidate-specific bug tracking

---

## Next Steps for Future Sessions

1. **Start Practice**: Run `python scripts/generate_problem.py --company google` to begin
2. **Master Priority 0**: Solve HistorySet and URL Content Grouping until bug-free in <15 min
3. **Weekly Mocks**: Use `interviewer.md` for mock interviews
4. **Track Progress**: Update the progress table above after each session
5. **Bug Journal**: Keep track of new bugs found to add to `common-bugs.md`

---

## Notes for Claude

When resuming this project:
1. Read `CLAUDE.md` first for full context
2. Check this `MEMORY.md` for session state
3. Candidate's main weakness is **code execution under pressure** (typos, logic bugs)
4. Conceptual understanding is strong - don't over-explain algorithms
5. Focus on **verification habits** and **typing accuracy**
6. Always remind to trace through code line-by-line before submitting
