1  What is the monotonic‑queue pattern?
A monotonic queue (usually implemented with a deque in Python) is a double‑ended queue that keeps its elements in sorted order—either non‑increasing (for maxima) or non‑decreasing (for minima) from front → back. It supports:

Operation	Cost	What it means
push(x)	 O(1) amortized	Pop items from the back that break the order, then append x.
pop_front()	O(1)	Remove expired element if it is exactly the one leaving the window.
front()	O(1)	Peek the max / min of the current window.

Because every index is inserted and removed once, the whole algorithm is O(n).

2  Why a deque and not a stack?
A stack only lets you remove from the same end you insert.
In sliding‑window problems an element can “expire” from the front of the window (when it slides past i‑k). If the expired index sits at the front of the structure you need O(1) removal.

A deque gives two‑end access: we discard smaller elements from the back when inserting (while nums[q[-1]] ≤ cur) and discard an expired maximum from the front (if q[0] == i‑k).

Hence the deque is the minimal data structure that lets us maintain both properties:

monotonic order (handle the back),

fast eviction of the oldest element (handle the front).

3  Line‑by‑line of your code
python
Copy
Edit
q = deque()               # stores *indices*, not values

for i, cur in enumerate(nums):

    # (A) Maintain non‑increasing order from front→back
    while q and nums[q[-1]] <= cur:
        q.pop()           # smaller values can never be max again

    q.append(i)           # push current index

    # (B) Remove index that slid out of the window [i-k+1 .. i]
    if q[0] == i - k:
        q.popleft()

    # (C) Collect answer when first full window is formed
    if i >= k - 1:
        output.append(nums[q[0]])   # front is the current maximum
Invariant: nums[q[0]] ≥ nums[q[1]] ≥ … ≥ nums[q[-1]] and every index in q is within the current window.

4  Compare with the monotonic stack pattern
Aspect	Monotonic queue	Monotonic stack
Access ends	Front and back	Only the back
Typical task	Sliding‑window max/min	Next greater/previous smaller element
Pop reason	Either because smaller than current or out of window	Only because smaller (or larger) than current
Example problems	Sliding Window Maximum, Minimum in Sliding Window, Number of Subarrays With Bounded Maximum	Largest Rectangle in Histogram, Daily Temperatures, Next Greater Element I/II

5  How to spot the pattern in interviews
Window of size k that shifts one step per iteration.

Need to output max/min (or monotone statistic) for every position.

Constraints demand O(n) or better; naive O(n k) is too slow.

The interviewer often phrases it as “For every index i, give me X of the last k elements”.

6  Other LeetCode problems solvable by a monotonic queue
ID	Title	Max/Min?	Twist
239	Sliding Window Maximum	Max	Canonical example (this one)
480	Sliding Window Median	Both—but needs two heaps plus lazy delete	Hard variant
1438	Longest Subarray with Diff ≤ Limit	Need to track both max & min	Two deques
1696	Jump Game VI	DP with windowed max	Deque over DP values
862	Shortest Subarray with Sum ≥ K	Deque on prefix sums	Indices represent candidate starts
1004	Max Consecutive Ones III	Count of zeros ≤ K—can also be done with single deque or two‑pointer	
2398	Maximum Number of Robots Within Budget	Maintain max + window sum	Deque + prefix sums

7  Interview checklist for getting it right
Explain the invariants first.
“The deque stores indices in decreasing values; the front is always the max of the current window.”

Handle out‑of‑window eviction before using q[0].

Store indices, not values—lets you decide if an element expired.

Complexity statement:
“Each index enters and leaves the deque once → O(n) time, O(k) space (≤ n).”

Edge cases: k = 1, k = n, duplicates in nums, negative values.