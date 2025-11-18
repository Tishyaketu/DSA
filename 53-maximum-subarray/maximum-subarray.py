class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumulativeSum = maxSum = nums[0]
        for num in nums[1:]:
          cumulativeSum = max(num,num+cumulativeSum)
          maxSum = max(cumulativeSum,maxSum)
        return maxSum