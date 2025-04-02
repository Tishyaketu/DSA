class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = set()
        res = 0
        for c in s:
          if c not in counts:
            counts.add(c)
          else:
            counts.remove(c)
            res+=2
        if counts: res+=1
        return res