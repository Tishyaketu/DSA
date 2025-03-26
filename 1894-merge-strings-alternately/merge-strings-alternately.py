class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        m, n  = len(word1), len(word2)
        ms = ''
        while i<m or j<n:
          if i<m:
            ms+=word1[i]
            i+=1
          if j<n:
            ms+=word2[j]
            j+=1
        return ms