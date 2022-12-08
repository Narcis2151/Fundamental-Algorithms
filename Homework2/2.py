from math import inf
from math import sqrt

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
vizitat[0] = True
while nr < m:
    min = float(inf)
    x = 0
    y = 0
    for i in range(m+1):
        if vizitat[i]:
            for j in range(m+1):
                if (not vizitat[j]) and graf[i][j]:
                    if min > graf[i][j]:
                        min = graf[i][j]
                        x = i
                        y = j
    suma += graf[x][y]
    vizitat[y] = True
    nr+=1
fout.write(str(round(suma,7)))
fin.close()
fout.close()