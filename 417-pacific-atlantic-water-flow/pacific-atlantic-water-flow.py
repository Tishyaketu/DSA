class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pq = deque([])
        aq = deque([])
        nr, nc = len(heights), len(heights[0])
        for i in range(nr):
          pq.append((i,0))
          aq.append((i,nc-1))
        for j in range(nc):
          pq.append((0,j))
          aq.append((nr-1,j))
        def bfs(q):
          reachable = set()
          while q:
            r, c = q.popleft()
            reachable.add((r,c))
            for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
              newr, newc = r+x, c+y
              if newr<0 or newc>=nc or newc<0 or newr>=nr:
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