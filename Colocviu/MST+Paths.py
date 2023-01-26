from collections import defaultdict
from collections import deque
import heapq
from sys import setrecursionlimit
from numpy import Inf

setrecursionlimit(10000)

def Levenshtein(a, b):
    if len(b)==0:
        return len(a)
    elif len(a)==0:
        return len(b)
    elif a[0]==b[0]:
        return Levenshtein(a[1:], b[1:])
    else:
        return 1+ min(Levenshtein(a[1:], b),
                      Levenshtein(a, b[1:]),
                      Levenshtein(a[1:], b[1:]))

class Graph_Neorientat:
    def __init__(self, n):
        self.n = n
        self.list = []
        self.graph = {i:[] for i in range(1, n+1)}
        self.kruskal = []
        self.tata = [0 for i in range(n+1)]
        self.h = [0 for i in range(n+1)]
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
        self.tata = [0 for i in range(n+1)]
        self.h = [0 for i in range(n+1)]
        self.kruskal = []
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
                if nrms == n-1:
                    break
        return self.kruskal, self.cost

    def CycleDetectUtil(self, i, visited, fin, tata, cicluri):
        visited[i] = 1
        for neighbour in self.graph[i]:
            if visited[neighbour[0]] == 0:
                tata[neighbour[0]] = i
                self.CycleDetectUtil(neighbour[0], visited, fin, tata, cicluri)
            else:
                if fin[neighbour[0]] == 0 and tata[i] != neighbour[0]: #daca nu e muchie din arbore => e muchie de intoarcere
                    v = i
                    ciclu = []
                    while v != neighbour[0]:
                        ciclu.append(v)
                        v = tata[v]
                    ciclu.append(neighbour[0])
                    ciclu.append(i)
                    cicluri.append(ciclu)
                    break
        fin[i] = 1

    def CycleDetect(self):
        visited=[0] * (self.n+1)
        tata = [0] * (self.n+1)
        fin = [0] * (self.n+1)
        cicluri = []
        for i in self.graph.keys():
            if visited[i] == 0:
                self.CycleDetectUtil(i, visited, fin, tata, cicluri)
        return cicluri

    def Prim(self, s):
        self.tata = [0 for i in range(n+1)]
        d = [float(Inf) for i in range(n+1)]
        self.cost = 0
        d[s] = 0
        vizitat = [0 for i in range(n+1)]
        Q=[]
        heapq.heappush(Q, (d[s], s))
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

    def Dijkstra(self, s):
        self.tata = [0 for i in range(n+1)]
        d = [float(Inf) for i in range(n+1)]
        self.cost = 0
        d[s] = 0
        #vizitat = [0 for i in range(n+1)]
        Q=[]
        heapq.heappush(Q, (d[s], s))
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
        self.graph = {i:[] for i in range(1,n+1)}

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

    def DAG(self, start):
        d = [-Inf] * (self.n + 1)
        tata = [0] * (self.n + 1)
        d[start] = 0
        sortare = self.SortTop()
        #print(sortare)
        for i in sortare:
            for (vecin, cost) in self.graph[i]:
                if d[i] + cost > d[vecin]:
                    d[vecin] = d[i] + cost
                    tata[vecin] = i
        return d[1:], tata[1:]

f = open("MST.in", "r")
line = f.readline()
v = line.split()
n = int(v[0])
m = int(v[1])

def citire_graf_neorientat(n, m):
    g = Graph_Neorientat(n)
    for i in range(m):
        line = f.readline()
        v = line.split()

        x, y, cost = v
        x = int(x)
        y = int(y)
        cost = int(cost)
        g.addEdge(x, y, cost)
    return g

g = citire_graf_neorientat(n, m)
f.close()

f = open("Ponderi_Negative.in", "r")
line = f.readline()
v = line.split()
n1 = int(v[0])
m1 = int(v[1])
def citire_graf_orientat(n1, m1):
    g = Graph_Orientat(n1)
    for i in range(m1):
        line = f.readline()
        v = line.split()

        x, y, cost = v
        x = int(x)
        y = int(y)
        cost = int(cost)
        g.addEdge(x, y, cost)
    return g
g2 = citire_graf_orientat(n1, m1)
f.close()
#print(g2.DAG(1))

def Prim_F(g):
    print("Introduceti nodul de start:")
    start = int(input())
    tata, dist = g.Prim(start)
    final_dist = sum(dist[1:])

    def print_muchii(tata):
        for x in range(1,n+1):
            if tata[x] != 0:
                print(x , tata[x])

    print_muchii(tata)
    print(f"dist : {dist[1:]}")
    print(final_dist)
    print(f"tata : {tata[1:]}")

def Dijkstra_F(g):
    print("Introduceti nodul de start:")
    start = int(input())
    tata, dist = g.Dijkstra(start)
    final_dist = sum(dist[1:])

    def print_muchii(tata):
        for x in range(1,n+1):
            if tata[x] != 0:
                print(x , tata[x])

    print_muchii(tata)
    print(f"dist : {dist[1:]}")
    print(f"tata : {tata[1:]}")
#print(g.list)
#print(g.Kruskal())
#print(g.graph)
#Prim_F(g)
#Dijkstra_F(g)

"""
graf_2 = Graph_Neorientat(n)
#print(g.Kruskal())
for i in g.Kruskal()[0]:
    #print(i)
    graf_2.addEdge(i[0], i[1], i[2])
#print(graf_2.graph)

graf_2.addEdge(3, 5, 14)
ciclu = graf_2.CycleDetect()[0]
print(ciclu)
max = 0

for i in range(len(graf_2.list)):
    if (graf_2.list[i][0] == ciclu[0] and graf_2.list[i][1] == ciclu[1]) or (graf_2.list[i][1] == ciclu[0] and graf_2.list[i][2] == ciclu[1]) or (graf_2.list[i][2] == ciclu[0] and graf_2.list[i][3] == ciclu[1]):
        if graf_2.list[i][2] > max:
            max = graf_2.list[i][2]
            muchie = graf_2.list[i]
print(muchie)
"""