"""
Implementarea problemei Check DFS
Plecand de la problema DFS, am sortat lista de adiacenta a fiecarui nod
In functie de ordinea in care apareau nodurile adiacente cu el in permutarea data
Complexitate ca DFS (O(V+E))
"""
import sys
sys.setrecursionlimit(100000)

l=input().split()
n=int(l[0])
m=int(l[1])

perm = [int(x) for x in input().split()]

ordine = [0 for i in range(n)]
for i in range(n):
    ordine[perm[i]-1] = i

#Memorarea grafului sub forma de lista de adiacenta pentru eficienta
ls=[[] for i in range(n)]
for i in range(m):
    u,v = [int(x) for x in input().split()]
    ls[u-1].append(v)
    ls[v-1].append(u)

#print(perm, ordine,ls)
for i in ls:
    i.sort(key=lambda x : ordine[x-1])
#print(perm, ordine,ls)

viz=[0 for i in range(n+1)]
l2=[]
def DFS(i):
    viz[i]=1
    l2.append(i+1)
    for x in range(len(ls[i])):
        if viz[ls[i][x]-1]==0:
            DFS(ls[i][x]-1)
DFS(0)
#print(l2)
if l2 == perm:
    print(1)
else:
    print(0)
    