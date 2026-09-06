from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # NeetCode's Solution
        res = []
        q = deque() # monotonically decreasing queue

        for r in range(len(nums)):
            if r >= k and nums[r-k] == q[0]:
                q.popleft()
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            if r >= k-1:
                res.append(q[0])

        return res