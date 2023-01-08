from collections import deque
class Solution(object):
    def shortestPathLength(self, graph):
        n = len(graph)
        all_mask = (1<<n) - 1
        q = deque()
        viz = set()

        for i in range(n):
            mask = 1<<i
            viz.add((i, mask))
            q.append((i, 0, mask))

        while len(q) > 0:
            x = q.popleft()
            if x[2] == all_mask:
                return x[1]

            for y in graph[x[0]]:
                mask_y = 1<<y
                mask_xy = x[2] | mask_y
                (nod, cost, mask) = (y, x[1]+1, mask_xy)

                if (y, mask_xy) not in viz:
                    viz.add((y, mask_xy))
                    q.append((nod, cost, mask))

sol = Solution()
print(sol.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))