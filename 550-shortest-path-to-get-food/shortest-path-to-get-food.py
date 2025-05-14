class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([])
        for i in range(m):
          for j in range(n):
            if grid[i][j]=='*':
              q.append((i,j,0))
              grid[i][j]='X'
        while q:
          r, c, s = q.popleft()
          for (x,y) in [(0,1),(1,0),(0,-1),(-1,0)]:
            newr, newc = r+x, c+y
            if newr<0 or newc>=n or newc<0 or newr>=m or grid[newr][newc]=='X': continue
            if grid[newr][newc]=='#': return s+1
            grid[newr][newc]='X'
            q.append((newr,newc,s+1))
        return -1