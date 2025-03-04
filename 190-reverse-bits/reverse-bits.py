class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 # this is the result that would be returned initially zero
        power = 31 # this is used to repsresent 32-bit numbers bits starting from 0 to 31
        while n: # to travrse allthe bits of 32-bit input integer
          res += (n&1)<<power # n&1 takes the rightmost bit, <<power left shifts that bit to its corresponding leftmost place
          n = n>>1 # right shift the input by 1 bit to process next bit
          power -= 1 # reduce the power to place next bit in its corresponding place
        return res #return the result