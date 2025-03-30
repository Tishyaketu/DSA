class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w_l = len(word)
        a_l = len(abbr)
        w_i, a_i = 0, 0
        while w_i<w_l and a_i<a_l:
          if word[w_i]==abbr[a_i]:
            w_i += 1
            a_i += 1
            continue
          if not abbr[a_i].isdigit():
            return False
          n_s_i = a_i
          while a_i<a_l and abbr[a_i].isdigit():
            a_i += 1
          n_s = abbr[n_s_i:a_i]
          if n_s[0]=='0':
            return False
          w_i += int(n_s)
        return w_i==w_l and a_i==a_l
