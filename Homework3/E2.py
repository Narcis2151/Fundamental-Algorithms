from collections import deque
fin = open("cuplaj.in")
l1 = fin.readline().split()
n = int(l1[0])
m = int(l1[1])
e = int(l1[2])
s = 0
t = n+m+1
graf = [[0 for i in range(t+1)] for j in range(t+1)]

for i in range(1, n+1):
    graf[s][i] = 1
for i in range(e):
    l = fin.readline().split()
    graf[int(l[0])][int(l[1])+n] = 1
for i in range(n+1, t):
    graf[i][t] = 1
fin.close()
graf_r = [[0 for i in range(t+1)] for j in range(t+1)]

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

    cupl=0 
    for i in range(t+1):
        cupl += graf_r[s][i]
    arce = []
    for i in range(1, n+1):
        if graf_r[i].count(1) == 1:
            x = graf_r[i].index(1)
            arce.append((i, x-n))
    return cupl, arce

cuplaj, arce = max_flow()
fout = open("cuplaj.out", "w")
fout.write(str(cuplaj)+"\n")
for arc in arce:
    fout.write(str(arc[0]) + ' ' + str(arc[1]) + '\n')
fout.close()