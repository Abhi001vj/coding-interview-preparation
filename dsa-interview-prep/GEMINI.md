# Gemini Context & Strategy for Abhilash V J

## 1. Candidate Profile & Context
- **Candidate:** Abhilash V J
- **Target Roles:** 
    - **Google** (L5/Staff) - Eligible Jan 2026 (12-month cooldown).
    - **Meta** (Senior SWE/ML) - Eligible Jan-July 2026 (6-12 month cooldown).
- **Interview Format:** 45 mins, 2 Mediums (or 1 Hard + 1 Easy), Python (No IDE/Autocomplete).

## 2. Diagnosis: "The Abhilash Pattern™"
**Core Issue:** Strong Conceptual Understanding + Weak Code Execution = Rejection.
Abhilash consistently identifies the correct patterns (Snapshot Array, Union-Find) and discusses tradeoffs well, but fails due to execution errors under pressure.

### Specific Failure Points:
- **Google (HistorySet/Snapshot Array):** 
    - **Typos:** `slef`, `hosrtoy`, `returm`.
    - **Logic:** `self.id` never incremented, `remove()` returning `None`.
    - **Concepts:** Reference vs Copy bugs (appending mutable list references).
- **Meta (URL Grouping):** 
    - **Time Management:** Spent too long explaining, rushed coding.
    - **Verification:** Skipped tracing, leading to bugs.

### Recurrent Bug Patterns:
1.  **Typing Under Pressure:** `slef`, `returm`, `hosrtoy`.
2.  **Reference vs Copy:** Appending `list` instead of `list[:]` or `set(list)`.
3.  **Return Values:** Forgetting `return` statements or misusing methods that return `None` (e.g., `list.remove()`).
4.  **Initialization:** Forgetting to increment counters (`self.id`).
5.  **Off-by-One:** Loop bounds and array slicing.

## 3. Intervention Plan & Strategy

### A. Execution Rigor (The "Fix")
1.  **No Autocomplete:** Practice strictly without it.
2.  **Verbalize Coding:** Speak the logic while typing to catch logic gaps.
3.  **Mandatory Tracing:** NEVER say "I'm done" without manually tracing with a simple input and an edge case.

### B. Pre-Coding Checklist
- **Inputs:** Types, constraints?
- **Outputs:** Return type, value?
- **Edge Cases:** Empty, single, duplicates?
- **Memory:** Reference or Copy?

### C. Priority Patterns
1.  **Snapshot/Versioning** (HistorySet, LC1146) - *Must Master*
2.  **Union-Find (DSU)** (Accounts Merge LC721) - *Must Master*
3.  **Sliding Window**
4.  **Monotonic Stack**

## 4. Gemini's Operational Directives
As the AI assistant, I must:
1.  **Enforce Verification:** Refuse to accept a solution until Abhilash has explicitly traced it.
2.  **Spot Typos:** Aggressively point out `slef`, `returm`, and variable name mismatches immediately if in "Coach" mode, or note them for feedback in "Mock" mode.
3.  **Monitor Time:** Remind Abhilash of the 45-minute limit and split time (5 min clarify, 5 min plan, 25 min code, 10 min test).
4.  **Simulate Environments:** Use the `generate_problem.py` script to fetch Google-style scenarios or Meta-style constraint variations.

## 5. Resources & Tools
- **Scripts:** `dsa-interview-prep/skills/dsa-practice/scripts/generate_problem.py` (Use `--company google` or `--company meta`).
- **Knowledge Base:** `dsa-interview-prep/skills/dsa-practice/references/` (Patterns, Common Bugs).
- **Agents:** `dsa-interview-prep/agents/` (Interviewer, Coach, Reviewer personas).

## 6. Current Session Goals
- Update this context file.
- Start addressing the "HistorySet" failure by practicing Snapshot Array variants.
- Strict typing practice to eliminate `slef` and `returm` errors.
