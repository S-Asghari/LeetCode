class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # # -------------------
        # # NeetCode's solution
        # # -------------------
        # tickets.sort()

        # V = set()
        # for dep, arr in tickets:
        #     V.add(dep)
        #     V.add(arr)
        
        # Graph = {v: [] for v in V} 
        # for dep, arr in tickets:
        #     Graph[dep].append(arr)

        # res = ["JFK"]

        # def DFS(dep):
        #     if len(res) == len(tickets) + 1:
        #         return True
            
        #     for i, arr in enumerate(list(Graph[dep])):
        #         res.append(arr)
        #         Graph[dep].pop(i)
        #         if DFS(arr):
        #             return True
        #         res.pop()
        #         Graph[dep].insert(i, arr)
        #     return False

        # DFS("JFK")
        # return res

        tickets.sort()

        V = set()
        for dep, arr in tickets:
            V.add(dep)
            V.add(arr)
        
        Graph = {v: [] for v in V} 
        for dep, arr in tickets:
            Graph[dep].append(arr)

        res = []

        def DFS(dep):
            if not Graph[dep]:
                res.append(dep)
                return

            while Graph[dep]:
                DFS(Graph[dep].pop(0))
            res.append(dep)

        DFS("JFK")
        return res[::-1]