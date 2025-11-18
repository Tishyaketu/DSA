class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumulativeSum = maxSum = nums[0]
        for num in nums[1:]:
          cumulativeSum = max(num,num+cumulativeSum) #only choose maximum value of the current element or the cumulative sum till the element
          maxSum = max(cumulativeSum,maxSum) # only choose the global maximum not only the cumulative value
        return maxSum