class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # start q from '*' set counter to
        # if valid and 'O' push into q, increment counter
        # if '#' then return counter val
        # if q is empty return -1
        m, n = len(grid), len(grid[0])
        q = deque([])
        for i in range(m):
          for j in range(n):
            if grid[i][j]=='*':
              q.append((i,j,0))
              grid[i][j] = 'X'
        while q:
          r, c, s = q.popleft()
          for (x,y) in [(1,0),(-1,0),(0,-1),(0,1)]:
            newr, newc = r+x, c+y
            if newr<0 or newc>=n or newc<0 or newr>=m:
              continue
            if grid[newr][newc]=='O': 
              q.append((newr,newc,s+1))
              grid[newr][newc] = 'X'
            elif grid[newr][newc]=='#': return s+1
        return -1
