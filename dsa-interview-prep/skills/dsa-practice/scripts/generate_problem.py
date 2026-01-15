#!/usr/bin/env python3
"""
DSA Problem Generator

Generates practice problems based on weak patterns and difficulty preferences.
Supports company-specific variations (Google scenarios, Meta constraints).
Integrates with problem-bank.md and tracks progress.
"""

import argparse
import json
import random
from pathlib import Path
from datetime import datetime

# Pattern definitions with associated problems
# Each problem has: id, name, url, company (G=Google, M=Meta, B=Both)
PROBLEM_BANK = {
    "snapshot-versioning": {
        "easy": [],
        "medium": [
            {"id": "LC1146", "name": "Snapshot Array", "url": "https://leetcode.com/problems/snapshot-array/", "company": "G"},
            {"id": "CUSTOM1", "name": "HistorySet", "url": None, "company": "G"},
            {"id": "LC981", "name": "Time Based Key-Value Store", "url": "https://leetcode.com/problems/time-based-key-value-store/", "company": "G"},
        ],
        "hard": []
    },
    "union-find": {
        "easy": [],
        "medium": [
            {"id": "LC721", "name": "Accounts Merge", "url": "https://leetcode.com/problems/accounts-merge/", "company": "B"},
            {"id": "LC547", "name": "Number of Provinces", "url": "https://leetcode.com/problems/number-of-provinces/", "company": "B"},
            {"id": "LC684", "name": "Redundant Connection", "url": "https://leetcode.com/problems/redundant-connection/", "company": "G"},
            {"id": "LC1101", "name": "Earliest Moment When Everyone Become Friends", "url": "https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/", "company": "G"},
            {"id": "CUSTOM2", "name": "URL Content Grouping", "url": None, "company": "M"},
        ],
        "hard": [
            {"id": "LC765", "name": "Couples Holding Hands", "url": "https://leetcode.com/problems/couples-holding-hands/", "company": "G"},
            {"id": "LC839", "name": "Similar String Groups", "url": "https://leetcode.com/problems/similar-string-groups/", "company": "G"},
        ]
    },
    "sliding-window": {
        "easy": [
            {"id": "LC643", "name": "Maximum Average Subarray I", "url": "https://leetcode.com/problems/maximum-average-subarray-i/", "company": "M"},
        ],
        "medium": [
            {"id": "LC3", "name": "Longest Substring Without Repeating Characters", "url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "company": "B"},
            {"id": "LC1004", "name": "Max Consecutive Ones III", "url": "https://leetcode.com/problems/max-consecutive-ones-iii/", "company": "M"},
            {"id": "LC904", "name": "Fruit Into Baskets", "url": "https://leetcode.com/problems/fruit-into-baskets/", "company": "M"},
            {"id": "LC424", "name": "Longest Repeating Character Replacement", "url": "https://leetcode.com/problems/longest-repeating-character-replacement/", "company": "B"},
            {"id": "LC567", "name": "Permutation in String", "url": "https://leetcode.com/problems/permutation-in-string/", "company": "B"},
            {"id": "LC438", "name": "Find All Anagrams in a String", "url": "https://leetcode.com/problems/find-all-anagrams-in-a-string/", "company": "B"},
        ],
        "hard": [
            {"id": "LC76", "name": "Minimum Window Substring", "url": "https://leetcode.com/problems/minimum-window-substring/", "company": "G"},
            {"id": "LC239", "name": "Sliding Window Maximum", "url": "https://leetcode.com/problems/sliding-window-maximum/", "company": "G"},
        ]
    },
    "monotonic-stack": {
        "easy": [],
        "medium": [
            {"id": "LC739", "name": "Daily Temperatures", "url": "https://leetcode.com/problems/daily-temperatures/", "company": "B"},
            {"id": "LC907", "name": "Sum of Subarray Minimums", "url": "https://leetcode.com/problems/sum-of-subarray-minimums/", "company": "G"},
            {"id": "LC901", "name": "Online Stock Span", "url": "https://leetcode.com/problems/online-stock-span/", "company": "G"},
            {"id": "LC735", "name": "Asteroid Collision", "url": "https://leetcode.com/problems/asteroid-collision/", "company": "M"},
        ],
        "hard": [
            {"id": "LC84", "name": "Largest Rectangle in Histogram", "url": "https://leetcode.com/problems/largest-rectangle-in-histogram/", "company": "G"},
            {"id": "LC85", "name": "Maximal Rectangle", "url": "https://leetcode.com/problems/maximal-rectangle/", "company": "G"},
        ]
    },
    "two-pointers": {
        "easy": [
            {"id": "LC167", "name": "Two Sum II", "url": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/", "company": "B"},
            {"id": "LC283", "name": "Move Zeroes", "url": "https://leetcode.com/problems/move-zeroes/", "company": "M"},
        ],
        "medium": [
            {"id": "LC15", "name": "3Sum", "url": "https://leetcode.com/problems/3sum/", "company": "B"},
            {"id": "LC11", "name": "Container With Most Water", "url": "https://leetcode.com/problems/container-with-most-water/", "company": "B"},
            {"id": "LC16", "name": "3Sum Closest", "url": "https://leetcode.com/problems/3sum-closest/", "company": "G"},
            {"id": "LC75", "name": "Sort Colors", "url": "https://leetcode.com/problems/sort-colors/", "company": "M"},
        ],
        "hard": [
            {"id": "LC42", "name": "Trapping Rain Water", "url": "https://leetcode.com/problems/trapping-rain-water/", "company": "B"},
        ]
    },
    "binary-search": {
        "easy": [
            {"id": "LC704", "name": "Binary Search", "url": "https://leetcode.com/problems/binary-search/", "company": "B"},
            {"id": "LC35", "name": "Search Insert Position", "url": "https://leetcode.com/problems/search-insert-position/", "company": "B"},
        ],
        "medium": [
            {"id": "LC33", "name": "Search in Rotated Sorted Array", "url": "https://leetcode.com/problems/search-in-rotated-sorted-array/", "company": "B"},
            {"id": "LC34", "name": "Find First and Last Position", "url": "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/", "company": "B"},
            {"id": "LC153", "name": "Find Minimum in Rotated Sorted Array", "url": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/", "company": "B"},
            {"id": "LC875", "name": "Koko Eating Bananas", "url": "https://leetcode.com/problems/koko-eating-bananas/", "company": "B"},
            {"id": "LC1011", "name": "Capacity To Ship Packages Within D Days", "url": "https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/", "company": "G"},
        ],
        "hard": [
            {"id": "LC4", "name": "Median of Two Sorted Arrays", "url": "https://leetcode.com/problems/median-of-two-sorted-arrays/", "company": "G"},
        ]
    },
    "dynamic-programming": {
        "easy": [
            {"id": "LC70", "name": "Climbing Stairs", "url": "https://leetcode.com/problems/climbing-stairs/", "company": "B"},
            {"id": "LC746", "name": "Min Cost Climbing Stairs", "url": "https://leetcode.com/problems/min-cost-climbing-stairs/", "company": "B"},
        ],
        "medium": [
            {"id": "LC198", "name": "House Robber", "url": "https://leetcode.com/problems/house-robber/", "company": "B"},
            {"id": "LC213", "name": "House Robber II", "url": "https://leetcode.com/problems/house-robber-ii/", "company": "G"},
            {"id": "LC322", "name": "Coin Change", "url": "https://leetcode.com/problems/coin-change/", "company": "G"},
            {"id": "LC300", "name": "Longest Increasing Subsequence", "url": "https://leetcode.com/problems/longest-increasing-subsequence/", "company": "G"},
            {"id": "LC139", "name": "Word Break", "url": "https://leetcode.com/problems/word-break/", "company": "G"},
            {"id": "LC62", "name": "Unique Paths", "url": "https://leetcode.com/problems/unique-paths/", "company": "G"},
        ],
        "hard": [
            {"id": "LC72", "name": "Edit Distance", "url": "https://leetcode.com/problems/edit-distance/", "company": "G"},
            {"id": "LC123", "name": "Best Time to Buy and Sell Stock III", "url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/", "company": "G"},
        ]
    },
    "graph-bfs-dfs": {
        "easy": [],
        "medium": [
            {"id": "LC200", "name": "Number of Islands", "url": "https://leetcode.com/problems/number-of-islands/", "company": "B"},
            {"id": "LC207", "name": "Course Schedule", "url": "https://leetcode.com/problems/course-schedule/", "company": "B"},
            {"id": "LC210", "name": "Course Schedule II", "url": "https://leetcode.com/problems/course-schedule-ii/", "company": "B"},
            {"id": "LC994", "name": "Rotting Oranges", "url": "https://leetcode.com/problems/rotting-oranges/", "company": "B"},
            {"id": "LC417", "name": "Pacific Atlantic Water Flow", "url": "https://leetcode.com/problems/pacific-atlantic-water-flow/", "company": "G"},
            {"id": "LC133", "name": "Clone Graph", "url": "https://leetcode.com/problems/clone-graph/", "company": "M"},
        ],
        "hard": [
            {"id": "LC127", "name": "Word Ladder", "url": "https://leetcode.com/problems/word-ladder/", "company": "G"},
            {"id": "LC329", "name": "Longest Increasing Path in a Matrix", "url": "https://leetcode.com/problems/longest-increasing-path-in-a-matrix/", "company": "G"},
        ]
    },
    "tree-traversal": {
        "easy": [
            {"id": "LC94", "name": "Binary Tree Inorder Traversal", "url": "https://leetcode.com/problems/binary-tree-inorder-traversal/", "company": "B"},
            {"id": "LC104", "name": "Maximum Depth of Binary Tree", "url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/", "company": "B"},
            {"id": "LC226", "name": "Invert Binary Tree", "url": "https://leetcode.com/problems/invert-binary-tree/", "company": "M"},
        ],
        "medium": [
            {"id": "LC102", "name": "Binary Tree Level Order Traversal", "url": "https://leetcode.com/problems/binary-tree-level-order-traversal/", "company": "B"},
            {"id": "LC199", "name": "Binary Tree Right Side View", "url": "https://leetcode.com/problems/binary-tree-right-side-view/", "company": "M"},
            {"id": "LC236", "name": "Lowest Common Ancestor", "url": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/", "company": "M"},
            {"id": "LC105", "name": "Construct Binary Tree from Preorder and Inorder", "url": "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/", "company": "G"},
            {"id": "LC98", "name": "Validate Binary Search Tree", "url": "https://leetcode.com/problems/validate-binary-search-tree/", "company": "M"},
            {"id": "LC543", "name": "Diameter of Binary Tree", "url": "https://leetcode.com/problems/diameter-of-binary-tree/", "company": "M"},
        ],
        "hard": [
            {"id": "LC124", "name": "Binary Tree Maximum Path Sum", "url": "https://leetcode.com/problems/binary-tree-maximum-path-sum/", "company": "M"},
            {"id": "LC297", "name": "Serialize and Deserialize Binary Tree", "url": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/", "company": "B"},
        ]
    },
    "heap-priority-queue": {
        "easy": [
            {"id": "LC703", "name": "Kth Largest Element in a Stream", "url": "https://leetcode.com/problems/kth-largest-element-in-a-stream/", "company": "M"},
        ],
        "medium": [
            {"id": "LC215", "name": "Kth Largest Element in an Array", "url": "https://leetcode.com/problems/kth-largest-element-in-an-array/", "company": "B"},
            {"id": "LC347", "name": "Top K Frequent Elements", "url": "https://leetcode.com/problems/top-k-frequent-elements/", "company": "B"},
            {"id": "LC621", "name": "Task Scheduler", "url": "https://leetcode.com/problems/task-scheduler/", "company": "M"},
            {"id": "LC253", "name": "Meeting Rooms II", "url": "https://leetcode.com/problems/meeting-rooms-ii/", "company": "M"},
        ],
        "hard": [
            {"id": "LC23", "name": "Merge k Sorted Lists", "url": "https://leetcode.com/problems/merge-k-sorted-lists/", "company": "B"},
            {"id": "LC295", "name": "Find Median from Data Stream", "url": "https://leetcode.com/problems/find-median-from-data-stream/", "company": "G"},
        ]
    },
    "backtracking": {
        "easy": [],
        "medium": [
            {"id": "LC46", "name": "Permutations", "url": "https://leetcode.com/problems/permutations/", "company": "B"},
            {"id": "LC78", "name": "Subsets", "url": "https://leetcode.com/problems/subsets/", "company": "B"},
            {"id": "LC39", "name": "Combination Sum", "url": "https://leetcode.com/problems/combination-sum/", "company": "B"},
            {"id": "LC79", "name": "Word Search", "url": "https://leetcode.com/problems/word-search/", "company": "M"},
            {"id": "LC22", "name": "Generate Parentheses", "url": "https://leetcode.com/problems/generate-parentheses/", "company": "B"},
        ],
        "hard": [
            {"id": "LC51", "name": "N-Queens", "url": "https://leetcode.com/problems/n-queens/", "company": "G"},
            {"id": "LC37", "name": "Sudoku Solver", "url": "https://leetcode.com/problems/sudoku-solver/", "company": "G"},
        ]
    },
    "linked-list": {
        "easy": [
            {"id": "LC206", "name": "Reverse Linked List", "url": "https://leetcode.com/problems/reverse-linked-list/", "company": "B"},
            {"id": "LC21", "name": "Merge Two Sorted Lists", "url": "https://leetcode.com/problems/merge-two-sorted-lists/", "company": "B"},
            {"id": "LC141", "name": "Linked List Cycle", "url": "https://leetcode.com/problems/linked-list-cycle/", "company": "B"},
        ],
        "medium": [
            {"id": "LC2", "name": "Add Two Numbers", "url": "https://leetcode.com/problems/add-two-numbers/", "company": "B"},
            {"id": "LC19", "name": "Remove Nth Node From End", "url": "https://leetcode.com/problems/remove-nth-node-from-end-of-list/", "company": "B"},
            {"id": "LC138", "name": "Copy List with Random Pointer", "url": "https://leetcode.com/problems/copy-list-with-random-pointer/", "company": "M"},
            {"id": "LC142", "name": "Linked List Cycle II", "url": "https://leetcode.com/problems/linked-list-cycle-ii/", "company": "B"},
            {"id": "LC146", "name": "LRU Cache", "url": "https://leetcode.com/problems/lru-cache/", "company": "B"},
        ],
        "hard": [
            {"id": "LC25", "name": "Reverse Nodes in k-Group", "url": "https://leetcode.com/problems/reverse-nodes-in-k-group/", "company": "G"},
        ]
    },
    "hashing": {
        "easy": [
            {"id": "LC1", "name": "Two Sum", "url": "https://leetcode.com/problems/two-sum/", "company": "B"},
            {"id": "LC242", "name": "Valid Anagram", "url": "https://leetcode.com/problems/valid-anagram/", "company": "B"},
        ],
        "medium": [
            {"id": "LC49", "name": "Group Anagrams", "url": "https://leetcode.com/problems/group-anagrams/", "company": "B"},
            {"id": "LC560", "name": "Subarray Sum Equals K", "url": "https://leetcode.com/problems/subarray-sum-equals-k/", "company": "B"},
            {"id": "LC128", "name": "Longest Consecutive Sequence", "url": "https://leetcode.com/problems/longest-consecutive-sequence/", "company": "B"},
            {"id": "LC238", "name": "Product of Array Except Self", "url": "https://leetcode.com/problems/product-of-array-except-self/", "company": "B"},
        ],
        "hard": [
            {"id": "LC41", "name": "First Missing Positive", "url": "https://leetcode.com/problems/first-missing-positive/", "company": "G"},
        ]
    },
    "intervals": {
        "easy": [
            {"id": "LC252", "name": "Meeting Rooms", "url": "https://leetcode.com/problems/meeting-rooms/", "company": "M"},
        ],
        "medium": [
            {"id": "LC56", "name": "Merge Intervals", "url": "https://leetcode.com/problems/merge-intervals/", "company": "B"},
            {"id": "LC57", "name": "Insert Interval", "url": "https://leetcode.com/problems/insert-interval/", "company": "G"},
            {"id": "LC435", "name": "Non-overlapping Intervals", "url": "https://leetcode.com/problems/non-overlapping-intervals/", "company": "G"},
            {"id": "LC986", "name": "Interval List Intersections", "url": "https://leetcode.com/problems/interval-list-intersections/", "company": "M"},
        ],
        "hard": []
    },
}

# Weakness weights (higher = more likely to be selected)
WEAKNESS_WEIGHTS = {
    "snapshot-versioning": 10,  # Highest priority - failed in Google interview
    "union-find": 10,           # Highest priority - failed in Meta interview
    "monotonic-stack": 8,
    "sliding-window": 7,
    "binary-search": 6,
    "dynamic-programming": 6,
    "graph-bfs-dfs": 5,
    "heap-priority-queue": 5,
    "tree-traversal": 5,        # Meta emphasizes trees
    "backtracking": 4,
    "two-pointers": 4,
    "linked-list": 3,
    "hashing": 3,
    "intervals": 4,
}

# Google scenario wrappers for common problems
GOOGLE_SCENARIOS = {
    "LC1146": {
        "scenario": "Google Docs Version Control",
        "description": """Design a system for Google Docs that tracks document state over time:
- save() - takes a snapshot and returns version_id
- edit(index, content) - modifies content at index
- getVersion(version_id, index) - retrieves content at that version

This allows users to "time travel" to see document state at any past version.""",
        "clarifications": ["Can edits happen after snapshots?", "What's the max document size?", "How often are snapshots taken?"]
    },
    "CUSTOM1": {
        "scenario": "Google Docs Collaborator Tracking",
        "description": """Design a data structure for Google Docs that tracks document collaborators:
- add(user) adds a collaborator, returns operation_id
- remove(user) removes a collaborator, returns operation_id
- members(op_id) returns the set of collaborators at that point

This allows "time travel" to see who was collaborating at any past operation.""",
        "clarifications": ["Can the same user be added twice?", "What if remove is called for non-existent user?", "Is op_id always sequential?"]
    },
    "LC721": {
        "scenario": "Gmail Account Linking",
        "description": """Gmail users sometimes create multiple accounts. Given a list of accounts with
their associated phone numbers and recovery emails, merge accounts that likely
belong to the same person. Two accounts belong to the same person if they share
any identifier (phone, recovery email, or secondary email).

Return merged accounts with all identifiers grouped together.""",
        "clarifications": ["Can one identifier belong to multiple people?", "How to handle case sensitivity?", "Should result be sorted?"]
    },
    "LC200": {
        "scenario": "Wifi Coverage Analysis",
        "description": """Google is planning WiFi coverage for a building floor plan. Given a 2D grid
where 1 represents areas that need coverage and 0 represents walls/obstacles,
determine how many separate coverage zones exist (areas connected horizontally
or vertically that all need coverage).

Each zone would need its own WiFi router.""",
        "clarifications": ["Do diagonal connections count?", "Can zones wrap around edges?", "What's the max grid size?"]
    },
    "LC207": {
        "scenario": "Build System Dependencies",
        "description": """Google's build system has targets with dependencies. Given a list of build
targets and their dependencies, determine if there's a valid build order.

If yes, output one valid order. If cycles exist, identify the targets causing them.""",
        "clarifications": ["Can a target depend on itself?", "Are there multiple valid orders?", "What's the max number of targets?"]
    },
    "LC875": {
        "scenario": "Server Provisioning",
        "description": """You're scaling Google Cloud VMs. Given N tasks with their processing requirements
and a deadline T, find the minimum VM capacity (processing power per hour) needed
to complete all tasks by the deadline.

Each VM processes one task at a time, and tasks must be processed in order.""",
        "clarifications": ["Can tasks be split across VMs?", "Are there constraints on number of VMs?", "Can VM capacity be fractional?"]
    },
    "LC253": {
        "scenario": "Google Meet Server Load",
        "description": """Google Meet runs on servers with limited capacity. Given a schedule of
meetings with start/end times, determine the minimum number of servers
needed so every meeting can run.

Each server handles one meeting at a time.""",
        "clarifications": ["Can meetings overlap?", "Are times inclusive or exclusive?", "What if end time equals start time?"]
    },
    "LC76": {
        "scenario": "Log Analysis Tool",
        "description": """You're analyzing server logs. Given a stream of log types (as a string) and a set of
error types we need to investigate, find the shortest continuous log segment that
contains at least one occurrence of each error type we're investigating.

Return the start and end positions of this segment.""",
        "clarifications": ["Can the same error type appear multiple times?", "What if not all error types are present?", "Are log types case-sensitive?"]
    },
    "LC3": {
        "scenario": "YouTube Watch Session Analysis",
        "description": """YouTube wants to analyze watch sessions. Given a stream of video IDs watched
in order (as a string of characters representing video categories), find the longest
continuous watching period where the user didn't rewatch any category.

Return the length of this period.""",
        "clarifications": ["What defines a 'session'?", "Are video IDs case-sensitive?", "What if user only watches one video?"]
    },
    "LC236": {
        "scenario": "Organization Chart Query",
        "description": """Given Google's org chart as a tree structure, find the lowest-level manager
who manages both employee A and employee B (directly or indirectly).

This helps determine approval chains for cross-team projects.""",
        "clarifications": ["Can an employee be their own manager?", "What if A and B are in same reporting chain?", "Is the tree always binary?"]
    },
}

# Meta constraint variations for common problems
META_VARIATIONS = {
    "LC49": {
        "standard": "Return groups in any order",
        "variation": "Return groups sorted by size (ascending), then lexicographically. Within each group, words should be sorted lexicographically.",
        "example": {
            "input": '["eat","tea","tan","ate","nat","bat"]',
            "standard_output": '[["bat"],["nat","tan"],["ate","eat","tea"]]',
            "meta_output": '[["bat"],["nat","tan"],["ate","eat","tea"]] # sorted by size, then lex'
        }
    },
    "CUSTOM2": {
        "standard": "Group URLs by content, return any representative",
        "variation": "Choose lexicographically SMALLEST URL as representative. Sort grouped URLs lexicographically.",
        "example": {
            "input": '{"z.com": "<html>a", "a.com": "<html>a", "m.com": "<html>a"}',
            "standard_output": '{"z.com": ["a.com", "m.com"]}',
            "meta_output": '{"a.com": ["m.com", "z.com"]} # a.com is lex smallest'
        }
    },
    "LC56": {
        "standard": "Return merged intervals",
        "variation": "Return merged intervals AND count how many original intervals each merged interval contains.",
        "example": {
            "input": "[[1,3],[2,6],[8,10]]",
            "standard_output": "[[1,6],[8,10]]",
            "meta_output": "[([1,6], 2), ([8,10], 1)] # with counts"
        }
    },
    "LC20": {
        "standard": "Return True/False if valid",
        "variation": "Return the INDEX of first invalid bracket, or -1 if valid.",
        "example": {
            "input": '"([)]"',
            "standard_output": "False",
            "meta_output": "2 # The ] at index 2 is first invalid"
        }
    },
    "LC253": {
        "standard": "Return minimum rooms needed",
        "variation": "Return minimum rooms AND which meetings are in which room.",
        "example": {
            "input": "[[0,30],[5,10],[15,20]]",
            "standard_output": "2",
            "meta_output": "(2, [[0], [1, 2]]) # Room 0: meeting 0, Room 1: meetings 1,2"
        }
    },
    "LC3": {
        "standard": "Return length of longest substring",
        "variation": "Return the ACTUAL substring. If multiple substrings have same max length, return the FIRST one.",
        "example": {
            "input": '"abcabcbb"',
            "standard_output": "3",
            "meta_output": '"abc" # the actual substring'
        }
    },
    "LC200": {
        "standard": "Count number of islands",
        "variation": "Return count AND coordinates of each island's cells as a list of lists.",
        "example": {
            "input": "grid with 2 islands",
            "standard_output": "2",
            "meta_output": "(2, [[(0,0),(0,1)], [(2,2)]]) # with coordinates"
        }
    },
    "LC102": {
        "standard": "Return levels top to bottom",
        "variation": "Return only nodes at depth K. If K exceeds tree depth, return empty list.",
        "example": {
            "input": "tree, k=2",
            "standard_output": "[[1],[2,3],[4,5,6,7]]",
            "meta_output": "[4,5,6,7] # only depth 2"
        }
    },
    "LC236": {
        "standard": "Return LCA, nodes guaranteed to exist",
        "variation": "Nodes might NOT exist in tree. Return None if either node doesn't exist.",
        "example": {
            "input": "tree, p=5, q=99 (99 not in tree)",
            "standard_output": "5 (assuming p,q exist)",
            "meta_output": "None # q doesn't exist"
        }
    },
    "LC1": {
        "standard": "Return any valid pair of indices",
        "variation": "Return ALL pairs that sum to target, sorted by sum of indices. If same sum, sort by smaller first index.",
        "example": {
            "input": "[1,2,3,4,5], target=6",
            "standard_output": "[1,3] # one valid pair",
            "meta_output": "[[0,4], [1,3]] # all pairs, sorted"
        }
    },
}


def get_script_dir():
    return Path(__file__).parent


def get_progress_file():
    return get_script_dir() / "progress.json"


def load_progress():
    progress_file = get_progress_file()
    if progress_file.exists():
        with open(progress_file) as f:
            return json.load(f)
    return {"solved": [], "failed": [], "attempts": {}}


def save_progress(progress):
    with open(get_progress_file(), "w") as f:
        json.dump(progress, f, indent=2)


def weighted_random_pattern():
    """Select a pattern weighted by weakness priority."""
    patterns = list(WEAKNESS_WEIGHTS.keys())
    weights = list(WEAKNESS_WEIGHTS.values())
    return random.choices(patterns, weights=weights, k=1)[0]


def filter_by_company(problems, company):
    """Filter problems by company preference."""
    if not company:
        return problems

    company = company.upper()
    if company == "GOOGLE":
        company = "G"
    elif company == "META":
        company = "M"

    # Include problems that match company or are common to both (B)
    return [p for p in problems if p.get("company", "B") in [company, "B"]]


def get_problem(pattern: str, difficulty: str, company: str = None):
    """Get a problem from the specified pattern, difficulty, and optionally company."""
    if pattern not in PROBLEM_BANK:
        print(f"Unknown pattern: {pattern}")
        print(f"Available patterns: {', '.join(PROBLEM_BANK.keys())}")
        return None

    problems = PROBLEM_BANK[pattern].get(difficulty, [])

    # Filter by company if specified
    if company:
        problems = filter_by_company(problems, company)

    if not problems:
        # Try adjacent difficulties
        if difficulty == "medium":
            alt_problems = PROBLEM_BANK[pattern].get("hard", []) or PROBLEM_BANK[pattern].get("easy", [])
        elif difficulty == "hard":
            alt_problems = PROBLEM_BANK[pattern].get("medium", [])
        elif difficulty == "easy":
            alt_problems = PROBLEM_BANK[pattern].get("medium", [])
        else:
            alt_problems = []

        if company:
            alt_problems = filter_by_company(alt_problems, company)
        problems = alt_problems

    if not problems:
        print(f"No problems found for {pattern} at {difficulty} difficulty" +
              (f" for {company}" if company else ""))
        return None

    # Prefer unsolved problems
    progress = load_progress()
    unsolved = [p for p in problems if p["id"] not in progress["solved"]]

    if unsolved:
        return random.choice(unsolved)
    return random.choice(problems)


def display_google_scenario(problem_id):
    """Display Google scenario wrapper for a problem."""
    if problem_id not in GOOGLE_SCENARIOS:
        return False

    scenario = GOOGLE_SCENARIOS[problem_id]
    print("\n" + "-" * 60)
    print("GOOGLE SCENARIO WRAPPER")
    print("-" * 60)
    print(f"Theme: {scenario['scenario']}")
    print()
    print("Problem Description:")
    print(scenario['description'])
    print()
    print("Clarifying Questions to Ask:")
    for q in scenario['clarifications']:
        print(f"  - {q}")
    print("-" * 60)
    return True


def display_meta_variation(problem_id):
    """Display Meta constraint variation for a problem."""
    if problem_id not in META_VARIATIONS:
        return False

    variation = META_VARIATIONS[problem_id]
    print("\n" + "-" * 60)
    print("META CONSTRAINT VARIATION")
    print("-" * 60)
    print(f"Standard: {variation['standard']}")
    print(f"Meta Twist: {variation['variation']}")
    print()
    print("Example:")
    print(f"  Input: {variation['example']['input']}")
    print(f"  Standard Output: {variation['example']['standard_output']}")
    print(f"  Meta Output: {variation['example']['meta_output']}")
    print("-" * 60)
    return True


def display_problem(problem, pattern, difficulty, time_limit, company=None):
    """Display the problem in a nice format."""
    print("\n" + "=" * 60)
    print(f"PRACTICE PROBLEM" + (f" ({company.upper()} Style)" if company else ""))
    print("=" * 60)
    print(f"Pattern: {pattern}")
    print(f"Difficulty: {difficulty}")
    print(f"Time Limit: {time_limit} minutes")
    print(f"Company: {problem.get('company', 'B')} (G=Google, M=Meta, B=Both)")
    print("-" * 60)
    print(f"Problem: {problem['name']} ({problem['id']})")
    if problem["url"]:
        print(f"URL: {problem['url']}")
    print("=" * 60)

    # Display company-specific information
    if company:
        company_upper = company.upper()
        if company_upper in ["GOOGLE", "G"]:
            display_google_scenario(problem['id'])
        elif company_upper in ["META", "M"]:
            display_meta_variation(problem['id'])

    print("\nSTART YOUR TIMER NOW!")
    print("\nRemember:")
    print("1. Ask clarifying questions (especially important!)")
    print("2. Discuss approach before coding")
    print("3. Talk through your code AS YOU WRITE")
    print("4. Test with examples and edge cases")
    print("5. Trace through your code line by line")
    print("=" * 60 + "\n")


def list_patterns():
    """List all available patterns with their priorities."""
    print("\nAvailable patterns (sorted by priority):")
    print("-" * 50)
    for pattern, weight in sorted(WEAKNESS_WEIGHTS.items(), key=lambda x: -x[1]):
        count = sum(len(PROBLEM_BANK[pattern].get(d, [])) for d in ["easy", "medium", "hard"])
        print(f"  {pattern:25} priority: {weight:2}  ({count} problems)")
    print()


def list_problems_by_company(company):
    """List all problems for a specific company."""
    company_code = "G" if company.upper() == "GOOGLE" else "M"
    print(f"\n{company.upper()} Problems:")
    print("-" * 60)

    for pattern, difficulties in PROBLEM_BANK.items():
        pattern_problems = []
        for diff, problems in difficulties.items():
            for p in problems:
                if p.get("company", "B") in [company_code, "B"]:
                    pattern_problems.append((diff, p))

        if pattern_problems:
            print(f"\n{pattern}:")
            for diff, p in pattern_problems:
                print(f"  [{diff:6}] {p['name']} ({p['id']})")


def main():
    parser = argparse.ArgumentParser(
        description="Generate DSA practice problems with company-specific variations"
    )
    parser.add_argument("--pattern", "-p", help="Specific pattern to practice")
    parser.add_argument("--difficulty", "-d", default="medium",
                       choices=["easy", "medium", "hard"],
                       help="Problem difficulty")
    parser.add_argument("--time", "-t", type=int, help="Time limit in minutes")
    parser.add_argument("--random", "-r", action="store_true",
                       help="Random pattern from weak areas")
    parser.add_argument("--company", "-c", choices=["google", "meta"],
                       help="Practice with company-specific style (Google scenarios or Meta variations)")
    parser.add_argument("--list-patterns", action="store_true",
                       help="List all available patterns")
    parser.add_argument("--list-company", choices=["google", "meta"],
                       help="List all problems for a specific company")

    args = parser.parse_args()

    if args.list_patterns:
        list_patterns()
        return

    if args.list_company:
        list_problems_by_company(args.list_company)
        return

    # Determine pattern
    if args.random or not args.pattern:
        pattern = weighted_random_pattern()
    else:
        pattern = args.pattern

    # Determine time limit
    time_limits = {"easy": 15, "medium": 25, "hard": 45}
    time_limit = args.time or time_limits[args.difficulty]

    # Get and display problem
    problem = get_problem(pattern, args.difficulty, args.company)
    if problem:
        display_problem(problem, pattern, args.difficulty, time_limit, args.company)


if __name__ == "__main__":
    main()
