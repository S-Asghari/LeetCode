import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heappush(min_heap, (nums1[0]+nums2[0], 0, 0))
        visited = set()
        visited.add((0, 0))
        result = []

        while k > 0 and min_heap:
            s, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1
            if i < len(nums1) - 1 and (i+1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))
            if j < len(nums2) - 1 and (i, j+1) not in visited:
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))

        return result
