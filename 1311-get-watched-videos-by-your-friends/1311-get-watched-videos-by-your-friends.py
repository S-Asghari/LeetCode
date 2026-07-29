from collections import deque

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = deque()
        visited = set()
        q.append((id, 0))
        visited.add(id)
        desiredFriends = set()

        while q:
            p, l = q.popleft()
            if l > level:
                break
            if l == level:
                desiredFriends.add(p)
            else:
                for f in friends[p]:
                    if f not in visited:
                        q.append((f, l+1))
                        visited.add(f)
        
        desiredVideos = {}
        for f in desiredFriends:
            for v in watchedVideos[f]:
                if v not in desiredVideos:
                    desiredVideos[v] = 1
                else:
                    desiredVideos[v] += 1

        answer = [(v, desiredVideos[v]) for v in desiredVideos]
        answer = sorted(answer, key = lambda x: (x[1], x[0]))
        return [v for v, freq in answer]