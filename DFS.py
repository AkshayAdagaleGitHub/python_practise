from inspect import stack


class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[] for i in range(self.V)]
        self.visited = [False for i in range(self.V)]

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,start):
        self.visited[start] = True
        print(start, end= ' ')

        for adj in self.graph[start]:
            if not self.visited[adj]:
                self.dfs(adj)

    def dfsIterative(self, start):
        stack = [start]
        visited = [False for i in range(self.V)]
        result = []

        while stack:
            u = stack.pop()
            print(u, end= ' ')
            if not self.visited[u]:
               result.append(u)
               visited[u] = True

            for adj in self.graph[u]:
                if not self.visited[adj]:
                    stack.append(adj)

graph = Graph(13)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(1,5)
graph.addEdge(2,4)
graph.addEdge(2,10)
graph.addEdge(2,7)
graph.addEdge(3,6)
graph.addEdge(4,7)
graph.addEdge(5,2)
graph.addEdge(5,8)
graph.addEdge(6,9)
graph.addEdge(8,11)
graph.addEdge(11,12)

# graph.dfs(1)
graph.dfsIterative(1)
