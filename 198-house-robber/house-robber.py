class Solution:
    def rob(self, nums: List[int]) -> int:
      memo = {}
      return self.robFrom(0,nums,memo)
    def robFrom(self,start,nums,memo):
      if start>=len(nums): return 0
      if start in memo: return memo[start]
      memo[start] = max(nums[start]+self.robFrom(start+2,nums,memo),self.robFrom(start+1,nums,memo))
      return memo[start]
        