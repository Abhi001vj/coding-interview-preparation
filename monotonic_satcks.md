Below is an “at‑a‑glance” cheat‑sheet that groups the problems you listed
by the kind of stack pattern they rely on, explains why that pattern
solves the problem, gives the typical Big‑O, and finishes with
actionable interview spotting tips.

🔑 Legend
MD‑stack = Monotone Decreasing stack

MI‑stack = Monotone Increasing stack

Op‑stack = Operator / value stack (expression parsing / evaluation)

Design = Implement data‑structure with stack(s)

Rec‑stack = Simulate recursion / tree traversal

Bal‑stack = Balanced parentheses or similar delimiter matching

#	Problem	Core pattern	How the stack is used	Time / Space
20	Valid Parentheses	Bal‑stack	push opening, pop on matching closing	O(n) / O(n)
42	Trapping Rain Water	MD‑stack	index stack stores decreasing heights; pop to close basins	O(n) / O(n)
85	Maximal Rectangle	MD‑stack (per row → hist)	reuse 84 logic row‑by‑row	O(m n) / O(n)
394	Decode String	Bal‑stack + Op	two stacks: counts and partial strings	O(n) / O(n)
84	Largest Rect. Histogram	MI‑stack	pop when current bar lower; area on each pop	O(n) / O(n)
224	Basic Calc (‑/+)	Op‑stack	sign / value stacks for parentheses	O(n) / O(n)
234	Palindrome Linked List	Rec‑stack or fast/slow + Bal‑stack	push first half values	O(n) / O(n)
94	In‑Order Traversal	Rec‑stack	iterative DFS	O(n) / O(h)
155	Min Stack	Design	extra stack of mins	push/pop O(1)
581	Shortest Unsorted Subarray	MD & MI combo	left scan MI, right scan MD	O(n) / O(1)
402	Remove K Digits	MD‑stack	build smallest number by popping bigger prev digits	O(n) / O(n)
143	Reorder List	Stack for second half	push 2nd half, interleave	O(n) / O(n)
975	Odd Even Jump	MI / MD maps + stack	next greater/smaller index via monotone stacks	O(n log n) / O(n)
232	Queue w/ Stacks	Design	two stacks (in/out)	amort. O(1) ops
225	Stack w/ Queues	Design	rotate queue on push	O(n) push / O(1) pop
150	Evaluate RPN	Value stack	push numbers, pop 2 on op	O(n) / O(n)
1944	Visible People	MD‑stack	next taller to right count	O(n) / O(n)
739	Daily Temps	MD‑stack	next warmer day	O(n) / O(n)
772	Basic Calculator III	Op‑stack (incl. * and /)	shunting‑yard style	O(n) / O(n)
3170	Lexicographically Min after *	MD‑stack of characters	keep smallest lexicographic	O(n) / O(n)
227	Basic Calculator II	Op‑stack (no parens)	keep last operand	O(n) / O(1)
2487	Remove Nodes From LL	MD‑stack / reverse pass	keep nodes ≥ max‑so‑far	O(n) / O(1)
1021	Remove Outermost Parens	Bal‑stack counter	track depth, skip depth = 1	O(n) / O(1)
921	Min Add to Make Valid	Bal‑stack counter	count unmatched opens/closes	O(n) / O(1)
144	Pre‑Order Traversal	Rec‑stack	iterative DFS	O(n) / O(h)
1130	Min Cost Tree From Leaf	MI‑stack	pop when middle ≤ right, cost += mid*min(neighbors)	O(n) / O(n)
1111	Max Nesting Depth Two Strings	Bal‑stack (depth)%2	assign alt depth to A/B	O(n) / O(1)

How to spot which stack pattern to apply
Symptom in the prompt	Likely pattern	Quick test
“Next greater/next smaller” • “visible to the right/left”	Monotone stack	Draw arrows; keep decreasing for next‑greater
“Remove digits/letters to keep smallest / largest sequence”	Monotone decreasing for smallest, increasing for largest	Think “greedy pop previous worse element”
“Evaluate / decode expression with nested delimiters”	Operator / Balanced‑stack	Parentheses or brackets present
“Need iter DFS/BFS but recursion not allowed”	Rec‑stack	Tree/graph traversal
“Implement data‑structure with constant ops”	Design stack/queue	Look for word “implement”
“Count matching (), return true/false, min adds”	Bal‑stack	Only two kinds of characters

Interview tips & gotchas
Dupes vs strict monotonicity
Decide whether you keep ≤ or < while comparing with stack top.

Pop‑then‑process, or process‑then‑pop?
For water/rectangle problems you pop first, because the popped element is
the middle/floor being evaluated.

Edge cases

Empty input → return 0 or empty.

Single element → no water / rectangle width 1.

All equal heights → ensure loops terminate.

Space
Mention worst‑case O(n) even if many interviewers think of stack as
“constant”; clarify the trade‑off.

Design problems (MinStack, Queue‑using‑Stacks)
Show amortized proof (in → out stack pattern) and discuss worst case.

Balance problems
A simple integer depth often replaces an explicit stack for (/)
(saves space).