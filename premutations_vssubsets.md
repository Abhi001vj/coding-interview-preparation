1  Permutations vs Subsets—concept & use‑cases
Permutations	Subsets (Power‑set)
What?	All order‑sensitive arrangements of the elements.	All order‑insensitive selections of elements (every combination, including empty set).
Count	n! (factorial) for n distinct items.	2ⁿ (every element either present or absent).
Typical use cases	• Generating every possible ordering (e.g., travelling‑salesman brute force, anagrams, seating arrangements).
• Problems that care about sequence or ordering.	• Feature‑subset search, subset‑sum / knapsack, “can we partition?”, powerset enumeration for bitmask DP, picking any combination regardless of order.
DSA Pattern	DFS / back‑tracking with “choose, explore, un‑choose” and a used boolean array.	DFS back‑tracking that branches on “include current element or not” (or iterative bitmask).
Key difference	Order matters—[a,b] and [b,a] are different.	Order doesn’t matter—[a,b] and [b,a] are the same subset.

2  Big‑O analysis of the two snippets
Function	Output size	Time	Space (incl. output)
permute_word	n! strings	O(n · n!) – each of n! leaves copies an n‑char path	O(n · n!) output + O(n) recursion stack/aux arrays
subsets	2ⁿ lists	O(n · 2ⁿ) – each subset copy takes O(n)	O(n · 2ⁿ) output + O(n) recursion stack

⚠️ The exponential factor comes from the number of answers you’re required to return, so no algorithm can asymptotically beat that for full enumeration.

3  Top 5 “subset” interview questions
#	Problem (LeetCode #)	Core idea / answer sketch	Time / Space
1	Subsets ( 78 )	Classic power‑set. DFS include/exclude or iterative bitmask.	O(n · 2ⁿ) / same
2	Subsets II ( 90 , duplicates)	Sort first, skip identical elements on the include branch to avoid duplicates.	O(n · 2ⁿ) worst / same
3	Combination Sum ( 39 )	Back‑tracking with running total; allow re‑use of same number by keeping index i in recursive call.	O(Σ) exponential in #solutions / recursion O(target/ min)
4	Partition to K Equal‑Sum Subsets ( 698 )	Bitmask DP or back‑tracking with pruning; keep current bucket sum, short‑circuit when a bucket matches target.	O(k · 2ⁿ) DP variant / O(2ⁿ)
5	Subset Sum / Can Reach Target (classic, LC 416 for 2‑way)	DP on total or bitset trick. For enumeration, back‑track; for boolean answer, 1‑D knapsack DP.	enumeration O(n · 2ⁿ); boolean DP O(n · target)

4  Top 5 “permutation” interview questions
#	Problem (LeetCode #)	Core idea / answer sketch	Time / Space
1	Permutations ( 46 )	DFS + used[] as in your snippet.	O(n · n!) / O(n · n!)
2	Permutations II ( 47 , duplicates)	Sort input, skip a duplicate nums[i] when nums[i] == nums[i‑1] and used[i‑1] is False.	O(n · n!) worst / same
3	Next Permutation ( 31 )	Scan from right to find first i with nums[i] < nums[i+1], swap with next larger element on the right, reverse suffix.	O(n) / O(1)
4	K‑th Permutation Sequence ( 60 )	Factoradic / factorial number system: build answer digit‑by‑digit using (k‑1)//(n‑1)! indexing.	O(n²) if using list pops / O(n)
5	Permutation in String ( 567 , substring check)	Sliding window of length len(p) + 26‑char freq arrays; check equality.	O(n) / O(1)

