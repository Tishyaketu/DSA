class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cdict = {'{':'}','[':']','(':')'}
        for c in s:
          if c in cdict:
            stack.append(c)
          else:
            if len(stack)==0 or cdict[stack[-1]]!=c: return False
            else: stack.pop()
        return len(stack)==0
