import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush_max(max_heap, num)
        for i in range(k-1):
            heapq.heappop_max(max_heap)
        return heapq.heappop_max(max_heap)