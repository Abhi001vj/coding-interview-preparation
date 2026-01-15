# Common Bug Patterns & Prevention

## Overview

Based on interview feedback and practice sessions, these are the most common bugs that cause interview failures. Study each pattern, understand WHY it happens, and internalize the prevention strategy.

---

## Bug Category 1: Off-by-One Errors

### Symptom
- Index out of bounds
- Missing first/last element
- Infinite loops

### Common Causes

#### Loop Bounds
```python
# BUG: Accessing arr[i+1] when i can be n-1
for i in range(len(arr)):
    if arr[i] < arr[i+1]:  # IndexError!
        ...

# FIX: Stop one element early
for i in range(len(arr) - 1):
    if arr[i] < arr[i+1]:
        ...
```

#### Binary Search
```python
# BUG: Using wrong inequality
while left < right:  # vs while left <= right
    mid = (left + right) // 2
    if arr[mid] < target:
        left = mid      # BUG! Should be mid + 1
    else:
        right = mid - 1

# FIX: Be explicit about what left/right mean
# If searching for exact value:
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

#### Subarray/Substring Length
```python
# BUG: Wrong length calculation
length = end - start  # Off by one!

# FIX: Inclusive range
length = end - start + 1
```

### Prevention Checklist
- [ ] Check loop bounds: what happens at i=0 and i=n-1?
- [ ] Trace through with 1-element and 2-element arrays
- [ ] For binary search: write invariant comments

---

## Bug Category 2: Initialization Errors

### Symptom
- Wrong answer for first/last element
- Wrong answer for min/max

### Common Causes

#### Wrong Initial Value for Min/Max
```python
# BUG: Initializing min to 0
min_val = 0
for x in arr:
    min_val = min(min_val, x)  # Wrong if all elements > 0!

# FIX: Use infinity or first element
min_val = float('inf')
# or
min_val = arr[0]  # Make sure arr is non-empty first!
```

#### Forgetting to Initialize
```python
# BUG: Variable not initialized in all paths
if condition:
    result = compute()
return result  # NameError if condition is False!

# FIX: Initialize before conditionals
result = default_value
if condition:
    result = compute()
return result
```

#### Wrong Default for Hash Map
```python
# BUG: Assuming key exists
count[char] += 1  # KeyError if char not in count!

# FIX: Use get() with default
count[char] = count.get(char, 0) + 1

# Or use defaultdict
from collections import defaultdict
count = defaultdict(int)
count[char] += 1
```

### Prevention Checklist
- [ ] What should happen for empty input?
- [ ] What's the correct initial value for accumulator?
- [ ] Are all variables initialized before use?

---

## Bug Category 3: Reference vs Copy (THE HISTORYSET BUG!)

### Symptom
- Modifying one object changes others
- Snapshots show same data
- List/set mutations affect previous states

### Common Causes

#### Appending Reference Instead of Copy
```python
# BUG: This was the HistorySet bug!
self.history.append(current_set)  # Appends reference
current_set.add(x)  # Modifies ALL snapshots!

# FIX: Append a copy
self.history.append(set(current_set))  # Copy!
# or
self.history.append(current_set.copy())
```

#### Shallow vs Deep Copy
```python
# BUG: Shallow copy doesn't copy nested objects
matrix = [[1, 2], [3, 4]]
copy = matrix[:]  # Shallow copy
copy[0][0] = 99
print(matrix)  # [[99, 2], [3, 4]] - Original changed!

# FIX: Deep copy for nested structures
import copy
deep = copy.deepcopy(matrix)
```

#### Modifying Input
```python
# BUG: Modifying input array
def process(arr):
    arr.sort()  # Modifies caller's array!
    return arr[0]

# FIX: Work on copy if needed
def process(arr):
    sorted_arr = sorted(arr)  # Creates new array
    return sorted_arr[0]
```

### Prevention Checklist
- [ ] When storing for later, am I storing a reference or copy?
- [ ] Do I need shallow or deep copy?
- [ ] Am I modifying the input? Is that intended?

---

## Bug Category 4: Loop Mutation Bugs

### Symptom
- Elements skipped
- Infinite loop
- Index out of range during iteration

### Common Causes

#### Modifying List While Iterating
```python
# BUG: Removing while iterating
for item in my_list:
    if should_remove(item):
        my_list.remove(item)  # Skips elements!

# FIX: Iterate over copy or use list comprehension
for item in my_list[:]:  # Iterate over copy
    if should_remove(item):
        my_list.remove(item)

# Or better:
my_list = [item for item in my_list if not should_remove(item)]
```

#### Modifying Dict While Iterating
```python
# BUG: Adding/removing keys while iterating
for key in my_dict:
    if condition:
        del my_dict[key]  # RuntimeError!

# FIX: Iterate over copy of keys
for key in list(my_dict.keys()):
    if condition:
        del my_dict[key]
```

#### Wrong Loop Variable
```python
# BUG: Using outer loop variable in inner loop
for i in range(n):
    for j in range(m):
        result[i][j] = matrix[i][i]  # Should be [i][j]!

# BUG: Reusing variable name
for node in nodes:
    for node in node.children:  # Shadows outer 'node'!
        ...
