from collections import deque

class Retea:
    def __init__(self, n):
        self.n = n

        self.lista_intrare=[[] for i in range(n)]
        self.lista_iesire=[[] for i in range(n)]

        self.flux=[[ 0 for j in range(n) ] for i in range(n)]
        self.cap=[[0 for j in range(n)] for i in range(n)]

        self.vizitat = [0 for i in range(self.n + 1)]
        self.tata = [None for i in range(self.n +1)]

    def addEdge(self, u, v, c):
        self.lista_iesire[u].append(v)
        self.lista_intrare[v].append(u)
        self.cap[u][v]=c

    def Cauta_Lant_Nesaturat_BFS(self):
        self.vizitat = [0 for i in range(self.n + 1)]
        self.tata = [None for i in range(self.n + 1)]
        queue = deque()
        queue.append(0)
        self.vizitat[0] = 1
        while len(queue) > 0:
            i = queue.popleft()

            for j in self.lista_iesire[i]:
                if self.vizitat[j] == 0 and self.cap[i][j] - self.flux[i][j] > 0:
                    queue.append(j)
                    self.vizitat[j] = 1
                    self.tata[j] = i
                    if j == self.n-1:
                        return True
            
            for j in self.lista_intrare[i]:
                if self.vizitat[j] == 0 and self.flux[j][i] > 0:
                    if j == self.n-1:
                        return True
                    queue.append(j)
                    self.vizitat[j] = 1
                    self.tata[j] = -i
                    
        return False

    def FordFulkerson(self):
        index = 1
        while self.Cauta_Lant_Nesaturat_BFS():
            x = self.n-1
            cr = float("inf")
            while x != 0:
                if self.tata[x]>=0:
                    #tata[x],x -capac lui reziduala c[tata[x]][x]-f[tata[x]][x]
                    cr = min(cr, self.cap[self.tata[x]][x] - self.flux[self.tata[x]][x])
                else:
                    #x,-tata[x] capac rezid f[x][-tata[x]]
                    cr = min(cr, self.flux[x][-self.tata[x]])
                x=abs(self.tata[x])
            print(f"Capacitatea reziduala la pasul {index} este : {cr}")
        
            x = self.n - 1  
            while x != 0:
                if self.tata[x] >= 0:
                    self.flux[self.tata[x]][x] += cr
                else:
                    self.flux[x][-self.tata[x]] -= cr
                x=abs(self.tata[x])
            index += 1

        for linie in self.flux:
            print(*linie)

def Citire():
    f = open("flow.in")
    line = f.readline().split()
    n = int(line[0])
    m = int(line[1])

    retea = Retea(n)
    for i in range(m):
        line = f.readline().split()
        nod1=line[0] 
        nod2=line[1] 
        if nod1 == "s":
            nod1=0
        if nod1 == "t":
            nod1 == n-1
        if nod2 == "s":
            nod2=0
        if nod2 == "t":
            nod2=n-1

        nod1=int(nod1)
        nod2=int(nod2)
        c=int(line[2])

        retea.addEdge(nod1, nod2, c)
    return retea
    
g = Citire()
g.FordFulkerson()




