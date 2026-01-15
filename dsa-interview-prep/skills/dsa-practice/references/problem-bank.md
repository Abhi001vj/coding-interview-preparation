# Comprehensive Problem Bank (600+ Problems)

## Organization

Problems organized by:
1. **Pattern** - Which technique to use
2. **Difficulty** - Easy/Medium/Hard
3. **Company** - Google (G), Meta (M), Both (B)
4. **Frequency** - How often asked (★ = high frequency)
5. **Priority** - Based on your interview feedback (⭐ = must master)

---

## PRIORITY 0: Your Actual Interview Questions

### Must Master First - These Cost You Offers

| # | Problem | Difficulty | Pattern | Company | Notes |
|---|---------|------------|---------|---------|-------|
| ⭐ | HistorySet (Custom) | Medium | Snapshot | Google | Failed Jan 2025 |
| ⭐ | URL Content Grouping | Medium | DSU/Hash | Meta | Failed Jul 2025 |
| 1146 | Snapshot Array | Medium | Snapshot | G★ | Same pattern as HistorySet |
| 721 | Accounts Merge | Medium | DSU | M★ | Same pattern as URL grouping |
| 981 | Time Based Key-Value Store | Medium | Snapshot | G★ | Versioning variant |
| 49 | Group Anagrams | Medium | Hash | M★ | Simpler grouping |

---

## SECTION 1: Arrays & Hashing (120 problems)

### Two Sum Variants
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 1 | Two Sum | Easy | Hash | B★ | Classic |
| 167 | Two Sum II - Sorted | Med | 2-Ptr | B | Binary search works too |
| 15 | 3Sum | Med | 2-Ptr | B★ | Sort first |
| 16 | 3Sum Closest | Med | 2-Ptr | G | Track min diff |
| 18 | 4Sum | Med | 2-Ptr | G | Extension |
| 454 | 4Sum II | Med | Hash | M | Different approach |
| 560 | Subarray Sum Equals K | Med | Prefix | B★ | Prefix sum + hash |
| 523 | Continuous Subarray Sum | Med | Prefix | M | Modulo trick |
| 525 | Contiguous Array | Med | Prefix | M | 0/1 to -1/1 |

### Array Manipulation
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 26 | Remove Duplicates | Easy | 2-Ptr | B | In-place |
| 27 | Remove Element | Easy | 2-Ptr | B | In-place |
| 80 | Remove Duplicates II | Med | 2-Ptr | G | Allow 2 |
| 283 | Move Zeroes | Easy | 2-Ptr | M★ | Order matters |
| 88 | Merge Sorted Array | Easy | 2-Ptr | B★ | From end |
| 189 | Rotate Array | Med | Array | B | k positions |
| 48 | Rotate Image | Med | Matrix | G★ | In-place |
| 54 | Spiral Matrix | Med | Matrix | B★ | Bounds tracking |
| 73 | Set Matrix Zeroes | Med | Matrix | M | O(1) space tricky |
| 36 | Valid Sudoku | Med | Hash | G | 3 hash sets |
| 128 | Longest Consecutive Sequence | Med | Hash | B★ | Union-find also works |
| 238 | Product of Array Except Self | Med | Prefix | B★ | Left/right products |
| 41 | First Missing Positive | Hard | Array | G★ | Index as hash |
| 287 | Find the Duplicate Number | Med | Floyd | M | Cycle detection |
| 442 | Find All Duplicates | Med | Index | M | Negate trick |
| 448 | Find Disappeared Numbers | Easy | Index | M | Negate trick |
| 645 | Set Mismatch | Easy | Math | M | XOR or hash |

### String Manipulation
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 242 | Valid Anagram | Easy | Hash | B | Frequency count |
| 49 | Group Anagrams | Med | Hash | B★ | Sort as key |
| 438 | Find All Anagrams | Med | Window | B★ | Fixed window |
| 567 | Permutation in String | Med | Window | B | Same as 438 |
| 5 | Longest Palindromic Substring | Med | Expand | B★ | Center expansion |
| 647 | Palindromic Substrings | Med | Expand | M | Count all |
| 516 | Longest Palindromic Subsequence | Med | DP | G | 2D DP |
| 125 | Valid Palindrome | Easy | 2-Ptr | B | Alphanumeric only |
| 680 | Valid Palindrome II | Easy | 2-Ptr | M★ | Delete at most 1 |
| 344 | Reverse String | Easy | 2-Ptr | B | In-place |
| 151 | Reverse Words | Med | String | M | Extra space ok |
| 557 | Reverse Words III | Easy | String | M | Each word |
| 8 | String to Integer (atoi) | Med | String | G | Edge cases |
| 12 | Integer to Roman | Med | Greedy | G | Lookup table |
| 13 | Roman to Integer | Easy | Hash | M | Left to right |
| 6 | Zigzag Conversion | Med | String | G | Row simulation |
| 28 | Find Index of First Occurrence | Easy | String | B | KMP optional |
| 14 | Longest Common Prefix | Easy | String | B | Character by character |
| 58 | Length of Last Word | Easy | String | B | Reverse iteration |
| 443 | String Compression | Med | 2-Ptr | M | In-place |
| 394 | Decode String | Med | Stack | B★ | Nested brackets |
| 767 | Reorganize String | Med | Heap | M★ | Greedy + heap |

