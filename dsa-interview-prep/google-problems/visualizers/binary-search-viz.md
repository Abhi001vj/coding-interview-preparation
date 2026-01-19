# Binary Search Pattern Visualizer

## Base Template

```python
def binary_search_min(lo, hi, is_valid):
    while lo < hi:
        mid = (lo + hi) // 2
        if is_valid(mid):
            hi = mid      # Keep mid, search left
        else:
            lo = mid + 1  # Skip mid, search right
    return lo
```

---

## How It Works: Step-by-Step Animation

### Finding Minimum Valid Value

```
Problem: Find smallest X where condition is TRUE

Search Space: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Condition:     ❌  ❌  ❌  ❌  ✅  ✅  ✅  ✅  ✅
                              ↑
                        Answer = 5

═══════════════════════════════════════════════════════════════════════

STEP 1: lo=1, hi=9
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
  ↑                   ↑               ↑
  lo              mid=5              hi

mid = (1+9)//2 = 5
is_valid(5)? ✅ YES
→ hi = mid = 5   (keep 5, it might be answer!)

═══════════════════════════════════════════════════════════════════════

STEP 2: lo=1, hi=5
┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │
└───┴───┴───┴───┴───┘
  ↑       ↑       ↑
  lo    mid=3    hi

mid = (1+5)//2 = 3
is_valid(3)? ❌ NO
→ lo = mid + 1 = 4   (skip 3, definitely wrong)

═══════════════════════════════════════════════════════════════════════

STEP 3: lo=4, hi=5
┌───┬───┐
│ 4 │ 5 │
└───┴───┘
  ↑   ↑
  lo  hi
mid=4

mid = (4+5)//2 = 4
is_valid(4)? ❌ NO
→ lo = mid + 1 = 5

═══════════════════════════════════════════════════════════════════════

STEP 4: lo=5, hi=5
┌───┐
│ 5 │
└───┘
  ↑
lo=hi

STOP! lo == hi
Return 5 ✅

═══════════════════════════════════════════════════════════════════════
```

---

## Example 1: LC 875 - Koko Eating Bananas

**Problem:** Koko eats k bananas/hour. Find minimum k to finish all piles in h hours.

```
piles = [3, 6, 7, 11], h = 8

Speed k=1:  ceil(3/1) + ceil(6/1) + ceil(7/1) + ceil(11/1) = 3+6+7+11 = 27 hours ❌
Speed k=4:  ceil(3/4) + ceil(6/4) + ceil(7/4) + ceil(11/4) = 1+2+2+3 = 8 hours  ✅
Speed k=5:  ceil(3/5) + ceil(6/5) + ceil(7/5) + ceil(11/5) = 1+2+2+3 = 8 hours  ✅

Answer: 4 (minimum k where hours ≤ 8)
```

**Visualization:**

```
Search: k ∈ [1, 11]  (1 to max(piles))

k:        1    2    3    4    5    6    7    8    9   10   11
hours:   27   15   12    8    8    7    6    5    4    4    4
valid:    ❌   ❌   ❌   ✅   ✅   ✅   ✅   ✅   ✅   ✅   ✅
                        ↑
                   Answer = 4

Binary Search Trace:
┌─────────────────────────────────────────────────────────────┐
│  lo=1, hi=11, mid=6  → valid(6)=7hrs ✅ → hi=6             │
│  lo=1, hi=6,  mid=3  → valid(3)=12hrs ❌ → lo=4            │
│  lo=4, hi=6,  mid=5  → valid(5)=8hrs ✅ → hi=5             │
│  lo=4, hi=5,  mid=4  → valid(4)=8hrs ✅ → hi=4             │
│  lo=4, hi=4          → STOP! Return 4                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Example 2: LC 1011 - Capacity to Ship Packages

**Problem:** Ship packages in order within d days. Find minimum capacity.

```
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], d = 5

Capacity 15: [1,2,3,4,5] [6,7] [8] [9] [10] = 5 days ✅
Capacity 14: [1,2,3,4] [5,6] [7] [8] [9] [10] = 6 days ❌

Minimum capacity = 15
```

**Visualization:**

```
Ship packages sequentially, minimize max daily load:

weights: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

capacity=10:
Day 1: [1,2,3,4]=10 | Day 2: [5]=5 | Day 3: [6]=6 | Day 4: [7]=7
Day 5: [8]=8 | Day 6: [9]=9 | Day 7: [10]=10
→ 7 days > 5 ❌

capacity=15:
Day 1: [1,2,3,4,5]=15 | Day 2: [6,7]=13 | Day 3: [8]=8
Day 4: [9]=9 | Day 5: [10]=10
→ 5 days = 5 ✅

Search Space: [max(weights), sum(weights)] = [10, 55]
                    ↑                            ↑
              must fit largest            one day ships all
              single package
```

---

## Example 3: LC 1283 - Smallest Divisor Given Threshold

**Problem:** Find smallest divisor where sum of ceil(nums[i]/divisor) ≤ threshold.

```
nums = [1, 2, 5, 9], threshold = 6

