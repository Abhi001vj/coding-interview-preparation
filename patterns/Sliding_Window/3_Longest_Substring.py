from typing import List
import collections

# FAANG Interview Stage 1: Clarify
# Q: What characters? (Ascii? Unicode? English letters?) -> "Assume English letters, symbols, spaces"
# Q: Case sensitive? -> "Yes"
# Q: Constraints? -> "0 <= s.length <= 5 * 10^4" (Need O(N))

# FAANG Interview Stage 2: Plan
# Approach: Sliding Window
# 1. Maintain a window [left, right] that contains unique characters.
# 2. Expand 'right'. If s[right] is already in the window (duplicate), shrink 'left' until the duplicate is removed.
# 3. Track max_len at each valid step.
# Complexity: Time O(N) (each char added/removed once), Space O(min(N, charset))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # FAANG Interview Stage 3: Code
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # While duplicate exists, shrink from left
            # "Talk through": We found a duplicate s[right], so we must evict 
            # everything up to the previous occurrence of s[right]
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Now window is valid, add new char
            char_set.add(s[right])
            
            # Update result
            max_len = max(max_len, right - left + 1)
            
        return max_len

# FAANG Interview Stage 4: Verify (Tests)
if __name__ == "__main__":
    solver = Solution()
    
    # Test 1: Standard
    # Window trace: [a] -> [ab] -> [abc] -> [bca] (pop a) -> [cab] (pop b) ...
    # Result: 3
    print(f"Test 1 ('abcabcbb'): {solver.lengthOfLongestSubstring('abcabcbb')} (Expected: 3)")
    
    # Test 2: All same
    print(f"Test 2 ('bbbbb'): {solver.lengthOfLongestSubstring('bbbbb')} (Expected: 1)")
    
    # Test 3: Substring inside
    print(f"Test 3 ('pwwkew'): {solver.lengthOfLongestSubstring('pwwkew')} (Expected: 3)")
    
    # Test 4: Empty
    print(f"Test 4 (''): {solver.lengthOfLongestSubstring('')} (Expected: 0)")