### Intervals
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 56 | Merge Intervals | Med | Sort | B★ | Classic |
| 57 | Insert Interval | Med | Sort | G★ | Three parts |
| 252 | Meeting Rooms | Easy | Sort | M | Check overlap |
| 253 | Meeting Rooms II | Med | Heap | M★ | Min heap for end times |
| 435 | Non-overlapping Intervals | Med | Greedy | G | Remove minimum |
| 452 | Minimum Arrows to Burst Balloons | Med | Greedy | G | Sort by end |
| 986 | Interval List Intersections | Med | 2-Ptr | M | Two pointers |

---

## SECTION 2: Two Pointers (50 problems)

### Opposite Direction
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 11 | Container With Most Water | Med | 2-Ptr | B★ | Shrink from outside |
| 42 | Trapping Rain Water | Hard | 2-Ptr | B★ | Also stack works |
| 75 | Sort Colors | Med | 2-Ptr | M★ | Dutch flag |
| 881 | Boats to Save People | Med | 2-Ptr | G | Greedy pairing |

### Same Direction (Fast/Slow)
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 141 | Linked List Cycle | Easy | Floyd | B★ | Fast/slow |
| 142 | Linked List Cycle II | Med | Floyd | B | Find cycle start |
| 287 | Find the Duplicate Number | Med | Floyd | M | Array as linked list |
| 876 | Middle of the Linked List | Easy | 2-Ptr | B | Fast/slow |
| 234 | Palindrome Linked List | Easy | 2-Ptr | M | Reverse second half |

---

## SECTION 3: Sliding Window (60 problems)

### Fixed Window
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 643 | Maximum Average Subarray I | Easy | Window | M | Fixed k |
| 1423 | Maximum Points from Cards | Med | Window | G | Complement window |
| 1456 | Maximum Vowels in Substring | Med | Window | M | Fixed k |
| 567 | Permutation in String | Med | Window | B | Frequency match |
| 438 | Find All Anagrams | Med | Window | B★ | All positions |
| 239 | Sliding Window Maximum | Hard | Deque | G★ | Monotonic deque |
| 480 | Sliding Window Median | Hard | Heap | G | Two heaps |

### Variable Window
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 3 | Longest Substring Without Repeating | Med | Window | B★ | Classic |
| 76 | Minimum Window Substring | Hard | Window | G★ | Shrink when valid |
| 424 | Longest Repeating Char Replacement | Med | Window | B★ | k replacements |
| 1004 | Max Consecutive Ones III | Med | Window | M★ | k flips |
| 904 | Fruit Into Baskets | Med | Window | M | At most 2 types |
| 209 | Minimum Size Subarray Sum | Med | Window | B | Target sum |
| 713 | Subarray Product Less Than K | Med | Window | G | Product constraint |
| 1248 | Count Nice Subarrays | Med | Window | M | k odd numbers |
| 1838 | Frequency of Most Frequent Element | Med | Window | G | With operations |

---

## SECTION 4: Binary Search (70 problems)

### Classic Binary Search
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 704 | Binary Search | Easy | BS | B | Template |
| 35 | Search Insert Position | Easy | BS | B | Lower bound |
| 34 | Find First and Last Position | Med | BS | B★ | Two binary searches |
| 278 | First Bad Version | Easy | BS | B | API call |
| 374 | Guess Number | Easy | BS | M | API call |

### Rotated Array
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 33 | Search in Rotated Sorted Array | Med | BS | B★ | Find sorted half |
| 81 | Search in Rotated Sorted Array II | Med | BS | G | With duplicates |
| 153 | Find Minimum in Rotated Sorted Array | Med | BS | B★ | Find pivot |
| 154 | Find Minimum in Rotated Sorted Array II | Hard | BS | G | With duplicates |
| 162 | Find Peak Element | Med | BS | B | Local maximum |
| 852 | Peak Index in Mountain Array | Med | BS | M | Similar to 162 |

### Binary Search on Answer
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 875 | Koko Eating Bananas | Med | BS | B★ | Minimize speed |
| 1011 | Capacity To Ship Packages | Med | BS | G★ | Minimize capacity |
| 410 | Split Array Largest Sum | Hard | BS | G | Minimize max sum |
| 1283 | Find Smallest Divisor | Med | BS | M | Minimize divisor |
| 1482 | Minimum Days to Make Bouquets | Med | BS | M | Binary on days |
| 1552 | Magnetic Force Between Balls | Med | BS | G | Maximize minimum |
| 2226 | Maximum Candies Allocated | Med | BS | M | Maximize minimum |

