class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backTracking(cS,left,right):
          if len(cS)==2*n:
            answer.append("".join(cS))
            return
          if left<n:
            cS.append('(')
            backTracking(cS,left+1,right)
            cS.pop()
          if right<left:
            cS.append(')')
            backTracking(cS,left,right+1)
            cS.pop()
        backTracking([],0,0)
        return answer