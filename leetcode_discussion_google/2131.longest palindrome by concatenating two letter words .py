<!-- https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/

Code
Testcase
Test Result
Test Result
2131. Longest Palindrome by Concatenating Two Letter Words
Medium
Topics
Companies
Hint
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters. -->

"""
Longest Palindrome by Concatenating Two Letter Words

Key Insights:
1. Two types of word pairs we need to handle:
   - Different letter pairs (like "lc" and "cl")
   - Same letter pairs (like "gg")
2. For palindromes:
   - Can use pairs of reversible words
   - Only one same-letter word can be in center

Complete Solution with Explanations:
"""

from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        Finds the longest palindrome that can be made by concatenating word pairs.
        
        Example 1: ["lc","cl","gg"]
        - Can use "lc" + "gg" + "cl" = "lcggcl" (length 6)
        
        Example 2: ["cc","ll","xx"]
        - Can only use one same-letter word (e.g., "cc") since only one can be center
        - Output: 2
        
        Example visualization for ["lc","cl","gg"]:
        1. Count frequencies:
           counts = {"lc": 1, "cl": 1, "gg": 1}
        
        2. Process pairs:
           "lc" and "cl":
           - Can use together: length += 4
           
           "gg":
           - Can use in center: length += 2
           
        Final length = 6 ("lcggcl")
        
        Time: O(n) for counting and processing words
        Space: O(1) since we only store 2-letter words
        """
        counts = Counter(words)
        length = 0
        central = False  # Track if we've used a center word
        
        for word in counts:
            # Case 1: Different letters (like "lc")
            if word[0] != word[1]:
                reverse = word[1] + word[0]
                if reverse in counts:
                    pairs = min(counts[word], counts[reverse])
                    length += 4 * pairs  # Each pair adds 4 to length
                    counts[word] -= pairs
                    counts[reverse] -= pairs
            
            # Case 2: Same letters (like "gg")
            else:
                pairs = counts[word] // 2  # Complete pairs we can use
                length += 4 * pairs  # Each pair adds 4 to length
                # Can only use one word in center
                if counts[word] % 2 and not central:
                    length += 2
                    central = True
        
        return length

"""
Detailed Examples:

1. ["lc","cl","gg"]
   counts = {"lc": 1, "cl": 1, "gg": 1}
   
   Process "lc":
   - Found "cl", can use as pair
   - length += 4
   
   Process "gg":
   - Same letters, can use in center
   - length += 2
   
   Final length = 6 ("lcggcl")

2. ["cc","ll","xx"]
   counts = {"cc": 1, "ll": 1, "xx": 1}
   
   Process "cc":
   - Same letters
   - Can use in center (central = False)
   - length += 2
   - central = True
   
   Process "ll" and "xx":
   - Same letters but central = True
   - Cannot use in center
   
   Final length = 2 ("cc")

3. ["ab","ty","yt","lc","cl","ab"]
   counts = {"ab": 2, "ty": 1, "yt": 1, "lc": 1, "cl": 1}
   
   Process pairs:
   - "ty"+"yt": length += 4
   - "lc"+"cl": length += 4
   
   Final length = 8 ("tylcclyt")

Time Complexity Analysis:
1. Counter creation: O(n)
2. Processing words: O(n)
   - Each word processed once
   - Constant time operations per word
Total: O(n)

Space Complexity Analysis:
1. Counter space: O(1)
   - Limited by possible 2-letter words (26*26)
2. Additional variables: O(1)
Total: O(1)

Key Points to Remember:

1. Different Letter Words:
   - Must find and use matching reverse pairs
   - Each pair contributes 4 to length
   - Need to update counts after using pairs

2. Same Letter Words:
   - Can use pairs normally (each adds 4)
   - Only ONE can be used in center
   - Must track central usage with boolean

3. Why Central Boolean is Needed:
   - Palindrome can only have one center
   - Multiple same-letter words might exist
   - Need to prevent using multiple centers

Edge Cases:

1. All Different Letter Words:
   ["ab", "cd"]
   Output: 0 (no pairs can be formed)

2. Multiple Same Letter Words:
   ["aa", "aa", "bb"]
   Output: 6 (can use both "aa"s)

3. Single Word:
   ["aa"]
   Output: 2 (can use as center)

Interview Tips:

1. Always explain why central tracking is needed
2. Demonstrate understanding of palindrome properties
3. Show clear separation of different and same letter cases
4. Consider mentioning optimizations:
   - Could use array instead of hash map
   - Could process same-letter words first
"""