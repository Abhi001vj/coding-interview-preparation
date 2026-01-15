# Time & Space Complexity Cheatsheet

## Quick Reference Table

### Data Structure Operations

| Data Structure | Access | Search | Insert | Delete | Space |
|---------------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Dynamic Array | O(1) | O(n) | O(1)* | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Table | N/A | O(1)* | O(1)* | O(1)* | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| BST (worst) | O(n) | O(n) | O(n) | O(n) | O(n) |
| Heap | O(1)** | O(n) | O(log n) | O(log n) | O(n) |
| Trie | N/A | O(m) | O(m) | O(m) | O(n*m) |

*Amortized
**Getting min/max only

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |

---

## Common Complexity Classes

### O(1) - Constant
```python
# Array access
arr[i]

# Hash table operations
dict[key]
set.add(x)

# Stack/Queue operations
stack.append(x)
stack.pop()
```

### O(log n) - Logarithmic
```python
# Binary search
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    ...

# Balanced tree operations
# Heap operations (insert, extract)
```

### O(n) - Linear
```python
# Single loop
for x in arr:
    process(x)

# Two pointers
left, right = 0, n - 1
while left < right:
    ...

# Sliding window
for end in range(n):
    while condition:
        start += 1
```

### O(n log n) - Linearithmic
```python
# Sorting
arr.sort()

# Heap operations on n elements
for x in arr:
    heapq.heappush(heap, x)

# Divide and conquer
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
```

### O(n²) - Quadratic
```python
# Nested loops
for i in range(n):
    for j in range(n):
        process(i, j)

# Comparing all pairs
for i in range(n):
    for j in range(i + 1, n):
        compare(arr[i], arr[j])
```

### O(2^n) - Exponential
```python
# All subsets
def subsets(arr, idx, current):
    if idx == len(arr):
        result.append(current[:])
        return
    current.append(arr[idx])
    subsets(arr, idx + 1, current)
    current.pop()
    subsets(arr, idx + 1, current)

# Fibonacci (naive)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### O(n!) - Factorial
```python
# All permutations
def permute(arr, start):
    if start == len(arr):
        result.append(arr[:])
        return
    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        permute(arr, start + 1)
        arr[start], arr[i] = arr[i], arr[start]
```

---

## Pattern-Specific Complexities

### Sliding Window
- Time: O(n) - each element visited at most twice
- Space: O(k) where k is window size or unique chars

### Two Pointers
- Time: O(n) - pointers move through array once
- Space: O(1) - in-place

### Binary Search
- Time: O(log n) - halving search space
- Space: O(1) iterative, O(log n) recursive

### BFS/DFS on Graph
- Time: O(V + E) - visit each vertex and edge once
- Space: O(V) - queue/stack + visited set

### BFS/DFS on Grid
- Time: O(m × n) - visit each cell once
- Space: O(m × n) - worst case queue/stack size

### Dynamic Programming
- Time: O(states × transitions)
- Space: O(states) - can often optimize to O(1) or O(n)

### Union-Find
- Time: O(α(n)) per operation (nearly O(1))
- Space: O(n) for parent and rank arrays

### Backtracking
- Time: O(k^n) or O(n!) depending on problem
- Space: O(n) for recursion depth

---

## Complexity Analysis Tips

### Loop Analysis
```python
# O(n)
for i in range(n):
    O(1) operation

# O(n²)
for i in range(n):
    for j in range(n):
        O(1) operation

# O(n²) - but NOT always!
for i in range(n):
    for j in range(i, n):  # Still O(n²), sum = n(n-1)/2
        O(1) operation

# O(n) - NOT O(n²)!
while left < right:  # Two pointers
    if condition:
        left += 1
    else:
        right -= 1
```

### Amortized Analysis
```python
# Dynamic array append
# Individual worst case: O(n) when resize
# Amortized: O(1) per operation

# Example: doubling strategy
# n operations cost: O(1) + O(2) + O(4) + ... + O(n) = O(2n) = O(n)
# Per operation: O(1) amortized
```

### Space Complexity Rules
1. Input space usually not counted
2. Recursive call stack counts!
3. Auxiliary space = extra space used

```python
# O(1) space - in place
def reverse(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# O(n) space - new array
def reverse(arr):
    return arr[::-1]

# O(n) space - recursion stack
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

---

## Common Gotchas

### String Operations in Python
```python
# O(n) - NOT O(1)!
s = s + "a"  # Creates new string

# O(n²) in a loop!
result = ""
for char in string:
    result += char  # O(n²) total!

# O(n) - use list
chars = []
for char in string:
    chars.append(char)  # O(1) each
result = "".join(chars)  # O(n) once
```

### List Operations in Python
```python
# O(1) amortized
list.append(x)
list.pop()

# O(n) - shifts all elements!
list.insert(0, x)
list.pop(0)
del list[0]

# O(n) - use deque for O(1)
from collections import deque
d = deque()
d.appendleft(x)  # O(1)
d.popleft()      # O(1)
```

### Membership Testing
```python
# O(n) - list
if x in my_list:  # Linear search

# O(1) average - set/dict
if x in my_set:   # Hash lookup
if x in my_dict:
```

### Sorting with Key Function
```python
# O(n log n) for sort
# BUT key function called O(n) times
# If key is expensive, total is O(n log n + n × key_cost)

# Bad: O(n² log n) if computing something expensive
arr.sort(key=lambda x: expensive_computation(x))

# Good: precompute keys
keys = [(expensive_computation(x), x) for x in arr]  # O(n × key_cost)
keys.sort()  # O(n log n)
```

---

## Interview Complexity Checklist

Before stating complexity, verify:

1. **Time Complexity**
   - [ ] Counted all loops correctly
   - [ ] Accounted for nested loops
   - [ ] Checked for hidden O(n) operations (string concat, list.insert)
   - [ ] Considered amortized vs worst case

2. **Space Complexity**
   - [ ] Counted recursion stack
   - [ ] Counted auxiliary data structures
   - [ ] Mentioned if modifying input (in-place)

3. **State Clearly**
   - "Time complexity is O(n) where n is the length of the array"
   - "Space complexity is O(n) for the hash map, or O(1) if we don't count the output"
