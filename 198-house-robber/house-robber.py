class Solution:
    def __init__(self):
      self.memo = {}
    def rob(self, nums: List[int]) -> int:
        # find max value, add to res
        # keep on adding non-adajacent left and right nbrs to res
        self.memo = {}
        return self.robFrom(0,nums)
    def robFrom(self,i,nums):
      if i>=len(nums): return 0
      if i in self.memo: return self.memo[i]
      ans = max(self.robFrom(i+1,nums),nums[i]+self.robFrom(i+2,nums))
      self.memo[i] = ans
      return ans