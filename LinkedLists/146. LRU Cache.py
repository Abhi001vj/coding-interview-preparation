# https://leetcode.com/problems/lru-cache/description/
# 146. LRU Cache
# Solved
# Medium
# Topics
# Companies
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.
```python
"""
LRU CACHE: Complete Implementation Analysis
=======================================

Core Data Structures:
1. HashMap: For O(1) key lookups
2. Doubly Linked List: For O(1) removals and insertions
3. Custom Node class: For storing key-value pairs

Key Operations:
1. get: O(1) lookup and move to front
2. put: O(1) insert/update and potential eviction
3. move_to_front: O(1) node repositioning
4. remove: O(1) node removal
"""

class Node:
    """
    Doubly Linked List Node
    Stores key for easier removal from hash map during eviction
    """
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    Visual Example:
    Capacity = 2
    Operations: put(1,1), put(2,2), get(1), put(3,3)
    
    Initial State:
    HEAD <-> TAIL
    cache = {}
    
    After put(1,1):
    HEAD <-> [1:1] <-> TAIL
    cache = {1: node1}
    
    After put(2,2):
    HEAD <-> [2:2] <-> [1:1] <-> TAIL
    cache = {1: node1, 2: node2}
    
    After get(1): (move to front)
    HEAD <-> [1:1] <-> [2:2] <-> TAIL
    cache = {1: node1, 2: node2}
    
    After put(3,3): (evict 2)
    HEAD <-> [3:3] <-> [1:1] <-> TAIL
    cache = {1: node1, 3: node3}
    """
    def __init__(self, capacity: int):
        """
        Initialize with dummy head and tail nodes
        HEAD <-> TAIL
        """
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # Dummy nodes for easier operations
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node: Node) -> None:
        """
        Remove node from linked list
        
        Before: A <-> B <-> C
        Remove B: A <-> C
        
        Time: O(1)
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _add(self, node: Node) -> None:
        """
        Add node right after head
        
        Before: HEAD <-> A
        Add B: HEAD <-> B <-> A
        
        Time: O(1)
        """
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
        
    def get(self, key: int) -> int:
        """
        Look up key and move to front if found
        
        Example:
        State: HEAD <-> [2:2] <-> [1:1] <-> TAIL
        get(1):
        1. Find node in cache
        2. Remove from current position
        3. Add after head
        Result: HEAD <-> [1:1] <-> [2:2] <-> TAIL
        
        Time: O(1)
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        """
        Add or update key-value pair
        
        Example (capacity = 2):
        State: HEAD <-> [2:2] <-> [1:1] <-> TAIL
        put(3,3):
        1. Remove 1 (LRU)
        2. Create new node
        3. Add after head
        Result: HEAD <-> [3:3] <-> [2:2] <-> TAIL
        
        Time: O(1)
        """
        if key in self.cache:
            self._remove(self.cache[key])
            
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        
        if len(self.cache) > self.capacity:
            # Remove from linked list and cache
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

"""
COMPLETE OPERATION SEQUENCE
-------------------------
Example: capacity = 2
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

Step-by-step:
1. Initialize:
   HEAD <-> TAIL

2. put(1,1):
   HEAD <-> [1:1] <-> TAIL
   cache = {1: node1}

3. put(2,2):
   HEAD <-> [2:2] <-> [1:1] <-> TAIL
   cache = {1: node1, 2: node2}

4. get(1):
   HEAD <-> [1:1] <-> [2:2] <-> TAIL
   cache = {1: node1, 2: node2}
   return 1

5. put(3,3):
   HEAD <-> [3:3] <-> [1:1] <-> TAIL
   cache = {1: node1, 3: node3}
   (evicted 2)

Continue sequence...

EDGE CASES
---------
1. Capacity = 1
2. Duplicate keys
3. Get non-existent key
4. Put when full
5. Get after eviction

TIME COMPLEXITY
-------------
All operations O(1):
- HashMap provides O(1) lookup
- Doubly linked list provides O(1) remove/add
- No iteration needed for eviction

SPACE COMPLEXITY
--------------
O(capacity):
- HashMap stores at most capacity items
- Linked list stores same nodes as HashMap
"""
```python
"""
LRU CACHE: Multiple Implementation Analysis
========================================
Example Sequence:
Operations: put(1,1), put(2,2), get(1), put(3,3), get(2)
"""

