
# Core Algorithm Patterns (1-5)

## 1. Prefix Sum Pattern
The prefix sum pattern involves preprocessing an array to create cumulative sums for efficient range queries.

### Implementation
```python
def build_prefix_sum(nums: List[int]) -> List[int]:
    """Creates prefix sum array for efficient range queries.
    
    Args:
        nums: Input array of integers
        
    Returns:
        Prefix sum array where prefix[i] = sum(nums[0:i])
        
    Time: O(n), Space: O(n)
    Example:
        >>> build_prefix_sum([1, 2, 3, 4])
        [0, 1, 3, 6, 10]  # Added 0 at start for easier queries
    """
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix

def range_sum(prefix: List[int], left: int, right: int) -> int:
    """Gets sum of range [left, right] inclusive.
    
    Args:
        prefix: Prefix sum array
        left: Start index (inclusive)
        right: End index (inclusive)
        
    Returns:
        Sum of elements from index left to right
    
    Time: O(1), Space: O(1)
    """
    return prefix[right + 1] - prefix[left]
```

### When to Use
- Range sum queries
- Finding subarrays with target sum
- Cumulative computations

### Example Problems
1. Range Sum Query - Immutable (LC #303)
2. Contiguous Array (LC #525)
3. Subarray Sum Equals K (LC #560)

## 2. Two Pointers Pattern
Two pointers technique involves using two pointers to traverse an array or list efficiently.

### Implementation
```python
def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    """Finds pair of numbers summing to target in sorted array.
    
    Args:
        nums: Sorted array of integers
        target: Target sum to find
        
    Returns:
        Indices of two numbers that sum to target
        
    Time: O(n), Space: O(1)
    Example:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    return []

def remove_duplicates(nums: List[int]) -> int:
    """Removes duplicates from sorted array in-place.
    
    Args:
        nums: Sorted array of integers
        
    Returns:
        Length of array after removing duplicates
        
    Time: O(n), Space: O(1)
    Example:
        >>> nums = [1, 1, 2, 2, 3]
        >>> k = remove_duplicates(nums)
        >>> nums[:k]
        [1, 2, 3]
    """
    if not nums:
        return 0
        
    write_pos = 1  # Position to write next unique element
    for read_pos in range(1, len(nums)):
        if nums[read_pos] != nums[read_pos - 1]:
            nums[write_pos] = nums[read_pos]
            write_pos += 1
            
    return write_pos
```

### When to Use
- Sorted arrays
- Finding pairs/triplets
- In-place array modifications

### Example Problems
1. Two Sum II (LC #167)
2. 3Sum (LC #15)
3. Container With Most Water (LC #11)

## 3. Sliding Window Pattern
Sliding window is used to process arrays/strings by maintaining a window that slides through the data.

### Implementation
```python
def max_sum_subarray(nums: List[int], k: int) -> int:
    """Finds maximum sum subarray of fixed size k.
    
    Args:
        nums: Array of integers
        k: Window size
        
    Returns:
        Maximum sum of any contiguous subarray of size k
        
    Time: O(n), Space: O(1)
    Example:
        >>> max_sum_subarray([1, 4, 2, 10, 2, 3, 1, 0, 20], 4)
        24  # Subarray [2, 10, 2, 3]
    """
    if not nums or k > len(nums):
        return 0
        
    # Calculate first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide window
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

def longest_substring_without_repeating(s: str) -> int:
    """Finds length of longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without duplicates
        
    Time: O(n), Space: O(min(m,n)) where m is charset size
    Example:
        >>> longest_substring_without_repeating("abcabcbb")
        3  # The substring "abc"
    """
    char_index = {}  # Last position of each char
    max_length = start = 0
    
    for end, char in enumerate(s):
        # If char in window, update start to skip duplicates
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        char_index[char] = end
        
    return max_length
```

### When to Use
- Subarray/substring problems
- Fixed or variable size windows
- Optimization over contiguous sequence

### Example Problems
1. Maximum Average Subarray I (LC #643)
2. Longest Substring Without Repeating Characters (LC #3)
3. Minimum Window Substring (LC #76)

## 4. Fast & Slow Pointers Pattern
Fast & slow pointers (Floyd's Tortoise and Hare) is used primarily for cycle detection.

### Implementation
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: Optional[ListNode]) -> bool:
    """Detects cycle in linked list using Floyd's algorithm.
    
    Args:
        head: Head of linked list
        
    Returns:
        True if cycle exists, False otherwise
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
        
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
            
    return False

def find_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """Finds start node of cycle if exists.
    
    Args:
        head: Head of linked list
        
    Returns:
        Start node of cycle or None if no cycle
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return None
        
    # Find meeting point
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
        
    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow
```

### When to Use
- Cycle detection in linked lists
- Finding middle element
- Detecting duplicate elements

### Example Problems
1. Linked List Cycle (LC #141)
2. Happy Number (LC #202)
3. Find the Duplicate Number (LC #287)

## 5. LinkedList In-place Reversal Pattern
This pattern handles reversing linked lists or parts of linked lists without extra space.

### Implementation
```python
def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses linked list in-place.
    
    Args:
        head: Head of linked list
        
    Returns:
        New head of reversed list
        
    Time: O(n), Space: O(1)
    Example:
        Input: 1->2->3->4->5
        Output: 5->4->3->2->1
    """
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
        
    return prev

def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """Reverses sublist between positions left and right.
    
    Args:
        head: Head of linked list
        left: Start position (1-based)
        right: End position (1-based)
        
    Returns:
        Head of modified list
        
    Time: O(n), Space: O(1)
    Example:
        >>> head = [1,2,3,4,5], left = 2, right = 4
        >>> reverse_between(head, 2, 4)
        [1,4,3,2,5]
    """
    if not head or left == right:
        return head
        
    dummy = ListNode(0, head)
    prev = dummy
    
    # Move to node before reversal starts
    for _ in range(left - 1):
        prev = prev.next
        
    curr = prev.next
    # Reverse sublist
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
        
    return dummy.next
```

### When to Use
- Reversing entire linked list
- Reversing sublist
- K-group reversals

### Example Problems
1. Reverse Linked List (LC #206)
2. Reverse Linked List II (LC #92)
3. Swap Nodes in Pairs (LC #24)

# Core Algorithm Patterns (6-15)

## 6. Monotonic Stack Pattern
A monotonic stack maintains elements in strictly increasing/decreasing order.

```python
def next_greater_element(nums: List[int]) -> List[int]:
    """Finds next greater element for each element in array.
    
    Args:
        nums: Array of integers
        
    Returns:
        Array where result[i] is next greater element for nums[i]
        
    Time: O(n), Space: O(n)
    Example:
        >>> next_greater_element([2, 1, 2, 4, 3])
        [4, 2, 4, -1, -1]
    """
    result = [-1] * len(nums)
    stack = []  # Stores indices
    
    for i, num in enumerate(nums):
        # Pop elements smaller than current
        while stack and nums[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
        
    return result

def largest_rectangle_histogram(heights: List[int]) -> int:
    """Finds largest rectangular area in histogram.
    
    Args:
        heights: Array of histogram bar heights
        
    Returns:
        Area of largest rectangle
        
    Time: O(n), Space: O(n)
    Example:
        >>> largest_rectangle_histogram([2, 1, 5, 6, 2, 3])
        10  # Heights [5, 6] form rectangle of area 10
    """
    stack = []  # (index, height) pairs
    max_area = 0
    heights.append(0)  # Sentinel to pop all elements
    
    for i, height in enumerate(heights):
        start = i
        while stack and stack[-1][1] > height:
            index, h = stack.pop()
            width = i - index
            max_area = max(max_area, width * h)
            start = index
        stack.append((start, height))
        
    return max_area
```

## 7. Top 'K' Elements Pattern
Uses heap data structure to find/maintain top k elements efficiently.

```python
import heapq

def find_kth_largest(nums: List[int], k: int) -> int:
    """Finds kth largest element in array.
    
    Args:
        nums: Array of integers
        k: Position from largest (1 for largest)
        
    Returns:
        kth largest element
        
    Time: O(n*log(k)), Space: O(k)
    Example:
        >>> find_kth_largest([3, 2, 1, 5, 6, 4], 2)
        5  # Second largest element
    """
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Finds k most frequent elements.
    
    Args:
        nums: Array of integers
        k: Number of frequent elements to return
        
    Returns:
        k most frequent elements
        
    Time: O(n*log(k)), Space: O(n)
    Example:
        >>> top_k_frequent([1,1,1,2,2,3], 2)
        [1, 2]  # 1 and 2 appear most frequently
    """
    # Count frequencies
    count = Counter(nums)
    
    # Use min heap to keep top k
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
            
    return [num for freq, num in heap]
```

## 8. Overlapping Intervals Pattern
Handles interval merging and intersection problems.

```python
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """Merges overlapping intervals.
    
    Args:
        intervals: List of [start, end] intervals
        
    Returns:
        Merged intervals
        
    Time: O(n*log(n)), Space: O(n)
    Example:
        >>> merge_intervals([[1,3], [2,6], [8,10], [15,18]])
        [[1,6], [8,10], [15,18]]
    """
    if not intervals:
        return []
        
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:  # Overlap
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
            
    return merged

def insert_interval(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """Inserts new interval into sorted non-overlapping intervals.
    
    Args:
        intervals: Sorted non-overlapping intervals
        newInterval: Interval to insert
        
    Returns:
        Updated list of merged intervals
        
    Time: O(n), Space: O(n)
    """
    result = []
    i = 0
    n = len(intervals)
    
    # Add intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    
    # Add remaining intervals
    result.extend(intervals[i:])
    return result
```

## 9. Modified Binary Search Pattern
Adapts binary search for various scenarios.

```python
def search_rotated(nums: List[int], target: int) -> int:
    """Searches for element in rotated sorted array.
    
    Args:
        nums: Rotated sorted array
        target: Element to find
        
    Returns:
        Index of target or -1 if not found
        
    Time: O(log n), Space: O(1)
    Example:
        >>> search_rotated([4,5,6,7,0,1,2], 0)
        4
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
            
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

def search_range(nums: List[int], target: int) -> List[int]:
    """Finds first and last position of element.
    
    Args:
        nums: Sorted array
        target: Element to find
        
    Returns:
        [start, end] positions of target
        
    Time: O(log n), Space: O(1)
    """
    def find_bound(nums: List[int], target: int, is_first: bool) -> int:
        left, right = 0, len(nums) - 1
        bound = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1  # Continue left
                else:
                    left = mid + 1   # Continue right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return bound
        
    return [
        find_bound(nums, target, True),
        find_bound(nums, target, False)
    ]
```
## 10. Binary Tree Traversal Pattern
Provides different ways to visit tree nodes systematically.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_traversals(root: Optional[TreeNode]) -> Dict[str, List[int]]:
    """Implements all three tree traversal methods.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Dictionary with preorder, inorder, and postorder traversals
        
    Time: O(n), Space: O(h) where h is tree height
    Example:
        Tree:     1
                /   \
               2     3
              / \   
             4   5
        
        Returns: {
            'preorder': [1,2,4,5,3],
            'inorder': [4,2,5,1,3],
            'postorder': [4,5,2,3,1]
        }
    """
    result = {'preorder': [], 'inorder': [], 'postorder': []}
    
    def preorder(node: Optional[TreeNode]) -> None:
        if not node:
            return
        result['preorder'].append(node.val)
        preorder(node.left)
        preorder(node.right)
    
    def inorder(node: Optional[TreeNode]) -> None:
        if not node:
            return
        inorder(node.left)
        result['inorder'].append(node.val)
        inorder(node.right)
    
    def postorder(node: Optional[TreeNode]) -> None:
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        result['postorder'].append(node.val)
    
    preorder(root)
    inorder(root)
    postorder(root)
    return result

def iterative_inorder(root: Optional[TreeNode]) -> List[int]:
    """Implements inorder traversal iteratively.
    
    Time: O(n), Space: O(h)
    """
    result = []
    stack = []
    curr = root
    
    while curr or stack:
        # Reach leftmost node
        while curr:
            stack.append(curr)
            curr = curr.left
            
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
        
    return result
```

## 11. Depth-First Search (DFS) Pattern
Used for exploring paths and tree/graph traversal to maximum depth first.

```python
def path_sum_ii(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    """Finds all root-to-leaf paths summing to target.
    
    Args:
        root: Binary tree root
        targetSum: Target path sum
        
    Returns:
        List of paths that sum to target
        
    Time: O(n), Space: O(h) where h is tree height
    Example:
        >>> path_sum_ii([5,4,8,11,null,13,4,7,2,null,null,5,1], 22)
        [[5,4,11,2], [5,8,4,5]]
    """
    def dfs(node: Optional[TreeNode], target: int, path: List[int], 
           result: List[List[int]]) -> None:
        if not node:
            return
            
        path.append(node.val)
        
        # Check leaf node
        if not node.left and not node.right and target == node.val:
            result.append(path[:])
            
        dfs(node.left, target - node.val, path, result)
        dfs(node.right, target - node.val, path, result)
        path.pop()  # Backtrack
    
    result = []
    dfs(root, targetSum, [], result)
    return result

def number_of_islands(grid: List[List[str]]) -> int:
    """Counts number of islands in binary grid.
    
    Args:
        grid: Binary matrix where '1' is land, '0' is water
        
    Returns:
        Number of islands (connected land cells)
        
    Time: O(m*n), Space: O(m*n)
    Example:
        >>> number_of_islands([
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ])
        3
    """
    if not grid:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r: int, c: int) -> None:
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] != '1'):
            return
            
        # Mark as visited
        grid[r][c] = '#'
        
        # Check all 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                islands += 1
                
    return islands
```

## 12. Breadth-First Search (BFS) Pattern
Used for level-by-level traversal and finding shortest paths.

```python
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Performs level-order traversal of binary tree.
    
    Args:
        root: Binary tree root
        
    Returns:
        List of levels, each containing node values
        
    Time: O(n), Space: O(w) where w is max width
    Example:
        >>> level_order([3,9,20,null,null,15,7])
        [[3],[9,20],[15,7]]
    """
    if not root:
        return []
        
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level)
        
    return result

def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """Finds shortest path from top-left to bottom-right.
    
    Path can move in 8 directions through empty cells (0).
    
    Time: O(n*m), Space: O(n*m)
    Example:
        >>> shortest_path_binary_matrix([[0,1],[1,0]])
        2
    """
    if not grid or grid[0][0] == 1:
        return -1
        
    n = len(grid)
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)
    ]
    
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    grid[0][0] = 1  # Mark as visited
    
    while queue:
        row, col, dist = queue.popleft()
        
        if row == n-1 and col == n-1:
            return dist
            
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if (0 <= r < n and 0 <= c < n and grid[r][c] == 0):
                grid[r][c] = 1  # Mark as visited
                queue.append((r, c, dist + 1))
                
    return -1
```

## 13. Matrix Traversal Pattern
Techniques for traversing and processing 2D matrices.

```python
def spiral_order(matrix: List[List[int]]) -> List[int]:
    """Returns elements of matrix in spiral order.
    
    Args:
        matrix: 2D integer matrix
        
    Returns:
        Elements in spiral order
        
    Time: O(m*n), Space: O(1) excluding output
    Example:
        >>> spiral_order([[1,2,3],[4,5,6],[7,8,9]])
        [1,2,3,6,9,8,7,4,5]
    """
    if not matrix:
        return []
        
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse left
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
            
        if left <= right:
            # Traverse up
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result

def rotate_image(matrix: List[List[int]]) -> None:
    """Rotates image 90 degrees clockwise in-place.
    
    Time: O(n²), Space: O(1)
    Example:
        >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
        >>> rotate_image(matrix)
        >>> matrix
        [[7,4,1],[8,5,2],[9,6,3]]
    """
    n = len(matrix)
    
    # Transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

## 14. Backtracking Pattern
For finding all possible combinations or permutations.

```python
def permutations(nums: List[int]) -> List[List[int]]:
    """Generates all possible permutations.
    
    Args:
        nums: List of distinct integers
        
    Returns:
        All possible permutations
        
    Time: O(n!), Space: O(n)
    Example:
        >>> permutations([1,2,3])
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    """
    def backtrack(start: int) -> None:
        if start == len(nums):
            result.append(nums[:])
            return
            
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    
    result = []
    backtrack(0)
    return result

def n_queens(n: int) -> List[List[str]]:
    """Solves N-Queens problem.
    
    Args:
        n: Board size
        
    Returns:
        All valid board configurations
        
    Time: O(n!), Space: O(n²)
    Example:
        >>> n_queens(4)
        [[".Q..","...Q","Q...","..Q."],
         ["..Q.","Q...","...Q",".Q.."]]
    """
    def create_board() -> List[str]:
        board = []
        for row in placed_queens:
            board_row = '.' * row + 'Q' + '.' * (n - row - 1)
            board.append(board_row)
        return board
    
    def can_place(row: int, col: int) -> bool:
        return (
            not cols[col] and
            not diag1[row + col] and
            not diag2[row - col]
        )
    
    def place_queen(row: int, col: int) -> None:
        cols[col] = True
        diag1[row + col] = True
        diag2[row - col] = True
        placed_queens[row] = col
    
    def remove_queen(row: int, col: int) -> None:
        cols[col] = False
        diag1[row + col] = False
        diag2[row - col] = False
    
    def backtrack(row: int) -> None:
        if row == n:
            result.append(create_board())
            return
            
        for col in range(n):
            if can_place(row, col):
                place_queen(row, col)
                backtrack(row + 1)
                remove_queen(row, col)
    
    result = []
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    placed_queens = [0] * n
    backtrack(0)
    return result
```

## 15. Dynamic Programming Pattern
For optimization problems with overlapping subproblems.

```python
def coin_change(coins: List[int], amount: int) -> int:
    """Finds minimum number of coins needed for amount.
    
    Args:
        coins: Available coin denominations
        amount: Target amount
        
    Returns:
        Minimum coins needed or -1 if impossible
        
    Time: O(amount * len(coins)), Space: O(amount)
    Example:
        >>> coin_change([1,2,5], 11)
        3  # 11 = 5 + 5 + 1
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
            
    return dp[amount] if dp[amount] != float('inf') else -1

def longest_increasing_subsequence(nums: List[int]) -> int:
    """Finds length of longest increasing subsequence.
    
    Args:
        nums: Array of integers
        
    Returns:
        Length of longest strictly increasing subsequence
        
    Time: O(n log n), Space: O(n)
    Example:
        >>> longest_increasing_subsequence([10,9,2,5,3,7,101,18])
        4  # [2,3,7,101]
    """
    if not nums:
        return 0
        
    # tails[i] = smallest value that ends an increasing subsequence of length i+1
    tails = []
    
    for num in nums:
        # Binary search to find position to insert num
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
                
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
            
    return len(tails)
```

### Common Variations and Extensions:

1. **Tree Traversal:**
   - Iterative implementations
   - Morris Traversal (O(1) space)
I can continue with Tree Traversal, DFS, BFS, Matrix Traversal, Backtracking, and Dynamic Programming patterns. Let me know your preference!