### 2D Binary Search
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 74 | Search a 2D Matrix | Med | BS | B | Treat as 1D |
| 240 | Search a 2D Matrix II | Med | BS | G | From corner |
| 4 | Median of Two Sorted Arrays | Hard | BS | G★ | Classic hard |
| 378 | Kth Smallest Element in Sorted Matrix | Med | BS | G | Binary on value |
| 658 | Find K Closest Elements | Med | BS | G | Binary + expand |

---

## SECTION 5: Stack & Queue (50 problems)

### Basic Stack
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 20 | Valid Parentheses | Easy | Stack | B★ | Classic |
| 155 | Min Stack | Med | Stack | B★ | Track min |
| 232 | Implement Queue using Stacks | Easy | Stack | B | Two stacks |
| 225 | Implement Stack using Queues | Easy | Queue | B | Push expensive |
| 150 | Evaluate Reverse Polish Notation | Med | Stack | B | Operators |
| 227 | Basic Calculator II | Med | Stack | G | +, -, *, / |
| 224 | Basic Calculator | Hard | Stack | G | With parentheses |
| 394 | Decode String | Med | Stack | B★ | Nested encoding |
| 636 | Exclusive Time of Functions | Med | Stack | M★ | Call stack |

### Monotonic Stack
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 739 | Daily Temperatures | Med | Mono | B★ | Next greater |
| 496 | Next Greater Element I | Easy | Mono | M | Hash + stack |
| 503 | Next Greater Element II | Med | Mono | G | Circular array |
| 907 | Sum of Subarray Minimums | Med | Mono | G★ | Contribution |
| 901 | Online Stock Span | Med | Mono | M | Previous greater |
| 735 | Asteroid Collision | Med | Stack | M★ | Simulation |
| 402 | Remove K Digits | Med | Mono | G | Greedy + stack |
| 84 | Largest Rectangle in Histogram | Hard | Mono | G★ | Classic |
| 85 | Maximal Rectangle | Hard | Mono | G | 2D version |
| 962 | Maximum Width Ramp | Med | Mono | G | Decreasing stack |
| 1944 | Number of Visible People in Queue | Hard | Mono | G | From right |

---

## SECTION 6: Linked List (40 problems)

### Basic Operations
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 206 | Reverse Linked List | Easy | List | B★ | Iterative + recursive |
| 92 | Reverse Linked List II | Med | List | G | Reverse portion |
| 25 | Reverse Nodes in k-Group | Hard | List | B★ | k at a time |
| 21 | Merge Two Sorted Lists | Easy | List | B★ | Dummy head |
| 23 | Merge k Sorted Lists | Hard | Heap | B★ | K-way merge |
| 61 | Rotate List | Med | List | G | Find kth from end |
| 82 | Remove Duplicates II | Med | List | G | Keep none |
| 83 | Remove Duplicates | Easy | List | M | Keep one |
| 203 | Remove Linked List Elements | Easy | List | M | Remove value |
| 237 | Delete Node | Med | List | M | Trick question |
| 19 | Remove Nth Node From End | Med | List | B★ | Two pointers |
| 24 | Swap Nodes in Pairs | Med | List | G | Every two |
| 328 | Odd Even Linked List | Med | List | M | Separate odd/even |
| 143 | Reorder List | Med | List | M★ | Multiple steps |
| 148 | Sort List | Med | List | G | Merge sort |
| 160 | Intersection of Two Linked Lists | Easy | List | M | Length diff |
| 138 | Copy List with Random Pointer | Med | Hash | B★ | Clone with random |
| 146 | LRU Cache | Med | Design | B★ | Hash + DLL |
| 460 | LFU Cache | Hard | Design | G | Complex design |

---

## SECTION 7: Trees (80 problems)

### Tree Traversal
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 94 | Binary Tree Inorder Traversal | Easy | Tree | B | Iterative |
| 144 | Binary Tree Preorder Traversal | Easy | Tree | B | Iterative |
| 145 | Binary Tree Postorder Traversal | Easy | Tree | B | Iterative tricky |
| 102 | Binary Tree Level Order | Med | BFS | B★ | Queue |
| 103 | Binary Tree Zigzag Level Order | Med | BFS | M | Alternate direction |
| 107 | Binary Tree Level Order II | Med | BFS | M | Bottom up |
| 199 | Binary Tree Right Side View | Med | BFS | B★ | Rightmost each level |
| 314 | Binary Tree Vertical Order | Med | BFS | M | Column index |
| 987 | Vertical Order Traversal | Hard | BFS | G | Strict ordering |

