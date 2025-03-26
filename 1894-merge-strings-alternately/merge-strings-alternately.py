class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        ms = ''
        while i<len(word1) and j<len(word2):
          ms+=word1[i]
          i+=1
          ms+=word2[j]
          j+=1
        if i<len(word1):
          ms+=word1[i:]
        else:
          ms+=word2[j:]
        return ms