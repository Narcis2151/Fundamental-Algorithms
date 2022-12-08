"""
Program pentru a determina daca putem imparti grupul de n persoane
Astfel incat persoanele care se displac sa fie impartite in grupuri diferite
Ideea: Parcurgem BF toate componentele conexe si "coloram" orice vecin j nevizitat al varfului curent i cu
culoarea diferita de cea a lui i
In aceeasi clasa Solution am implementat si subpunctul b al problemei:
Afisarea celor 2 grupe de persoane, in cazul in care impartirea este posibila
Numele acestei functii este possibleBipartition2
Complexitate identica cu cea pentru parcurgerea BFS -> O(v+e)
"""

class Solution:
    def possibleBipartition(self, n, dislikes):
        from collections import deque
        viz = [0 for i in range(n)]
        graf = [[] for i in range(n)]

        #memoram graful prin intermediul unei liste de adiacenta -> parcurgerea va fi mai eficienta
        for muchie in dislikes:
            u = muchie[0] - 1
            v = muchie[1] - 1
            graf[u].append(v)
            graf[v].append(u)

        #print(graf)

        #Functia pentru parcurgerea BFS
        def BFS(i):
            q = deque([])
            viz[i] = 1
            q.append(i)

            while len(q)>0:
                u = q.popleft()
                for k in range(len(graf[u])):
                    #print(viz)
                    #print(u)

                    v = graf[u][k]
                    if viz[v] == 0:
                        q.append(v)

                        #Colorarea vecinilor lui u
                        if viz[u] == 1:
                            viz[v] = 2
                        else:
                            viz[v] = 1

                    #Testam extremitatile
                    if viz[v] == viz[u]:
                        return 0
            return 1

        #Parcurgem BF fiecare componenta conexa a grafului
        for i in range(0, n):
            if viz[i] == 0:
                if BFS(i) == 0:
                    return False
        return True   


    def possibleBipartition2(self, n: int, dislikes: list[list[int]]) -> list[list[int]]:
        from collections import deque
        viz = [0 for i in range(n)]
        graf = [[] for i in range(n)]
        #Adaugam o lista ce va contine impartirea in cele 2 grupuri
        lf=[[] for i in range(2)]

        #memoram graful prin intermediul unei liste de adiacenta -> parcurgerea va fi mai eficienta
        for muchie in dislikes:
            u = muchie[0] - 1
            v = muchie[1] - 1
            graf[u].append(v)
            graf[v].append(u)

        #print(graf)

        #Functia pentru parcurgerea BFS
        def BFS(i):
            q = deque([])
            viz[i] = 1
            q.append(i)

            while len(q)>0:
                u = q.popleft()
                for k in range(len(graf[u])):
                    #print(viz)
                    #print(u)

                    v = graf[u][k]
                    if viz[v] == 0:
                        q.append(v)

                        #Colorarea vecinilor lui u
                        if viz[u] == 1:
                            viz[v] = 2
                        else:
                            viz[v] = 1

                    #Testam extremitatile
                    if viz[v] == viz[u]:
                        return 0
            return 1

        #Parcurgem BF fiecare componenta conexa a grafului
        for i in range(0, n):
            if viz[i] == 0:
                if BFS(i) == 0:
                    return lf
        #Daca impartirea este posibila, persoanele sunt puse in cele 2 grupuri in functie de culoarea asociata
        #In timpul parcurgerii BF
        #Daca nu este posibila, este intoarsa o lista vida

        for i in range(len(viz)):
            if viz[i] == 1:
                lf[0].append(i+1)
            else:
                lf[1].append(i+1)
        
        return lf

#x = Solution()
#print(x.possibleBipartition(5,[[1,2],[2,3],[3,4],[4,5],[1,5]]))
#print(x.possibleBipartition2(4,[[1,2],[1,3],[2,4]]))