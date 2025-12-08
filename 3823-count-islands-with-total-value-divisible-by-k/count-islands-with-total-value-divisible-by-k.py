class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n, q, count, islands, water, land = len(grid), len(grid[0]), deque([]), 0, [], set(), set()
        for i in range(m):
          for j in range(n):
            if (i,j) not in water and (i,j) not in land:
              if grid[i][j]==0: water.add((i,j))
              else:
                land.add((i,j))
                q.append((i,j))
                island = []
                island.append(grid[i][j])
                while q:
                  row, col = q.popleft()
                  for (x,y) in [(0,1),(1,0),(0,-1),(-1,0)]:
                    new_row, new_col = row + x, col + y
                    if 0<=(new_row)<=m-1 and 0<=new_col<=n-1 and (new_row,new_col) not in water and (new_row,new_col) not in land:
                      if grid[new_row][new_col]!=0:
                        land.add((new_row,new_col))
                        island.append(grid[new_row][new_col])
                        q.append((new_row,new_col))
                      else: water.add((new_row,new_col))
                islands.append(island)
        for island in islands:
          total = 0
          for land in island:
            total += land
          if total%k==0: count += 1
        return count
