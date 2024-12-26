# https://leetcode.com/problems/logger-rate-limiter/description/
# 359. Logger Rate Limiter
# Easy
# Topics
# Companies
# Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

# All messages will come in chronological order. Several messages may arrive at the same timestamp.

# Implement the Logger class:

# Logger() Initializes the logger object.
# bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.
 

# Example 1:

# Input
# ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
# [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
# Output
# [null, true, true, false, false, false, true]

# Explanation
# Logger logger = new Logger();
# logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
# logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
# logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
# logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
# logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
# logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
 

# Constraints:

# 0 <= timestamp <= 109
# Every timestamp will be passed in non-decreasing order (chronological order).
# 1 <= message.length <= 30
# At most 104 calls will be made to shouldPrintMessage.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 345.1K
# Submissions
# 452.6K
# Acceptance Rate
# 76.2%
# Topics
# Companies
# Similar Questions
# Discussion (8)

class Logger:
    """
    Logger Rate Limiter Implementation
    
    Visual Example of Internal State:
    -------------------------------
    message_timestamps = {
        "foo": 1,   # Next allowed timestamp: 11
        "bar": 2    # Next allowed timestamp: 12
    }
    
    Timeline Visualization:
    ---------------------
    timestamp: 1  2  3  4  5  6  7  8  9  10 11
    foo:        P  -  x  -  -  -  -  -  -  x  P
    bar:        -  P  -  -  -  -  -  x  -  -  -
    
    P = Printed
    x = Attempted but rejected
    - = No attempt
    
    Design Choices:
    --------------
    1. Use dictionary to store message -> timestamp mapping
    2. Timestamps represent the last time message was printed
    3. Simple O(1) lookup and update operations
    
    Space Complexity: O(M) where M is number of unique messages
    Time Complexity: O(1) for each operation
    """

    def __init__(self):
        """
        Initialize the logger with an empty dictionary to store message timestamps.
        
        Dictionary Structure:
        message (str) -> timestamp (int) mapping
        """
        self.message_timestamps = {}
        self.RATE_LIMIT = 10  # seconds

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Determines if a message should be printed at given timestamp.
        
        Args:
            timestamp: Current timestamp (guaranteed to be in chronological order)
            message: Message to be potentially printed
            
        Returns:
            bool: True if message should be printed, False otherwise
            
        Example State Changes:
        ------------------
        Initial state: {"foo": 1}
        
        Call: shouldPrintMessage(3, "foo")
        Check: 3 < (1 + 10)
        Result: False
        New state: {"foo": 1}  # Unchanged
        
        Call: shouldPrintMessage(11, "foo")
        Check: 11 >= (1 + 10)
        Result: True
        New state: {"foo": 11}  # Updated
        """
        # If message not seen before or rate limit period has passed
        if (message not in self.message_timestamps or 
            timestamp >= self.message_timestamps[message] + self.RATE_LIMIT):
            
            # Update the last printed timestamp for this message
            self.message_timestamps[message] = timestamp
            return True
            
        return False


"""
Alternative Implementation using Queue (for cleanup):
-------------------------------------------------

from collections import deque

class LoggerWithCleanup:
    def __init__(self):
        self.message_times = {}  # message -> timestamp
        self.msg_queue = deque()  # (timestamp, message) pairs
        self.RATE_LIMIT = 10
        
    def cleanup_old_messages(self, current_time: int):
        # Remove messages older than rate limit window
        while self.msg_queue and current_time - self.msg_queue[0][0] >= self.RATE_LIMIT:
            old_time, old_msg = self.msg_queue.popleft()
            # Only remove if timestamp matches (handles duplicates)
            if self.message_times.get(old_msg) == old_time:
                del self.message_times[old_msg]
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Clean up old messages first
        self.cleanup_old_messages(timestamp)
        
        if message not in self.message_times:
            self.message_times[message] = timestamp
            self.msg_queue.append((timestamp, message))
            return True
            
        last_printed = self.message_times[message]
        if timestamp >= last_printed + self.RATE_LIMIT:
            self.message_times[message] = timestamp
            self.msg_queue.append((timestamp, message))
            return True
            
        return False

Comparison of Implementations:
---------------------------
1. Basic Dictionary Approach:
   + Simple and efficient
   + O(1) operations
   - Keeps growing with unique messages
   - No cleanup of old entries

2. Queue-based Approach:
   + Automatically cleans up old entries
   + Maintains memory efficiency
   - Slightly more complex
   - Additional space for queue
   
Usage Example:
------------
logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))   # True
print(logger.shouldPrintMessage(2, "bar"))   # True
print(logger.shouldPrintMessage(3, "foo"))   # False
print(logger.shouldPrintMessage(8, "bar"))   # False
print(logger.shouldPrintMessage(10, "foo"))  # False
print(logger.shouldPrintMessage(11, "foo"))  # True
"""