class BruteForceLRUCache:
    """
    APPROACH 1: ARRAY-BASED BRUTE FORCE
    ---------------------------------
    Visual Process:
    
    Initial: []
    
    put(1,1):
    cache = [[1,1]]
    
    put(2,2):
    cache = [[1,1], [2,2]]
    
    get(1): Move [1,1] to end
    cache = [[2,2], [1,1]]
    
    put(3,3): Remove oldest
    cache = [[1,1], [3,3]]
    
    Advantages:
    + Simple implementation
    + Easy to understand
    
    Disadvantages:
    - O(n) operations
    - Linear search for each operation
    """
    def __init__(self, capacity: int):
        self.cache = []  # List of [key,value] pairs
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Search Process Visualization:
        cache = [[1,1], [2,2], [3,3]]
        get(2):
        1. Search through array
        2. Find [2,2]
        3. Remove and append to end
        Result: [[1,1], [3,3], [2,2]]
        """
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Put Process Visualization:
        cache = [[1,1], [2,2]], capacity = 2
        put(3,3):
        1. Check if full: Yes
        2. Remove oldest: [[2,2]]
        3. Add new: [[2,2], [3,3]]
        """
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return

        if self.capacity == len(self.cache):
            self.cache.pop(0)
        self.cache.append([key, value])

class OptimalLRUCache:
    """
    APPROACH 2: DOUBLY LINKED LIST + HASHMAP
    -------------------------------------
    Visual Structure:
    HEAD <-> [key1:val1] <-> [key2:val2] <-> TAIL
    cache = {key1: node1, key2: node2}
    
    Operations Visualization:
    1. get(key):
       - Find node in cache O(1)
       - Remove from list O(1)
       - Add to head O(1)
    
    2. put(key,value):
       - If exists: update and move to head
       - If full: remove tail.prev
       - Add new node at head
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: 'Node') -> None:
        """
        Remove Node Visualization:
        Before: A <-> B <-> C
        Remove B: A <-> C
        Time: O(1)
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node: 'Node') -> None:
        """
        Insert at Head Visualization:
        Before: HEAD <-> A
        Insert B: HEAD <-> B <-> A
        Time: O(1)
        """
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

class BuiltInLRUCache:
    """
    APPROACH 3: ORDERED DICT
    ----------------------
    Visual Process using OrderedDict:
    
    Initial: OrderedDict()
    
    put(1,1): OrderedDict([(1,1)])
    put(2,2): OrderedDict([(1,1), (2,2)])
    get(1):   OrderedDict([(2,2), (1,1)])
    put(3,3): OrderedDict([(1,1), (3,3)])
    
    Advantages:
    + Clean implementation
    + Built-in ordering
    + O(1) operations
    
    Disadvantages:
    - Platform dependent
    - Less control over internals
    """
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        """
        Get Operation Visualization:
        cache = OrderedDict([(1,1), (2,2)])
        get(1):
        1. Check existence
        2. Move to end
        3. Return value
        Result: OrderedDict([(2,2), (1,1)])
        """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Put Operation Visualization:
        cache = OrderedDict([(1,1), (2,2)])
        put(3,3):
        1. Remove oldest if full
        2. Add/Update key
        3. Move to end
        Result: OrderedDict([(2,2), (3,3)])
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

"""
COMPLEXITY ANALYSIS
-----------------
1. Brute Force:
   Time: O(n) for all operations
   Space: O(n)
   Operations require linear search

2. Optimal (DLL + HashMap):
   Time: O(1) for all operations
   Space: O(n)
   Constant time node manipulation

3. Built-in OrderedDict:
   Time: O(1) for all operations
   Space: O(n)
   Leverages built-in implementation

EDGE CASES AND CONSIDERATIONS
--------------------------
1. Empty Cache
2. Single Element
3. Full Cache
4. Duplicate Keys
5. Get Non-existent Key
6. Remove Last Element
7. Update Existing Key
"""
```