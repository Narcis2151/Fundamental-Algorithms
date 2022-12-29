fin = open("cuvinte.in", "r")

def Levenshtein(a, b):
    if len(b)==0:
        return len(a)
    elif len(a)==0:
        return len(b)
    elif a[0]==b[0]:
        return Levenshtein(a[1:], b[1:])
    else:
        return 1+ min(Levenshtein(a[1:], b),
                      Levenshtein(a, b[1:]),
                      Levenshtein(a[1:], b[1:]))


cuvinte=fin.read().split()
print(cuvinte)
k=int(input())
n=10
muchii=[]
tata=[0]*(n)
h=[0]*(n)

for i in range(n-1):
    for j in range(i+1, n):
        d=Levenshtein(cuvinte[i], cuvinte[j])
        muchii.append((i,j,d))

def Reprez(u):
    if tata[u] ==0:
        return u
    tata[u]=Reprez(tata[u])
    return tata[u]


def Reuneste(u,v):
    ru=Reprez(u)
    rv=Reprez(v)

    if h[ru]>h[rv]:
        tata[rv]=ru
    else:
        tata[ru]=rv
        if h[ru]==h[rv]:
            h[rv]=h[rv]+1

muchii=sorted(muchii, key=(lambda t: t[2]))

nrmsel=0 
cost=0
arbore=[]
i=0
while i< len(muchii):
   m=muchii[i]
   if Reprez(m[0]) != Reprez(m[1]):
        arbore.append((m[0], m[1]))
        Reuneste(m[0], m[1])
        cost=cost+m[2]
        nrmsel=nrmsel+1

        if nrmsel == n - k:  
            break
   i+=1 


for i in range(n):
    if tata[i]==0:
        print(cuvinte[i], end=" ")
        for j in range(n):
            if tata[j]==i:
                print(cuvinte[j], end=" ")
        print()
print(muchii[i+1][2])

fin.close()