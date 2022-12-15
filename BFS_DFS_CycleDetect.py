from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = {i:[] for i in range(n)}

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self):
        #print(self.graph)
        traversal = []
        visited = [False] * self.n
        for i in self.graph.keys():
            if visited[i] == False:
                queue = deque()
                visited[i] = True
                queue.append( i)

                while len(queue) > 0:
                    x = queue.popleft()
                    traversal.append(x)

                    for neibourgh in self.graph[x]:
                        if visited[neibourgh] == False:
                            visited[neibourgh] = True
                            queue.append(neibourgh)
        return traversal
    
    def DFSUtil(self, i, visited, traversal):
        visited[i] = True
        traversal.append(i)

        for neighbour in self.graph[i]:
            if visited[neighbour] == False:
                self.DFSUtil(neighbour, visited, traversal)

    def DFS(self):
        #print(self.graph)
        traversal = []
        visited=[False] * len(self.graph)
        for i in self.graph.keys():
            if visited[i] == False:
                self.DFSUtil(i, visited, traversal)
        return traversal

    def CycleDetectUtil(self, i, visited):
        visited[i] = 0

        for neighbour in self.graph[i]:

            if visited[neighbour] == 0:
                return True

            if visited[neighbour] == -1 and self.CycleDetectUtil(neighbour, visited) == True:
                return True
            
        visited[i] = 1
        return False

    def CycleDetect(self):
        visited = [-1] * len(self.graph)
        #print(self.graph)
        for i in self.graph.keys():
            if self.CycleDetectUtil(i, visited) == True:
                return True
        return False
                
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.BFS())
print(g.DFS())
print(g.CycleDetect())