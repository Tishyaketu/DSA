class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n==1: return nums[0]
        for i in range(n):
          if nums[i] in memo: 
            memo[nums[i]]+=1
            if memo[nums[i]]>(n//2): return nums[i]
          else: memo[nums[i]] = 1
