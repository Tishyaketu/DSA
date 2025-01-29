class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        lensum = 0
        for i in range(n+1):
          lensum+=i
        numsum = 0
        for i in range(len(nums)):
          numsum+=nums[i]
        return lensum-numsum