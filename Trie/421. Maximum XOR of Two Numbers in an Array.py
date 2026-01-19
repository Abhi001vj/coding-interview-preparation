"""
421. Maximum XOR of Two Numbers in an Array (Medium)
Pattern: Trie (Bit Manipulation)

--------------------------------------------------------------------------------
PROBLEM UNDERSTANDING
--------------------------------------------------------------------------------
Find max(nums[i] ^ nums[j]).
Constraints: nums length 2*10^5. O(N^2) is too slow.
We need O(N) or O(N log K) where K is number of bits (32).

--------------------------------------------------------------------------------
INTUITION: The "Opposite Bit" Strategy
--------------------------------------------------------------------------------
To maximize XOR, we want bits to differ (0^1 = 1).
For a number X, starting from the most significant bit (MSB), we want to find
another number Y that has the OPPOSITE bit at that position.

Example: X = 10110...
We want Y  = 01001...
Result     = 11111... (Maximized)

We use a Trie to store the binary representations. 
For each number, we greedily traverse the Trie looking for the opposite path.

--------------------------------------------------------------------------------
VISUALIZATION: TRIE TRAVERSAL
--------------------------------------------------------------------------------
Number: 25 (11001)
Root
 |
 0  1 (Have 1? Want 0. Go 0 if exists -> +1 to XOR result bit)
    |
    ...
    
If we want '1' and '0' branch exists, we take it and current XOR bit becomes 1.
If '0' branch doesn't exist, we are forced to take '1', current XOR bit becomes 0.

--------------------------------------------------------------------------------
ALGORITHM
--------------------------------------------------------------------------------
1. Insert all numbers into a Binary Trie.
2. For each number, traverse the Trie:
   - For bit 'b', check if child '1-b' exists.
   - If yes, go there, add (1 << bit) to current_xor.
   - If no, go to 'b', add 0.
3. Track global maximum.

Complexity: O(N * 32) -> O(N).
--------------------------------------------------------------------------------
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        
        # 1. Build Trie
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        # 2. Query Max XOR
        max_xor = 0
        for num in nums:
            node = root
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                wanted = 1 - bit
                
                if wanted in node.children:
                    curr_xor |= (1 << i)
                    node = node.children[wanted]
                else:
                    node = node.children[bit]
            max_xor = max(max_xor, curr_xor)
            
        return max_xor

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaximumXOR([3, 10, 5, 25, 2, 8])) # Expected: 28 (5 ^ 25)

