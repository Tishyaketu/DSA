class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine): return False
        rd = collections.Counter(ransomNote)
        md = collections.Counter(magazine)
        for char, count in rd.items():
          if count > md[char]: return False
        return True