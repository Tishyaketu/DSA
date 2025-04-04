class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rowsets = [set() for _ in range(n)]
        colsets = [set() for _ in range(n)]
        boxsets = [set() for _ in range(n)]
        for i in range(n):
          for j in range(n):
            element = board[i][j]
            if element!='.':
              if element in rowsets[i]:
                return False
              rowsets[i].add(element)
              if element in colsets[j]:
                return False
              colsets[j].add(element)
              boxNum = ((i//3)*3) + j//3
              if element in boxsets[boxNum]:
                return False
              boxsets[boxNum].add(element)
        return True