2  Sliding‑window anatomy
Pointer	Role	Typical operations
right	Expands the window one element at a time.	Add nums[right] to bookkeeping structures.
left	Shrinks the window when constraints break.	Remove nums[left]; increment left.
Book‑keeping	Tracks window state so we can test the constraint quickly.	Here it’s a freq map; in an optimized version you’d keep monotone deques for min and max.

Invariants maintained
Window [left, right] always satisfies max‑min ≤ 2.
The inner while loop restores this after inserting nums[right].

All subarrays counted end at right.
Once the invariant is true again, every starting point k in [left, right] forms a valid subarray (k, …, right).

3  Why count += (right‑left+1) is correct
Think of fixing right and sliding left:

makefile
Copy
Edit
nums:     [ a  b  c  d  e ]
index:      0  1  2  3  4
                      ↑right
          ↑left
After the while loop, the window [left, right] is the longest possible segment ending at right that still respects the constraint.
For any start index k with left ≤ k ≤ right, the segment [k, right] is also valid—because removing elements from the left cannot increase (max‑min).

Hence:

sql
Copy
Edit
number of valid subarrays that end at index right
        =  length of the current window
        =  right - left + 1
Accumulating that value for every right enumerates each qualifying subarray exactly once.

Why isn’t [left, right] just “one subarray”?
Because we’re counting all possible lengths: [left, right], [left+1, right], …, [right, right].

4  Complexity
Aspect	Cost
Time	 O(n · C) where C = cost of max(freq) and min(freq) calls (here ≤ 10 because width ≤ 10, otherwise use deques for O(1)).
Space	 O(u) where u = unique values in window (≤ 101 per constraints).

An optimized version replaces max(freq)/min(freq) (which are O(u)) with two monotone deques so the whole algorithm is pure O(n).

5  Sibling LeetCode problems that use the same counting trick
Problem	Core constraint	Sliding‑window detail
713. Subarray Product < K	Product constraint	count += right-left+1 when product under threshold.
930. Binary Subarrays With Sum	Sum in fixed window	Two‑pointer count of subarrays with sum = K via at most K minus at most K‑1.
992. Subarrays with K Different Integers	Exactly K uniques	atMost(K) – atMost(K-1); each atMost uses the same right-left+1 trick.
1248. Count Number of Nice Subarrays	Exactly K odds	Reduces to previous problem.
1838. Frequency of the Most Frequent Element	Maximize freq with limited total adds	Window where (right-left+1)*max ≤ sum+k. Count windows as they grow.
2401. Longest Nice Subarray	Bitwise‑AND = 0	Same expand/contract pattern; counts or tracks length.
1456. Maximum Vowels in Substring of Length L	Fixed length window	Sliding window but length constrained.
424. Longest Repeating Character Replacement	Window where (size‑max_freq)≤K	Same deques idea.
1658. Min Ops to Reduce X to 0	Find longest subarray with sum = total‑X via window.	

Studying these together helps you recognise two archetypes:

“At most” counter: Count windows where a metric ≤ threshold (product, sum, distinct count, max‑min).
→ Use right-left+1.

“Longest / shortest window” finder: Maintain a single best length, don’t accumulate.

Understanding when to count vs when to track a max is a favourite interviewer probe.

6  Typical follow‑up questions & great answers
Question	What they test	Key talking points
Q1. How would you get pure O(n) without max(freq) / min(freq) scans?	Data‑structure fluency	Maintain two monotone deques: one keeps potential max candidates in decreasing order, the other min candidates in increasing order.
Q2. Can you handle a larger range, e.g. max‑min ≤ k where k may be 1e5?	Scalability thinking	Same algorithm; constraint only affects deque logic, not asymptotics.
Q3. How to modify if bricks must contain at most 2 distinct numbers (not value range)?	Generalisation	Replace deques with a Counter and maintain len(counter) ≤ 2.
Q4. Why do we add (right‑left+1) instead of (right‑left)?	Attention to fence‑posts	Explain off‑by‑one logic clearly—window length formula.
Q5. How do you count subarrays WHERE (max‑min) == 2 exactly?	Edge adjustments	Answer: Count ≤ 2 minus count ≤ 1. Standard at‑most/at‑most‑1 difference technique.

7  Interview‑ready takeaways
Pattern recognition: Anytime the property is monotone when you drop elements from the left, suspect a sliding window.

Window length trick:
Counting subarrays that end at right ⇒ add right‑left+1.
Finding a single best window ⇒ update a best variable.

Double‑ended queues solve “maintain max/min in O(1)”—quote the “sliding‑window maximum” problem (LeetCode 239) as precedent.

At‑most vs exact: Many “exact‑K” problems become “atMost(K) − atMost(K‑1)”.

Explain invariants. State them explicitly; interviewers look for that discipline.

Edge cases: empty array, window shrinks to empty, duplicate deletes in map, modulus overflow if counting huge.