5  When to reach for which pattern
Goal	Preferred pattern
“Need all orderings of n items.”	Permutation DFS with used[].
“Need all combinations irrespective of order.”	Subset DFS include/exclude or bitmask iteration.
“Need the k‑th lexicographic ordering.”	Factorial‑number‑system direct math (Perm. #4).
“Need to know whether a subset exists with some property.”	Bitmask DP / knapsack; enumerate only if you must output actual subsets.
“List all sums/ways until you hit a target but stop early.”	DFS with pruning + sorting to break recursion quickly.

Keep these templates and complexity figures handy—interviewers love follow‑ups like “how would you handle duplicates?” or “what if we only want existence, not enumeration?” A quick pivot from enumeration‑heavy O(n · 2ⁿ) / O(n · n!) to a DP or greedy answer shows depth.

# Permutations vs Subsets – Interview Cheat Sheet

---

## 1  Concepts & Use‑Cases

|                         | **Permutations**                                                                | **Subsets / Power‑set**                                            |
| ----------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Definition**          | All *order‑sensitive* arrangements of the elements.                             | All *order‑insensitive* selections of elements, incl. empty set.   |
| **Count**               | `n!` for `n` distinct items.                                                    | `2ⁿ` possibilities.                                                |
| **Key Use‑Cases**       | Travelling‑salesman brute force, anagrams, seating orders, scheduler search.    | Feature selection, subset‑sum, knapsack, partition, bitmask DP.    |
| **Algorithmic Pattern** | DFS / back‑tracking with **choose → explore → un‑choose** and a `used[]` array. | DFS that **branches include / exclude** (or iterate all bitmasks). |
| **Core Difference**     | `[a,b] ≠ [b,a]`.                                                                | `[a,b] ≡ [b,a]`.                                                   |

---

## 2  Complexities

| Function       | Output Size  | Time        | Space (incl. output)       |
| -------------- | ------------ | ----------- | -------------------------- |
| `permute_word` | `n!` strings | `O(n · n!)` | `O(n · n!)` + `O(n)` stack |
| `subsets`      | `2ⁿ` lists   | `O(n · 2ⁿ)` | `O(n · 2ⁿ)` + `O(n)` stack |

⚠️ Enumeration cost is unavoidable; complexity is dominated by number of answers.

---

## 3  Top Subset Problems

|  #                 | Problem & Link      | Quick Idea             | Template Code | Time / Space |
| ------------------ | ------------------- | ---------------------- | ------------- | ------------ |
| 1                  | **Subsets** (LC 78) | Classic power‑set DFS. | \`\`\`python  |              |
| def subsets(nums): |                     |                        |               |              |

```
 res = []
 def dfs(i, path):
     if i == len(nums):
         res.append(path[:])
         return
     dfs(i+1, path)            # exclude
     dfs(i+1, path+[nums[i]])   # include
 dfs(0, [])
 return res
```

``| `O(n·2ⁿ)` / same | | 2 | **Subsets II** (LC 90, dupes) | Sort & skip duplicates on *include* branch. |``python
def subsetsWithDup(nums):
nums.sort()
res = \[]
def dfs(i, path):
res.append(path\[:])
for j in range(i, len(nums)):
if j>i and nums\[j]==nums\[j-1]:
continue
dfs(j+1, path+\[nums\[j]])
dfs(0, \[])
return res
``| `O(n·2ⁿ)` / same | | 3 | **Combination Sum** (LC 39) | Back‑track keeping running total; reuse allowed. |``python
def combinationSum(nums, target):
nums.sort()
res = \[]
def dfs(i, remain, path):
if remain==0:
res.append(path\[:]); return
if remain<0 or i==len(nums):
return
\# choose i
dfs(i, remain-nums\[i], path+\[nums\[i]])
\# skip i
dfs(i+1, remain, path)
dfs(0, target, \[])
return res

````| exponential / stack depth ≤ target/min |
| 4 | **Partition to K Equal‑Sum Subsets** (LC 698) | Bitmask DP or backtrack with buckets. | Skeleton:
```python
def canPartitionK(nums,k):
    target=sum(nums)//k
    nums.sort(reverse=True)
    used=[False]*len(nums)
    def backtrack(start,k,cur):
        if k==1: return True
        if cur==target:
            return backtrack(0,k-1,0)
        for i in range(start,len(nums)):
            if used[i] or cur+nums[i]>target: continue
            used[i]=True
            if backtrack(i+1,k,cur+nums[i]): return True
            used[i]=False
            if cur==0: break
        return False
    return sum(nums)%k==0 and backtrack(0,k,0)
``` | `O(k·2ⁿ)` DP / `O(2ⁿ)` |
| 5 | **Subset Sum / 0‑1 Knapsack Exists** (LC 416) | 1‑D DP bitset. | ```python
def canPartition(nums):
    s=sum(nums)
    if s&1: return False
    target=s//2
    bits=1
    for x in nums:
        bits |= bits<<x
    return (bits>>target)&1
``` | `O(n·target)` → bitset `O(n·s/64)` / `O(target)` |

---
## 4  Top Permutation Problems

| # | Problem & Link | Idea | Template Code | Time / Space |
|---|---|---|---|---|
| 1 | **Permutations** (LC 46) | DFS with `used[]`. | ```python
def permute(nums):
    res, path, used = [], [], [False]*len(nums)
    def dfs():
        if len(path)==len(nums):
            res.append(path[:]); return
        for i,n in enumerate(nums):
            if used[i]: continue
            used[i]=True; path.append(n)
            dfs()
            path.pop(); used[i]=False
    dfs(); return res
``` | `O(n·n!)` / same |
| 2 | **Permutations II** (LC 47) | Sort & skip duplicates when `used[i-1]==False`. | ```python
def permuteUnique(nums):
    nums.sort(); res=[]; used=[False]*len(nums)
    def dfs(path):
        if len(path)==len(nums): res.append(path[:]); return
        for i in range(len(nums)):
            if used[i] or (i and nums[i]==nums[i-1] and not used[i-1]):
                continue
            used[i]=True; dfs(path+[nums[i]]); used[i]=False
    dfs([]); return res
``` | `O(n·n!)` / same |
| 3 | **Next Permutation** (LC 31) | Rightmost ascent, swap, reverse suffix. | ```python
def nextPermutation(nums):
    i=len(nums)-2
    while i>=0 and nums[i]>=nums[i+1]: i-=1
    if i>=0:
        j=len(nums)-1
        while nums[j]<=nums[i]: j-=1
        nums[i],nums[j]=nums[j],nums[i]
    nums[i+1:]=reversed(nums[i+1:])
``` | `O(n)` / `O(1)` |
| 4 | **K‑th Permutation Sequence** (LC 60) | Factorial numeral system. | ```python
from math import factorial
def getPermutation(n,k):
    nums=list(map(str,range(1,n+1)))
    k-=1; res=[]
    for i in range(n,0,-1):
        idx,k=divmod(k,factorial(i-1))
        res.append(nums.pop(idx))
    return ''.join(res)
``` | `O(n²)` / `O(n)` |
| 5 | **Permutation in String** (LC 567) | Sliding window freq compare. | ```python
def checkInclusion(p,s):
    if len(p)>len(s): return False
    cnt=[0]*26
    for c in p: cnt[ord(c)-97]+=1
    diff=len(p)
    for i,ch in enumerate(s):
        idx=ord(ch)-97
        cnt[idx]-=1; diff-= (cnt[idx]>=0)
        if i>=len(p):
            idx2=ord(s[i-len(p)])-97
            diff+= (cnt[idx2]>=0)
            cnt[idx2]+=1
        if diff==0: return True
    return False
``` | `O(n)` / `O(1)` |

---
## 5  Choosing the Right Pattern

> **All orderings needed?** → use *Permutations* template.
>
> **All combinations (orderless)?** → use *Subsets* template.
>
> **Only k‑th lexicographic ordering?** → use factorial‑number‑system approach.
>
> **Need existence / optimisation, not enumeration?** → transform into DP/greedy (e.g., knapsack, bitset subset‑sum).  
>
> **Enumerate but stop early on condition?** → DFS with pruning & sorting.

---
### Quick Reference – Generic Template Snippets

```python
# Generic permutation DFS (with duplicates handled if input sorted)

def permute_backtrack(arr):
   arr.sort()
   res, used = [], [False]*len(arr)
   def dfs(path):
       if len(path)==len(arr):
           res.append(path[:]); return
       for i,v in enumerate(arr):
           if used[i] or (i and arr[i]==arr[i-1] and not used[i-1]):
               continue
           used[i]=True; dfs(path+[v]); used[i]=False
   dfs([])
   return res

# Generic subsets (include/exclude)

def subsets_backtrack(arr):
   res=[]
   def dfs(i,path):
       if i==len(arr): res.append(path[:]); return
       dfs(i+1,path)          # exclude
       dfs(i+1,path+[arr[i]]) # include
   dfs(0,[])
   return res
````

<div align="center">✨  Keep this sheet for last‑minute interview refreshers!  ✨</div>
