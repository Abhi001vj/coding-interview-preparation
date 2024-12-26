# https://leetcode.com/problems/lfu-cache/description/
# 460. LFU Cache
# Hard
# Topics
# Companies
# Design and implement a data structure for a Least Frequently Used (LFU) cache.

# Implement the LFUCache class:

# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[4,3], cnt(4)=2, cnt(3)=3
 

# Constraints:

# 1 <= capacity <= 104
# 0 <= key <= 105
# 0 <= value <= 109
# At most 2 * 105 calls will be made to get and put.

from collections import defaultdict, OrderedDict

class LFUCache:
    """
    LFU Cache implementation using dictionaries and OrderedDict
    
    Data structures:
    - values: key -> value
    - counts: key -> frequency
    - freq_keys: frequency -> OrderedDict(key -> None)  # OrderedDict to maintain LRU order
    - min_freq: tracks current minimum frequency
    
    Example state after operations:
    LFUCache(2)
    put(1,1): 
        values = {1: 1}
        counts = {1: 1}
        freq_keys = {1: OrderedDict([(1, None)])}
        min_freq = 1
        
    put(2,2):
        values = {1: 1, 2: 2}
        counts = {1: 1, 2: 1}
        freq_keys = {1: OrderedDict([(1, None), (2, None)])}
        min_freq = 1
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}              # key -> value
        self.counts = {}              # key -> frequency
        self.freq_keys = defaultdict(OrderedDict)  # frequency -> OrderedDict of keys
        self.min_freq = 0
        
    def get(self, key: int) -> int:
        """
        Get value for key and update its frequency
        Example:
        get(1) when freq(1)=1:
            1. Get value
            2. Remove key from freq_keys[1]
            3. Add key to freq_keys[2]
            4. Update counts[key] = 2
            5. Update min_freq if needed
        """
        if key not in self.values:
            return -1
            
        # Update frequency
        self._update_frequency(key)
        return self.values[key]
        
    def put(self, key: int, value: int) -> None:
        """
        Put value and handle capacity/LFU eviction
        Example:
        put(3,3) when cache full [1,2]:
            1. If key exists: update value and frequency
            2. If cache full: remove LFU key (min_freq)
            3. Add new key with freq=1
            4. Update min_freq = 1
        """
        if self.capacity == 0:
            return
            
        if key in self.values:
            self._update_frequency(key)
            self.values[key] = value
            return
            
        # Handle capacity
        if len(self.values) >= self.capacity:
            # Remove least frequent key
            lfu_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
            del self.values[lfu_key]
            del self.counts[lfu_key]
            
        # Add new key
        self.values[key] = value
        self.counts[key] = 1
        self.freq_keys[1][key] = None
        self.min_freq = 1
        
    def _update_frequency(self, key: int) -> None:
        """
        Helper to update frequency of a key
        Steps:
        1. Get current frequency
        2. Remove from current frequency list
        3. Add to next frequency list
        4. Update minimum frequency if needed
        """
        freq = self.counts[key]
        # Remove from current frequency
        del self.freq_keys[freq][key]
        
        # Update minimum frequency if needed
        if freq == self.min_freq and not self.freq_keys[freq]:
            self.min_freq += 1
            
        # Add to next frequency
        self.counts[key] = freq + 1
        self.freq_keys[freq + 1][key] = None

Let me break this down with examples of both operations and explain why O(1) removal matters.

Remove from any position O(1) - Used in _update_frequency:

pythonCopy# When we call get(1) or put(1,x), we need to update its frequency
del self.freq_keys[freq][key]  # Remove key from current frequency list

# Example:
freq_keys[2] = OrderedDict([(5, None), (1, None), (3, None)])
# If we access key=1, we need to remove it from freq 2
# We need O(1) removal because this happens on EVERY access

Remove oldest (LRU) O(1) - Used in put for eviction:

pythonCopy# When cache is full and we need to evict
lfu_key, _ = self.freq_keys[min_freq].popitem(last=False)  
# popitem(last=False) removes the FIRST/OLDEST item in O(1)
Let's see a complete example:
pythonCopy# Initialize cache with capacity 2
lfu = LFUCache(2)

# 1. put(1,1)
values = {1: 1}
counts = {1: 1}
freq_keys = {
    1: OrderedDict([(1, None)])  # freq 1, only key 1
}
min_freq = 1

# 2. put(2,2)
values = {1: 1, 2: 2}
counts = {1: 1, 2: 1}
freq_keys = {
    1: OrderedDict([(1, None), (2, None)])  # both at freq 1
}
min_freq = 1

# 3. get(1) - increases freq of 1
values = {1: 1, 2: 2}
counts = {1: 2, 2: 1}  # 1's freq increased
freq_keys = {
    1: OrderedDict([(2, None)]),  # 2 stays at freq 1
    2: OrderedDict([(1, None)])   # 1 moved to freq 2
}
min_freq = 1

# 4. put(3,3) - need to evict key 2 (lowest freq)
values = {1: 1, 3: 3}
counts = {1: 2, 3: 1}
freq_keys = {
    1: OrderedDict([(3, None)]),  # 3 at freq 1
    2: OrderedDict([(1, None)])   # 1 at freq 2
}
min_freq = 1

# 5. put(4,4) - need to evict key 3 (lowest freq)
values = {1: 1, 4: 4}
counts = {1: 2, 4: 1}
freq_keys = {
    1: OrderedDict([(4, None)]),  # 4 at freq 1
    2: OrderedDict([(1, None)])   # 1 at freq 2
}
min_freq = 1
The O(1) operations are crucial because:

Every get/put operation needs to update frequencies
When cache is full, we need to find and remove LFU (and break ties with LRU)
These operations happen very frequently in a cache

Without O(1) operations, each cache access could be O(n), making the cache inefficient for its intended use case of fast access.def _update_frequency(self, key: int) -> None:
    # 1. Get current frequency of the key
    freq = self.counts[key]  # Example: if key=1 has freq=2

    # 2. Remove key from its current frequency list
    del self.freq_keys[freq][key]
    # Example: if freq_keys[2] had {1: None, 3: None}
    # Now freq_keys[2] has {3: None}

    # 3. Update min_freq if needed
    if freq == self.min_freq and not self.freq_keys[freq]:
        self.min_freq += 1
    # Example: if min_freq was 2 and we just removed 
    # the last key with freq=2, min_freq becomes 3

    # 4. Add key to next frequency level
    self.counts[key] = freq + 1  # Update key's frequency
    self.freq_keys[freq + 1][key] = None  # Add to next freq list


Let me break this down:

First, why OrderedDict?

pythonCopyself.freq_keys = defaultdict(OrderedDict)  # frequency -> OrderedDict of keys
We need OrderedDict because:

We need to track which key was used LEAST RECENTLY among keys with same frequency
When there's a tie in frequency, we remove the LEAST RECENTLY used key
OrderedDict maintains insertion order

Example:
pythonCopy# When two keys have same frequency = 2
self.freq_keys[2] = OrderedDict([(1, None), (2, None), (3, None)])
# 1 is least recently used, 3 is most recently used

Why key -> None?

pythonCopyself.freq_keys[1][key] = None

We only care about the KEYS and their ORDER
The None is just a placeholder value because dictionaries need values
We could use a list instead, but OrderedDict gives us O(1) removal from any position

Here's a concrete example:
pythonCopy# Initial state:
put(1,1):  freq_keys[1] = OrderedDict([(1, None)])
put(2,2):  freq_keys[1] = OrderedDict([(1, None), (2, None)])

# After get(1):
# 1's frequency increases to 2
freq_keys[1] = OrderedDict([(2, None)])         # 2 remains at freq 1
freq_keys[2] = OrderedDict([(1, None)])         # 1 moves to freq 2

# When we need to evict at freq 1:
lfu_key, _ = self.freq_keys[1].popitem(last=False)  # Gets oldest key (2)
The OrderedDict essentially acts like a queue that lets us:

Add items to the end (most recently used)
Remove items from any position in O(1) time
Remove oldest item (least recently used) in O(1) time