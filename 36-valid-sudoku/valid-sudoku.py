class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rowsets = [set() for _ in range(N)]
        colsets = [set() for _ in range(N)]
        boxsets = [set() for _ in range(N)]
        for i in range(N):
          for j in range(N):
            element = board[i][j]
            if element!='.':
              if element in rowsets[i]:
                return False
              rowsets[i].add(element)
              if element in colsets[j]:
                return False
              colsets[j].add(element)
              boxNum = ((i//3)*3)+j//3
              if element in boxsets[boxNum]:
                return False
              boxsets[boxNum].add(element)
              
        return True 