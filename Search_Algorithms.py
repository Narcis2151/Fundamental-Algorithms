from collections import defaultdict
from collections import deque
from sys import setrecursionlimit
from numpy import Inf

setrecursionlimit(10000)
class Graph_Neorientat:
    def __init__(self, n):
        self.n = n
        self.graph = {i:[] for i in range(1,n+1)}

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def BFS(self):
        traversal = []
        visited = [False] * (self.n+1)
        for i in self.graph.keys():
            if visited[i] == False:
                queue = deque()
                visited[i] = True 
                queue.append(i)

                while len(queue) > 0:
                    x = queue.popleft()
                    traversal.append(x)

                    for neibourgh in self.graph[x]:
                        if visited[neibourgh] == False:
                            visited[neibourgh] = True
                            queue.append(neibourgh)
        return traversal
    #Folosim BFS daca vrem sa determinam lantul/drumul minim intre 2 noduri
    #Lantul minim il aflam din vectorul de tati dupa ce apelam BFS din nodul de start
    #Dupa o parcurgere BFS din start -> daca nodul de sfarsit este vizitat -> afisam lantul, altfel nu exista lant
    #Parcurgerea BFS(u) se poate opri cand l-am marcat pe v ca fiind vizitat
    def BFS_1(self, i):
        traversal = []
        d = [Inf] * (self.n+1)
        tata = [0] * (self.n+1)
        visited = [False] * (self.n+1)
        queue = deque()
        visited[i] = True 
        d[i] = 0
        queue.append(i)

        while len(queue) > 0:
            x = queue.popleft()
            traversal.append(x)

            for neibourgh in self.graph[x]:
                if visited[neibourgh] == False:
                    visited[neibourgh] = True
                    queue.append(neibourgh)
                    tata[neibourgh] = x
                    d[neibourgh] = d[x] + 1
        return traversal, tata[1:], d[1:]

    def DFSUtil(self, i, visited, traversal, desc, tata, fin, d, timp):
        visited[i] = 0
        timp += 1
        traversal.append(i)
        desc[i] = timp

        for neighbour in self.graph[i]:
            if visited[neighbour] == -1:
                tata[neighbour] = i
                d[neighbour] = d[i] + 1
                timp = self.DFSUtil(neighbour, visited, traversal, desc, tata, fin, d, timp=timp)
        visited[i] = 1
        timp += 1
        fin[i] = timp
        return timp 
    #Folosim DFS daca vrem sa determinam cilcuri / circuite 
    
    def DFS(self):
        traversal = []
        visited=[-1] * (self.n+1)
        timp = 0
        desc = [0] * (self.n+1)
        fin = [0] * (self.n+1)
        tata = [0] * (self.n+1)
        d = [0] * (self.n+1)
        for i in self.graph.keys():
            if visited[i] == -1:
                timp = self.DFSUtil(i, visited, traversal, desc, tata, fin, d, timp=timp)
        return traversal, desc[1:], fin[1:], tata[1:], d[1:]

    def CycleDetectUtil(self, i, visited, tata, cicluri):
        visited[i] = 1

        for neighbour in self.graph[i]:
            if visited[neighbour] == 0:
                tata[neighbour] = i
                self.CycleDetectUtil(neighbour, visited, tata, cicluri)
            else:
                if tata[i] != neighbour: #daca nu e muchie din arbore => e muchie de intoarcere
                    v = i
                    ciclu = []
                    while v != neighbour:
                        ciclu.append(v)
                        v = tata[v]
                    ciclu.append(neighbour)
                    ciclu.append(i)
                    cicluri.append(ciclu)
                    break


    def CycleDetect(self):
        visited=[0] * (self.n+1)
        tata = [0] * (self.n+1)
        cicluri = []
        for i in self.graph.keys():
            if visited[i] == 0:
                self.CycleDetectUtil(i, visited, tata, cicluri)
        return cicluri