Divisor 1: ceil(1/1)+ceil(2/1)+ceil(5/1)+ceil(9/1) = 1+2+5+9 = 17 ❌
Divisor 4: ceil(1/4)+ceil(2/4)+ceil(5/4)+ceil(9/4) = 1+1+2+3 = 7  ❌
Divisor 5: ceil(1/5)+ceil(2/5)+ceil(5/5)+ceil(9/5) = 1+1+1+2 = 5  ✅

Answer: 5
```

**Visualization:**

```
Key Insight: As divisor ↑, sum ↓ (monotonic!)

divisor:  1    2    3    4    5    6    7    8    9
sum:     17   12    9    7    5    5    4    4    4
valid:    ❌   ❌   ❌   ❌   ✅   ✅   ✅   ✅   ✅
                            ↑
                      Smallest valid

Visual of division:
nums = [1, 2, 5, 9]

div=5:  ┌───────┐
        │ 1/5=1 │  ceil → 1
        │ 2/5=1 │  ceil → 1
        │ 5/5=1 │  ceil → 1
        │ 9/5=2 │  ceil → 2
        └───────┘
        sum = 5 ≤ 6 ✅
```

---

## Example 4: LC 1552 - Magnetic Force (Maximum Problem)

**Problem:** Place m balls in positions to MAXIMIZE minimum distance.

```
positions = [1, 2, 3, 4, 7], m = 3

Place 3 balls to maximize minimum distance between any two.

Distance 1: balls at [1,2,3] → min_dist=1
Distance 2: balls at [1,3,7] → min_dist=2
Distance 3: balls at [1,4,7] → min_dist=3 ✅
Distance 4: balls at [1,7] only 2 balls fit ❌

Answer: 3
```

**Visualization:**

```
Positions: 1  2  3  4  5  6  7
           ●──●──●──●──────●

Can we place 3 balls with min_distance=d?

d=1: [1,2,3] ✅
     ●──●──●

d=2: [1,3,7] ✅
     ●─────●──────────●

d=3: [1,4,7] ✅
     ●────────●─────────●

d=4: Only [1,7] works, can't fit 3 balls ❌

Search: Find MAXIMUM d where we can place m balls
Use: mid = (lo + hi + 1) // 2  ← +1 for maximum!
```

---

## Example 5: LC 410 - Split Array Largest Sum

**Problem:** Split array into k subarrays, minimize the largest sum.

```
nums = [7, 2, 5, 10, 8], k = 2

Split to minimize max subarray sum:

[7,2,5] + [10,8] → max(14, 18) = 18 ✅
[7,2,5,10] + [8] → max(24, 8) = 24 ❌

Answer: 18
```

**Visualization:**

```
nums = [7, 2, 5, 10, 8]

Goal: Split into k=2 parts, minimize largest part

If max_sum_allowed = X, how many parts needed?

X=15: [7,2,5] | [10] | [8] → 3 parts ❌ (>k)
X=18: [7,2,5] | [10,8] → 2 parts ✅
X=20: [7,2,5,10] is 24 > 20, so [7,2,5] | [10,8] → still 2 parts

Binary Search for minimum X where parts ≤ k:

     max(nums)=10        sum(nums)=32
          ↓                   ↓
Search: [10 ──────────────── 32]

X=10: Can't fit 10 alone ❌
X=18: [7,2,5] [10,8] = 2 parts ✅
X=15: [7,2,5] [10] [8] = 3 parts ❌

Answer: 18 (minimum X where parts ≤ 2)
```

---

## Pattern Summary

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BINARY SEARCH ON ANSWER                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  STEP 1: Identify the search space                                 │
│          lo = minimum possible answer                              │
│          hi = maximum possible answer                              │
│                                                                     │
│  STEP 2: Define is_valid(mid) function                             │
│          Returns True if mid satisfies the condition               │
│                                                                     │
│  STEP 3: Use correct template                                      │
│                                                                     │
│          FIND MINIMUM:              FIND MAXIMUM:                   │
│          mid = (lo+hi)//2           mid = (lo+hi+1)//2              │
│          if valid:                  if valid:                       │
│              hi = mid                   lo = mid                    │
│          else:                      else:                           │
│              lo = mid + 1               hi = mid - 1                │
│                                                                     │
│  STEP 4: Return lo (they converge to same value)                   │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  KEY INSIGHT: The answer space is MONOTONIC                        │
│                                                                     │
│  For MINIMUM: [❌ ❌ ❌ ❌ ✅ ✅ ✅ ✅]                              │
│                          ↑ answer                                   │
│                                                                     │
│  For MAXIMUM: [✅ ✅ ✅ ✅ ❌ ❌ ❌ ❌]                              │
│                       ↑ answer                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Common Boundaries

| Problem Type | lo | hi |
|--------------|----|----|
| Eating speed | 1 | max(piles) |
| Ship capacity | max(weights) | sum(weights) |
| Divisor | 1 | max(nums) |
| Distance | 1 | max_pos - min_pos |
| Split array sum | max(nums) | sum(nums) |
| Days to bloom | min(bloomDay) | max(bloomDay) |
