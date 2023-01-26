from collections import deque

class Retea:
    def __init__(self, n):
        self.n = n + 1

        self.lista_intrare=[[] for i in range(self.n+1)]
        self.lista_iesire=[[] for i in range(self.n+1)]

        self.flux=[[ 0 for j in range(self.n+1) ] for i in range(self.n+1)]
        self.cap=[[0 for j in range(self.n+1)] for i in range(self.n+1)]

        self.vizitat = [0 for i in range(self.n + 1)]
        self.tata = [-1 for i in range(self.n +1)]

    def addEdge(self, u, v):

        self.lista_iesire[u].append(v)

        self.lista_intrare[v].append(u)
            
        self.cap[u][v]=1

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
                    if j == self.n:
                        return True

            for j in self.lista_intrare[i]:
                if self.vizitat[j] == 0 and self.flux[j][i] > 0:
                    queue.append(j)
                    self.vizitat[j] = 1
                    self.tata[j] = (-1)*i
                    if j == self.n:
                        return True

            
        return False

    def FordFulkerson(self):
        index = 1
        while self.Cauta_Lant_Nesaturat_BFS():
            x = self.n
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
        
            x = self.n
            while x != 0:
                print(self.tata[x])
                if self.tata[x] >= 0:
                    self.flux[self.tata[x]][x] += cr
                else:
                    self.flux[x][-self.tata[x]] -= cr
                x=abs(self.tata[x])
            index += 1

        for linie in self.flux:
            print(*linie)

def Citire():
    f = open("cuplaj2.in")
    line = f.readline().split()
    n = int(line[0])
    m = int(line[1])

    retea = Retea(n+m)

    line = f.readline().split()
    for index, value in enumerate(line):
        retea.cap[0][index+1] = int(value)
        retea.lista_iesire[0].append(index+1)
        retea.lista_intrare[index].append(0)

    line = f.readline().split()
    for index, value in enumerate(line):
        retea.cap[n+index+1][retea.n] = int(value)
        retea.lista_iesire[n+index+1].append(retea.n)
        retea.lista_intrare[retea.n].append(n+index+1)
    
    for i in range(n):
        for j in range(m):
            retea.addEdge(i+1, n+j+1)
    return retea
    
g = Citire()
g.FordFulkerson()




