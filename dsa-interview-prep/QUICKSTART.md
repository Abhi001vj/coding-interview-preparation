# DSA Interview Prep - Quick Start Guide

## Overview

This system is designed to help you pass Google and Meta coding interviews by addressing your specific weaknesses:
- Inefficient algorithms → Pattern recognition & optimization
- Buggy code → Structured verification
- Slow progress → Time-boxed practice
- Communication gaps → Talk-through training

---

## Daily Workflow

### Morning (30 min) - Pattern Review
```bash
cd dsa-interview-prep
# Review one pattern from references/patterns.md
# Memorize the template code
```

### Main Practice (2-3 hours) - Problem Solving
```bash
# Start a practice session
claude "Let's practice DSA. Give me a medium problem from my weak areas."

# Or run a mock interview
claude "Run a 45-minute mock interview for Google L5"
```

### Evening (15 min) - Review & Log
```bash
# Review today's problems, log progress
python skills/dsa-practice/scripts/tracker.py log
```

---

## Using Claude for Practice

### Start a Practice Session
```
You: "I want to practice sliding window problems"
Claude: [Gives problem, times you, reviews solution]
```

### Get a Random Problem
```
You: "Give me a random medium from my weak patterns"
Claude: [Selects from your priority areas in CLAUDE.md]
```

### Mock Interview Mode
```
You: "Run a mock Google interview - 45 minutes, 2 problems"
Claude: [Acts as interviewer, times strictly, gives feedback]
```

### Code Review
```
You: [Paste your solution]
You: "Review this for bugs and optimization"
Claude: [Points out issues, suggests improvements]
```

### Explain a Concept
```
You: "Explain Union-Find with the Accounts Merge problem"
Claude: [Deep dive with examples and variations]
```

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Your profile, weaknesses, rules |
| `agents/interviewer.md` | Mock interview persona |
| `agents/coach.md` | Teaching/explaining persona |
| `agents/reviewer.md` | Code review persona |
| `skills/dsa-practice/SKILL.md` | Practice skill definition |
| `references/patterns.md` | 12 algorithm patterns with templates |
| `references/common-bugs.md` | Bug patterns to avoid |
| `references/problem-bank.md` | 100+ curated problems |
| `assets/8-week-plan.md` | Structured study schedule |

---

## The 5-Step Problem-Solving Framework

Use this for EVERY problem:

### 1. STOP (2 min)
- Read problem twice
- Identify: input type, output type, constraints
- Ask clarifying questions

### 2. THINK (5 min)
- Draw example
- Identify pattern (see patterns.md)
- List 2-3 approaches with Big-O
- Choose best approach, justify

### 3. TALK (while coding)
- Explain each line as you write
- State assumptions
- Note potential edge cases

### 4. CODE (15-20 min)
- Write clean, readable code
- Use meaningful variable names
- Handle edge cases inline

### 5. TEST (5 min)
- Trace through with given example
- Try edge cases: empty, single element, duplicates
- Verify complexity matches analysis

---

## Time Targets

| Difficulty | Target Time | Max Time |
|------------|-------------|----------|
| Easy | 10 min | 15 min |
| Medium | 20 min | 25 min |
| Hard | 35 min | 45 min |

If you exceed max time, STOP and review the solution.

---

## Weekly Schedule Template

| Day | Focus | Problems |
|-----|-------|----------|
| Mon | Arrays/Strings | 3 medium |
| Tue | Trees/Graphs | 3 medium |
| Wed | DP/Recursion | 2-3 medium |
| Thu | Sliding Window/Two Pointers | 3 medium |
| Fri | Stack/Queue/Heap | 3 medium |
| Sat | Mock Interview | 4 problems (2 sessions) |
| Sun | Review weak areas | Re-solve failed problems |

---

## Progress Tracking

### Daily Log Format
```
Date: YYYY-MM-DD
Problems: [list with times]
Bugs: [what went wrong]
Learnings: [key insights]
```

### Weekly Review Questions
1. What patterns am I still slow on?
2. What bugs keep recurring?
3. Am I meeting time targets?
4. What topics need more practice?

---

## Emergency Quick Reference

### Forgot a Pattern?
→ Check `references/patterns.md`

### Keep Making Same Bug?
→ Check `references/common-bugs.md`

### Need Problem Ideas?
→ Check `references/problem-bank.md`

### Stuck on a Problem?
→ Set 5-min timer, if still stuck, look at hint/approach only

### Interview in X Days?
→ Follow `assets/8-week-plan.md` acceleration track

---

## Commands Cheat Sheet

```bash
# Generate a random problem
python skills/dsa-practice/scripts/generate_problem.py --difficulty medium --pattern sliding-window

# Log today's progress
python skills/dsa-practice/scripts/tracker.py log

# View weekly stats
python skills/dsa-practice/scripts/tracker.py stats --week

# Find problems by pattern
python skills/dsa-practice/scripts/tracker.py find --pattern dsu
```
