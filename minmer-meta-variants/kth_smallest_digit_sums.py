
import heapq 
# Kth Smallest Digit Sums

def get_digit_sum(num):
    digit_sum  = 0
    while num!=0:
        digit_sum += num% 10
        num //= 10
    return digit_sum

def solution(nums: int, k: int):
    max_heap = []
    for i,num in enumerate(nums):
        digit_sum = get_digit_sum(num)
        print(f"num: {num} digit sum: {digit_sum} ")
        if max_heap and (len(max_heap) >=k or -max_heap[0][0] > digit_sum):
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-digit_sum, -i, num))
        else:
            heapq.heappush(max_heap, (-digit_sum, -i, num))
    
    result = []
    print(f"heap: {max_heap}")
    while max_heap:
        result.append(heapq.heappop(max_heap)[2])
    result.reverse()
    return result

test_cases = [[[3,44,55,111111,10,101,], 2]]
for nums, k in test_cases:
    print(solution(nums, k))