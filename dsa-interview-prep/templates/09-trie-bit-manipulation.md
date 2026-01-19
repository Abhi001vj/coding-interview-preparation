# Trie & Bit Manipulation

## Introduction

This template covers two related patterns: Tries (prefix trees) for string operations and Bit Tries for XOR optimization. A Trie efficiently stores and searches strings by prefix, while a Bit Trie processes numbers bit-by-bit to optimize XOR operations.

---

# Part 1: String Trie

## Pattern Recognition - String Trie

Use this pattern when you see:
- "Prefix search" / "Autocomplete"
- "Word dictionary with wildcards"
- "Count words with common prefix"
- "Longest common prefix"
- "Word break" problems

## Base Template - String Trie

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # Optional: count words ending here


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.count += 1

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

---

## LeetCode Problems - String Trie

### Problem 1: LC 208 - Implement Trie

**Link:** [https://leetcode.com/problems/implement-trie-prefix-tree/](https://leetcode.com/problems/implement-trie-prefix-tree/)

**Problem:** Implement insert, search, startsWith.

```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True  # End marker

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '$' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
```

**Complexity:** O(m) for all operations where m = word length

---

### Problem 2: LC 211 - Design Add and Search Words

**Link:** [https://leetcode.com/problems/design-add-and-search-words-data-structure/](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

**Problem:** Search with '.' wildcard matching any character.

**Pattern:** Trie + DFS for wildcard

```python
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '$' in node

            char = word[i]
            if char == '.':
                # Try all children
                for child in node:
                    if child != '$' and dfs(node[child], i + 1):
                        return True
                return False
            else:
                if char not in node:
                    return False
                return dfs(node[char], i + 1)

        return dfs(self.root, 0)
```

**Complexity:** O(m) insert, O(26^m) worst case search with all dots

---

### Problem 3: LC 212 - Word Search II

**Link:** [https://leetcode.com/problems/word-search-ii/](https://leetcode.com/problems/word-search-ii/)

**Problem:** Find all words from dictionary in grid.

**Pattern:** Trie + Grid DFS

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = {}
        for word in words:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word  # Store word at end

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node:
                return

            next_node = node[char]

            # Found a word
            if '$' in next_node:
                result.append(next_node['$'])
                del next_node['$']  # Avoid duplicates

            # Mark visited
            board[r][c] = '#'

            # Explore neighbors
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            # Restore
            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
```

**Complexity:** O(m * n * 4^L) where L = max word length

---

### Problem 4: LC 720 - Longest Word in Dictionary

**Link:** [https://leetcode.com/problems/longest-word-in-dictionary/](https://leetcode.com/problems/longest-word-in-dictionary/)

**Problem:** Find longest word that can be built one character at a time.

**Pattern:** Trie + BFS/DFS

```python
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Build Trie
        root = {}
        for word in words:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word

        # BFS to find longest buildable word
        result = ""
        stack = [root]

        while stack:
            node = stack.pop()
            for key in node:
                if key != '$' and '$' in node[key]:
                    # This prefix forms a valid word
                    word = node[key]['$']
                    if len(word) > len(result) or (len(word) == len(result) and word < result):
                        result = word
                    stack.append(node[key])

        return result
```

**Complexity:** O(sum of word lengths)

---

# Part 2: Bit Trie (XOR Optimization)

## Pattern Recognition - Bit Trie

Use this pattern when you see:
- "Maximum XOR of two numbers"
- "XOR queries on array"
- "Count pairs with XOR in range"
- Need to optimize bit-by-bit decisions

## Base Template - Bit Trie

```python
class BitTrie:
    def __init__(self, max_bits=31):
        self.root = {}
        self.max_bits = max_bits

    def insert(self, num: int) -> None:
        node = self.root
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def find_max_xor(self, num: int) -> int:
        """Find number in trie that gives max XOR with num."""
        node = self.root
        result = 0

        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit  # Want opposite for max XOR

            if want in node:
                result |= (1 << i)
                node = node[want]
            elif bit in node:
                node = node[bit]
            else:
                break

        return result
```

---

## LeetCode Problems - Bit Trie

### Problem 5: LC 421 - Maximum XOR of Two Numbers

**Link:** [https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

**Problem:** Find maximum XOR of any two numbers in array.

**Pattern:** Bit Trie - for each number, find best XOR partner

```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Determine max bits needed
        max_num = max(nums)
        max_bits = max_num.bit_length() if max_num else 0

        # Build trie and find max XOR
        root = {}
        max_xor = 0

        for num in nums:
            # Insert num into trie
            node = root
            for i in range(max_bits - 1, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        for num in nums:
            # Find max XOR for this num
            node = root
            curr_xor = 0

            for i in range(max_bits - 1, -1, -1):
                bit = (num >> i) & 1
                want = 1 - bit

                if want in node:
                    curr_xor |= (1 << i)
                    node = node[want]
                else:
                    node = node[bit]

            max_xor = max(max_xor, curr_xor)

        return max_xor
```

**Complexity:** O(n * 32)

---

### Problem 6: LC 1707 - Maximum XOR With Element From Array

**Link:** [https://leetcode.com/problems/maximum-xor-with-an-element-from-array/](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

**Problem:** For each query (xi, mi), find max XOR with nums[j] where nums[j] <= mi.

**Pattern:** Offline queries + sort + incremental trie

```python
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        # Add query index for result placement
        indexed_queries = [(x, m, i) for i, (x, m) in enumerate(queries)]
        indexed_queries.sort(key=lambda q: q[1])  # Sort by m

        root = {}
        result = [-1] * len(queries)
        num_idx = 0

        def insert(num):
            node = root
            for i in range(29, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        def find_max_xor(num):
            if not root:
                return -1
            node = root
            xor_val = 0
            for i in range(29, -1, -1):
                bit = (num >> i) & 1
                want = 1 - bit
                if want in node:
                    xor_val |= (1 << i)
                    node = node[want]
                elif bit in node:
                    node = node[bit]
                else:
                    return -1
            return xor_val

        for x, m, idx in indexed_queries:
            # Add all valid numbers to trie
            while num_idx < len(nums) and nums[num_idx] <= m:
                insert(nums[num_idx])
                num_idx += 1

            result[idx] = find_max_xor(x)

        return result
```

**Complexity:** O(n log n + q log q + (n + q) * 30)

---

### Problem 7: LC 1938 - Maximum Genetic Difference Query

**Link:** [https://leetcode.com/problems/maximum-genetic-difference-query/](https://leetcode.com/problems/maximum-genetic-difference-query/)

**Problem:** For each node in tree, find max XOR with any ancestor.

**Pattern:** DFS with trie insert/remove

```python
class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)

        # Build tree
        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        # Group queries by node
        query_map = [[] for _ in range(n)]
        for idx, (node, val) in enumerate(queries):
            query_map[node].append((val, idx))

        result = [0] * len(queries)
        trie = {}
        count = {}  # Count nodes at each trie position

        def insert(num):
            node = trie
            for i in range(17, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                key = (id(node), bit)
                count[key] = count.get(key, 0) + 1
                node = node[bit]

        def remove(num):
            node = trie
            for i in range(17, -1, -1):
                bit = (num >> i) & 1
                key = (id(node), bit)
                count[key] -= 1
                if count[key] == 0:
                    del node[bit]
                    return
                node = node[bit]

        def query(num):
            node = trie
            res = 0
            for i in range(17, -1, -1):
                bit = (num >> i) & 1
                want = 1 - bit
                key = (id(node), want)
                if count.get(key, 0) > 0:
                    res |= (1 << i)
                    node = node[want]
                else:
                    node = node[bit]
            return res

        def dfs(u):
            insert(u)

            for val, idx in query_map[u]:
                result[idx] = query(val)

            for v in children[u]:
                dfs(v)

            remove(u)

        dfs(root)
        return result
```

**Complexity:** O((n + q) * 18)

---

# Part 3: Common Bit Manipulation Tricks

## Essential Bit Operations

```python
# Check if bit is set
def is_bit_set(num, i):
    return (num >> i) & 1

# Set bit
def set_bit(num, i):
    return num | (1 << i)

# Clear bit
def clear_bit(num, i):
    return num & ~(1 << i)

# Toggle bit
def toggle_bit(num, i):
    return num ^ (1 << i)

# Count set bits
def count_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count
# Or use: bin(num).count('1')

# Lowest set bit
def lowest_set_bit(num):
    return num & (-num)

# Clear lowest set bit
def clear_lowest_bit(num):
    return num & (num - 1)

# Check if power of 2
def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0
```

---

### Problem 8: LC 136 - Single Number

**Link:** [https://leetcode.com/problems/single-number/](https://leetcode.com/problems/single-number/)

**Problem:** Find the number that appears once (others appear twice).

**Pattern:** XOR all numbers

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
```

**Complexity:** O(n)

---

### Problem 9: LC 137 - Single Number II

**Link:** [https://leetcode.com/problems/single-number-ii/](https://leetcode.com/problems/single-number-ii/)

**Problem:** Find the number that appears once (others appear three times).

**Pattern:** Count bits modulo 3

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            bit_sum = sum((num >> i) & 1 for num in nums)
            if bit_sum % 3:
                result |= (1 << i)

        # Handle negative numbers
        if result >= 2**31:
            result -= 2**32

        return result
```

**Complexity:** O(32n) = O(n)

---

### Problem 10: LC 260 - Single Number III

**Link:** [https://leetcode.com/problems/single-number-iii/](https://leetcode.com/problems/single-number-iii/)

**Problem:** Find two numbers that appear once (others appear twice).

**Pattern:** XOR to find difference, split by differing bit

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # XOR all = a ^ b (the two unique numbers)
        xor_all = 0
        for num in nums:
            xor_all ^= num

        # Find a bit where a and b differ
        diff_bit = xor_all & (-xor_all)

        # Split numbers into two groups
        a = b = 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
```

**Complexity:** O(n)

---

## Common Mistakes

1. **Wrong bit range in Bit Trie**
   - Check max value to determine bits needed
   - Usually 30-31 bits for positive integers

2. **Forgetting to handle negative XOR**
   - Python integers are unbounded
   - May need `if result >= 2**31: result -= 2**32`

3. **Off-by-one in bit iteration**
   - MSB first: `range(max_bits - 1, -1, -1)`
   - LSB first: `range(max_bits)`

4. **Not using bit_length()**
   - `max_num.bit_length()` gives minimum bits needed

5. **String Trie: forgetting end marker**
   - Use `'$'` or `is_end` flag

---

## Practice Checklist

### String Trie
- [ ] LC 208 - Implement Trie (Basic)
- [ ] LC 211 - Add and Search Words (Wildcard)
- [ ] LC 212 - Word Search II (Grid + Trie)
- [ ] LC 720 - Longest Word in Dictionary

### Bit Trie / XOR
- [ ] LC 421 - Maximum XOR of Two Numbers
- [ ] LC 1707 - Maximum XOR With Element
- [ ] LC 1938 - Maximum Genetic Difference

### Bit Manipulation
- [ ] LC 136 - Single Number (XOR basics)
- [ ] LC 137 - Single Number II (Bit counting)
- [ ] LC 260 - Single Number III (Two unique)
- [ ] LC 191 - Number of 1 Bits
- [ ] LC 338 - Counting Bits
