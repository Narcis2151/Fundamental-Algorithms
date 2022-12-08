fin = open("disjoint.in", "r")
fout = open("disjoint.out", "w")

nm = fin.readline().split()
n, m = int(nm[0]), int(nm[1])
tata = {}
h = {}
for i in range(n):
    tata[i+1] = 0
    h[i+1] = 0

def Reprez(u):
    if tata[u] == 0:
        return u
    tata[u] = Reprez(tata[u])
    return tata[u]

def Reuneste(u, v):
    ru = Reprez(u)
    rv = Reprez(v)
    if h[ru] > h[rv]:
        tata[rv] = ru
    else:
        tata[ru] = rv
        if h[ru] == h[rv]:
            h[rv] = h[rv] + 1

for i in range(m):
    cuv = fin.readline().split()
    #print(cuv)
    c, u, v = int(cuv[0]), int(cuv[1]), int(cuv[2])
    #print(c,u,v)
    if c == 2:
        if Reprez(u) == Reprez(v):
            fout.write("DA\n")
        else:
            fout.write("NU\n")
    else:
        if Reprez(u) != Reprez(v):
            Reuneste(u,v)
            
#print(tata,h)
fin.close()
fout.close()