import heapq
from math import inf

class Graph_Neorientat:
    def __init__(self, n):
        self.n = n
        self.list = []
        self.graph = {i:[] for i in range(0, n+1)}
        self.kruskal = []
        self.tata = [0 for i in range(n+2)]
        self.h = [0 for i in range(n+2)]
        self.cost = 0

    def addEdge(self, u, v, c):
        self.list.append((u, v, c))
        self.graph[u].append((v, c))
        self.graph[v].append((u, c))

    def Reprez(self, u):
        if self.tata[u] ==0:
            return u
        self.tata[u] = self.Reprez(self.tata[u])
        return self.tata[u]

    def Reuneste(self, u, v):
        ru = self.Reprez(u)
        rv = self.Reprez(v)

        if self.h[ru] > self.h[rv]:
            self.tata[rv] = ru

        else:
            self.tata[ru] = rv
            if self.h[ru] == self.h[rv]:
                self.h[rv] += 1

    def Kruskal(self):
        ls = sorted(self.list, key = lambda x: x[2])
        self.tata = [0 for i in range(self.n+1)]
        self.h = [0 for i in range(self.n+1)]
        self.cost = 0
        nrms = 0
        for muchie in ls:
            u = muchie[0]
            v = muchie[1]
            if self.Reprez(u) != self.Reprez(v):
                self.kruskal.append(muchie)
                self.Reuneste(u, v)
                self.cost += muchie[2]
                nrms += 1
                if nrms == self.n:
                    break
        return self.kruskal, self.cost

    def Prim(self):
        self.tata = [0 for i in range(self.n+1)]
        d = [float(inf) for i in range(self.n+1)]
        self.cost = 0
        d[0] = 0
        vizitat = [0 for i in range(self.n+1)]
        Q=[]
        heapq.heappush(Q, (d[0], 0))
        while len(Q) > 0:
            u = heapq.heappop(Q)[1]
            vizitat[u] += 1

            if vizitat[u] == 1:
                for (v, cost) in self.graph[u]:
                    if vizitat[v] == 0:
                        if d[v] > cost:
                            self.tata[v] = u
                            d[v] = cost
                            heapq.heappush(Q, (d[v], v))
        return self.tata, d

    def Dijkstra(self):
        self.tata = [0 for i in range(self.n+1)]
        d = [float(inf) for i in range(self.n+1)]
        self.cost = 0
        d[0] = 0
        #vizitat = [0 for i in range(n+1)]
        Q=[]
        heapq.heappush(Q, (d[0], 0))
        while len(Q) > 0:
            u = heapq.heappop(Q)[1]
            #vizitat[u] += 1

            #if vizitat[u] == 1:
            for (v, cost) in self.graph[u]:
                #if vizitat[v] == 0:
                    if d[v] > d[u] + cost:
                        self.tata[v] = u
                        d[v] = d[u] + cost
                        heapq.heappush(Q, (d[v], v))
        return self.tata, d

class Graph_Orientat:
    def __init__(self, n):
        self.n = n
        self.graph = {i:[] for i in range(0,n+1)}

    def addEdge(self, u, v, c):
        self.graph[u].append((v, c))

    def SortTopUtil(self, i, visited, s, fin, tata, cicl):
        visited[i] = 1
        for neighbour in self.graph[i]:
            if visited[neighbour[0]] == 0:
                tata[neighbour[0]] = i
                self.SortTopUtil(neighbour[0], visited, s, fin, tata, cicl)
            else:
                if fin[neighbour[0]] == 0:
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
            return "Graful are cicluri, sortare topologica imposibila"
        else:
            return s[::-1]

    def DAG(self):
        d = [-inf] * (self.n + 1)
        tata = [0] * (self.n + 1)
        d[0] = 0
        sortare = self.SortTop()
        print(sortare)
        for i in sortare:
            for (vecin, cost) in self.graph[i]:
                if d[i] + cost > d[vecin]:
                    d[vecin] = d[i] + cost
                    tata[vecin] = i
        return d, tata

def citeste_neorientat():
    f = open("multi_surse.in")
    line = f.readline().split()
    n = int(line[0])
    m = int(line[1])

    g = Graph_Neorientat(n)
    for i in range(m):
        line = f.readline()
        v = line.split()

        x, y, cost = v
        x = int(x)
        y = int(y)
        cost = int(cost)
        g.addEdge(x, y, cost)
    
    line = f.readline().split()
    for i in line[1:]:
        g.addEdge(0, int(i), 0)
    return g
    f.close()

def citeste_orientat():
    f = open("multi_surse.in")
    line = f.readline().split()
    n = int(line[0])
    m = int(line[1])

    g = Graph_Orientat(n)
    for i in range(m):
        line = f.readline()
        v = line.split()

        x, y, cost = v
        x = int(x)
        y = int(y)
        cost = int(cost)
        g.addEdge(x, y, cost)
    
    line = f.readline().split()
    for i in line[1:]:
        g.addEdge(0, int(i), 0)
    return g
    f.close()

g = citeste_neorientat()
g_o = citeste_orientat()

#print(g_o.graph)
#print(g_o.DAG())
#print(g.Kruskal())
