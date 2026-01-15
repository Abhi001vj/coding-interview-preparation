# Google Interview Scenario Wrappers

## Overview

Google wraps standard algorithm problems in practical, real-world scenarios. This makes pattern recognition harder but tests if you can extract the core problem from business requirements.

**Key Insight**: The underlying algorithm is usually the same as a standard LeetCode problem, but wrapped in Google-specific language around products like Google Docs, YouTube, Maps, Gmail, etc.

---

## How Google Presents Problems

### Standard LeetCode Format
```
Given an array of integers and a target, find two numbers that add up to target.
```

### Google Scenario Format
```
You're building a shopping cart feature for Google Shopping. Given a list of item
prices and a gift card balance, find which two items the customer can buy to use
up exactly the gift card amount. Return the item indices.
```

**Same algorithm (Two Sum), different presentation.**

---

## Scenario Wrapper Examples by Pattern

### Pattern 1: Snapshot/Versioning (YOUR INTERVIEW QUESTION)

#### Standard: LC1146 Snapshot Array
```
Implement a SnapshotArray that supports:
- set(index, val)
- snap() - takes a snapshot and returns snap_id
- get(index, snap_id) - returns value at snap time
```

#### Google Scenario: HistorySet (Your Actual Interview)
```
Design a data structure for Google Docs that tracks document collaborators:
- add(user) adds a collaborator, returns operation_id
- remove(user) removes a collaborator, returns operation_id
- members(op_id) returns the set of collaborators at that point

This allows "time travel" to see who was collaborating at any past operation.
```

#### Google Scenario: Document Version Control
```
You're building version control for Google Docs. Users can:
- edit(doc_id, content) - saves a new version
- history(doc_id, version) - retrieves content at that version
- diff(doc_id, v1, v2) - shows what changed between versions

Design the system to minimize storage while supporting fast retrieval.
```

#### Google Scenario: Config Management
```
Google services have configuration that changes over time. Design:
- setConfig(key, value) at timestamp
- getConfig(key, timestamp) returns value at that time
- Changes should be retrievable at any past timestamp
```

---

### Pattern 2: Union-Find / DSU

#### Standard: LC721 Accounts Merge
```
Given list of accounts [name, email1, email2, ...], merge accounts
belonging to same person (share any email).
```

#### Google Scenario: User Account Linking (Similar to your Meta question)
```
Gmail users sometimes create multiple accounts. Given a list of accounts with
their associated phone numbers and recovery emails, merge accounts that likely
belong to the same person. Two accounts belong to the same person if they share
any identifier (phone, recovery email, or secondary email).
```

#### Google Scenario: Data Center Connectivity
```
You have N data centers. Given a list of network links [dc1, dc2] representing
direct connections, determine:
1. How many isolated networks exist?
2. What's the minimum links needed to connect all data centers?
3. If a link fails, does the network become disconnected?
```

#### Google Scenario: Synonym Groups
```
For Google Search, you're given pairs of words that are synonyms.
Given a query, find all equivalent queries by replacing words with synonyms.
Synonyms are transitive: if A=B and B=C, then A=C.
```

---

### Pattern 3: Sliding Window

#### Standard: LC3 Longest Substring Without Repeating Characters
```
Given a string, find the length of the longest substring without repeating characters.
```

#### Google Scenario: Session Analysis
```
YouTube wants to analyze watch sessions. Given a stream of video IDs watched
in order, find the longest continuous watching period where the user didn't
rewatch any video. Return the duration (number of videos).
```

#### Google Scenario: API Rate Limiting
```
Design a rate limiter for Google Cloud API. Given timestamps of API calls from
a user, find the maximum number of calls in any K-second window. Alert if it
exceeds the limit.
```

#### Standard: LC76 Minimum Window Substring
```
Given strings s and t, find minimum window in s containing all chars of t.
```

#### Google Scenario: Log Analysis
```
You're analyzing server logs. Given a stream of log types and a set of error
types we need to investigate, find the shortest continuous log segment that
contains at least one occurrence of each error type we're investigating.
```

---

### Pattern 4: Graph BFS/DFS

#### Standard: LC200 Number of Islands
```
Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
```

#### Google Scenario: Wifi Coverage Analysis
```
Google is planning WiFi coverage for a building floor plan. Given a 2D grid
where 1 represents areas that need coverage and 0 represents walls/obstacles,
determine how many separate coverage zones exist (areas connected horizontally
or vertically that all need coverage).
```

#### Standard: LC207/210 Course Schedule
```
Given prerequisites, determine if all courses can be finished.
```

#### Google Scenario: Build System Dependencies
```
Google's build system has targets with dependencies. Given a list of build
targets and their dependencies, determine:
1. Is there a valid build order?
2. If yes, what's one valid order?
3. Which targets are causing cycles (if any)?
```

#### Google Scenario: Ad Campaign Scheduling
```
You have N ad campaigns. Some campaigns can't run together due to conflicts.
Given pairs of conflicting campaigns and a maximum of K simultaneous slots,
determine if all campaigns can be scheduled.
```

---

### Pattern 5: Binary Search

#### Standard: LC875 Koko Eating Bananas
```
Koko can eat bananas at speed K. Find minimum K to eat all piles in H hours.
```

