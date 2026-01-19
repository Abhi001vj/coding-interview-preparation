# Problem Solution Template

## [Problem Number]. [Problem Title]
**Difficulty:** [Easy/Medium/Hard] | **Pattern:** [Pattern Name] | **Companies:** Google, Meta

---

## 1. Google/Meta Style Question Transformation

### Original LeetCode Problem:
[Brief description of the original problem]

### Google Scenario Wrapper:
> "At Google, we're building [realistic scenario]. You need to [transformed problem statement that hides the algorithm]..."

### Meta Constraint Twist:
> Same problem but: [Different constraint or output format variation]

---

## 2. Clarifying Questions (Ask in Interview!)

Before coding, always clarify:

1. **Input Constraints:**
   - What's the size range of the input? (n ≤ ?)
   - Can there be negative numbers/empty inputs/duplicates?
   - Is the input sorted/unsorted?

2. **Edge Cases:**
   - What should I return for empty input?
   - How to handle ties/duplicates?

3. **Output Requirements:**
   - Return indices or values?
   - Need to preserve order?
   - In-place modification allowed?

---

## 3. Pattern Recognition

### Why this pattern?
- **Key Signal 1:** [What in the problem indicates this pattern]
- **Key Signal 2:** [Another indicator]

### Pattern Match:
| Problem Feature | Pattern Indicator |
|-----------------|-------------------|
| [Feature] | [Why it points to this pattern] |

---

## 4. Approach Discussion

### Approach 1: [Name] - [Time] / [Space]
**Intuition:** [1-2 sentences on why this works]

**Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Pros:** [advantages]
**Cons:** [disadvantages]

### Approach 2: [Name] - [Time] / [Space] (Optimal)
**Intuition:** [1-2 sentences on why this works]

**Steps:**
1. [Step 1]
2. [Step 2]

---

## 5. Base Template

```python
# The base template for this pattern
def base_template(params):
    """
    Base template for [Pattern Name]
    """
    # Template code here
    pass
```

---

## 6. Solution - How We Modify the Template

### Template Modification Needed:
- **What changes:** [Specific modifications]
- **Why:** [Reasoning]

```python
# Full solution with detailed comments
class Solution:
    def solve(self, params):
        """
        [Brief description]

        Time: O(...)
        Space: O(...)
        """
        # Implementation with step-by-step comments
        pass
```

---

## 7. Complexity Analysis

### Time Complexity: O(...)
- [Breakdown of each operation]
- [Why this is optimal/not optimal]

### Space Complexity: O(...)
- [What takes space]
- [Can it be optimized?]

---

## 8. Test Cases & Edge Cases

```python
# Test Case 1: Basic example
Input: ...
Expected: ...
Trace: [step-by-step execution]

# Test Case 2: Edge case - empty/minimal
Input: ...
Expected: ...

# Test Case 3: Edge case - large/boundary
Input: ...
Expected: ...
```

---

## 9. Common Mistakes to Avoid

1. **[Mistake 1]:** [Description and how to avoid]
2. **[Mistake 2]:** [Description and how to avoid]
3. **[Mistake 3]:** [Description and how to avoid]

---

## 10. Follow-up Questions

### Follow-up 1: [Question]
**Answer:** [Brief solution approach]

### Follow-up 2: [Question]
**Answer:** [Brief solution approach]

### Related Problems:
- LC XXX - [Problem Name] (Similar because...)
- LC YYY - [Problem Name] (Builds on this by...)

---

## 11. Interview Tips

- **Time Target:** [X] minutes for this difficulty
- **Communication Points:** [What to say out loud]
- **Red Flags to Avoid:** [Common interview mistakes]
