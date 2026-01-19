# Google Tagged LeetCode Problems (6 Months)

Master index of 344 Google-tagged problems organized by pattern.

**Counts:** Medium: 271 | Hard: 73 | Total: 344

---

## Quick Navigation

| Pattern | Count | Link |
|---------|-------|------|
| [Binary Search](#binary-search) | 25 | [Solutions](solutions/01-binary-search/) |
| [Two Pointers](#two-pointers) | 28 | [Solutions](solutions/02-two-pointers/) |
| [Sliding Window](#sliding-window) | 22 | [Solutions](solutions/03-sliding-window/) |
| [Monotonic Stack](#monotonic-stack) | 18 | [Solutions](solutions/04-monotonic-stack/) |
| [Heap / Priority Queue](#heap--priority-queue) | 24 | [Solutions](solutions/05-heap/) |
| [Interval Problems](#interval-problems) | 15 | [Solutions](solutions/06-intervals/) |
| [Backtracking](#backtracking) | 25 | [Solutions](solutions/07-backtracking/) |
| [Dynamic Programming](#dynamic-programming) | 55 | [Solutions](solutions/08-dp/) |
| [Graph / BFS / DFS](#graph--bfs--dfs) | 45 | [Solutions](solutions/09-graph/) |
| [Tree Problems](#tree-problems) | 32 | [Solutions](solutions/10-trees/) |
| [Linked List](#linked-list) | 18 | [Solutions](solutions/11-linked-list/) |
| [String Manipulation](#string-manipulation) | 20 | [Solutions](solutions/12-strings/) |
| [Math & Bit Manipulation](#math--bit-manipulation) | 17 | [Solutions](solutions/13-math-bits/) |

---

## Pattern Visualizers

Interactive ASCII visualizations for each pattern:

| Pattern | Visualizer |
|---------|------------|
| Binary Search | [visualizers/binary-search-viz.md](visualizers/binary-search-viz.md) |
| Two Pointers | [visualizers/two-pointers-viz.md](visualizers/two-pointers-viz.md) |
| Sliding Window | [visualizers/sliding-window-viz.md](visualizers/sliding-window-viz.md) |
| Monotonic Stack | [visualizers/monotonic-stack-viz.md](visualizers/monotonic-stack-viz.md) |
| Heap | [visualizers/heap-viz.md](visualizers/heap-viz.md) |
| Backtracking | [visualizers/backtracking-viz.md](visualizers/backtracking-viz.md) |

---

## Binary Search

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | [Solution](solutions/01-binary-search/0004-median-of-two-sorted-arrays.md) | Binary Search on Partition |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Med | [Solution](solutions/01-binary-search/0033-search-in-rotated-sorted-array.md) | Modified Binary Search |
| 34 | [Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Med | [Solution](solutions/01-binary-search/0034-find-first-and-last-position.md) | Find Boundaries |
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Med | [Solution](solutions/01-binary-search/0074-search-a-2d-matrix.md) | 2D Binary Search |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Med | [Solution](solutions/01-binary-search/0153-find-minimum-in-rotated-sorted-array.md) | Rotated Array |
| 154 | [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | Hard | [Solution](solutions/01-binary-search/0154-find-minimum-in-rotated-sorted-array-ii.md) | With Duplicates |
| 162 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Med | [Solution](solutions/01-binary-search/0162-find-peak-element.md) | Peak Finding |
| 410 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | Hard | [Solution](solutions/01-binary-search/0410-split-array-largest-sum.md) | BS on Answer |
| 528 | [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | Med | [Solution](solutions/01-binary-search/0528-random-pick-with-weight.md) | Prefix Sum + BS |
| 540 | [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/) | Med | [Solution](solutions/01-binary-search/0540-single-element-in-sorted-array.md) | Parity Check |
| 658 | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | Med | [Solution](solutions/01-binary-search/0658-find-k-closest-elements.md) | BS on Window |
| 852 | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | Med | [Solution](solutions/01-binary-search/0852-peak-index-in-mountain-array.md) | Peak Finding |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Med | [Solution](solutions/01-binary-search/0875-koko-eating-bananas.md) | BS on Answer |
| 1011 | [Capacity To Ship Packages](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Med | [Solution](solutions/01-binary-search/1011-capacity-to-ship-packages.md) | BS on Answer |
| 1283 | [Find the Smallest Divisor](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) | Med | [Solution](solutions/01-binary-search/1283-find-smallest-divisor.md) | BS on Answer |
| 1482 | [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | Med | [Solution](solutions/01-binary-search/1482-minimum-days-for-bouquets.md) | BS on Answer |
| 1552 | [Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/) | Med | [Solution](solutions/01-binary-search/1552-magnetic-force-between-balls.md) | BS on Answer (MAX) |
| 1838 | [Frequency of Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) | Med | [Solution](solutions/01-binary-search/1838-frequency-of-most-frequent.md) | BS + Sliding Window |
| 2226 | [Maximum Candies Allocated](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/) | Med | [Solution](solutions/01-binary-search/2226-maximum-candies-allocated.md) | BS on Answer |
| 2616 | [Minimize Maximum Difference of Pairs](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/) | Med | [Solution](solutions/01-binary-search/2616-minimize-max-difference-of-pairs.md) | BS on Answer |

---

## Two Pointers

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Med | [Solution](solutions/02-two-pointers/0011-container-with-most-water.md) | Opposite Direction |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Med | [Solution](solutions/02-two-pointers/0015-3sum.md) | Sort + Two Pointers |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Med | [Solution](solutions/02-two-pointers/0016-3sum-closest.md) | Sort + Two Pointers |
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | Med | [Solution](solutions/02-two-pointers/0018-4sum.md) | Nested Two Pointers |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | [Solution](solutions/02-two-pointers/0042-trapping-rain-water.md) | Two Pointers + Max |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Med | [Solution](solutions/02-two-pointers/0075-sort-colors.md) | Dutch National Flag |
| 80 | [Remove Duplicates II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Med | [Solution](solutions/02-two-pointers/0080-remove-duplicates-ii.md) | Same Direction |
| 167 | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Med | [Solution](solutions/02-two-pointers/0167-two-sum-ii.md) | Opposite Direction |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Med | [Solution](solutions/02-two-pointers/0287-find-duplicate-number.md) | Floyd's Cycle |
| 581 | [Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | Med | [Solution](solutions/02-two-pointers/0581-shortest-unsorted-subarray.md) | Two Pointers |
| 611 | [Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/) | Med | [Solution](solutions/02-two-pointers/0611-valid-triangle-number.md) | Sort + Two Pointers |
| 633 | [Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/) | Med | [Solution](solutions/02-two-pointers/0633-sum-of-square-numbers.md) | Opposite Direction |
| 1679 | [Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | Med | [Solution](solutions/02-two-pointers/1679-max-k-sum-pairs.md) | Sort + Two Pointers |

---

## Sliding Window

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 3 | [Longest Substring Without Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Med | [Solution](solutions/03-sliding-window/0003-longest-substring-without-repeating.md) | Variable Window |
| 30 | [Substring with Concatenation](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Hard | [Solution](solutions/03-sliding-window/0030-substring-with-concatenation.md) | Fixed Window |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | [Solution](solutions/03-sliding-window/0076-minimum-window-substring.md) | Find Shortest |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Med | [Solution](solutions/03-sliding-window/0209-minimum-size-subarray-sum.md) | Find Shortest |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | [Solution](solutions/03-sliding-window/0239-sliding-window-maximum.md) | Monotonic Deque |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Med | [Solution](solutions/03-sliding-window/0424-longest-repeating-char-replacement.md) | Variable Window |
| 438 | [Find All Anagrams](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Med | [Solution](solutions/03-sliding-window/0438-find-all-anagrams.md) | Fixed Window |
| 480 | [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) | Hard | [Solution](solutions/03-sliding-window/0480-sliding-window-median.md) | Two Heaps + Window |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Med | [Solution](solutions/03-sliding-window/0567-permutation-in-string.md) | Fixed Window |
| 904 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Med | [Solution](solutions/03-sliding-window/0904-fruit-into-baskets.md) | At Most K |
| 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Med | [Solution](solutions/03-sliding-window/1004-max-consecutive-ones-iii.md) | Variable Window |
| 1358 | [Number of Substrings Containing All Three](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) | Med | [Solution](solutions/03-sliding-window/1358-substrings-with-all-three.md) | Count Subarrays |
| 1423 | [Maximum Points from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | Med | [Solution](solutions/03-sliding-window/1423-max-points-from-cards.md) | Reverse Thinking |
| 2106 | [Maximum Fruits Harvested](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/) | Hard | [Solution](solutions/03-sliding-window/2106-max-fruits-harvested.md) | Sliding Window |

---

## Monotonic Stack

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | [Solution](solutions/04-monotonic-stack/0042-trapping-rain-water.md) | Decreasing Stack |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | [Solution](solutions/04-monotonic-stack/0084-largest-rectangle-histogram.md) | Increasing Stack |
| 85 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | Hard | [Solution](solutions/04-monotonic-stack/0085-maximal-rectangle.md) | Histogram per Row |
| 402 | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | Med | [Solution](solutions/04-monotonic-stack/0402-remove-k-digits.md) | Increasing Stack |
| 735 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Med | [Solution](solutions/04-monotonic-stack/0735-asteroid-collision.md) | Stack Simulation |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Med | [Solution](solutions/04-monotonic-stack/0739-daily-temperatures.md) | Next Greater |
| 901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | Med | [Solution](solutions/04-monotonic-stack/0901-online-stock-span.md) | Previous Greater |
| 907 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | Med | [Solution](solutions/04-monotonic-stack/0907-sum-of-subarray-minimums.md) | Contribution Count |
| 962 | [Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp/) | Med | [Solution](solutions/04-monotonic-stack/0962-max-width-ramp.md) | Decreasing Stack |
| 1944 | [Number of Visible People in Queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) | Hard | [Solution](solutions/04-monotonic-stack/1944-visible-people-in-queue.md) | Decreasing Stack |
| 2104 | [Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/) | Med | [Solution](solutions/04-monotonic-stack/2104-sum-of-subarray-ranges.md) | Min + Max Contribution |

---

## Heap / Priority Queue

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | [Solution](solutions/05-heap/0023-merge-k-sorted-lists.md) | Min Heap |
| 215 | [Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Med | [Solution](solutions/05-heap/0215-kth-largest-element.md) | Min Heap Size K |
| 218 | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | Hard | [Solution](solutions/05-heap/0218-skyline-problem.md) | Max Heap + Events |
| 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Med | [Solution](solutions/05-heap/0253-meeting-rooms-ii.md) | Min Heap |
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | [Solution](solutions/05-heap/0295-find-median-from-stream.md) | Two Heaps |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Med | [Solution](solutions/05-heap/0347-top-k-frequent.md) | Min Heap Size K |
| 355 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Med | [Solution](solutions/05-heap/0355-design-twitter.md) | Merge K Lists |
| 373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Med | [Solution](solutions/05-heap/0373-k-pairs-smallest-sums.md) | Lazy Expansion |
| 407 | [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) | Hard | [Solution](solutions/05-heap/0407-trapping-rain-water-ii.md) | Min Heap BFS |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Med | [Solution](solutions/05-heap/0621-task-scheduler.md) | Max Heap + Cooldown |
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Med | [Solution](solutions/05-heap/0743-network-delay-time.md) | Dijkstra |
| 767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | Med | [Solution](solutions/05-heap/0767-reorganize-string.md) | Max Heap |
| 778 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | [Solution](solutions/05-heap/0778-swim-in-rising-water.md) | Min Heap Path |
| 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Med | [Solution](solutions/05-heap/0787-cheapest-flights-k-stops.md) | Modified Dijkstra |
| 1102 | [Path With Maximum Minimum Value](https://leetcode.com/problems/path-with-maximum-minimum-value/) | Med | [Solution](solutions/05-heap/1102-path-with-max-min-value.md) | Max Heap Path |
| 1353 | [Maximum Number of Events](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) | Med | [Solution](solutions/05-heap/1353-max-events-attended.md) | Greedy + Heap |
| 1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Med | [Solution](solutions/05-heap/1631-path-with-min-effort.md) | Dijkstra Variant |
| 1834 | [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) | Med | [Solution](solutions/05-heap/1834-single-threaded-cpu.md) | Simulation + Heap |
| 2402 | [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/) | Hard | [Solution](solutions/05-heap/2402-meeting-rooms-iii.md) | Two Heaps |

---

## Interval Problems

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Med | [Solution](solutions/06-intervals/0056-merge-intervals.md) | Sort by Start |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Med | [Solution](solutions/06-intervals/0057-insert-interval.md) | Three Phases |
| 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Med | [Solution](solutions/06-intervals/0253-meeting-rooms-ii.md) | Sort + Heap |
| 452 | [Minimum Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Med | [Solution](solutions/06-intervals/0452-minimum-arrows.md) | Sort by End |
| 715 | [Range Module](https://leetcode.com/problems/range-module/) | Hard | [Solution](solutions/06-intervals/0715-range-module.md) | Interval Tree |
| 729 | [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Med | [Solution](solutions/06-intervals/0729-my-calendar-i.md) | Overlap Check |
| 1326 | [Minimum Taps to Water Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) | Hard | [Solution](solutions/06-intervals/1326-minimum-taps.md) | Greedy Jump Game |
| 2054 | [Two Best Non-Overlapping Events](https://leetcode.com/problems/two-best-non-overlapping-events/) | Med | [Solution](solutions/06-intervals/2054-two-best-events.md) | Sort + Binary Search |

---

## Backtracking

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 17 | [Letter Combinations of Phone](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Med | [Solution](solutions/07-backtracking/0017-letter-combinations.md) | Cartesian Product |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Med | [Solution](solutions/07-backtracking/0022-generate-parentheses.md) | Constrained Generation |
| 37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | Hard | [Solution](solutions/07-backtracking/0037-sudoku-solver.md) | Constraint Satisfaction |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Med | [Solution](solutions/07-backtracking/0039-combination-sum.md) | With Reuse |
| 40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Med | [Solution](solutions/07-backtracking/0040-combination-sum-ii.md) | No Reuse + Dedup |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | Med | [Solution](solutions/07-backtracking/0046-permutations.md) | All Orderings |
| 51 | [N-Queens](https://leetcode.com/problems/n-queens/) | Hard | [Solution](solutions/07-backtracking/0051-n-queens.md) | Constraint Satisfaction |
| 52 | [N-Queens II](https://leetcode.com/problems/n-queens-ii/) | Hard | [Solution](solutions/07-backtracking/0052-n-queens-ii.md) | Count Solutions |
| 60 | [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) | Hard | [Solution](solutions/07-backtracking/0060-permutation-sequence.md) | Math + Backtrack |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | Med | [Solution](solutions/07-backtracking/0078-subsets.md) | Include/Exclude |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) | Med | [Solution](solutions/07-backtracking/0079-word-search.md) | Grid DFS |
| 90 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | Med | [Solution](solutions/07-backtracking/0090-subsets-ii.md) | Dedup Subsets |
| 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Med | [Solution](solutions/07-backtracking/0131-palindrome-partitioning.md) | String Partition |
| 282 | [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) | Hard | [Solution](solutions/07-backtracking/0282-expression-add-operators.md) | Expression Building |
| 679 | [24 Game](https://leetcode.com/problems/24-game/) | Hard | [Solution](solutions/07-backtracking/0679-24-game.md) | Expression Building |

---

## Dynamic Programming

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Med | [Solution](solutions/08-dp/0005-longest-palindromic-substring.md) | Expand Around Center |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard | [Solution](solutions/08-dp/0010-regular-expression-matching.md) | 2D DP |
| 44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | Hard | [Solution](solutions/08-dp/0044-wildcard-matching.md) | 2D DP |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Med | [Solution](solutions/08-dp/0045-jump-game-ii.md) | Greedy |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Med | [Solution](solutions/08-dp/0053-maximum-subarray.md) | Kadane's Algorithm |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | Med | [Solution](solutions/08-dp/0055-jump-game.md) | Greedy |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Med | [Solution](solutions/08-dp/0062-unique-paths.md) | Grid DP |
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Hard | [Solution](solutions/08-dp/0072-edit-distance.md) | 2D DP |
| 91 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | Med | [Solution](solutions/08-dp/0091-decode-ways.md) | 1D DP |
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | Med | [Solution](solutions/08-dp/0096-unique-bst.md) | Catalan Numbers |
| 120 | [Triangle](https://leetcode.com/problems/triangle/) | Med | [Solution](solutions/08-dp/0120-triangle.md) | Bottom-Up DP |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Med | [Solution](solutions/08-dp/0122-best-time-buy-sell-ii.md) | State Machine |
| 123 | [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | Hard | [Solution](solutions/08-dp/0123-best-time-buy-sell-iii.md) | State Machine |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Med | [Solution](solutions/08-dp/0128-longest-consecutive-sequence.md) | HashSet |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | Med | [Solution](solutions/08-dp/0134-gas-station.md) | Greedy |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Med | [Solution](solutions/08-dp/0152-max-product-subarray.md) | Track Min/Max |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | Med | [Solution](solutions/08-dp/0198-house-robber.md) | 1D DP |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Med | [Solution](solutions/08-dp/0213-house-robber-ii.md) | Circular Array |
| 221 | [Maximal Square](https://leetcode.com/problems/maximal-square/) | Med | [Solution](solutions/08-dp/0221-maximal-square.md) | 2D DP |
| 279 | [Perfect Squares](https://leetcode.com/problems/perfect-squares/) | Med | [Solution](solutions/08-dp/0279-perfect-squares.md) | BFS or DP |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Med | [Solution](solutions/08-dp/0300-longest-increasing-subsequence.md) | Binary Search Opt |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | Med | [Solution](solutions/08-dp/0322-coin-change.md) | Unbounded Knapsack |
| 329 | [Longest Increasing Path in Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Hard | [Solution](solutions/08-dp/0329-longest-increasing-path.md) | DFS + Memo |
| 337 | [House Robber III](https://leetcode.com/problems/house-robber-iii/) | Med | [Solution](solutions/08-dp/0337-house-robber-iii.md) | Tree DP |
| 354 | [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) | Hard | [Solution](solutions/08-dp/0354-russian-doll-envelopes.md) | Sort + LIS |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Med | [Solution](solutions/08-dp/0416-partition-equal-subset-sum.md) | 0/1 Knapsack |
| 486 | [Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | Med | [Solution](solutions/08-dp/0486-predict-the-winner.md) | Game Theory |
| 494 | [Target Sum](https://leetcode.com/problems/target-sum/) | Med | [Solution](solutions/08-dp/0494-target-sum.md) | 0/1 Knapsack |
| 516 | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | Med | [Solution](solutions/08-dp/0516-longest-palindromic-subsequence.md) | Interval DP |
| 518 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Med | [Solution](solutions/08-dp/0518-coin-change-ii.md) | Unbounded Knapsack |
| 647 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Med | [Solution](solutions/08-dp/0647-palindromic-substrings.md) | Expand Center |
| 712 | [Minimum ASCII Delete Sum](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) | Med | [Solution](solutions/08-dp/0712-min-ascii-delete-sum.md) | LCS Variant |
| 931 | [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) | Med | [Solution](solutions/08-dp/0931-min-falling-path-sum.md) | Grid DP |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Med | [Solution](solutions/08-dp/1143-longest-common-subsequence.md) | Classic LCS |
| 1277 | [Count Square Submatrices](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) | Med | [Solution](solutions/08-dp/1277-count-square-submatrices.md) | Maximal Square Variant |
| 1626 | [Best Team With No Conflicts](https://leetcode.com/problems/best-team-with-no-conflicts/) | Med | [Solution](solutions/08-dp/1626-best-team-no-conflicts.md) | LIS Variant |

---

## Graph / BFS / DFS

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | [Solution](solutions/09-graph/0127-word-ladder.md) | BFS Shortest Path |
| 130 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Med | [Solution](solutions/09-graph/0130-surrounded-regions.md) | Boundary DFS |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Med | [Solution](solutions/09-graph/0200-number-of-islands.md) | DFS/BFS Grid |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Med | [Solution](solutions/09-graph/0207-course-schedule.md) | Topological Sort |
| 399 | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | Med | [Solution](solutions/09-graph/0399-evaluate-division.md) | Weighted Graph |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Med | [Solution](solutions/09-graph/0417-pacific-atlantic.md) | Multi-Source BFS |
| 542 | [01 Matrix](https://leetcode.com/problems/01-matrix/) | Med | [Solution](solutions/09-graph/0542-01-matrix.md) | Multi-Source BFS |
| 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Med | [Solution](solutions/09-graph/0695-max-area-of-island.md) | DFS Grid |
| 721 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Med | [Solution](solutions/09-graph/0721-accounts-merge.md) | Union-Find |
| 802 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Med | [Solution](solutions/09-graph/0802-eventual-safe-states.md) | Cycle Detection |
| 863 | [All Nodes Distance K](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | Med | [Solution](solutions/09-graph/0863-nodes-distance-k.md) | Tree to Graph + BFS |
| 934 | [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/) | Med | [Solution](solutions/09-graph/0934-shortest-bridge.md) | DFS + BFS |
| 947 | [Most Stones Removed](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Med | [Solution](solutions/09-graph/0947-most-stones-removed.md) | Union-Find |
| 994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Med | [Solution](solutions/09-graph/0994-rotting-oranges.md) | Multi-Source BFS |
| 1091 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Med | [Solution](solutions/09-graph/1091-shortest-path-binary-matrix.md) | BFS 8-directional |
| 1101 | [Earliest Moment When Everyone Friends](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/) | Med | [Solution](solutions/09-graph/1101-earliest-moment-friends.md) | Union-Find |
| 1192 | [Critical Connections](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | [Solution](solutions/09-graph/1192-critical-connections.md) | Tarjan's Bridge |
| 1254 | [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | Med | [Solution](solutions/09-graph/1254-number-of-closed-islands.md) | DFS + Boundary |
| 1293 | [Shortest Path with Obstacles](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | Hard | [Solution](solutions/09-graph/1293-shortest-path-obstacles.md) | BFS + State |
| 2092 | [Find All People With Secret](https://leetcode.com/problems/find-all-people-with-secret/) | Hard | [Solution](solutions/09-graph/2092-find-all-people-secret.md) | Time-Based Union-Find |

---

## Tree Problems

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Med | [Solution](solutions/10-trees/0098-validate-bst.md) | Inorder/Bounds |
| 99 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | Med | [Solution](solutions/10-trees/0099-recover-bst.md) | Morris Traversal |
| 102 | [Binary Tree Level Order](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Med | [Solution](solutions/10-trees/0102-level-order.md) | BFS |
| 105 | [Construct Tree from Preorder/Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Med | [Solution](solutions/10-trees/0105-construct-from-preorder-inorder.md) | Divide & Conquer |
| 114 | [Flatten Binary Tree](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | Med | [Solution](solutions/10-trees/0114-flatten-binary-tree.md) | Morris-like |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | [Solution](solutions/10-trees/0124-max-path-sum.md) | DFS + Global Max |
| 129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | Med | [Solution](solutions/10-trees/0129-sum-root-to-leaf.md) | DFS Path |
| 230 | [Kth Smallest Element in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Med | [Solution](solutions/10-trees/0230-kth-smallest-bst.md) | Inorder |
| 236 | [Lowest Common Ancestor](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Med | [Solution](solutions/10-trees/0236-lca.md) | DFS |
| 297 | [Serialize and Deserialize](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | [Solution](solutions/10-trees/0297-serialize-deserialize.md) | Preorder |
| 450 | [Delete Node in BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Med | [Solution](solutions/10-trees/0450-delete-node-bst.md) | BST Property |
| 662 | [Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/) | Med | [Solution](solutions/10-trees/0662-max-width-binary-tree.md) | BFS + Indexing |
| 987 | [Vertical Order Traversal](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | Hard | [Solution](solutions/10-trees/0987-vertical-order.md) | BFS + Sorting |
| 1110 | [Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/) | Med | [Solution](solutions/10-trees/1110-delete-nodes-return-forest.md) | DFS |
| 1161 | [Maximum Level Sum](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) | Med | [Solution](solutions/10-trees/1161-max-level-sum.md) | BFS |

---

## Linked List

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Med | [Solution](solutions/11-linked-list/0002-add-two-numbers.md) | Carry Propagation |
| 19 | [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Med | [Solution](solutions/11-linked-list/0019-remove-nth-from-end.md) | Two Pointers |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Med | [Solution](solutions/11-linked-list/0024-swap-nodes-in-pairs.md) | Pair Swap |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | [Solution](solutions/11-linked-list/0025-reverse-k-group.md) | Group Reversal |
| 61 | [Rotate List](https://leetcode.com/problems/rotate-list/) | Med | [Solution](solutions/11-linked-list/0061-rotate-list.md) | Find New Head |
| 82 | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | Med | [Solution](solutions/11-linked-list/0082-remove-duplicates-ii.md) | Two Pointers |
| 86 | [Partition List](https://leetcode.com/problems/partition-list/) | Med | [Solution](solutions/11-linked-list/0086-partition-list.md) | Two Lists |
| 92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | Med | [Solution](solutions/11-linked-list/0092-reverse-linked-list-ii.md) | Partial Reversal |
| 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Med | [Solution](solutions/11-linked-list/0138-copy-list-random-pointer.md) | HashMap or Interleave |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Med | [Solution](solutions/11-linked-list/0142-linked-list-cycle-ii.md) | Floyd's Algorithm |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Med | [Solution](solutions/11-linked-list/0143-reorder-list.md) | Split + Reverse + Merge |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Med | [Solution](solutions/11-linked-list/0146-lru-cache.md) | HashMap + DLL |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/) | Med | [Solution](solutions/11-linked-list/0148-sort-list.md) | Merge Sort |
| 237 | [Delete Node in Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) | Med | [Solution](solutions/11-linked-list/0237-delete-node.md) | Copy Next |
| 328 | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) | Med | [Solution](solutions/11-linked-list/0328-odd-even-linked-list.md) | Partition |
| 460 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | [Solution](solutions/11-linked-list/0460-lfu-cache.md) | Frequency Lists |

---

## String Manipulation

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 6 | [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/) | Med | [Solution](solutions/12-strings/0006-zigzag-conversion.md) | Row-wise Build |
| 8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | Med | [Solution](solutions/12-strings/0008-string-to-integer.md) | Parsing |
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | Med | [Solution](solutions/12-strings/0012-integer-to-roman.md) | Greedy |
| 43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Med | [Solution](solutions/12-strings/0043-multiply-strings.md) | Grade School |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Med | [Solution](solutions/12-strings/0049-group-anagrams.md) | Sort/Count Key |
| 68 | [Text Justification](https://leetcode.com/problems/text-justification/) | Hard | [Solution](solutions/12-strings/0068-text-justification.md) | Simulation |
| 151 | [Reverse Words in String](https://leetcode.com/problems/reverse-words-in-a-string/) | Med | [Solution](solutions/12-strings/0151-reverse-words.md) | Split + Reverse |
| 179 | [Largest Number](https://leetcode.com/problems/largest-number/) | Med | [Solution](solutions/12-strings/0179-largest-number.md) | Custom Sort |
| 273 | [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/) | Hard | [Solution](solutions/12-strings/0273-integer-to-english-words.md) | Divide by 1000 |
| 394 | [Decode String](https://leetcode.com/problems/decode-string/) | Med | [Solution](solutions/12-strings/0394-decode-string.md) | Stack |
| 443 | [String Compression](https://leetcode.com/problems/string-compression/) | Med | [Solution](solutions/12-strings/0443-string-compression.md) | Two Pointers |

---

## Math & Bit Manipulation

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Med | [Solution](solutions/13-math-bits/0007-reverse-integer.md) | Overflow Check |
| 29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) | Med | [Solution](solutions/13-math-bits/0029-divide-two-integers.md) | Bit Manipulation |
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | Med | [Solution](solutions/13-math-bits/0031-next-permutation.md) | Find Pattern |
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Med | [Solution](solutions/13-math-bits/0050-pow-x-n.md) | Fast Exponentiation |
| 137 | [Single Number II](https://leetcode.com/problems/single-number-ii/) | Med | [Solution](solutions/13-math-bits/0137-single-number-ii.md) | Bit Counting |
| 166 | [Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/) | Med | [Solution](solutions/13-math-bits/0166-fraction-to-decimal.md) | Long Division |
| 204 | [Count Primes](https://leetcode.com/problems/count-primes/) | Med | [Solution](solutions/13-math-bits/0204-count-primes.md) | Sieve of Eratosthenes |
| 343 | [Integer Break](https://leetcode.com/problems/integer-break/) | Med | [Solution](solutions/13-math-bits/0343-integer-break.md) | Math (Use 3s) |
| 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Med | [Solution](solutions/13-math-bits/0371-sum-of-two-integers.md) | Bit Manipulation |
| 421 | [Maximum XOR of Two Numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Med | [Solution](solutions/13-math-bits/0421-max-xor-two-numbers.md) | Bit Trie |

---

## Stack & Calculator

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Med | [Solution](solutions/14-stack/0150-evaluate-rpn.md) | Stack |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | Med | [Solution](solutions/14-stack/0155-min-stack.md) | Auxiliary Stack |
| 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Hard | [Solution](solutions/14-stack/0224-basic-calculator.md) | Recursion/Stack |
| 227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Med | [Solution](solutions/14-stack/0227-basic-calculator-ii.md) | Stack + Precedence |
| 636 | [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | Med | [Solution](solutions/14-stack/0636-exclusive-time.md) | Call Stack |
| 921 | [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | Med | [Solution](solutions/14-stack/0921-min-add-parentheses.md) | Balance Count |

---

## Design Problems

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Med | [Solution](solutions/15-design/0146-lru-cache.md) | HashMap + DLL |
| 208 | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | Med | [Solution](solutions/15-design/0208-implement-trie.md) | Trie |
| 380 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Med | [Solution](solutions/15-design/0380-insert-delete-random.md) | HashMap + Array |
| 460 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | [Solution](solutions/15-design/0460-lfu-cache.md) | Frequency Maps |
| 1146 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Med | [Solution](solutions/15-design/1146-snapshot-array.md) | Versioning |
| 2296 | [Design a Text Editor](https://leetcode.com/problems/design-a-text-editor/) | Hard | [Solution](solutions/15-design/2296-design-text-editor.md) | Two Stacks |

---

## Matrix Problems

| # | Problem | Difficulty | Solution | Pattern Variant |
|---|---------|------------|----------|-----------------|
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Med | [Solution](solutions/16-matrix/0036-valid-sudoku.md) | Hash Sets |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Med | [Solution](solutions/16-matrix/0048-rotate-image.md) | Transpose + Reverse |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Med | [Solution](solutions/16-matrix/0054-spiral-matrix.md) | Simulation |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Med | [Solution](solutions/16-matrix/0073-set-matrix-zeroes.md) | In-place Markers |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | Med | [Solution](solutions/16-matrix/0189-rotate-array.md) | Reverse Three Times |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Med | [Solution](solutions/16-matrix/0238-product-except-self.md) | Prefix/Suffix |
| 304 | [Range Sum Query 2D](https://leetcode.com/problems/range-sum-query-2d-immutable/) | Med | [Solution](solutions/16-matrix/0304-range-sum-query-2d.md) | Prefix Sum 2D |
| 498 | [Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/) | Med | [Solution](solutions/16-matrix/0498-diagonal-traverse.md) | Simulation |

---

## Problem Count Summary

| Difficulty | Count | Target |
|------------|-------|--------|
| Medium | 271 | 271 |
| Hard | 73 | 73 |
| **Total** | **344** | **344** |

---

## Study Plan

### Week 1-2: Foundation Patterns
- Binary Search (20 problems)
- Two Pointers (15 problems)
- Sliding Window (15 problems)

### Week 3-4: Stack & Heap
- Monotonic Stack (10 problems)
- Heap/Priority Queue (20 problems)

### Week 5-6: Graph & Trees
- Graph/BFS/DFS (25 problems)
- Tree Problems (20 problems)

### Week 7-8: DP & Advanced
- Dynamic Programming (30 problems)
- Backtracking (15 problems)

### Week 9-10: Mixed Practice
- Design Problems
- String/Math/Bit Problems
- Review weak areas