### Tree Properties
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 104 | Maximum Depth | Easy | DFS | B | Recursion |
| 111 | Minimum Depth | Easy | BFS | B | BFS faster |
| 100 | Same Tree | Easy | DFS | B | Compare |
| 101 | Symmetric Tree | Easy | DFS | B | Mirror |
| 110 | Balanced Binary Tree | Easy | DFS | M | Height check |
| 226 | Invert Binary Tree | Easy | DFS | B | Swap children |
| 617 | Merge Two Binary Trees | Easy | DFS | M | Add values |
| 543 | Diameter of Binary Tree | Easy | DFS | B★ | Path through node |
| 662 | Maximum Width | Med | BFS | G | Index tracking |

### Path Problems
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 112 | Path Sum | Easy | DFS | B | Target sum |
| 113 | Path Sum II | Med | DFS | G | All paths |
| 437 | Path Sum III | Med | Prefix | M★ | Any start/end |
| 129 | Sum Root to Leaf Numbers | Med | DFS | M | Form numbers |
| 124 | Binary Tree Maximum Path Sum | Hard | DFS | B★ | Global max |
| 687 | Longest Univalue Path | Med | DFS | G | Same value |

### BST Problems
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 98 | Validate Binary Search Tree | Med | DFS | B★ | Bounds or inorder |
| 99 | Recover Binary Search Tree | Med | Inorder | G | Two swapped |
| 230 | Kth Smallest Element in BST | Med | Inorder | B | Count |
| 235 | Lowest Common Ancestor of BST | Med | BST | B | Use BST property |
| 236 | Lowest Common Ancestor of Binary Tree | Med | DFS | B★ | General tree |
| 450 | Delete Node in BST | Med | BST | G | Three cases |
| 700 | Search in BST | Easy | BST | M | Recursive/iterative |
| 701 | Insert into BST | Med | BST | M | Find position |
| 108 | Convert Sorted Array to BST | Easy | BST | M | Mid as root |
| 109 | Convert Sorted List to BST | Med | BST | G | Find middle |
| 173 | Binary Search Tree Iterator | Med | Stack | G | Inorder iterator |
| 530 | Minimum Absolute Difference in BST | Easy | Inorder | M | Adjacent in inorder |

### Tree Construction
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 105 | Construct from Preorder and Inorder | Med | Tree | B★ | Classic |
| 106 | Construct from Inorder and Postorder | Med | Tree | G | Similar |
| 889 | Construct from Preorder and Postorder | Med | Tree | G | Not unique |
| 114 | Flatten Binary Tree to Linked List | Med | DFS | G | Preorder flatten |
| 297 | Serialize and Deserialize Binary Tree | Hard | BFS/DFS | B★ | Design |
| 428 | Serialize and Deserialize N-ary Tree | Hard | BFS/DFS | G | N-ary version |

### Special Trees
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 222 | Count Complete Tree Nodes | Med | BS | G | O(log²n) |
| 863 | All Nodes Distance K | Med | BFS | M★ | Build parent map |
| 1110 | Delete Nodes And Return Forest | Med | DFS | G | Return roots |

---

## SECTION 8: Graphs (90 problems)

### BFS
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 200 | Number of Islands | Med | BFS/DFS | B★ | Grid classic |
| 695 | Max Area of Island | Med | DFS | M | Track area |
| 733 | Flood Fill | Easy | BFS/DFS | M | Paint fill |
| 542 | 01 Matrix | Med | BFS | B★ | Multi-source |
| 994 | Rotting Oranges | Med | BFS | M★ | Multi-source |
| 1091 | Shortest Path in Binary Matrix | Med | BFS | G | 8 directions |
| 286 | Walls and Gates | Med | BFS | M | Multi-source |
| 127 | Word Ladder | Hard | BFS | G★ | Transform |
| 126 | Word Ladder II | Hard | BFS+DFS | G | All paths |
| 752 | Open the Lock | Med | BFS | G | State space |
| 815 | Bus Routes | Hard | BFS | G | Graph on routes |
| 1293 | Shortest Path with Obstacles Elimination | Hard | BFS | G | 3D BFS |

### DFS
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 130 | Surrounded Regions | Med | DFS | B | Boundary DFS |
| 417 | Pacific Atlantic Water Flow | Med | DFS | M★ | From oceans |
| 1254 | Number of Closed Islands | Med | DFS | M | Boundary check |
| 79 | Word Search | Med | DFS | B★ | Backtracking |
| 212 | Word Search II | Hard | Trie+DFS | G | Multiple words |
| 329 | Longest Increasing Path in Matrix | Hard | DFS+Memo | G★ | With memoization |
| 934 | Shortest Bridge | Med | BFS+DFS | G | Two islands |

### Topological Sort
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 207 | Course Schedule | Med | Topo | B★ | Cycle detection |
| 210 | Course Schedule II | Med | Topo | B★ | Return order |
| 269 | Alien Dictionary | Hard | Topo | G★ | Build graph |
| 310 | Minimum Height Trees | Med | Topo | G | Remove leaves |
| 444 | Sequence Reconstruction | Med | Topo | G | Unique order |
| 802 | Find Eventual Safe States | Med | Topo | M | Reverse edges |

