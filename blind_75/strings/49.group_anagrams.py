
# https://leetcode.com/problems/group-anagrams/description/
# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from collections import defaultdict

# Solution 1: Sorting as Key
def groupAnagrams_sort(strs: list[str]) -> list[list[str]]:
    """
    Time: O(n * k*log(k)) where n is number of strings, k is max string length
    Space: O(n*k) for the hashmap
    
    Approach: Use sorted string as key
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Create key by sorting characters
        key = ''.join(sorted(s))
        groups[key].append(s)
        
    return list(groups.values())

# Solution 2: Character Count Array as Key
def groupAnagrams_count(strs: list[str]) -> list[list[str]]:
    """
    Time: O(n * k) where n is number of strings, k is max string length
    Space: O(n*k) for the hashmap
    
    Approach: Use character count tuple as key
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Create count array for lowercase letters
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        # Convert count array to tuple for hashable key
        key = tuple(count)
        groups[key].append(s)
        
    return list(groups.values())

# Solution 3: Prime Product as Key (for discussion)
def groupAnagrams_prime(strs: list[str]) -> list[list[str]]:
    """
    Time: O(n * k) where n is number of strings, k is max string length
    Space: O(n) for the hashmap
    
    Note: This is mainly for discussion - has overflow issues
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    
    groups = defaultdict(list)
    
    for s in strs:
        # Create key by multiplying prime numbers
        key = 1
        for c in s:
            key *= primes[ord(c) - ord('a')]
        groups[key].append(s)
        
    return list(groups.values())

# Visualization helper
def visualize_grouping(strs: list[str]):
    """
    Helper to visualize how strings are grouped
    """
    print("\nGrouping Analysis for:", strs)
    print("=" * 50)
    
    # Show sorting based groups
    sort_groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        sort_groups[key].append(s)
        
    print("\nSorting-based grouping:")
    for key, group in sort_groups.items():
        print(f"Key '{key}' -> {group}")
        print(f"Character frequency: {get_char_freq(key)}")
        
    # Show count based groups
    count_groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        count_groups[key].append(s)
        
    print("\nCount-based grouping:")
    for key, group in count_groups.items():
        freq = {chr(i + ord('a')): v for i, v in enumerate(key) if v > 0}
        print(f"Frequency {freq} -> {group}")

def get_char_freq(s: str) -> dict:
    """Helper to get character frequencies"""
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

# Test function
def test_solutions():
    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
        ["", "b"],
        ["abc", "cba", "bac", "xyz"]
    ]
    
    for test in test_cases:
        print("\nTesting with:", test)
        print("="*50)
        
        # Run all solutions
        results = {
            "Sort": groupAnagrams_sort(test),
            "Count": groupAnagrams_count(test),
            "Prime": groupAnagrams_prime(test)
        }
        
        # Verify all solutions give same grouping
        base = set(tuple(sorted(group)) for group in results["Sort"])
        for method, result in results.items():
            current = set(tuple(sorted(group)) for group in result)
            assert base == current, f"{method} gave different grouping!"
            print(f"{method} result: {result}")
        
        # Show detailed grouping analysis
        visualize_grouping(test)

# Run tests
test_solutions()