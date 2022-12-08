"""
Rezolvarea problemei Course Scheduling 2
Returneaza un array gol daca nu se poate crea un mod de organizarea evenimentelor
Sau un mod posibil daca acest lucru se poate
Bazat pe sortarea topologica folosind DFS + o functie de detectare a circuitelor

"""
class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        #Construirea grafului, a stivei si a listei ce va contine sortarea
        sol=[]
        viz = [0 for i in range(numCourses)]
        graf = [[] for i in range(numCourses)]
        st = []
        
        for arc in prerequisites:
            u = arc[0]
            v = arc[1]
            graf[v].append(u)
        
        #Functia de parcurgere DFS
        def DFS(i):
            viz[i] = 1
            for x in range(len(graf[i])):
                if viz[graf[i][x]]==0:
                    DFS(graf[i][x])
            st.append(i)
        
        
        #Functia de detectare a circuitelor
        def cycle_det():
            ind = 0
            pozitii = dict()
            pozitii[st[-1]] = ind

            while len(st)>0:
                pozitii[st[-1]] = ind
                sol.append(st[-1])
                ind = ind + 1
                st.pop()
            #print(pozitii)
            for i in range(numCourses):
                for j in graf[i]:
                    x1 = pozitii[i]
                    x2 = pozitii[j]

                    if x1 > x2:
                        return True
            return False

        #DFS pentru fiecare componenta conexa
        for i in range(numCourses):
            if viz[i] == 0:
                DFS(i)

        if cycle_det() == True:
            return []
        else:
            return sol

x = Solution()     
print(x.findOrder(4,[[1,0],[2,0],[2,1],[0,2],[3,2]]))