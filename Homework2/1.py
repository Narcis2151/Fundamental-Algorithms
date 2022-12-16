from math import inf
from math import sqrt
from sys import maxsize
fin = open("retea2.in", "r")
fout = open("retea2.out", "w")

nm = fin.readline().split()
n, m = int(nm[0]), int(nm[1])

def dist(a,b):
    return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])

centrale = []
blocuri = []
graf = [[0 for i in range(m+1)] for i in range(m+1)]
for i in range(n):
    u,v = (int(x) for x in fin.readline().split())
    centrale.append((u,v))

for i in range(m):
    u,v = (int(x) for x in fin.readline().split())
    blocuri.append((u,v))

for x in range(len(blocuri)-1):
    for y in range(x+1, len(blocuri)):
        graf[x][y] = sqrt(dist(blocuri[x], blocuri[y]))
        graf[y][x] = sqrt(dist(blocuri[x], blocuri[y]))

for x in range(len(blocuri)):
    min=float(inf)
    for y in range(len(centrale)):
        d = sqrt(dist(blocuri[x], centrale[y]))
        if d < min:
            min = d
    #print(min)
    graf[x][m] = min
    graf[m][x] = min

#print(graf)

vizitat = [0 for i in range(m+1)]
nr = 0
suma = float(0)
tata = [None] * (m+1)
d = [float(inf)] * (m+1)
tata[0] = -1
d[0] = 0
#print(graf)
while nr < m+1:
    #print(d)
    min = float(inf)
    for i in range(len(graf)):
        if vizitat[i] == 0 and d[i] < min:
            min = d[i]
            u = i

    vizitat[u] = 1
    nr +=1
    suma += d[u]
    #print(suma)


    for v in range(len(graf[u])):
        if graf[u][v] > 0 and vizitat[v] == 0 and d[v] > graf[u][v]:
            d[v] = graf[u][v]
            tata[v] = u

#print(*graf, sep='\n')
fout.write(str(round(suma,7)))
fin.close()
fout.close()