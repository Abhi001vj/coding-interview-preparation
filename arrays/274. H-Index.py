# https://leetcode.com/problems/h-index/description/
# 274. H-Index
# Medium
# Topics
# Companies
# Hint
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1
 

# Constraints:

# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
"""
H-Index Problem - Comprehensive Solution Analysis
==============================================

Understanding H-Index:
-------------------
The h-index measures both productivity and citation impact of a researcher.
A researcher has h-index of h if they have at least h papers cited at least h times each.

Visual Example:
-------------
Citations: [3,0,6,1,5]
Sorted:    [6,5,3,1,0]
           ↑ ↑ ↑       These 3 papers have ≥3 citations each
h-index = 3

Visual representation of the concept:
Papers:     P1 P2 P3 P4 P5
Citations:   6  5  3  1  0
Threshold:   1  2  3  4  5
            ✓  ✓  ✓  ✗  ✗
"""
"""
Implementation of H-Index calculation with multiple approaches.
Each solution includes detailed visualization and step-by-step explanation.
"""
"""
Additional Insights for Interviews:
--------------------------------
1. Solution Evolution:
   - Start with intuitive sorting approach
   - Optimize using counting when value range is known
   - Consider binary search for different constraints

2. Edge Cases:
   - Empty citation list
   - All zeros
   - All same values
   - Single paper
   - Very large citation counts

3. System Design Considerations:
   - Real-time h-index calculation
   - Distributed computation
   - Memory vs speed trade-offs
   - Updates and maintenance

4. Code Quality:
   - Clear variable names
   - Comprehensive comments
   - Error handling
   - Modular design
"""
from typing import List

class HIndexSolutions:
    def approach1_sorting(self, citations: List[int]) -> int:
        """
        Sorting-based approach for H-Index calculation.
        
        Visual example of the process:
        Input: [3,0,6,1,5]
        
        Step 1: Sort descending
        [6,5,3,1,0]
         ↑ position 1: 6 >= 1 ✓ (h could be 1)
         ↑ position 2: 5 >= 2 ✓ (h could be 2)
         ↑ position 3: 3 >= 3 ✓ (h could be 3)
         ↑ position 4: 1 < 4  ✗ (stop here)
        
        Therefore h-index = 3
        """
        # Sort citations in descending order for efficient checking
        citations.sort(reverse=True)
        n = len(citations)
        
        # Find largest h where h papers have at least h citations
        # Example: [6,5,3,1,0]
        # i=0: 6 >= 1 true, h=1
        # i=1: 5 >= 2 true, h=2
        # i=2: 3 >= 3 true, h=3
        # i=3: 1 >= 4 false, break
        h = 0
        for i in range(n):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
                
        return h

    def approach2_counting_sort(self, citations: List[int]) -> int:
        """
        Counting sort approach for H-Index calculation.
        
        Visual example of counting process:
        Input: [3,0,6,1,5]
        
        Step 1: Count frequencies (capped at n=5)
        Index:  0  1  2  3  4  5
        Count:  1  1  0  1  0  2
        
        Step 2: Calculate cumulative counts from right
        Index:  5  4  3  2  1  0
        Count:  2  2  3  3  4  5
        Return when count >= index (at 3)
        """
        n = len(citations)
        # Create counting array where counts[i] = number of papers with i citations
        # For [3,0,6,1,5], after counting:
        # counts = [1,1,0,1,0,2] meaning:
        # 1 paper with 0 citations
        # 1 paper with 1 citation
        # 0 papers with 2 citations
        # 1 paper with 3 citations
        # 0 papers with 4 citations
        # 2 papers with 5+ citations
        counts = [0] * (n + 1)
        
        # Count citations, capping at n since we can't have h-index > n
        for citation in citations:
            counts[min(citation, n)] += 1
            
        # Scan from right to left, accumulating papers
        # When total papers >= current index, we've found h-index
        total = 0
        for i in range(n, -1, -1):
            total += counts[i]  # Add papers with i citations
            if total >= i:      # If enough papers with ≥i citations
                return i
        return 0

    def approach3_binary_search(self, citations: List[int]) -> int:
        """
        Binary search approach for H-Index calculation.
        
        Visual example of binary search process:
        Input: [3,0,6,1,5], n=5
        
        Step 1: Search range [0,5]
        mid=3: count papers ≥3 (3,6,5) = 3 papers ✓
        
        Step 2: Search range [3,5]
        mid=4: count papers ≥4 (6,5) = 2 papers ✗
        
        Step 3: Search range [3,3]
        Found h-index = 3
        """
        left, right = 0, len(citations)
        
        while left < right:
            # Try a potential h-index value
            mid = (left + right + 1) // 2
            
            # Count papers with at least mid citations
            # Example: mid=3, citations=[3,0,6,1,5]
            # Count papers ≥3: [3,6,5] = 3 papers
            count = sum(1 for c in citations if c >= mid)
            
            # If enough papers have ≥mid citations,
            # try a larger h-index
            if count >= mid:
                left = mid
            # Otherwise, try a smaller h-index
            else:
                right = mid - 1
                
        return left

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_counts = [0]*(n+1)

        for c in citations:
            paper_counts[min(n,c)] += 1

        h = n
        papers = paper_counts[n]

        while papers < h:
            h -= 1
            papers += paper_counts[h]
        
        return h
    
def main():
    # Test case demonstrating all approaches
    citations = [3, 0, 6, 1, 5]
    solver = HIndexSolutions()
    
    print("H-Index Analysis for citations =", citations)
    print("Sorting approach:", solver.approach1_sorting(citations.copy()))
    print("Counting approach:", solver.approach2_counting_sort(citations.copy()))
    print("Binary search approach:", solver.approach3_binary_search(citations.copy()))

if __name__ == "__main__":
    main()