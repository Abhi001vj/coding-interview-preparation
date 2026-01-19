from typing import List
import collections

# FAANG Interview Stage 1: Clarify
# Q: Return indices? -> "Yes, starting indices"
# Q: Order matters? -> "No"

# FAANG Interview Stage 2: Plan
# Approach: Fixed Sliding Window
# 1. Count p (target).
# 2. Maintain window of size len(p).
# 3. Add s[right], Remove s[left] (if window too big).
# 4. If counts match, add index.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = collections.Counter(p)
        s_count = collections.Counter()
        
        output = []
        
        # Initialize first window (size np-1) to make loop cleaner
        # Or just loop normally
        
        for i in range(ns):
            # Add right char
            s_count[s[i]] += 1
            
            # Remove left char (if window exceeded size)
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            
            # Check match
            if s_count == p_count:
                output.append(i - np + 1)
        
        return output

if __name__ == "__main__":
    solver = Solution()
    print(f"Test 1: {solver.findAnagrams('cbaebabacd', 'abc')} (Expected: [0, 6])")
    print(f"Test 2: {solver.findAnagrams('abab', 'ab')} (Expected: [0, 1, 2])")
