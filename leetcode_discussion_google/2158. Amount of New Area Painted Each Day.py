# 2158. Amount of New Area Painted Each Day
# Solved
# Hard
# Topics
# Companies
# Hint
# There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

# Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

# Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.

 

# Example 1:


# Input: paint = [[1,4],[4,7],[5,8]]
# Output: [3,3,1]
# Explanation:
# On day 0, paint everything between 1 and 4.
# The amount of new area painted on day 0 is 4 - 1 = 3.
# On day 1, paint everything between 4 and 7.
# The amount of new area painted on day 1 is 7 - 4 = 3.
# On day 2, paint everything between 7 and 8.
# Everything between 5 and 7 was already painted on day 1.
# The amount of new area painted on day 2 is 8 - 7 = 1. 
# Example 2:


# Input: paint = [[1,4],[5,8],[4,7]]
# Output: [3,3,1]
# Explanation:
# On day 0, paint everything between 1 and 4.
# The amount of new area painted on day 0 is 4 - 1 = 3.
# On day 1, paint everything between 5 and 8.
# The amount of new area painted on day 1 is 8 - 5 = 3.
# On day 2, paint everything between 4 and 5.
# Everything between 5 and 7 was already painted on day 1.
# The amount of new area painted on day 2 is 5 - 4 = 1. 
# Example 3:


# Input: paint = [[1,5],[2,4]]
# Output: [4,0]
# Explanation:
# On day 0, paint everything between 1 and 5.
# The amount of new area painted on day 0 is 5 - 1 = 4.
# On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.
# The amount of new area painted on day 1 is 0.
 

# Constraints:

# 1 <= paint.length <= 105
# paint[i].length == 2
# 0 <= starti < endi <= 5 * 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 30.9K
# Submissions
# 55.9K
# Acceptance Rate
# 55.4%
# Topics
# Companies
# 0 - 6 months
# Google
# 2
# 6 months ago
# TikTok
# 3
# Uber
# 3
# Hint 1
# What’s a good way to keep track of intervals that you have already painted?
# Hint 2
# Create an array of all 1’s, and when you have painted an interval, set the values in that interval to 0.
# Hint 3
# Using this array, how can you quickly calculate the amount of new area that you paint on a given day?
# Hint 4
# Calculate the sum of the new array in the interval that you paint.

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        res = []
        painted = {}

        for start, end in paint:
            work = 0
            while start< end:
                if start in painted:
                    prev_end = painted[start]
                    painted[start] = max(painted[start],end)       
                    start = prev_end
                else:
                    painted[start] = end
                    work+=1
                    start+=1
            res.append(work)
        
        return res
    

    # O(N^2)
    # Space O(N^2)