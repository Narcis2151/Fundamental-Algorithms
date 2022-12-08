import heapq as hq

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        graf = {i: [] for i in range(0, n)}
        
        for e, w in zip(edges, succProb):
            v1, v2 = e
            graf[v1].append((w, v2))
            graf[v2].append((w, v1))
        
        max_heap = [(-1, start)]
        vizitat = set()

        
        while max_heap:
            prob, v = hq.heappop(max_heap)            
            
            if v in vizitat: 
                continue
            if v == end: 
                return -prob    
            
            vizitat.add(v)
            
            for prob_vecin, vecin in graf[v]:
                if vecin not in vizitat:
                    hq.heappush(max_heap, (prob * prob_vecin, vecin))
        
        return 0.0

