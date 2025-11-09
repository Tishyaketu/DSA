class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      count = 0
      sum_val = 0
      map_dict = {0: 1}
      for i in range(len(nums)):
        sum_val += nums[i]
        if sum_val - k in map_dict:
          count += map_dict[sum_val - k]
        map_dict[sum_val] = map_dict.get(sum_val, 0) + 1
      return count