"""
Problem: Find Approximate Median in a Stream with Limited Memory

Approaches:
1. Bucketing with Fixed Memory
2. Two Heaps with Trimming
3. Reservoir Sampling
4. Moving Window Average

Visual Example of Bucketing:
Stream: 1.2, 3.4, 2.1, 5.6, 4.3, ...

Buckets (size 1.0):
[1.0-2.0): count=1 (1.2)
[2.0-3.0): count=1 (2.1)
[3.0-4.0): count=1 (3.4)
[4.0-5.0): count=1 (4.3)
[5.0-6.0): count=1 (5.6)
"""

class BucketMedianFinder:
    """
    Approach 1: Bucketing with Fixed Memory
    Time: O(1) for insert, O(b) for median where b is number of buckets
    Space: O(b) where b is number of buckets
    """
    def __init__(self, bucket_size: float, num_buckets: int):
        """
        Initialize with bucket size and number of buckets
        Example: bucket_size=1.0, num_buckets=10
        """
        self.bucket_size = bucket_size
        self.buckets = [0] * num_buckets
        self.total_elements = 0
        self.min_val = float('inf')
        self.max_val = float('-inf')
        
    def _get_bucket(self, num: float) -> int:
        """Get bucket index for a number"""
        return int(num / self.bucket_size)
    
    def add_number(self, num: float) -> None:
        """
        Add number to appropriate bucket
        Example:
        num=3.4, bucket_size=1.0
        bucket_index = 3
        buckets[3] += 1
        """
        bucket = self._get_bucket(num)
        if bucket < len(self.buckets):
            self.buckets[bucket] += 1
            self.total_elements += 1
            self.min_val = min(self.min_val, num)
            self.max_val = max(self.max_val, num)
    
    def find_median(self) -> float:
        """
        Find approximate median
        Returns middle value of the bucket containing median
        
        Example:
        total=5 elements
        median_pos=3
        count up buckets until we reach median_pos
        return middle of that bucket
        """
        if self.total_elements == 0:
            return 0
            
        median_pos = (self.total_elements + 1) // 2
        count = 0
        
        # Find bucket containing median
        for i, bucket_count in enumerate(self.buckets):
            count += bucket_count
            if count >= median_pos:
                # Return middle of bucket
                bucket_start = i * self.bucket_size
                return bucket_start + (self.bucket_size / 2)
                
        return 0

class TrimmedHeapMedianFinder:
    """
    Approach 2: Two Heaps with Trimming
    Time: O(log k) for insert, O(1) for median
    Space: O(k) where k is max heap size
    """
    def __init__(self, max_size: int):
        self.max_heap = []  # Store smaller half
        self.min_heap = []  # Store larger half
        self.max_size = max_size
        
    def add_number(self, num: float) -> None:
        """
        Add number maintaining balance
        If heaps get too large, trim them
        """
        if len(self.max_heap) == 0 or -self.max_heap[0] > num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
            
        # Balance heaps
        while len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        while len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
            
        # Trim heaps if too large
        while len(self.max_heap) + len(self.min_heap) > self.max_size:
            if len(self.max_heap) > len(self.min_heap):
                heappop(self.max_heap)
            else:
                heappop(self.min_heap)
    
    def find_median(self) -> float:
        """Get approximate median from heap tops"""
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.min_heap) > 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return 0

def test_median_finders():
    """
    Test both approaches with a stream of numbers
    """
    # Test Bucketing
    bucket_finder = BucketMedianFinder(1.0, 10)
    stream = [1.2, 3.4, 2.1, 5.6, 4.3]
    for num in stream:
        bucket_finder.add_number(num)
        print(f"After {num}, median ≈ {bucket_finder.find_median()}")
        
    # Test Trimmed Heaps
    heap_finder = TrimmedHeapMedianFinder(5)
    for num in stream:
        heap_finder.add_number(num)
        print(f"After {num}, median ≈ {heap_finder.find_median()}")

"""
Trade-offs:

1. Bucketing:
   Pros:
   - Fixed memory usage
   - Simple implementation
   - Good for large ranges
   Cons:
   - Approximate results
   - Need to choose bucket size
   
2. Trimmed Heaps:
   Pros:
   - More accurate
   - Handles outliers well
   Cons:
   - More complex
   - Might lose important values when trimming

3. Reservoir Sampling:
   Pros:
   - Fixed memory
   - Unbiased sampling
   Cons:
   - Very approximate
   - Might miss important values

Edge Cases:
1. Empty stream
2. Single value
3. All same values
4. Extreme outliers
5. Very sparse distribution
"""