#### Google Scenario: Server Provisioning
```
You're scaling Google Cloud VMs. Given N tasks with their processing requirements
and a deadline T, find the minimum VM capacity (processing power per hour) needed
to complete all tasks by the deadline. Each VM processes one task at a time.
```

#### Standard: LC1011 Capacity To Ship Packages
```
Find minimum ship capacity to ship all packages in D days.
```

#### Google Scenario: Video Transcoding
```
YouTube needs to transcode N video chunks. Given processing times for each chunk
and K transcoding servers, find the minimum server processing capacity needed
to transcode everything within T hours, given chunks must be processed in order
on each server.
```

---

### Pattern 6: Dynamic Programming

#### Standard: LC322 Coin Change
```
Find minimum coins needed to make amount.
```

#### Google Scenario: Cloud Storage Optimization
```
Google Cloud offers storage tiers: hot ($10/GB), warm ($5/GB), cold ($1/GB).
Moving data between tiers costs $2 per move. Given data access patterns over
N months, find the minimum cost storage strategy.
```

#### Standard: LC1143 Longest Common Subsequence
```
Find LCS of two strings.
```

#### Google Scenario: Merge Conflict Resolution
```
In Google Docs collaborative editing, two users make different edits to a
document. Given the original text and both edited versions, find the longest
sequence of characters that both users kept unchanged, preserving order.
```

---

### Pattern 7: Heap/Priority Queue

#### Standard: LC253 Meeting Rooms II
```
Find minimum conference rooms required.
```

#### Google Scenario: Video Conference Load Balancing
```
Google Meet runs on servers with limited capacity. Given a schedule of
meetings with start/end times, determine the minimum number of servers
needed so every meeting can run. Each server handles one meeting at a time.
```

#### Standard: LC295 Find Median from Data Stream
```
Design data structure to find running median.
```

#### Google Scenario: Latency Monitoring
```
For Google Search, we track query latencies. Design a system that supports:
- recordLatency(ms) - records a latency measurement
- getMedianLatency() - returns current median latency

The system should work efficiently for millions of requests per second.
```

---

### Pattern 8: Tree Operations

#### Standard: LC236 Lowest Common Ancestor
```
Find LCA of two nodes in a binary tree.
```

#### Google Scenario: Organization Chart
```
Given Google's org chart as a tree structure, find the lowest-level manager
who manages both employee A and employee B (directly or indirectly).
```

#### Standard: LC297 Serialize/Deserialize Binary Tree
```
Design serialization/deserialization for binary tree.
```

#### Google Scenario: File System Sync
```
Design a system to sync a file system tree between two machines. You need:
- serialize(root) - converts tree to string for network transfer
- deserialize(data) - reconstructs the tree on the other machine

The format should be space-efficient for large directory structures.
```

---

## Common Google Scenario Themes

### Products Frequently Referenced
| Product | Common Problem Types |
|---------|---------------------|
| Google Docs | Versioning, collaboration, diff/merge |
| YouTube | Streaming, recommendations, scheduling |
| Google Maps | Graphs, shortest path, regions |
| Gmail | Filtering, classification, threading |
| Google Cloud | Resource allocation, scheduling |
| Google Search | Ranking, text processing, indexing |
| Google Meet | Scheduling, load balancing |
| Android | Resource management, app lifecycle |

### Common Scenario Patterns
1. **Multi-tenancy**: Multiple users/accounts/services sharing resources
2. **Temporal**: Time-based queries, versioning, snapshots
3. **Scale**: Handling millions/billions of requests
4. **Distributed**: Data across multiple servers/regions
5. **Real-time**: Streaming data, live updates

---

## Practice Strategy

### Step 1: Solve Standard Problem
Solve the LeetCode version first. Understand the algorithm thoroughly.

### Step 2: Read Google Scenario
Read the scenario version. Practice extracting:
- What's the core data structure?
- What operations are needed?
- What's the underlying algorithm?

### Step 3: Map Back
Write down: "This is basically [LC problem] because..."

### Step 4: Practice Both Ways
- Given a LeetCode problem, create your own Google scenario
- Given a scenario, identify the underlying algorithm

---

## Quick Reference: Problem to Scenario Mapping

| LeetCode | Google Scenario |
|----------|----------------|
| Two Sum | Shopping cart matching |
| Snapshot Array | Document version control |
| Accounts Merge | User account linking |
| Number of Islands | Coverage zone analysis |
| Course Schedule | Build dependency resolution |
| LRU Cache | Browser/app cache |
| Meeting Rooms II | Video conference scaling |
| Median from Stream | Latency monitoring |
| Serialize Tree | File system sync |
| Word Ladder | Search query suggestions |
| Min Window Substring | Log analysis |
| Longest Substring No Repeat | Session analysis |
| Coin Change | Resource optimization |
| LCA | Org chart queries |
| Task Scheduler | Job scheduling with cooldowns |

---

## Interview Tips for Google Scenarios

1. **Don't panic** when you don't immediately recognize the problem
2. **Ask clarifying questions** to understand the actual requirements
3. **Identify the core operation** - what data, what queries?
4. **Map to known patterns** - "This sounds like..."
5. **Confirm with interviewer** - "So essentially this is [pattern], right?"
6. **Discuss tradeoffs** - Google loves hearing about scale considerations