### Union-Find (DSU) ⭐ YOUR WEAK AREA
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 721 | Accounts Merge | Med | DSU | M★ | ⭐ YOUR INTERVIEW |
| 547 | Number of Provinces | Med | DSU | B | Basic DSU |
| 684 | Redundant Connection | Med | DSU | B★ | Cycle detection |
| 685 | Redundant Connection II | Hard | DSU | G | Directed graph |
| 990 | Satisfiability of Equality Equations | Med | DSU | G | Equality groups |
| 1101 | Earliest Moment When Everyone Become Friends | Med | DSU | M★ | Time-based |
| 765 | Couples Holding Hands | Hard | DSU | G | Swap counting |
| 839 | Similar String Groups | Hard | DSU | G | String similarity |
| 952 | Largest Component Size by Common Factor | Hard | DSU | G | Math + DSU |
| 1202 | Smallest String With Swaps | Med | DSU | G | Sort within groups |
| 399 | Evaluate Division | Med | DFS/DSU | M | Weighted graph |
| 2092 | Find All People With Secret | Hard | DSU | G | Time-ordered |

### Shortest Path
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 743 | Network Delay Time | Med | Dijkstra | G★ | Classic |
| 787 | Cheapest Flights Within K Stops | Med | BFS/DP | G★ | With constraint |
| 1514 | Path with Maximum Probability | Med | Dijkstra | G | Max product |
| 778 | Swim in Rising Water | Hard | BS+BFS | G | Binary on answer |
| 1368 | Minimum Cost to Make Valid Path | Hard | 0-1 BFS | G | Deque BFS |

### Advanced Graph
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 133 | Clone Graph | Med | BFS/DFS | B | Clone with hash |
| 261 | Graph Valid Tree | Med | DSU | G | n-1 edges, connected |
| 323 | Number of Connected Components | Med | DSU | M | Count roots |
| 1192 | Critical Connections | Hard | Tarjan | G | Bridge finding |
| 909 | Snakes and Ladders | Med | BFS | G | Board to index |

---

## SECTION 9: Dynamic Programming (100 problems)

### 1D DP
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 70 | Climbing Stairs | Easy | DP | B | Fibonacci |
| 746 | Min Cost Climbing Stairs | Easy | DP | M | With cost |
| 198 | House Robber | Med | DP | B★ | Classic |
| 213 | House Robber II | Med | DP | B | Circular |
| 337 | House Robber III | Med | TreeDP | G | Tree version |
| 91 | Decode Ways | Med | DP | B★ | String DP |
| 639 | Decode Ways II | Hard | DP | G | With wildcards |
| 139 | Word Break | Med | DP | B★ | String DP |
| 140 | Word Break II | Hard | DP+Back | G | All ways |
| 152 | Maximum Product Subarray | Med | DP | B★ | Track min/max |
| 53 | Maximum Subarray | Med | DP | B★ | Kadane |
| 121 | Best Time to Buy and Sell Stock | Easy | DP | B★ | One transaction |
| 122 | Best Time to Buy and Sell Stock II | Med | Greedy | B | Unlimited |
| 123 | Best Time to Buy and Sell Stock III | Hard | DP | G★ | Two transactions |
| 188 | Best Time to Buy and Sell Stock IV | Hard | DP | G | k transactions |
| 309 | Best Time with Cooldown | Med | DP | G | State machine |
| 714 | Best Time with Transaction Fee | Med | DP | G | With fee |
| 300 | Longest Increasing Subsequence | Med | DP | B★ | Binary search O(n log n) |
| 354 | Russian Doll Envelopes | Hard | DP | G | 2D LIS |
| 673 | Number of LIS | Med | DP | G | Count ways |
| 334 | Increasing Triplet Subsequence | Med | Greedy | M | O(1) space |

### 2D DP
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 62 | Unique Paths | Med | DP | B | Grid |
| 63 | Unique Paths II | Med | DP | B | With obstacles |
| 64 | Minimum Path Sum | Med | DP | B | Grid sum |
| 120 | Triangle | Med | DP | M | Bottom-up |
| 931 | Minimum Falling Path Sum | Med | DP | M | Grid min |
| 221 | Maximal Square | Med | DP | B★ | 2D grid |
| 1277 | Count Square Submatrices | Med | DP | G | Similar to 221 |
| 72 | Edit Distance | Med | DP | B★ | Classic |
| 1143 | Longest Common Subsequence | Med | DP | B★ | Classic |
| 583 | Delete Operation for Two Strings | Med | DP | G | LCS variant |
| 712 | Minimum ASCII Delete Sum | Med | DP | G | LCS variant |
| 10 | Regular Expression Matching | Hard | DP | G★ | Pattern matching |
| 44 | Wildcard Matching | Hard | DP | G | Simpler than 10 |
| 97 | Interleaving String | Med | DP | G | Three strings |
| 115 | Distinct Subsequences | Hard | DP | G | Count ways |

