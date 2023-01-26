from collections import deque
fin = open("maxflow.in")
l1 = fin.readline().split()
n = int(l1[0])
m = int(l1[1])
graf = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    l = fin.readline().split()
    graf[int(l[0])-1][int(l[1])-1] = int(l[2])
fin.close()
graf_r = [[0] * n for i in range(n)]

tata = [0 for i in range(n+1)]

from collections import deque
def bfs():
    global graf, graf_r
    #extragere drum
    coada = deque([0])
    dr = {0: []}
    if 0 == n-1:
        return dr[0]
    while len(coada):
        u = coada.popleft()
        for v in range(len(graf)):
            if (graf[u][v] - graf_r[u][v] > 0) and (v not in dr):
                dr[v] = dr[u] + [(u, v)]
                if v == n-1:
                    return dr[v]
                coada.append(v)
    return None

def max_flow():
    global graf, start, graf_r,n
    drum = bfs()
    while drum != None:
        flow = min(graf[u][v] - graf_r[u][v] for u, v in drum)
        for u, v in drum:
            graf_r[u][v] += flow #arc direct
            graf_r[v][u] -= flow #arc invers
        drum = bfs()
    S=0 #suma fluxuri
    for i in range(n):
        S+=graf_r[0][i]
    return S

fout=open("maxflow.out", "w")
fout.write(str(max_flow()))
#print(graf_r)
fout.close()