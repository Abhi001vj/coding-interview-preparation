# 11. Container With Most Water

**Difficulty:** Medium
**Pattern:** Two Pointers (Greedy / Shrinking Window)

---

## 1. Google/Meta-Style Interview Transformation

**Raw Problem:** You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water.

**Interview Scenario (The "Optimization" Prompt):**
"Imagine we are building a dam or a retaining wall system using a set of available vertical barriers of varying heights placed at fixed intervals. We want to select two barriers to form the sides of a reservoir. The goal is to maximize the volume of water stored. The water level is limited by the shorter of the two barriers. How do you efficiently find the optimal pair of barriers?"

**Why this transformation?**
*   It moves away from abstract "lines" to a physical problem (volume/area).
*   It tests if you can formulate the objective function: $Area = (right - left) \times \min(height[left], height[right])$.

---

## 2. Clarifying Questions (Phase 1)

1.  **Input Format:** "Can heights be zero?" (Yes, but area would be zero).
2.  **Uniqueness:** "Are heights unique?" (No).
3.  **Result:** "Do I return the indices or the maximum area?" (Maximum area).
4.  **Constraints:** "Is $N$ large?" (Yes, $N$ up to $10^5$, implying an $O(N)$ solution is required. $O(N^2)$ will TLE).

---

## 3. Pattern Matching & Intuition

**Candidate Pattern:** Two Pointers (Converging).

**Why not Brute Force?**
Checking every pair $(i, j)$ is $O(N^2)$. With $N=10^5$, this is too slow (`10^10` ops).

**The Greedy Intuition:**
We want to maximize $Width \times Height$.
1.  Start with the maximum possible width (pointers at `0` and `n-1`).
2.  To maximize area, we need to potentially increase height to compensate for the decreasing width as we narrow the window.
3.  **Key Decision:** Which pointer do we move?
    *   The area is limited by the *shorter* line.
    *   If we move the *taller* line inward, the width decreases, and the new height cannot possibly be higher than the *shorter* line (which is the current bottleneck). So area **must** decrease or stay same.
    *   If we move the *shorter* line, the width decreases, BUT we *might* find a much taller line that increases the `min_height` enough to get a larger area.
    *   **Rule:** Always move the pointer pointing to the shorter line.

---

## 4. Base Template & Modification

**Standard Two Pointers (Converging):**
```python
left, right = 0, len(height) - 1
while left < right:
    # Logic
    if condition: left += 1
    else: right -= 1
```

**Modified Template:**
Use the height comparison as the condition for movement.

---

## 5. Optimal Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            # The height of the container is determined by the shorter wall
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update global max
            max_water = max(max_water, current_area)
            
            # Greedy Move: Move the shorter wall inward
            # Reasoning: Moving the taller wall can only result in the same or less area
            # (because width decreases and height is limited by the current short wall).
            # Moving the shorter wall gives us a CHANCE to find a taller wall.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
```

---

## 6. Big O Analysis

*   **Time Complexity:** $O(N)$
    *   The pointers `left` and `right` traverse the array exactly once.
*   **Space Complexity:** $O(1)$
    *   Only scalar variables used.

---

## 7. Follow-up & Extensions

**Q: What if the lines have width (thickness)?**
**A:** We would adjust the width calculation (e.g., `(right - left - thickness)`).

**Q: What if we wanted to find the container with the most water, but the water cannot rise above a certain level `L`?**
**A:** The height calculation becomes `min(height[left], height[right], L)`. The logic remains the same.
