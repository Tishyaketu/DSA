class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for s,d,pr in flights:
          adj[s].append((d,pr))
        stops = 0
        q = deque([(src,0)])
        cost = [inf] * n
        while stops<=k and q:
          sz = len(q)
          for _ in range(sz):
            node, price = q.popleft()
            for nbr, baseprice in adj[node]:
              if price+baseprice>cost[nbr]: continue
              cost[nbr] = price+baseprice
              q.append((nbr,cost[nbr]))
          stops+=1
        return -1 if cost[dst]==inf else cost[dst]