### Knapsack Type
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 416 | Partition Equal Subset Sum | Med | DP | B★ | 0/1 knapsack |
| 494 | Target Sum | Med | DP | B | +/- assignment |
| 322 | Coin Change | Med | DP | B★ | Unbounded |
| 518 | Coin Change II | Med | DP | B | Count ways |
| 279 | Perfect Squares | Med | DP/BFS | B | Unbounded |
| 377 | Combination Sum IV | Med | DP | G | Order matters |
| 474 | Ones and Zeroes | Med | DP | G | 3D knapsack |
| 1049 | Last Stone Weight II | Med | DP | G | Minimize diff |

### Interval DP
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 516 | Longest Palindromic Subsequence | Med | DP | G | Interval |
| 312 | Burst Balloons | Hard | DP | G | Last balloon |
| 1312 | Minimum Insertions for Palindrome | Hard | DP | G | LPS variant |
| 1000 | Minimum Cost to Merge Stones | Hard | DP | G | Interval merge |

### State Machine DP
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 265 | Paint House II | Hard | DP | G | K colors |
| 256 | Paint House | Med | DP | G | 3 colors |
| 276 | Paint Fence | Med | DP | G | Same/diff |

---

## SECTION 10: Heap / Priority Queue (35 problems)

| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 215 | Kth Largest Element | Med | Heap | B★ | QuickSelect |
| 347 | Top K Frequent Elements | Med | Heap | B★ | Bucket sort O(n) |
| 692 | Top K Frequent Words | Med | Heap | G | Custom sort |
| 703 | Kth Largest Element in Stream | Easy | Heap | M | Min heap size k |
| 973 | K Closest Points to Origin | Med | Heap | M★ | Max heap |
| 23 | Merge k Sorted Lists | Hard | Heap | B★ | K-way merge |
| 295 | Find Median from Data Stream | Hard | Heap | B★ | Two heaps |
| 480 | Sliding Window Median | Hard | Heap | G | Two heaps + lazy |
| 253 | Meeting Rooms II | Med | Heap | M★ | Min heap |
| 621 | Task Scheduler | Med | Heap | M★ | Greedy + heap |
| 767 | Reorganize String | Med | Heap | M★ | Same as 621 |
| 373 | Find K Pairs with Smallest Sums | Med | Heap | G | K-way merge |
| 378 | Kth Smallest Element in Sorted Matrix | Med | Heap | G | K-way merge |
| 632 | Smallest Range Covering Elements | Hard | Heap | G | K pointers |
| 355 | Design Twitter | Med | Design | G | Heap + merge |
| 1834 | Single-Threaded CPU | Med | Heap | M★ | Event simulation |
| 2054 | Two Best Non-Overlapping Events | Med | Heap | M | Sweep line |

---

## SECTION 11: Backtracking (40 problems)

### Subsets & Combinations
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 78 | Subsets | Med | Back | B★ | Power set |
| 90 | Subsets II | Med | Back | B | With duplicates |
| 77 | Combinations | Med | Back | B | nCk |
| 39 | Combination Sum | Med | Back | B★ | Reuse allowed |
| 40 | Combination Sum II | Med | Back | B | No reuse |
| 216 | Combination Sum III | Med | Back | G | k numbers |
| 377 | Combination Sum IV | Med | DP | G | Count ways |

### Permutations
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 46 | Permutations | Med | Back | B★ | Classic |
| 47 | Permutations II | Med | Back | B | With duplicates |
| 31 | Next Permutation | Med | Array | G★ | In-place |
| 60 | Permutation Sequence | Hard | Math | G | k-th permutation |
| 784 | Letter Case Permutation | Med | Back | M | Case variants |

### Grid Backtracking
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 79 | Word Search | Med | Back | B★ | Grid search |
| 212 | Word Search II | Hard | Trie+Back | G | Multiple words |
| 51 | N-Queens | Hard | Back | G★ | Classic |
| 52 | N-Queens II | Hard | Back | G | Count only |
| 37 | Sudoku Solver | Hard | Back | G | Constraint prop |
| 980 | Unique Paths III | Hard | Back | G | Visit all |

### String Backtracking
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 17 | Letter Combinations of Phone | Med | Back | B★ | Phone keypad |
| 22 | Generate Parentheses | Med | Back | B★ | Valid parens |
| 131 | Palindrome Partitioning | Med | Back | G | All partitions |
| 93 | Restore IP Addresses | Med | Back | G | Valid IPs |
| 282 | Expression Add Operators | Hard | Back | G | +, -, * |
| 241 | Different Ways to Add Parentheses | Med | DC | G | All parenthesizations |

---

## SECTION 12: Design Problems (30 problems)

