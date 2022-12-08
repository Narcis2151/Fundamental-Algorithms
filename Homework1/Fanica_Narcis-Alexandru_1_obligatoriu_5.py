"""
Algoritm pentru determinarea distantei de la fiecare nod la cel mai apropiat punct de control
Bazat pe algoritmul de parcurgere BFS in care determinam distanta de fiecare nod
De la nodul din care pornim cautarea
Apoi gasim cel mai apropiat punct de control
"""

from collections import deque
f=open("graf.in")
f2=open("graf.out",'w')

v=f.readline().split()
n=int(v[0])
m=int(v[1])

#Formam lista de adiacenta corespunzatoare grafului
ls=[[] for i in range(n)]
for i in range(m):
    u,v = [int(x) for x in f.readline().split()]
    ls[u-1].append(v)
    ls[v-1].append(u)

#Lista de puncte de control
l=f.readline()
v=l.split()
puncte=[]
for x in v:
    puncte.append(int(x))

#Functia pentru parcurgerea BFS si determinarea distantei
def BFS(i):
    q=deque([])
    q.append(i)
    viz[i]=1
    d[i]=0
    while len(q)>0:
        x=q.popleft()
        #l2.append(x+1)
        for j in ls[x]:
            if viz[j-1]==0:
                q.append(j-1)
                viz[j-1]=1
                tata[j-1]=x
                d[j-1]=d[x]+1

#Pentru fiecare nod parcurgem graful BFS si determinam distanta de la nodul respectiv
#La punctele de control
#Apoi o selectam pe cea mai mica
l_min=[]
for i in range(n):
    viz=[0]*(n)
    tata=[0]*(n)
    d=[None]*(n)
    #l2=[]

    BFS(i)
    #print(l2)
    min=None
    for j in range(n):
        if j+1 in puncte:
            if min==None:
                min=d[j]
            elif min>d[j]:
                min=d[j]
    l_min.append(min)

f2.write(str(l_min))
f.close()
f2.close()
