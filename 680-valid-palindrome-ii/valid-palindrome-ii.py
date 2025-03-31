class Solution:
    def validPalindrome(self, s: str) -> bool:
      def cPal(s,i,j):
        while i<j:
          if s[i] != s[j]:
            return False
          i+=1
          j-=1
        return True  
      i, j = 0, len(s)-1
      while i<j:
        if s[i]!=s[j]:
          return cPal(s,i+1,j) or cPal(s,i,j-1)
        i += 1
        j -= 1
      return True      