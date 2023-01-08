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
graf_r = graf
print(graf)
tata = [0 for i in range(n+1)]

def BFS():
    global graf, graf_r, n, m, tata
    viz = [0 for i in range(n+1)]
    q = deque()
    q.append(1)
    viz[1] = 1
    while len(q) != 0:
        i = q.popleft()
        for ind, val in enumerate(graf[i-1]):
             if viz[ind+1] == 0 and val > 0:
                q.append(ind+1)
                viz[ind+1] = 1
                tata[ind+1] = i
    return True if viz[n] else False

def max_flow():
    global graf, graf_r, n, m, tata
    max_flow = 0
    while BFS():
        flow = float("Inf")
        x = n
        while x != 1:
            flow = min(flow, graf[tata[x]-1][x-1])
            x = tata[x]

        max_flow += flow

        v = n
        while v != 1:
            u = tata[v]
            graf[u-1][v-1] -= flow 
            graf[v-1][u-1] += flow 
            v = tata[v]

    return max_flow

fout=open("maxflow.out", "w")
fout.write(str(max_flow()))
fout.close()