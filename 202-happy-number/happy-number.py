class Solution:
    def isHappy(self, n: int) -> bool:
        def gn(num):
          ts = 0
          while num>0:
            num, d = divmod(num,10)
            ts+=d**2
          return ts
        sr = n
        fr = gn(n)
        while fr!=1 and sr!=fr:
          sr = gn(sr)
          fr = gn(gn(fr))
        return fr==1