class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c, sv, md, n = 0, 0, {0:1}, len(nums)
        for i in range(n):
          sv += nums[i]
          if sv - k in md: c += md[sv - k]
          md[sv] = md.get(sv,0) + 1
        return c