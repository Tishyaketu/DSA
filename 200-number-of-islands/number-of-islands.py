class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])
        iCount = 0
        for i in range(rowLength):
          for j in range(colLength):
            if grid[i][j]=="1":
              q = deque([])
              q.append((i,j))
              grid[i][j] = "0"
              iCount+=1
              while q:
                row, col = q.popleft()
                for (x,y) in [(-1,0),(1,0),(0,-1),(0,1)]:
                  nbrRow, nbrCol = row+x, col+y
                  if nbrRow<0 or nbrCol>=colLength or nbrRow>=rowLength or nbrCol<0 or grid[nbrRow][nbrCol]!="1":
                    continue
                  q.append((nbrRow,nbrCol))
                  grid[nbrRow][nbrCol]="0"
        return iCount