```

### Prevention Checklist
- [ ] Am I modifying a collection while iterating?
- [ ] Are my loop variables uniquely named?
- [ ] Do nested loops use correct indices?

---

## Bug Category 5: Return Value Bugs

### Symptom
- Function returns None
- Wrong type returned
- Missing return in some paths

### Common Causes

#### Missing Return Statement
```python
# BUG: Forgot to return
def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    # Missing return!

# FIX: Always return
    return max_val
```

#### Return Inside Loop
```python
# BUG: Returning too early
def all_positive(arr):
    for x in arr:
        if x > 0:
            return True  # Wrong! Returns on first positive
        else:
            return False
    return True

# FIX: Think about logic
def all_positive(arr):
    for x in arr:
        if x <= 0:
            return False  # Found counter-example
    return True  # All passed
```

#### Wrong Return Type
```python
# BUG: Returning wrong type
def get_indices(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i  # Should return list!
    return -1  # Should return [] or None

# FIX: Be consistent with return type
def get_indices(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return [i]  # Consistent list return
    return []
```

### Prevention Checklist
- [ ] Does every code path return something?
- [ ] Is the return type consistent?
- [ ] Am I returning at the right point in loops?

---

## Bug Category 6: Integer Overflow / Division

### Symptom
- Wrong results for large numbers
- Unexpected float results

### Common Causes

#### Integer Division
```python
# BUG: Python 3 returns float
mid = (left + right) / 2  # Returns float!

# FIX: Use integer division
mid = (left + right) // 2

# Better: Avoid overflow
mid = left + (right - left) // 2
```

#### Modulo Operations
```python
# BUG: Negative number modulo
print(-1 % 3)  # Python: 2, but some languages: -1

# For consistent behavior across languages:
def mod(a, b):
    return ((a % b) + b) % b
```

### Prevention Checklist
- [ ] Am I using // for integer division?
- [ ] Can intermediate values overflow?
- [ ] How does modulo work with negatives?

---

## Bug Category 7: Boolean Logic Errors

### Symptom
- Condition always True/False
- Wrong branch taken

### Common Causes

#### De Morgan's Law Confusion
```python
# BUG: Wrong negation
if not (a and b):  # True when either is False
    ...

# vs
if not a and not b:  # True only when BOTH are False
    ...

# De Morgan's Laws:
# not (a and b) == (not a) or (not b)
# not (a or b) == (not a) and (not b)
```

#### Short-Circuit Evaluation
```python
# BUG: Second condition can error
if len(arr) > 0 and arr[0] > 5:  # OK
if arr[0] > 5 and len(arr) > 0:  # BUG! arr[0] checked first

# BUG: Side effect not executed
if False and expensive_function():  # Function never called!
```

#### Chained Comparisons
```python
# Python allows this (correct):
if 0 <= x <= 10:
    ...

# But be careful:
if a == b == c:  # True if all three equal
if a != b != c:  # NOT "all different"! a could equal c
```

### Prevention Checklist
- [ ] Write out truth table for complex conditions
- [ ] Check order of conditions for safety
- [ ] Be explicit with parentheses

---

## Bug Category 8: Edge Cases Not Handled

### Symptom
- Crashes on empty input
- Wrong result for single element
- Boundary conditions fail

### Must-Check Edge Cases

#### Arrays/Lists
- Empty: `[]`
- Single element: `[1]`
- Two elements: `[1, 2]`
- All same: `[5, 5, 5]`
- Already sorted
- Reverse sorted
- Contains duplicates
- Contains negative numbers
- Contains zero

#### Strings
- Empty: `""`
- Single char: `"a"`
- All same char: `"aaaa"`
- Spaces: `"   "`, `" a b "`
- Special chars if relevant

#### Numbers
- Zero
- Negative
- Max int value
- Min int value

#### Trees/Graphs
- Null/None root
- Single node
- Linear tree (all left or all right)
- Complete tree
- Disconnected graph

### Prevention Strategy
```python
def solution(arr):
    # Handle edge cases first
    if not arr:
        return []  # or appropriate default

    if len(arr) == 1:
        return arr[0]  # or appropriate handling

    # Main logic for arr with 2+ elements
    ...
```

---

## Pre-Submission Checklist

Before saying "I'm done", verify:

```
[ ] 1. Handles empty input
[ ] 2. Handles single element
[ ] 3. No off-by-one in loops
[ ] 4. All variables initialized
[ ] 5. Not mutating while iterating
[ ] 6. Correct return in all paths
[ ] 7. Reference vs copy correct
[ ] 8. Integer division used (// not /)
[ ] 9. Loop bounds correct
[ ] 10. Variable names unique (no shadowing)
```

---

## Debug Strategy

When you find a bug:

1. **Identify the symptom**: What's wrong with the output?
2. **Locate the bug**: Add print statements or trace manually
3. **Understand the cause**: WHY did this happen?
4. **Fix correctly**: Don't just patch, fix the root cause
5. **Verify the fix**: Test with the failing case
6. **Check for similar bugs**: Same mistake elsewhere?

### Trace Template
```python
def solution(arr):
    print(f"Input: {arr}")  # Add during debug
    for i, x in enumerate(arr):
        print(f"  i={i}, x={x}, state={state}")  # Track state
        ...
    print(f"Output: {result}")  # Verify output
    return result
```
