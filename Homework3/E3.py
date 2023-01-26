from collections import deque
fin = open("harta.in")
n=int(fin.readline())
s=0
t=2*n+1
graf = [[0 for i in range(t+1)] for j in range(t+1)]
graf_r = [[0 for i in range(t+1)] for j in range(t+1)]

for i in range(1, n+1):
    l = fin.readline().split()
    graf[s][i] = int(l[0])
    graf[n+i][t] = int(l[1])
fin.close()
for i in range(1, n+1):
    for j in range(1, n+1):
        if i!=j:
            graf[i][n+j] = 1
#print(graf)


def bfs():
    global graf, graf_r, s, t
    q = deque([s])
    dr = {s: []}
    if t == s:
        return dr[s]
    while len(q) > 0:
        u = q.popleft()
        for v in range(len(graf)):
            if (graf[u][v] - graf_r[u][v] > 0) and (v not in dr):
                dr[v] = dr[u] + [(u, v)]
                if v == t:
                    return dr[v]
                q.append(v)
    return None

def max_flow():
    global graf, graf_r, s, t, n, m, e
    dr = bfs()
    while dr != None:
        flow = min(graf[u][v] - graf_r[u][v] for u, v in dr)
        for u, v in dr:
            graf_r[u][v] += flow 
            graf_r[v][u] -= flow 
        dr = bfs()

    numar=0 
    for i in range(t+1):
        numar += graf_r[s][i]
    arce = []
    #print(graf_r)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graf_r[i][n+j] == 1:
                arce.append((i, j))
    return numar, arce

numar, arce = max_flow()
fout = open("harta.out", "w")
fout.write(str(numar)+"\n")
for arc in arce:
    fout.write(str(arc[0]) + ' ' + str(arc[1]) + '\n')
fout.close()