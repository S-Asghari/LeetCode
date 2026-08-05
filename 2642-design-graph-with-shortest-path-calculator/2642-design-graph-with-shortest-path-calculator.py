class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adjacency = [[float('inf') for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            self.adjacency[i][i] = 0
        for u, v, w in edges:
            self.adjacency[u][v] = w
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.adjacency[i][j] = min(self.adjacency[i][j], self.adjacency[i][k] + self.adjacency[k][j])

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.adjacency[u][v] = min(self.adjacency[u][v], w)
        for i in range(self.n):
            for j in range(self.n):
                self.adjacency[i][j] = min(self.adjacency[i][j], self.adjacency[i][u] + self.adjacency[u][v] + self.adjacency[v][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        if self.adjacency[node1][node2] < float('inf'):
            return self.adjacency[node1][node2]
        else:
            return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)