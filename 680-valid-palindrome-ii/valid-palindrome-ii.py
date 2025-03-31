class Solution:
    def validPalindrome(self, s: str) -> bool:
      i, j = 0, len(s)-1
      while i<j:
        if s[i]!=s[j]:
          return self.cPal(s,i+1,j) or self.cPal(s,i,j-1)
        i += 1
        j -= 1
      return True
    def cPal(self,s,i,j):
      while i<j:
        if s[i] != s[j]:
          return False
        i+=1
        j-=1
      return True        
