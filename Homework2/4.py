import heapq as hq
from math import inf
class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        graf = {i: [] for i in range(0, n)}
        
        for e, w in zip(edges, succProb):
            u, v = e
            graf[u].append((w, v))
            graf[v].append((w, u))
        
        max_heap = [(1, start)]
        vizitat = [0] * n
        d = [-200000000 for i in range(n)]

        while max_heap:

            prob, u = hq.heappop(max_heap)            
            prob = abs(prob)

            if vizitat[u] !=0:
                continue

            if u == end: 
                return prob    
            
            vizitat[u] += 1
            
            for prob_v, v in graf[u]:
                prob_v *= prob
                if d[v] < prob_v:
                    d[v] = prob_v       
                    hq.heappush(max_heap, (-prob_v, v))        
        return 0.0

sol = Solution()
print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))
