from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Happy Coding's solution
        graph = defaultdict(set)
        for bus, route in enumerate(routes):
            for station in route:
                graph[station].add(bus)
        
        visitedStations = set()
        visitedBuses = set()
        q = deque([source])
        visitedStations.add(source)
        answer = 0
        
        while q:
            for _ in range(len(q)):
                station = q.popleft()

                if station == target:
                    return answer

                for bus in graph[station]:
                    if bus not in visitedBuses:
                        for nextStation in routes[bus]:
                            if nextStation not in visitedStations:
                                q.append(nextStation)
                                visitedStations.add(nextStation)
                        visitedBuses.add(bus)
            
            answer += 1
        
        return -1
