import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for s in stones:
            heapq.heappush_max(max_heap, s)
        
        while len(max_heap) > 1:
            y = heapq.heappop_max(max_heap)
            x = heapq.heappop_max(max_heap)
            if x != y:
                heapq.heappush_max(max_heap, y - x)

        if not max_heap:
            return 0
        else:
            return heapq.heappop_max(max_heap)