class Graph_Orientat:
    def __init__(self, n):
        self.n = n
        self.graph = {i:[] for i in range(1,n+1)}

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self):
        #print(self.graph)
        traversal = []
        visited = [False] * (self.n+1)
        for i in self.graph.keys():
            if visited[i] == False:
                queue = deque()
                visited[i] = True 
                queue.append(i)

                while len(queue) > 0:
                    x = queue.popleft()
                    traversal.append(x)

                    for neibourgh in self.graph[x]:
                        if visited[neibourgh] == False:
                            visited[neibourgh] = True
                            queue.append(neibourgh)
        return traversal[1:]
    #Folosim BFS daca vrem sa determinam lantul/drumul minim intre 2 noduri
    #Lantul minim il aflam din vectorul de tati dupa ce apelam BFS din nodul de start
    #Dupa o parcurgere BFS din start -> daca nodul de sfarsit este vizitat -> afisam lantul, altfel nu exista lant
    #Parcurgerea BFS(u) se poate opri cand l-am marcat pe v ca fiind vizitat
    def BFS_1(self, i):
        traversal = []
        d = [Inf] * (self.n+1)
        tata = [0] * (self.n+1)
        visited = [False] * (self.n+1)
        queue = deque()
        visited[i] = True 
        d[i] = 0
        queue.append(i)

        while len(queue) > 0:
            x = queue.popleft()
            traversal.append(x)

            for neibourgh in self.graph[x]:
                if visited[neibourgh] == False:
                    visited[neibourgh] = True
                    queue.append(neibourgh)
                    tata[neibourgh] = x
                    d[neibourgh] = d[x] + 1
        return traversal[1:], tata[1:], d[1:]
    
    def DFSUtil(self, i, visited, traversal, desc, tata, fin, d, timp):
        visited[i] = 0
        timp += 1
        traversal.append(i)
        desc[i] = timp

        for neighbour in self.graph[i]:
            if visited[neighbour] == -1:
                tata[neighbour] = i
                d[neighbour] = d[i] + 1
                timp = self.DFSUtil(neighbour, visited, traversal, desc, tata, fin, d, timp=timp)
        visited[i] = 1
        timp += 1
        fin[i] = timp
        return timp
    #Folosim DFS daca vrem sa determinam cilcuri / circuite 
    def DFS(self):
        traversal = []
        visited=[-1] * (self.n+1)
        timp = 0
        desc = [0] * (self.n+1)
        fin = [0] * (self.n+1)
        tata = [0] * (self.n+1)
        d = [0] * (self.n+1)
        for i in self.graph.keys():
            if visited[i] == -1:
                timp = self.DFSUtil(i, visited, traversal, desc, tata, fin, d, timp=timp)
        return traversal, desc[1:], fin[1:], tata[1:], d[1:]

    def CycleDetectUtil(self, i, visited, tata, fin, circuite):
        visited[i] = 1

        for neighbour in self.graph[i]:
            if visited[neighbour] == 0:
                tata[neighbour] = i
                self.CycleDetectUtil(neighbour, visited, tata, fin, circuite)
            else:
                if fin[neighbour] == 0:
                    v = i
                    circuit = []
                    while v != neighbour:
                        circuit.append(v)
                        v = tata[v]
                    circuit.append(neighbour)
                    circuit.append(i)
                    circuit.reverse()
                    circuite.append(circuit)
                    break

        fin[i] = 1

    def CycleDetect(self):
        visited=[0] * (self.n+1)
        fin = [0] * (self.n+1)
        tata = [0] * (self.n+1)
        circuite = []
        for i in self.graph.keys():
            if visited[i] == 0:
                self.CycleDetectUtil(i, visited, tata, fin, circuite)
        return circuite

    def CTCUtil(self, i, visited, s):
            visited[i] = 1

            for neighbour in self.graph[i]:
                if visited[neighbour] == 0:
                    self.CTCUtil(neighbour, visited, s)
            s.append(i)

    def CTCUtil2(self, gt, i, visited, comp):
        visited[i] = 1
        comp.append(i)

        for neighbour in gt[i]:
            if visited[neighbour] == 0:
                self.CTCUtil2(gt, neighbour, visited, comp)

    def CTC(self):
        componente = []
        visited=[0] * (self.n+1)
        s = []
        for i in self.graph.keys():
            if visited[i] == 0:
                self.CTCUtil(i, visited, s)

        gt = {i : [] for i in range(1,self.n+1)}
        for i in self.graph.keys():
            for j in self.graph[i]:
                gt[j].append(i)
        
        visited=[0] * (self.n+1)
        while len(s) > 0:
            x = s.pop()
            if visited[x] == 0:
                comp=[]
                self.CTCUtil2(gt, x, visited, comp)
                comp.reverse()
                componente.append(comp)
        return componente

    def SortTopUtil(self, i, visited, s, fin, tata, cicl):
        visited[i] = 1
        for neighbour in self.graph[i]:
            if visited[neighbour] == 0:
                tata[neighbour] = i
                self.SortTopUtil(neighbour, visited, s, fin, tata, cicl)
            else:
                if fin[neighbour] == 0:
                    cicl.append(True)
                    break
        fin[i] = 1
        s.append(i)

    def SortTop(self):
        visited = [0] * (self.n+1)
        s = []
        fin = [0] * (self.n+1)
        tata = [0] * (self.n+1)
        cicl = []
        for i in self.graph.keys():
            if visited[i] == 0:
                self.SortTopUtil(i, visited, s, fin, tata, cicl)
        if cicl!=[]:
            print("Graful are cicluri, sortare topologica imposibila")
        else:
            while len(s) > 0:
                print(s.pop())
        

g = Graph_Neorientat(11)
g.addEdge(1, 3)
g.addEdge(1, 9)
g.addEdge(1, 5)
g.addEdge(3, 2)
g.addEdge(3, 6)
g.addEdge(2, 5)
g.addEdge(9, 6)
g.addEdge(9, 7)
g.addEdge(9, 8)
g.addEdge(7, 4)
g.addEdge(4, 9)
g.addEdge(4, 8)
g.addEdge(11, 8)
g.addEdge(10, 11)
#print(g.graph)
#print(g.BFS())
#print(g.BFS_1(2))
#print(g.DFS())
#print(g.CycleDetect())

g2=Graph_Orientat(5)
g2.addEdge(1, 3)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
g2.addEdge(3, 4)
g2.addEdge(4, 5)
g2.addEdge(3, 5)
g2.SortTop()

