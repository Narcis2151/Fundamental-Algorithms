class Solution:
    def validArrangement(self, pairs):
        from collections import defaultdict
        graf = defaultdict(list)
        gout = defaultdict(int)
        gin = defaultdict(int)
        for x, y in pairs:
            graf[x].append(y)
            gout[x]+=1
            gin[y]+=1

        s = pairs[0][0]
        for x in gout:
            if gout[x] == gin[x] +1:
                s = x
                break            
                
        rasp = []
        def euler(x):
            while graf[x]:
                euler(graf[x].pop())    
            rasp.append(x)

        euler(s)
        rasp.reverse()
        r = [[rasp[i], rasp[i+1]] for i in range(len(rasp)-1)]
        return r
sol = Solution()
print(sol.validArrangement([[5,1],[4,5],[11,9],[9,4]])) 