### Data Structure Design ⭐ YOUR WEAK AREA
| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 1146 | Snapshot Array | Med | Design | G★ | ⭐ YOUR INTERVIEW |
| 981 | Time Based Key-Value Store | Med | Design | G★ | Versioning |
| 146 | LRU Cache | Med | Design | B★ | Hash + DLL |
| 460 | LFU Cache | Hard | Design | G | Complex |
| 380 | Insert Delete GetRandom O(1) | Med | Design | M★ | Array + hash |
| 381 | Insert Delete GetRandom Duplicates | Hard | Design | G | With duplicates |
| 155 | Min Stack | Med | Design | B★ | Track min |
| 716 | Max Stack | Hard | Design | G | Doubly linked |
| 208 | Implement Trie | Med | Trie | B★ | Prefix tree |
| 211 | Design Add and Search Words | Med | Trie | G | With wildcards |
| 1472 | Design Browser History | Med | Design | M | Back/forward |
| 341 | Flatten Nested List Iterator | Med | Stack | M | Iterator |
| 173 | Binary Search Tree Iterator | Med | Stack | G | Inorder iterator |
| 284 | Peeking Iterator | Med | Design | G | Wrapper |
| 355 | Design Twitter | Med | Design | G | Heap + merge |
| 535 | Encode and Decode TinyURL | Med | Hash | M | URL shortener |
| 2296 | Design a Text Editor | Hard | Design | G | Cursor ops |
| 729 | My Calendar I | Med | Design | G | Interval insert |
| 731 | My Calendar II | Med | Design | G | Allow double book |
| 732 | My Calendar III | Hard | Design | G | Sweep line |

---

## SECTION 13: Trie (15 problems)

| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 208 | Implement Trie | Med | Trie | B★ | Basic |
| 211 | Design Add and Search Words | Med | Trie | G | Wildcard |
| 212 | Word Search II | Hard | Trie+DFS | G | Multiple words |
| 648 | Replace Words | Med | Trie | G | Dictionary roots |
| 677 | Map Sum Pairs | Med | Trie | G | Sum with prefix |
| 745 | Prefix and Suffix Search | Hard | Trie | G | Complex design |
| 1268 | Search Suggestions System | Med | Trie | M★ | Autocomplete |
| 1233 | Remove Sub-Folders | Med | Trie | G | Path prefix |
| 1044 | Longest Duplicate Substring | Hard | BS+Hash | G | Rolling hash |
| 421 | Maximum XOR of Two Numbers | Med | Trie | G | Bit trie |

---

## SECTION 14: Greedy (35 problems)

| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 55 | Jump Game | Med | Greedy | B★ | Can reach |
| 45 | Jump Game II | Med | Greedy | B | Min jumps |
| 134 | Gas Station | Med | Greedy | G★ | Circular |
| 135 | Candy | Hard | Greedy | G | Two passes |
| 455 | Assign Cookies | Easy | Greedy | M | Sort both |
| 605 | Can Place Flowers | Easy | Greedy | M | Check neighbors |
| 763 | Partition Labels | Med | Greedy | G★ | Last occurrence |
| 406 | Queue Reconstruction by Height | Med | Greedy | G | Sort + insert |
| 435 | Non-overlapping Intervals | Med | Greedy | G | Sort by end |
| 452 | Minimum Arrows | Med | Greedy | G | Same as 435 |
| 621 | Task Scheduler | Med | Greedy | M★ | With idle |
| 846 | Hand of Straights | Med | Greedy | G | Consecutive |
| 1326 | Minimum Number of Taps | Hard | Greedy | G | Jump game variant |
| 1353 | Maximum Events | Med | Greedy | G | Heap + greedy |
| 1899 | Merge Triplets to Form Target | Med | Greedy | G | Check each |
| 678 | Valid Parenthesis String | Med | Greedy | M | Track range |

---

## SECTION 15: Bit Manipulation (25 problems)

| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 136 | Single Number | Easy | Bit | B★ | XOR |
| 137 | Single Number II | Med | Bit | G | Count bits |
| 260 | Single Number III | Med | Bit | G | Separate groups |
| 191 | Number of 1 Bits | Easy | Bit | B | Hamming weight |
| 338 | Counting Bits | Easy | Bit | M | DP |
| 190 | Reverse Bits | Easy | Bit | M | Bit by bit |
| 231 | Power of Two | Easy | Bit | B | n & (n-1) |
| 268 | Missing Number | Easy | Bit | M | XOR all |
| 371 | Sum of Two Integers | Med | Bit | G | No arithmetic |
| 389 | Find the Difference | Easy | Bit | M | XOR |
| 461 | Hamming Distance | Easy | Bit | M | XOR + count |
| 477 | Total Hamming Distance | Med | Bit | G | Count per bit |
| 898 | Bitwise ORs of Subarrays | Med | Bit | G | Unique ORs |
| 421 | Maximum XOR | Med | Trie | G | Bit trie |

