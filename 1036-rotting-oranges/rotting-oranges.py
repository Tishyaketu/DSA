class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, lvl, m, n, q = 0, -1, len(grid), len(grid[0]), deque([])
        for i in range(m):
          for j in range(n):
            if grid[i][j] == 1: fresh += 1
            elif grid[i][j] == 2: q.append((i,j))
        if fresh == 0: return 0
        q.append((-1,-1))
        while q:
          r, c = q.popleft()
          if r == -1:
            lvl += 1
            if q:
              q.append((-1,-1))
          else:
            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
              newr, newc = r+x, c+y
              if 0<=newr<=m-1 and 0<=newc<=n-1 and grid[newr][newc]==1:
                grid[newr][newc]=2
                fresh -= 1
                q.append((newr,newc))
        return lvl if fresh==0 else -1