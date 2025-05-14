class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cdict = {}
        n = len(nums)
        for i in range(n):
          num = nums[i]
          if num in cdict: return num
          cdict[num] = 1