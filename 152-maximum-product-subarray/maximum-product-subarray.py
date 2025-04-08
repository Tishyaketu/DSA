class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.memo = {}
        n = len(nums)
        return self.calculate(1,nums[0],n,nums)
    def calculate(self,i,prevProd,n,nums):
        if i>=n: return prevProd
        key = (i, prevProd)
        if key in self.memo: return self.memo[key]
        self.memo[key] = max(self.calculate(i+1,prevProd*nums[i],n,nums),self.calculate(i+1,nums[i],n,nums),prevProd)
        return self.memo[key]