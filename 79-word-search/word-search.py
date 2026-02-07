class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS=len(board)
        self.COLS=len(board[0])
        self.b=board
        for r in range(self.ROWS):
          for c in range(self.COLS):
            if self.dfs(r,c,word): return True
        return False
    def dfs(self,r,c,suffix):
      if len(suffix)==0: return True
      if r<0 or r==self.ROWS or c<0 or c==self.COLS or self.b[r][c]!=suffix[0]:
        return False
      self.b[r][c]='#'
      for rO,cO in [(0,1),(1,0),(-1,0),(0,-1)]:
        if self.dfs(r+rO,c+cO,suffix[1:]): return True
      self.b[r][c]=suffix[0]
      return False