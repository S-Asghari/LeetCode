from collections import defaultdict, deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacency = defaultdict(list)
        for src in range(n):
            if src != headID:
                adjacency[manager[src]].append(src)
        
        ans = 0
        q = deque()
        q.append([headID, 0])

        while q:
            manager, t = q.popleft()
            ans = max(ans, t)
            for employee in adjacency[manager]:
                q.append([employee, t + informTime[manager]])

        return ans