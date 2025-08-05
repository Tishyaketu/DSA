class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idict = {}
        for i in range(len(nums)):
          idict[nums[i]] = i
        for i in range(len(nums)):
          cmplmnt = target - nums[i]
          if cmplmnt in idict and idict[cmplmnt]!=i: return [idict[cmplmnt],i]