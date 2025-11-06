class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        a, b, c, d, e = 0, -1, len(grid), len(grid[0]), deque([]) # a=fresh, b=lvl, e=q
        for f in range(c):
          for i in range(d):
            if grid[f][i] == 1: a += 1
            elif grid[f][i] == 2: 
              e.append((f,i))
        if a == 0: return 0
        e.append((-1,-1))
        while e:
          j, k = e.popleft() # j= row, k=col         
          if j == -1: 
            b += 1
            if e: e.append((-1,-1))
          else:
            for l, m in [(1,0),(-1,0),(0,1),(0,-1)]:
              n, o = j + l, k + m #n = newr, o = newc
              if 0<= n <=c-1 and 0<= o <=d-1 and grid[n][o] == 1:
                grid[n][o] = 2
                a -= 1
                e.append((n, o))
        return b if a == 0 else -1

