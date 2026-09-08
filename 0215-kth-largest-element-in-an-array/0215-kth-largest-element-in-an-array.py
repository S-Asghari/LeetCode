import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    # ----------
    # Solution 1
    # ----------
    #     max_heap = []
    #     for num in nums:
    #         heapq.heappush_max(max_heap, num)
    #     for i in range(k-1):
    #         heapq.heappop_max(max_heap)
    #     return heapq.heappop_max(max_heap)
    # ----------
    # Solution 2
    # ----------
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                # heapq.heappop(heap)
                # heapq.heappush(heap, nums[i])
                heapq.heappushpop(heap, nums[i])
        return heapq.heappop(heap)
