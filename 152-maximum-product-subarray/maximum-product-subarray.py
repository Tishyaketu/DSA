class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.memo = {}
        return self.dfs(1, nums[0],nums)
    def dfs(self, i, previousProduct,nums):
            key = (i, previousProduct)
            if (key in self.memo):
                return self.memo[key]
            if (i >= len(nums)):
                return previousProduct
			# 3 choices, Include the current number in the product, start a new product, or end the product
            ans = max(self.dfs(i + 1, previousProduct * nums[i],nums), self.dfs(i + 1, nums[i],nums), previousProduct)
            self.memo[key] = ans
            return ans