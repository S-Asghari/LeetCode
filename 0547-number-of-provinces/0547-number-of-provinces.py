class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = set()
        
        def recurse(city):
            for city2, connected in enumerate(isConnected[city]):
                if connected == 1:
                    if not city2 in visited:
                        visited.add(city2)
                        recurse(city2)

        
        for city in range(n):
            if city not in visited:
                provinces += 1
                visited.add(city)
                recurse(city)

        return provinces