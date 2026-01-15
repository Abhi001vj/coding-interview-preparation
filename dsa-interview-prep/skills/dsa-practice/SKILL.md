# DSA Practice Skill

## Overview
This skill provides structured DSA practice for Google/Meta interview preparation, tailored to address specific weaknesses identified in previous interviews.

## Commands

### `/practice [options]`
Generate a practice problem based on weak areas.

**Options:**
- `--pattern <name>` - Specific pattern (sliding-window, dsu, dp, etc.)
- `--difficulty <level>` - easy, medium, hard
- `--time <minutes>` - Set timer (default: 25 for medium)
- `--random` - Random from weak patterns

**Examples:**
```
/practice --pattern sliding-window --difficulty medium
/practice --random --time 20
/practice --pattern dsu
```

### `/mock [options]`
Start a timed mock interview session.

**Options:**
- `--company <name>` - google, meta (adjusts style)
- `--duration <minutes>` - Total time (default: 45)
- `--problems <count>` - Number of problems (default: 2)

**Examples:**
```
/mock --company google --duration 45
/mock --company meta --problems 2
```

### `/review`
Review your most recent solution for bugs and improvements.

**Triggers code review agent with:**
- Correctness verification
- Bug detection
- Complexity analysis
- Style suggestions

### `/explain <topic>`
Deep dive explanation of a concept or pattern.

**Topics:**
- Pattern names: `sliding-window`, `dsu`, `monotonic-stack`, etc.
- Concepts: `time-complexity`, `space-complexity`, `recursion`
- Problems: `LC###` or problem name

**Examples:**
```
/explain dsu
/explain LC721
/explain monotonic-stack
```

### `/hint`
Get a hint for the current problem without full solution.

**Hint levels:**
1. First hint: General approach direction
2. Second hint: Key data structure/technique
3. Third hint: Specific implementation detail

### `/solution`
Show optimal solution with full explanation (use after attempting).

### `/similar`
Find similar problems to the current one for more practice.

### `/stats`
Show practice statistics and progress.

---

## Workflow Integration

### Starting a Practice Session
```
User: /practice --pattern dsu --difficulty medium
Claude: [Presents problem, starts timer]

User: [Works on solution]
User: [Pastes code]
User: /review

Claude: [Runs reviewer agent, gives feedback]

User: /similar
Claude: [Lists related problems for reinforcement]
```

### Mock Interview Flow
```
User: /mock --company google
Claude: [Acts as interviewer agent]
Claude: [Presents Problem 1, tracks time]

User: [Solves problem, discusses]

Claude: [Presents Problem 2]

User: [Solves problem]

Claude: [Provides structured feedback with scores]
```

---

## Problem Selection Logic

### Priority Patterns (from CLAUDE.md)
1. **snapshot-versioning** - HistorySet, Snapshot Array
2. **union-find** - Accounts Merge, URL deduplication
3. **sliding-window** - Max Consecutive Ones III
4. **monotonic-stack** - Sum of Subarray Minimums

### Selection Algorithm
```python
def select_problem(pattern=None, difficulty="medium"):
    if pattern:
        problems = get_problems_by_pattern(pattern)
    else:
        # Weighted random from weak patterns
        weights = get_weakness_weights()
        pattern = weighted_random_choice(weights)
        problems = get_problems_by_pattern(pattern)

    # Filter by difficulty
    problems = filter_by_difficulty(problems, difficulty)

    # Prefer unsolved or failed problems
    problems = sort_by_priority(problems)

    return problems[0]
```

---

## Timer and Tracking

### Time Limits
| Difficulty | Warning | Cutoff |
|------------|---------|--------|
| Easy | 10 min | 15 min |
| Medium | 20 min | 25 min |
| Hard | 35 min | 45 min |

### Session Logging
Each problem attempt records:
- Problem ID and name
- Pattern/topic
- Time taken
- Result: solved/partial/failed
- Bugs found
- Notes

---

## Scoring Criteria

### Per-Problem Score (0-100)
- **Correctness** (40 points)
  - Works on examples: 15
  - Handles edge cases: 15
  - Bug-free: 10

- **Efficiency** (30 points)
  - Optimal time complexity: 15
  - Optimal space complexity: 10
  - Clean implementation: 5

- **Process** (30 points)
  - Asked clarifying questions: 5
  - Discussed approach before coding: 10
  - Communicated while coding: 10
  - Tested solution: 5

### Mock Interview Pass Threshold
- Minimum 70/100 average across problems
- No critical bugs in either problem
- Completed within time limit

---

## Integration with Reference Files

### patterns.md
Used for:
- Pattern recognition hints
- Template code suggestions
- Related problem recommendations

### common-bugs.md
Used for:
- Bug detection during review
- Warning about pattern-specific pitfalls
- Prevention tips

### problem-bank.md
Used for:
- Problem selection
- Difficulty calibration
- Progress tracking

---

## Adaptive Difficulty

### Difficulty Adjustment Rules
```
IF solved 3 consecutive problems < target_time:
    increase_difficulty()

IF failed 2 consecutive problems OR took > 2x target_time:
    decrease_difficulty()
    suggest_pattern_review()

IF same bug type appears 3+ times:
    add_to_bug_focus_list()
    show_bug_pattern_reminder()
```

---

## Session Templates

### Quick Practice (30 min)
1. Review one pattern (5 min)
2. Solve 1 medium problem (25 min)

### Standard Practice (1 hour)
1. Warm-up easy problem (10 min)
2. Main medium problem (25 min)
3. Review and optimization (15 min)
4. Log and plan tomorrow (10 min)

### Intensive Practice (2 hours)
1. Pattern deep-dive (20 min)
2. Problem 1 - medium (25 min)
3. Problem 2 - medium (25 min)
4. Problem 3 - medium/hard (35 min)
5. Review all solutions (15 min)

### Mock Interview (1 hour)
1. Full mock interview (45 min)
2. Detailed feedback review (15 min)
