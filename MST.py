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

f = open("MST.in", "r")
line = f.readline()
v = line.split()
n = int(v[0])
m = int(v[1])

def citire_graf(n, m):
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

g = citire_graf(n, m)
f.close()


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
#print(g.list)
#print(g.Kruskal())
#print(g.graph)
#Prim_F(g)
