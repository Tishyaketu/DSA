from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        dp = [float('-inf')] * len(nums)
        return self.recursion(nums, 0, float('-inf'), dp)

    def recursion(self, nums: List[int], idx: int, prev: int, dp: List[float]) -> int:
        if idx >= len(nums):
            return 0

        curr = nums[idx]
        left = right = 0
        
        if curr > prev:
            if dp[idx] == float('-inf'):
                dp[idx] = 1 + self.recursion(nums, idx + 1, curr, dp)
            left = dp[idx]

        right = self.recursion(nums, idx + 1, prev, dp)
        return max(left, right)