---

## SECTION 16: Math & Simulation (30 problems)

| # | Problem | Diff | Pattern | Co. | Notes |
|---|---------|------|---------|-----|-------|
| 7 | Reverse Integer | Med | Math | B | Overflow |
| 9 | Palindrome Number | Easy | Math | B | No string |
| 50 | Pow(x, n) | Med | Math | B★ | Fast power |
| 69 | Sqrt(x) | Easy | Math | B | Binary search |
| 29 | Divide Two Integers | Med | Math | G | Bit shifting |
| 166 | Fraction to Recurring Decimal | Med | Hash | G | Cycle detection |
| 172 | Factorial Trailing Zeroes | Med | Math | M | Count 5s |
| 202 | Happy Number | Easy | Hash | M | Cycle detection |
| 204 | Count Primes | Med | Math | G | Sieve |
| 273 | Integer to English Words | Hard | String | G★ | Groups of 3 |
| 43 | Multiply Strings | Med | String | G | School method |
| 66 | Plus One | Easy | Array | B | Carry |
| 67 | Add Binary | Easy | String | B | Carry |
| 2 | Add Two Numbers | Med | List | B★ | Digit by digit |
| 365 | Water and Jug Problem | Med | Math | G | GCD |
| 593 | Valid Square | Med | Math | G | Check distances |
| 223 | Rectangle Area | Med | Math | G | Overlap |
| 149 | Max Points on a Line | Hard | Math | G | GCD for slope |
| 470 | Implement Rand10 Using Rand7 | Med | Prob | G | Rejection sampling |
| 528 | Random Pick with Weight | Med | Prob | G★ | Prefix sum + BS |

---

## Google-Style Scenario Wrappers

Google wraps standard problems in practical scenarios. Practice recognizing them:

| LC Problem | Google-Style Scenario |
|------------|----------------------|
| 1146 Snapshot Array | "Design a version control system for configuration" |
| 721 Accounts Merge | "Deduplicate user profiles across systems" |
| 56 Merge Intervals | "Optimize calendar booking slots" |
| 200 Number of Islands | "Count disconnected server clusters" |
| 207 Course Schedule | "Validate build dependency order" |
| 146 LRU Cache | "Design a memory-efficient page cache" |
| 127 Word Ladder | "Find shortest refactoring path between code versions" |
| 621 Task Scheduler | "Optimize batch job scheduling with cooldowns" |
| 743 Network Delay Time | "Calculate propagation time in a distributed system" |
| 76 Minimum Window Substring | "Find smallest log segment containing all error types" |

---

## Meta-Style Constraint Variations

Meta typically modifies:
- Output format
- Constraint boundaries
- Edge case requirements

| LC Problem | Meta Variation |
|------------|---------------|
| 1 Two Sum | "Return indices in descending order" |
| 15 3Sum | "Return count instead of triplets" |
| 200 Number of Islands | "Return list of island sizes" |
| 56 Merge Intervals | "Return non-overlapping gaps instead" |
| 102 Level Order | "Return only odd-level nodes" |
| 46 Permutations | "Return only permutations with specific property" |
| 215 Kth Largest | "Return k largest elements sorted" |

---

## Problem Count Summary

| Category | Easy | Medium | Hard | Total |
|----------|------|--------|------|-------|
| Arrays & Hashing | 25 | 70 | 10 | 105 |
| Two Pointers | 5 | 15 | 5 | 25 |
| Sliding Window | 5 | 40 | 10 | 55 |
| Binary Search | 10 | 35 | 10 | 55 |
| Stack & Queue | 5 | 30 | 10 | 45 |
| Linked List | 10 | 25 | 5 | 40 |
| Trees | 20 | 45 | 15 | 80 |
| Graphs | 5 | 55 | 25 | 85 |
| Dynamic Programming | 10 | 60 | 30 | 100 |
| Heap | 5 | 20 | 10 | 35 |
| Backtracking | 0 | 30 | 10 | 40 |
| Design | 0 | 20 | 10 | 30 |
| Trie | 0 | 10 | 5 | 15 |
| Greedy | 5 | 25 | 5 | 35 |
| Bit Manipulation | 10 | 12 | 3 | 25 |
| Math | 8 | 15 | 7 | 30 |
| **Total** | **123** | **507** | **170** | **800** |

---

## Weekly Practice Schedule

### Week 1-2: Priority 0 + Priority 1
- HistorySet, Snapshot Array, Time-Based KV
- Accounts Merge, Union-Find basics
- Target: 25 problems

### Week 3-4: Arrays & Two Pointers
- Two Sum variants, Sliding Window
- Target: 30 problems

### Week 5-6: Trees & Graphs
- Tree traversals, BFS/DFS, Topological Sort
- Target: 40 problems

### Week 7-8: DP & Design
- 1D/2D DP, Design problems
- Mock interviews
- Target: 30 problems + 4 mocks
