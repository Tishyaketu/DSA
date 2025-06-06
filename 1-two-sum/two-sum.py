class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxDict = {}
        for i in range(len(nums)):
          c = target - nums[i]
          if c in idxDict: return [idxDict[c],i]
          idxDict[nums[i]] = i