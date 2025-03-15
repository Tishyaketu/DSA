class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fw = strs[0]
        for i in range(len(fw)):
          for j in range(1,len(strs)):
            if i==len(strs[j]) or strs[0][i]!=strs[j][i]:
              return fw[:i]
        return fw