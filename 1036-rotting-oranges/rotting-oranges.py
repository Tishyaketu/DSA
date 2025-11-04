class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        a, b, c, d, e = 0, -1, deque([]), len(grid), len(grid[0])
        for f in range(d):
          for g in range(e):
            if grid[f][g]==1: a += 1
            elif grid[f][g]==2: 
              c.append((f,g))
        if a == 0: return 0
        c.append((-1,-1))
        while c:
          h, i = c.popleft()
          if h == -1:
            b += 1
            if c:
              c.append((-1,-1))
          else:
            for j,k in [(0,1),(1,0),(0,-1),(-1,0)]:
              l, m = h+j, i+k
              if l>=0 and l<=d-1 and m>=0 and m<=e-1:
                if grid[l][m]==1:
                  grid[l][m] = 2
                  a -= 1
                  c.append((l,m))
        return b if a==0 else -1