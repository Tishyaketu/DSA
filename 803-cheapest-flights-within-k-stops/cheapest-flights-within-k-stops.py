class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for flight in flights:
          adj[flight[0]].append((flight[1],flight[2]))
        q = deque([(src,0)])
        stops = 0
        minCost = [inf for _ in range(n)]
        while stops<=k and q:
          sz = len(q)
          for _ in range(sz):
            node, cumulativeCost = q.popleft()
            for nbr,baseCost in adj[node]:
              if cumulativeCost+baseCost>minCost[nbr]: continue
              minCost[nbr] = cumulativeCost+baseCost
              q.append((nbr,minCost[nbr]))
          stops+=1
        return -1 if minCost[dst]==inf else minCost[dst]