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
    #     heap = nums[:k]
    #     heapq.heapify(heap)
    #     for i in range(k, len(nums)):
    #         if nums[i] > heap[0]:
    #             # heapq.heappop(heap)
    #             # heapq.heappush(heap, nums[i])
    #             heapq.heappushpop(heap, nums[i])
    #     return heapq.heappop(heap)
    # ----------
    # Solution 3
    # ----------
        def partition(p, l, r):
            i = l
            lt = l   # nums[l:lt] < p
            gt = r   # nums[gt+1:r+1] > p
            while i <= gt:
                if nums[i] < p:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > p:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            return lt, gt # nums[l:lt] < p == nums[lt:gt+1] < nums[gt+1:r+1]

        l, r = 0, len(nums) - 1
        while True:
            p = nums[l]
            lt, gt = partition(p, l, r)
            count_greater = r - gt
            count_equal = gt - lt + 1

            if k <= count_greater:
                l = gt + 1 # kth largest is in the ">p" zone
            elif k <= count_greater + count_equal:
                return p # kth largest falls in the "==p" zone
            else:
                k -= count_greater + count_equal
                r = lt - 1  # kth largest is in the "<p" zone