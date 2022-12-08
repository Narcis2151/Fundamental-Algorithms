"""
Program pentru determinarea componentelor tare conexe dintr-un graf orientat
Bazat pe algoritmul lui Kosaraju
Complexitate O(V+E)
"""
import sys
sys.setrecursionlimit(1000000)
f=open('ctc.in', 'r')
f2=open('ctc.out', 'w')
n,m=f.readline().split()

#print(n,m)
n=int(n)
m=int(m)
graf=[[] for i in range(n)]
graf2=[[] for i in range(n)]
nr = 0 
#Memorarea grafului sub forma de lista de adiacenta + creearea transpusei
for i in range(m):
    u,v = [int(x) for x in f.readline().split()]
    graf[u-1].append(v)
    graf2[v-1].append(u)
#print(graf)
#print(graf2)
st=[]
viz=[0]*n
comp=[[] for i in range (n)]

#Prima parcurgere DFS
def DFS1(i):
    viz[i]=1
    for x in range(len(graf[i])):
        if viz[graf[i][x]-1]==0:
            DFS1(graf[i][x]-1)
    st.append(i+1)


for i in range(n):
    if viz[i]==0:
        DFS1(i)

#Al doilea DFS
def DFS2(i,nr):
    viz[i]=1
    comp[nr].append(i+1)
    for x in range(len(graf2[i])):
        if viz[graf2[i][x]-1]==0:
            DFS2(graf2[i][x]-1,nr)
#print(st)

viz=[0]*n
while st!=[]:
    x = st.pop()
    if viz[x-1]==0:
        DFS2(x,nr)
        nr+=1
#print(comp)
comp=comp[:nr]

f2.write(str(nr))
f2.write('\n')
for i in comp:
    for j in i:
        f2.write(str(j)+" ")
    f2.write("\n")
#f2.write(str(comp))
f.close()
f2.close()
