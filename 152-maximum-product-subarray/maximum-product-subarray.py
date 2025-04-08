class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.memo = {}
        return self.recurse(1,nums[0],nums)
    def recurse(self,i,prevProd,nums):
        if i>=len(nums): return prevProd
        key = (i, prevProd)
        if key in self.memo: return self.memo[key]
        self.memo[key] = max(self.recurse(i+1,prevProd*nums[i],nums),self.recurse(i+1,nums[i],nums),prevProd)
        return self.memo[key]