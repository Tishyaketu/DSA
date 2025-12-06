class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2: return False
        parDict = {'{':'}','[':']','(':')'}
        stack = []
        for c in s:
          if c in parDict: stack.append(c)
          else: 
            if len(stack)==0: return False
            elif c==parDict[stack[-1]]: stack.pop()
            else: return False
        return len(stack)==0