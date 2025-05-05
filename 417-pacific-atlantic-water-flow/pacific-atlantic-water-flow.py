class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        numr, numc = len(heights), len(heights[0])
        pq = deque([])
        aq = deque([])
        for i in range(numr):
          pq.append((i,0))
          aq.append((i,numc-1))
        for j in range(numc):
          pq.append((0,j))
          aq.append((numr-1,j))
        def bfs(q):
          reachable = set()
          while q:
            r, c = q.popleft()
            reachable.add((r,c))
            for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
              newr, newc = r+x, c+y
              if newr<0 or newc>=numc or newc<0 or newr>=numr:
                continue
              if (newr,newc) in reachable:
                continue
              if heights[newr][newc]<heights[r][c]:
                continue
              q.append((newr,newc))
          return reachable
        pr = bfs(pq)
        ar = bfs(aq)
        return list(pr.intersection(ar))