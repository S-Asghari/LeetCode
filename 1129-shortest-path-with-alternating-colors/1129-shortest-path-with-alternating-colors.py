from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # NeetCode's solution!
        
        redAdj = defaultdict(list)
        blueAdj = defaultdict(list)

        for src, des in redEdges:
            redAdj[src].append(des)
        
        for src, des in blueEdges:
            blueAdj[src].append(des)
        
        ans = [-1 for node in range(n)]
        q = deque()
        q.append([0, 0, None]) # [des, length, edgeColor]
        visited = set()
        visited.add((0, None)) # (des, edgeColor)

        while q:
            node, length, edgeColor = q.popleft()
            
            if ans[node] == -1:
                ans[node] = length
            
            if edgeColor != "RED":
                for nei in redAdj[node]:
                    if (nei, "RED") not in visited:
                        q.append([nei, length+1, "RED"])
                        visited.add((nei, "RED"))
            
            if edgeColor != "BLUE":
                for nei in blueAdj[node]:
                    if (nei, "BLUE") not in visited:
                        q.append([nei, length+1, "BLUE"])
                        visited.add((nei, "BLUE"))

        return ans